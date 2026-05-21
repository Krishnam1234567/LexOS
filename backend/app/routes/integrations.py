"""
LexOS — Integrations & Security API
Enterprise integration status, audit logs, and AI governance policies.
"""
from fastapi import APIRouter
router = APIRouter(prefix="/integrations", tags=["Integrations"])


@router.get("/")
async def get_integrations_data():
    """Get enterprise integration status and sync activity."""
    return {
        "summary": {
            "connected": 6,
            "total": 9,
            "records_synced_24h": "27.7K",
            "avg_uptime_pct": 99.1,
            "pending_setup": 2,
        },
        "integrations": [
            {
                "id": "sap",        "name": "SAP S/4HANA",        "category": "ERP",            "logo": "🏭",
                "status": "connected",    "lastSync": "2 min ago",      "recordsSync": "12,840",
                "description": "Contract data, purchase orders, and vendor management sync",
                "features": ["Contract Lifecycle", "Vendor Management", "Invoice Matching"],
                "health": 99.8,
            },
            {
                "id": "salesforce", "name": "Salesforce CRM",      "category": "CRM",            "logo": "☁️",
                "status": "connected",    "lastSync": "5 min ago",      "recordsSync": "8,220",
                "description": "Deal contracts, NDAs, and customer agreement tracking",
                "features": ["Opportunity Contracts", "NDA Automation", "E-Signature Triggers"],
                "health": 98.2,
            },
            {
                "id": "workday",    "name": "Workday HCM",         "category": "HR",             "logo": "👥",
                "status": "connected",    "lastSync": "12 min ago",     "recordsSync": "3,401",
                "description": "Employment contracts, ESOP grants, and compliance records",
                "features": ["Employment Contracts", "ESOP Tracking", "Policy Acknowledgements"],
                "health": 97.5,
            },
            {
                "id": "docusign",   "name": "DocuSign",            "category": "E-Signature",    "logo": "✍️",
                "status": "connected",    "lastSync": "1 min ago",      "recordsSync": "2,180",
                "description": "Digital signature workflows and contract execution tracking",
                "features": ["Signature Workflows", "Audit Trail", "Template Library"],
                "health": 100,
            },
            {
                "id": "slack",      "name": "Slack",               "category": "Communication",  "logo": "💬",
                "status": "warning",      "lastSync": "1h 32m ago",     "recordsSync": "—",
                "description": "Legal alerts, approval notifications, and team collaboration",
                "features": ["Alert Notifications", "Approval Workflows", "Legal Bot"],
                "health": 72,
            },
            {
                "id": "jira",       "name": "Jira",                "category": "Project Mgmt",   "logo": "🎯",
                "status": "connected",    "lastSync": "18 min ago",     "recordsSync": "1,045",
                "description": "Legal matter tracking, task assignment, and deadline management",
                "features": ["Matter Tracking", "SLA Alerts", "Board Integrations"],
                "health": 96.1,
            },
            {
                "id": "sharepoint", "name": "SharePoint",          "category": "Document Mgmt",  "logo": "📁",
                "status": "disconnected", "lastSync": "Never",          "recordsSync": "—",
                "description": "Document management, version control, and team collaboration",
                "features": ["Document Sync", "Version Control", "Access Management"],
                "health": 0,
            },
            {
                "id": "servicenow", "name": "ServiceNow",          "category": "ITSM",           "logo": "⚙️",
                "status": "pending",      "lastSync": "Connecting...",  "recordsSync": "—",
                "description": "IT risk governance, policy management, and audit tracking",
                "features": ["Risk Management", "Policy Compliance", "Audit Logs"],
                "health": 0,
            },
            {
                "id": "greenhouse", "name": "Greenhouse",          "category": "Recruiting",     "logo": "🌱",
                "status": "disconnected", "lastSync": "Never",          "recordsSync": "—",
                "description": "Employment contracts, offer letter automation, and I-9 compliance",
                "features": ["Offer Contracts", "I-9 Management", "Background Checks"],
                "health": 0,
            },
        ],
        "recent_activity": [
            {"time": "2m ago",  "event": "Salesforce sync completed — 42 new contracts imported",              "status": "success"},
            {"time": "5m ago",  "event": "DocuSign: 3 signatures received on MSA — Acme Corp",               "status": "success"},
            {"time": "14m ago", "event": "SAP: 8 vendor contracts flagged for review",                        "status": "info"},
            {"time": "1h ago",  "event": "Slack integration: Webhook timeout error (retrying)",               "status": "warning"},
            {"time": "2h ago",  "event": "Workday: ESOP grant batch processed — 23 employees",               "status": "success"},
            {"time": "3h ago",  "event": "Jira: 5 legal matters closed — SLA within target",                 "status": "success"},
        ],
    }
