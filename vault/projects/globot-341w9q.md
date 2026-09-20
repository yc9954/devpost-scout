---
slug: "globot-341w9q"
url: "https://devpost.com/software/globot-341w9q"
title: "Globot"
hackathon: "Gemini 3 Hackathon"
organization: "Google"
winner: true
words: 420
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/supply_logistics"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Globot

> Multi-Agents. 2M-token compliance analysis. Satellite imagery risk detection. Globot turns sudden supply chain chaos into confident decisions in 60 seconds.

[Devpost](https://devpost.com/software/globot-341w9q) · hackathon [[Gemini 3 Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[disaster_emergency]] [[finance_payments]] [[legal_justice]] [[supply_logistics]]
**user** [[government_staff]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** chromadb, clerk, crewai, deck.gl, fastapi, gemini-3-flash, gemini-embeddings, gemini-vision, python, react, sqlite, typescript, vite, websocket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for globot

## Body

Homepage Introduction Homepage Introduction Homepage Introduction Homepage Introduction Homepage Introduction Homepage Introduction Choose Ports 2D Global Route Real-time Map Human On The Loop Multi-agent roles are working Satellite cloud image analysis (cross-verification of information) Automated decision-making system based on Google services 3D Global Route Real-time Map Real-time system logs Token usage management Route compliance analysis File upload Ship information filling Administrator backend management Inspiration On a Friday at 4:55 PM, the Red Sea crisis erupts. You're responsible for $50 million in cargo, drowning in Excel spreadsheets while Reuters updates flood in. Your boss is yelling. What do you do? This scenario inspired Globot — an Agentic AI system that transforms reactive crisis management into proactive defense . What it does Globot is a 5-Agent AI Reasoning Engine powered by Gemini 3 that: 🔭 Market Sentinel : Monitors geopolitical signals from Reuters/Bloomberg in real-time 🛡️ Risk Hedger : Calculates financial impact of route changes (fuel costs +$180K, freight volatility) 🚢 Logistics Orchestrator : Automatically replans shipping routes to avoid conflict zones 📋 Compliance Manager : Analyzes 500-page insurance policies using Gemini's 2M token context window ⚖️ Adversarial Debate : Red-team tests every decision to prevent AI hallucinations Key Innovation : We use Gemini Vision to analyze satellite imagery, detecting port congestion and canal blockages 6 hours before official announcements. How we built it Backend : Python + FastAPI + CrewAI (Multi-Agent Orchestration) Frontend : React + TypeScript + Deck.gl (3D Globe Visualization) AI : Gemini 3 Flash (Reasoning) + Gemini Vision (Satellite Analysis) + Gemini Embeddings (RAG) Auth : Clerk (Enterprise-grade authentication) Database : SQLite + ChromaDB (Vector Store) Challenges we ran into aiohttp Compatibility : Python 3.13 introduced breaking changes; we implemented monkey patches to maintain CrewAI compatibility Long Context Window : Feeding 500-page legal documents required careful prompt engineering Multimodal Reasoning : Getting Gemini Vision to output structured risk assessments from satellite images Accomplishments we're proud of Visual Risk Intelligence : First supply chain AI to use satellite imagery for early warning Explainable AI : Every decision shows a transparent Chain-of-Thought reasoning process Human-in-the-Loop : All critical decisions require human approval — responsible AI in action What we learned Gemini's multimodal capabilities enable use cases impossible with text-only models Long context windows unlock enterprise document understanding Multi-agent systems are more robust than single-model approaches What's next for Globot Integration with Bloomberg Terminal API for live market data MarineTraffic API for real-time AIS ship tracking Sentinel-2 Satellite API for automated port monitoring Expansion to air freight and rail logistics <div