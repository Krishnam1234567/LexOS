"""
LexOS — Contract Intelligence API
Full CRUD with SQLite persistence and Gemini AI analysis.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import settings
from app.db.sqlite_db import get_conn, add_audit_log
from google import genai
import uuid


router = APIRouter(prefix="/contracts", tags=["Contracts"])


class ContractAnalysisRequest(BaseModel):
    contract_id: str
    contract_name: str
    contract_type: str
    key_concern: str | None = None


class ContractAddRequest(BaseModel):
    name: str
    counterparty: str
    type: str
    value: str
    endDate: str
    status: str = "active"
    risk: str = "medium"


@router.get("/")
async def get_contracts_data():
    """Get contract repository from database."""
    conn = get_conn()
    contracts = [dict(r) for r in conn.execute("SELECT * FROM contracts ORDER BY id").fetchall()]
    conn.close()

    # Compute derived stats
    active = [c for c in contracts if c["status"] == "active"]
    high_risk = sum(1 for c in contracts if c["risk"] == "high")
    medium_risk = sum(1 for c in contracts if c["risk"] == "medium")
    low_risk = sum(1 for c in contracts if c["risk"] == "low")
    total_clauses = len(contracts) * 47  # simulated

    return {
        "total_contracts": len(contracts),
        "total_contracts_change": f"+{len(contracts) - 3} this quarter",
        "total_value": f"${sum(int(c['value'].replace('$','').replace(',','')) for c in contracts if c['value'] != '$0'):,}",
        "expiring_soon": sum(1 for c in contracts if c["endDate"] < "2027-01-01"),
        "ai_reviewed_percentage": f"{min(98, 85 + len(contracts))}%",
        "contracts": contracts,
        "clause_analysis": {
            "totalClauses": total_clauses,
            "highRisk": high_risk * 3,
            "mediumRisk": medium_risk * 8,
            "lowRisk": total_clauses - high_risk * 3 - medium_risk * 8,
        },
        "ai_insights": [
            {"title": "Indemnification Gap Detected", "description": f"Contract CTR-2024-003 contains unlimited indemnity exposure without reciprocal cap.", "severity": "destructive", "contract_id": "CTR-2024-003"},
            {"title": "Auto-Renewal Clause Warning", "description": f"3 contracts have 30-day auto-renewal windows approaching. Review recommended.", "severity": "warning", "contract_id": "CTR-2024-001"},
            {"title": "Favorable Terms Identified", "description": f"AWS Enterprise License has 15% below-market pricing with guaranteed SLA.", "severity": "primary", "contract_id": "CTR-2024-006"},
        ],
    }


@router.post("/add")
async def add_contract(req: ContractAddRequest):
    """Add a new contract to the database."""
    conn = get_conn()
    # Generate unique ID
    count = conn.execute("SELECT COUNT(*) FROM contracts").fetchone()[0]
    ctr_id = f"CTR-2024-{count + 1:03d}"

    conn.execute(
        "INSERT INTO contracts VALUES (?,?,?,?,?,?,?,?,?)",
        (ctr_id, req.name, req.counterparty, req.type, req.value, req.endDate, req.status, req.risk, None)
    )
    conn.commit()
    conn.close()

    add_audit_log("sarah.chen@nexustech.com", f"New contract added: {req.name} ({ctr_id})", "medium", f"Contract: {ctr_id}")
    return {"status": "created", "id": ctr_id, "name": req.name}


@router.post("/analyze")
async def analyze_contract(req: ContractAnalysisRequest):
    """AI-powered contract analysis using Gemini. Saves result to DB."""
    if not settings.GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY not configured")
    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        prompt = (
            f"You are an expert contract lawyer. Analyze this enterprise contract:\n"
            f"Contract ID: {req.contract_id}\n"
            f"Name: {req.contract_name}\n"
            f"Type: {req.contract_type}\n"
            f"{f'Key concern: {req.key_concern}' if req.key_concern else ''}\n\n"
            f"Provide: 1) Key risk clauses to watch, 2) Compliance obligations, "
            f"3) Negotiation leverage points, 4) Recommended next action.\n"
            f"Be concise and actionable. 4-5 sentences max. Professional legal tone."
        )
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

        # Persist analysis to DB
        conn = get_conn()
        conn.execute("UPDATE contracts SET analysis=? WHERE id=?", (response.text, req.contract_id))
        conn.commit()
        conn.close()

        add_audit_log("ai-system", f"AI analysis completed for contract {req.contract_id}", "low", f"Contract: {req.contract_id}")
        return {"contract_id": req.contract_id, "analysis": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
