---
slug: "cloudsentinel"
url: "https://devpost.com/software/cloudsentinel"
title: "Incident Copilot"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 1129
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Incident Copilot

> Turn alerts into root cause, citations, and remediation scripts.

[Devpost](https://devpost.com/software/cloudsentinel) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** bash, css, docker, html, javascript, javascript-(es-modules), kubernetes, postgresql, python, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for incident copilot

## Body

Dashboard Cline Anamolies Incidents Logs Similar You.com Inspiration Outages are expensive—enterprises lose an estimated $5.6K–$9K per minute during incidents. Most tools are reactive: they alert you when something is already broken, then you spend precious time searching runbooks, Stack Overflow, and docs to figure out why and how to fix it . We wanted an AI assistant that turns that chaos into a clear path: detect → explain → remediate , with live citations and executable fixes, so developers can act fast instead of guessing. We also wanted to show that sponsor technologies—You.com’s search, Cline’s CLI, Sanity’s structured content, and Akamai’s LKE—fit naturally into a single observability pipeline. Incident Copilot is our proof that these building blocks can power a real “copilot” for incident response. What it does Incident Copilot is an AI-powered observability assistant that: Ingests logs and metrics from your systems. Detects anomalies in real time using statistical baselines (e.g., Z-score). Predicts failure probability (0–100%) so you can act before full outages. Explains root cause in plain language and enriches recommendations with You.com live web search—runbooks, docs, and Stack Overflow with citations. Remediates by generating fix scripts via Cline CLI (e.g., scale replicas, rollback, config). You can view the script or, when enabled, auto-execute it. Learns from resolved incidents: when you submit feedback (success/partial/failed + what you did), the next similar incident surfaces “Learning: similar incident resolved with: …” from the knowledge base. Surfaces “similar past incidents” and “incidents by service” using Sanity (or local DB) as a structured knowledge backend. We deliver this through a real-time dashboard (KPIs, anomalies, incidents, citations, similar incidents), a CLI ( incident-copilot status , anomalies , predict , explain , `r How we built it Stack: Python 3.11+, FastAPI, SQLAlchemy, SQLite (PostgreSQL-ready), vanilla JS modules for the dashboard. All open-source; ML uses scikit-learn/numpy for anomaly and prediction logic. Architecture: Six microservices behind one API gateway: Ingestion (8001) – logs/metrics API and storage Anomaly (8002) – baseline + Z-score detection Prediction (8003) – failure probability Recommendation (8004) – root cause, You.com search, Cline CLI, incident CRUD, feedback, auto-remediation execution Knowledge (8005) – Sanity GROQ (when configured), similar-incidents, incidents-by-service, feedback sync API Gateway (8000) – single entry point, dashboard, static assets, proxy to all services Sponsor integrations: You.com: Called during POST /explain to search for runbooks/docs; results and URLs are returned as citation-backed recommendations. Cline: Invoked in POST /remediate/{id} with incident context (error type, service); returns a remediation script. We added optional auto-execution (opt-in via AUTO_REMEDIATE_EXECUTE_ENABLED ) so the same endpoint can run the script and return stdout/stderr/returncode. Sanity: Knowledge service queries Sanity (GROQ) when SANITY_PROJECT_ID is set; we also keep a local SQLite fallback for similar-incidents and incidents-by-service so the product works without Sanity. Akamai/LKE: One Helm chart deploys to Minikube or Linode Kubernetes Engine; Terraform and deploy scripts for LKE provisioning and CI/CD-friendly deploys. Learning loop: When users resolve an incident or run remediation, they can PATCH /incidents/{id} and POST /incidents/{id}/feedback with outcome and remediation used. That feedback is stored and synced to Knowledge; GET /similar-incidents prioritizes past successes, and the next POST /explain adds a “Learning: similar incident resolved with: …” line to recommendations. Dashboard: Modular CSS/JS (config, state, api, render, ui, app) with auto-refresh, quick actions (Detect, Predict, Create incident, with optional “Auto-remediate on create”), and incident table with Remediate and Execute buttons that call the recommendation service (with optional execution). Challenges we ran into Docker path handling: Services use Path(__file__).parents[2] to find the project root; in Docker the path depth differed and caused IndexError . We fixed it by checking len(parents) >= 3 and falling back to the service directory so the same code works in local and container runs. You.com API: Initial requests failed with “invalid request parameter(s).” We switched to the correct base URL and query parameter format ( https://ydc-index.io/v1/search , query ) and adjusted response parsing for results.web and snippets/descriptions. Cline CLI availability: The Cline CLI isn’t always installed in demo environments. We kept the pipeline working by falling back to a mock script (e.g., sample kubectl commands) when the CLI isn’t present, so the flow and UI still demonstrate the full “remediate + optional execute” behavior. Safety of auto-execution: Running arbitrary remediation scripts (e.g., kubectl) without consent is risky. We made execution opt-in via AUTO_REMEDIATE_EXECUTE_ENABLED and kept the default as “script only”; the API still returns a clear message when execution is requested but disabled. Accomplishments that we're proud of End-to-end flow in one weekend: Ingest → detect → predict → explain (with You.com citations) → remediate (Cline script ± execution) → feedback → “similar incidents” learning, all wired through a single gateway and dashboard. Four sponsor integrations in one product: You.com for live citations, Cline for script generation (and optional execution), Sanity for structured incident knowledge, and LKE/Minikube for deployment—each used in a concrete, demoable way. Learning from resolved incidents: Feedback (outcome + remediation used) is stored and used to improve the next explain; “similar past incidents” and “Learning: similar incident resolved with: …” make the system smarter over time. Auto-remediation execution: Beyond “show script,” we added safe, opt-in execution: POST /remediate/{id}?execute=true and “Auto-remediate on create” in the dashboard, with execution only when AUTO_REMEDIATE_EXECUTE_ENABLED is set. One chart for local and cloud: The same Helm chart runs on Minikube (when LKE isn’t available) and on Linode LKE, with clear docs and scripts for both paths. What we learned API contracts and fallbacks matter: Small differences in base URLs and response shapes (e.g., You.com) can block integration; having mock/fallback behavior (Cline mock, local DB without Sanity) keeps the product demoable and resilient. Environment parity: Path and env assumptions (e.g., parents[2] , DATABASE_URL ) need to be tested in Docker and K8s; defensive checks (path length, env defaults) save time when switching between local and deployed runs. Safety and UX for “auto” features: Auto-execution is powerful but dangerous; an explicit env flag and clear API response when execution is disabled made the feature acceptable for a hackathon and for future production use. Structured content pays off: Using Sanity (and a compatible local schema) for “similar incidents” and “incidents by service” made it straightforward to add the feedback loop and learning recommendations without re-architecting the backend. What's next for Incident Copilot Production hardening: Replace SQLite with PostgreSQL for multi-replica and scale; add auth (API keys / OIDC) and rate limiting on the gateway. Richer remediation: Support more runbook types (e.g., PagerDuty, Opsgenie), approval gates before execution, and dry-run modes that show planned changes without applying them. Observability of the copilot itself: Metrics and tracing for ingestion latency, anomaly-detection delay, and remediation success/failure so operators can tune thresholds and trust the pipeline. SaaS path: Single-cluster free tier; paid tiers for multi-cluster, SSO, and SLA-backed auto-remediation with audit logs—building on the feasibility we demonstrated in the hackathon. <div