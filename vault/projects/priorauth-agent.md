---
slug: "priorauth-agent"
url: "https://devpost.com/software/priorauth-agent"
title: "PriorAuth Agent"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 1166
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/clinician"
  - "user/legal_professional"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
---

# PriorAuth Agent

> A voice-to-submission AI agent that converts a clinician's spoken case into a completed prior authorization in under 3 minutes — replacing a 2-day manual process costing hospitals $262B annually.

[Devpost](https://devpost.com/software/priorauth-agent) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[voice_speech]]
**domain** [[developer_tools]] [[health_clinical]] [[labor_employment]] [[mental_health]]
**user** [[clinician]] [[legal_professional]] [[patient_family]] [[social_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[regulation_legal_text]] [[sensor_telemetry]] [[transcript_audio]]

**stack** amazon-bedrock, amazon-nova-lite, amazon-nova-sonic, amazon-web-services, aws-iam, bedrock-knowledge-base, boto3, flask, nova-act, opensearch-serverless, opentelemetry, playwright, python, server-sent

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments i'm proud of
- what i learned
- built for impact
- what's next

## Body

PriorAuth Agent Inspiration Prior authorization costs U.S. hospitals $262 billion annually in claim denials, and 46% of those denials stem from preventable data entry errors — staff manually keying patient demographics, ICD-10 codes, and clinical justifications into dozens of different payer portals, each with unique UIs and no API standardization. Physicians average 43 PA requests per week, consuming 12 staff hours that could go to patient care. 93% of physicians report PA delays necessary care, and 29% have witnessed a serious adverse event — hospitalization, permanent impairment, or death — tied to PA delays. The key insight behind PriorAuth Agent is that provider-side PA automation is a browser problem, not an API problem . Existing PA solutions require expensive per-payer API integrations. But if a human can fill a web form, an AI agent can fill it too — on any payer portal, without any partnership or API agreement. That reframing is what makes browser-native automation the right approach. What It Does A clinician pastes or speaks a case into the dashboard, and within minutes has a reviewed, ready-to-submit prior authorization package. The multi-agent system executes an end-to-end workflow: Voice Intake — Extracts structured patient demographics, clinical findings, and therapy history from free-form transcript Clinical Coding (Amazon Nova Lite) — Maps ICD-10 and CPT codes via Bedrock Converse API with coding guardrails Policy Retrieval (Bedrock Knowledge Base) — Queries a real RAG pipeline (S3 → OpenSearch Serverless → Titan Embeddings v2) for payer-specific medical necessity criteria, with local JSON fallback Medical Necessity Analysis (Nova Lite + Extended Thinking) — Evaluates criteria, calculates denial risk, generates payer-ready clinical justification narrative Browser Automation (Playwright / Nova Act) — Opens a visible Chromium browser and fills the payer portal form field-by-field Human-in-the-Loop Gate — Pauses workflow, presents structured review snapshot to clinician Portal Submission — Submits only after explicit clinician approval from the cached, reviewed payload The dashboard streams every stage in real time via Server-Sent Events, including trace steps, denial risk score, coding source, and the active orchestrator mode. How I Built It Multi-Agent Orchestration The system runs as a Strands Agents stage graph with seven specialized tool-agents, each backed by Amazon Nova Lite via BedrockModel . The orchestrator factory pattern selects Strands when available and falls back to a legacy in-process orchestrator for resilience. OpenTelemetry spans instrument each stage ( voice_intake , clinical_coding , knowledge_retrieval , medical_necessity , portal_submission ) with business attributes like extended_thinking_used and coding.source . Amazon Nova Integration Points Nova 2 Lite (Bedrock Converse API): Powers ICD-10/CPT code mapping and medical necessity justification generation. Extended thinking mode is enabled by default for justification — the system attempts reasoningConfig first and falls back to standard inference if the model doesn't support it. Nova 2 Sonic ( /api/transcribe demo gateway): Endpoint that accepts audio input and maps to the pipeline entry point. Uses mock transcript for demo; the production path targets amazon.nova-sonic-v1:0 via Bedrock. Full bidirectional streaming is a planned next step. Bedrock Knowledge Base : Real AWS infrastructure — S3 bucket with policy documents, OpenSearch Serverless vector index, IAM role with scoped permissions, Titan Text Embeddings v2 for indexing, and automated ingestion pipeline. The retrieval agent queries the KB for payer-specific PA criteria and scores candidates by payer match, procedure code match, and service keyword overlap. Strands Agents SDK : Seven @tool -decorated functions registered as stage agents with BedrockModel(model_id="amazon.nova-lite-v1:0") . Browser Automation A tri-mode submission adapter supports Playwright (visible Chromium, default), Nova Act (when API key is available), and HTTP adapter (for fast testing). Playwright mode types each field with human-like delay so the browser automation is visually demonstrable. Human-in-the-Loop Safety HITL is a first-class workflow state, not an afterthought. The run pauses at needs_approval , the dashboard presents a structured review snapshot, and the /api/runs/<id>/approve endpoint resumes submission from the cached, already-reviewed payload — bypassing all upstream reasoning to avoid latency and output variability after approval. Engineering Quality Fallback chains : Strands → legacy orchestrator, Bedrock KB → local policies, extended thinking → standard inference, Nova → heuristic coding Coding guardrails : All model-returned ICD-10/CPT codes are validated against clinically plausible ranges before proceeding downstream Type-safe contracts : Protocol-based Bedrock client typing, dataclass DTOs with to_dict() serialization Test coverage : Pipeline extraction, guardrail behavior, KB parsing, HITL approval loop, portal API Challenges I Ran Into KB parsing reliability was the first meaningful hurdle. Bedrock KB chunks can arrive flattened into single-line strings, which breaks line-oriented parsers. I added a normalization pass that reconstructs parseable policy structure before any field extraction runs. Model fallback transparency was a subtler problem. Silent model fallbacks hide runtime behavior in ways that are hard to debug and impossible to demonstrate to judges. I added explicit output fields ( coding.source , retrieval_source , extended_thinking_used ) so the active execution path is always visible in both the dashboard and structured JSON output. HITL determinism was the final key challenge. Re-running the full workflow after clinician approval introduced unnecessary latency and potential variability. I resolved this by having the approval path submit directly from the cached payload — skipping upstream reasoning entirely. Accomplishments I'm Proud Of Three things stand out: the real Bedrock Knowledge Base pipeline with provisioned AWS infrastructure (S3 + OpenSearch Serverless + IAM + ingestion) and graceful local fallback, the HITL design with cached payload resume that avoids re-running reasoning after approval, and the explicit execution traceability — every agent stage surfaces its source, mode, and confidence in structured output so the system is auditable end-to-end. What I Learned In clinical workflows, reliability and observability matter as much as model quality. A system that produces correct results unpredictably, or fails silently, is not deployable. Multi-agent systems require explicit traceability at each stage to be trustworthy. And human approval must be first-class in both backend state and UI — not an afterthought bolted onto an automated pipeline. Built For Impact The providers who benefit most from PA automation are small practices and rural clinics — organizations without dedicated PA staff or IT teams to build custom integrations. A 2-person family practice submitting 20+ PAs per week loses an entire staff position to administrative work. PriorAuth Agent's browser-native approach means it works against any payer portal without per-payer API agreements, which is exactly the constraint that blocks small providers from existing enterprise PA solutions. For patients, the impact is direct: 82% of patients report abandoning treatment because the PA process is too complex. Reducing PA turnaround from days to minutes means fewer patients fall through the cracks between approval and care delivery. The regulatory environment is also moving this direction — CMS-0057 mandates electronic prior authorization by 2027, creating urgency for provider-side automation tools that work across heterogeneous payer systems. What's Next Replace the transcript parser with real Nova 2 Sonic bidirectional voice streaming with async tool calls Add metadata filtering and richer source attribution for Bedrock KB retrieval Integrate Bedrock Guardrails for transcript and justification safety controls Expand payer policy coverage and harden the production telemetry export pipeline <div