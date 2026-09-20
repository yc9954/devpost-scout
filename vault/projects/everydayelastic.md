---
slug: "everydayelastic"
url: "https://devpost.com/software/everydayelastic"
title: "EverydayElastic"
hackathon: "AI Accelerate: Unlocking New Frontiers"
organization: "Google"
winner: true
words: 1119
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# EverydayElastic

> When incidents hit, every second counts—but finding the right runbook, policy, or past ticket wastes critical time.

[Devpost](https://devpost.com/software/everydayelastic) · hackathon [[AI Accelerate- Unlocking New Frontiers]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** elasticsearch, gcp, nextjs, python, slack, typescript, vertexai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- live deployment
- what's next for everydayelastic

## Body

Home Page Chat Page System Architecture Inspiration Organizations today struggle with information overload. Knowledge is scattered across documentation, incident tickets, policies, and runbooks. Teams waste hours searching for the right information during critical incidents, and context-switching between multiple systems slows down response times. We built EverydayElastic to solve this problem: a conversational AI platform that brings together semantic search and generative AI to provide instant, grounded answers with actionable follow-ups. What it does EverydayElastic is an AI-powered knowledge search platform that combines Elasticsearch's semantic search with Google Vertex AI's Gemini models. Users can: Ask natural language questions about their knowledge base (incidents, policies, documentation) Get AI-generated responses grounded in retrieved documents with source citations Take immediate action with suggested follow-ups like posting incident alerts to Slack Search across 7,800+ documents with sub-second latency using hybrid search Key Features: Semantic Search : Hybrid retrieval combining BM25 keyword search and dense vector embeddings Intelligent Reranking : Google Vertex AI reranking ensures the most relevant results surface first Context-Aware Responses : Gemini 2.5 Flash generates grounded answers with citations to prevent hallucination Slack Integration : Automatically detects critical incidents and suggests posting to team channels with rich formatting Conversation Management : Persistent chat history with session management Real-time Interface : Modern React-based UI with markdown rendering and expandable sources Observability Built-in : Prometheus metrics from backend/app/core/metrics.py and OpenTelemetry traces exported via backend/app/dependencies.py into Elastic APM dashboards How we built it Technology Stack Backend (Python) FastAPI : High-performance async web framework for REST API Elasticsearch 8.15 : Semantic search with Open Inference API integration Google Vertex AI : Text generation (Gemini 2.5 Flash Lite), embeddings, and reranking Slack Web API : Rich message formatting with Block Kit OpenTelemetry & Prometheus : Observability and metrics Frontend (TypeScript/React) Next.js 15 : Server-side rendering with App Router Tailwind CSS : Utility-first styling React Markdown : Rendered AI responses with syntax highlighting Lucide Icons : Modern iconography Infrastructure Google Cloud Run : Serverless container deployment Elasticsearch Cloud : Managed cluster with semantic_text mapping Secret Manager : Secure credential management Architecture The system follows a three-tier architecture: User Layer : Web browser and Slack workspace for notifications Application Layer : Frontend (Next.js) handles UI, conversation state, and user interactions Backend (FastAPI) orchestrates search, AI generation, and integrations External Services : Elasticsearch, Vertex AI, and Slack APIs Search Pipeline: User query → Backend extracts keywords and context Elasticsearch performs hybrid search (BM25 + semantic vectors) Vertex AI reranks results by relevance Top 4 documents form context for LLM Gemini generates grounded response with citations Workflows engine suggests follow-up actions (e.g., Slack alerts) Data Flow: Frontend sends POST to /chat/completions with user message Backend queries Elasticsearch using Open Inference API for embeddings Results reranked via Vertex AI Reranking API Context built from top documents and passed to Gemini Response returned with sources and suggested actions User can trigger actions (e.g., post to Slack) via /chat/actions endpoint Implementation Highlights Hybrid Search # Combines keyword (BM25) and semantic (vector) search { "query": { "bool": { "should": [ {"match": {"content": query}}, # BM25 {"semantic": {"field": "content", "query": query}} # Vectors ] } } } Grounded Generation Context from retrieved documents included in system prompt Citations enforced in response format Temperature kept low (0.3) for factual accuracy Slack Integration OAuth-based Web API for rich formatting Block Kit for structured message display Automatic fallback to webhooks if API fails Incident detection based on severity tags Observability Instrumentation Prometheus /metrics endpoint backed by REQUEST_LATENCY and SEARCH_SOURCE_COUNTER in backend/app/core/metrics.py configure_tracing() in backend/app/dependencies.py wires OpenTelemetry OTLP exports (Gemini + Elasticsearch spans) into Elastic APM with environment-driven configuration Challenges we ran into Elasticsearch Open Inference API : Initially struggled with the correct inference endpoint configuration. Required understanding the semantic_text field type and how it integrates with external embedding models. Reranking Integration : Getting Vertex AI reranking to work with Elasticsearch results required proper document formatting and handling of the rerank response structure. Token Context Management : Balancing between providing enough context to the LLM (for accurate responses) while staying within token limits. Solved by limiting to top 4 documents and truncating very long documents. Slack OAuth Tokens : Managing OAuth token refresh and handling expired credentials gracefully. Implemented a fallback mechanism to webhooks when API calls fail. Response Latency : Initial implementation took 5-6 seconds per query. Optimized by: Reducing search result size from 20 to 8 documents Async/await throughout the backend Using Gemini 2.5 Flash Lite instead of Pro Parallel execution where possible Citation Accuracy : Early versions sometimes hallucinated sources. Fixed by: Strict system prompts with citation requirements Lower temperature (0.3) Validating returned citations against actual sources Accomplishments that we're proud of End-to-end Integration : Successfully integrated three major platforms (Elasticsearch, Vertex AI, Slack) into a cohesive system that feels seamless to the end user. Production-Ready Architecture : Built with observability, metrics, structured logging, and proper error handling from day one. Sub-3-Second Response Time : Achieved fast end-to-end latency (2-3 seconds) despite multiple API calls and AI processing. Grounded AI : Zero hallucination issues in testing because all responses are grounded in retrieved documents with citations. Rich Slack Integration : Not just basic text notifications—implemented proper Block Kit formatting with structured incident data. Clean Separation of Concerns : Modular architecture with clear boundaries between search, generation, and actions makes the codebase maintainable and extensible. What we learned Elasticsearch Semantic Search : Deep dive into hybrid search, semantic_text field types, and Open Inference API for embeddings and reranking. Vertex AI APIs : Learned about different Gemini models (Flash vs Pro), function calling, and the importance of prompt engineering for grounded responses. RAG Architecture : Practical experience with Retrieval-Augmented Generation patterns, context window management, and citation handling. Async Python : Leveraged FastAPI's async capabilities for concurrent I/O operations (Elasticsearch + Vertex AI in parallel). Next.js 15 : Worked with the new App Router, Server Components, and modern React patterns. Production Observability : Implemented structured logging, Prometheus metrics, and health check endpoints for monitoring. Live Deployment Backend (Cloud Run) : https://everydayelastic-backend-1064261519338.us-central1.run.app Frontend (Cloud Run) : https://everydayelastic-frontend-1064261519338.us-central1.run.app Quick checks: # Health curl -s https://everydayelastic-backend-1064261519338.us-central1.run.app/health | jq # Slack webhook action (posts to webhook-bound channel) curl -s -X POST "https://everydayelastic-backend-1064261519338.us-central1.run.app/chat/actions" \ -H "Content-Type: application/json" \ -d '{ "action": "slack_webhook", "payload": { "channel": "sev-1-war-room", "message": "Cloud Run webhook test from EverydayElastic", "ticket_info": {"severity":"Sev-1","status":"Investigating","owner":"On-call"} } }' What's next for EverydayElastic Short‑term (2–4 weeks) Streaming responses (SSE) for token‑by‑token replies Query expansion (synonyms, reformulation) to boost recall Conversation memory with session resume Medium‑term (2–3 months) Bi‑directional Slack (slash commands, channel ID lookups) Auto‑escalation rules with PagerDuty handoff Multilingual retrieval + generation Long‑term (6+ months) Function calling to trigger actions (create tickets, update status) Multimodal search (PDF/images with OCR) Analytics + RBAC and audit logs <div