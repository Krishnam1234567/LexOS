"""
LexOS — Global Expansion Simulator API
Jurisdiction analysis, legal readiness, and market-entry requirements.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import settings
from google import genai

router = APIRouter(prefix="/expansion", tags=["Global Expansion"])


class ExpansionAnalysisRequest(BaseModel):
    jurisdiction: str
    business_description: str


@router.get("/")
async def get_expansion_data():
    """Get global expansion simulator with jurisdiction readiness data."""
    return {
        "jurisdictions": [
            {
                "code": "EU",
                "name": "European Union",
                "flag": "🇪🇺",
                "status": "active",
                "readiness": 82,
                "regulations": ["GDPR", "AI Act", "DSA", "DMA"],
                "risks": [
                    {"label": "Data Privacy", "level": "high"},
                    {"label": "AI Compliance", "level": "medium"},
                    {"label": "Tax Complexity", "level": "high"},
                ],
                "timeline": "4–6 months",
                "cost": "$320K",
                "score": [
                    {"subject": "Legal", "A": 78},
                    {"subject": "Tax", "A": 55},
                    {"subject": "Labor", "A": 85},
                    {"subject": "IP", "A": 90},
                    {"subject": "Data", "A": 42},
                    {"subject": "Corp", "A": 70},
                ],
                "tasks": [
                    {"done": True,  "text": "GDPR Data Processing Agreement drafted"},
                    {"done": True,  "text": "EU Entity formation (Netherlands BV)"},
                    {"done": False, "text": "AI Act compliance assessment"},
                    {"done": False, "text": "VAT registration in 5 member states"},
                    {"done": False, "text": "Employment contracts — local law review"},
                ],
                "ai_insight": "GDPR and the new AI Act present significant compliance hurdles. Consider a Netherlands BV structure for tax efficiency and EU passporting benefits.",
            },
            {
                "code": "SG",
                "name": "Singapore",
                "flag": "🇸🇬",
                "status": "planning",
                "readiness": 65,
                "regulations": ["PDPA", "MAS Guidelines", "Companies Act"],
                "risks": [
                    {"label": "Licensing", "level": "medium"},
                    {"label": "Data Transfer", "level": "low"},
                    {"label": "FX Controls", "level": "low"},
                ],
                "timeline": "2–3 months",
                "cost": "$85K",
                "score": [
                    {"subject": "Legal", "A": 88},
                    {"subject": "Tax", "A": 79},
                    {"subject": "Labor", "A": 82},
                    {"subject": "IP", "A": 85},
                    {"subject": "Data", "A": 68},
                    {"subject": "Corp", "A": 91},
                ],
                "tasks": [
                    {"done": True,  "text": "PDPA compliance gap analysis"},
                    {"done": False, "text": "Singapore Pte Ltd incorporation"},
                    {"done": False, "text": "MAS AI guidelines review"},
                    {"done": False, "text": "Employment Pass applications"},
                ],
                "ai_insight": "Singapore offers the most favorable regulatory environment. Recommend prioritizing expansion here before India for faster market entry.",
            },
            {
                "code": "IN",
                "name": "India",
                "flag": "🇮🇳",
                "status": "research",
                "readiness": 41,
                "regulations": ["DPDP Act", "IT Act", "FEMA", "Companies Act"],
                "risks": [
                    {"label": "Regulatory Flux", "level": "high"},
                    {"label": "IP Enforcement", "level": "medium"},
                    {"label": "FDI Restrictions", "level": "medium"},
                ],
                "timeline": "6–9 months",
                "cost": "$140K",
                "score": [
                    {"subject": "Legal", "A": 55},
                    {"subject": "Tax", "A": 48},
                    {"subject": "Labor", "A": 62},
                    {"subject": "IP", "A": 58},
                    {"subject": "Data", "A": 35},
                    {"subject": "Corp", "A": 52},
                ],
                "tasks": [
                    {"done": False, "text": "DPDP Act readiness assessment"},
                    {"done": False, "text": "FDI structure — FEMA compliance"},
                    {"done": False, "text": "Indian subsidiary incorporation"},
                    {"done": False, "text": "GST registration and compliance"},
                    {"done": False, "text": "Local counsel engagement"},
                ],
                "ai_insight": "Regulatory environment is in flux with DPDP Act implementation. Wait 2 quarters for clarity before committing capital.",
            },
            {
                "code": "US",
                "name": "United States",
                "flag": "🇺🇸",
                "status": "active",
                "readiness": 94,
                "regulations": ["CCPA", "SOX", "HIPAA", "State Laws"],
                "risks": [
                    {"label": "State Patchwork", "level": "medium"},
                    {"label": "Litigation", "level": "high"},
                    {"label": "Employment", "level": "medium"},
                ],
                "timeline": "1–2 months",
                "cost": "$45K",
                "score": [
                    {"subject": "Legal", "A": 95},
                    {"subject": "Tax", "A": 88},
                    {"subject": "Labor", "A": 80},
                    {"subject": "IP", "A": 97},
                    {"subject": "Data", "A": 75},
                    {"subject": "Corp", "A": 96},
                ],
                "tasks": [
                    {"done": True,  "text": "Delaware C-Corp formation"},
                    {"done": True,  "text": "CCPA compliance program"},
                    {"done": True,  "text": "IP portfolio registration"},
                    {"done": False, "text": "Multi-state employment compliance"},
                ],
                "ai_insight": "US operations are mature. Focus on multi-state employment compliance and state-level privacy law monitoring.",
            },
        ],
        "cost_comparison": [
            {"name": "EU",        "cost": 320, "time": 5},
            {"name": "Singapore", "cost": 85,  "time": 2.5},
            {"name": "India",     "cost": 140, "time": 7.5},
            {"name": "USA",       "cost": 45,  "time": 1.5},
        ],
    }


@router.post("/analyze")
async def analyze_jurisdiction(req: ExpansionAnalysisRequest):
    """AI-powered jurisdiction expansion analysis."""
    if not settings.GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY not configured")
    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        prompt = (
            f"You are a global legal expansion advisor. Analyze expansion into {req.jurisdiction} for: {req.business_description}\n\n"
            f"Provide: 1) Key legal requirements, 2) Major risks, 3) Recommended entity structure, 4) Timeline estimate.\n"
            f"Be concise and practical. 4-5 sentences max."
        )
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return {"jurisdiction": req.jurisdiction, "analysis": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
