---
slug: "aeroguard-tech"
url: "https://devpost.com/software/aeroguard-tech"
title: "AeroGuard.tech"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 597
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# AeroGuard.tech

> AeroGuard: A DePIN response network. Edge nodes detect disasters offline, AI agents dispatch help, and Solana ensures trustless aid. From physical truth to cloud action.

[Devpost](https://devpost.com/software/aeroguard-tech) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[measured_ablation]] [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[disaster_emergency]] [[health_clinical]]
**substrate** [[geospatial]] [[video_visual]]

**stack** css, javascript, phython, typescript

## How they structured the write-up

- 🌍 the problem we’re solving
- 🏗️ system architecture (monorepo)

## Body

logo 🛡️ A.E.G.I.S. Garden A dvanced E ncryption & G lobal I ntrusion S ystem http://googleusercontent.com/image_generation_content/4 An Industry-Grade, Real-Time SOC & Disaster Response Platform A.E.G.I.S. Garden is a real-time Security Operations Center (SOC)–style decision platform designed to operate in high-chaos, high-stakes environments such as cyber incidents, infrastructure failures, and disaster response scenarios. At its core, A.E.G.I.S. helps teams detect incidents, triage them intelligently, prioritize what actually matters, coordinate responses, and maintain trust and accountability — all in real time . 🌍 The Problem We’re Solving In real-world operations — whether disaster response or cybersecurity — teams face the same challenges: Noise: Too many alerts, not enough clarity. Opacity: No explanation for why something is urgent. Latency: Slow coordination across people and systems. Distrust: Lack of trust when money, identity, or decisions are involved. Fragility: Systems that fail silently or "work only in demos." Most dashboards visualize data. A.E.G.I.S. Garden operationalizes decisions. 🏗️ System Architecture (Monorepo) The backend and frontend are fully decoupled but connected via strict schemas, WebSockets, and shared audit semantics. AEGIS-Garden/ ├── packages/ │ ├── api/ # FastAPI backend (Real-time, AI, Audit, WS) │ ├── dashboard/ # React + Vite SOC UI (The "Garden" Interface) │ ├── solana-demo/ # Trust, Identity, and Fund-control primitives │ └── tests/ # E2E and Unit testing suites └── scripts/ # Deployment and Mode switching ## 🧩 Core Platform Components & Technologies --- ## 🔮 Google Gemini — Multimodal AI Reasoning Engine **How we use it:** - Analyzes incidents using _text, images, and structured data_ - Produces **strict JSON outputs** for automation - Generates **priority scores**, **confidence levels**, and _human-readable rationales_ - Supports **function calling** (dispatch, request evidence, freeze flows) - Performs _self-validation_ to reduce hallucinations **Why it matters:** _Gemini turns raw alerts into explainable decisions, not black-box scores._ --- ## 🔁 OpenRouter — LLM Infrastructure & Resilience Layer **How we use it:** - Routes tasks across multiple models/providers - **Smart Routing:** chooses models based on _latency, cost, and reasoning depth_ - Enables **A/B testing** of reasoning quality - Provides fallback if a provider fails **Why it matters:** _OpenRouter prevents single-model dependency and enables long-term system resilience._ --- ## ❄️ Snowflake — Predictive Analytics & Foresight **How we use it:** - **Snowpipe Streaming** for real-time ingestion - **Snowflake Cortex** for impact prediction, priority ranking, and demand forecasting - Time-series analytics on evolving incidents - **External Functions** to trigger actions outside Snowflake **Why it matters:** _Snowflake makes A.E.G.I.S. predictive, not just reactive._ --- ## 🍃 MongoDB Atlas — Real-Time State & Matching **How we use it:** - Stores incidents, triage results, and audit logs - **Change Streams:** push updates instantly via WebSockets - **Vector Search:** semantic matching (incident ↔ responder) - **Geospatial Queries:** proximity-based decisions (Ottawa region) - **TTL Indexes:** automatic cleanup of stale data **Why it matters:** _MongoDB acts as the real-time nervous system of the platform._ --- ## 🟣 Solana — Trust, Identity & Controlled Execution **How we use it:** - **Token Extensions (Transfer Hooks):** restrict spending - **Time-locked funds** to prevent misuse - **Compressed NFTs:** used as verified responder identities - **Blinks:** for one-click donation or action flows - On-chain auditability for transparency **Why it matters:** _Solana enables trustless control, especially critical when money is involved during crises._ --- ## 🎙️ ElevenLabs — Human-Centered Alerting **How we use it:** - Generates real-time **voice alerts** for High/Critical incidents - Audio plays automatically in the UI _(with user opt-in)_ - Alerts are **rate-limited** to avoid overload - Every alert is logged in the audit trail **Why it matters:** _Dashboards fail when people are distracted — voice cuts through chaos._ <div