---
slug: "ghostnet-the-dead-internet-recovery-engine"
url: "https://devpost.com/software/ghostnet-the-dead-internet-recovery-engine"
title: "GhostNet — The Dead Internet Recovery Engine"
hackathon: "Dev Season of Code "
organization: "DSOC Official"
winner: true
words: 895
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/media_journalism"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# GhostNet — The Dead Internet Recovery Engine

> GhostNet detects link rot (dead/broken web pages), reconstructs lost content using AI forensics from multiple archive sources, and builds a searchable knowledge graph of preserved internet content.

[Devpost](https://devpost.com/software/ghostnet-the-dead-internet-recovery-engine) · hackathon [[Dev Season of Code]]

## Facets

**mechanism** [[cross_origin_web]] [[graph_reasoning]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[media_journalism]] [[supply_logistics]]
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** asyncpg, celery, chrome, common-crawl-index-api, d3.js, docker-compose, extension, fastapi, google-gemini-2.5, langchain, lucide-react, manifest, neo4j, postgresql

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for ghostnet

## Body

Inspiration I've been bookmarking stuff for years — tutorials, blog posts, documentation pages, research links. And every time I go back to check something, half of them are dead. 404. Gone. No cache, no archive, nothing. I looked into it and the numbers are wild. Studies show that about 38% of web pages from 2013 are no longer accessible. Link rot is a real problem and it's getting worse. The Wayback Machine exists, sure, but it's passive — you have to go check manually, and half the time the snapshot is incomplete or missing. I wanted something that actively watches my links, tells me when they're dying, and actually tries to bring them back. That's how GhostNet started. What it does GhostNet is a dead internet recovery engine. Three core things: URL Monitoring — You add URLs to a watchlist. GhostNet continuously checks their health, tracks response times, detects content changes, and flags pages that are degrading or already dead. AI Reconstruction — When a page dies, GhostNet's "Necromancer Engine" kicks in. It pulls real content fragments from the Wayback Machine, Common Crawl, and academic citations. Then it feeds those fragments to Google Gemini, which cross-references everything and rebuilds the original page. Each section gets tagged as verified (from archives), reconstructed (from fragments), or inferred (AI-generated). You get a confidence score so you know how much to trust it. Knowledge Graph — Every monitored URL becomes a node in a Neo4j graph. GhostNet maps how pages link to, cite, and reference each other. You can visualize the entire network, see which nodes are critical (lots of dependents), and predict cascade failures — if one key page dies, what else breaks. How I built it The stack: Backend — FastAPI (Python 3.12) with async everywhere. SQLAlchemy + asyncpg for PostgreSQL. Celery + Redis for background health checks. Neo4j for the knowledge graph. Alembic for migrations. Frontend — React 18 + TypeScript + Vite. Tailwind CSS with a custom dark theme (all gn-* prefixed tokens). D3.js for the graph visualization — nodes have radial gradients, glow filters, and animated particles flowing along edges. Lucide icons throughout. AI/LLM — Google Gemini 2.5 Flash as the primary model, with automatic fallback to Gemini 2.5 Pro, then OpenAI GPT-4o, then Anthropic Claude. Built through LangChain so swapping models is trivial. Archive Sources — The Wayback Machine CDX API for snapshots, Common Crawl index API (with dynamic index discovery so it doesn't break when new crawls drop), and Semantic Scholar for academic citations. Browser Extension — Chrome Manifest V3 extension that scans pages for broken links in real-time and reports them back to the GhostNet backend. Infrastructure — Docker Compose orchestrating PostgreSQL, Redis, Neo4j, MinIO (S3-compatible storage), ChromaDB (vector search), and the app containers. The reconstruction flow looks like this: User clicks "Reconstruct" → Backend fetches fragments from Wayback + Common Crawl + Semantic Scholar → Fragments get cleaned (BeautifulSoup text extraction) → Fragments + URL context sent to Gemini → Gemini returns structured JSON sections with type tags → Confidence scorer calculates overall reliability → Results persisted to PostgreSQL with source attribution → Frontend renders color-coded reconstruction with source panel Challenges I ran into DNS resolution on Windows — My local machine couldn't resolve web.archive.org during development. The Wayback Machine API calls kept failing with getaddrinfo failed . Had to make the archive fetching resilient — graceful fallback to LLM inference when archives are unreachable. SQLAlchemy async gotchas — Ran into MissingGreenlet errors when trying to pass the database session from the API endpoint into the reconstruction service. Async SQLAlchemy doesn't let you lazy-load relationships outside the original coroutine context. Fixed it by running the reconstruction without a DB session, then persisting results back in the endpoint with eager-loaded relationships. Common Crawl index names — I was hardcoding index names like CC-MAIN-2025-08 and getting 404s. Turns out the naming convention isn't sequential — you have to discover available indexes dynamically from their collinfo.json endpoint. Neo4j + PostgreSQL ID mismatch — The frontend sends PostgreSQL UUIDs but Neo4j stores URL strings. Graph queries were returning empty because I was searching Neo4j by UUID. Added a resolution layer that converts UUID → URL before hitting Neo4j. Pydantic v2 namespace conflicts — Had a model_used field on a Pydantic schema that clashed with Pydantic's protected model_ namespace. Small thing but it broke serialization silently. What I learned Async Python is powerful but the ecosystem has sharp edges — especially around SQLAlchemy's async session management. You really have to think about where your coroutine boundaries are. Building a multi-source data aggregation pipeline that's resilient to failures (rate limits, DNS issues, API changes) requires a different mindset than just "call the API and parse the response." Every external call needs a timeout, a retry, and a graceful fallback. D3.js force-directed graphs are deceptively simple to start and incredibly deep to make look good. The particle animation system alone took multiple iterations to get right — decoupling it from the D3 simulation tick so particles loop continuously was the key insight. What's next for GhostNet Scheduled health checks via Celery Beat (currently manual) Vector similarity search with ChromaDB for finding related dead pages Decay prediction model — using check history to predict when a page will die before it actually does Public API so other tools can query GhostNet's reconstruction database Multi-user support with authentication <div