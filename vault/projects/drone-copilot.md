---
slug: "drone-copilot"
url: "https://devpost.com/software/drone-copilot"
title: "drone-copilot"
hackathon: "Gemini Live Agent Challenge"
organization: "Google"
winner: true
words: 977
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# drone-copilot

> Voice-controlled drone copilot powered by Gemini Live API and Google Cloud Run

[Devpost](https://devpost.com/software/drone-copilot) · hackathon [[Gemini Live Agent Challenge]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** djitellopy, fastapi, gemini, html/css, javascript, opencv, pydantic, python, sounddevice, websockets

## How they structured the write-up

- inspiration
- what it does
- how i built it
- the moment it clicked
- challenges
- what i learned
- accomplishments that i'm proud of
- what's next for drone copilot

## Body

System architecture: voice input → Gemini Live API (Cloud Run) → tool calls → drone commands, with live video feed back to dashboard. Web dashboard showing live drone video feed, telemetry, AI perception overlay, and mission status in real time. Auto-generated inspection report with annotated frames and AI findings, produced from a single voice command. Auto-generated inspection report with annotated frames and AI findings, produced from a single voice command. Inspiration I've always been drawn to the idea of machines you can just talk to — not type at, not tap through menus, but actually speak to like you would a person. Science fiction made it look effortless. Reality, until recently, rarely matched that. When the Gemini Live Agent Challenge was announced, the Gemini Live API changed the equation for me. Native real-time audio meant building something that doesn't just execute instructions — it listens , sees , and talks back . That's a fundamentally different kind of interaction than anything I'd built before. I already had a DJI Tello drone from a previous experiment. I'd built autonomous inspection with it before, but it was always command-driven. This felt like the right moment to push further: what if you could just have a conversation with a drone? So I built drone-copilot. What It Does Drone-copilot lets you have a real conversation with a drone. You open the web dashboard, click Mic On , and start talking: "Take off" — it takes off "What do you see?" — it looks at the live video feed and describes the scene in natural language "Move forward 20 centimeters" — it moves, precisely "Rotate 45 degrees" — it rotates "Inspect the box on the table" — it launches a full autonomous inspection mission: scanning, approaching, capturing frames, and generating a detailed report The drone also talks back. When you ask it a question, it answers. When it completes a maneuver, it confirms. The dashboard shows the live video feed, telemetry, AI perception overlay, and mission status in real time. How I Built It The architecture has two main parts. Backend (Cloud Run) — A FastAPI service that maintains a persistent Gemini Live API session. It relays audio and video between the client and Gemini, handles session resumption with context compression, and manages the real-time bidirectional WebSocket connection. Client (local) — A Python process that captures microphone audio and drone video frames, then dispatches tool calls. When Gemini decides to act — move, rotate, inspect — it issues structured function calls that map directly to drone commands. Pydantic schemas keep the model's output deterministic even though the underlying reasoning isn't. # Gemini returns structured tool calls like this: { "name": "move_drone", "args": { "direction": "forward", "distance_cm": 20 } } The key design decision was keeping the Gemini Live session alive for the entire interaction rather than doing request-response per command. This is what makes the conversation feel fluid — Gemini has continuous context: it remembers what it just said, what the drone did, and what it currently sees. The Moment It Clicked I said "take off" — and it took off. That sounds simple. But I'd spent days debugging WebSocket relay, audio encoding formats, session management, and tool call parsing. So when I said the words and the drone lifted off the floor on its own, it genuinely surprised me. Then I asked "what do you see?" — and it described the room. Correctly. In full sentences. Talking back. That's when this stopped feeling like a demo and started feeling like something real. Challenges Getting the Live API and the Flash model to work together was the central technical challenge. The Live API runs in a streaming, stateful session — but mission-critical decisions like "is the target centered in frame?" need fast, reliable structured output. Threading the needle between conversational flow and deterministic tool execution took significant iteration. Wind. The DJI Tello has no GPS — it uses optical flow for position hold. Outdoors, even a light breeze is enough to push it off course mid-inspection. I lost count of how many test runs I had to redo waiting for the wind to calm down. Real-world constraints have no mercy. What I Learned Voice interaction with physical hardware is a completely different design space than chat. Latency, interruption handling, barge-in — these matter in ways they never do when you're typing. A 300ms delay in a chat interface is invisible. When you're talking to a drone mid-flight, it's jarring. I also learned that real-world testing surfaces things no simulator can. The wind problem wasn't in any spec. It just showed up, repeatedly, until I adapted. Accomplishments That I'm Proud Of The voice conversation loop works end-to-end. You speak, the drone acts, and it speaks back — all through a single persistent Gemini Live session. The inspection mission is fully autonomous: the drone scans the environment, locks onto a target, approaches it, captures detailed frames, and returns a structured visual report — all triggered by a single voice command. Building something that genuinely surprised me is rare. This did. What's Next for Drone Copilot New mission types. Inspection is the beginning. The same architecture — voice intent → AI reasoning → structured commands → physical action — can support perimeter patrol, inventory counting, or search and assist scenarios. Better hardware. The DJI Tello is great for prototyping, but its limitations are real: wind sensitivity, optical flow drift in low light, short battery life. Adapting the system for a GPS-equipped drone with longer range is the natural next step. A reusable platform. The core pattern — audio capture, multimodal reasoning, structured tool dispatch, safety checks — shouldn't need to be rebuilt for every project. The goal is to package this into a layer that lets developers build voice-driven physical agents without reinventing the control loop from scratch. Drones are just the first case. <div