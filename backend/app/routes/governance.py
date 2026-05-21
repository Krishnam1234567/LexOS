"""
LexOS — Governance & Board Management API
Board resolutions, ESOP, directors, and corporate calendar.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import settings
from google import genai

router = APIRouter(prefix="/governance", tags=["Governance"])


class ResolutionDraftRequest(BaseModel):
    resolution_type: str
    context: str


@router.get("/")
async def get_governance_data():
    """Get governance data — board, resolutions, ESOP, and calendar."""
    return {
        "summary": {
            "board_members": 6,
            "resolutions_ytd": 14,
            "esop_granted_pct": 8.2,
            "avg_attendance": 92,
        },
        "board_members": [
            {"id": 1, "name": "Sarah Chen",           "role": "Chairperson",            "committees": ["Audit", "Risk"],              "tenure": "4y 2m", "attendance": 95, "independent": True,  "avatar": "SC"},
            {"id": 2, "name": "Marcus Okafor",         "role": "CEO (Executive)",         "committees": ["Strategy"],                   "tenure": "3y 8m", "attendance": 100,"independent": False, "avatar": "MO"},
            {"id": 3, "name": "Priya Krishnamurthy",   "role": "Independent Director",    "committees": ["Audit", "Compensation"],      "tenure": "2y 5m", "attendance": 88, "independent": True,  "avatar": "PK"},
            {"id": 4, "name": "James Whitfield",       "role": "CFO (Executive)",         "committees": ["Finance", "Risk"],            "tenure": "5y 1m", "attendance": 92, "independent": False, "avatar": "JW"},
            {"id": 5, "name": "Dr. Anika Müller",      "role": "Independent Director",    "committees": ["Compensation", "Strategy"],   "tenure": "1y 11m","attendance": 96, "independent": True,  "avatar": "AM"},
            {"id": 6, "name": "Robert Lin",            "role": "Independent Director",    "committees": ["Risk", "Finance"],            "tenure": "3y 0m", "attendance": 84, "independent": True,  "avatar": "RL"},
        ],
        "resolutions": [
            {"id": "BR-2026-14", "title": "Approval of FY2026 Annual Budget",                  "date": "May 15, 2026", "status": "passed", "votes": {"for": 6, "against": 0, "abstain": 0}, "type": "Financial"},
            {"id": "BR-2026-13", "title": "Series C Funding Term Sheet Authorization",          "date": "May 8, 2026",  "status": "passed", "votes": {"for": 5, "against": 1, "abstain": 0}, "type": "Corporate"},
            {"id": "BR-2026-12", "title": "ESOP Pool Expansion — Additional 5%",               "date": "Apr 22, 2026", "status": "passed", "votes": {"for": 5, "against": 0, "abstain": 1}, "type": "Compensation"},
            {"id": "BR-2026-11", "title": "EU Subsidiary Incorporation Approval",              "date": "Apr 10, 2026", "status": "passed", "votes": {"for": 6, "against": 0, "abstain": 0}, "type": "Corporate"},
            {"id": "BR-2026-10", "title": "CEO Compensation Review FY2026",                    "date": "Mar 28, 2026", "status": "passed", "votes": {"for": 4, "against": 0, "abstain": 2}, "type": "Compensation"},
        ],
        "esop": {
            "total_pool_pct": 15.0,
            "granted_pct": 10.8,
            "available_pct": 4.2,
            "distribution": [
                {"name": "Employees", "value": 72, "color": "#2563EB"},
                {"name": "Available", "value": 28, "color": "#1F2937"},
            ],
            "vesting_data": [
                {"quarter": "Q1'25", "vested": 120},
                {"quarter": "Q2'25", "vested": 85},
                {"quarter": "Q3'25", "vested": 145},
                {"quarter": "Q4'25", "vested": 210},
                {"quarter": "Q1'26", "vested": 180},
                {"quarter": "Q2'26", "vested": 95},
            ],
        },
        "calendar": [
            {"date": "Jun 25", "title": "Q2 2026 Board Meeting",                    "type": "meeting",    "urgent": False},
            {"date": "Jul 1",  "title": "ESOP Vesting Cliff — Batch 4",             "type": "esop",       "urgent": False},
            {"date": "Jul 15", "title": "Annual General Meeting",                    "type": "agm",        "urgent": True},
            {"date": "Aug 1",  "title": "Director Appointment Vote",                 "type": "vote",       "urgent": False},
            {"date": "Sep 30", "title": "Annual Report Filing Deadline",             "type": "compliance", "urgent": False},
        ],
    }


@router.post("/draft-resolution")
async def draft_resolution(req: ResolutionDraftRequest):
    """AI-drafted board resolution text."""
    if not settings.GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY not configured")
    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        prompt = (
            f"Draft a formal corporate board resolution for a Delaware-incorporated company.\n"
            f"Resolution type: {req.resolution_type}\nContext: {req.context}\n\n"
            f"Format: WHEREAS recitals + RESOLVED clauses. Professional legal language. Keep it concise."
        )
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return {"draft": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
