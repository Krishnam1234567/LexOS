"""
LexOS — Litigation Prediction API
AI-powered case risk scoring, outcome prediction, and cost forecasting.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import settings
from google import genai

router = APIRouter(prefix="/litigation", tags=["Litigation"])


class LitigationAnalysisRequest(BaseModel):
    case_id: str
    description: str


@router.get("/")
async def get_litigation_data():
    """Get litigation portfolio, risk scores, and AI recommendations."""
    return {
        "summary": {
            "active_cases": 14,
            "high_risk_cases": 4,
            "total_exposure": "$8.6M",
            "avg_win_probability": 69,
            "cases_resolved_ytd": 31,
            "favorable_outcomes": 24,
        },
        "risk_factors": [
            {"subject": "Contractual Breach", "A": 78, "fullMark": 100},
            {"subject": "IP Infringement",    "A": 45, "fullMark": 100},
            {"subject": "Employment",          "A": 32, "fullMark": 100},
            {"subject": "Regulatory",          "A": 61, "fullMark": 100},
            {"subject": "Data Privacy",        "A": 55, "fullMark": 100},
            {"subject": "Antitrust",           "A": 20, "fullMark": 100},
        ],
        "case_outcomes": [
            {"month": "Jan", "won": 4, "settled": 2, "lost": 1},
            {"month": "Feb", "won": 3, "settled": 3, "lost": 0},
            {"month": "Mar", "won": 5, "settled": 1, "lost": 2},
            {"month": "Apr", "won": 6, "settled": 2, "lost": 1},
            {"month": "May", "won": 4, "settled": 4, "lost": 0},
            {"month": "Jun", "won": 7, "settled": 2, "lost": 1},
        ],
        "cost_trend": [
            {"month": "Jan", "projected": 420, "actual": 390},
            {"month": "Feb", "projected": 480, "actual": 460},
            {"month": "Mar", "projected": 350, "actual": 380},
            {"month": "Apr", "projected": 520, "actual": 490},
            {"month": "May", "projected": 610, "actual": 570},
            {"month": "Jun", "projected": 580, "actual": None},
        ],
        "active_cases": [
            {
                "id": "LIT-001",
                "title": "Westbrook Corp vs. Nexus Technologies",
                "type": "Contractual Breach",
                "risk": 72,
                "status": "In Discovery",
                "nextHearing": "Jun 28, 2026",
                "exposure": "$2.4M",
                "winProb": 67,
                "counsel": "Morrison & Foerster",
                "ai_recommendation": "Based on precedent analysis and current discovery status, recommend pursuing early settlement negotiation. Similar cases resolved 40% faster with 23% cost reduction when settled in discovery phase. Confidence: 84%",
            },
            {
                "id": "LIT-002",
                "title": "Patent Infringement – TechVault LLC",
                "type": "IP Dispute",
                "risk": 45,
                "status": "Pre-Trial",
                "nextHearing": "Jul 12, 2026",
                "exposure": "$850K",
                "winProb": 82,
                "counsel": "Wilson Sonsini",
                "ai_recommendation": "Strong prior-art defense identified in USPTO database. Recommend filing IPR petition simultaneously with trial defense to create settlement leverage. Confidence: 88%",
            },
            {
                "id": "LIT-003",
                "title": "Ex-Employee NDA Violation",
                "type": "Employment",
                "risk": 31,
                "status": "Mediation",
                "nextHearing": "Jun 18, 2026",
                "exposure": "$120K",
                "winProb": 91,
                "counsel": "Baker McKenzie",
                "ai_recommendation": "Mediation proceeding favorably. Plaintiff's counsel has signaled willingness to settle at $40-60K. Recommend counter at $45K with confidentiality clause. Expected resolution within 30 days. Confidence: 91%",
            },
            {
                "id": "LIT-004",
                "title": "GDPR Enforcement – EU RegBody",
                "type": "Regulatory",
                "risk": 88,
                "status": "Active",
                "nextHearing": "Jun 22, 2026",
                "exposure": "$5.2M",
                "winProb": 38,
                "counsel": "Linklaters",
                "ai_recommendation": "High-risk regulatory enforcement action. Recommend immediate engagement with DPA to demonstrate remediation steps. Voluntary disclosure of corrective measures could reduce maximum fine by 30-50%. Engage EU regulatory counsel immediately. Confidence: 76%",
            },
        ],
    }


@router.post("/analyze")
async def analyze_case(req: LitigationAnalysisRequest):
    """Get AI analysis for a specific case."""
    if not settings.GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY not configured")
    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        prompt = (
            f"You are a legal AI analyst. Analyze this litigation case and provide:\n"
            f"1. Risk assessment (0-100)\n2. Win probability\n3. Strategic recommendation\n"
            f"4. Estimated cost range\n\nCase ID: {req.case_id}\nDescription: {req.description}\n\n"
            f"Respond in 3-4 sentences, professional legal tone."
        )
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return {"case_id": req.case_id, "analysis": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
