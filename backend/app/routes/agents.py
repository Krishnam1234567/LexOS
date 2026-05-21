from fastapi import APIRouter, HTTPException
from app.schemas.agents import AgentsResponse
from app.schemas.chat import ChatRequest, ChatResponse
from app.config import settings
from google import genai

router = APIRouter(prefix="/agents", tags=["AI Agents"])

@router.get("/", response_model=AgentsResponse)
async def get_agents_data():
    """Get AI Agents activity, metrics, and approval queues with rich virtual data."""
    return {
        # ── Summary KPIs ─────────────────────────────────────────────────────
        "active_agents": 5,
        "total_agents": 8,
        "tasks_completed_month": 7284,
        "pending_approval": 4,

        # ── Agent Registry ────────────────────────────────────────────────────
        "agents": [
            {
                "id": 1,
                "name": "Compliance Agent",
                "description": "Continuously monitors 12 regulatory frameworks (GDPR, CCPA, SOC 2, HIPAA, ISO 27001, PCI DSS, and more), auto-triggers alerts on new amendments, and generates compliance gap reports.",
                "status": "active",
                "tasksCompleted": 2341,
                "lastAction": "1 min ago",
                "confidence": 98,
            },
            {
                "id": 2,
                "name": "Contract Agent",
                "description": "Reviews and analyses every incoming contract using NLP clause extraction. Flags jurisdiction conflicts, risky indemnity clauses, and auto-renewal traps. Manages end-to-end contract lifecycle.",
                "status": "active",
                "tasksCompleted": 3127,
                "lastAction": "3 mins ago",
                "confidence": 97,
            },
            {
                "id": 3,
                "name": "Filing Agent",
                "description": "Automates legal filings across Delaware, California, UK Companies House, MAS Singapore, and EU jurisdictions. Tracks deadlines, prepares documents, and submits via integrated APIs.",
                "status": "active",
                "tasksCompleted": 812,
                "lastAction": "22 mins ago",
                "confidence": 95,
            },
            {
                "id": 4,
                "name": "Litigation Risk Agent",
                "description": "Predicts litigation probability using historical case data, clause patterns, and jurisdictional precedents. Monitors 28 active legal disputes and scores each by financial exposure.",
                "status": "active",
                "tasksCompleted": 634,
                "lastAction": "45 mins ago",
                "confidence": 93,
            },
            {
                "id": 5,
                "name": "Governance Agent",
                "description": "Manages board resolutions, director conflict-of-interest checks, equity cap-table events, and corporate governance workflows. Ensures board-level decisions are fully documented and traceable.",
                "status": "active",
                "tasksCompleted": 189,
                "lastAction": "1 hour ago",
                "confidence": 91,
            },
            {
                "id": 6,
                "name": "Global Expansion Agent",
                "description": "Analyses market-entry legal requirements, entity structuring options, and tax treaty implications for new geographies. Currently tracking potential expansion to Japan, UAE, and Brazil.",
                "status": "idle",
                "tasksCompleted": 97,
                "lastAction": "3 hours ago",
                "confidence": 89,
            },
            {
                "id": 7,
                "name": "IP & Trademark Agent",
                "description": "Manages intellectual property portfolio across 7 jurisdictions — tracks filing deadlines, conducts freedom-to-operate searches, and monitors competitor IP activity.",
                "status": "idle",
                "tasksCompleted": 43,
                "lastAction": "5 hours ago",
                "confidence": 90,
            },
            {
                "id": 8,
                "name": "Due Diligence Agent",
                "description": "Performs automated M&A and vendor due diligence — scans corporate structure, litigation history, UCC filings, sanctions lists, and financial covenants. Currently assigned to 2 active targets.",
                "status": "idle",
                "tasksCompleted": 41,
                "lastAction": "8 hours ago",
                "confidence": 94,
            },
        ],

        # ── Recent Activity Feed ──────────────────────────────────────────────
        "recent_activity": [
            {"agent": "Contract Agent",      "action": "Identified 4 high-risk indemnity clauses in MSA-2026-114 (Vendor: NovaTech Solutions). Flagged for legal review.", "timestamp": "2 mins ago",   "type": "alert"},
            {"agent": "Compliance Agent",    "action": "Detected GDPR Article 25 amendment — impact analysis generated. 3 data-processing workflows flagged for policy update.", "timestamp": "8 mins ago",   "type": "alert"},
            {"agent": "Filing Agent",        "action": "Successfully filed Acme Corporation Q1 Delaware Annual Report. Reference: DEL-2026-AC-00341.",                           "timestamp": "35 mins ago",  "type": "success"},
            {"agent": "Litigation Risk Agent","action": "Updated risk score for Case #LIT-2026-007 (Employment — Jane Roe v. Acme Corp) from Medium to High. Settlement window recommended.", "timestamp": "1 hour ago",   "type": "alert"},
            {"agent": "Contract Agent",      "action": "Completed AI review of 47 new vendor NDAs. 41 auto-approved, 6 escalated for human review.",                           "timestamp": "2 hours ago",  "type": "success"},
            {"agent": "Governance Agent",    "action": "Board resolution for Q2 stock option grant prepared and routed to 7 directors for e-signature. 4/7 signed.",           "timestamp": "3 hours ago",  "type": "info"},
            {"agent": "IP & Trademark Agent","action": "Trademark clearance search completed for 'LexOS' — clear in US, EU, IN, SG, UK. USPTO filing initiated.",              "timestamp": "5 hours ago",  "type": "success"},
            {"agent": "Global Expansion Agent","action": "Japan market-entry legal report generated: KK entity recommended, 14 regulatory checkpoints identified.",            "timestamp": "6 hours ago",  "type": "info"},
            {"agent": "Compliance Agent",    "action": "SOC 2 Type II readiness assessment: 92% ready. 8 control gaps identified with remediation playbooks generated.",       "timestamp": "8 hours ago",  "type": "info"},
            {"agent": "Due Diligence Agent", "action": "Target Company DD (Project Falcon) Phase 1 complete: No sanctions hits, 2 UCC filings flagged, litigation clean.",     "timestamp": "1 day ago",    "type": "success"},
        ],

        # ── Human Approval Queue ──────────────────────────────────────────────
        "approval_queue": [
            {
                "id": 1,
                "agent": "Contract Agent",
                "task": "Auto-renew AWS Enterprise License Agreement (CTR-2024-001) for 3-year term at locked pricing",
                "reasoning": "Contract terms are highly favourable. AWS has guaranteed pricing through 2027 with no service degradation clauses. Usage patterns show 93% capacity utilisation — renewal strongly recommended. No adverse clauses detected.",
                "confidence": 98,
                "impact": "High",
            },
            {
                "id": 2,
                "agent": "Filing Agent",
                "task": "Submit CCPA Annual Privacy Report to California Attorney General (Deadline: Jul 1, 2026)",
                "reasoning": "All required documentation collected and verified. Consumer request logs reconciled. Compliance score 96%. Draft report reviewed by Compliance Agent — no issues. Ready for submission.",
                "confidence": 96,
                "impact": "High",
            },
            {
                "id": 3,
                "agent": "Litigation Risk Agent",
                "task": "Initiate pre-trial settlement offer for Case #LIT-2026-007 (Jane Roe v. Acme Corp) — recommended offer: $85,000",
                "reasoning": "Litigation risk score elevated to 74/100. Plaintiff has strong documentation of alleged wrongful termination. Estimated trial cost: $320K+ over 18 months. Settlement at $85K achieves 73% cost saving and eliminates reputational risk.",
                "confidence": 87,
                "impact": "High",
            },
            {
                "id": 4,
                "agent": "Governance Agent",
                "task": "Execute FY2026 Equity Grant — issue 450,000 stock options to 23 employees at $4.20 strike price",
                "reasoning": "Board pre-approved the option pool expansion in March 2026. 409A valuation completed May 1, 2026 at $4.20/share. All grant recipients verified against cap table. Delaware corporate formalities confirmed.",
                "confidence": 99,
                "impact": "Medium",
            },
        ],
    }


@router.post("/chat", response_model=ChatResponse)
async def chat_with_agent(req: ChatRequest):
    """Chat with the Legal AI Copilot powered by Gemini with conversation history."""
    if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == "your_gemini_api_key_here":
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY is not configured in backend/.env")

    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)

        system_instruction = (
            "You are LexOS, an Enterprise AI Legal Operating System. You are an expert in:\n"
            "- Contract analysis, clause extraction, and risk identification\n"
            "- Global regulatory compliance (GDPR, CCPA, HIPAA, SOC 2, DORA, MAS TRM)\n"
            "- Litigation risk prediction and dispute resolution strategy\n"
            "- Corporate governance, board management, and ESOP\n"
            "- Legal entity structuring and global expansion\n"
            "- Legal analytics, KPI reporting, and cost forecasting\n\n"
            "Be concise (2-4 sentences), precise, and professional. Cite relevant laws where applicable. "
            "If asked about specific contracts or cases in the LexOS system, reference realistic examples."
        )

        # Build conversation string including history
        conversation = f"[System]: {system_instruction}\n\n"
        for msg in (req.history or []):
            role_label = "User" if msg.role == "user" else "LexOS AI"
            conversation += f"[{role_label}]: {msg.content}\n"
        conversation += f"[User]: {req.message}"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation,
        )
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
