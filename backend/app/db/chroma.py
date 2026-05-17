"""
ChromaDB connection manager using httpx for the REST API.
"""

import httpx

from app.config import settings


async def check_chroma() -> dict:
    """Ping ChromaDB heartbeat endpoint and return connection status."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            # Heartbeat
            heartbeat = await client.get(f"{settings.chroma_url}/api/v1/heartbeat")
            heartbeat.raise_for_status()

            # Version
            version_resp = await client.get(f"{settings.chroma_url}/api/v1/version")
            version_resp.raise_for_status()

        return {
            "status": "healthy",
            "host": f"{settings.CHROMA_HOST}:{settings.CHROMA_PORT}",
            "heartbeat": heartbeat.json(),
            "version": version_resp.json(),
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
        }
