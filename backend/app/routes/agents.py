"""
LexOS — AI Legal Agents API
Autonomous agent management with SQLAlchemy ORM persistence.
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

from app.schemas.chat import ChatRequest, ChatResponse
from app.config import settings
from app.db.session import get_db
from app.db.models import Agent, ApprovalQueueItem, RecentActivity, AuditLog
from google import genai

router = APIRouter(prefix="/agents", tags=["AI Agents"])


async def _add_audit_log(db: AsyncSession, user: str, action: str, severity: str, resource: str):
    log_id = f"LOG-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    db.add(AuditLog(id=log_id, user=user, action=action, severity=severity,
                    resource=resource, time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ip="192.168.1.1"))


@router.get("/")
async def get_agents_data(db: AsyncSession = Depends(get_db)):
    """Get AI Agents from database."""
    agents_result = await db.execute(select(Agent).order_by(Agent.id))
    agents = [{"id": a.id, "name": a.name, "description": a.description, "status": a.status,
               "tasksCompleted": a.tasksCompleted, "lastAction": a.lastAction, "confidence": a.confidence}
              for a in agents_result.scalars().all()]

    activity_result = await db.execute(select(RecentActivity).order_by(RecentActivity.id.desc()).limit(15))
    activity = [{"id": a.id, "agent": a.agent, "action": a.action, "timestamp": a.timestamp, "type": a.type}
                for a in activity_result.scalars().all()]

    queue_result = await db.execute(select(ApprovalQueueItem).order_by(ApprovalQueueItem.id))
    queue = [{"id": q.id, "agent": q.agent, "task": q.task, "reasoning": q.reasoning,
              "confidence": q.confidence, "impact": q.impact}
             for q in queue_result.scalars().all()]

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
async def approve_task(item_id: int, db: AsyncSession = Depends(get_db)):
    """Approve an agent task."""
    result = await db.execute(select(ApprovalQueueItem).where(ApprovalQueueItem.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Approval item not found")

    agent_name = item.agent
    task_text = item.task

    await db.delete(item)

    # Increment agent tasks
    agent_result = await db.execute(select(Agent).where(Agent.name == agent_name))
    agent = agent_result.scalar_one_or_none()
    if agent:
        agent.tasksCompleted += 1
        agent.lastAction = datetime.now().strftime("%H:%M")

    db.add(RecentActivity(agent=agent_name, action=f"APPROVED: {task_text}", timestamp="Just now", type="success"))
    await _add_audit_log(db, "sarah.chen@nexustech.com", f"Approved agent task: {task_text[:80]}...", "medium", f"Agent: {agent_name}")
    return {"status": "approved", "task": task_text, "agent": agent_name}


@router.post("/reject/{item_id}")
async def reject_task(item_id: int, db: AsyncSession = Depends(get_db)):
    """Reject an agent task."""
    result = await db.execute(select(ApprovalQueueItem).where(ApprovalQueueItem.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Approval item not found")

    agent_name = item.agent
    task_text = item.task

    await db.delete(item)
    db.add(RecentActivity(agent=agent_name, action=f"REJECTED by human review: {task_text}", timestamp="Just now", type="alert"))
    await _add_audit_log(db, "sarah.chen@nexustech.com", f"Rejected agent task: {task_text[:80]}...", "high", f"Agent: {agent_name}")
    return {"status": "rejected", "task": task_text, "agent": agent_name}


@router.post("/toggle/{agent_id}")
async def toggle_agent(agent_id: int, db: AsyncSession = Depends(get_db)):
    """Toggle agent between active and idle."""
    result = await db.execute(select(Agent).where(Agent.id == agent_id))
    agent = result.scalar_one_or_none()
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    new_status = "idle" if agent.status == "active" else "active"
    agent.status = new_status
    agent.lastAction = "Just now"

    db.add(RecentActivity(agent=agent.name,
                          action=f"Agent {'paused' if new_status == 'idle' else 'activated'} by operator",
                          timestamp="Just now", type="info"))
    await _add_audit_log(db, "sarah.chen@nexustech.com",
                         f"{'Paused' if new_status == 'idle' else 'Activated'} agent: {agent.name}", "medium", "Agent Management")
    return {"status": new_status, "agent_id": agent_id, "name": agent.name}


@router.post("/chat", response_model=ChatResponse)
async def chat_with_agent(req: ChatRequest, db: AsyncSession = Depends(get_db)):
    """Chat with the Legal AI Copilot powered by Gemini with live database context."""
    if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == "your_gemini_api_key_here":
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY is not configured in backend/.env")

    try:
        # Load active enterprise context from the database
        from app.db.models import Contract, ComplianceTask, LitigationCase, LegalEntity
        
        c_res = await db.execute(select(Contract))
        contracts = c_res.scalars().all()
        
        a_res = await db.execute(select(Agent))
        agents = a_res.scalars().all()
        
        t_res = await db.execute(select(ComplianceTask).where(ComplianceTask.status != "completed"))
        tasks = t_res.scalars().all()
        
        l_res = await db.execute(select(LitigationCase))
        cases = l_res.scalars().all()
        
        e_res = await db.execute(select(LegalEntity))
        entities = e_res.scalars().all()

        contracts_str = ", ".join([f"{c.id} ({c.name} with {c.counterparty}, risk: {c.risk})" for c in contracts[:5]])
        agents_str = ", ".join([f"{a.name} ({a.status})" for a in agents])
        tasks_str = ", ".join([f"'{t.title}' (due {t.due}, {t.priority})" for t in tasks[:5]])
        cases_str = ", ".join([f"{c.id} ({c.title}, status: {c.status}, exposure: {c.exposure}, win probability: {c.winProb}%)" for c in cases])
        entities_str = ", ".join([f"{e.name} ({e.jurisdiction}, {e.type}, risk: {e.risk})" for e in entities])

        client = genai.Client(api_key=settings.GEMINI_API_KEY)

        system_instruction = (
            "You are LexOS, an Enterprise AI Legal Operating System. You have direct access to the live corporate legal database.\n"
            "Here is the active real-time context of the enterprise from the database:\n\n"
            f"1. Active Subsidiaries & Entities: {entities_str}\n"
            f"2. Core Contracts in Repository: {contracts_str}\n"
            f"3. Active Compliance Checklist: {tasks_str}\n"
            f"4. Litigations Monitored: {cases_str}\n"
            f"5. Running AI Agents: {agents_str}\n\n"
            "Use this live enterprise context to answer queries accurately. If the user asks about contracts, compliance tasks, active lawsuits, or entities, answer based on the real records listed above.\n"
            "Be precise, professional, and concise (2-4 sentences max). Cite laws where relevant."
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

