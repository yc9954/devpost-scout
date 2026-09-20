---
slug: "tribune"
url: "https://devpost.com/software/tribune"
title: "Tribune"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1199
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "user/general_public"
  - "user/government_staff"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Tribune

> GitHub for democracy. Every policy change cited to a voice.

[Devpost](https://devpost.com/software/tribune) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[civic_government]] [[developer_tools]] [[housing_homeless]] [[transportation]]
**user** [[general_public]] [[government_staff]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** anthropic-claude, elasticsearch, fastapi, framer-motion, gemini, jina, mapbox, nextjs, openai-realtime, python, react, shadcn-ui, sqlite, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tribune

## Body

Every policy change traced to a real voice 200 real Palo Alto policies, 9 categories 35 residents interviewed, every quote linked to the policy clause it references Ask anything: Our agent searches policies, quotes, and diffs, then writes a cited research brief Live AI phone interview with real-time transcript and human-in-the-loop steering Inspiration In Palo Alto, the city council meets twice a month to vote on policies that affect parking, housing, zoning, and bike lanes. These decisions shape where you can live, how you get to work, and what your neighborhood looks like. But fewer than 2% of residents ever attend a council meeting. The other 98% are busy: working, caregiving, commuting. Their opinions exist, but nobody collects them. We asked: what if instead of waiting for residents to show up, you went to them? What if an AI agent could read the agenda overnight, figure out who's affected, call those people directly, and turn their feedback into policy revisions, with every line cited to a real voice? That's Tribune, GitHub for democracy. We turn phone calls into policy diffs. What it does Tribune automates the entire civic feedback loop in three steps: Watch : Tribune scrapes city council agendas, municipal codes, and government PDFs overnight. It extracts every policy proposal, identifies affected neighborhoods, and geo-tags them. For our demo, we processed real Palo Alto city council documents and extracted ~200 actionable policies across 9 categories (housing, transportation, zoning, etc.). Listen : Instead of hoping residents attend a 7pm meeting, Tribune calls them. An AI phone agent conducts natural interviews with residents on affected streets, asking about concerns, following up in real time, and transcribing everything. Each quote is tagged with sentiment, topic, and linked to the specific policy clause it references. Draft : Tribune generates policy revisions as diffs, red lines for removed text, green lines for additions: where every single change cites the resident interviews that motivated it. Policymakers can approve the revision, request changes, or send it to committee. Like a pull request, but for legislation. The platform also includes a Research Desk : an AI agent powered by Claude that can answer natural language questions about the entire policy corpus. Ask "How do renters feel about the parking changes?" and watch it search across policies, resident quotes, and proposed revisions in real time, streaming its reasoning step by step. How we built it Tribune is a full-stack platform with 5 AI providers, 3 Elasticsearch indices, and a real-time voice calling pipeline. Data Pipeline (4 stages) Collect: PrimeGov API + web scrapers discover documents from Palo Alto's city council site Download: Async HTTP fetches PDFs, deduplicates by content hash Extract: Google Gemini 2.0 Flash reads PDFs and outputs structured policy JSON (title, clause, geography, category) Classify: GPT-4o-mini scores each policy on actionability and resident impact (1-5) Search (Elasticsearch + JINA) 3 indices: policies, resident quotes, and proposed diffs Hybrid search pipeline: BM25 text search + kNN vector search (JINA embeddings, 1024-dim) fused via Reciprocal Rank Fusion (k=60), then reranked with JINA Reranker v3 Custom civic synonym analyzer (ADU = granny flat, BMR = affordable housing, etc.) Semantic text fields with auto-chunking for conceptual search Elasticsearch Agent Builder integration with 7 ES|QL tools callable via Agent-to-Agent protocol AI Research Agent (Claude Sonnet 4.5) 8 tools: search_policies, search_quotes, search_diffs, analyze_sentiment, find_related_policies, semantic_search, ask_agent_builder, trending_topics Up to 4 reasoning iterations per query Multi-turn conversation with history, follow-up questions reference prior findings Streams every step (thinking → tool call → result → answer) to the browser via SSE Voice Calling (OpenAI Realtime + Twilio) Twilio WebSocket connects call audio to OpenAI's Realtime API bidirectionally AI interviewer greets, introduces the policy, asks for feedback, follows up naturally, thanks the resident Live transcript streams to the monitoring UI via WebSocket Human in the loop: Policymakers can send hidden "directions" mid-call to steer the conversation On call end: auto-analysis → extract quotes → generate policy diff — full loop closes automatically Diff Generation (Claude Sonnet 4.5) Takes original clause + all interview data (sentiment, concerns, demographics, quotes) Constraint: must copy original text exactly and only insert or delete 1-2 short clauses (<15 words each) Every insertion must trace to specific constituent concerns Output includes revised clause, commit message with statistics, and citation chain Stack Frontend: Next.js 16, React 19, TypeScript, Tailwind v4, Framer Motion, Mapbox GL, shadcn/ui Backend: FastAPI (Python), two servers: port 8000 (REST API) and port 8001 (voice server) Database: SQLite (WAL mode) with 12 tables tracking the full chain: raw documents → policies → interviews → quotes → analysis → diffs Config: City configuration is YAML-based. Adding a new city = adding one file. Challenges we ran into PDF extraction at scale. Government PDFs are hostile, with inconsistent formatting, scanned images, tables within tables. We iterated heavily on our Gemini extraction prompts to reliably pull structured policy data from 200+ documents with different layouts. Citation integrity. Our core design principle is that every policy revision must trace back to a real resident voice. Building the citation chain (diff → interview IDs → quotes → resident) across 12 database tables while keeping it queryable and renderable in the UI was our hardest architectural challenge. Voice call reliability. The Twilio → OpenAI Realtime bidirectional audio pipeline is latency-sensitive. Getting natural-feeling conversations with sub-second response times required careful buffer management and prompt engineering to keep the AI interviewer concise and interruptible. Hybrid search tuning. Balancing BM25 keyword relevance against semantic vector similarity via RRF fusion required extensive testing. Civic language is domain-specific ("ADU" vs "granny flat"), so we built a custom synonym analyzer to bridge how residents talk and how policies are written. Accomplishments that we're proud of Processed ~200 real Palo Alto city council policies from actual government documents: this is not mock data Built a full AI phone interview pipeline that closes the loop automatically: call → transcript → analysis → policy revision Created a multi-turn research agent with 8 Elasticsearch-backed tools that streams its reasoning in real time Designed a citation-first architecture where zero policy changes exist without traced resident feedback Shipped 7 polished frontend pages with an editorial design system in 36 hours Integrated 5 AI providers (Gemini, OpenAI, Anthropic Claude, JINA, Elasticsearch) into a coherent pipeline What we learned Hybrid search (BM25 + semantic vectors + reranking) dramatically outperforms either approach alone for domain-specific civic text The Elasticsearch Agent Builder A2A protocol enables powerful delegation patterns: our Claude agent can offload complex ES|QL queries to Kibana agents Real-time voice AI has crossed the threshold where natural phone interviews are possible: six months ago, the latency would have made this unusable Government data is messy, inconsistent, and poorly structured. But it's public. An automated pipeline can democratize access to information that currently requires attending a meeting in person What's next for Tribune We're just getting started. There are 19,500 incorporated municipalities in the US, each holding council meetings that almost no one attends. Tribune starts with Palo Alto but is designed to scale to any city via YAML configuration. Next: expanding to more Bay Area cities, building relationships with city clerks and council staff, and exploring how this platform could serve state legislatures and federal public comment periods. <div