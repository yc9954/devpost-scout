---
slug: "conjure-m960jz"
url: "https://devpost.com/software/conjure-m960jz"
title: "Conjure"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 690
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/sensor_telemetry"
---

# Conjure

> Turn your vision into reality. With a single prompt create a fully walkable 3D world.

[Devpost](https://devpost.com/software/conjure-m960jz) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[sensor_telemetry]]

**stack** agentverse, fastapi, fetch.ai, fetch.ai-agentverse, google-gemini-api, next.js, npm, pydantic, pytest, python, react, react-three-fiber, tailwind-css, three.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned

## Body

Conjured Living Room GIF Conjured Agent Swarm Description 8/29 of our Agents Inspiration We built Conjure because we wanted to make 3D world creation feel as simple as writing a sentence. During LA Hacks, we kept coming back to the same frustration: most people can describe a space they want, but very few can actually model it. There is a huge gap between imagination and execution. Our goal was to close that gap with an agent-driven system that turns natural language into a walkable world in minutes, not days. We were also excited by the Fetch.ai Agentverse track and wanted to prove that a multi-agent architecture could coordinate real spatial reasoning, not just chat responses. What it does Conjure takes a prompt like “design a cozy two-floor cabin with warm lighting” and generates a complete 3D interior that users can walk through in the browser. We make heavy use of Fetch.AI and Agentverse agents for orchestration and task completion. It does three things well: Converts user intent into a structured world plan (rooms, dimensions, style, lighting, furniture, navigation). Runs a coordinated multi-agent build pipeline and streams live progress so users can see what each agent is doing. Produces a playable, editable world spec that can be regenerated after user edits without losing the high-level design intent. Instead of presenting generation as a black box, we expose the “thinking process” through real-time activity updates, which makes the experience more transparent and much more engaging. How we built it We built Conjure as a full-stack system with a strict shared schema between agents and rendering. Backend orchestration: FastAPI service with a staged agent pipeline. Core data model: a central WorldSpec object that every agent reads and updates. Pipeline strategy: sequential planning agents first, parallel build agents in the middle, then validation and post-processing agents. All powered by Agentverse. Frontend: Next.js + React Three Fiber/Three.js for real-time rendering and first-person navigation. Realtime UX: WebSocket status streaming so users can watch generation progress from intent parsing to final world assembly. A key architectural decision was making each agent operate on the same canonical spec. That gave us deterministic handoffs and cleaner debugging: if something looked wrong visually, we could trace the exact section of the world spec that introduced it. We also enforced geometric guardrails (grid and dimension validation) to keep outputs coherent. Conceptually, we treated layout quality like an optimization balance: $$ \text{World Quality} \approx \alpha(\text{coherence}) + \beta(\text{walkability}) + \gamma(\text{style consistency}) - \delta(\text{constraint violations}) $$ This helped us frame tradeoffs when tuning prompts and validators. Challenges we ran into The hardest challenges were around reliability, not feature count. External product integration was brittle. We initially explored real catalog-style furniture linking, but vendor behavior, CORS constraints, and unstable asset endpoints made the experience inconsistent and hard to trust. LLM outputs needed strict guardrails. Natural language generation was strong creatively but sometimes weak spatially. We had to add schema constraints and validation to prevent room overlap, bad dimensions, and placement drift. Frontend/backend type drift risk. Keeping TypeScript world types synchronized with backend schema evolution required discipline; without it, subtle rendering bugs appeared quickly. Edit workflows were computationally expensive. Small user edits sometimes required a broad pipeline rerun. It worked, but it highlighted the need for finer-grained incremental regeneration. Scaling to larger buildings introduced performance pressure. As primitive counts increased, we had to think early about instancing, culling, and render strategy so the walkable experience stayed smooth. What we learned We learned that users care most about trust + responsiveness . A flashy generation means less if the system feels unpredictable. The best results came from combining creative generation with strict structure and visibility. We also learned that architecture simplicity is a competitive advantage in hackathon conditions. A clear staged pipeline and a shared world schema let us move fast without collapsing under complexity. Most importantly, we learned to prioritize deterministic value over fragile novelty. Procedural assets and validated world specs gave us a more reliable product than external dependency-heavy features. That pivot made Conjure better: more stable, more interactive, and more aligned with our core mission of turning plain language into explorable 3D spaces. <div