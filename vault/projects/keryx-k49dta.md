---
slug: "keryx-k49dta"
url: "https://devpost.com/software/keryx-k49dta"
title: "Keryx"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 701
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/supply_logistics"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Keryx

> Drones map real buildings in minutes, creating AI-operable world models where assistive agents navigate and search for locations (ex. food, elevator). Provides on-demand street view.

[Devpost](https://devpost.com/software/keryx-k49dta) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[supply_logistics]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** apple-depth-pro, css, css-frontend-react-18, csv, debian, debian-data-csv, dict), drones, eslint, fastapi, git, google-fonts, google-fonts-(inter)-backend/api-fastapi, heif

## How they structured the write-up

- inspiration
- what it does
- methods
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for keryx

## Body

Keryx Inspiration Keryx is a system that can map any building in minutes and navigate it like a human, by taking drone footage and converting it to a versatile 3D representation. By allowing AI to navigate such a representation, we could help with accessibility, large events, and even emergency response. What it does Keryx turns a real building into an AI-operable world. A fast FPV drone flies through a building and records video. We convert the footage into a 3D scene representation. AI agents move through the 3D model to search and reason — they request camera views at ((x, y, z, \theta)) and get rendered images from our pipeline. Through Poke + MCP, you talk to the AI in plain language: “Where’s the nearest printer?” “Guide me to the check-in booth.” The system spawns several subagents to explore the building interior and returns a path for the human to reach their desired space or location. Methods Capture: Extracted keyframes from drone footage and assigned spatial coordinates (trajectory + pose). World graph: Built a navigable graph where nodes are images at 3D poses and edges represent valid moves. Novel views are synthesized using Apple Depth Pro for metric depth and reprojection (no full 3D mesh needed). Agents: Implemented agents that traverse the graph: a Qwen3-VL vision-language model (via vLLM on Modal) decides where to go next and when the goal is in view. Agents are bounded to the mapped volume and run for multiple steps. Backend: Deployed depth + view-rendering and agent inference on Modal (GPU endpoints, volumes for checkpoints and model cache). FastAPI serves the “get image at pose” API the frontend and agents call. Frontend: React + Vite app with three modes: Manual (drive the camera by pose), Agent (conversational search via MCP), and Replay (play back a trajectory from CSV + manifest). Integration: Wired the system to Poke + MCP so users can message the AI and get real navigation and answers grounded in the building map. Challenges we ran into Converting raw video into structured spatial data quickly — From noisy drone telemetry and keyframes to a clean trajectory and consistent coordinate frame. Designing lightweight but navigable world graphs — Balancing graph density (enough views to move smoothly) with storage and render cost. We avoided full 3D reconstruction by using depth + reprojection for novel views. Making the agent truly agentic — Keeping the VL model on-task (move vs. “found it”), constraining it to the mapped bounds, and handling variable-length exploration (up to (N) steps) without hallucinating positions. Integrating MCP cleanly with spatial reasoning — Exposing “ask the building agent” through MCP so Poke could drive our backend without leaking implementation details. Accomplishments that we're proud of Mapped a real building during TreeHacks — Real drone footage, real coordinates, real graph. Built agents that move through a real-world map — Not simulation: the agent requests poses and gets images from our pipeline. Integrated conversational AI with spatial reasoning — Natural-language queries that resolve to “go here, look there” in the same coordinate system. Shipped a full hardware + AI + agentic stack in one weekend — Drone → graph → agents → MCP → frontend. What we learned Depth-based novel view synthesis can replace full 3D reconstruction for many indoor navigation tasks: Depth Pro gives metric depth and we reproject to new views without building meshes. Modal made it feasible to run heavy GPU workloads (depth model, VL inference) and serve them as HTTP endpoints without managing clusters. MCP is a strong fit for “tool use” style agents: our backend exposes “get image at pose” and “run exploration agent”; Poke + MCP turn that into a conversational interface. Real-world data is messy — trajectory alignment, coordinate frames, and keyframe selection mattered as much as model choice. What's next for Keryx Full 3D SLAM or faster reconstruction — Denser maps, loop closure, or real-time capable pipelines. AR navigation overlays — “Turn left at the next door” over a phone camera view. Real world application: emergency response — first responders querying “where are the exits?” or “where are the rooms with injured people” from a freshly captured building. Our vision: Any building. Mapped in minutes. Navigable by AI. <div