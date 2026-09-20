---
slug: "detour-64kpds"
url: "https://devpost.com/software/detour-64kpds"
title: "Detour"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 825
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "substrate/geospatial"
---

# Detour

> On-board AI agents autonomously saving satellites from orbital debris.

[Devpost](https://devpost.com/software/detour-64kpds) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[multi_agent]] [[provenance_signing]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[health_clinical]] [[labor_employment]]
**substrate** [[geospatial]]

**stack** agents, cdm, cloudflare, dgx-spark, llm, nextjs, nvidia, shadcn, typescript, vercel

## How they structured the write-up

- tl;dr 🛰️
- the problem with today's debris avoidance
- how we built it
- challenges we ran into
- what we learned
- what's next for detour ⏭️

## Body

The Detour Dashboard Simulation Mode Agentic Terminal Conjunction Feed and Debris Tracking Try it here -> https://detour-azure.vercel.app/ TL;DR 🛰️ Detour is an edge-first, autonomous decision-support system for satellite debris avoidance. Built for the ASUS Ascent GX10 / NVIDIA DGX Spark, Detour transforms raw orbital data into direct physical action, enabling agents to independently determine when a satellite requires a maneuver and generating the precise path-adjustment commands to execute it. It ingests live Two-Line Element (TLE) sets, propagates orbits in real-time, and generates a prioritized feed of Conjunction Data Message (CDM)-style events. The core of Detour is a multi-agent workflow powered by a local NVIDIA open model via vLLM. The system evaluates risks against real-world satellite constraints, such as fuel budgets, burn limits, and mission horizons, to ensure any proposed maneuver is both physically possible and operationally safe. Our agentic approach provides a transparent audit log, showing the system's reasoning as it screens, ranks, and triages the most dangerous objects in the debris field. Ultimately, Detour automates a high-stakes workflow that satellite operators have managed manually for decades, redefining the future of orbital infrastructure! The problem with today's debris avoidance Low Earth Orbit is getting overwhelmed with operational satellites and debris. Even a small debris fragment can cause catastrophic damage at orbital speeds. Satellite operators therefore run continuous conjunction assessments to predict close approaches and decide whether an avoidance maneuver is worth the operational cost (fuel/Δv, mission disruption, and the risk of creating new conjunctions). Conjunction warnings are typically delivered to operators as Conjunction Data Messages (CDMs), which are standardized notifications generated from tracking and screening systems that summarize an upcoming close approach. Operators are often overwhelmed by a constant stream of these messages. Because the data is so technically dense, it’s difficult to quickly filter out the noise and identify which threats actually require a maneuver. We built Detour! How we built it The Agentic Engine Detour is designed to run entirely at the edge, simulating the air-gapped environment of a real satellite or ground station. We utilized the ASUS Ascent GX10 (NVIDIA DGX Spark) to host our agentic workforce, deploying the NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 model via vLLM for low-latency reasoning. We split the workload into specialized roles: The Ingest & Screening Agents: These manage the live TLE data stream and run the heavy SGP4 physics to predict where every object in the catalog will be over the next 24 hours. The Navigator Agent: This agent acts as the primary "operator." It evaluates threats against the user-defined constraints and decides if a maneuver is necessary. -The Logic Loop: To ensure accuracy, we kept the math and logic separate. The agents call Python-based physics libraries for orbital propagation and only use the LLM layer for high-level decision logic and maneuver triage. The dashboard We built a Next.js + React + TypeScript dashboard styled with shadcn/ui for a clean, high-contrast mission-control layout. The visualization uses a Three.js 3D globe to render the target orbit and surrounding debris environment in real-time. Left Panel: Handles NORAD lookup and the live conjunction feed. Right Panel: Exposes constraint inputs that define the rules for the agents. Terminal: Provides a readable system trace, showing exactly how the agents are fetching data, screening threats, and calculating maneuvers. Challenges we ran into We quickly found that LLMs are excellent at reasoning but terrible at orbital mechanics. Early versions of the agent tried to "guess" the result of a burn. We solved this by implementing a strict Tool Use architecture, forcing the model to offload all math to the SGP4 propagator and only interpret the results. We also found that our agents could not calculate all the orbital paths of the thousands of debris with a latency sufficient for inference; to fix this, we ended up using a Gaussian stochastic sampling distribution. to model each asteroid path. Lastly, running a local LLM alongside a heavy 3D visualization and real-time physics engine on a single edge device was a huge challenge. We had to aggressively optimize our vLLM configuration and context window to ensure the agents could act without choking the GPU. What we learned We discovered that for time-sensitive orbital operations, latency is a safety risk. We learned how to optimize model throughput using vLLM to ensure that our Planning Agent could evaluate multiple maneuver candidates in seconds, which would be impossible with the round-trip latency of a cloud API. We learned that in the NVIDIA ecosystem, balancing between model size and hardware limits is really important. We spent a significant amount of time testing different quantizations and parameters to ensure our agents could run in parallel on the ASUS GX10 without hitting VRAM bottlenecks. What's next for Detour ⏭️ Onboard to operator-grade data sources: Integrate services that provide richer conjunction products (e.g., true CDMs, higher-fidelity screening outputs, and more frequent updates) so Detour’s agents can rank threats more accurately, reduce false alarms, and recommend safer maneuvers with clearer tradeoffs. Deploying to a real satellite :) <div