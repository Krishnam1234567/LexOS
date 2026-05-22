"""
LexOS — AI Legal Agents API
Autonomous agent management with real database persistence.
"""
from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.config import settings
from app.db.sqlite_db import get_conn, add_audit_log
from google import genai
import json
from datetime import datetime

router = APIRouter(prefix="/agents", tags=["AI Agents"])


@router.get("/")
async def get_agents_data():
    """Get AI Agents from database."""
    conn = get_conn()
    agents = [dict(r) for r in conn.execute("SELECT * FROM agents ORDER BY id").fetchall()]
    activity = [dict(r) for r in conn.execute("SELECT * FROM recent_activity ORDER BY id DESC LIMIT 15").fetchall()]
    queue = [dict(r) for r in conn.execute("SELECT * FROM approval_queue ORDER BY id").fetchall()]
    conn.close()

    active = sum(1 for a in agents if a["status"] == "active")
    total_tasks = sum(a["tasksCompleted"] for a in agents)

    return {
        "active_agents": active,
        "total_agents": len(agents),
        "tasks_completed_month": total_tasks,
        "pending_approval": len(queue),
        "agents": agents,
        "recent_activity": activity,
        "approval_queue": queue,
    }


@router.post("/approve/{item_id}")
async def approve_task(item_id: int):
    """Approve an agent task — removes from queue, logs success, increments agent tasks."""
    conn = get_conn()
    item = conn.execute("SELECT * FROM approval_queue WHERE id=?", (item_id,)).fetchone()
    if not item:
        conn.close()
        raise HTTPException(status_code=404, detail="Approval item not found")

    item = dict(item)
    # Remove from queue
    conn.execute("DELETE FROM approval_queue WHERE id=?", (item_id,))
    # Increment agent tasks
    conn.execute("UPDATE agents SET tasksCompleted = tasksCompleted + 1, lastAction = ? WHERE name = ?",
                 (datetime.now().strftime("%H:%M"), item["agent"]))
    # Add success activity
    conn.execute("INSERT INTO recent_activity (agent, action, timestamp, type) VALUES (?, ?, ?, ?)",
                 (item["agent"], f"APPROVED: {item['task']}", "Just now", "success"))
    conn.commit()
    conn.close()

    add_audit_log("sarah.chen@nexustech.com", f"Approved agent task: {item['task'][:80]}...", "medium", f"Agent: {item['agent']}")
    return {"status": "approved", "task": item["task"], "agent": item["agent"]}


@router.post("/reject/{item_id}")
async def reject_task(item_id: int):
    """Reject an agent task — removes from queue, logs rejection."""
    conn = get_conn()
    item = conn.execute("SELECT * FROM approval_queue WHERE id=?", (item_id,)).fetchone()
    if not item:
        conn.close()
        raise HTTPException(status_code=404, detail="Approval item not found")

    item = dict(item)
    conn.execute("DELETE FROM approval_queue WHERE id=?", (item_id,))
    conn.execute("INSERT INTO recent_activity (agent, action, timestamp, type) VALUES (?, ?, ?, ?)",
                 (item["agent"], f"REJECTED by human review: {item['task']}", "Just now", "alert"))
    conn.commit()
    conn.close()

    add_audit_log("sarah.chen@nexustech.com", f"Rejected agent task: {item['task'][:80]}...", "high", f"Agent: {item['agent']}")
    return {"status": "rejected", "task": item["task"], "agent": item["agent"]}


@router.post("/toggle/{agent_id}")
async def toggle_agent(agent_id: int):
    """Toggle agent between active and idle."""
    conn = get_conn()
    agent = conn.execute("SELECT * FROM agents WHERE id=?", (agent_id,)).fetchone()
    if not agent:
        conn.close()
        raise HTTPException(status_code=404, detail="Agent not found")

    new_status = "idle" if agent["status"] == "active" else "active"
    conn.execute("UPDATE agents SET status=?, lastAction=? WHERE id=?",
                 (new_status, "Just now", agent_id))
    conn.execute("INSERT INTO recent_activity (agent, action, timestamp, type) VALUES (?, ?, ?, ?)",
                 (agent["name"], f"Agent {'paused' if new_status == 'idle' else 'activated'} by operator", "Just now", "info"))
    conn.commit()
    conn.close()

    add_audit_log("sarah.chen@nexustech.com", f"{'Paused' if new_status == 'idle' else 'Activated'} agent: {agent['name']}", "medium", "Agent Management")
    return {"status": new_status, "agent_id": agent_id, "name": agent["name"]}


@router.post("/chat", response_model=ChatResponse)
async def chat_with_agent(req: ChatRequest):
    """Chat with the Legal AI Copilot powered by Gemini with conversation history."""
    if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == "your_gemini_api_key_here":
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY is not configured in backend/.env")

    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)

        system_instruction = (
            "You are LexOS, an Enterprise AI Legal Operating System. You are an expert in:\n"
            "- Contract analysis, clause extraction, and risk identification\n"
            "- Global regulatory compliance (GDPR, CCPA, HIPAA, SOC 2, DORA, MAS TRM)\n"
            "- Litigation risk prediction and dispute resolution strategy\n"
            "- Corporate governance, board management, and ESOP\n"
            "- Legal entity structuring and global expansion\n"
            "- Legal analytics, KPI reporting, and cost forecasting\n\n"
            "Be concise (2-4 sentences), precise, and professional. Cite relevant laws where applicable. "
            "If asked about specific contracts or cases in the LexOS system, reference realistic examples."
        )

        conversation = f"[System]: {system_instruction}\n\n"
        for msg in (req.history or []):
            role_label = "User" if msg.role == "user" else "LexOS AI"
            conversation += f"[{role_label}]: {msg.content}\n"
        conversation += f"[User]: {req.message}"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation,
        )
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
