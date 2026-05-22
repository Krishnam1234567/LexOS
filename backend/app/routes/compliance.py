"""
LexOS — Compliance Automation API
Database-backed compliance monitoring with Gemini AI analysis.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import settings
from app.db.sqlite_db import get_conn, add_audit_log
from google import genai


router = APIRouter(prefix="/compliance", tags=["Compliance"])


class ComplianceAnalysisRequest(BaseModel):
    framework: str
    context: str


class TaskUpdateRequest(BaseModel):
    title: str
    due: str
    priority: str
    status: str


@router.get("/")
async def get_compliance_data():
    """Get compliance data from database."""
    conn = get_conn()
    scores = [dict(r) for r in conn.execute("SELECT * FROM compliance_scores").fetchall()]
    tasks = [dict(r) for r in conn.execute("SELECT * FROM compliance_tasks ORDER BY id").fetchall()]
    filings = [dict(r) for r in conn.execute("SELECT * FROM upcoming_filings ORDER BY deadline").fetchall()]
    updates = [dict(r) for r in conn.execute("SELECT * FROM regulatory_updates ORDER BY id DESC").fetchall()]
    conn.close()

    avg_score = sum(s["score"] for s in scores) // max(len(scores), 1)
    pending_tasks = sum(1 for t in tasks if t["status"] in ("pending", "in_progress"))
    non_compliant = sum(1 for s in scores if s["score"] < 85)

    return {
        "overall_score": f"{avg_score}%",
        "active_frameworks": len(scores),
        "tasks_due": pending_tasks,
        "non_compliant": non_compliant,
        "compliance_scores": scores,
        "monthly_trend": [
            {"month": "Jan", "compliance": 82}, {"month": "Feb", "compliance": 85},
            {"month": "Mar", "compliance": 87}, {"month": "Apr", "compliance": 89},
            {"month": "May", "compliance": avg_score}, {"month": "Jun", "compliance": avg_score + 1},
            {"month": "Jul", "compliance": avg_score - 2}, {"month": "Aug", "compliance": avg_score + 2},
            {"month": "Sep", "compliance": avg_score + 1}, {"month": "Oct", "compliance": avg_score + 3},
            {"month": "Nov", "compliance": avg_score + 2}, {"month": "Dec", "compliance": avg_score + 4},
        ],
        "tasks": tasks,
        "upcoming_filings": filings,
        "regulatory_updates": updates,
    }


@router.post("/tasks")
async def add_or_update_task(req: TaskUpdateRequest):
    """Add a new compliance task."""
    conn = get_conn()
    conn.execute(
        "INSERT INTO compliance_tasks (title, due, priority, status) VALUES (?, ?, ?, ?)",
        (req.title, req.due, req.priority, req.status)
    )
    conn.commit()
    conn.close()
    add_audit_log("sarah.chen@nexustech.com", f"Created compliance task: {req.title}", "low", "Compliance Module")
    return {"status": "created", "title": req.title}


@router.post("/tasks/{task_id}/status")
async def update_task_status(task_id: int, status: str):
    """Update compliance task status."""
    conn = get_conn()
    task = conn.execute("SELECT * FROM compliance_tasks WHERE id=?", (task_id,)).fetchone()
    if not task:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    conn.execute("UPDATE compliance_tasks SET status=? WHERE id=?", (status, task_id))
    conn.commit()
    conn.close()
    add_audit_log("sarah.chen@nexustech.com", f"Updated compliance task #{task_id} status to {status}", "low", "Compliance Module")
    return {"status": "updated", "task_id": task_id, "new_status": status}


@router.post("/analyze")
async def analyze_compliance(req: ComplianceAnalysisRequest):
    """AI-powered compliance analysis using Gemini."""
    if not settings.GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY not configured")
    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        prompt = (
            f"You are a regulatory compliance expert. Analyze the compliance status for:\n"
            f"Framework: {req.framework}\n"
            f"Context: {req.context}\n\n"
            f"Provide: 1) Current compliance gaps, 2) Regulatory exposure risk, "
            f"3) Immediate remediation steps, 4) Timeline recommendation.\n"
            f"Be precise and actionable. 4-5 sentences. Professional compliance tone."
        )
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        add_audit_log("ai-system", f"AI compliance analysis for {req.framework}", "low", "Compliance AI")
        return {"framework": req.framework, "analysis": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
