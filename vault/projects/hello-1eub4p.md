---
slug: "hello-1eub4p"
url: "https://devpost.com/software/hello-1eub4p"
title: "PrismLines"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 806
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# PrismLines

> Ride-or-Die on a topic? Put your money where your heart is. PrismLines is an end-to-end experience that makes betting on your favourite topics as easy as picking a belief.

[Devpost](https://devpost.com/software/hello-1eub4p) · hackathon [[NexHacks]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** langgraph, openai, polymarket, python, react, supabase, tavily, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for prismlines

## Body

Explore Community Funds Fund Explore 2 Individual Fund View Overall Portfolio View + Analytics Friends Profile view Chrome extension view 1 Chrome Extension view 2 AI Agent Architecture Inspiration None of us are big gamblers. But we do have strong opinions about the world, politics, sports, tech launches, and pop culture. We kept thinking it would be fun to put a small amount of money behind what we genuinely care about, except prediction markets still feel like a trader’s tool. We did not have the betting knowledge, the time to research properly, or the confidence to build strategies without guessing. So we built PrismLines, a way to “bet on your interests” while still enjoying the experience, with AI agents that do the heavy lifting for research, modeling, and strategy construction, plus a UI that makes risk and payoff actually understandable. What it does PrismLines is an end-to-end Polymarket trading assistant that helps beginners and power users visualize risk, build strategies, and execute trades with confidence. AI-guided trading: You pick a topic or market you care about, and our agents summarize context, key drivers, and what matters for the bet. TradFi-style insight: We generate payoff intuition and risk framing so users understand what they are committing to. Parlays made visual: Complex strategy building becomes draw-a-line simple. You connect markets by drawing lines between them to form multi-leg positions. Instead of learning jargon, you visually link the bets you want to combine. One flow, start to finish: Discover, research, strategy, risk explanation, and optional execution. Add your Friends! Socialize and add others or your friends to see what funds they own or created. How we built it We designed PrismLines with LangGraph to allow for easy state management and transition between nodes (different agents). AI agent network (LangGraph) Orchestration agent : Implements the core event loop and runtime environment. It manages state persistence and inter-process communication (IPC), enforcing strict Pydantic schema validation on all agent outputs to ensure type safety across the asynchronous pipeline. Research agents : Executes the information retrieval workflow. It utilizes Tavily Search for unstructured data aggregation, followed by a recursive extraction loop to parse HTML content. The resulting dataset is synthesized via an LLM into a structured investment thesis with cited evidence. Allocator agents : Interacts with the Polymarket Gamma API to retrieve real-time order book data (CLOB). It performs server-side filtering for liquidity clustering and bid-ask spread constraints, then applies the Kelly Criterion sizing algorithms to map conviction scores into a probabilistic portfolio allocation configuration. Polymarket integration Pulled market data and structured it into formats the agents can reason over, like markets, outcomes, and pricing or odds. UI and UX for strategy construction Built the core interaction where connecting bets is literally drawing lines, turning multi-market strategies into a visual, beginner-friendly workflow. Challenges we ran into Making agents reliable under hackathon time: Getting multiple agents to cooperate without loops, contradictions, or noisy outputs was harder than writing a single chatbot. Orchestration complexity: We had to enforce structure with roles, tool boundaries, and output formats so the system stayed consistent and professional. Polymarket plus agents at the same time: Debugging agent behavior while integrating Polymarket market data created a moving target. When outputs looked wrong, we had to figure out if it was data handling, modeling logic, prompts, tooling, or orchestration. Turning complex strategies into simple UX: Parlays and multi-leg positions can get complicated fast, so we had to keep the UI intuitive without oversimplifying. Accomplishments that we're proud of This was our first time building real AI agents with LangChain, and we learned the framework fast enough to ship in under 24 hours. We built an agent network with an orchestrator, research agents, and action agents that performs multiple functions end-to-end, not just a single assistant prompt. We created a novel strategy-building interaction, parlays by drawing lines, which makes advanced concepts approachable and visual. We delivered a product that feels like a professional trading tool while still being friendly to beginners. What we learned Agent systems need strong structure, clear tool contracts, and careful control over outputs. Reliability and UX are often harder than raw model capability. Combining live market data with multi-step reasoning requires transparent assumptions and guardrails, otherwise users cannot trust the output. Great visualization and interaction design can make complex trading concepts feel natural. What's next for PrismLines Deeper payoff modeling: True P&L curves across probability shifts and time horizons, plus scenario controls for resolve sooner versus later. Multi-market strategy analytics: Portfolio-wide payoff graphs, exposure breakdowns, and correlation-aware modeling. Trade execution and tracking: One-click execution flows, position monitoring, and clear explanations of what changed since entry. Personalized agents: Learn a user’s risk tolerance and interests to recommend strategies and hedges that match their style. Education mode: Built-in explainers so beginners learn strategies as they use them without feeling overwhelmed. <div