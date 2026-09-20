---
slug: "tradewizard-g6hqr5"
url: "https://devpost.com/software/tradewizard-g6hqr5"
title: "TradeWizard"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 739
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/scientific_research"
  - "user/researcher"
  - "substrate/geospatial"
---

# TradeWizard

> TradeWizard helps people navigate uncertainty with confidence when money is on the line.

[Devpost](https://devpost.com/software/tradewizard-g6hqr5) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]] [[scientific_research]]
**user** [[researcher]]
**substrate** [[geospatial]]

**stack** amazon-web-services, bedrock, next.js, python, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tradewizard

## Body

Inspiration Prediction markets promise one of the purest signals about the future, yet most people interact with them as speculation rather than informed decision-making. We were inspired by the gap between the sophistication of professional analysts and the experience available to everyday traders. At the same time, a new generation of foundation models; particularly those delivered through Amazon Web Services and its Nova family; made it possible to rethink how real-time intelligence could be delivered at scale and at low cost. TradeWizard was born from the belief that prediction markets shouldn’t just aggregate opinions; they should provide structured, explainable intelligence that helps people act with confidence. What it does TradeWizard is an AI-powered intelligence layer that sits on top of live prediction markets such as Polymarket and transforms raw data into explainable trading strategies. Instead of forcing users to interpret news, polling shifts, sentiment swings, and liquidity signals on their own, TradeWizard deploys coordinated AI agents that analyze markets continuously and synthesize their findings into clear recommendations. The system explains probabilities, highlights catalysts, identifies risks, and proposes entry or exit strategies so users trade with structured reasoning rather than instinct. In short, TradeWizard turns prediction markets from information overload into guided decision environments. How we built it TradeWizard is built as a multi-agent intelligence platform orchestrated through LangGraph workflows from LangChain. More than a dozen specialized agents run in parallel, analyzing news, polling data, market microstructure, sentiment signals, and risk dynamics before feeding their outputs into a consensus engine that produces a final strategy thesis. The backend is split across Node.js and Python services, connected through shared state pipelines, with data persistence handled by Supabase and observability powered by Opik. A major architectural focus was deep integration with Amazon Nova models through Amazon Bedrock. Nova enables long-context reasoning, tool-calling, and low-cost inference, allowing us to scale autonomous agents without exploding compute costs. This made it feasible to run multiple agents per market and still deliver near-real-time insights. Challenges we ran into One of the hardest challenges was orchestration complexity. Multi-agent systems quickly become difficult to coordinate, especially when each agent may call tools, retrieve memory, or trigger follow-up reasoning. Ensuring deterministic workflows, reproducibility, and explainability required careful state management and checkpointing. Another major challenge was cost control. Running multiple agents per market can become expensive if model selection isn’t optimized. Integrating Amazon Nova helped dramatically reduce inference costs, but we still had to design caching layers, timeout rules, and adaptive tool usage to maintain sustainability at scale. We also had to design the system so outputs remained understandable to humans. Producing insights is easy; producing insights that people trust is much harder. Accomplishments that we're proud of We’re proud that TradeWizard isn’t just a prototype; it’s a production-ready intelligence system with real agent orchestration, real market data, and real explainable outputs. Our deepest technical achievement is the successful integration of Amazon Nova models across our agent workflows, enabling long-context reasoning and tool-driven analysis at a fraction of the cost of comparable models. This allowed us to move beyond single-model prompts and toward a true autonomous intelligence architecture. We’re also proud of the system’s explainability: every recommendation includes reasoning, risk factors, and invalidation scenarios, which builds trust and usability. What we learned We learned that model choice is not just about intelligence; it’s about economics. The availability of Nova models changed our architecture because lower inference costs made multi-agent reasoning viable in production rather than just in demos. We also learned that the hardest part of AI systems isn’t generation; it’s coordination. Designing workflows where agents collaborate, critique each other, and converge on a thesis requires more product thinking than model tuning. Most importantly, we learned that users don’t want predictions; they want clarity. The value lies in structured reasoning, not raw output. What's next for TradeWizard Our next step is to deepen Nova-driven optimization by benchmarking each agent against different Nova variants and dynamically routing tasks to the most cost-effective model. This will allow TradeWizard to scale intelligence coverage across thousands of markets without sacrificing responsiveness or affordability. We’re also completing the user interface to deliver a full intelligence dashboard, expanding into additional event categories beyond politics, and building performance tracking so strategies can be evaluated against real outcomes. Long term, TradeWizard aims to become the default intelligence layer for event-driven markets; a system where anyone can trade the future with the analytical support once reserved for professionals. <div