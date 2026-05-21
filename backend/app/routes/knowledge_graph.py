"""
LexOS — Knowledge Graph API
Legal entity relationships, dependency mapping, and graph data.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import settings
from google import genai

router = APIRouter(prefix="/knowledge-graph", tags=["Knowledge Graph"])


class RelationshipQueryRequest(BaseModel):
    entity_name: str
    context: str


@router.get("/")
async def get_knowledge_graph_data():
    """Get legal knowledge graph nodes, edges, and relationship data."""
    return {
        "summary": {
            "total_nodes": 247,
            "total_relationships": 1038,
            "high_risk_links": 18,
            "documents_indexed": 891,
        },
        "nodes": [
            {"id": "n1", "label": "Master SaaS Agreement",  "sublabel": "Acme Corp",       "type": "contract",   "x": 300, "y": 100, "risk": "low",    "icon": "📄"},
            {"id": "n2", "label": "GDPR DPA",               "sublabel": "EU Operations",    "type": "regulation", "x": 580, "y": 80,  "risk": "high",   "icon": "⚖️"},
            {"id": "n3", "label": "IP License",             "sublabel": "Patent Pool A",    "type": "contract",   "x": 120, "y": 220, "risk": "medium", "icon": "🔗"},
            {"id": "n4", "label": "Employment Agreement",   "sublabel": "Key Personnel",    "type": "entity",     "x": 480, "y": 250, "risk": "low",    "icon": "👥"},
            {"id": "n5", "label": "Subsidiary",             "sublabel": "LexOS EU BV",      "type": "entity",     "x": 300, "y": 360, "risk": "medium", "icon": "🏢"},
            {"id": "n6", "label": "SOC 2 Type II",          "sublabel": "Compliance",       "type": "compliance", "x": 140, "y": 380, "risk": "low",    "icon": "🛡️"},
            {"id": "n7", "label": "Litigation",             "sublabel": "Westbrook Case",   "type": "litigation", "x": 550, "y": 380, "risk": "high",   "icon": "⚠️"},
            {"id": "n8", "label": "Indemnification",        "sublabel": "Clause A-7",       "type": "clause",     "x": 420, "y": 480, "risk": "medium", "icon": "📋"},
        ],
        "edges": [
            {"from": "n1", "to": "n2", "label": "governed by"},
            {"from": "n1", "to": "n3", "label": "licenses"},
            {"from": "n1", "to": "n4", "label": "employs"},
            {"from": "n2", "to": "n5", "label": "applies to"},
            {"from": "n5", "to": "n6", "label": "certified by"},
            {"from": "n4", "to": "n7", "label": "involved in"},
            {"from": "n7", "to": "n8", "label": "invokes"},
            {"from": "n1", "to": "n8", "label": "contains"},
        ],
        "relationships": [
            {"id": "R-001", "from": "Master SaaS Agreement (Acme Corp)",  "to": "GDPR Data Processing Agreement",    "relation": "Governed By",    "type": "regulatory",   "risk": "high"},
            {"id": "R-002", "from": "Master SaaS Agreement (Acme Corp)",  "to": "IP License – Patent Pool A",        "relation": "Licenses",       "type": "contractual",  "risk": "medium"},
            {"id": "R-003", "from": "GDPR DPA",                          "to": "LexOS EU BV",                       "relation": "Binds Entity",   "type": "corporate",    "risk": "high"},
            {"id": "R-004", "from": "Employment Agreement",              "to": "Westbrook Litigation",              "relation": "Evidence In",    "type": "litigation",   "risk": "high"},
            {"id": "R-005", "from": "Indemnification Clause A-7",        "to": "Westbrook Litigation",              "relation": "Defense Basis",  "type": "litigation",   "risk": "medium"},
            {"id": "R-006", "from": "LexOS EU BV",                       "to": "SOC 2 Type II",                     "relation": "Certified Under","type": "compliance",   "risk": "low"},
        ],
    }


@router.post("/query")
async def query_relationships(req: RelationshipQueryRequest):
    """AI-powered legal relationship query."""
    if not settings.GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY not configured")
    try:
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        prompt = (
            f"You are a legal knowledge graph expert. Analyze legal relationships for: {req.entity_name}\n"
            f"Context: {req.context}\n\n"
            f"Identify: key legal dependencies, risk propagation paths, and recommended actions. 3-4 sentences."
        )
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return {"entity": req.entity_name, "analysis": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
