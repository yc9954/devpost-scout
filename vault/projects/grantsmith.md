---
slug: "grantsmith"
url: "https://devpost.com/software/grantsmith"
title: "Nebula"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 439
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/scientific_research"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# Nebula

> Nebula is an AI grant-writing copilot powered by Amazon Nova.

[Devpost](https://devpost.com/software/grantsmith) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[retrieval_grounding]] [[structural_withholding]]
**domain** [[developer_tools]] [[scientific_research]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** amazon-web-services, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for nebula

## Body

Landing Page Workflow Pipeline Data Ingestion Draft Generation Nebula Inspiration Nonprofits and small teams spend too much time turning dense RFPs into compliant proposals, and even more time proving every claim with evidence. The hardest part is not drafting text, it is maintaining traceability and complete requirement coverage under deadline pressure. Nebula was built to reduce that risk by turning source documents into citation-backed, compliance-aware drafts teams can trust. What It Does Nebula ingests an RFP and supporting organizational documents, then runs a structured proposal workflow that: extracts requirements into a validated artifact generates section drafts with traceable citations ( doc_id , page , snippet ) computes a coverage matrix ( met | partial | missing ) flags missing evidence before submission exports final outputs as JSON and Markdown Result: faster proposal assembly with auditability built in. How We Built It Nebula uses a modular, production-minded architecture: Frontend: Next.js for upload, workflow controls, and artifact review Backend: FastAPI endpoints for ingestion, retrieval, drafting, coverage, and export Retrieval backbone: deterministic chunking + embeddings + project-scoped similarity retrieval Artifact contracts: strict Pydantic schema validation with repair safeguards Operations baseline: structured logs, request correlation IDs, redaction rules, Docker-first runtime Intelligence path: Amazon Nova models on AWS Bedrock for extraction, drafting, and coverage deterministic orchestration to keep outputs reliable and reproducible clear stage separation for planning, writing, evidence mapping, and compliance checks Challenges We Ran Into Balancing determinism and flexibility: reliable demos vs. better semantic quality Schema reliability: LLM output must validate against strict artifact contracts Citation integrity: every claim must map to retrievable evidence or be marked unsupported Scope discipline: separating must-have trust features from stretch enhancements Submission readiness: proving production Nova usage with concrete technical evidence Accomplishments We’re Proud Of Delivered end-to-end workflow from upload to export with traceable artifacts Implemented citation-first drafting with explicit missing-evidence signaling Enforced schema contracts across requirements, drafts, and coverage outputs Built a reliable execution backbone with health checks and reproducible startup Added security and observability safeguards early, not as post-hoc fixes What We Learned Trust beats verbosity: grounded, cited output is more useful than fluent unsupported text Schema-first design makes AI systems maintainable and testable Agentic behavior works best with narrow responsibilities and deterministic orchestration Documentation quality materially impacts judging confidence Security and observability should be first-pass architecture decisions What’s Next for Nebula Near term: complete internal agentic upgrades while preserving API/UI contracts harden runtime reliability, error handling, and observability keep Nova-on-AWS evidence and submission artifacts synchronized Post-submission: add richer reviewer-mode scoring and feedback workflows expand multimodal evidence ingestion evaluate targeted Nova Act automation paths move from local-first MVP storage to production-grade AWS controls <div