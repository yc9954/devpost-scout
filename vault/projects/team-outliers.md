---
slug: "team-outliers"
url: "https://devpost.com/software/team-outliers"
title: "Team Outliers"
hackathon: "USAII® Global AI Hackathon 2026"
organization: "USAII"
winner: true
words: 1027
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/geospatial"
---

# Team Outliers

> Defeating the 911 queue: An AI triage system that intercepts overflow, dynamically clusters duplicates, and instantly prioritizes life-threatening emergencies.

[Devpost](https://devpost.com/software/team-outliers) · hackathon [[USAII- Global AI Hackathon 2026]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[civic_government]] [[disaster_emergency]] [[education]] [[health_clinical]] [[supply_logistics]]
**user** [[educator_student]] [[frontline_worker]] [[general_public]]
**substrate** [[geospatial]]

**stack** ai, fastapi, json, postgresql, python

## How they structured the write-up

- inspiration
- what it does
- scope, stakeholders, & assumptions
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for team outliers

## Body

logo high level architecture Inspiration When a mass emergency strikes, traditional call centers collapse under the weight of chronological (First-In, First-Out) queues. As students at CMU Africa, we researched global emergency response data and found a terrifying reality. Between 2023–2024, South Africa’s 10111 emergency lines received 17.7 million calls, but 11.1 million (62%) went unanswered due to capacity limits. Globally, up to 75% of emergency line calls are non-critical "noise" or duplicate reports. (source: https://businesstech.co.za/news/government/771561/why-saps-10111-call-centres-leave-you-hanging ) If 500 people witness a warehouse fire and call 112, a chronological queue forces a person suffering a cardiac arrest across town to wait behind 500 duplicate reports. We realized that legacy tech fails in a crisis: IVR ("Press 1 for Police") creates too much friction for panicked callers, and rule-based keyword routing is fragile (e.g., "I drove past a fire engine" vs. "My house is on fire" both trigger the word "fire" but carry vastly different severities). We needed a system that could dynamically sort emergencies by semantic severity, not by timestamp, without ever dropping a caller in need. What it does CrisisCluster is a 3-tier AI triage agent that acts as an asynchronous data engineering layer for public safety answering points (PSAPs). It intercepts overflow calls, structures the chaotic data, and reorganizes the dispatcher's queue. Dynamic Priority Queue: Replaces chronological routing. High-severity calls (e.g., home invasions, cardiac arrest) are identified via NLP and instantly pushed to the top of the human dispatcher's queue. Asynchronous Deflection: Low-priority calls (e.g., noise complaints) are processed, logged into the system for future review, and safely disconnected to instantly free up telecom bandwidth. Smart Intercept (Semantic Deduplication): Uses AI clustering to identify duplicate reports of mass events, consolidating dozens of individual calls into a single, actionable "Master Incident" ticket. Scope, Stakeholders, & Assumptions To ensure responsible deployment, we clearly defined the boundaries of CrisisCluster: Users & Stakeholders: Our primary users are Human Dispatchers, who use the dashboard to manage crises. Downstream stakeholders include First Responders (who rely on the accurate location/severity data) and Civilian Callers (whose lives depend on queue efficiency). We also defined a Public Safety Policy Board as the governance stakeholder responsible for setting the AI's confidence thresholds. Real Decisions & Downstream Risks: The system directly connects to the high-stakes decision of physical resource allocation (e.g., which emergency gets the last available ambulance). The primary downstream risk is misprioritization, if the AI misinterprets a call's severity, an ambulance could be fatally delayed. We mitigate this by keeping the human dispatcher in absolute control of the final dispatch decision. Explicit Scope & Non-Goals: Our scope is strictly limited to asynchronous data structuring and queue sorting. Our explicit non-goals include autonomous AI dispatching and automated medical advice (e.g., AI giving CPR instructions), as these carry unacceptable life-safety liabilities. Clear Assumptions: We assume that callers are using standard audio phone lines (not relying on video/text formats yet), and that local PSAPs have an existing digital CAD (Computer-Aided Dispatch) infrastructure that our JSON payloads can integrate into. How we built it We designed CrisisCluster as a high-level, modular pipeline that processes, analyzes, and routes emergency data in real-time: Interactive Command Dashboard: We built a web-based interface for dispatchers to view the live priority queue. To make it a true command center, we integrated communication features so the dispatcher can instantly initiate outbound calls directly from the dashboard to reach victims without switching systems. Call Simulation: We paired the dashboard with a mock "Call Simulator" frontend to safely trigger and demonstrate various concurrent emergency scenarios. AI Processing Engine: We utilized speech-to-text models alongside Large Language Models (LLMs) to ingest unstructured incoming audio and extract critical context, such as location and severity level. Clustering & Deduplication: By converting the extracted data into vector embeddings, our backend continuously compares new incoming calls against active incidents to seamlessly group duplicate reports. Challenges we ran into Our biggest technical and ethical hurdle was the "False Positive Deduplication Trap." If our AI aggressively clusters duplicate calls to save bandwidth, what happens when a caller reports a known fire, but crucially adds: "I am trapped on the third floor"? If the AI blindly drops the call as a duplicate, it costs a life. To solve this, we engineered a strict Active Verification Guardrail. We programmed the AI to halt the deduplication process if it detects novel entities regarding human safety. Before dropping any suspected duplicate, the system explicitly verifies with the caller: "Units are en route. Are there new injuries or trapped individuals?" Any affirmative answer completely bypasses the cluster and elevates the caller to Maximum Priority for a live human dispatcher. Accomplishments that we're proud of Zero-Shot Novelty Detection: We successfully engineered the LLM to handle novel, untrained incident types. If a caller reports a bizarre, unprecedented event, the AI scores the severity based purely on described physical impact (structural damage, human injury) rather than failing because it lacks a historical keyword. The Master Incident UI: Transforming 50 chaotic, separate mock calls into one clean, color-coded "Master Incident" card on the frontend felt like a massive leap forward in UI/UX for public safety. Strict Human-in-the-Loop Integrity: CrisisCluster never autonomously dispatches police or ambulances. It only structures and routes data, ensuring human dispatchers retain absolute, unencumbered authority over physical resource allocation. What we learned The Limits of Legacy Systems: We learned exactly why rigid decision trees fail in crises, they lack the semantic context necessary to understand human panic. Model Lifecycle & Governance: We realized that defining who owns the AI is just as important as the code. We mapped out an AI Governance protocol where a Public Safety Policy Board owns the confidence thresholds, auditing and adjusting them after mass casualty events to perfectly balance false positives against false negatives. What's next for Team Outliers Our immediate next step is expanding our audio ingestion pipeline to fully support regional African languages natively, specifically Kinyarwanda, Swahili, and Hausa. In a crisis, citizens revert to their mother tongue. If our AI can seamlessly ingest mixed dialects, translate them to structured English/French data, and prioritize them for dispatchers, we can fundamentally scale the viability of emergency infrastructure in diverse, multilingual cities across the globe. <div