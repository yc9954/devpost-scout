---
slug: "shipyard-own7ys"
url: "https://devpost.com/software/shipyard-own7ys"
title: "Shipyard"
hackathon: " GenAI Genesis 2026"
organization: "GenAI Genesis"
winner: true
words: 744
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "domain/transportation"
  - "user/developer"
  - "substrate/code_repository"
---

# Shipyard

> Visualize your repo's production readiness as a 3D city, then ship it with AI agents

[Devpost](https://devpost.com/software/shipyard-own7ys) · hackathon [[GenAI Genesis 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[developer_tools]] [[media_journalism]] [[transportation]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** claude-api, framer-motion-backend-express, frontend-next.js-14, oauth, react-three-fiber, socket.io, tailwind, typescript, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for shipyard

## Body

Inspiration Every developer has shipped code that was not quite production-ready: missing tests, no CI/CD, hardcoded secrets, no Docker config. The issue is not that developers do not know what production readiness means. The checklist is simply long, repetitive, and easy to ignore. We wanted to turn that checklist into something visual and tangible. Instead of abstract scores or reports, what if a repository’s readiness appeared as a city? Each missing piece of infrastructure would represent a building that has not yet been constructed. As the repository improves, the city grows. This idea became Shipyard . What it does Shipyard analyzes any GitHub repository across eight dimensions of production readiness : Tests CI/CD Docker Documentation Environment variables Security Logging Deployment The results are visualized as an interactive 3D city . Each category appears as a building whose height and glow reflect its score. Users can click any building to open a specialist AI agent that understands the repository’s actual codebase. Instead of giving generic advice, the agent reads source files, detects frameworks, and generates real code such as: Dockerfiles GitHub Actions workflows test files .env.example templates configuration updates When a user accepts changes, the building grows. When all eight buildings are complete, the repository is considered production-ready. All accepted changes can then be exported as a ZIP. The deployment building also recommends a hosting platform (Vercel, Railway, Fly.io, etc.) based on the detected stack and generates platform-specific setup scripts. How we built it Frontend Next.js 14 React Three Fiber for the 3D city rendering Zustand for state management Framer Motion for UI animations Monaco Editor for inline code review Buildings use physically based rendering (PBR) materials. Height, color, and emissive glow are driven by live scan data. Backend Express with TypeScript Socket.IO for real-time streaming The repository scan runs in two phases: Heuristic phase Eight deterministic analyzers run in parallel using regex patterns, file checks, and dependency detection. Results stream via WebSocket so buildings rise in real time. Deep analysis phase A single Claude Sonnet call receives all scan results and generates contextual tasks for each building. AI agents Each building has a specialist agent powered by Claude Sonnet 4.6 with domain-specific system prompts. Agents receive: repository structure detected frameworks cross-building change log Code generation follows an implement → evaluate → refine loop with a maximum of three iterations. A dedicated evaluator agent checks output quality. Infrastructure GitHub OAuth authentication session-based state management monorepo-aware dependency merging archiver for ZIP exports Challenges we ran into Conversation history limits Long agent conversations exceeded token limits. We implemented automatic summarization that condenses older messages while preserving recent context. Cross-building coherence Agents sometimes generated conflicting suggestions. For example, the Security agent might modify .gitignore while the Environment Variables agent remained unaware. We solved this using a shared change log that every agent receives as context. Two-phase scan timing The heuristic scan is fast and shows buildings rising immediately, while deep LLM analysis takes longer. We had to merge LLM results into the existing scan output without resetting progress. Real-time 3D synchronization Streaming WebSocket events required careful synchronization between the Zustand state store and the Three.js scene graph to prevent flickering or stale renders. Accomplishments that we're proud of Buildings rise in real time during scans, creating a satisfying feedback loop Deep analysis uses a single LLM call across all eight categories, keeping costs low Agents generate repository-specific changes instead of generic advice The full workflow functions end-to-end: scan → visualize → chat → generate code → accept → export ZIP → deploy Monorepo support correctly merges dependencies across frontend/ , server/ , and root directories What we learned Gamification improves engagement Turning a checklist into visible progress makes developers care about code quality improvements. Heuristic plus LLM works best Deterministic checks provide instant feedback. The LLM provides deeper reasoning and context. Combining both approaches produces faster and more useful results. Agent specialization matters Generic prompts produce vague suggestions. Focused agents with domain-specific prompts generate more actionable outputs. Real-time feedback is essential Early versions waited for scans to finish before displaying results. Streaming progress events made the experience significantly more engaging. What's next for Shipyard Custom 3D building models using detailed .glb assets GitHub pull request integration instead of ZIP exports Persistent sessions to track repository readiness over time Team dashboards aggregating scores across multiple repositories Additional categories such as accessibility, performance, API documentation, and dependency freshness Live deployment verification that deploys preview environments and runs health checks <div