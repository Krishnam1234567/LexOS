import asyncio
import itertools
from typing import List, Dict, Any, Tuple
from google import genai
from google.genai import types

from app.config import settings

class KeyPool:
    """Thread-safe round-robin API key selector."""
    def __init__(self, keys: List[str]):
        self.keys = keys
        if not self.keys:
            raise ValueError("No valid API keys found in configuration.")
        self._iterator = itertools.cycle(self.keys)
        self._lock = asyncio.Lock()

    async def get_key(self) -> str:
        async with self._lock:
            return next(self._iterator)

# Initialize global key pool
try:
    key_pool = KeyPool(settings.api_keys)
except ValueError:
    key_pool = None

async def generate_with_key(contents: List[types.Content], config: types.GenerateContentConfig) -> Tuple[types.GenerateContentResponse, str]:
    """Helper to run a Gemini call using a round-robin key, with auto-retry on 429."""
    if not key_pool:
        raise ValueError("API Key pool is empty.")
    
    max_retries = 5
    last_error = None
    
    for attempt in range(max_retries):
        api_key = await key_pool.get_key()
        client = genai.Client(api_key=api_key)
        try:
            # Using flash model for fast execution
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=contents,
                config=config
            )
            return response, api_key
        except Exception as e:
            last_error = e
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                print(f"[KeyPool] Key ...{api_key[-4:]} exhausted quota. Auto-rotating to next key...")
                continue
            raise # If it's another error, raise immediately
            
    # If all retries exhausted
    raise last_error

async def run_actor(actor_id: int, system_instruction: str, history: List[types.Content], user_message: str, tools: List[types.Tool]) -> Dict[str, Any]:
    """Runs a single actor to generate a response and potential tool calls."""
    actor_history = [
        types.Content(role="user", parts=[types.Part.from_text(text=f"[System Instruction]: {system_instruction}")])
    ] + history + [
        types.Content(role="user", parts=[types.Part.from_text(text=user_message)])
    ]
    
    config = types.GenerateContentConfig(tools=tools, temperature=0.7) # Slight temp for variance between actors
    response, key_used = await generate_with_key(actor_history, config)
    
    return {
        "id": actor_id,
        "response": response,
        "key_used": key_used
    }

async def run_critic(critic_id: int, original_prompt: str, context: str, response_text: str, function_calls: List[types.FunctionCall]) -> Dict[str, Any]:
    """Runs a critic to evaluate a generated response for hallucination and accuracy."""
    
    func_call_str = "\n".join([f"- {call.name}({call.args})" for call in function_calls]) if function_calls else "None"
    
    if critic_id == 1:
        # Critic 1: Fact Checker (focuses on DB context)
        instruction = "You are a Fact Checker Critic. Your job is to ensure the response perfectly aligns with the provided Database Context. Return PASS or FAIL, followed by a brief reasoning."
        prompt = (
            f"User Prompt: {original_prompt}\n\n"
            f"Database Context:\n{context}\n\n"
            f"Model Response: {response_text}\n"
            f"Model Tool Calls: {func_call_str}\n\n"
            "Evaluate if the model made any claims that contradict the Database Context or hallucinates facts not present. "
            "Reply strictly with 'PASS' or 'FAIL: [reason]'"
        )
    else:
        # Critic 2: Hallucination & Tool Misuse Detector
        instruction = "You are a Hallucination Detector Critic. Your job is to catch fabricated entities, invented statistics, or inappropriate tool usage. Return PASS or FAIL, followed by a brief reasoning."
        prompt = (
            f"User Prompt: {original_prompt}\n\n"
            f"Database Context:\n{context}\n\n"
            f"Model Response: {response_text}\n"
            f"Model Tool Calls: {func_call_str}\n\n"
            "Evaluate if the model hallucinated or misused tools (e.g., calling 'add_legal_entity' when not explicitly requested). "
            "Reply strictly with 'PASS' or 'FAIL: [reason]'"
        )

    contents = [
        types.Content(role="user", parts=[types.Part.from_text(text=f"[System Instruction]: {instruction}")]),
        types.Content(role="user", parts=[types.Part.from_text(text=prompt)])
    ]
    
    config = types.GenerateContentConfig(temperature=0.0) # Critics must be deterministic
    response, key_used = await generate_with_key(contents, config)
    
    result_text = response.text.strip()
    passed = result_text.startswith("PASS")
    
    return {
        "id": critic_id,
        "passed": passed,
        "reasoning": result_text,
        "key_used": key_used
    }

async def run_aggregator(actor1_res: Dict[str, Any], actor2_res: Dict[str, Any]) -> Dict[str, Any]:
    """Selects the best response between two actors. For simplicity and speed, we pick the one with function calls, or the shorter one."""
    
    has_funcs1 = bool(actor1_res["response"].function_calls)
    has_funcs2 = bool(actor2_res["response"].function_calls)
    
    if has_funcs1 and not has_funcs2:
        return actor1_res
    if has_funcs2 and not has_funcs1:
        return actor2_res
        
    len1 = len(actor1_res["response"].text or "")
    len2 = len(actor2_res["response"].text or "")
    
    # Prefer conciseness
    return actor1_res if len1 <= len2 else actor2_res

async def actor_critic_pipeline(system_instruction: str, context_str: str, history: List[types.Content], user_message: str, tools: List[types.Tool]) -> Tuple[types.GenerateContentResponse, str]:
    """
    Executes the full Actor-Critic pipeline:
    1. Run 2 Actors concurrently
    2. Aggregate (pick best)
    3. Run 2 Critics concurrently
    4. Retry once if failed
    """
    if not key_pool:
        raise ValueError("API Key pool not initialized.")

    print("[Actor-Critic] Starting pipeline...")
    
    # 1. Run Actors in parallel
    actor1_task = run_actor(1, system_instruction, history, user_message, tools)
    actor2_task = run_actor(2, system_instruction, history, user_message, tools)
    
    actor1_res, actor2_res = await asyncio.gather(actor1_task, actor2_task)
    
    # 2. Aggregate
    best_actor = await run_aggregator(actor1_res, actor2_res)
    best_response = best_actor["response"]
    best_text = best_response.text or ""
    function_calls = best_response.function_calls or []
    
    print(f"[Actor-Critic] Selected Actor {best_actor['id']} (Used key: ...{best_actor['key_used'][-4:]})")
    
    # 3. Run Critics in parallel
    critic1_task = run_critic(1, user_message, context_str, best_text, function_calls)
    critic2_task = run_critic(2, user_message, context_str, best_text, function_calls)
    
    c1_res, c2_res = await asyncio.gather(critic1_task, critic2_task)
    
    print(f"[Actor-Critic] Critic 1: {'PASS' if c1_res['passed'] else 'FAIL'} (Key: ...{c1_res['key_used'][-4:]})")
    print(f"[Actor-Critic] Critic 2: {'PASS' if c2_res['passed'] else 'FAIL'} (Key: ...{c2_res['key_used'][-4:]})")
    
    # 4. Evaluate Critics
    if c1_res["passed"] and c2_res["passed"]:
        print("[Actor-Critic] Both critics passed. Returning response.")
        return best_response, ""
        
    # 5. Retry path (if failed)
    print("[Actor-Critic] Critics failed. Retrying with feedback...")
    feedback = "PREVIOUS ATTEMPT FAILED VALIDATION.\n"
    if not c1_res["passed"]:
        feedback += f"Fact Checker Feedback: {c1_res['reasoning']}\n"
    if not c2_res["passed"]:
        feedback += f"Hallucination Feedback: {c2_res['reasoning']}\n"
        
    retry_instruction = f"{system_instruction}\n\n{feedback}\nYou MUST correct these issues in your new response."
    
    # Run a single actor for retry
    retry_actor = await run_actor(3, retry_instruction, history, user_message, tools)
    print(f"[Actor-Critic] Retry complete (Key: ...{retry_actor['key_used'][-4:]})")
    
    return retry_actor["response"], feedback
