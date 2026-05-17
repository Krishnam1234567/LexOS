from fastapi import APIRouter
from app.schemas.digital_twin import DigitalTwinResponse

router = APIRouter(prefix="/digital-twin", tags=["Legal Digital Twin"])

@router.get("/", response_model=DigitalTwinResponse)
async def get_digital_twin_data():
    """Get legal digital twin entity and director data."""
    return {
        "total_entities": 5,
        "total_jurisdictions": 5,
        "active_directors": 12,
        "legal_exposure": "Medium",
        "entities": [
            {"id": 1, "name": "Acme Corporation (Parent)", "type": "C-Corp", "jurisdiction": "Delaware, USA", "risk": "low"},
            {"id": 2, "name": "Acme EU Holdings B.V.", "type": "B.V.", "jurisdiction": "Netherlands", "risk": "medium"},
            {"id": 3, "name": "Acme UK Limited", "type": "Limited", "jurisdiction": "United Kingdom", "risk": "low"},
            {"id": 4, "name": "Acme APAC Pte Ltd", "type": "Pte Ltd", "jurisdiction": "Singapore", "risk": "high"},
            {"id": 5, "name": "Acme Innovation Labs Inc.", "type": "C-Corp", "jurisdiction": "California, USA", "risk": "low"},
        ],
        "directors": [
            {"name": "Jane Doe", "role": "CEO", "entities": 3, "conflicts": 0},
            {"name": "John Smith", "role": "CFO", "entities": 2, "conflicts": 0},
            {"name": "Alice Johnson", "role": "General Counsel", "entities": 5, "conflicts": 1},
            {"name": "Bob Williams", "role": "Director", "entities": 2, "conflicts": 0},
        ]
    }
