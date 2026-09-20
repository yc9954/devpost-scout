---
slug: "root4"
url: "https://devpost.com/software/root4"
title: "AfriGov Sentinel"
hackathon: "Elasticsearch Agent Builder Hackathon"
organization: "Elastic"
winner: true
words: 714
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# AfriGov Sentinel

> When a hospital loses power in Lomé, AfriGov Sentinel gets the right person on the phone in 8 seconds — powered by Elastic Agent Builder.

[Devpost](https://devpost.com/software/root4) · hackathon [[Elasticsearch Agent Builder Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[civic_government]] [[developer_tools]] [[health_clinical]]
**user** [[general_public]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** claude-3-7-sonnet, elastic-agent-builder, elastic-cloud, elasticsearch, esql, fastapi, javascript, netlify, python, render

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned
- what's next

## Body

Le diagramme d'architecture du projet. Afrigov Sentinel's Home Page Inspiration West Africa has a governance problem that isn't talked about enough: the gap between when a public service fails and when someone with the power to fix it finds out. A generator fails at a hospital in Lomé. ICU patients are on life support. Who do you call? The SAMU? The ministry? A general hotline that rings for 40 minutes? By the time the right person is reached, hours have passed. This isn't a technology problem — it's a routing problem . The information exists. The responsible official exists. The two just never connect fast enough. AfriGov Sentinel was built to close that gap. What it does AfriGov Sentinel is a civic incident reporting platform powered by a multi-step Elastic AI Agent that transforms a citizen's description into a structured decision in under 10 seconds. A citizen opens the platform, describes the problem, pins the exact location on an interactive map, optionally attaches a photo or video, and hits submit. The Elastic Agent autonomously executes four steps: Semantic search on the incidents index — finds the 5 most contextually similar past cases to ground the analysis in real history ES|QL analytics — queries the region and service for current incident frequency, average severity, and critical count Contact lookup — searches the services_contacts index to identify the exact named official responsible, with direct phone and email LLM reasoning (Claude 3.7 Sonnet) — synthesizes all three data sources into a risk score (0–5), a decision tier, a grounded explanation, and a 3-step action plan Critical incidents ( CRITICAL_ESCALATION ) are automatically logged to an escalations index and surface immediately in the authority dashboard. Authorities access a protected interface showing live incident maps, KPI stats, and escalation queues — with one-click resolution. How we built it Elastic Agent Builder is the core. The agent is configured with platform.core.search , platform.core.execute_esql , and platform.core.generate_esql tools. The system prompt enforces the 4-step pipeline — the agent cannot produce a decision without first running Search and ES|QL. Elasticsearch stores four indices: incidents — citizen reports with geo_point, severity, status services_contacts — 24 named officials across all 5 regions of Togo agent_decisions — every AI decision logged with full context escalations — critical incidents requiring authority action FastAPI orchestrates everything: it indexes the incident, calls the Agent Builder /converse endpoint, logs the decision, and triggers escalation when needed. The frontend is a single HTML file with Leaflet.js for mapping — responsive across mobile and desktop, with address search, GPS geolocation, and photo/video upload. The UI is split into two separate views: citizens report, authorities manage. Challenges we faced The biggest challenge was understanding how Elastic Agent Builder actually sequences tool calls. Early implementations treated it like a single-prompt LLM — one input, one output. The breakthrough came when we restructured the system prompt to explicitly enforce the 4-step pipeline, forcing the agent to ground every decision in real data before reasoning. The second challenge was the API response format. The Agent Builder /converse endpoint returns responses nested inside data.response.message , not at the top level — something that took debugging to discover. Building a dual-interface product (citizen vs. authority) also required thinking carefully about what each user actually needs. Citizens don't need dashboards. Authorities don't need the reporting form. Separating those concerns made both interfaces significantly cleaner. What we learned Elastic Agent Builder is genuinely powerful when used correctly — as an autonomous multi-step reasoning engine, not a prompt wrapper. The moment the agent started using ES|QL to pull real regional statistics before generating a risk score, the quality of decisions jumped dramatically. It stopped making up context and started reasoning from data. We also learned that for civic tech in West Africa, the most important feature isn't the AI — it's the direct contact . Telling a citizen "someone will look into it" is worthless. Telling them "call Dr. Kossi Amevor at +228 22 21 34 56, he is the Regional Health Director for Maritime" is actionable. What's next SMS/USSD interface for citizens without smartphones Automatic weekly reports generated by the agent for each region (Done) Integration with official government ticketing systems Expansion to neighboring countries (Ghana, Benin, Burkina Faso) Real-time push notifications to officials via WhatsApp Business API <div