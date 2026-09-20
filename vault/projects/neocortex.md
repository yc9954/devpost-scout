---
slug: "neocortex"
url: "https://devpost.com/software/neocortex"
title: "Neocortex"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 638
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/graph_reasoning"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
---

# Neocortex

> Less Tokens. More Answers.

[Devpost](https://devpost.com/software/neocortex) · hackathon [[NexHacks]]

## Facets

**mechanism** [[benchmark_measured]] [[graph_reasoning]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]] [[sensor_telemetry]]

**stack** commander.js, express.js, github-api, node.js, openai-embeddings-api, passion, pnpm, react, simple-git, tailwind-css, tree-sitter, typescript, vite, voyage-ai-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for neocortex
- built with
- try it

## Body

Our logo Sample UI Neocortex Inspiration Modern AI coding assistants struggle with unfamiliar codebases. They dump entire files into context or miss critical dependencies. We asked: what if an AI could understand code the way a senior engineer does - by following function calls, understanding relationships, and retrieving only what's relevant? Neocortex was born from watching LLMs hallucinate about code they couldn't see while ignoring the exact functions that mattered. What it does Neocortex is a semantic code retrieval engine that gives AI laser-focused context. Point it at any GitHub repository, ask a question like "how does authentication work?", and it returns the exact functions, classes, variables, and types needed to answer, compressed to fit your token budget. Three stages: Parse - Tree-sitter extracts every function, class, and type into a searchable dependency graph Search - OpenAI embeddings + keyword matching + graph traversal finds relevant code Compress - Intelligent slicing maximizes relevance within your token budget Instead of 17,000 tokens of code, you get 1,200 tokens of exactly what matters. We integrated this as a full MCP (Model Context Protocol) server so any AI assistant can use Neocortex as a tool. MCP Tools: Tool Description index_repo Clone and index any GitHub repository search_code Semantic search with natural language resolve_symbol Find definitions by exact name get_snippet Get code from specific file:lines classify_query Analyze query intent for search optimization How we built it Pipeline architecture in TypeScript: AST Parsing - Tree-sitter extracts code entities and relationships Dependency Graph - Bidirectional edges tracking function calls Vector Embeddings - OpenAI text-embedding-3-small for semantic search Query Classifier - Tunes search strategy based on query type Compression Pipeline - Query-aware slicing to cut tokens while preserving relevance MCP Server - LeanMCP exposes everything as AI-callable tools Tree-sitter was chosen because it powers GitHub's syntax highlighting and provides precise AST access. The hybrid search (embeddings + keywords + graph expansion) outperforms pure semantic search on code. Challenges we ran into Embedding score calibration : OpenAI embeddings return 0.2-0.4 scores for relevant code, not 0.8+ like expected. We spent hours thinking search was broken before recalibrating thresholds. Graph explosion : Expanding dependencies 2 levels deep can return hundreds of entities. We implemented depth limiting and prioritization to keep results focused. Token budgets : Fitting meaningful code into 2,000 tokens while preserving context required building a slicing algorithm that keeps signatures, relevant lines, and truncates intelligently. Sleep deprivation : At 3 AM, every bug looks like a feature. Caffeine got us through. Accomplishments that we're proud of Our benchmarks across 4 repositories (56 queries): Metric Result Average token reduction 85.2% Cost savings 93.8% Search latency 246ms Debugging queries 95.6% reduction Multi-hop queries 95.5% reduction By Token Budget: Budget Reduction 500 tokens 93.9% 1,000 tokens 87.0% 2,000 tokens 74.5% 4,000 tokens 86.1% Cost Savings (GPT-4o): Scale Monthly Savings 10,000 queries $808 100,000 queries $8,080 Other wins: Hybrid search beats pure semantic search Query classification auto-adjusts strategy Full MCP server with 5 tools Zero-config for any TypeScript/JavaScript repo Team collaboration integrated seamlessly What we learned Embedding similarity scores vary wildly between models - calibrate empirically Graph-based context expansion is crucial - functions don't exist in isolation Token budgets force information density thinking Tree-sitter is powerful once you learn its query patterns MCP is the future of AI tool integration "Power naps" during hackathons are a gamble What's next for Neocortex Multi-language support (Python, Go, Rust) VS Code extension SDK Cached indexes for instant queries Fine-tuned reranker for code relevance MCP registry publishing Built With TypeScript Tree-sitter OpenAI Embeddings LeanMCP Node.js Express.js React + Vite Tailwind CSS Try It git clone https://github.com/rusheelsharma/neocortex cd neocortex && pnpm install # Run demo pnpm demo # Query any repo pnpm dev context https://github.com/user/repo "how does X work?" # Start MCP server pnpm mcp:dev Built by Software Developers for Software Developers 💪 <div