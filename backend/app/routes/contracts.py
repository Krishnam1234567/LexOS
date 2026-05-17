from fastapi import APIRouter
from app.schemas.contracts import ContractsResponse

router = APIRouter(prefix="/contracts", tags=["Contracts"])

@router.get("/", response_model=ContractsResponse)
async def get_contracts_data():
    """Get contract repository and AI analysis data."""
    return {
        "total_contracts": "1,247",
        "total_contracts_change": "+23 this month",
        "total_value": "$127.3M",
        "expiring_soon": 12,
        "ai_reviewed_percentage": "100%",
        "contracts": [
            {"id": "CTR-2024-001", "name": "AWS Enterprise Agreement", "counterparty": "Amazon Web Services", "type": "Cloud Services", "value": "$2.4M", "endDate": "2027-01-15", "status": "active", "risk": "low"},
            {"id": "CTR-2024-002", "name": "Office Lease Agreement", "counterparty": "WeWork Inc.", "type": "Real Estate", "value": "$850K", "endDate": "2026-05-31", "status": "active", "risk": "medium"},
            {"id": "CTR-2024-003", "name": "Master Services Agreement", "counterparty": "Accenture Consulting", "type": "Consulting", "value": "$1.2M", "endDate": "2024-12-31", "status": "pending", "risk": "high"},
            {"id": "CTR-2023-087", "name": "SaaS License - Salesforce", "counterparty": "Salesforce Inc.", "type": "Software", "value": "$450K", "endDate": "2024-12-31", "status": "active", "risk": "low"},
            {"id": "CTR-2022-045", "name": "Partnership Agreement - TechCorp", "counterparty": "TechCorp Ltd.", "type": "Partnership", "value": "$3.5M", "endDate": "2025-09-15", "status": "active", "risk": "medium"},
        ],
        "clause_analysis": {
            "totalClauses": 1247,
            "highRisk": 23,
            "mediumRisk": 156,
            "lowRisk": 1068
        },
        "ai_insights": [
            {
                "title": "Jurisdiction Conflict Detected",
                "description": "MSA with Accenture contains conflicting jurisdiction clauses (NY vs DE)",
                "contract_id": "CTR-2024-003",
                "severity": "destructive"
            },
            {
                "title": "Auto-Renewal Risk",
                "description": "Office lease auto-renews in 14 days. Consider renegotiation.",
                "contract_id": "CTR-2024-002",
                "severity": "warning"
            },
            {
                "title": "Favorable Terms Identified",
                "description": "AWS contract has favorable price protection clause for 2026",
                "contract_id": "CTR-2024-001",
                "severity": "primary"
            }
        ]
    }
