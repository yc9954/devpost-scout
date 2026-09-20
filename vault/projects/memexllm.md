---
slug: "memexllm"
url: "https://devpost.com/software/memexllm"
title: "MemexLLM"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 797
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# MemexLLM

> Your Personal AI assistant

[Devpost](https://devpost.com/software/memexllm) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: graph_reasoning, vision_ocr</sub>
  <sub>weak: developer_tools, education, labor_employment, legal_justice</sub>
**user** [[researcher]]
  <sub>weak: educator_student</sub>
**substrate** [[document_pdf]] [[structured_db]]
  <sub>weak: geospatial, sensor_telemetry</sub>

**stack** docker, fastapi, groq, lamaindex, next.js, posthog, python, sentry

## Body

Inspiration Every researcher knows the pain — hundreds of PDFs, dozens of tabs, and hours lost just finding information you already read somewhere. I watched PhD students spend entire weekends on literature reviews that should take hours. The real problem wasn't a lack of AI tools — it was that existing tools hallucinated, gave uncited answers, and weren't built around academic workflows. NotebookLM was the closest thing, but it lacked hybrid search, knowledge visualization, and self-hosting for privacy-sensitive research. I wanted to build something that treated citations as a first-class feature, not an afterthought. ** What it does** MemexLLM is a production-ready document intelligence platform that lets you chat with your entire research library and get fully cited, hallucination-free answers in seconds. Upload 50+ formats — PDFs, YouTube videos, audio lectures, DOCX, PPTX and more Ask questions naturally and get answers with exact page numbers and chunk-level citations Visualize a knowledge graph showing how concepts connect across all your sources Generate AI-powered multi-speaker podcasts from dense academic papers Auto-create flashcards, quizzes, and mind maps for retention and exam prep Self-host completely free under the MIT license for full data privacy How we built it The stack was chosen deliberately for each layer of the problem: Frontend: Next.js 16 with App Router and React Server Components for performance. Optimistic UI updates make chat feel instantaneous even during streaming responses. Backend: FastAPI for its native async support — critical for handling concurrent long-running LLM requests. Business logic lives in a clean service layer (ChatService, IngestionService) with PostgreSQL-backed background workers via Procrastinate for heavy document processing. RAG Pipeline: Built on LlamaIndex with a multi-stage retrieval system — parallel dense (semantic) and sparse (BM25) search, HyDE for complex queries, Query Fusion to merge results, and Cohere reranking for a final precision pass. Google Gemini 2.5 Flash handles generation for its large context window and multimodal capabilities. Storage: Polyglot persistence — PostgreSQL (Supabase) for structured data, Qdrant for vector similarity search, and Supabase Storage for raw files. Row-level security ensures complete data isolation between users. Audio: Kokoro TTS powers the multi-speaker podcast generation pipeline. Challenges we ran into Hallucination prevention was the hardest problem. We implemented a multi-layer policy system with confidence score thresholds — if retrieved context scores below 0.5, the AI returns nothing rather than guessing. Getting this balance right without making the system overly restrictive took significant tuning. Streaming + database consistency was a nasty race condition. Token streaming and async DB writes would conflict, risking message loss. We solved it by creating a new async session post-stream to persist messages only after the stream completes, with citations extracted and stored separately. Memory-safe large file processing — naive document ingestion would OOM on anything over ~20MB. We rebuilt the upload pipeline with streaming chunked processing that handles 100MB+ PDFs without breaking a sweat. Hybrid search fusion — balancing semantic and keyword retrieval results without one drowning out the other required careful weight tuning and iterative testing across diverse query types. ** Accomplishments that we're proud of** Zero hallucinations — every response is grounded in source material with verifiable citations Sub-500ms retrieval — hybrid search delivers results faster than most single-method systems 100MB+ file support — memory-safe streaming handles documents most platforms choke on Full self-hosting — researchers at institutions with strict data policies can run it entirely on their own infrastructure Adopted at 150+ universities — real researchers using it for real work within weeks of launch Built solo end-to-end — frontend, backend, RAG pipeline, auth, DevOps, and design What we learned RAG is an engineering problem, not just a prompt problem. Hybrid retrieval, reranking, and policy layers matter far more than prompt wording. Streaming state is deceptively complex. Managing consistency across async boundaries taught us a lot about distributed systems thinking at a small scale. Citations aren't a feature — they're the foundation. Building attribution in from day one changed every architecture decision downstream. Vector database schema design is critical early. Retrofitting chunk metadata into Qdrant payloads after the fact was painful — design for retrieval from the start. Users trust AI less than you expect, and rightly so. The most positive feedback was always about citations and transparency, not raw capability. ** What's next for MemexLLM** Real-time collaboration — multi-user notebooks with shared libraries and live co-editing Custom embedding models — support for domain-specific embeddings (biomedical, legal, financial) Advanced analytics — usage insights, retrieval quality metrics, and query performance dashboards Mobile app — native iOS and Android for on-the-go research with audio mode front and center Offline mode — local processing for air-gapped or highly sensitive research environments Plugin system — extensible architecture so teams can build custom content generators on top Integration APIs — webhooks and REST endpoints for connecting with Zotero, Notion, and Obsidian <div