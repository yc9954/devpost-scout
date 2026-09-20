---
slug: "devforge-p7it9g"
url: "https://devpost.com/software/devforge-p7it9g"
title: "DevForge"
hackathon: "United Hacks V7"
organization: "Hack United"
winner: true
words: 1172
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# DevForge

> DevForge: Turn ideas into working software with an AI engineering team.

[Devpost](https://devpost.com/software/devforge-p7it9g) · hackathon [[United Hacks V7]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]]
  <sub>weak: cross_origin_web, human_in_the_loop, retrieval_grounding, vision_ocr</sub>
**domain** [[developer_tools]]
  <sub>weak: labor_employment, security_privacy</sub>
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]]
  <sub>weak: document_pdf, structured_db</sub>

**stack** chromadb, deepseek, docker, fastapi, groq, jwt, kubernetes, mongodb, next.js, oauth2, openai, openrouter, python, react

## Body

Introduction to DevForge What makes DevForge Different From Goal to Production in 8 Phases Swarm Architecture DevForge vs the Field User Experience Login Page Dashboard page featuring Luna, our little mascot cat! ≽^•⩊•^≼ Agents Information Page Tools Information Page Monitoring Page User Settings Page Notebook Page DevForge Inspiration Every one of us has felt the same gut punch: you open Cursor or Claude Code, ask it to build something real, not a todo app, an actual system, and by the time it's done you've burned through your monthly budget on what should have been a $10 job. The tools are genuinely magic. They're also priced like it. Frontier labs charge premium rates because they're running their best models for every tool call, every file read, every "let me check that again." That's fine for a quick surgical edit. It falls apart the moment you want an agent to actually run a project , discovery through deploy, because that's thousands of small calls, not a handful of big ones. We kept asking why every call in an agentic loop needs to hit the most expensive model available. A file read confirmation doesn't need the same brain as an architecture decision. That question became DevForge: describe what you want in plain English, and let a swarm of specialized agents build it, where each agent uses the model that's actually appropriate for its job. What it does DevForge is a notebook style workspace. Feed it sources (docs, audio, PDFs, YouTube links), talk to it, and when you're ready, type /swarm <your goal> . That spins up a team of 37 specialized agents, an orchestrator, architect, backend/frontend/database engineers, a critic, QA, security, SRE, DevOps, a release manager, that walk your goal through an 8 phase SDLC: Discovery, Planning, Architecture, Repo Discovery, Contracting, Build, Quality, Deploy & Monitor. You watch it happen live: an artifact tree fills in as files get written, a WebSocket feed streams what each agent is doing, and at key checkpoints the swarm stops and asks you for approval before committing to a direction. If the critic scores a build below a quality bar, it retries automatically, up to three times, before escalating to a human instead of quietly shipping something broken. How we built it The engine is a Python multi-agent orchestration core: an in-process asyncio message bus (Redis Streams if you need to scale out), a DAG-based task graph so independent work runs in parallel, and a three-tier memory system, a scratchpad per agent, a shared blackboard per sub-swarm, and a long-term ChromaDB vector store so the swarm keeps context across a long build. On top sits a six-layer safety system: tool allowlists, side-effect gating, prompt injection detection, a circuit breaker after three consecutive failures, quota enforcement, and a filesystem jail. The notebook UI is a Next.js/TypeScript frontend on a FastAPI + MongoDB backend. The decision we're proudest of: the swarm engine runs in-process inside the same FastAPI server, so phase gates and human approvals resolve through plain asyncio.Future s instead of a fragile chain of service calls. The cost part is what we actually care about most. Every agent role points at a model tier , not a fixed model. Cheap providers routed through OpenRouter handle the bulk of the ReAct loop, the perceive, plan, act, reflect grind that dominates token volume. We save expensive frontier calls for the places they earn their keep: architecture decisions, critic review, ambiguous planning. If a build costs roughly $$ C_{\text{total}} = \sum_{i=1}^{n} t_i \cdot p_{m(i)} $$ the lever that matters isn't shrinking $t_i$, agentic loops are chatty no matter what, it's shrinking $p_{m(i)}$ for steps where a cheaper model gets you the same answer. Route the low-stakes majority of steps to a model priced an order of magnitude lower, and the total cost curve bends hard without the build getting dumber where it counts. A CostLedger tracks real spend per run so budgets aren't a guess. Challenges we ran into Wiring the phase-gate approval flow was a real fight: getting a human's approve/reject click to correctly pause an asyncio task graph mid-execution, without deadlocking or losing state on a dropped WebSocket connection, took a few embarrassing rewrites. Model routing took a lot of trial and error too. Push too much onto the cheap tier and the critic starts approving mediocre architecture. Push too little and you're back to burning frontier money on boilerplate, which defeats the whole point. The three-tier memory system was its own quiet nightmare. Too generous a scratchpad leaks irrelevant context into every downstream call. Too sparse a blackboard means agents re-derive decisions their teammates already made, which costs even more than just paying for a bigger model. Getting that balance right ate more of our clock than any single feature we shipped. Accomplishments that we're proud of We got a goal typed into a chat box to turn into a running, tested, deployed system with almost no hand-holding, end to end, with a human stepping in only at the checkpoints that matter. The parts nobody sees on a demo call are the ones we're quietly proudest of: a critic that actually rejects its own team's work and forces a retry, a safety net that stops a rogue tool call before it touches a real filesystem, a cost ledger that tells you in real dollars what a build cost, not an estimate. We're also proud we didn't fake the multi-agent story. Thirty-four roles isn't a marketing number. Architect, critic, engineers, QA, security, SRE, DevOps, release manager are all separately specced agents with their own tool allowlists and model tiers, coordinating through a real message bus and task graph, not one model prompted seven different ways and relabeled. What we learned Frontier coding agents aren't overpriced because the labs are greedy. They're priced for a human making one sharp request at a time, and at that job they're worth it. The moment you turn that into an autonomous, multi-hour, thousand-call swarm, the economics only work if you stop treating "the model" as a single choice and start treating it as a routing problem. Cost as an architecture decision, not just a billing line, is what we're carrying into whatever we build next. What's next for DevForge Model routing today is mostly static, tuned by hand per role. The obvious next step is adaptive routing: let the orchestrator watch the critic's pass/fail history per role and per model, and shift automatically, cheaper model as long as quality holds, escalate the instant it doesn't. Past that: finishing the Redis Streams and Kubernetes/KEDA scaling paths so a swarm can burst across workers, shipping the analytics panel we already built, and closing the gaps in our own API contract, source re-processing, pagination, rate limiting. Longer term, we want the swarm to learn across runs, not just within one, so the fiftieth build on your codebase is measurably cheaper and sharper than the first. And yes, our mascot cat Luna supervised every single line of this build, mostly from the top of a keyboard! ≽^•⩊•^≼ <div