from fastapi import APIRouter
from app.schemas.contracts import ContractsResponse

router = APIRouter(prefix="/contracts", tags=["Contracts"])

@router.get("/", response_model=ContractsResponse)
async def get_contracts_data():
    """Get contract repository and AI analysis data with rich virtual records."""
    return {
        # ── Summary KPIs ─────────────────────────────────────────────────────
        "total_contracts": "1,247",
        "total_contracts_change": "+23 this month",
        "total_value": "$127.3M",
        "expiring_soon": 14,
        "ai_reviewed_percentage": "100%",

        # ── Contract Repository ───────────────────────────────────────────────
        "contracts": [
            # ── Cloud & Infrastructure ──────────────────────────────────────
            {
                "id": "CTR-2024-001",
                "name": "AWS Enterprise License Agreement",
                "counterparty": "Amazon Web Services, Inc.",
                "type": "Cloud Infrastructure",
                "value": "$2.4M",
                "endDate": "2027-01-15",
                "status": "active",
                "risk": "low",
            },
            {
                "id": "CTR-2025-112",
                "name": "Google Cloud Platform — Strategic Partnership",
                "counterparty": "Google LLC",
                "type": "Cloud Infrastructure",
                "value": "$1.1M",
                "endDate": "2026-11-30",
                "status": "active",
                "risk": "low",
            },
            {
                "id": "CTR-2025-089",
                "name": "Azure Active Directory & M365 Enterprise",
                "counterparty": "Microsoft Corporation",
                "type": "Software / Cloud",
                "value": "$620K",
                "endDate": "2026-08-31",
                "status": "active",
                "risk": "low",
            },
            # ── SaaS Licenses ────────────────────────────────────────────────
            {
                "id": "CTR-2023-087",
                "name": "Salesforce CRM Enterprise Edition",
                "counterparty": "Salesforce, Inc.",
                "type": "SaaS License",
                "value": "$450K",
                "endDate": "2026-12-31",
                "status": "active",
                "risk": "low",
            },
            {
                "id": "CTR-2024-204",
                "name": "Workday HCM — HR Platform License",
                "counterparty": "Workday, Inc.",
                "type": "SaaS License",
                "value": "$380K",
                "endDate": "2027-03-31",
                "status": "active",
                "risk": "low",
            },
            {
                "id": "CTR-2025-301",
                "name": "Databricks Unified Analytics Platform",
                "counterparty": "Databricks, Inc.",
                "type": "SaaS / AI Platform",
                "value": "$290K",
                "endDate": "2026-09-30",
                "status": "active",
                "risk": "low",
            },
            # ── Real Estate ──────────────────────────────────────────────────
            {
                "id": "CTR-2024-002",
                "name": "NYC HQ Office Lease — WeWork Hudson Yards",
                "counterparty": "WeWork Inc.",
                "type": "Real Estate",
                "value": "$1.7M",
                "endDate": "2026-06-01",
                "status": "active",
                "risk": "high",
            },
            {
                "id": "CTR-2023-055",
                "name": "London Office Lease — Canary Wharf",
                "counterparty": "British Land PLC",
                "type": "Real Estate",
                "value": "$950K",
                "endDate": "2028-03-31",
                "status": "active",
                "risk": "low",
            },
            {
                "id": "CTR-2024-178",
                "name": "Singapore Regional HQ Lease — One Raffles Quay",
                "counterparty": "CapitaLand Commercial Trust",
                "type": "Real Estate",
                "value": "$730K",
                "endDate": "2027-12-31",
                "status": "active",
                "risk": "medium",
            },
            # ── Consulting & Professional Services ───────────────────────────
            {
                "id": "CTR-2024-003",
                "name": "Digital Transformation MSA",
                "counterparty": "Accenture Consulting LLP",
                "type": "Professional Services",
                "value": "$1.2M",
                "endDate": "2026-05-31",
                "status": "pending",
                "risk": "high",
            },
            {
                "id": "CTR-2025-041",
                "name": "Cybersecurity Audit & Penetration Testing",
                "counterparty": "CrowdStrike Holdings, Inc.",
                "type": "Security Services",
                "value": "$280K",
                "endDate": "2026-07-15",
                "status": "active",
                "risk": "low",
            },
            {
                "id": "CTR-2025-198",
                "name": "External Legal Counsel Retainer Agreement",
                "counterparty": "Kirkland & Ellis LLP",
                "type": "Legal Services",
                "value": "$1.5M",
                "endDate": "2027-01-01",
                "status": "active",
                "risk": "low",
            },
            # ── Partnerships & Data ──────────────────────────────────────────
            {
                "id": "CTR-2022-045",
                "name": "Strategic Technology Partnership — TechCorp",
                "counterparty": "TechCorp Ltd.",
                "type": "Partnership",
                "value": "$3.5M",
                "endDate": "2026-09-15",
                "status": "active",
                "risk": "medium",
            },
            {
                "id": "CTR-2024-311",
                "name": "Data Licensing Agreement — Market Intelligence",
                "counterparty": "Bloomberg L.P.",
                "type": "Data License",
                "value": "$420K",
                "endDate": "2026-12-31",
                "status": "active",
                "risk": "low",
            },
            # ── Healthcare / Compliance ──────────────────────────────────────
            {
                "id": "CTR-2024-088",
                "name": "HIPAA Business Associate Agreement",
                "counterparty": "MedData Analytics Corp.",
                "type": "Healthcare / HIPAA",
                "value": "$190K",
                "endDate": "2026-06-10",
                "status": "active",
                "risk": "high",
            },
            # ── Manufacturing & Supply Chain ─────────────────────────────────
            {
                "id": "CTR-2025-227",
                "name": "Hardware Supply Agreement — IoT Devices",
                "counterparty": "Foxconn Industrial Internet",
                "type": "Supply Chain",
                "value": "$5.2M",
                "endDate": "2027-06-30",
                "status": "active",
                "risk": "medium",
            },
            {
                "id": "CTR-2025-349",
                "name": "Last-Mile Logistics Framework Agreement",
                "counterparty": "FedEx Corporation",
                "type": "Logistics",
                "value": "$310K",
                "endDate": "2026-10-31",
                "status": "active",
                "risk": "low",
            },
            # ── Employment / HR ──────────────────────────────────────────────
            {
                "id": "CTR-2025-500",
                "name": "Executive Compensation & Severance Agreement — CTO",
                "counterparty": "Dr. Priya Mehta (CTO)",
                "type": "Employment",
                "value": "$2.8M",
                "endDate": "2028-01-01",
                "status": "active",
                "risk": "low",
            },
            {
                "id": "CTR-2026-011",
                "name": "Contractor Master Services Agreement — AI Division",
                "counterparty": "NovaTech Solutions Pvt. Ltd.",
                "type": "Contractor / MSA",
                "value": "$640K",
                "endDate": "2026-11-30",
                "status": "pending",
                "risk": "high",
            },
            # ── Expired / Completed ──────────────────────────────────────────
            {
                "id": "CTR-2023-001",
                "name": "Legacy ERP System Support Agreement",
                "counterparty": "SAP SE",
                "type": "Software Support",
                "value": "$510K",
                "endDate": "2025-12-31",
                "status": "expired",
                "risk": "low",
            },
        ],

        # ── AI Clause Analysis Summary ────────────────────────────────────────
        "clause_analysis": {
            "totalClauses": 4893,
            "highRisk": 67,
            "mediumRisk": 412,
            "lowRisk": 4414,
        },

        # ── AI-Generated Insights ─────────────────────────────────────────────
        "ai_insights": [
            {
                "title": "Jurisdiction Conflict — CTR-2024-003",
                "description": "Master Services Agreement with Accenture contains conflicting dispute resolution clauses: Section 14.2 specifies New York arbitration while Section 22.5 references Delaware courts. Recommend immediate amendment before renewal.",
                "contract_id": "CTR-2024-003",
                "severity": "destructive",
            },
            {
                "title": "Imminent Auto-Renewal — CTR-2024-002",
                "description": "WeWork NYC HQ lease auto-renews for 24 months on Jun 1 unless terminated in writing by May 25. Given 40% office underutilisation post-hybrid-work policy, renegotiation or downsizing is strongly recommended.",
                "contract_id": "CTR-2024-002",
                "severity": "warning",
            },
            {
                "title": "HIPAA BAA Expiry Risk — CTR-2024-088",
                "description": "Business Associate Agreement with MedData Analytics expires Jun 10, 2026. Processing PHI after expiry without a valid BAA constitutes a HIPAA violation carrying penalties up to $1.9M. Renewal must be executed immediately.",
                "contract_id": "CTR-2024-088",
                "severity": "destructive",
            },
            {
                "title": "High-Risk Indemnity Clause — CTR-2026-011",
                "description": "NovaTech MSA (CTR-2026-011) contains an uncapped mutual indemnity clause in Section 9.3 — Acme is exposed to unlimited liability for third-party claims. Standard market cap is 2× annual contract value. Amendment required before execution.",
                "contract_id": "CTR-2026-011",
                "severity": "destructive",
            },
            {
                "title": "Favourable Price Lock — CTR-2024-001",
                "description": "AWS Enterprise Agreement (CTR-2024-001) includes a price protection covenant locking compute rates at May 2024 levels through January 2027 — estimated savings of $340K vs. current list pricing. Renewal is strategically recommended.",
                "contract_id": "CTR-2024-001",
                "severity": "primary",
            },
            {
                "title": "Supply Chain Force Majeure Gap — CTR-2025-227",
                "description": "Foxconn hardware supply agreement lacks a specific pandemic/geopolitical force majeure clause. Given ongoing Taiwan Strait tensions, Acme is exposed to supply disruption without contractual remedy. Recommend addendum before Q3.",
                "contract_id": "CTR-2025-227",
                "severity": "warning",
            },
            {
                "title": "Data Processing Addendum Required — CTR-2025-301",
                "description": "Databricks contract predates the GDPR Article 28 DPA requirement. A Data Processing Addendum must be executed to maintain GDPR compliance for EU workloads processed on the platform.",
                "contract_id": "CTR-2025-301",
                "severity": "warning",
            },
        ],
    }
