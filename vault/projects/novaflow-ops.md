---
slug: "novaflow-ops"
url: "https://devpost.com/software/novaflow-ops"
title: "NovaFlow Ops"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 585
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "domain/scientific_research"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# NovaFlow Ops

> Nova 2 Lite plans, Titan Embeddings grounds (RAG), and Playwright executes, producing auditable evidence (logs + screenshots).

[Devpost](https://devpost.com/software/novaflow-ops) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[retail_commerce]] [[scientific_research]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** bedrock, boto3, docker, dynamodb, fastapi, next.js, nova2, novaact, python, react, s3, tailwind, uvicorn

## How they structured the write-up

- inspiration
- what it does
- why it matters
- how we built it
- security and controls
- challenges we ran into
- accomplishments
- what we learned
- what's next

## Body

Inspiration Small teams lose hours every week doing repetitive browser-based operations: updating settings across dashboards, copying data between tools, logging into admin portals, and executing workflows where APIs are limited or inconsistent. We wanted a system that turns a plain-English request into real browser work that is verifiable , not hand-wavy. Most “AI agents” fail at trust: they hallucinate or they act without proof. NovaFlow Ops was designed to fix that. What it does NovaFlow Ops converts a natural-language task into a deterministic execution plan and runs it in a real browser session with auditable evidence. Plan (Amazon Nova 2 Lite) Nova 2 Lite performs planning + reasoning and outputs a bounded JSON plan made of simple UI primitives (click, type, wait, assert, screenshot). This keeps execution controllable and predictable. Retrieve context (Amazon Titan Text Embeddings v2) A “Brand Kit” (docs, policies, examples) is indexed using Titan Embeddings v2. For each task, the system retrieves the most relevant context (RAG) to ground planning and reduce hallucinations. Execute (Playwright) The plan is executed step-by-step in a real Chromium browser session using Playwright. Each step is atomic and produces structured output. Auditable output (logs + screenshots) Every run generates: Structured execution logs (timeline, step metadata, outcomes) Evidence screenshots saved as artifacts and served via API Results are inspectable and reproducible, not “trust me bro”. Why it matters NovaFlow Ops is built for the reality of business ops: lots of tools, weak APIs, repeated manual work, and the need for traceability. Operational efficiency : reduces time spent on repetitive web ops work. Auditability & governance : every action is logged and backed by evidence screenshots. Safer agent execution : bounded DSL, URL controls, and configurable policies. Reproducible deployment : mock mode enables consistent demos and local dev without AWS dependencies. How we built it Frontend (Next.js 16) : a simple dashboard to submit tasks and review run logs/screenshots. Backend (FastAPI) : orchestration for retrieval (RAG), planning, and step execution. Provider modes : NOVA_PROVIDER=bedrock : real AWS Bedrock ( Nova 2 Lite + Titan embeddings ) NOVA_PROVIDER=mock : deterministic local planner + embeddings for offline reproducibility Core mapping (clear and explicit) Nova 2 Lite = planning / reasoning of the agent Titan Embeddings v2 = retrieval (RAG) Playwright = verifiable execution Output = auditable ( logs + screenshots ) Security and controls Agentic workflows are risky if they can navigate anywhere. NovaFlow Ops includes practical safeguards: Starting URL policy ( STARTING_URL_MODE ) with allowlist support URL sanitization and SSRF protections A strict runner DSL: one primitive action per step (no arbitrary code execution) Challenges we ran into Reliability : UI automation can be fragile, so we enforced deterministic flows and strict step boundaries. Trust : we made logs + screenshot artifacts first-class output. Security : we restricted navigation via allowlists and SSRF checks. Accomplishments End-to-end pipeline: task → RAG → plan → Playwright execution → logs + screenshot evidence Clean separation of responsibilities: Nova 2 Lite = planning/reasoning Titan Embeddings v2 = retrieval (RAG) Playwright = verifiable execution Fully auditable runs with evidence artifacts accessible via API Mock mode for reproducible demos without AWS What we learned RAG improves consistency, but auditability is what builds trust . Bounded execution primitives outperform “fully autonomous” agents in reliability. Governance and observability matter more than flashy autonomy in real systems. What's next More execution primitives and workflow templates for common ops tasks Role-based approvals for sensitive actions (publish/update/delete) Richer observability dashboard and run analytics Additional connectors (CRM, ticketing, e-commerce admin panels) <div