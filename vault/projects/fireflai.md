---
slug: "fireflai"
url: "https://devpost.com/software/fireflai"
title: "Fireflai"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 841
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Fireflai

> A multi agent AI tool for fire fighters

[Devpost](https://devpost.com/software/fireflai) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[sensor_fusion]]
  <sub>weak: cross_origin_web, voice_speech</sub>
  <sub>weak: accessibility, developer_tools, disaster_emergency, labor_employment, transportation</sub>
**user** [[legal_professional]]
  <sub>weak: frontline_worker</sub>
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]
  <sub>weak: sensor_telemetry</sub>

**stack** arize, aura, browserbase, deepgram, fetchai

## Body

FireflAI See through smoke. Reach the victim faster. Inspiration Firefighters enter burning buildings blind — no floor plan, no idea where the fire started or which room someone is trapped in. They find out by feeling through black smoke, one second at a time. Yet two things that could change that already exist: the 911 call, full of detail stuck on the phone line, and a near-complete visual record of most homes sitting in public real-estate listings. FireflAI stitches them together and hands the crew a hazard-annotated 3D model of the house before they go through the door. Every second of orientation we save is a second closer to the person inside. What it does An operator drops a property link and the 911 call text into the dispatch console. FireflAI does the rest, live: Pulls the home's listing photos and curates the ones worth reconstructing Reconstructs an explorable 3D model + 360° panorama of the interior from a single photo Maps the house into a room-by-room graph (doors, windows, entry points) Reads the 911 call and pins hazards — fire, smoke, gas, electrical, collapse, trapped occupants, exits — onto the panorama at real angles Plans the safest route to the victim, steering around fire and blocked paths Runs four specialist agents (fire, structural, evacuation, personnel) that argue to a go / no-go consensus and a tight commander briefing The crew sees a live dashboard: incident map, streaming agent feed, the walkable 3D world with a toggleable hazard overlay, the recommended path, and the briefing. How we built it A FastAPI backend and a React 19 + TypeScript + Tailwind frontend, streaming stage-by-stage over WebSockets. Pipeline: acquire → curate → map → reconstruct → hazard → plan → tactical → briefing Browserbase — a stealth cloud browser gets past Zillow's PerimeterX; we regex photo URLs out of the page payload (not the brittle gallery DOM), with a canned fallback so a blocked scrape never kills a demo Groq (Llama 4 Scout) — every vision stage (curate / map / hazard / tactical), fast enough to feel live, with rate-limit backoff and a JSON-mode fallback World Labs (Marble) — turns the hero photo into a 3D world + equirectangular panorama + Gaussian splats, rendered in-browser with three.js / react-three-fiber Hazard overlay — fuses the 911 text + room graph + panorama into markers as yaw/pitch coordinates, so nothing repaints the image NetworkX — rooms weighted by fire/smoke/hazards, Dijkstra from "outside" to the trapped occupant Fetch.ai (uAgents + Agentverse + ASI:One) — six stage agents + a coordinator that's @-mentionable from ASI:One; ASI:One parses the free-text call and writes the briefing Arize AX — the whole run is one OpenInference trace, plus an LLM-as-judge that scores every briefing on grounding, actionability, safety-completeness, and clarity, logged right next to the trace it grades Mapbox for the dispatch map Challenges we ran into Zillow fights scrapers. Browserbase stealth + proxy beat PerimeterX, and regexing photo hashes out of the payload made extraction layout-proof. Hallucination is lethal here. An invented exit could get someone killed, so we engineered grounding: geometry only from photos, fire/smoke only from the call, and a briefing that's forbidden from asserting a go/no-go the analysis doesn't support — it defaults to "UNDETERMINED, commander to assess." Hazards in 3D from plain text. Solved by treating the panorama as a 360° equirectangular canvas and having the model emit yaw/pitch so markers land on the right wall. Free-tier limits. Batched curation, ran the map on the best five images, downscaled thumbnails, added backoff. Accomplishments that we're proud of A true end-to-end pipeline: paste a link and a call, get back a walkable, hazard-annotated 3D model and a go/no-go briefing — from public data, before anyone's on scene Consensus that surfaces dissent and weights by confidence, not a black-box answer We built the eval too — an LLM judge that takes the minimum of its scores, because a briefing is only as safe as its weakest part It streams live over WebSockets and fails gracefully — every fragile dependency has a fallback What we learned For life-safety AI, "don't hallucinate" has to be engineered, not hoped for — grounded prompts, safe defaults, and an automated judge that catches an invented exit before a human would Single-image 3D reconstruction is shockingly good now, and a 360° panorama beats trying to repaint pixels for spatial annotation The right division of labor: pixels → Groq, text/orchestration → ASI:One, agent choreography → uAgents/Agentverse, observability/eval → Arize Real-world data is hostile — bot detection, lazy galleries, and rate limits made robustness work as important as the AI What's next for FireflAI Live audio — transcribe the 911 call in real time so the hazard map updates as the caller talks Better geometry — fuse multiple photos and floor plans into one consistent multi-room model Mid-incident sensor fusion — pull in dispatch CAD data and smoke/heat and SCBA telemetry after the crew is inside Offline + on-truck — package it for a vehicle's data terminal with cached reconstructions for known addresses <div