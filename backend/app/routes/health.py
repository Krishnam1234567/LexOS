"""
Health check routes — verifies connectivity to all three data stores.
"""

from fastapi import APIRouter

from app.db.postgres import check_postgres
from app.db.neo4j import check_neo4j
from app.db.chroma import check_chroma

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check():
    """
    Comprehensive health check.
    Pings PostgreSQL, Neo4j, and ChromaDB in parallel and reports
    the aggregate status of the LexOS data infrastructure.
    """
    import asyncio

    pg, neo, chroma = await asyncio.gather(
        check_postgres(),
        check_neo4j(),
        check_chroma(),
    )

    all_healthy = all(
        svc["status"] == "healthy" for svc in [pg, neo, chroma]
    )

    return {
        "platform": "LexOS",
        "status": "operational" if all_healthy else "degraded",
        "services": {
            "postgresql": pg,
            "neo4j": neo,
            "chromadb": chroma,
        },
    }


@router.get("/health/postgres")
async def health_postgres():
    """Individual PostgreSQL health check."""
    return await check_postgres()


@router.get("/health/neo4j")
async def health_neo4j():
    """Individual Neo4j health check."""
    return await check_neo4j()


@router.get("/health/chroma")
async def health_chroma():
    """Individual ChromaDB health check."""
    return await check_chroma()
