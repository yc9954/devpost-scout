---
slug: "containos"
url: "https://devpost.com/software/containos"
title: "ContainOS"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 869
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ContainOS

> Physics-Grounded Multi-Agent Copilot for Rapid Wildfire Containment.

[Devpost](https://devpost.com/software/containos) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[disaster_emergency]] [[health_clinical]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** claude, codex, css, fastapi, google-gemini, gpt-4o, html, indexeddb, javascript, json, json-react-19, leaflet.js, node.js, openai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges
- accomplishments
- what we learned
- what's next for containos

## Body

Dashboard Inspiration The first three hours of a wildfire, the initial attack, are the most critical in determining whether the wildfire can be rapidly contained with minimal damage or whether a massive, multi-day operation is needed. Incident commanders on the ground must rapidly assess a fire, decide where to deploy crews and aircraft, and issue evacuation warnings as conditions evolve. Despite unprecedented access to satellite imagery, low earth orbit data, drone feeds, and AI-enabled cameras, responders still lack a unified system that synthesizes this information into actionable, real-time guidance. We built ContainOS to provide real-time, physics-grounded decision support for firefighters en route, reducing cognitive friction during high-pressure moments. What it does ContainOS transforms fragmented wildfire data into a unified decision-support platform for containment operations. It ingests wind, terrain, infrastructure, topography, and population data to generate structured insights and prioritized alerts about present and impending risks, enabling rapid triage decisions by incident commanders. Historical fire data is incorporated to surface relevant precedents and escalation patterns from past incidents. Beyond presenting base data through a streamlined, low-friction interface optimized for tablet use in the field, ContainOS generates prioritized alerts tied directly to the fire’s interaction with its surroundings. The system supports both online and offline operation and integrates proactive text-based alerting for first responders in low-connectivity environments, flagging immediate hazards such as downed powerlines or significant wind shifts. How we built it ContainOS combines deterministic wildfire physics with a feedback-aware multi-agent AI system. The system uses four coordinated GPT-4o reasoning agents that operate as a structured agent graph for fire behavior, risk assessment, notifications, and recommendations, alongside a Gemini-powered historical context component. All outputs pass through a deterministic validation layer. Before agent reasoning, the backend computes a deterministic physics state, conceptually forming a physics graph over the fire perimeter and nearby communities, from time-indexed environmental snapshots (wind, terrain, vegetation, infrastructure, fire perimeter, and population data). This includes: Baseline spread velocity Slope and fuel multipliers A deterministic threat level Community exposure using distance thresholds The frontend visualizes these dynamics per segment, rendering fast, moderate, and slow spread zones. On top of this physics baseline, the GPT-4o agents generate: Fire behavior analysis Infrastructure risk assessment A small, prioritized set of tactical alerts (1–5) A top containment recommendation with a 0–100 confidence score All outputs are validated against deterministic constraints. If an agent contradicts the physics baseline, the system injects structured feedback and re-runs the affected agents. The system allows up to three total attempts (initial generation plus two retries). If consistency cannot be achieved, it safely falls back with a confidence score of 0. Together, the physics state and agent reasoning form a constrained two-layer architecture, where probabilistic inference is bounded deterministically. This architecture prevents generative reasoning from overriding physical reality, converting AI into a bounded, constraint-validated system for high-stakes decision support. Challenges A core challenge was architecting a system where a deterministic physics pipeline and a multi-agent reasoning graph operate in lockstep. The physics layer establishes a non-negotiable baseline, while probabilistic agents generate structured assessments on top of it. Ensuring these layers remained aligned required explicit validation, constraint enforcement, and bounded retries. Rather than functioning as a linear AI pipeline, the system continuously reconciles agent outputs with computed physical state to preserve reliability under rapidly changing conditions. Another challenge was deploying AI into real operational workflows without introducing misplaced trust. In wildfire containment, recommendations affect evacuation timing, crew deployment, and infrastructure protection. We had to design the system so that AI assistance augments situational awareness without projecting unwarranted certainty, remaining transparent, bounded, and clearly subordinate to human judgment. Accomplishments We iterated directly with former CalFire leadership to refine alert prioritization, evacuation logic, and interface clarity based on real operational workflows. We built a feedback-aware, physics-constrained multi-agent system that enforces physically consistent, self-correcting reasoning in a high-stakes environment. By validating probabilistic agent outputs against a deterministic physics baseline and enforcing bounded retries with safe fallback behavior, the system prevents generative outputs from contradicting physical reality. This ensures recommendations remain consistent, explainable, and grounded in computed state. Most importantly, we demonstrated a practical framework for responsible AI in life-critical domains: generative reasoning explicitly constrained by deterministic physical models, structured validation loops, visible uncertainty through confidence scoring, and clear preservation of human authority in decision-making. This approach shows how AI systems can augment rather than replace expert judgment in safety-critical contexts. What we learned We learned that high-stakes AI systems must be explicitly bounded by deterministic constraints; generative outputs cannot be trusted without formal validation against physical reality. This is especially true in wildfire containment, where lives are at stake and operational decisions must remain grounded in computed state. We also learned the importance of iteratively reviewing our product with real users, for not only initial insights on user pain points but continuous alignment and redirection as needed. This project reinforced how modern AI systems can responsibly support public sector decision-making when deliberately constrained and purpose-built. What's next for ContainOS Ensuring ContainOS is useful in the field will require direct feedback from incident commanders. We hope to work with CalFIRE to extensively test and update this tool for eventual rollout across California and beyond, for real application in containing wildfires right when they start. <div