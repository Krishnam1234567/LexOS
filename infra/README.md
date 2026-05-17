# LexOS Infrastructure

This directory contains deployment configurations:

```
infra/
├── docker/          # Dockerfiles for individual services
├── k8s/             # Kubernetes manifests (Helm charts / raw YAML)
│   ├── base/        # Base manifests
│   └── overlays/    # Environment-specific patches (dev, staging, prod)
└── scripts/         # Deployment & migration scripts
```

## Quick Start (Local Dev)

From the project root:

```bash
# Start all infrastructure services
docker-compose up -d

# Verify everything is healthy
curl http://localhost:8080/health
```

## Services

| Service    | Port  | Purpose                        |
|------------|-------|--------------------------------|
| PostgreSQL | 5432  | User metadata, org data, RBAC  |
| Neo4j      | 7474/7687 | Legal Knowledge Graph     |
| ChromaDB   | 8000  | Vector store for RAG           |
| Backend    | 8080  | FastAPI API Gateway            |
| Frontend   | 5173  | React/Vite UI                  |
