---
slug: "loop-customer-whisperer"
url: "https://devpost.com/software/loop-customer-whisperer"
title: "Loop — Customer Whisperer"
hackathon: "Slack Agent Builder Challenge"
organization: "Salesforce"
winner: true
words: 353
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "substrate/geospatial"
---

# Loop — Customer Whisperer

> The teammate who's already read the thread.

[Devpost](https://devpost.com/software/loop-customer-whisperer) · hackathon [[Slack Agent Builder Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[housing_homeless]]
**substrate** [[geospatial]]

**stack** bolt, javascript, libsql, mcp, node.js, salesforce, slack, turso

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for loop — customer whisperer

## Body

Inspiration Support and sales teams live in Slack. The worst moment in any customer conversation is the handoff, the person pulled in has zero context and has to reconstruct it while the customer waits. We wanted an agent that eliminates "can you catch me up?" entirely. What it does Loop watches customer channels. When a thread is handed to someone, it DMs them a brief: the synthesized issue, live Salesforce case context, related prior threads found by workspace search, a routing suggestion for the strongest expert, and a one-click AI-drafted reply. It keeps a living canvas dossier per thread, answers follow-ups with full context, and remembers each user's own past conversations. How we built it Bolt for JavaScript for all Slack surfaces (events, actions, modals, commands, OAuth install). Claude (Opus 4.8) via the Anthropic SDK for handoff classification, brief synthesis, and reply drafting. MCP twice, through the Anthropic MCP connector: the "Salesforce" hosted MCP server for live case data, and the "Slack" MCP server for "seen this before" search and canvases. Multi-tenant from the ground up: "Turso" data layer, per-workspace encrypted install tokens, per-org Salesforce connect (OAuth 2.1 + PKCE), and a per-workspace Anthropic key entered in the App Home Settings modal. Deployed on Render. Challenges we ran into Making agentic MCP calls fast enough for a Slack interaction (streaming + low effort), keeping every enrichment step gracefully degradable so a brief always sends, and turning a single-workspace prototype into a real multi-tenant app with encrypted, isolated per-org data and a durable free datastore (Turso). Accomplishments that we're proud of A genuinely ambient agent, not a chatbot you summon, but one that acts at the exact moment context is lost, that's too a fully installable, multi-tenant, Marketplace-ready product. What we learned The MCP connector makes "bring your own SaaS data" surprisingly clean; and the hardest part of a Slack agent isn't the AI, it's the multi-tenant plumbing (OAuth, encryption, isolation, uninstall hygiene). What's next for Loop — Customer Whisperer Proactive SLA nudges for stale threads, sentiment/at-risk detection, a resolution knowledge base that makes draft replies cite the known fix, and Salesforce write-back. <div