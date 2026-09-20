---
slug: "crisisavert"
url: "https://devpost.com/software/crisisavert"
title: "CrisisAvert"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 443
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "substrate/geospatial"
---

# CrisisAvert

> CrisisAvert is a sophisticated emergency management platform that leverages agentic AI to simulate and coordinate responses to natural disasters like floods and earthquakes

[Devpost](https://devpost.com/software/crisisavert) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
  <sub>weak: on_device_local, sensor_fusion</sub>
**domain** [[civic_government]] [[developer_tools]] [[disaster_emergency]]
  <sub>weak: climate_energy</sub>
  <sub>weak: frontline_worker</sub>
**substrate** [[geospatial]]

**stack** context, express.js, frontend-(/client):-react, google-gemini-sdk-(ai-reasoning), google-maps, mcp, model, socket.io, socket.io-client, tailwindcss, vite, web-speech-api.-backend-(/server):-node.js

## Body

CRISISAVERT — AI-POWERED EMERGENCY COMMAND CENTER AI that thinks as fast as disasters unfold. ================================================================================ INSPIRATION Flood evacuations delayed by hours. Rescue resources sent to wrong areas. First responders stopping life-saving work to fight clunky systems. Every disaster second is a decision buried under data overload. With climate change intensifying disasters globally, manual coordination isn't enough. CrisisAvert builds the AI emergency responders need. ================================================================================ WHAT IT DOES An agentic AI command center turning reactive data visualization into proactive coordination: • Voice-Activated Commands — "Activate Flood Protocol" hands-free. No keyboards in the field. • AI Threat Assessment — Google Gemini performs chain-of-thought reasoning on disaster data, analyzing seismic patterns, infrastructure impact, delivering severity scores with full reasoning transparency. No black box. • Geospatial Intelligence — Real-time satellite mapping with impact zone overlays. • Autonomous Response — Deploys simulated Supply, Medical, Aerial units with centralized command dashboard. • Privacy-First — Ephemeral sessionStorage auto-wipes sensitive data. Built for government deployment. ================================================================================ HOW I BUILT IT Dual-core architecture: THE ORACLE (Node.js + Gemini SDK) — Analyzes threats, generates assessments with confidence scores via chain-of-thought reasoning. THE HAND (React + Vite + Socket.IO) — Real-time WebSocket communication renders geospatial overlays and deployment logs. WORKFLOW: Threat detected → AI analyzes → Coordinated deployment RESPONSE TIME: Under 60 seconds vs. 15-30 minutes traditional STACK: Google Gemini, React, Node.js, Socket.IO, Google Maps API, Web Speech API ================================================================================ CHALLENGES • AI Transparency — Life-or-death decisions need visible reasoning, not black boxes. Chain-of-thought solved this. • Voice Recognition — Emergency terms like "Uttarakhand" or "magnitude 7.2" fail in Web Speech API. Built custom fuzzy matching layer. • Real-Time Sync — Socket.IO architecture with heartbeat monitoring for disaster-critical reliability. • Solo Development — Limited budget meant ruthless prioritization and modular architecture. ================================================================================ ACCOMPLISHMENTS Built complete agentic AI system solo: frontend, backend, AI engine, voice interface, mapping, real-time comms. An emergency professional said: "This addresses a real problem we have." • Sub-60-second response time • Auditable AI reasoning • Hands-free operation • Privacy-first for government use ================================================================================ WHAT I LEARNED • Agentic AI needs context management and human oversight at decision points • Chain-of-thought reasoning is non-negotiable for high-stakes applications • Voice interfaces need visual fallbacks for noisy environments • WebSocket fault tolerance isn't optional • Privacy must be architectural, not added later ================================================================================ WHAT'S NEXT SHORT-TERM: USGS earthquake feeds, NOAA weather, NASA wildfire data, mobile interface MEDIUM-TERM: Offline-first for degraded connectivity, multi-agency access, NIMS/FEMA compliance LONG-TERM: VR training, sensor marketplace, production pilots with emergency agencies, international deployment VISION: Global emergency coordination platform with unified AI-powered response. ================================================================================ BUILT WITH google-gemini-ai, nodejs, react, socket-io, voice-recognition, geospatial-mapping, emergency-response, disaster-management, agentic-ai, chain-of-thought, real-time-systems, google-maps-api, vite, express <div