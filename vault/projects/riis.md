---
slug: "riis"
url: "https://devpost.com/software/riis"
title: "RIIS"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 789
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# RIIS

> Rapid Incident Intelligence System

[Devpost](https://devpost.com/software/riis) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[multi_agent]] [[on_device_local]] [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** fastapi, fetch, javascript, python, pytorch, raspberry-pi, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for riis

## Body

Gaussian Splatting VR Reconstruction of Scene Automated Human Detection RIIS the Robot Inspiration Structural collapses kill survivors not because rescue is impossible, but because care can't reach them in time. In the first hour after a building comes down, survival rates drop sharply with every passing minute, yet the patient is often alive, conscious, and reachable. The barrier isn't medical capability. It's access. We built RIIS to close that gap — to put a provider's eyes, voice, and intelligence inside a collapse zone before any human can safely enter, so the patient-provider relationship begins the moment the building falls, not hours later when the rubble clears. What it does RIIS sends a ground robot into collapsed structures ahead of human responders. The rover navigates the space and streams live video to the operator's command interface, where YOLOv8-pose inference runs in real time, drawing skeleton overlays on any survivors it detects and triggering a triage pipeline. Four AI agents built on Fetch.ai's uAgents framework coordinate the post-detection workflow: Scout detects the patient, Triage generates a structured SBAR assessment using ASI-1 Mini, Comms dispatches multilingual voice contact through ElevenLabs, and Mapping kicks off a 3D Gaussian Splat reconstruction of the scene. The finished reconstruction loads into a Meta Quest 2, allowing incident commanders to walk through the space virtually before sending anyone in. How we built it Layer Choice Rover hardware PiCar-X with Raspberry Pi 5, streaming JPEG frames over WebSocket Detection YOLOv8-pose running on-device, drawing skeleton overlays on detected survivors in real time Backend FastAPI + Python serving the annotated video stream, SSE events, and rover control endpoints Command UI Vanilla HTML/CSS/JS dark command interface embedded in the browser, no build step Multi-agent system Fetch.ai uAgents with four agents registered on Agentverse — Scout, Triage, Comms, Mapping Triage reasoning ASI-1 Mini via Fetch.ai's LLM endpoint, generating SBAR assessments on patient detection Voice contact ElevenLabs Multilingual v2 generating pre-rendered audio files played at the rover on detection 3D reconstruction MASt3R for camera pose estimation, InstantSplat for Gaussian Splat training VR visualization Unity loading the .splat file on Meta Quest 2 with a breadcrumb trail and survivor marker The system was designed so each layer produces an inspectable artifact — annotated video frames, SBAR reports, reconstructed scenes — rather than a black-box response. Every output can be verified independently before the next stage runs. Challenges we ran into Getting YOLOv8-pose responsive enough on a laptop CPU for real-time demo work required more tuning than expected, so we ended up lowering the confidence threshold and adding a detection latch to prevent single-frame dropouts from breaking the operator UI. Fetch.ai's agent mailbox system had its own quirks around startup ordering and bureau lifecycle that cost us a few hours. MASt3R is genuinely sensitive to scene texture, which made staging the rubble scene a problem in its own right. We needed enough visual variety for the pose estimator to anchor on, while still looking like a collapse zone on camera. Coordinating five subsystems among four people with hard-interface contracts was its own engineering challenge. Accomplishments that we're proud of The full pipeline runs end-to-end: rover detects a prone person, skeleton overlay renders in real time, the agent chain fires in sequence, ElevenLabs delivers the survivor contact in Spanish, and a 3D scene gets reconstructed that you can walk through in VR. Detection runs locally on the operator's laptop with no cloud round-trip; LLM triage, voice synthesis, and reconstruction are cloud-accelerated where it matters. Each subsystem is independently runnable — the rover code mocks its hardware off-Pi, the dashboard falls back to recorded playback when no rover is present, and the reconstruction pipeline operates on any folder of frames. That separability is what let us build the system in parallel and integrate it under deadline. What we learned Multi-agent systems sound clean on paper, but the coordination layer is where complexity accumulates. Getting the bureau startup, the WebSocket bridge, and the dashboard's first client handshake to all sequence correctly took as long as the agent logic itself. Gaussian Splatting is genuinely impressive for scene reconstruction, but it requires disciplined photographic coverage to produce clean output. Tight interface contracts between teammates were essential, so we mocked each subsystem against its contract before integration day, so all four components could develop in parallel without blocking on each other. What's next for RIIS Adding thermal imaging for low-visibility environments, integrating the triage agent's SBAR output directly into EMS dispatch systems, and bringing the Gaussian Splat reconstruction time under 60 seconds end-to-end. Longer term, we want to make the autonomy stack robust enough that the rover can explore unfamiliar collapse geometry without operator intervention, and ship RIIS as a first-response kit any fire department could deploy without specialized training. <div