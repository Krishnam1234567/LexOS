"""
LexOS — Centralized Configuration
Reads from environment variables with sensible local defaults.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application-wide settings loaded from env vars."""

    # ── App ───────────────────────────────────
    APP_NAME: str = "LexOS"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    # ── PostgreSQL ────────────────────────────
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "lexos"
    POSTGRES_PASSWORD: str = "lexos_secret"
    POSTGRES_DB: str = "lexos_db"

    @property
    def postgres_dsn(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # ── Neo4j ─────────────────────────────────
    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "lexos_graph_secret"

    # ── ChromaDB ──────────────────────────────
    CHROMA_HOST: str = "localhost"
    CHROMA_PORT: int = 8000

    @property
    def chroma_url(self) -> str:
        return f"http://{self.CHROMA_HOST}:{self.CHROMA_PORT}"

    # ── AI Models ─────────────────────────────
    GEMINI_API_KEY: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
