from fastapi import APIRouter
from app.schemas.compliance import ComplianceResponse

router = APIRouter(prefix="/compliance", tags=["Compliance"])

@router.get("/", response_model=ComplianceResponse)
async def get_compliance_data():
    """Get compliance monitoring and regulatory updates with rich virtual data."""
    return {
        # ── Summary KPIs ──────────────────────────────────────────────────────
        "overall_score": "94%",
        "active_frameworks": 14,
        "tasks_due": 11,
        "non_compliant": 3,

        # ── Framework-Level Compliance Scores (Bar Chart) ─────────────────────
        "compliance_scores": [
            {"category": "GDPR",          "score": 95},
            {"category": "CCPA",          "score": 91},
            {"category": "SOC 2",         "score": 89},
            {"category": "ISO 27001",     "score": 92},
            {"category": "HIPAA",         "score": 83},
            {"category": "PCI DSS",       "score": 97},
            {"category": "MAS TRM",       "score": 88},
            {"category": "FCA",           "score": 90},
            {"category": "DORA",          "score": 79},
            {"category": "NIST CSF",      "score": 94},
            {"category": "CIS Controls",  "score": 96},
            {"category": "PDPA (SG)",     "score": 87},
            {"category": "IT Act (IN)",   "score": 85},
            {"category": "UK GDPR",       "score": 93},
        ],

        # ── 12-Month Compliance Trend (Line Chart) ───────────────────────────
        "monthly_trend": [
            {"month": "Jun '25", "compliance": 86},
            {"month": "Jul '25", "compliance": 88},
            {"month": "Aug '25", "compliance": 85},
            {"month": "Sep '25", "compliance": 90},
            {"month": "Oct '25", "compliance": 91},
            {"month": "Nov '25", "compliance": 89},
            {"month": "Dec '25", "compliance": 92},
            {"month": "Jan '26", "compliance": 93},
            {"month": "Feb '26", "compliance": 93},
            {"month": "Mar '26", "compliance": 91},
            {"month": "Apr '26", "compliance": 95},
            {"month": "May '26", "compliance": 94},
        ],

        # ── Active Compliance Tasks ───────────────────────────────────────────
        "tasks": [
            # High Priority
            {
                "id": 1,
                "title": "Q2 GDPR Data Protection Impact Assessment (DPIA) — EU Cloud Workloads",
                "due": "2026-05-25",
                "status": "pending",
                "priority": "high",
            },
            {
                "id": 2,
                "title": "HIPAA BAA Renewal — MedData Analytics Corp. (CTR-2024-088)",
                "due": "2026-05-30",
                "status": "active",
                "priority": "high",
            },
            {
                "id": 3,
                "title": "Annual SOC 2 Type II Audit Preparation — Engage External Auditor",
                "due": "2026-06-01",
                "status": "active",
                "priority": "high",
            },
            {
                "id": 4,
                "title": "DORA ICT Risk Assessment — Acme EU Holdings B.V. (Netherlands)",
                "due": "2026-06-10",
                "status": "pending",
                "priority": "high",
            },
            {
                "id": 5,
                "title": "Delaware Annual Franchise Tax Filing — FY2025",
                "due": "2026-06-01",
                "status": "active",
                "priority": "high",
            },
            # Medium Priority
            {
                "id": 6,
                "title": "ISO 27001 Annex A Controls Review — Quarterly Update",
                "due": "2026-06-15",
                "status": "active",
                "priority": "medium",
            },
            {
                "id": 7,
                "title": "CCPA Consumer Rights Request Audit — Q2 2026",
                "due": "2026-06-20",
                "status": "completed",
                "priority": "medium",
            },
            {
                "id": 8,
                "title": "MAS TRM Compliance Self-Assessment — Acme APAC Pte Ltd",
                "due": "2026-06-30",
                "status": "active",
                "priority": "medium",
            },
            {
                "id": 9,
                "title": "PCI DSS v4.0 Network Segmentation Validation",
                "due": "2026-07-01",
                "status": "pending",
                "priority": "medium",
            },
            {
                "id": 10,
                "title": "GDPR Article 28 DPA Execution — Databricks (CTR-2025-301)",
                "due": "2026-07-10",
                "status": "pending",
                "priority": "medium",
            },
            {
                "id": 11,
                "title": "NIST CSF Gap Assessment — Annual Cyber Posture Review",
                "due": "2026-07-15",
                "status": "active",
                "priority": "medium",
            },
            # Low Priority
            {
                "id": 12,
                "title": "Employee GDPR & Privacy Awareness Training — All Staff Completion",
                "due": "2026-07-31",
                "status": "active",
                "priority": "low",
            },
            {
                "id": 13,
                "title": "UK GDPR Transfer Impact Assessment — Post-Brexit Data Flows",
                "due": "2026-08-01",
                "status": "pending",
                "priority": "low",
            },
            {
                "id": 14,
                "title": "IT Act (India) Compliance Audit — Acme Innovation Labs Partners",
                "due": "2026-08-15",
                "status": "pending",
                "priority": "low",
            },
            {
                "id": 15,
                "title": "Update Vendor Risk Register — Annual Third-Party Compliance Review",
                "due": "2026-08-31",
                "status": "active",
                "priority": "low",
            },
        ],

        # ── Upcoming Regulatory Filings ────────────────────────────────────────
        "upcoming_filings": [
            {"framework": "GDPR",        "filing": "Annual DPO Activity Report",                   "deadline": "May 31, 2026",  "jurisdiction": "European Union"},
            {"framework": "Delaware",    "filing": "Annual Franchise Tax Return",                   "deadline": "Jun 01, 2026",  "jurisdiction": "Delaware, USA"},
            {"framework": "HIPAA",       "filing": "Breach Notification Policy Attestation",        "deadline": "Jun 10, 2026",  "jurisdiction": "USA (Federal)"},
            {"framework": "CCPA",        "filing": "Consumer Privacy Annual Notice Update",         "deadline": "Jun 15, 2026",  "jurisdiction": "California, USA"},
            {"framework": "SOC 2",       "filing": "Type II Audit Report — FY2025/26",             "deadline": "Jul 01, 2026",  "jurisdiction": "USA (AICPA)"},
            {"framework": "MAS TRM",     "filing": "Technology Risk Self-Assessment Report",        "deadline": "Jun 30, 2026",  "jurisdiction": "Singapore"},
            {"framework": "FCA",         "filing": "Operational Resilience Self-Assessment",        "deadline": "Jul 15, 2026",  "jurisdiction": "United Kingdom"},
            {"framework": "PCI DSS",     "filing": "Quarterly Network Scan Report (ASV)",          "deadline": "Jul 01, 2026",  "jurisdiction": "Global (PCI SSC)"},
            {"framework": "UK GDPR",     "filing": "Annual ICO Registration Renewal",              "deadline": "Aug 01, 2026",  "jurisdiction": "United Kingdom"},
            {"framework": "DORA",        "filing": "ICT Risk Register Submission",                  "deadline": "Jun 17, 2026",  "jurisdiction": "European Union"},
        ],

        # ── Regulatory Updates Feed ───────────────────────────────────────────
        "regulatory_updates": [
            {
                "title": "🔴 GDPR — Article 25 Amendment (Effective Jun 1, 2026)",
                "description": "EU Commission published updated data minimisation and privacy-by-design requirements under Article 25. Organisations must document all data processing decisions with proportionality justification. Acme's 3 cloud-native pipelines are impacted.",
                "action_text": "View AI Impact Analysis →",
                "severity": "destructive",
            },
            {
                "title": "🟡 DORA — ICT Third-Party Risk Rules (Live Jan 17, 2026)",
                "description": "EU Digital Operational Resilience Act is now fully in force. Acme EU Holdings B.V. must submit ICT risk register to Dutch AFM by Jun 17. Key gap: 4 critical ICT vendors not yet classified under DORA's concentration risk framework.",
                "action_text": "Generate Remediation Plan →",
                "severity": "warning",
            },
            {
                "title": "🟡 CCPA — New Sensitive Data Category Regulations",
                "description": "California Privacy Protection Agency finalised rules on sensitive personal information processing. AI-inferred data about employees may now qualify as 'sensitive PI'. LexOS has flagged 2 internal ML models for review.",
                "action_text": "Review Flagged Models →",
                "severity": "warning",
            },
            {
                "title": "🟢 SOC 2 — Q1 Readiness Assessment Completed",
                "description": "LexOS Compliance Agent completed the SOC 2 Type II readiness review. Overall score: 89%. 8 control gaps identified across CC6 (Logical Access) and CC7 (Change Management). Remediation playbooks auto-generated.",
                "action_text": "View Playbook →",
                "severity": "primary",
            },
            {
                "title": "🟢 CCPA — Q1 Consumer Rights Audit Passed",
                "description": "Quarterly consumer rights request audit completed with no violations. 47 Data Subject Access Requests and 12 deletion requests fulfilled within statutory timelines. Compliance Agent attestation report available.",
                "action_text": "",
                "severity": "primary",
            },
            {
                "title": "🔴 HIPAA — Business Associate Agreement Expiry Risk",
                "description": "BAA with MedData Analytics Corp. (CTR-2024-088) expires Jun 10, 2026. Processing Protected Health Information without a valid BAA is a HIPAA violation. Penalty range: $100 – $1.9M per violation category. Immediate renewal required.",
                "action_text": "Initiate BAA Renewal →",
                "severity": "destructive",
            },
        ],
    }
