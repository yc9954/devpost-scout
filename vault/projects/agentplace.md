---
slug: "agentplace"
url: "https://devpost.com/software/agentplace"
title: "AgentPlace"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 825
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# AgentPlace

> The AI-native digital marketplace that haggles for you

[Devpost](https://devpost.com/software/agentplace) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[on_device_local]] [[realtime_stream]]
**domain** [[finance_payments]] [[labor_employment]]
**substrate** [[financial_record]] [[structured_db]]

**stack** asi:one, fetch.ai, python, typescript, uagents

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agentplace

## Body

Agent Architecture Customer Job Request Screen Matching & Negotiating Visualization Deals Screen Job Progress Screen Vendor Calendar View Inspiration We were inspired by recent examples of autonomous agent interaction in applications like Moltbook and we wanted to explore how this kind of AI socialization could be more directly beneficial to humans rather than exclusionary toward them. Our entire team has dealt with the exhausting dance of hiring an independent contractors in the past, scouring online listings and negotiating prices for days. We wanted to build something that could meaningfully improve that experience for both sides. What it does AgentPlace is an autonomous marketplace which connects clients and contractors through AI-mediated job requests. Clients submit natural language job requests, which are referenced against our existing vendor network. If suitable contractors are found, the client's agent begins negotiating price with multiple vendor's agents using context about their respective users and vendors such as experience, expected wages by job type, distance traveled, and past interactions. If the agents reach a deal, the client can approve it and handle payment and job tracking from end to end within the platform. This gives clients control and visibility on the entire process. Contractors have their own dashboards for managing upcoming jobs and filling out profile information to strengthen how their negotiating agents advocate for them. Contractors are able to list their own desired hours and income then sit back while their agent actively finds and schedules jobs for them. How we built it We built our multi-agent system on top of Fetch.ai’s uAgents framework. This let us take advantage of existing inter-agent communication standards and protocols while focusing our time on designing AgentPlace’s core product experience. Because AgentPlace is a web app, we were also able to integrate supporting infrastructure like MCP servers for negotiation workflows and register our agents through Fetch.ai’s AgentVerse for discovery and orchestration. This stack gave us the flexibility to prototype complex agent interactions while still delivering a usable interface for both clients and contractors. Challenges we ran into Agent Orchestration We had to coordinate multiple locally running agents, including negotiator agents, orchestrated through a mailbox agent deployed on AgentVerse. Managing communication flow and state across these agents was non-trivial. Natural Language to Structured Jobs Turning open-ended job requests into well-defined job objects required building agent pipelines that could interpret, structure, and validate user input without requiring a centralized database of every possible task they could do. General-Purpose Agent Diversity We designed a variety of general-purpose agents responsible for different parts of the user journey, which introduced challenges around specialization, context sharing, and reliability. Among these are AI workflows, the ASI1 orchestrator, individualized agents per client and contractor, and both matching and ranking agents. This separation enabled the system to be accurate and specialized, but introduced a thick layer of complexity. Payment Protocol Integration: Implementing the full Fetch.ai Agent Payment Protocol with on-chain verification meant wiring up cosmpy for ledger queries, handling gRPC DNS resolution issues, and building an autonomous buyer agent state machine that could handle every edge case (network failures, invalid transactions, declined payments) without human intervention. Accomplishments that we're proud of We’re proud of how ambitious we were in tackling user needs through agents instead of defaulting to simpler, non-agent solutions. We leaned into the complexity of autonomous negotiation rather than avoiding it. We’re incredibly proud of the intuitiveness of our UX. Both contractors and clients can easily understand how AgentPlace represents them and helps them reach better deals without needing to understand the underlying agent systems. What we learned Building AgentPlace taught us that the hardest part of agentic systems isn't the AI -- it's the orchestration. Making 24 agents cooperate reliably, handle failures gracefully, and produce outcomes that actually help humans required as much systems engineering as it did AI design. We also learned that the Fetch.ai ecosystem provides genuinely useful primitives for multi-agent systems. The uAgents framework, Agentverse mailbox, Almanac registration, and the standardized payment protocol gave us building blocks that would have taken weeks to build from scratch. The fact that our agents can be discovered and interacted with by any agent on the network -- not just ours -- opens up possibilities we hadn't originally considered. We also learned that UX for agent systems is an unsolved design problem. Users need to trust their agents without understanding the underlying protocols. Our solution -- streaming protocol events with human-readable labels -- bridges that gap. What's next for AgentPlace Our next step is validation. We want to test AgentPlace with real contractors and clients to ensure the agents and workflows we’ve built actually address their needs, particularly around client acquisition and price negotiation. We are also interested in incorporating richer external data, like localized job pricing and market trends, so negotiating agents can make more informed decisions. Longer term, we want to continue expanding AgentPlace’s agent infrastructure and explore how autonomous negotiation could apply across other contracting and service marketplaces. <div