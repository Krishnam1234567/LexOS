from fastapi import APIRouter
from app.schemas.digital_twin import DigitalTwinResponse

router = APIRouter(prefix="/digital-twin", tags=["Legal Digital Twin"])

@router.get("/", response_model=DigitalTwinResponse)
async def get_digital_twin_data():
    """Get legal digital twin entity and director data with rich virtual records."""
    return {
        # ── Summary KPIs ──────────────────────────────────────────────────────
        "total_entities": 9,
        "total_jurisdictions": 8,
        "active_directors": 18,
        "legal_exposure": "Medium",

        # ── Legal Entity Registry ─────────────────────────────────────────────
        "entities": [
            # ── Parent ───────────────────────────────────────────────────────
            {
                "id": 1,
                "name": "Acme Corporation (Parent)",
                "type": "C-Corporation",
                "jurisdiction": "Delaware, USA",
                "risk": "low",
            },
            # ── US Subsidiaries ──────────────────────────────────────────────
            {
                "id": 2,
                "name": "Acme Innovation Labs Inc.",
                "type": "C-Corporation",
                "jurisdiction": "California, USA",
                "risk": "low",
            },
            {
                "id": 3,
                "name": "Acme Financial Services LLC",
                "type": "LLC",
                "jurisdiction": "New York, USA",
                "risk": "medium",
            },
            # ── European Entities ────────────────────────────────────────────
            {
                "id": 4,
                "name": "Acme EU Holdings B.V.",
                "type": "Besloten Vennootschap (B.V.)",
                "jurisdiction": "Netherlands (Amsterdam)",
                "risk": "medium",
            },
            {
                "id": 5,
                "name": "Acme UK Limited",
                "type": "Private Limited Company",
                "jurisdiction": "United Kingdom (London)",
                "risk": "low",
            },
            {
                "id": 6,
                "name": "Acme GmbH",
                "type": "Gesellschaft mit beschränkter Haftung",
                "jurisdiction": "Germany (Berlin)",
                "risk": "low",
            },
            # ── APAC Entities ────────────────────────────────────────────────
            {
                "id": 7,
                "name": "Acme APAC Pte Ltd",
                "type": "Private Limited Company",
                "jurisdiction": "Singapore",
                "risk": "high",
            },
            {
                "id": 8,
                "name": "Acme India Private Limited",
                "type": "Private Limited Company",
                "jurisdiction": "India (Mumbai)",
                "risk": "medium",
            },
            # ── Special Purpose / JV ─────────────────────────────────────────
            {
                "id": 9,
                "name": "Acme-TechCorp JV Holdings Ltd.",
                "type": "Joint Venture (50/50)",
                "jurisdiction": "Cayman Islands",
                "risk": "high",
            },
        ],

        # ── Board of Directors & Officers ─────────────────────────────────────
        "directors": [
            # ── C-Suite ──────────────────────────────────────────────────────
            {
                "name": "Jennifer L. Harrington",
                "role": "Chief Executive Officer (CEO)",
                "entities": 7,
                "conflicts": 0,
            },
            {
                "name": "Marcus D. Okafor",
                "role": "Chief Financial Officer (CFO)",
                "entities": 5,
                "conflicts": 0,
            },
            {
                "name": "Dr. Priya Mehta",
                "role": "Chief Technology Officer (CTO)",
                "entities": 3,
                "conflicts": 0,
            },
            {
                "name": "Alice Johnson",
                "role": "General Counsel & Corporate Secretary",
                "entities": 9,
                "conflicts": 1,
            },
            {
                "name": "Samuel K. Brennan",
                "role": "Chief Operating Officer (COO)",
                "entities": 4,
                "conflicts": 0,
            },
            {
                "name": "Vivienne Lau",
                "role": "Chief Compliance Officer (CCO)",
                "entities": 6,
                "conflicts": 0,
            },
            # ── Independent Board Directors ───────────────────────────────────
            {
                "name": "Robert A. Williams",
                "role": "Independent Director / Audit Committee Chair",
                "entities": 2,
                "conflicts": 0,
            },
            {
                "name": "Dr. Fatima Al-Rashidi",
                "role": "Independent Director / Compensation Committee",
                "entities": 2,
                "conflicts": 1,
            },
            {
                "name": "James T. Nakamura",
                "role": "Independent Director / Risk Committee Chair",
                "entities": 3,
                "conflicts": 0,
            },
            {
                "name": "Helena Svensson",
                "role": "Independent Director (EU Rep.)",
                "entities": 2,
                "conflicts": 0,
            },
            # ── Regional / Subsidiary Directors ───────────────────────────────
            {
                "name": "Rajesh Iyer",
                "role": "Managing Director — Acme India Pvt Ltd",
                "entities": 2,
                "conflicts": 0,
            },
            {
                "name": "Sophie Moreau",
                "role": "Director — Acme EU Holdings B.V. / Acme GmbH",
                "entities": 2,
                "conflicts": 0,
            },
            {
                "name": "David Ong Wei Ming",
                "role": "Director — Acme APAC Pte Ltd",
                "entities": 1,
                "conflicts": 1,
            },
            {
                "name": "Thomas J. Fitzgerald",
                "role": "Director — Acme Financial Services LLC",
                "entities": 1,
                "conflicts": 0,
            },
            {
                "name": "Nadia Petrov",
                "role": "Director — Acme UK Limited",
                "entities": 1,
                "conflicts": 0,
            },
            {
                "name": "Huang Wei",
                "role": "JV Representative — Acme-TechCorp JV Holdings",
                "entities": 1,
                "conflicts": 2,
            },
            {
                "name": "Christopher A. Evans",
                "role": "VP Legal & Deputy General Counsel",
                "entities": 5,
                "conflicts": 0,
            },
            {
                "name": "Laura Kim",
                "role": "Associate General Counsel — APAC & India",
                "entities": 3,
                "conflicts": 0,
            },
        ],
    }
