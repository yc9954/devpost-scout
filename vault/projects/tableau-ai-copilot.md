---
slug: "tableau-ai-copilot"
url: "https://devpost.com/software/tableau-ai-copilot"
title: "Tableau AI Copilot"
hackathon: "Tableau Hackathon"
organization: "Tableau"
winner: true
words: 893
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Tableau AI Copilot

> Your intelligent AI assistant for Tableau Cloud

[Devpost](https://devpost.com/software/tableau-ai-copilot) · hackathon [[Tableau Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]]

**stack** gemini, langchainjs, langgraphjs, react, restapi, tableau, typescipt, vite, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tableau ai copilot

## Body

Landing Page Copilot Chat Page Querying Visualization Generation for the previous query Canvas Tab to pin your visualizations for later reference Inspiration The inspiration for Tableau AI Copilot came from observing a common pain point: finding the right visualization in Tableau Cloud is harder than it should be. Users have hundreds of dashboards but don't know what exists, can't search effectively by name, and waste time browsing manually. Non-technical users struggle even more. We envisioned a future where you could simply ask "Show me Q4 sales performance" and instantly get the right dashboard—no browsing, no guessing, just natural conversation with your data. That's why we built Tableau AI Copilot: to democratize access to analytics through the power of AI. What it does Tableau AI Copilot transforms how you interact with Tableau Cloud by adding an intelligent, conversational layer powered by Google Gemini AI and LangGraph agents. Key Features: • Natural Language Discovery: Ask "Show me sales dashboard" and AI semantically searches all Tableau content • Embedded Visualizations: Dashboards appear instantly in chat with full interactivity • Secure Authentication: JWT-based authentication using Tableau Connected Apps • Multi-Agent AI System: Router, Discovery, Retriever, Analyzer, and Summarizer agents working together • Real-time Progress: Watch agents work with animated status indicators Tech Integration: • Tableau REST API v3.22 for metadata • Tableau Embedding API v3 for interactive dashboards • OpenAI embeddings for semantic search (50-60% relevance) • Google Gemini Pro for reasoning • ChromaDB for vector storage User Journey: Connect to Tableau Cloud (one-click authentication) Workbooks automatically indexed with AI embeddings Ask questions in natural language AI finds relevant dashboards and displays them inline Interact with live Tableau visualizations directly in chat How we built it Architecture: React + TypeScript frontend ↔ Node.js backend ↔ LangGraph agents ↔ Tableau Cloud + Google Gemini + OpenAI Frontend: • React 18 with TypeScript for type safety • Tailwind CSS and shadcn/ui for modern UI • Tableau Embedding API v3 for visualizations • Socket.IO for real-time updates Backend: • Node.js + Express with TypeScript • LangChain.js + LangGraph for multi-agent orchestration • Google Gemini Pro for reasoning • OpenAI embeddings for semantic search • Tableau REST API v3.22 integration • JWT authentication with Connected Apps • ChromaDB for vector storage Key Implementation: Tableau Integration: JWT token generation, REST API client with 12+ endpoints, semantic indexing AI Agents: State-based LangGraph workflow with 5 specialized agents and conditional routing Semantic Search: OpenAI embeddings (1536-dim vectors), cosine similarity ranking Security: Server-side credentials, session-based auth, CORS protection Development took [X weeks] with comprehensive testing at each phase. Challenges we ran into Tableau Authentication: Connected Apps JWT authentication required understanding Direct Trust, secret signing, and token lifecycle. Solution: Created proper JWT generation with automatic refresh and comprehensive test scripts. Semantic Search Accuracy: Initial keyword matching returned irrelevant results. Solution: Switched to OpenAI embeddings with rich metadata descriptions, achieving 50-60% relevance. Embedding API Integration: Tableau's Web Components required special React handling and JWT refresh. Solution: Built React wrapper component managing lifecycle and authentication. Multi-Agent Orchestration: Coordinating multiple AI agents while maintaining state was complex. Solution: Used LangGraph's StateGraph with explicit transitions and WebSocket progress updates. Real-Time Updates: Users needed to see progress during 5-15 second AI processing. Solution: Implemented Socket.IO with animated agent status indicators. TypeScript Types: Integrating multiple libraries with proper types required significant effort. Solution: Created comprehensive type definitions for all APIs and state schemas. Accomplishments that we're proud of Technical Achievements: • Full Tableau Platform integration (REST API v3.22 + Embedding API v3) • Advanced multi-agent AI system with LangGraph • Semantic search with 50-60% relevance accuracy • Production-ready TypeScript codebase with 15,000+ lines • 30+ API endpoints, 12+ Tableau integrations Innovation Highlights: • First AI copilot specifically for Tableau Cloud • Semantic discovery using embeddings (not keyword search) • Embedded chat experience with inline visualizations • Multi-agent intelligence with specialized tasks Impact Potential: • Reduces dashboard discovery from minutes to seconds • Makes BI tools accessible to non-technical users • Helps users discover visualizations they didn't know existed • Increases Tableau ROI through better discoverability What we learned Technical Learnings: • Tableau Developer Platform: Deep dive into Connected Apps (JWT + Direct Trust), REST API v3.22, Embedding API v3 architecture • AI Orchestration: LangGraph's StateGraph for complex agent workflows, conditional routing, state management • Semantic Search: OpenAI embeddings capture meaning better than keywords, quality metadata is crucial • Full-Stack TypeScript: End-to-end type safety catches errors early and makes refactoring safer • Real-Time UX: WebSocket progress updates transform user perception of AI speed Product Learnings: • Real-time feedback is essential for AI applications • Server-side credentials are simpler than OAuth flows for users • Showing agent progress builds trust in AI results • Natural language lowers barriers to entry significantly Key Lessons: Start with authentication (everything depends on it) Test each component independently with scripts TypeScript from day one saves maintenance time Design state schema before building agents AI quality depends heavily on prompt engineering What's next for Tableau AI Copilot Immediate Roadmap: • Tableau Pulse integration for metric insights • Custom view generation based on natural language • Multi-workbook analysis and comparison • Slack and Teams bot integration Long-Term Vision: • Enterprise features: Multi-tenancy, SSO, audit logging • Platform expansion: Mobile apps, voice interface • AI enhancement: Fine-tuned models, reasoning chains • Data sources: Direct DB connections, cloud warehouses, SaaS integrations <div