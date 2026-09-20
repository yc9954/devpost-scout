---
slug: "atlarix-nova-agent-architecture-intelligence-for-developers"
url: "https://devpost.com/software/atlarix-nova-agent-architecture-intelligence-for-developers"
title: "Atlarix"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 877
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Atlarix

> AI coding copilot that maps your codebase and codes with Amazon Nova

[Devpost](https://devpost.com/software/atlarix-nova-agent-architecture-intelligence-for-developers) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[accessibility]] [[developer_tools]] [[health_clinical]] [[labor_employment]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]]

**stack** anthropic, aws-bedrock-(amazon-nova-models), aws-sdk-v3, drizzle-orm, electron, github, google-gemini-(fallback), lm-studio, monaco-editor, node.js, ollama, openai, openrouter, react

## How they structured the write-up

- 💡 inspiration
- 🔨 how we built it
- 🧗 challenges we faced
- 🎓 what we learned
- 🚀 what's next

## Body

Mcp & Searxng Prompting AI Providers Diagrams Tools Project Templates blueprints Atlarix: AI Coding Copilot Powered by Amazon Nova 💡 Inspiration Most AI coding tools work blind. They scan open files, guess at architecture, and burn through tokens on context they don't need. On small projects that's manageable. On anything real — a monorepo, a multi-service backend, a codebase with years of history — it breaks down fast. We built Atlarix to fix this. The core idea: parse the entire codebase once using Round-Trip Engineering (RTE), build a live node/edge graph of every file, function, class, API route, and database operation, and use that graph as a RAG knowledge base for every AI query. The AI always has full architectural context before touching anything. Traditional tools load ~100K tokens per query. Atlarix loads ~5K — because it only injects what's relevant. With AWS Bedrock support added in v2.7, Atlarix now runs Amazon Nova models as the AI backbone — bringing Nova's reasoning and tool use capabilities into a full agentic coding workflow with visual architecture design, a four-agent system, and a 57-tool permission layer. 🔨 How We Built It 1. AWS Bedrock & Amazon Nova Integration Atlarix connects to Amazon Nova via AWS Bedrock using a dedicated provider adapter. Users configure their AWS credentials and region in Settings → AI Providers, and Atlarix fetches available Nova models (Nova Lite, Nova Pro, Nova Micro) directly. Authentication uses AWS bearer token + optional region config. The integration slots into Atlarix's existing multi-provider system — Nova sits alongside OpenAI, Anthropic, Gemini, and others, and the Auto router can select Nova based on task complexity. Nova's tool use capabilities map directly to Atlarix's 57-tool system — file operations, semantic search, web research, command execution, and DB queries all work with Nova as the active model. 2. Round-Trip Engineering (RTE) + Blueprint The foundation of Atlarix is the Blueprint — a live, interactive architecture diagram of your entire codebase. RTE parsers walk the project (TypeScript, Python, and more via Tree-sitter) and produce a node/edge graph stored in SQLite. A file watcher monitors changes and re-parses only affected nodes. This graph is the RAG knowledge base. When Nova (or any provider) receives a query, Atlarix hits the graph first, identifies relevant nodes, and injects only those source files into context. Full architectural awareness at a fraction of the token cost. The Blueprint is also editable — users design new features visually (Containers and Beacons on a React Flow canvas), then generate implementation plans from the design. 3. Four-Agent System with Guided & Autonomous Modes Nova powers a four-agent specialist system: Research — web search, codebase exploration, read-only analysis Architect — Blueprint design, planning, structural decisions Builder — code generation, file writes, command execution Reviewer — static analysis, pattern matching, quality gates In Guided mode, a controller delegates to specialists flat. In Autonomous mode, agents spawn sub-agents with a depth limit. Every delegation event surfaces in the Activity Stream in real time. 4. Permission System Every file write, code generation, and command execution goes through a permission queue. Nova proposes the change; the user sees a full diff before approving. Batch approval, individual approval, and reject all are supported. No action executes without explicit user sign-off. 5. DB Extension Nova can interact with connected databases through four tools: db_query, db_schema, db_list, and db_mutate. Users connect PostgreSQL, MySQL, MariaDB, or SQLite via connection string — Atlarix auto-detects the engine and database name. The schema is injected into the system prompt so Nova always has structural context before writing a query. 🧗 Challenges We Faced Token efficiency at scale. Large codebases can have thousands of nodes. Getting the RAG retrieval tight enough that Nova receives exactly the right context — not too much, not too little — required careful graph traversal logic and import-based edge inference. Multi-provider routing. Atlarix supports 10 providers. Making Nova's tool use response format work consistently within the same pipeline as OpenAI and Anthropic required provider-specific adapters while keeping the agent layer provider-agnostic. macOS notarization. Atlarix is a real shipped desktop app — Apple Notarized and code-signed. Getting the CI/CD pipeline (GitHub Actions + electron-forge) to handle signing, notarization, and publishing reliably took significant work. v3.7 ships as Apple Verified on macOS. 🎓 What We Learned Nova's reasoning capability handles complex multi-step coding tasks well — particularly in Autonomous mode where the Architect agent needs to reason about codebase structure before the Builder acts. The price-performance ratio on Nova Lite makes it a strong choice for the fast/routine tasks in the agent pipeline while reserving heavier models for complex reasoning steps. Visual architecture design genuinely changes how developers approach problems. Users who start in Blueprint first write less throwaway code. 🚀 What's Next v3.9 — GitHub Actions pipeline reading: Atlarix surfaces CI/CD failures directly in the coding environment and lets Nova diagnose and fix build errors in context Windows build — EV code signing in progress; full Mac/Windows/Linux parity coming in 2026 Atlarix Workforce — multi-workspace orchestration, scheduled agent runs, Slack integration, team-shared Blueprints GitHub Marketplace listing — timed to the v3.9 CI/CD integration release Atlarix is in active development with real users on Mac and Linux. Every feature described here ships in the current release. Built by NorahLabs — atlarix.dev <div