from fastapi import APIRouter
from app.schemas.dashboard import DashboardResponse

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/", response_model=DashboardResponse)
async def get_dashboard_data():
    """Get enterprise dashboard overview data with rich virtual metrics."""
    return {
        # ── KPI Header Cards ────────────────────────────────────────────────
        "legal_risk_score": "72/100",
        "legal_risk_change": "-8% from last month",
        "active_contracts": "1,247",
        "active_contracts_change": "+23 this week",
        "litigation_risk": "Low",
        "litigation_risk_change": "28 cases monitored",
        "compliance_rate": "96%",
        "compliance_rate_change": "+2% this quarter",

        # ── 12-Month Risk & Compliance Trend ────────────────────────────────
        "risk_trend_data": [
            {"month": "Jun '25", "risk": 78, "compliance": 87},
            {"month": "Jul '25", "risk": 74, "compliance": 89},
            {"month": "Aug '25", "risk": 82, "compliance": 85},
            {"month": "Sep '25", "risk": 70, "compliance": 91},
            {"month": "Oct '25", "risk": 67, "compliance": 92},
            {"month": "Nov '25", "risk": 71, "compliance": 90},
            {"month": "Dec '25", "risk": 65, "compliance": 93},
            {"month": "Jan '26", "risk": 60, "compliance": 94},
            {"month": "Feb '26", "risk": 59, "compliance": 94},
            {"month": "Mar '26", "risk": 75, "compliance": 90},
            {"month": "Apr '26", "risk": 68, "compliance": 95},
            {"month": "May '26", "risk": 72, "compliance": 96},
        ],

        # ── Litigation by Category (Pie Chart) ──────────────────────────────
        "litigation_data": [
            {"name": "Contract Disputes",      "value": 12},
            {"name": "IP & Patent Issues",     "value": 8},
            {"name": "Employment Claims",      "value": 5},
            {"name": "Regulatory Violations",  "value": 3},
            {"name": "Data Privacy Breaches",  "value": 4},
            {"name": "Product Liability",      "value": 2},
            {"name": "Securities Disputes",    "value": 1},
        ],

        # ── Global Jurisdiction Exposure (Bar Chart) ─────────────────────────
        "jurisdiction_data": [
            {"name": "USA",       "contracts": 412, "risk": 38},
            {"name": "UK",        "contracts": 189, "risk": 14},
            {"name": "EU",        "contracts": 346, "risk": 52},
            {"name": "APAC",      "contracts": 167, "risk": 22},
            {"name": "India",     "contracts": 73,  "risk": 9},
            {"name": "Canada",    "contracts": 60,  "risk": 7},
        ],

        # ── Upcoming Deadlines ───────────────────────────────────────────────
        "upcoming_deadlines": [
            {"id": 1,  "title": "Q2 GDPR Data Protection Impact Assessment",         "date": "May 25, 2026", "type": "Compliance",  "risk": "high"},
            {"id": 2,  "title": "Board Resolution — Stock Option Grant (FY2026)",     "date": "May 28, 2026", "type": "Governance",   "risk": "medium"},
            {"id": 3,  "title": "Contract Renewal — AWS Enterprise Agreement",        "date": "Jun 01, 2026", "type": "Contract",     "risk": "low"},
            {"id": 4,  "title": "Annual Report Filing — Delaware Secretary of State", "date": "Jun 05, 2026", "type": "Compliance",   "risk": "high"},
            {"id": 5,  "title": "HIPAA BAA Renewal — Vendor: MedData Analytics",     "date": "Jun 10, 2026", "type": "Compliance",   "risk": "high"},
            {"id": 6,  "title": "IP Trademark Registration — LexOS Brand (USPTO)",   "date": "Jun 14, 2026", "type": "IP",           "risk": "medium"},
            {"id": 7,  "title": "SOC 2 Type II Audit Kick-off",                      "date": "Jun 20, 2026", "type": "Compliance",   "risk": "medium"},
            {"id": 8,  "title": "Software License Renewal — Salesforce Enterprise",  "date": "Jun 30, 2026", "type": "Contract",     "risk": "low"},
            {"id": 9,  "title": "CCPA Privacy Policy Annual Update",                 "date": "Jul 01, 2026", "type": "Compliance",   "risk": "medium"},
            {"id": 10, "title": "NDA Expiry — TechCorp Strategic Partnership",       "date": "Jul 15, 2026", "type": "Contract",     "risk": "low"},
        ],

        # ── Recent Alerts ────────────────────────────────────────────────────
        "recent_alerts": [
            {"id": 1, "message": "New GDPR Amendment (Article 25) effective Jun 1 — data minimisation rules updated",                                          "time": "1 hour ago",   "severity": "high"},
            {"id": 2, "message": "Clause mismatch in Vendor Agreement #CTR-2024-003 — jurisdiction conflict detected (NY vs DE)",                              "time": "3 hours ago",  "severity": "high"},
            {"id": 3, "message": "HIPAA Business Associate Agreement with MedData Analytics expires in 30 days — renewal required",                             "time": "6 hours ago",  "severity": "high"},
            {"id": 4, "message": "Acme APAC Pte Ltd regulatory filing deadline approaching — Singapore MAS compliance window closes May 30",                   "time": "10 hours ago", "severity": "medium"},
            {"id": 5, "message": "Office lease at WeWork (NYC HQ) auto-renews in 11 days — review or renegotiate before Jun 1",                                "time": "14 hours ago", "severity": "medium"},
            {"id": 6, "message": "Stock option grant resolution requires board approval before May 28 — 3 board members yet to sign",                           "time": "1 day ago",    "severity": "medium"},
            {"id": 7, "message": "Compliance check passed: EU GDPR Q1 audit completed, no material violations found",                                          "time": "1 day ago",    "severity": "low"},
            {"id": 8, "message": "AWS Enterprise Agreement price lock extended through 2027 — favorable terms auto-captured",                                   "time": "2 days ago",   "severity": "low"},
            {"id": 9, "message": "LexOS Contract Agent reviewed 47 new vendor agreements this week — 5 flagged for human review",                               "time": "2 days ago",   "severity": "medium"},
            {"id": 10,"message": "Trademark search complete — 'LexOS' clear in all target markets (US, EU, IN, SG)",                                           "time": "3 days ago",   "severity": "low"},
        ],
    }
