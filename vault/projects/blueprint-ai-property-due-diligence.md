---
slug: "blueprint-ai-property-due-diligence"
url: "https://devpost.com/software/blueprint-ai-property-due-diligence"
title: "BLUEPRINT: AI Property Due Diligence"
hackathon: "Google Cloud Rapid Agent Hackathon"
organization: "Google"
winner: true
words: 795
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# BLUEPRINT: AI Property Due Diligence

> Seven AI agents read public records on any US address, permits, flood zones, EPA data, then run an adversarial AI debate before delivering a buyer risk score. Powered by Elastic Agent Builder MCP.

[Devpost](https://devpost.com/software/blueprint-ai-property-due-diligence) · hackathon [[Google Cloud Rapid Agent Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[civic_government]] [[climate_energy]] [[developer_tools]] [[disaster_emergency]] [[finance_payments]] [[legal_justice]]
  <sub>weak: transportation</sub>
**user** [[legal_professional]] [[researcher]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** elastic-agent-builder, elasticsearch, elser, epa-ejscreen, fastapi, fema-nfhl, gemini, google-cloud-adk, google-cloud-run, javascript, leaflet.js, mcp, nyc-open-data, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blueprint: ai property due diligence

## Body

Most buyers close without knowing the open permits, flood history, or Superfund site nearby. BLUEPRINT finds all of it. Live Elastic MCP connected, 7-agent pipeline ready — before you even type an address. Each card is a real agent making real API calls. The permit database just flagged 30 open filings. Score is 65, verdict is NEGOTIATE, and the AI debate is still running. You're watching it think. Neighbourhood score, air quality, flood history, transit access, everything a buyer should know but rarely does. Five live ES|QL queries, actual query text, actual row counts, and the percolator matched before anyone asked. Brooklyn or LA? Two full analyses in parallel, one head-to-head verdict, deal-breaker in plain English. All 11 Elastic capabilities live, ELSER, RRF fusion, percolator alerts, Agent Builder MCP, one cluster. Six indices, 111 events in memory, 23 MCP tools discovered live from the Agent Builder endpoint. Inspiration Buying a home is the largest financial decision most people ever make - and they do it with almost no information. A 30-minute walkthrough. A seller's disclosure that's legally optional in half the states. A county permit system that takes a human hours to navigate. I wanted to build something that could do what a real estate attorney, a permit researcher, and an environmental consultant do - in 60 seconds, for any address in the US. What it does BLUEPRINT runs seven AI agents against any US address. It checks building permits across 65 city databases, flood zone status from FEMA, earthquake and climate risk from USGS, environmental hazard proximity from EPA EJSCREEN, and neighborhood data from OpenStreetMap - then synthesizes everything into a buyer risk score. The twist: before the final score is delivered, two Gemini agents run an adversarial debate. An OptimistAgent and a PessimistAgent argue the score in opposite directions. The system resolves the tension and delivers a confidence-adjusted verdict with an exact action plan: what to negotiate, what to fix, ranked by risk-point impact. How we built it Google Cloud ADK 2.0 for the multi-agent pipeline - SequentialAgent orchestrates seven LlmAgents, each with FunctionTools for their data source Elastic Agent Builder MCP as the intelligence layer - SynthesisAgent connects over Streamable HTTP MCP and runs ELSER sparse-vector hybrid search (BM25 + RRF-fused) over everything in memory Elasticsearch stores six live indices: property events, synthesis reports, cases, shared data, watchlist, and percolator alerts ES|QL for five cross-reference queries per analysis, surfaced as actual query text in the report Percolator for reverse-search: saved risk profiles match automatically the moment an analysis completes Gemini 3 Flash Preview for all agent reasoning, with Vertex AI fallback FastAPI + SSE for real-time streaming of pipeline progress to the browser Google Cloud Run for deployment Challenges we ran into Getting the adversarial debate to produce stable, non-degenerate scores was harder than expected. Early versions had the Optimist and Pessimist always anchoring at the extremes. We solved it by adding corpus-level percentile anchoring - agents are told where the preliminary score sits relative to all properties ever analysed, which pulls the debate toward a realistic range. The MCP transport layer also had a subtle bug where the connection would silently drop after the first tool call. Took a full debugging session to trace it to a keep-alive issue in the Streamable HTTP transport. Accomplishments that we're proud of The percolator felt like magic the first time it worked. You run an analysis, and before you've scrolled to the bottom, a saved risk profile has already matched and surfaced an alert - without being asked. That's Elasticsearch doing work the user didn't know to ask for. The adversarial debate architecture is something we haven't seen in property research tools. The fact that the UI shows the tug-of-war - Optimist at 48, Pessimist at 88, settled at 70 - makes the AI's reasoning visible instead of opaque. What we learned ELSER sparse-vector search is genuinely better than keyword search for this use case. Property reports contain domain jargon, permit codes, and environmental terminology that exact-match search misses. ELSER surfaces semantically related findings across the corpus without needing manual synonym lists. Building with MCP changed how we thought about AI tool design. Tools as a protocol - not hardcoded function calls - meant we could swap, extend, and debug the intelligence layer without touching the agent code. What's next for BLUEPRINT: AI Property Due Diligence Watchlist alerts : properties already in the watchlist index get re-analysed automatically when new permit filings or FEMA remapping events come in National permit coverage : 65 cities today, working toward all 50 states via Socrata and county API partnerships Lender integration : export the risk report as a structured PDF for mortgage underwriters Portfolio mode : run 10 properties in parallel for investors comparing acquisition targets <div