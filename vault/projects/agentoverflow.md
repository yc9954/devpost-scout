---
slug: "agentoverflow"
url: "https://devpost.com/software/agentoverflow"
title: "AgentOverflow"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 667
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# AgentOverflow

> Stack Overflow 2.0: break the prompt spiral-> jump straight to the proven fix.

[Devpost](https://devpost.com/software/agentoverflow) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[web_dom]]

**stack** chrome, gemini, javascript, node.js, python

## How they structured the write-up

- inspiration
- what it does (three buckets)
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for agentoverflow
- share solution json schema

## Body

Flow understanding of how posting a solution works AgentOverflow: Stack Overflow for AI/Agent Problems We’re bringing back our favorite developer tool — Stack Overflow — but rebuilt for the LLM and agent era. Developers waste time and tokens re-solving the same hallucination-driven issues. AgentOverflow captures, validates, and reuses real solutions — so you can break the spiral and ship faster. Inspiration Devs burn time and tokens re-solving identical LLM failures; chat histories vanish, solutions don’t persist. Prompt spirals from hallucinations derail debugging and waste compute. We wanted a portable, structured format so that once a problem is solved, the fix lives forever. What It Does (Three Buckets) 🧩 1) Share JSON One-click “Share Solution” from a Claude share (or any public page). Scrapes, extracts, and assembles a Share Solution JSON — a canonical schema for storing LLM problem–solution pairs. LAVA validates and enforces structure (title, problem, context, technical details, code, tags). User adds short human context in our web app → LAVA re-checks summary alignment → stored + indexed in Elastic. 🔍 2) Find Solution When you’re stuck, click Find Solution . We scrape your current conversation, build a “query JSON,” and run a hybrid Elastic search over validated fixes. Returns ranked, community-verified solutions — you can copy the fix or reuse the exact prompt that worked. ⚙️ 3) Modular Context Protocol (MCP) Our MCP layer pipes structured solutions directly into live LLM sessions. Injects high-signal, low-noise context (code, logs, configs, prior fixes) at runtime. Turns LLMs from passive responders into context-aware problem solvers. How We Built It Chrome Extension (MV3 Side Panel) → captures URL and user action. Node.js Backend → orchestrates scraping and calls LAVA. Playwright Scraper → merges inline JSON ( NEXT_DATA ), DOM + code, shadow DOM, CDP snapshot; falls back to Jina/Readability; optional Bright Data proxy. Normalizer → canonical URLs, solution_id = sha256(canonical_url), de-dupe, preserve raw code. LAVA (Assembler → Validator) → populates schema, enforces required keys, integrates human-context correction. Web App → displays JSON, gathers human validation, saves to DB, indexes to Elasticsearch. MCP Server → injects stored JSON data into future LLM sessions in real time. Challenges We Ran Into Scraping Claude pages — dynamic Next.js + shadow DOM + iframes made extraction tricky. Canonicalization & de-dupe across mirrored URLs. Schema strictness — ensuring no fabricated fields, consistent arrays, and raw code preservation. MV3 plumbing — extension → backend → web app CORS flow. Elastic tuning — balancing vector + keyword recall without over-matching. Accomplishments We’re Proud Of Reliable multi-extractor pipeline that preserves full code context. Seamless extension → web app → DB integration. LAVA’s dual-phase validation (assembler + human-context correction). The Share Solution JSON — a portable format for AI problem–solution memory. Functional Find Solution loop : stuck → match → copy fix → unblocked in seconds. MCP turning static knowledge into live agent context. What We Learned LLM output isn’t reusable knowledge until you add structure and validation. Guardrails prevent hallucination, not just fine-tuning. Human context + schema validation beats auto-summarization. Canonical URLs + hashes create a single source of truth. Small UX choices (side panel, copy button, “open in web app”) dramatically improve adoption. What’s Next for AgentOverflow Team Repos : org-scoped libraries of problem–solution pairs with permissions, versioning, ownership. Better Ranking : success feedback, solve-rate metrics, evaluation signals. Deeper Elastic Integration : vector on code + technical_deep_context, framework-specific synonyms. More Input Channels : ingest Slack, Discord, GitHub issues into the same schema. Quality Gates : automatic spec/API validation before publishing. SDK + API : let any LLM or agent read/write Share Solution JSONs. Share Solution JSON Schema { "solution_id": "", "share_link": "", "type": "", "title": "", "problem": "", "context": "", "technical_description": "", "solution": "", "summary": "", "error_messages": [], "attempted_solutions": [], "code_snippets": [], "technical_deep_context": "", "tags": [], "created_at": "" } #tECHNICAL stACK Extension: Chrome MV3 + Side Panel API Backend: Node.js, Express, Playwright AI Stack: LAVA API + Claude Sonnet 3.5 Search: Elasticsearch Storage: LRU Cache + DB Scraping: Playwright, Jina Reader, Readability, optional Bright Data <div