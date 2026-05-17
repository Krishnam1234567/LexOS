"""
PostgreSQL connection manager using async SQLAlchemy.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import text

from app.config import settings

engine = create_async_engine(
    settings.postgres_dsn,
    echo=settings.DEBUG,
    pool_size=10,
    max_overflow=20,
)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def check_postgres() -> dict:
    """Ping PostgreSQL and return connection status."""
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT version()"))
            version = result.scalar()
        return {
            "status": "healthy",
            "version": version,
            "host": f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}",
            "database": settings.POSTGRES_DB,
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
        }


async def close_postgres():
    """Dispose the engine connection pool."""
    await engine.dispose()
