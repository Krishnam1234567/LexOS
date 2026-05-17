from fastapi import APIRouter, HTTPException
from app.schemas.agents import AgentsResponse
from app.schemas.chat import ChatRequest, ChatResponse
from app.config import settings
from google import genai

router = APIRouter(prefix="/agents", tags=["AI Agents"])

@router.get("/", response_model=AgentsResponse)
async def get_agents_data():
    """Get AI Agents activity and approval queues."""
    return {
        "active_agents": 4,
        "total_agents": 6,
        "tasks_completed_month": 4934,
        "pending_approval": 2,
        "agents": [
            {"id": 1, "name": "Compliance Agent", "description": "Monitors regulatory changes and ensures continuous compliance", "status": "active", "tasksCompleted": 1247, "lastAction": "2 mins ago", "confidence": 98},
            {"id": 2, "name": "Filing Agent", "description": "Automates legal filings and deadline management", "status": "active", "tasksCompleted": 456, "lastAction": "15 mins ago", "confidence": 95},
            {"id": 3, "name": "Contract Agent", "description": "Reviews, analyzes, and manages contract lifecycle", "status": "active", "tasksCompleted": 2341, "lastAction": "5 mins ago", "confidence": 97},
            {"id": 4, "name": "Governance Agent", "description": "Manages board resolutions and corporate governance", "status": "idle", "tasksCompleted": 89, "lastAction": "2 hours ago", "confidence": 92},
            {"id": 5, "name": "Expansion Agent", "description": "Analyzes global expansion legal requirements", "status": "active", "tasksCompleted": 234, "lastAction": "30 mins ago", "confidence": 94},
            {"id": 6, "name": "Litigation Agent", "description": "Predicts litigation risk and monitors legal disputes", "status": "idle", "tasksCompleted": 567, "lastAction": "1 hour ago", "confidence": 96},
        ],
        "recent_activity": [
            {"agent": "Contract Agent", "action": "Identified 3 high-risk clauses in MSA-2024-089", "timestamp": "2 mins ago", "type": "alert"},
            {"agent": "Compliance Agent", "action": "Completed GDPR compliance check for Q2", "timestamp": "15 mins ago", "type": "success"},
            {"agent": "Filing Agent", "action": "Filed Delaware annual report", "timestamp": "1 hour ago", "type": "success"},
            {"agent": "Expansion Agent", "action": "Generated UK expansion compliance report", "timestamp": "2 hours ago", "type": "info"},
        ],
        "approval_queue": [
            {"id": 1, "agent": "Contract Agent", "task": "Auto-renew AWS Enterprise Agreement", "reasoning": "Contract terms remain favorable. Price locked until 2027. No major changes in service requirements.", "confidence": 98, "impact": "Medium"},
            {"id": 2, "agent": "Filing Agent", "task": "Submit CCPA annual compliance report", "reasoning": "All required documentation collected. Compliance verified at 96%. Ready for submission.", "confidence": 95, "impact": "High"},
        ]
    }

@router.post("/chat", response_model=ChatResponse)
async def chat_with_agent(req: ChatRequest):
    """Chat with the Legal AI Copilot powered by Gemini."""
    if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == "your_gemini_api_key_here":
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY is not configured in backend/.env")
    
    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        # We can pass context here to make it act like a legal assistant
        system_instruction = "You are LexOS, an Enterprise AI Legal Operating System assistant. You help users analyze contracts, check compliance, predict litigation risk, and navigate legal operations. Be concise, professional, and helpful."
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"System Instruction: {system_instruction}\n\nUser: {req.message}",
        )
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
