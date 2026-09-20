---
slug: "legalmindz"
url: "https://devpost.com/software/legalmindz"
title: "Legalmindz"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 2799
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/mental_health"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
  - "user/general_public"
  - "user/legal_professional"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Legalmindz

> Ethiopia has 2.5 million businesses but only 3,000 lawyers. Legalmindz brings Legal AI for 120 Million People, because 120 million people deserve accessible legal services.

[Devpost](https://devpost.com/software/legalmindz) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[multi_agent]] [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[structural_withholding]] [[vision_ocr]]
**domain** [[agriculture_food]] [[civic_government]] [[developer_tools]] [[education]] [[finance_payments]] [[health_clinical]] [[labor_employment]] [[legal_justice]] [[mental_health]] [[transportation]]
**user** [[developer]] [[frontline_worker]] [[general_public]] [[legal_professional]] [[small_business]]
**substrate** [[code_repository]] [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-web-services, bedrock, nextjs, nova

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for legalmindz
- why this matters
- try it
- built with
- team

## Body

Legalmindz multi agent legalmindz nova stack legalmindz features legalmindz workflow legamindz agent chat LegalMindz Nova - AI Legal Infrastructure for 120 Million People Inspiration 120 million people. 3,000 lawyers. That is Ethiopia today. One lawyer for every 40,000 citizens. In the United States, the ratio is 1:250 -- Ethiopia's is 160 times worse. If you are a small business owner in Addis Ababa, a coffee farmer in Sidama, a startup founder in Hawassa - you have almost certainly never consulted a lawyer. You have never had a contract reviewed. You signed what was placed in front of you, or you signed nothing at all. 2.5 million Ethiopian businesses. 83% have never had a single legal document reviewed. When disputes arise - and they do - these businesses lose. Not because they were wrong. Because they had no documentation. No protection. No legal infrastructure. One contract costs $500 . A typical Ethiopian SME earns less than that in a month. This is not a technology gap. It is an access gap. And access gaps are exactly what AI was built to close. LegalMindz delivers Fortune 500-grade legal infrastructure to a market where it has never existed -- powered entirely by Amazon Nova. #AmazonNova Live Demo | Source Code What It Does LegalMindz is a full-stack AI legal platform that gives every Ethiopian business access to contract drafting, risk analysis, legal research, voice consultation, and workflow automation -- in both English and Amharic - powered end-to-end by Amazon Nova models through Amazon Bedrock. 1. Multi-Agent Contract Drafting (4 Specialized Agents) A four-agent pipeline generates legally compliant Ethiopian contracts with real-time token streaming . You watch the contract materialize word by word as each agent completes its phase. The Pipeline: Research Agent (Nova Pro) - Embeds the query via Nova Embed, retrieves relevant Ethiopian law articles from pgvector via cosine similarity, and identifies the legal requirements for the specific contract type Compliance Agent (Nova Pro) - Cross-references the research output against Ethiopia's Civil Code (1960), Commercial Code (Proclamation 1243/2021), and Labour Proclamation 1156/2019 to produce a mandatory clause checklist Drafting Agent (Nova Pro) -- Generates the complete contract via streamText , token by token via SSE, incorporating the research findings and compliance requirements. Full bilingual support -- the entire contract can be drafted in Amharic with Ge'ez script legal citations Review Agent (Nova Pro) -- Performs adversarial compliance audit on the finished contract, checking for gaps, ambiguities, and missing mandatory provisions 49 contract templates spanning employment (standard, fixed-term, part-time, probationary, managerial, domestic worker, construction, internship), commercial and residential leases, sales agreements (goods, vehicle, business, property, export, installment), service contracts (consulting, IT, construction, transport, cleaning, security, catering, training, accounting, marketing), NDAs (mutual, employee, investor, vendor), partnership and joint venture, and specialized instruments (agency, franchise, loan, supply, maintenance, software license, distribution, power of attorney, guarantee, settlement, MOU, share purchase). 2. Contract Risk Analysis (Streaming 3-Step Pipeline) Upload a PDF or paste any contract text. A streaming SSE pipeline reviews the document against Ethiopian law in real time: Step 1: Structure Review -- Parses the document structure and identifies clause boundaries Step 2: Compliance Check (Nova Pro) -- Evaluates every clause against Ethiopian federal law. Uses structured JSON output ( generateObject pattern) with severity ratings, specific article violations, and missing mandatory clauses Step 3: Risk Scoring -- Produces an actionable report: risk level (High/Medium/Low), clause-by-clause issues with the specific Ethiopian law violated (e.g., "Labour Proclamation 1156/2019, Article 42"), and recommended compliant replacement language Full Amharic analysis available -- every field, every recommendation, rendered in Ge'ez script. 3. Voice Legal Consultation in Amharic (Amazon Nova Sonic) A small business owner in rural Ethiopia opens LegalMindz on their phone, taps the microphone, and asks a legal question in Amharic -- the language 120 million Ethiopians actually speak. The AI listens, understands, and speaks the answer back in Amharic, grounded in Ethiopian law, citing specific proclamation articles. No app literacy required. No English required. No lawyer required. Technical architecture: Amazon Nova Sonic ( amazon.nova-sonic-v1:0 ) via InvokeModelWithBidirectionalStreamCommand Custom Sonic Bridge -- a dedicated Node.js WebSocket server running on EC2 that translates between the browser's audio stream and Bedrock's bidirectional streaming API Audio pipeline: Browser microphone → 16kHz/16-bit/mono PCM → base64 → WebSocket → Sonic Bridge → Bedrock Nova Sonic → 24kHz/16-bit/mono PCM audio response → WebSocket → custom PCMPlayer with gapless AudioContext scheduling System prompts in both English and Amharic (full Ge'ez script: "አንተ "LegalMindz" ነህ — የኢትዮጵያ ሕግ ባለሙያ AI" ) Animated AI persona with state transitions: idle → listening → thinking → speaking Graceful degradation: if Nova Sonic WebSocket is unreachable (e.g., HTTPS/WSS mismatch), automatically falls back to Nova Pro SSE streaming via /api/voice This is the first Amharic-language legal voice AI ever built. 4. Deep Research (Nova Pro + Nova Act + Tool Use) Complex legal questions trigger a Deep Research pipeline that goes far beyond a chatbot summary: Step 1: Research Planning (Nova Pro, generateObject ) -- Creates a structured research plan with 2-4 topics, each with 2-4 specific search queries Step 2: Agentic Execution (Nova Pro, generateText with tool use) -- The model autonomously decides when and how to call two tools: browseEthiopianLaw -- Calls the Nova Act sidecar (Flask on EC2, port 8001) which uses Amazon Nova Act browser automation to navigate negarit.gov.et (Ethiopia's official Federal Negarit Gazette) and extract authoritative legal text webSearch -- Calls the Tavily API for supplementary analysis, commentary, and comparative law Up to 6 agentic steps ( stepCountIs(6) stop condition), with real-time progress streaming via SSE Output: structured research plan, collected sources with URLs, and synthesized findings with citations This is a researched legal brief, not a chatbot response. 5. Workflow Automation (4-Agent Pipeline × 8 Workflow Types) Eight pre-built legal workflows, each executing a four-agent pipeline: Workflow What It Produces Due Diligence Corporate structure review, regulatory compliance status, risk ratings, recommended actions Contract Review Clause-by-clause analysis, compliance issues, risk assessment with law references Business Registration Step-by-step registration guide with documents, offices, timelines, fees Employment Law Audit Labour Proclamation 1156/2019 compliance check across contracts, hours, benefits, termination Tax Compliance Income tax, VAT, withholding tax, pension review with gap analysis IP Protection Trademark, copyright, patent strategy with EIPO filing procedures Real Estate Advisory Land lease, property transfer, construction permits, EIA requirements Dispute Resolution Negotiation/mediation/arbitration/litigation strategy with cost and timeline analysis Each workflow executes: Legal Research Agent (Nova Pro + Tavily tool use) -- Retrieves applicable Ethiopian law Document Analysis Agent (Nova Pro) -- Extracts key entities, obligations, risks Compliance Check Agent (Nova Lite) -- Fast compliance verification Report Generation Agent (Nova Pro) -- Produces the final deliverable with markdown formatting All workflows support bilingual output (English/Amharic) and downloadable reports. 6. Legal Chat with RAG (7 Model Options) RAG-enhanced legal chat grounded in Ethiopian federal law: Embedding pipeline: User query → Nova Embed ( amazon.nova-embed-v1:0 ) with Titan Embed v2 ( amazon.titan-embed-text-v2:0 ) fallback → 1024-dimensional vector Vector search: Cosine similarity search against pgvector (IVFFlat index) over Ethiopian law articles covering Labour Proclamation 1156/2019, Civil Code 1960, Commercial Code 1243/2021, Tax Law, IP Law, Investment Proclamation, Constitutional Law, Family Law, Environmental Law, Banking, Telecom, Mining, Consumer Protection, and Arbitration Law RAG citations: Sources are returned as message metadata and displayed as inline citations with relevance percentages Optional web search: Tavily integration for live supplementary sources Bilingual system prompts: Amharic mode triggers Ge'ez script citation format ( የሠራተኛ አዋጅ ቁጥር 1156/2019 አንቀጽ 42 ) 7 selectable models -- all Amazon Bedrock: Model ID Use Case Nova Pro us.amazon.nova-pro-v1:0 Deep legal reasoning Nova 2 Lite amazon.nova-2-lite-v1:0 Fast chat responses Nova Lite v1 us.amazon.nova-lite-v1:0 Lightweight queries Nova Micro us.amazon.nova-micro-v1:0 Ultra-fast single-turn Titan Text Premier us.amazon.titan-text-premier-v2:0 AWS Titan reasoning Titan Text Express us.amazon.titan-text-express-v1 AWS Titan fast Titan Text Lite us.amazon.titan-text-lite-v1 AWS Titan lightweight 7. Document OCR (Nova Pro Vision) Upload a PDF or image of any legal document: PDF: Extracted via pdf-parse v2 (class-based API, serverless-compatible) Image: Processed by Nova Pro Vision ( us.amazon.nova-pro-v1:0 multimodal) using InvokeModelCommand with base64-encoded image input -- extracts all text verbatim, preserving clause numbers, section headers, and legal formatting Fallback chain: pdf-parse v2 → pdf-parse v1 → Nova Pro Vision → error with diagnostics How We Built It The Amazon Nova Stack Every user interaction in LegalMindz flows through Amazon Bedrock. This is not one model bolted onto an existing application. Amazon Nova IS the platform. Every feature, every agent, every pipeline runs on Nova. Capability Amazon Nova Model Model ID Multi-agent reasoning (drafting, analysis, workflows, research) Nova Pro us.amazon.nova-pro-v1:0 Fast chat, compliance checking Nova 2 Lite amazon.nova-2-lite-v1:0 Lightweight queries Nova Lite v1 us.amazon.nova-lite-v1:0 Ultra-fast single-turn Nova Micro us.amazon.nova-micro-v1:0 Real-time bidirectional voice (Amharic + English) Nova Sonic amazon.nova-sonic-v1:0 Text embeddings for RAG vector search Nova Embed amazon.nova-embed-v1:0 Embedding fallback Titan Embed v2 amazon.titan-embed-text-v2:0 Document OCR (multimodal vision) Nova Pro Vision us.amazon.nova-pro-v1:0 (multimodal) Deep research browser automation Nova Act Via EC2 sidecar AWS Titan reasoning Titan Text Premier us.amazon.titan-text-premier-v2:0 AWS Titan fast Titan Text Express us.amazon.titan-text-express-v1 AWS Titan lightweight Titan Text Lite us.amazon.titan-text-lite-v1 11 Amazon models. One platform. Zero external LLM dependencies. Architecture ┌─────────────────────────────────────────────────────────────────┐ │ Vercel (Next.js 16, React 19) │ │ │ │ /chat — RAG legal chat (7 model selector) │ │ /draft — Multi-agent contract drafting (4 agents, SSE) │ │ /analyze — Contract risk analysis (streaming pipeline) │ │ /upload — Document OCR (pdf-parse + Nova Pro Vision) │ │ /voice — Real-time voice consultation (Nova Sonic) │ │ /workflow — 8 workflow types (4-agent pipelines) │ │ /dashboard — Usage metrics │ │ │ │ Deep Research: Nova Pro + Nova Act + Tavily (tool use, SSE) │ └──────┬──────────────────┬──────────────────┬────────────────────┘ │ │ │ ▼ ▼ ▼ ┌──────────────┐ ┌──────────────┐ ┌────────────────────────────┐ │ Neon Postgres│ │ SQLite │ │ Amazon Bedrock │ │ (pgvector) │ │ (local) │ │ │ │ Ethiopian │ │ contracts │ │ Nova Pro Nova 2 Lite │ │ law articles │ │ analyses │ │ Nova Lite Nova Micro │ │ 1024-dim │ │ documents │ │ Nova Sonic Nova Embed │ │ vectors │ │ metrics │ │ Titan Premier/Express/Lite │ │ IVFFlat idx │ │ │ │ Nova Pro Vision (OCR) │ └──────────────┘ └──────────────┘ └──────────