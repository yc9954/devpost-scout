---
slug: "campaignpilot-cross-system-marketing-intelligence-agent"
url: "https://devpost.com/software/campaignpilot-cross-system-marketing-intelligence-agent"
title: "CampaignPilot: Cross-System Marketing Intelligence Agent"
hackathon: "Elasticsearch Agent Builder Hackathon"
organization: "Elastic"
winner: true
words: 560
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# CampaignPilot: Cross-System Marketing Intelligence Agent

> When CPA spikes, Google Ads says "optimize bids." CampaignPilot checks your website, products, and support tickets — and tells you it's your CDN that crashed. 18 ES|QL tools, ELSER search, 11 indices.

[Devpost](https://devpost.com/software/campaignpilot-cross-system-marketing-intelligence-agent) · hackathon [[Elasticsearch Agent Builder Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[health_clinical]] [[retail_commerce]]
**substrate** [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[web_dom]]

**stack** a2a, elastic-agent-builder, elastic-workflows, elasticsearch, elser, es|ql, kibana, mcp, python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for campaignpilot: cross-system marketing intelligence agent

## Body

Inspiration Every marketing team runs the same playbook when CPA spikes: check bids, check creatives, check audiences. But the real cause is often invisible — a CDN outage crashing your landing page, a product price increase killing conversions, or a wave of support complaints driving churn. These root causes live in completely separate systems that no ad platform connects. We built CampaignPilot to answer one question: What if an AI agent could reason across ads, website, product, AND support data to find the real root cause automatically? What it does CampaignPilot is a cross-system marketing intelligence agent that monitors multi-channel ad campaigns in real time. When anomalies occur, the agent doesn't just analyze ad metrics — it automatically investigates website health, product catalog changes, and customer support sentiment to deliver a root cause diagnosis with actionable recommendations. Example: CPA spiked 130% → Agent checks ads (✅ normal) → checks website (🔴 CDN degraded, 6800ms load time) → checks support (✅ normal) → Diagnosis: WEBSITE-LEVEL problem, route to engineering, not marketing. How we built it 11 Elasticsearch indices with 22,000+ documents covering campaigns, channel metrics, creative assets, audience segments, website events, product catalog, and support tickets 18 custom tools in Agent Builder: 11 ES|QL query tools for structured analytics, 3 ELSER semantic search tools for natural language search, and 4 platform tools LOOKUP JOIN for cross-index campaign correlation semantic_text fields (×7) enabling natural language search across competitors, creatives, and support tickets 3 Elastic Workflows for automated campaign optimization, budget reallocation, and daily briefing generation Custom Streamlit frontend with real-time dashboard, anomaly scanner, agent chat, and action log MCP Server + A2A Protocol for external integration Challenges we ran into The main challenge was designing the agent's reasoning flow. A naive agent stops after checking ad metrics and concludes "creatives are fine." We needed the agent to reliably cross system boundaries — from ads → website → product → support — every time. We solved this by designing a structured system prompt with an explicit cross-system root cause analysis step and a classification table (AD-LEVEL / WEBSITE-LEVEL / PRODUCT-LEVEL / CUSTOMER-LEVEL) that guides the agent's reasoning path. Accomplishments that we're proud of The agent can correctly diagnose that a CDN outage (not bad creatives) caused a CPA spike — a conclusion that requires reasoning across 3 separate data sources 18 tools working together through Agent Builder's orchestration, with the agent autonomously selecting the right tool at each step A complete Streamlit dashboard that gives marketers a single-pane view across all campaigns, anomalies, and agent conversations What we learned ES|QL is remarkably powerful for time-series anomaly detection with STATS + EVAL + CASE patterns ELSER semantic search transforms support ticket investigation from keyword matching to intent understanding The real differentiator isn't more tools — it's teaching the agent when to cross system boundaries Agent Builder + ES|QL + ELSER is a surprisingly complete stack for building production-grade AI agents What's next for CampaignPilot: Cross-System Marketing Intelligence Agent Real data integration — connecting to live Google Ads, Meta Ads, and Google Analytics APIs Multi-agent architecture — specialized agents for each data domain (ads, website, support) coordinated by an orchestrator agent Automated remediation — moving from "recommend actions" to "execute actions" with human-in-the-loop approval via Elastic Workflows Alerting pipeline — proactive anomaly detection using Elasticsearch Watcher that triggers the agent before a human notices <div