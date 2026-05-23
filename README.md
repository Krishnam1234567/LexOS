# <p align="center"><img src="https://img.shields.io/badge/LexOS-Legal%20Operating%20System-blue?style=for-the-badge&logo=scala&logoColor=white" alt="LexOS Banner" /></p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-v0.110.0-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/React-v18.3-20232A?style=flat-square&logo=react&logoColor=61DAFB" alt="React" />
  <img src="https://img.shields.io/badge/SQLite-Async-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D7191C?style=flat-square&logo=python&logoColor=white" alt="SQLAlchemy" />
  <img src="https://img.shields.io/badge/Gemini_2.5_Flash-AI_Copilot-8E75C2?style=flat-square&logo=google&logoColor=white" alt="Gemini" />
  <img src="https://img.shields.io/badge/License-Enterprise-000000?style=flat-square" alt="License" />
</p>

<p align="center">
  <strong>The Real-Time Autonomous Legal Intelligence Infrastructure Layer of the AI Economy.</strong>
</p>

<p align="center">
  <i>“LexOS continuously simulates, governs, predicts, and automates the legal reality of an enterprise before risk becomes damage.”</i>
</p>

---

## 🏛️ Core Platform Vision

LexOS is a real-time **Legal Operating System** designed to generate a comprehensive **Legal Digital Twin** for every enterprise. Unlike legacy legal databases or simple contract repositories, LexOS acts as an active, autonomous corporate shield:

*   📖 **Statutory Comprehension** — Continuously ingests, maps, and interprets dynamic regulatory frameworks.
*   🛡️ **Proactive Governance** — Auto-structures board resolutions, ESOP cliffs, and tracks founder risk pools.
*   🔮 **Dispute Forecasting** — Scores litigation probabilities and detects liability leaks.
*   🤝 **Obligation Monitoring** — Traces SLA compliance, renewal options, and vendor exposures.
*   📊 **Decision Simulations** — Pre-simulates cross-border hiring and tax obligations before expansion.

---

## 🏗️ Architecture & Database Design

LexOS utilizes a robust, non-blocking asynchronous pipeline designed for rapid execution and localized data control:

```
                  ┌────────────────────────────────────────┐
                  │          React + Vite Frontend         │
                  │        (Dynamic HSL Dark Mode)         │
                  └───────────────────┬────────────────────┘
                                      │ HTTP Queries
                  ┌───────────────────▼────────────────────┐
                  │          FastAPI API Gateway           │
                  │        (Async Endpoint Router)         │
                  └───────────────────┬────────────────────┘
                                      │ Depends(get_db) injection
                  ┌───────────────────▼────────────────────┐
                  │         SQLAlchemy AsyncEngine         │
                  │       (aiosqlite Database Driver)      │
                  └───────────────────┬────────────────────┘
                                      │ I/O Operations
                  ┌───────────────────▼────────────────────┐
                  │            SQLite File                 │
                  │            (lexos.db)                  │
                  └────────────────────────────────────────┘
```

---

## 📋 Full Product Roster (16 Core Modules)

### 📂 1. Identity & Organization Management
*   **Company Onboarding**: Instant registration with multi-jurisdictional profile creation.
*   **Entity Registration**: Automated legal structuring, corporate registry entries, and hierarchy maps.
*   **Access Control**: Enterprise-grade RBAC/ABAC mappings, SSO integrations, and isolated tenancy.

### 👥 2. Legal Digital Twin Engine
*   **Corporate Mirroring**: An interactive visual twin reflecting subsidiaries, cap tables, and active share ownership.
*   **Obligations & Risk**: Traces litigation exposures, tax risk points, and upcoming milestones.
*   **Geographic Mappings**: Visual country-by-country regulatory matrices detailing tax residency laws.

### ✍️ 3. Contract Intelligence Platform
*   **Adversarial Audits**: AI-powered clause parsing, arbitration risks, and missing liability clause checks.
*   **Negotiation Engine**: Dynamic drafting tools providing redline suggestions and clause comparison charts.
*   **Timeline Tracker**: Active calendar indicators mapping SLA targets, renewal deadlines, and penalty terms.

### 🌐 4. Regulatory Intelligence Engine
*   **Statutory Ingestion**: Automated scanning of government portals, regulatory gazettes, and court decisions.
*   **AI Interpretation**: Direct plain-language summaries detailing exact regulatory impacts.
*   **Policy Bridging**: Bridges upcoming amendments with current internal policies.

### 🤖 5. Compliance Automation Engine
*   **Status Heatmaps**: Live score indicators highlighting current state-wide compliance standings.
*   **Auto-Filing**: Automated drafting, scheduling, and completion of state, labor, and tax filings.
*   **Readiness Auditing**: Chronological logs maintaining ISO 27001 and SOC 2 evidence rosters.

### ⚖️ 6. Litigation Prediction Engine
*   **Clause Scoring**: Rates incoming agreements for litigation risks using clause models.
*   **Counterparty Analytics**: Measures historical dispute records, vendor risks, and partner liabilities.
*   **Safeguard Generator**: Recommends defensive contract terms to prevent litigation before it begins.

### 🌎 7. Jurisdiction Simulation Engine
*   **Market Entry Scans**: Simulates licenses, local corporate structures, and local compliance prior to launch.
*   **Hiring Audits**: Analyzes cross-border labor laws, local benefit policies, and remote hiring compliance.
*   **Data Residency Checks**: Checks cross-border data transfer structures against GDPR, CCPA, and DPDP.

### 🏛️ 8. Governance & Board Intelligence
*   **Board Workflows**: Meeting drafting, resolution workflows, and secure voting trackers.
*   **Option Governance**: Traces ESOP vesting cliff schedules and option allocations.
*   **Policy Control**: Version-controlled corporate policies paired with automatically updated SOPs.

### 👥 9. Autonomous AI Legal Agents
*   🛡️ **Compliance Agent** — Watches rules and identifies internal policy gaps.
*   📂 **Filing Agent** — Drafts corporate registry updates and schedules tax returns.
*   📄 **Contract Agent** — Auto-reviews customer NDAs, SLAs, and MSAs.
*   🏛️ **Governance Agent** — Prepares board resolutions and tracks voting parameters.
*   🌎 **Expansion Agent** — Simulates foreign jurisdictions and payroll rules.
*   📝 **Audit Agent** — Continuously monitors evidence for SOC 2 compliance.
*   ⚖️ **Litigation Agent** — Predicts litigation risks in active disputes.

### 📊 10. Legal Knowledge Graph
*   **Law Graph**: Maps statutory relations, amendment history, and precedents.
*   **Corporate Graph**: Tracks companies, directorship networks, and ownership hierarchies.
*   **Contract Graph**: Maps cross-agreement dependencies and structural conflicts.

### 🔒 11. AI Explainability & Trust Engine
*   **Legal Citation Engine**: Generates precise citations linking all AI outputs back to official laws.
*   **Reasoning Engine**: Provides clear step-by-step logic detailing how AI came to a decision.
*   **Human Review Locks**: Custom approval gates requiring human authorization for high-impact filings.

### 🔌 12. Enterprise Integration Hub
*   **ERP Systems**: SAP, Oracle.
*   **HR Management**: Workday, BambooHR.
*   **CRM Platforms**: Salesforce, HubSpot.
*   **Identity Provider**: Okta, Azure AD.
*   **Enterprise Chat**: Slack, Microsoft Teams.

### 📈 13. Analytics & Executive Intelligence
*   **Executive Dashboard**: High-level visual reports mapping enterprise risks and spend forecasts.
*   **Analytics Hub**: Compliance trajectories, contract distributions, and budget estimations.
*   **Board Reports**: Auto-compiles PDF summaries for executive briefings.

### 🛡️ 14. Security & AI Governance
*   **Identity Verification**: Granular RBAC, MFA access, and SSO security.
*   **AI Guardrails**: Real-time prompt injection defense and hallucination prevention.
*   **Data Security**: End-to-end encryption (AES-256 at rest, TLS 1.3 in transit).

### ⚡ 15. Developer Platform & APIs
*   **API Gateway**: Open API structures mapping all business models.
*   **SDK Libraries**: Developer libraries for Python, Node.js, and Java.
*   **Webhooks**: Real-time event notifications for contract sign-offs and regulatory alerts.

### ⚙️ 16. Infrastructure & DevOps
*   **Orchestration**: Enterprise deployment configs for Kubernetes.
*   **GPU Serving**: Optimized microservice pipelines for localized legal LLM inference.
*   **Observability**: Integrated monitoring stacks for traces, metrics, and logs.

---

## 🧠 AI Core Systems

| AI System | Functionality | Business Purpose |
| :--- | :--- | :--- |
| **Legal LLMs** | Deep legal reasoning & logic parsing | Interprets complex regulations, contracts, and rulings. |
| **RAG Engine** | Semantic retrieval of dynamic laws | Pulls relevant regulatory clauses from vector indices. |
| **Prediction Models** | Quantitative litigation scoring | Analyzes case histories and judge patterns to predict wins. |
| **Graph AI** | Direct relationship mapping | Identifies corporate conflicts of interest and loopholes. |
| **Agentic AI** | Fully autonomous operations | Orchestrates complex filing and audit workflow loops. |
| **Explainable AI** | Precise, source-linked citation logs | Ensures AI outputs are legally defensible and auditable. |

---

## 🎯 Target Personas & Value Loop

### User Personas
*   **CEOs**: Direct visual oversight into enterprise-wide legal vulnerabilities.
*   **CFOs**: Precise compliance cost forecasts and litigation financial modeling.
*   **CLOs & General Counsel**: Direct governance tools, meeting resolutions, and contract evaluations.
*   **HR Teams**: Automated labor compliance audits and cross-border payroll calculations.
*   **Procurement**: Real-time checks for incoming supplier agreements.
*   **Governments / Startups**: National legal infrastructure mapping and global expansion tools.

### Monetization Model
*   **SaaS Subscriptions**: Recurring seat-based license fees.
*   **Enterprise Licenses**: Annual customized deployments.
*   **APIs**: Usage billing by data transaction.
*   **Government Deployments**: Structural infrastructure contracts.
*   **Marketplace**: Commissions on third-party plugin integrations.

---

## 🛠️ Developer Runbook (Local Setup)

### Prerequisites
*   Python 3.12+ (or 3.13)
*   Node.js 20+

### 1. Launching the Backend (FastAPI)
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Gemini API key in your `.env` configuration:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
4. Boot the FastAPI API server:
   ```bash
   uvicorn app.main:app --reload --port 8080
   ```
   *Note: On startup, LexOS automatically creates a local `lexos.db` SQLite database file and seeds it with comprehensive enterprise mock datasets.*

### 2. Launching the Frontend (React + Vite)
1. Move to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Boot the React development server:
   ```bash
   npm run dev
   ```
4. Access the web interface at **`http://localhost:5173`**!

---

## 🎯 What LexOS Is and Is Not

*   ❌ **LexOS is NOT**: A law firm, a basic PDF document manager, or just another simple contract template tool.
*   ✅ **LexOS IS**: A **Real-Time Autonomous Legal Intelligence Infrastructure Layer**.

**It becomes the legal nervous system and predictive governance shield of the modern AI economy.**

---

**Built for the AI economy.** 🏛️
