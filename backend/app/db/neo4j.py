"""
Neo4j connection manager using the official async driver.
"""

from neo4j import AsyncGraphDatabase

from app.config import settings

_driver = None


def get_neo4j_driver():
    """Lazy-initialize the Neo4j async driver."""
    global _driver
    if _driver is None:
        _driver = AsyncGraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD),
        )
    return _driver


async def check_neo4j() -> dict:
    """Ping Neo4j and return connection status."""
    try:
        driver = get_neo4j_driver()
        async with driver.session() as session:
            result = await session.run("RETURN 1 AS ping")
            record = await result.single()
            server_info = await driver.get_server_info()
        return {
            "status": "healthy",
            "server": str(server_info.address),
            "agent": server_info.agent,
            "ping": record["ping"],
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
        }


async def close_neo4j():
    """Close the Neo4j driver."""
    global _driver
    if _driver is not None:
        await _driver.close()
        _driver = None
