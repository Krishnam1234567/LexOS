from fastapi import APIRouter
from app.schemas.dashboard import DashboardResponse

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/", response_model=DashboardResponse)
async def get_dashboard_data():
    """Get enterprise dashboard overview data."""
    return {
        "legal_risk_score": "72/100",
        "legal_risk_change": "-8% from last month",
        "active_contracts": "1,247",
        "active_contracts_change": "+23 this week",
        "litigation_risk": "Low",
        "litigation_risk_change": "28 cases monitored",
        "compliance_rate": "96%",
        "compliance_rate_change": "+2% this quarter",
        "risk_trend_data": [
            {"month": "Jan", "risk": 65, "compliance": 92},
            {"month": "Feb", "risk": 59, "compliance": 94},
            {"month": "Mar", "risk": 80, "compliance": 88},
            {"month": "Apr", "risk": 81, "compliance": 90},
            {"month": "May", "risk": 56, "compliance": 95},
            {"month": "Jun", "risk": 55, "compliance": 96},
        ],
        "litigation_data": [
            {"name": "Contract Disputes", "value": 12},
            {"name": "IP Issues", "value": 8},
            {"name": "Employment", "value": 5},
            {"name": "Regulatory", "value": 3},
        ],
        "jurisdiction_data": [
            {"name": "USA", "contracts": 145, "risk": 23},
            {"name": "UK", "contracts": 89, "risk": 12},
            {"name": "EU", "contracts": 234, "risk": 45},
            {"name": "APAC", "contracts": 67, "risk": 8},
        ],
        "upcoming_deadlines": [
            {"id": 1, "title": "Q2 Compliance Filing - GDPR", "date": "May 15, 2026", "type": "Compliance", "risk": "high"},
            {"id": 2, "title": "Board Resolution - Stock Options", "date": "May 18, 2026", "type": "Governance", "risk": "medium"},
            {"id": 3, "title": "Contract Renewal - AWS Enterprise", "date": "May 20, 2026", "type": "Contract", "risk": "low"},
            {"id": 4, "title": "Annual Report Filing - Delaware", "date": "May 25, 2026", "type": "Compliance", "risk": "high"},
        ],
        "recent_alerts": [
            {"id": 1, "message": "New GDPR amendment detected affecting data retention", "time": "2 hours ago", "severity": "high"},
            {"id": 2, "message": "Contract clause mismatch in vendor agreement #2341", "time": "5 hours ago", "severity": "medium"},
            {"id": 3, "message": "Compliance check passed for EU operations", "time": "1 day ago", "severity": "low"},
        ]
    }
