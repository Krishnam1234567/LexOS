# LexOS

**Enterprise AI Legal Operating System**

> *"LexOS continuously simulates, governs, predicts, and automates the legal reality of an enterprise before risk becomes damage."*

---

## Architecture

```
LexOS/
├── frontend/        → React + Vite (UI)
├── backend/         → FastAPI (API Gateway)
├── ai_services/     → LLM orchestration, RAG, legal reasoning
├── infra/           → Docker, Kubernetes, deployment configs
└── docker-compose.yml
```

## Data Infrastructure

| Service        | Technology | Purpose                                |
|----------------|-----------|----------------------------------------|
| **PostgreSQL** | v16       | User metadata, organizations, RBAC     |
| **Neo4j**      | v5        | Legal Knowledge Graph (laws, entities)  |
| **ChromaDB**   | v0.6      | Vector store for RAG / embeddings       |

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 20+ (for frontend)
- Python 3.12+ (for local backend dev)

### 1. Start Infrastructure
```bash
docker-compose up -d
```

### 2. Verify Health
```bash
curl http://localhost:8080/health
```

### 3. API Docs
Open [http://localhost:8080/docs](http://localhost:8080/docs) for the interactive Swagger UI.

## Development

### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

### Frontend (React/Vite)
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

| Method | Endpoint            | Description                       |
|--------|---------------------|-----------------------------------|
| GET    | `/`                 | Platform info                     |
| GET    | `/health`           | Aggregate health (all 3 DBs)      |
| GET    | `/health/postgres`  | PostgreSQL connectivity            |
| GET    | `/health/neo4j`     | Neo4j connectivity                 |
| GET    | `/health/chroma`    | ChromaDB connectivity              |

---

**Built for the AI economy.** 🏛️
