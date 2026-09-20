---
slug: "medsearch-53okmp"
url: "https://devpost.com/software/medsearch-53okmp"
title: "MedSearch AI"
hackathon: "AI Accelerate: Unlocking New Frontiers"
organization: "Google"
winner: true
words: 610
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/clinician"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# MedSearch AI

> MedSearch AI turns 20 hours of medical research into 20 seconds. Multi-agents search PubMed/ClinicalTrials/FDA using Elasticsearch+Vertex AI to deliver cited answers (>95% accuracy) in <3s.

[Devpost](https://devpost.com/software/medsearch-53okmp) · hackathon [[AI Accelerate- Unlocking New Frontiers]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[supply_logistics]]
**user** [[clinician]] [[general_public]] [[patient_family]]
  <sub>weak: researcher</sub>
**substrate** [[code_repository]] [[document_pdf]] [[sensor_telemetry]] [[video_visual]]

**stack** elasticsearch, fastapi, gemini, google, langchain, nextjs, python, shadcn, tailwind, vertexai, virtualmachine, websockets

## How they structured the write-up

- inspiration: clinicians and researchers drown in information: millions of papers and trials, scattered across systems, with little time to read
- what it does: multi‑agent medical research assistant that:
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for medsearch

## Body

Inspiration: Clinicians and researchers drown in information: millions of papers and trials, scattered across systems, with little time to read Traditional search misses semantically related content and offers no confidence or citation guarantees We wanted an assistant that thinks like a medical research resident: find the right evidence, connect it, and present it clearly with citations Elastic’s hybrid search plus Google Cloud Vertex AI felt like the fastest path to production-grade relevance and scale Personal motivation: reduce the hours clinicians spend hunting for answers so they can spend more time with patients What it does: Multi‑agent medical research assistant that: Understands intent (research vs. clinical vs. drug safety) and searches the right sources Runs hybrid retrieval (BM25 + vector) across PubMed, ClinicalTrials.gov, and FDA drugs Streams a synthesized, citation‑backed answer in under 3 seconds Shows per‑claim citations with titles, phases, and dates for quick verification Uses answerability guards to avoid hallucinations when evidence is weak Falls back to curated mock data if Elasticsearch or embeddings fail, so users still get cited answers Live, production‑style app with a clean UI and real‑time progress indicators How we built it Frontend: Next.js 15 (TypeScript), Tailwind, shadcn/ui; WebSocket UI for real‑time progress and streaming Backend: FastAPI (Python 3.11), LangGraph 0.2.x + LangChain 0.3.x for multi‑agent orchestration Search: Elasticsearch 8.15 hybrid search with per‑source indices and tailored BM25 field boosts (e.g., warnings/adverse_reactions for drug queries) AI: Google Vertex AI gemini-embedding-001 for semantic vectors gemini-2.5-flash (with escalation to gemini-2.5-pro) for synthesis and utility prompts Systems: Redis cache for embeddings/results, Nginx reverse proxy, WebSocket streaming; deployed on Google Compute Engine (e2-standard-2) Techniques: Intent‑aware query expansion for medical terminology Answerability guard with coverage scoring before synthesis Resilient fallback patterns (ES errors → curated mock data) and “degraded mode” startup Challenges we ran into “Zero results” incidents due to brittle exception paths returning empty lists despite fallback data being available Irrelevant drug answers until we: Added intent‑aware query expansion Tuned BM25 boosts on domain‑specific fields (e.g., adverse reactions) Introduced answerability guard thresholds A sneaky zero‑width space (U+200B) causing a Python SyntaxError in production Docker Compose references in docs vs. reality (manifests managed on the VM, not in repo) causing setup confusion WebSocket stability and TLS termination through Nginx while preserving low latency Git push hiccups during final docs updates; switched to SSH remote and resolved Accomplishments that we're proud of End‑to‑end, production‑like system that transforms 20 hours of research into a 20‑second cited answer 95%+ citation alignment in our tests; honest “insufficient evidence” responses when needed Sub‑3‑second streaming answers with clear, readable citations and progress updates Robust resilience: degraded mode and mock fallbacks keep the experience usable during outages Practical relevance tuning: index‑specific BM25 fields and smart query expansion materially improved outcomes Clear, accurate documentation and screenshots aligned with the current codebase What we learned Relevance is a full‑stack problem: intent classification, retrieval tuning, and synthesis guards all matter Domain‑specific BM25 boosts and targeted query expansion drastically reduce irrelevant results Build for failure: degraded mode, fallbacks, and caches keep UX stable despite transient errors WebSocket + Nginx + TLS requires careful configuration for reliability at low latency Keep docs ruthlessly up‑to‑date with the actual system (models, versions, infra) to reduce onboarding friction What's next for MedSearch Scale data coverage: expand PubMed/ClinicalTrials ingestion and add guideline repositories Clinician‑friendly features: PICO‑style query builder, saved searches, export to PDF/Notion Stronger safety: more granular answerability metrics, contradiction checks, and bias audits Human‑in‑the‑loop: one‑click feedback to refine retrieval and synthesis over time Deeper reasoning: selective escalation to gemini‑2.5-pro for complex clinical questions Observability: retrieval quality dashboards, latency/cost analytics, and eval harnesses Enterprise readiness: role‑based access, fine‑grained auditing, and stricter privacy controls (no PHI) <div