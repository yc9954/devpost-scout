---
slug: "epiq-1ubx5q"
url: "https://devpost.com/software/epiq-1ubx5q"
title: "Epiq"
hackathon: "Google Cloud Rapid Agent Hackathon"
organization: "Google"
winner: true
words: 658
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Epiq

> Intelligent A.I Outbreak Tracker

[Devpost](https://devpost.com/software/epiq-1ubx5q) · hackathon [[Google Cloud Rapid Agent Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[health_clinical]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** cloud, gemini, google, services

## How they structured the write-up

- what it does
- findings & learnings
- mongodb atlas differentiators
- architecture
- tech stack

## Body

Epiq — AI Disease Outbreak Tracker Epiq is a real-time epidemiological intelligence platform. Autonomous AI agents continuously gather active disease-outbreak reports from sources like WHO, CDC, ECDC and PAHO, store them in MongoDB Atlas , and surface them on a live world map with SEIR-based spread forecasting. Select any disease and the system autonomously queries Atlas, synthesises a situation report, and finds clinically similar outbreaks. Built for the MongoDB + Google Cloud hackathon — Atlas is the single source of truth and three Atlas differentiators are used end to end. What it does Epiq monitors active disease outbreaks globally in real time. Every 24 hours a Scraper Agent (Google ADK + Gemini) searches WHO Disease Outbreak News, CDC Health Advisories, ECDC CDTR, PAHO alerts, and ProMED, then upserts structured records into MongoDB Atlas. A Reader Agent answers natural-language questions by issuing live find / aggregate / count queries via the MongoDB MCP Server — every query is streamed into the in-app Activity terminal so users see exactly what the AI is doing. An Orchestrator Agent combines Reader output with a SEIR epidemic model to produce 30, 60, and 90-day spread projections. Atlas Vector Search finds clinically similar diseases by embedding symptom profiles with gemini-embedding-001 and running cosine-similarity search. A native Time Series collection powers a 14-day trend chart. Findings & Learnings MongoDB MCP Server removes the impedance mismatch between LLMs and databases — the agent writes natural queries and the MCP layer executes them against Atlas without custom tool boilerplate. Atlas Vector Search required storing 768-dim embeddings at write time (scrape + seed); once indexed, semantic similarity across disease profiles is a single aggregation pipeline stage. Native Time Series collections enforce append-only semantics cleanly; using timeField + metaField lets the $match + $group trend query stay simple. Separating the MCP path (agents reasoning over data) from the Motor path (fast deterministic UI reads) kept latency acceptable — the map loads instantly while the AI reasoning runs in the background. Google ADK's AgentTool wrapper made composing the Reader into the Orchestrator trivial; the main challenge was prompt engineering to keep the Reader from calling Atlas Admin API tools instead of data query tools. MongoDB Atlas differentiators Feature How Epiq uses it MongoDB MCP Server The Reader Agent (Google ADK + Gemini 2.5 Pro) talks to Atlas through the official mongodb-mcp-server over MCP. On every disease selection it issues real find / aggregate / count calls — each one is streamed live into the in-app Activity terminal . Atlas Vector Search Disease clinical profiles are embedded with gemini-embedding-001 (768-dim) and stored on disease_info.embedding . A $vectorSearch aggregation finds clinically similar outbreaks (e.g. Ebola → Marburg, Lassa), shown as "Similar Patterns". Native Time Series Case/death counts are appended to the outbreaks_timeseries time series collection ( timeField / metaField ). The "14-Day Trend" chart reads them back via a $match + $group aggregation. Architecture flowchart LR UI["React + Vite SPA<br/>(map, SEIR, charts)"] API["FastAPI backend"] subgraph Agents["Google ADK agents (Gemini 2.5 Pro)"] Scraper["Scraper Agent<br/>(Google Search + url_context)"] Reader["Reader Agent"] Orch["Orchestrator + SEIR"] end MCP["mongodb-mcp-server<br/>(MCP)"] Atlas[("MongoDB Atlas<br/>outbreak_tracker")] Gemini["Gemini API<br/>(LLM + embeddings)"] UI -->|"REST /outbreaks /search /read /outbreaks/history"| API API -->|Motor async driver| Atlas API --> Agents Reader -->|find / aggregate| MCP --> Atlas Scraper -->|writes outbreaks + disease_info + time series| Atlas Agents --> Gemini API -->|"embed_text() $vectorSearch"| Atlas Two data paths to Atlas, on purpose: MCP path — agents reason over the database via the MongoDB MCP server (the AI/agent showcase). Motor path — the FastAPI REST endpoints read/write Atlas directly with the async motor driver (fast, deterministic UI data). Collections in outbreak_tracker : outbreaks , disease_info , scrape_history , outbreaks_timeseries . Tech stack Frontend: React, TypeScript, Vite, Tailwind CSS, Leaflet (map), Recharts (charts) Backend: FastAPI, Motor (async MongoDB), APScheduler (24 h scrape job) AI: Google ADK multi-agent system, Gemini 2.5 Pro, gemini-embedding-001 Data: MongoDB Atlas (MCP Server, Vector Search, Time Series) Deploy: Google Cloud Run (single container — see cloudrun-deploy.md ) <div