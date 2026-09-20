---
slug: "trustos"
url: "https://devpost.com/software/trustos"
title: "KickOff"
hackathon: "Google Cloud Rapid Agent Hackathon"
organization: "Google"
winner: true
words: 1069
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# KickOff

> Seven Gemini 3 agents move 82,500 World Cup fans to MetLife Stadium — reasoning over live MongoDB Atlas via MCP, every decision a database write streamed onto a photorealistic 3D map.

[Devpost](https://devpost.com/software/trustos) · hackathon [[Google Cloud Rapid Agent Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** a2a, agent-starter-pack, cloud-build, cloud-run, docker, fastapi, gemini-3, google-agent-development-kit-(adk), google-cloud-agent-builder, google-maps-photorealistic-3d-tiles, model-context-protocol-(mcp), mongodb-atlas, mongodb-change-streams, mongodb-mcp-server

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kickoff

## Body

Inspiration The FIFA World Cup kicks off today , and on July 19, 2026 the final lands at MetLife Stadium: 82,500 fans converging on a venue with no parking to speak of, served by one rail line, two bus corridors and a park & ride. Transit on big match days fails the same way every time — not for lack of capacity, but for lack of coordination : each corridor operator reacts locally and late. That's a textbook multi-agent problem. We wanted to show that a team of LLM agents, sharing one operational database, can run matchday logistics the way a human control room wishes it could — sensing surges early, rebalancing the network, and explaining every intervention in plain language. What it does KickOff Agent is a live control room for matchday transit. One click launches a full matchday at MetLife Stadium: A planner agent designs the transport plan — fan allocations across four real corridors (NJ Transit rail from Secaucus, shuttle buses from Port Authority and Grand Central, park & ride from Hackensack) — and commits it to MongoDB Atlas. A simulator advances the matchday tick by tick: arrival waves, queue buildups, and random incidents (a stalled train, a tunnel slowdown). Four corridor concierge agents , each owning one corridor, watch their queues and decide — boost capacity, divert fans to a healthier corridor, or hold — writing each decision with its reasoning into Atlas through the MongoDB MCP server. When a corridor goes critical, a coordinator agent is escalated and rebalances the whole network, creating a brand-new surge_history collection live mid-run — schema evolution as a feature, not a migration. The trick that makes the demo honest: the UI never talks to the agents. Every visual — the photorealistic 3D map of the real Meadowlands with glowing corridor routes and growing queue towers, the corridor cards, the agent decision feed, the surge alerts — is a projection of MongoDB Atlas change streams . If a panel updates, it's because an agent wrote a document. The database is the single source of truth and the event bus. How we built it Agents: Seven LlmAgent s built with the Google Agent Development Kit (ADK) on Gemini 3 ( gemini-3-flash-preview ), each with a focused system prompt and MongoDB MCP tools. Deployed to Vertex AI Agent Engine (one reasoning engine per agent), with an in-process mode for friction-free local runs — identical agent code in both. MongoDB via MCP: Agents read corridor state and write decisions through the official MongoDB MCP server ( mongodb-mcp-server ) — find , insert-many , collection creation — so the agents' hands on the database are real tool calls, not hardcoded driver glue. Event flow: Atlas change streams → FastAPI gateway → Server-Sent Events → browser. One stream powers everything; refresh mid-run and the UI rebuilds itself from the database. Frontend: TypeScript + Vite, Google Maps photorealistic 3D tiles rendering the actual Meadowlands — corridor polylines that shift color on surge, flow pulses whose speed tracks throughput, extruded queue towers at each origin, and a cinematic camera that flies to a corridor going critical (with a Three.js stylized fallback if no Maps key is configured). Infra: Gateway containerized (multi-stage Node + Python build) on Cloud Run via Cloud Build; agents on Agent Engine; scaffolding aligned with the agent-starter-pack ; dependency versions locked with uv so the deployed container exactly matches the tested environment. Challenges we ran into Gemini 3 preview quotas. The shared per-minute rate limit punished seven chatty agents. We added a dispatch layer with quota-aware exponential backoff and a concurrency semaphore so escalations survive a crowded minute. A silent reasoning blackout. A datetime field deep in the corridor snapshot made json.dumps throw inside the dispatcher — agents looked idle while the simulation hummed along. One default=str restored the entire decision feed. Lesson: instrument the dispatch path, not just the agents. Living on alpha APIs. The Maps 3D alpha channel started rejecting empty polyline coordinates mid-hackathon and took our launch button down with it. We hardened boot so the control panel can never be killed by the scene, with a graceful 3D fallback. Dependency drift in production. A fresh pip resolve in the container pulled a newer google-adk whose MCP schema validation rejected the MongoDB MCP server's tool schemas — works on my machine, fails on Cloud Run. Exporting the uv lockfile into the image fixed it for good. M0 Atlas budget engineering. Free-tier connection limits meant treating connections like a scarce resource: one client, bounded concurrency, and change streams doing the fan-out. Accomplishments that we're proud of A true multi-agent system — seven agents with distinct roles, escalation paths, and agent-to-agent dispatch — not one prompt wearing seven hats. Database-as-event-bus done for real: every pixel of the UI is driven by Atlas change streams; the demo is auditable by reading the collections. A coordinator that performs live schema evolution , creating and populating surge_history mid-incident — showing why a document database fits agent workloads. A photorealistic digital twin of the Meadowlands that makes agent decisions legible to a non-technical viewer in seconds. End-to-end runs delivering ~90% of 82,500 fans by kickoff, with every diversion and capacity boost explained in the feed. What we learned Agents are most trustworthy when their only output is a database write — reasoning becomes data you can query, replay, and audit. MCP is the right boundary between LLMs and state: swapping driver glue for MCP tools made agent behavior inspectable and the demo honest. Production agent systems fail in the plumbing, not the prompts — serialization, quotas, version drift. Lock everything, back off everywhere, and make failure loud. Change streams turn MongoDB into a real-time pub/sub layer with zero extra infrastructure — a perfect match for agent swarms. What's next for KickOff Real data feeds: NJ Transit GTFS-RT, traffic and weather APIs, and ticket-scan telemetry replacing the simulator for live matchdays. Fan-facing concierge: the same corridor agents answering individual "when should I leave?" queries, personalized from live corridor state. All 104 matches, 16 stadiums: the corridor model generalizes to every World Cup venue — and to concerts, marathons, and evacuations. Atlas Vector Search over the decision history so agents learn from past surges ("last time rail hit 3× at tick 40, the diversion that worked was…"). Coordinator-graded postmortems: automatic after-action reports comparing plan vs. outcome, written back to Atlas as the institutional memory of the system. <div