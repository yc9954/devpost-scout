---
slug: "standin-skpgje"
url: "https://devpost.com/software/standin-skpgje"
title: "StandIn"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 1073
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/legal_justice"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# StandIn

> StandIn on Business.

[Devpost](https://devpost.com/software/standin-skpgje) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[multi_agent]] [[on_device_local]] [[retrieval_grounding]] [[structural_withholding]]
**domain** [[legal_justice]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** asusgx10, auth0, fetch.ai, gemini, gemma, mongodb, python, uagent, vite

## How they structured the write-up

- the problem
- what standin can do for you
- architecture
- how does standin stand out?
- challenges we ran into
- accomplishments we're proud of
- tech stack
- what's next

## Body

StandIn StandIn is a network of agents that represent different individuals at an organisation to gather updates and share scoped context for low-stakes tasks, allowing users to free up their brain space for high-stakes strategy and decision making. The Problem Atlassian found that meetings are ineffective 72% of the time . Microsoft's Work Trend Index identified inefficient meetings as the number one productivity disruptor . Otter.ai estimated that cutting unnecessary meeting attendance could save companies more than 5,000 employees over $100 million per year . But the real inspiration came from personal experiences. When our team first got together, what baffled us was how much time we spent attending meetings even as interns. That made no sense. Meetings consume not just time, but brain space: attending them, following up on them, chasing action items, updating briefs, scheduling follow-up calls. While the rise of agentic AI has accelerated productivity -- automating summaries, notifications, and admin tasks -- its potential hasn't been fully applied here. The missing piece is that agents that don't just act for one user in isolation, but communicate and coordinate across users proactively. The urgent question we're tackeling: How do we make more time for the tasks that matter the most? That's why we came up with a system to safely gather, verify, and route. What StandIn Can Do For You Before StandIn After StandIn 3 back-and-forth Slack messages to find a meeting time Agent negotiates a shared slot and adds it to both calendars automatically Action items buried in meeting notes Tickets created and assigned to the right stakeholders instantly Catching up on Slack threads after a long focus block Summarised, scoped update delivered to you on demand Architecture User sends a query | v StandIn Orchestrator Agent (Fetch.ai uAgent) | | Gemini classifies intent | Delegates to capability agent v Capability Agent Router | _____|___________________ | | | v v v status_ history_ perform_ agent agent action_agent | v Calendar / Jira / Slack | | raw data returned v GX10 Trust Layer (local) | | filters sensitive content | redacted output only leaves boundary v Orchestrator assembles answer | v User receives response Why this architecture? Fetch.ai uAgents handle inter-agent communication and identity — each agent can represent a distinct user with its own context boundary. Gemini classifies intent at the orchestrator level, routing queries to the right capability without exposing full context to each agent. ASUS GX10 + Gemma 3:4B via Ollama runs the trust layer locally — raw workplace data (Slack messages, calendar details, Jira tickets) never leaves the trusted hardware boundary. RAG grounds responses in live workspace context rather than hallucinated summaries. Auth0 for AI Agents three primitives wired across the agent network. Token Vault lets the Status Agent act as the requesting user when calling Slack each brief pulls that user's personal OAuth token rather than a shared service account, so the data scoped to their channels. CIBA turns the approval gate from a REST endpoint into a second-device push confirmation. FGA enforces document-level read permissions in the Historical Agent at query time, not after synthesis. How does StandIn stand out? StandIn is not a meeting AI summariser or a personal Claude -- it's the only system where AI agents negotiate on behalf of multiple users simultaneously, rather than acting as a personal assistant for one. It sends role-specific agents to exchange scoped updates before the meeting, verifies contradictions across those agents, redacts sensitive context locally on the ASUS GX10, and only escalates when human judgment is actually required and proactively notifies users. Challenges We Ran Into Making local AI production-reliable. Installing Gemma 3:4B via Ollama was step one. The real work was proving the system was actually invoking the local model on every call, that valid output was being correctly parsed, and that malformed or hallucinated responses were safely rejected before corrupting downstream actions. Designing a privacy boundary that actually holds. Multi-agent systems create a subtle privacy risk: raw workplace data gets fetched somewhere before it gets filtered. Our initial architecture fetched on the user's machine and sent raw data to the GX10 for redaction still local, but not airtight. We redesigned so ingestion happens on the GX10 first, meaning raw workplace context never leaves the trusted hardware boundary. Only redacted, scoped output flows back to the orchestrator. Choreographing agents that don't know each other. Designing the communication protocol between Fetch.ai uAgents, the Gemini intent classifier, and three capability agents required careful thinking about failure modes: what happens when an agent times out, returns ambiguous intent, or receives cross-user context it shouldn't have? We built explicit scoping rules to prevent context bleed between agents representing different users. Accomplishments We're Proud Of We shipped a real end-to-end coordination loop. A natural language query travels from a Fetch.ai uAgent through intent classification, gets routed to the right capability agent, hits live integrations (Calendar, Slack, Jira), passes through a local trust layer on the GX10, and returns a grounded answer. No mocked responses. We made privacy a design constraint, not an afterthought. Gemma 3:4B runs entirely on the ASUS GX10 — sensitive workplace context never touches an external model. For enterprise deployment, that's the difference between a tool legal approves and one they block. We validated a new coordination paradigm. Most AI tools are personal and siloed. StandIn's agents negotiate across users — finding shared calendar slots, assigning tasks to the right people — rather than acting in isolation. That's the core unlock, and we got it working. Tech Stack Layer Technology Why Agent framework Fetch.ai uAgents Enables distinct agent identities and inter-agent messaging across users Intent classification Gemini Fast, accurate routing at the orchestrator level Local AI model Gemma 3:4B via Ollama Keeps sensitive data on-device; no external model calls for trust layer Trust hardware ASUS GX10 Dedicated local compute for the privacy boundary Retrieval RAG Grounds responses in live workspace data Integrations Google Calendar, Slack, Jira Core coordination surfaces Backend Python Agent logic and orchestration Frontend Vite Lightweight interface for user queries What's Next We've already spoken with employers and working professionals who immediately recognized the pain StandIn targets, so the next step is to scale and expand this to be a product that institutions can benefit from. Expand the agent network to support more users coordinating simultaneously Add support for more integrations (Notion, Linear, Microsoft Teams) Harden the trust layer with role-based context scoping Explore a mobile interface for on-the-go async coordination <div