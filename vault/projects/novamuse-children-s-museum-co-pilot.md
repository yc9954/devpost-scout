---
slug: "novamuse-children-s-museum-co-pilot"
url: "https://devpost.com/software/novamuse-children-s-museum-co-pilot"
title: "NovaMuse: Children's Museum Co-Pilot"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 947
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/transportation"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# NovaMuse: Children's Museum Co-Pilot

> Smart automation for children's museums, predicts crowding, guides families, alerts staff to safety issues, and turns exhibits into adaptive, story-based learning adventures.

[Devpost](https://devpost.com/software/novamuse-children-s-museum-co-pilot) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[transportation]]
**user** [[legal_professional]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-ecr, aws-app-runner, aws-cli, aws-iam, bedrock, css, docker, fastapi, html, javascript, jinja, nova, python, uvicorn

## How they structured the write-up

- about novamuse: children’s museum co-pilot

## Body

Staff portal to identify visitor flow problems, safety concerns, environmental resource use Visitor kiosk to generate quests and answer questions adding to the educational content of the exhibit Main dashboard Concept : visitor's kiosk About NovaMuse: Children’s Museum Co-Pilot Inspiration Children’s museums are designed for joyful exploration, but the behind-the-scenes work is constant. On a busy day, staff are simultaneously handling check‑in surges, managing crowding around popular exhibits, responding to small safety incidents, and completing repetitive administrative tasks that keep the museum running. When demand spikes, the museum can shift from “guided discovery” to “constant reaction.” NovaMuse started from a simple question: How can we make a children’s museum safer and easier to operate—without reducing the magic of hands‑on learning? Instead of building a generic chatbot, we focused on the kinds of moments that matter in museums: When a zone becomes overcrowded and staff need quick, consistent playbook actions When a minor incident (spill, lost item, conflict) needs to be logged and routed fast When a child asks a great question but staff are busy and can’t always stop to explain What the project does NovaMuse is a prototype “museum co-pilot layer” built around three outcomes: efficiency , safety , and learning . 1) Efficiency NovaMuse provides a staff dashboard that consolidates operational signals into one view: A live summary of zones, capacity status, and safety alerts One-click generation of a daily report (downloadable Markdown artifact) Downloadable JSON “automation run” artifacts that represent repeatable admin workflows (designed to be replaced by real UI automation) This is intentionally practical: museums already run on checklists and logs; NovaMuse helps teams produce them faster and more consistently. 2) Safety NovaMuse simulates occupancy per zone, escalates alerts, and recommends playbook actions (redirect traffic, open overflow routing, temporarily pause entry). We compute a simple crowd-pressure score: [ \text{CrowdPressure} = \frac{N}{C} ] where (N) is the number of visitors currently in a zone and (C) is the zone’s safe capacity. As (\text{CrowdPressure}) increases, NovaMuse escalates guidance from “monitor” → “redirect” → “pause entry.” Privacy-by-design: the demo uses counts only (no cameras, no identity tracking). It models the type of operational signal a museum can safely use without collecting personal data. 3) Learning experience NovaMuse includes a visitor kiosk experience designed for short, kid-friendly interactions: Exhibit Q&A grounded in curated exhibit facts (safe, age-appropriate) Mini “quests” (3 steps) that turn an exhibit into a structured challenge: observe → try → explain The kiosk is meant to complement staff, not replace them—especially during busy periods when educators are handling operations. How we built it We built an MVP that runs locally for development and can also be deployed publicly for judges. Architecture Backend: Python + FastAPI (API endpoints + page routes) UI: Server-rendered HTML templates plus lightweight JavaScript for actions and refresh Artifacts: downloadable Markdown daily reports and JSON workflow run logs Containerization: Docker Deployment: Amazon ECR + AWS App Runner (public URL) AI integration approach NovaMuse supports two execution modes: Mock mode (default): deterministic, curated responses so the demo works without AWS credentials and stays grounded for a children’s environment. Bedrock mode (optional): the kiosk Q&A can call Amazon Bedrock with Amazon Nova when environment variables and IAM permissions are configured. Nova-specific integration detail To run Nova 2 Lite reliably, we invoke Bedrock using the inference profile ID (for example: us.amazon.nova-2-lite-v1:0 ) rather than the base model ID, because on-demand throughput may not be enabled for the base ID in all accounts/regions. This ensures the deployment is aligned with Bedrock’s supported invocation path. UI workflow automation For museum operations automation, we implemented “Nova Act style” workflow runs as a structured placeholder: the app generates step-by-step run artifacts that mirror how a real automated workflow would execute (navigate UI, export attendance, close-out routine). The intended next step is to replace the simulated runner with actual Amazon Nova Act workflows to automate real museum admin portals with higher reliability. Challenges we faced Deployment reliability: Even a small web app can fail in production if ports and health checks don’t match platform expectations. We had to align container listening ports with App Runner configuration and health checks. Public demo state management: A judging demo must be replayable. We implemented a full “clean slate” reset so the simulation can be restored to a known starting point. Hosted UI responsiveness: Real-time dashboards can drift if state updates aren’t explicit. We implemented predictable refresh patterns after actions so staff always see the correct occupancy and alert state. Model invocation troubleshooting: The project includes both mock mode and Bedrock mode. We added logging and stepwise tests (local CLI tests, then deployed tests) to isolate whether failures came from code, permissions, model IDs, or account configuration. Kid-safe behavior from day one: The kiosk experience must stay short, appropriate, and grounded. We constrained responses, structured prompts, and included safe fallback behavior so the system remains usable in a children’s setting. What we learned An operations copilot is mostly decision support: clear alerts, consistent playbooks, and fewer repetitive tasks—not replacing staff judgment. “Small” infrastructure details (ports, health checks, environment variables, IAM roles) often determine whether a demo is usable. Building for children changes the bar: privacy, guardrails, and deterministic fallbacks are not optional—especially in public kiosk experiences. What’s next Replace the simulated workflow runner with real Amazon Nova Act automation for museum admin portals (incident routing, exports, end-of-day close). Add Nova 2 Sonic for a voice-first kiosk experience that supports pre-readers and accessibility. Add Nova multimodal embeddings to expand retrieval beyond text (signage, exhibit guides, images) for stronger museum-specific RAG. Connect to real operational signals (ticket scans, counters, IoT devices) and persist state in a database so the system scales across multiple instances. <div