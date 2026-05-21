"""
LexOS — Analytics & Executive Intelligence API
Legal KPIs, spend forecasting, and executive intelligence reporting.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import settings
from google import genai

router = APIRouter(prefix="/analytics", tags=["Analytics"])


class ReportRequest(BaseModel):
    period: str
    focus_area: str


@router.get("/")
async def get_analytics_data():
    """Get analytics, KPIs, spend trends, and executive intelligence."""
    return {
        "kpis": {
            "total_legal_spend": "$2.1M",
            "spend_change": "+8%",
            "cost_per_matter": "$4,820",
            "cost_change": "-12%",
            "matter_cycle_time": "8.3 days",
            "cycle_change": "-22%",
            "prevention_rate": "74%",
            "prevention_change": "+11%",
            "attorney_hours_saved": 847,
            "ai_savings_usd": 212000,
        },
        "legal_spend": [
            {"month": "Jan", "internal": 180, "external": 320, "budget": 520},
            {"month": "Feb", "internal": 210, "external": 290, "budget": 520},
            {"month": "Mar", "internal": 195, "external": 410, "budget": 600},
            {"month": "Apr", "internal": 220, "external": 360, "budget": 580},
            {"month": "May", "internal": 240, "external": 280, "budget": 520},
            {"month": "Jun", "internal": 200, "external": 350, "budget": 550},
        ],
        "risk_trends": [
            {"month": "Jan", "contractRisk": 62, "complianceRisk": 45, "litigationRisk": 38},
            {"month": "Feb", "contractRisk": 58, "complianceRisk": 42, "litigationRisk": 41},
            {"month": "Mar", "contractRisk": 71, "complianceRisk": 39, "litigationRisk": 55},
            {"month": "Apr", "contractRisk": 65, "complianceRisk": 51, "litigationRisk": 48},
            {"month": "May", "contractRisk": 55, "complianceRisk": 43, "litigationRisk": 52},
            {"month": "Jun", "contractRisk": 48, "complianceRisk": 38, "litigationRisk": 44},
        ],
        "efficiency": [
            {"name": "Contract Review",  "aiTime": 2.1, "manualTime": 14},
            {"name": "Due Diligence",    "aiTime": 5.5, "manualTime": 40},
            {"name": "Compliance Check", "aiTime": 1.2, "manualTime": 8},
            {"name": "Risk Assessment",  "aiTime": 0.8, "manualTime": 6},
            {"name": "NDA Analysis",     "aiTime": 0.3, "manualTime": 2.5},
        ],
        "matters_by_category": [
            {"name": "Commercial",  "value": 34, "color": "#2563EB"},
            {"name": "Employment",  "value": 22, "color": "#10B981"},
            {"name": "IP & Tech",   "value": 18, "color": "#8B5CF6"},
            {"name": "Regulatory",  "value": 15, "color": "#F59E0B"},
            {"name": "Litigation",  "value": 11, "color": "#EF4444"},
        ],
        "spend_forecast": [
            {"month": "Jul", "forecast": 510, "lower": 460, "upper": 560},
            {"month": "Aug", "forecast": 530, "lower": 470, "upper": 590},
            {"month": "Sep", "forecast": 490, "lower": 430, "upper": 550},
            {"month": "Oct", "forecast": 540, "lower": 480, "upper": 600},
            {"month": "Nov", "forecast": 580, "lower": 510, "upper": 650},
            {"month": "Dec", "forecast": 620, "lower": 550, "upper": 690},
        ],
        "executive_summary": {
            "ai_efficiency": "AI automation saved 847 attorney-hours this quarter, equivalent to $212K in external counsel fees. Contract review automation leads at 85% time reduction.",
            "priority_risks": "GDPR enforcement action and Westbrook litigation are highest financial exposure at $7.6M combined. Recommend immediate senior counsel escalation.",
            "q3_forecast": "Projected spend of $1.54M for H2 2026 within 5% of budget. Contract pipeline growth suggests 18% increase in commercial matters — proactive resourcing recommended.",
        },
    }


@router.post("/report")
async def generate_executive_report(req: ReportRequest):
    """Generate AI executive intelligence report."""
    if not settings.GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY not configured")
    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        prompt = (
            f"Generate a concise executive legal intelligence summary for period: {req.period}.\n"
            f"Focus area: {req.focus_area}.\n"
            f"Include: key risks, cost insights, AI efficiency gains, and 2 strategic recommendations.\n"
            f"Format as a professional board-level memo. 150 words max."
        )
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return {"period": req.period, "report": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
