"""
LexOS — API Gateway
Enterprise AI Legal Operating System

Main FastAPI application entry point.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
# from app.db.postgres import close_postgres
# from app.db.neo4j import close_neo4j
# from app.routes.health import router as health_router
from app.routes.dashboard import router as dashboard_router
from app.routes.digital_twin import router as digital_twin_router
from app.routes.contracts import router as contracts_router
from app.routes.compliance import router as compliance_router
from app.routes.agents import router as agents_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage startup/shutdown lifecycle."""
    # ── Startup ───────────────────────────────
    print(f"START {settings.APP_NAME} v{settings.APP_VERSION} starting...")
    print(f"   PostgreSQL -> {settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}")
    print(f"   Neo4j      -> {settings.NEO4J_URI}")
    print(f"   ChromaDB   -> {settings.chroma_url}")

    yield

    # ── Shutdown ──────────────────────────────
    print(f"STOP {settings.APP_NAME} shutting down...")
    # await close_postgres()
    # await close_neo4j()


app = FastAPI(
    title=settings.APP_NAME,
    description=(
        "AI-powered Legal Operating System — API Gateway.\n\n"
        "Creates a Legal Digital Twin for every enterprise by continuously "
        "simulating, governing, predicting, and automating legal reality."
    ),
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# ── CORS ──────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite dev + fallback
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ───────────────────────────────────
# app.include_router(health_router)
app.include_router(dashboard_router)
app.include_router(digital_twin_router)
app.include_router(contracts_router)
app.include_router(compliance_router)
app.include_router(agents_router)


@app.get("/", tags=["root"])
async def root():
    """Landing endpoint — confirms the API gateway is running."""
    return {
        "platform": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "message": "Legal Digital Twin Engine — Online",
        "docs": "/docs",
    }
