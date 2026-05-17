from fastapi import APIRouter
from app.schemas.compliance import ComplianceResponse

router = APIRouter(prefix="/compliance", tags=["Compliance"])

@router.get("/", response_model=ComplianceResponse)
async def get_compliance_data():
    """Get compliance monitoring and regulatory updates."""
    return {
        "overall_score": "96%",
        "active_frameworks": 12,
        "tasks_due": 8,
        "non_compliant": 2,
        "compliance_scores": [
            {"category": "GDPR", "score": 95},
            {"category": "CCPA", "score": 88},
            {"category": "SOC 2", "score": 92},
            {"category": "ISO 27001", "score": 90},
            {"category": "HIPAA", "score": 85},
            {"category": "PCI DSS", "score": 94},
        ],
        "monthly_trend": [
            {"month": "Jan", "compliance": 89},
            {"month": "Feb", "compliance": 91},
            {"month": "Mar", "compliance": 88},
            {"month": "Apr", "compliance": 93},
            {"month": "May", "compliance": 96},
            {"month": "Jun", "compliance": 96},
        ],
        "tasks": [
            {"id": 1, "title": "Q2 GDPR Data Protection Impact Assessment", "due": "2026-05-15", "status": "pending", "priority": "high"},
            {"id": 2, "title": "Annual SOC 2 Type II Audit Preparation", "due": "2026-05-20", "status": "active", "priority": "high"},
            {"id": 3, "title": "CCPA Consumer Rights Request Review", "due": "2026-05-18", "status": "completed", "priority": "medium"},
            {"id": 4, "title": "ISO 27001 Policy Review & Update", "due": "2026-05-25", "status": "active", "priority": "medium"},
            {"id": 5, "title": "Employee Privacy Training Completion", "due": "2026-05-30", "status": "active", "priority": "low"},
        ],
        "upcoming_filings": [
            {"framework": "GDPR", "filing": "Annual DPO Report", "deadline": "May 31, 2026", "jurisdiction": "EU"},
            {"framework": "CCPA", "filing": "Privacy Policy Update", "deadline": "June 15, 2026", "jurisdiction": "California"},
            {"framework": "SOC 2", "filing": "Type II Audit Report", "deadline": "July 1, 2026", "jurisdiction": "USA"},
        ],
        "regulatory_updates": [
            {
                "title": "GDPR Amendment - Article 25",
                "description": "New data minimization requirements effective June 1, 2026",
                "action_text": "Read AI Analysis →",
                "severity": "warning"
            },
            {
                "title": "CCPA Compliance Verified",
                "description": "Quarterly audit completed. No issues found.\nVerified: May 10, 2026",
                "action_text": "",
                "severity": "primary"
            },
            {
                "title": "Action Required: HIPAA",
                "description": "Business Associate Agreement needs renewal for 2 vendors",
                "action_text": "Assign Task →",
                "severity": "destructive"
            }
        ]
    }
