---
slug: "chronos-a71yqo"
url: "https://devpost.com/software/chronos-a71yqo"
title: "CHRONOS"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 387
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/climate_energy"
  - "domain/supply_logistics"
  - "user/general_public"
  - "substrate/geospatial"
---

# CHRONOS

> CHRONOS: The Self-Healing Brain for Weather-Resilient Logistics.

[Devpost](https://devpost.com/software/chronos-a71yqo) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[climate_energy]] [[supply_logistics]]
**user** [[general_public]]
**substrate** [[geospatial]]

**stack** firebase, gemini, javascript, node.js

## How they structured the write-up

- the story of chronos

## Body

deploy cargo sentinel report landing page dashboard The Story of CHRONOS Inspiration The inspiration for CHRONOS came from witnessing the fragility of global trade during recent geopolitical and climate-driven disruptions. We realized that while we live in an era of "big data," logistics managers are still stuck in a reactive loop—identifying problems only after they have caused significant delays. We wanted to build a system that doesn't just watch the world happen, but actively thinks ahead to solve problems before they manifest. How We Built It CHRONOS was architected as an AI-native "digital twin" of the global supply chain. The Brain : We utilized Google Gemini 2.5 to power a multi-agent framework. The Logic : We implemented a recursive Reflexion Loop where a Planner Agent and a Critic Agent debate routing options. The Math : The Critic Agent audits routes using a weighted efficiency score $S$, calculated as: $$S = w_1(T_{delta}) + w_2(C_{cost}) + w_3(CO_2)$$ where the system optimizes for minimal time delay, cost increase, and carbon footprint. The Visualization : The frontend was built using React, Vite, and Three.js to create a real-time 3D globe. The Infrastructure : We deployed the backend on Google Cloud Run and used Firebase Firestore for real-time data synchronization between the AI agents and the user dashboard. Challenges We Faced The "Hallucination" Barrier : In early iterations, the LLM would occasionally suggest routes that were geographically impossible. We solved this by implementing Gemini Tool Calling , forcing the agent to verify every waypoint through real-world Geocoding APIs. Data Latency : Relying on official news feeds meant the AI was sometimes hours behind real-world events. This led us to develop the Public Sentinel PWA , allowing crowdsourced "ground truth" data to be ingested directly into the reasoning engine. State Management : Syncing the internal "thoughts" of multiple agents with a 3D frontend in real-time required a robust NoSQL architecture using Firestore listeners. What We Learned Building CHRONOS taught us that the future of software isn't just about better interfaces, but about autonomous agency . We learned how to move beyond simple prompt-engineering into complex agentic workflows where AI models critique their own logic to ensure operational safety. Most importantly, we saw how AI can be a direct tool for sustainability by making carbon-aware routing a mathematical necessity rather than an afterthought. <div