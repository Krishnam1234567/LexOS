"""
LexOS — Security & AI Governance API
Role management, audit logs, and AI safety controls.
"""
from fastapi import APIRouter
router = APIRouter(prefix="/security", tags=["Security"])


@router.get("/")
async def get_security_data():
    """Get security posture, audit logs, roles, and AI governance policies."""
    return {
        "summary": {
            "security_score": "94/100",
            "active_users": 18,
            "external_users": 3,
            "ai_actions_24h": 342,
            "ai_human_reviewed": 8,
            "alerts": 3,
            "high_severity_alerts": 1,
        },
        "access_activity": [
            {"hour": "00", "accesses": 4},  {"hour": "04", "accesses": 2},
            {"hour": "08", "accesses": 38}, {"hour": "10", "accesses": 72},
            {"hour": "12", "accesses": 55}, {"hour": "14", "accesses": 81},
            {"hour": "16", "accesses": 64}, {"hour": "18", "accesses": 28},
            {"hour": "20", "accesses": 12}, {"hour": "22", "accesses": 7},
        ],
        "security_posture": [
            {"label": "MFA Enrollment",         "value": 100, "color": "bg-accent"},
            {"label": "Encryption at Rest",     "value": 100, "color": "bg-accent"},
            {"label": "Role Compliance",        "value": 94,  "color": "bg-accent"},
            {"label": "AI Policy Adherence",    "value": 87,  "color": "bg-primary"},
            {"label": "External User Isolation","value": 100, "color": "bg-accent"},
            {"label": "Audit Coverage",         "value": 100, "color": "bg-accent"},
        ],
        "roles": [
            {"id": 1, "name": "General Counsel",       "users": 1, "permissions": ["All Access", "AI Override", "Admin Panel"],        "level": "admin"},
            {"id": 2, "name": "Senior Legal Counsel",  "users": 4, "permissions": ["Contracts RW", "Compliance RW", "Agents Read"],    "level": "senior"},
            {"id": 3, "name": "Legal Analyst",         "users": 8, "permissions": ["Contracts Read", "Compliance Read", "Reports"],    "level": "standard"},
            {"id": 4, "name": "External Counsel",      "users": 3, "permissions": ["Assigned Matters Only", "Limited AI Access"],      "level": "external"},
            {"id": 5, "name": "Board Observer",        "users": 2, "permissions": ["Governance View", "Analytics Read"],               "level": "observer"},
        ],
        "audit_logs": [
            {"id": "AL-8821", "user": "Sarah Chen",        "action": "Exported contract data — Q1 batch (847 records)",                               "time": "2 min ago",  "severity": "medium", "ip": "192.168.1.45", "resource": "Contracts"},
            {"id": "AL-8820", "user": "Marcus Okafor",     "action": "Approved AI recommendation — Early settlement LIT-004",                        "time": "18 min ago", "severity": "high",   "ip": "10.0.2.12",   "resource": "Litigation"},
            {"id": "AL-8819", "user": "API System",        "action": "Salesforce sync completed — 42 records updated",                               "time": "23 min ago", "severity": "low",    "ip": "Internal",    "resource": "Integrations"},
            {"id": "AL-8818", "user": "Priya K.",          "action": "Modified compliance task — GDPR Article 32 deadline extended",                  "time": "1h ago",     "severity": "medium", "ip": "192.168.1.67","resource": "Compliance"},
            {"id": "AL-8817", "user": "External Counsel 2","action": "Accessed LIT-002 — Patent matter documents",                                   "time": "2h ago",     "severity": "low",    "ip": "203.45.12.88","resource": "Litigation"},
            {"id": "AL-8816", "user": "James Whitfield",   "action": "Role change — Robert Lin promoted to Senior Counsel",                           "time": "4h ago",     "severity": "high",   "ip": "10.0.2.15",  "resource": "Admin"},
            {"id": "AL-8815", "user": "AI Agent — ContractGuard","action": "Flagged 3 contracts for clause anomaly — auto-paused pending review",    "time": "6h ago",     "severity": "medium", "ip": "AI System",   "resource": "AI Agents"},
        ],
        "ai_governance_policies": [
            {"name": "Human-in-the-Loop for High Risk",  "status": "active",   "description": "All AI actions with risk score >70 require human approval before execution."},
            {"name": "AI Confidence Threshold",          "status": "active",   "description": "Actions with AI confidence <80% are queued for review rather than auto-executed."},
            {"name": "Data Minimization Guard",          "status": "active",   "description": "AI models only access the minimum necessary data for each task."},
            {"name": "Explainability Logging",           "status": "active",   "description": "All AI decisions are logged with reasoning chains for audit trail."},
            {"name": "Bias Detection Protocol",          "status": "warning",  "description": "Monthly bias audit scheduled. Last audit: Apr 2026 — 2 flagged patterns under review."},
            {"name": "External Counsel Data Isolation",  "status": "active",   "description": "External users cannot access data outside assigned matters."},
        ],
    }
