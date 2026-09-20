---
slug: "abc-xapnio"
url: "https://devpost.com/software/abc-xapnio"
title: "Alchemetrics"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 528
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Alchemetrics

> Alchemetrics is a real-time AI dashboard that tracks cauldrons, matches tickets, and forecasts overflows, bringing automation and clarity to Poyo’s Potion Factory’s magical chaos.

[Devpost](https://devpost.com/software/abc-xapnio) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[sensor_fusion]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** css, fastapi, nemotron, nextjs, numpy, pandas, python, sqlalchemy, sqlite, tailwind

## How they structured the write-up

- ⚗️ stack:
- ⚗️ agents:
- ⚗️ integration:

## Body

Alchemetrics 🔮 Inspiration We got inspired by the chaos of Poyo’s Potion Factory which are dozens of cauldrons bubbling away, witches flying all over to pick up potions, and logs that didn’t always match reality. We wanted a way to actually keep track of everything in real time, catch missing potion, and make sure nothing slipped through the cracks. Basically, we wanted to bring a little magic to monitoring magic. 🔮 What it does Our dashboard watches all the cauldrons, figures out when potion is collected, matches it to the Transport Tickets, and flags anything weird, like underreported, overreported, or missing potion. It also forecasts when cauldrons might overflow and plans the witches’ routes so the collection is efficient. Everything is visualized on a map and timeline so you can see exactly what’s happening, in real time. 🔮 How we built it We built a multi-agent system orchestrated by Nemotron (NVIDIA’s LLM planner). Nemotron decides which agent/tool to call next, logs all reasoning, and keeps potion discrepancies low. ⚗️ Stack: FastAPI for APIs, Postgres for state, NumPy/Pandas/OR-Tools for calculations, Next.js + Tailwind for the dashboard. ⚗️ Agents: Planner (Nemotron): Coordinates all agents, logs decisions, ensures low discrepancies. Event Detection: Finds drain windows using slope/hysteresis, computes true volumes. Ticket Matching: Matches tickets to drains, handles outliers. Discrepancy Auditor: Flags anomalies with tolerance rules. Forecasting: Projects fill levels & overflow ETAs. UI Agent: Aggregates map, timeline, and Planner reasoning for the dashboard. ⚗️ Integration: All logic functions are exposed as FastAPI endpoints. /state/overview aggregates data for the front-end, while consistent JSON contracts ensure smooth agent communication. Early mock responses let us test before full Nemotron integration. 🔮 Challenges we ran into Integrating multiple agents (Nemotron planner, detection, matching, forecasting) into a cohesive system. Connecting the backend logic to a live database and ensuring correct state updates. Exposing our Python functions as FastAPI endpoints with consistent JSON contracts. Getting the front end dashboard to display real time cauldron data and reasoning traces. Handling edge cases in drain detection, ticket matching, and forecasting with minimal mock data. Keeping the system modular so that agents could be swapped or upgraded without breaking the rest of the pipeline. 🔮 Accomplishments that we're proud of Built a full multi-agent system that actually talks to each other. Real-time detection and auditing that gives clear, explainable results. End-to-end system from sensor data to optimized witch routes. Dashboard that shows maps, tables, and reasoning traces in one place. Demo scripts that let us test everything without needing the full factory running. A very cute UI! 🔮 What we learned How to organize a multi-agent system in Python with FastAPI. How to make detection, matching, and forecasting logic modular but still connected. That slope detection actually works surprisingly well in practice. The trade offs between exact optimization and fast heuristics. Why keeping reasoning traces visible is critical when you automate decisions. 🔮 What's next for Alchemetrics Make the agents smarter with probabilistic reasoning or AI guidance. Add notifications via Slack/Discord for anomalies. Improve forecasting with advanced time series models. Add user roles and authentication for the dashboard. Handle more complex routing scenarios with multi day deliveries and priorities. <div