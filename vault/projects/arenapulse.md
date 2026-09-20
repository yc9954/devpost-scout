---
slug: "arenapulse"
url: "https://devpost.com/software/arenapulse"
title: "ArenaPulse"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 565
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ArenaPulse

> Autonomous crowd-safety & B2B supply coordinator for stadiums, combining real-time surge forecasting, RAG supply-chain checks, and automatic flash deals with human-in-the-loop vetoes.

[Devpost](https://devpost.com/software/arenapulse) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[human_in_the_loop]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[developer_tools]] [[health_clinical]] [[supply_logistics]]
**user** [[legal_professional]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** arize-phoenix, elasticsearch, fastapi, framer-motion, google-adk, google-genai, leaflet-maps, python, react, tailwind-css, typescript, vite, xgboost, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for arenapulse

## Body

Inspiration Imagine 60,000 fans rushing toward a stadium gate at halftime. In stadium operations, critical windows of safety are measured in minutes, but the manual response loop—staff reporting a crush, radios crackling, allocating supplies, and redirecting crowds—typically takes over 18 minutes. Meanwhile, concession stands run out of stock while adjacent stands sit full, leading to invisible, lost revenue. We built ArenaPulse to close this gap. It is an autonomous operations manager for stadiums and large-scale events that acts in seconds. By connecting early crowd density forecasts to real-world logistics, ArenaPulse redirects crowds, dispatches supplies, files restocking orders, and rolls out commerce-boosting deals automatically—while keeping human operators in control. What it does ArenaPulse runs a robust 8-stage multi-agent pipeline: Perception : Triage telemetry events using a fast XGBoost ML model, then run primary Gemini 3 risk assessment. Planning : Decides coordinates-based dispatches, priority levels, and actions. Inventory Allocation : Dynamically allocates stock from adjacent depots. Validation : Prevents overall resource shortfalls. Verification (RAG Loop) : Runs a hybrid dense/sparse vector check in Elasticsearch against real-world constraints (e.g., road closures, lead times). If infeasible, the agent triggers a self-correction loop. Human-in-the-Loop Approval : Pauses high-impact decisions for manual operator approval. Execution : Dispatches supplies and drafts automated B2B purchase orders. Demand Shaping : Pushes targeted flash deals (e.g., "25% off water at East Plaza") to pull fans toward under-utilized vendors. How we built it We structured ArenaPulse as a monorepo containing a React/Vite/TS frontend and a FastAPI backend: The Agent Brain (Gemini 3 + Google Cloud ADK) : The unified google-genai SDK drives all reasoning. The planning core is built using the Agent Development Kit (ADK) as a code-first LlmAgent , autonomously invoking tools. The Database Superpower (Elasticsearch) : Houses vendor locations, inventory, and supply constraints. Elasticsearch powers our geospatial searches, hybrid semantic RAG verification, and real-time ES|QL analytics queries that feed our dashboard charts. Observability (Arize Phoenix) : Auto-instruments every Gemini model call and OTel span. It logs our LLM-Judge evaluations (which score plan safety 1–10) directly into Arize Phoenix traces. Challenges we ran into A major challenge was managing dependencies between the newer Gemini SDK and OpenTelemetry. We resolved this by bypassing the heavy Phoenix server package in favor of the lightweight arize-phoenix-otel package, keeping the container boot fast and robust. We also had to design a reliable self-correction loop to prevent infinite replanning when multiple constraints conflicted. Accomplishments that we're proud of Closed-Loop Action : Built a system that doesn't just display alerts but autonomously acts on them (routing logistics, restock orders, and commerce deals) in under 3 seconds. Intelligent Self-Correction : Implemented a RAG verification loop where the agent catches its own mistakes (like dispatching resources through a closed road), explains the conflict, and drafts a new viable plan. Real-time ES|QL Integration : Successfully wired live Elasticsearch ES|QL analytics to feed the dashboard graphs dynamically, proving production readiness. What we learned Building ArenaPulse proved that multi-agent systems shouldn't just answer questions—they should safely execute real-world actions. We learned how to design robust fallback heuristics so that the application gracefully degrades if third-party credentials run out of quota during an event. What's next for ArenaPulse We plan to integrate real camera feed object-detection data (YOLO/CV) to replace simulated crowd density, deploy the backend to Google Cloud Run, and expand the supplier portal so concession vendors can bid on dynamic restock contracts in real-time. <div