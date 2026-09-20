---
slug: "marketverse-zgjmlv"
url: "https://devpost.com/software/marketverse-zgjmlv"
title: "MarketVerse"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 621
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
---

# MarketVerse

> Simulate 24 months of startup reality in 60 seconds. AI agents play your customers, competitors, and investors, so you know what works before you build.

[Devpost](https://devpost.com/software/marketverse-zgjmlv) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**substrate** [[document_pdf]] [[sensor_telemetry]]

**stack** anthropic, claude, fastapi, next, python, react, recharts, server-side-events, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for marketverse

## Body

Home page Simulation Data entry page Simulation done and result page Investors and Competitor and AI recommendation Changes founder can do and resimulate Inspiration Most startups fail not because founders can't build but because they build the wrong thing for the wrong market at the wrong price. Validation is slow, expensive, and often comes too late. We wanted to compress years of market feedback into 60 seconds, before a single line of product code is written. What it does MarketVerse is an AI-powered startup simulator. You describe your startup in one paragraph like name, market, pricing, category and within 60 seconds it: 1) Generates a living market: 20 customer personas, 5 competitors, and 3 investors, each powered by Claude AI with their own budgets, behavior patterns, and decision logic 2) Runs 24 months of simulation: MRR growth, churn, competitor moves, and market events (economic downturns, viral moments, regulatory changes) all unfold in real time via a streaming UI 3) Delivers an investor-grade verdict: confidence score, immediate actions, supporting evidence, and a ranked growth playbook 4) Lets you steer: apply a strategic decision (lower price, launch annual plan, ship mobile app, expand market) and Claude re-simulates all 24 months with that change baked in from day one. How we built it Backend - FastAPI with async SSE streaming. Three Claude models run in parallel during market generation: 'claude-sonnet-4.6' for persona and competitor generation, 'claude-haiku-4.5-20251001' for month-by-month economic evaluation, and 'claude-opus-4.8' for the final verdict. The simulation engine publishes events to in-memory asyncio queues and streams them to the client as Server-Sent Events. Frontend - Next.js 16 with React 19. Four distinct UI states (form → generating → running → results) with live-updating KPI cards, an MRR area chart, a market events feed, and an interactive decision panel. Falls back to a full demo mode if the API isn't reachable. AI Architecture - Each month is evaluated by a Claude model that considers the startup's current metrics, active market modifiers, competitor actions, and persona behavior scores. The final verdict uses Claude Opus to synthesize all 24 months into a structured analysis with evidence, immediate actions, and prioritized recommendations. Challenges we ran into Streaming latency: getting real-time SSE to feel smooth while actual Claude inference was happening required careful async pipelining and a sleep between months to let the UI breathe Structured output reliability: coaxing Claude to return valid JSON month-data on every call, including edge cases like month 1 with no prior data required careful prompt engineering and fallback handling Decision re-simulation UX: making "apply a decision and re-run" feel instant even though it triggers a full new 24-month Claude pipeline meant pre-computing modified startup params on the frontend before the API call Accomplishments that we're proud of A multi-model Claude architecture where three different models handle different layers of the simulation fast and cheap for high-volume per-month evaluation, powerful for final synthesis A streaming UI that makes a 60-second AI pipeline feel like a live market unfolding rather than a loading spinner The decision engine: being able to change one variable and immediately see 24 months of alternate history is genuinely useful for founders What we learned Multi-model architectures where cheaper/faster models handle high-volume tasks (per-month evaluation) and expensive models handle synthesis (verdict) dramatically improve both cost and latency. The trick is designing clean handoffs between them. We also learned that the best AI product demos aren't chatbots they're experiences where the AI is doing something you couldn't do yourself. What's next for MarketVerse Persistent simulation history so founders can compare multiple scenarios side by side Multiplayer mode: two founders simulate competing startups in the same market Export to PDF pitch deck with simulation data as supporting evidence for investor meetings <div