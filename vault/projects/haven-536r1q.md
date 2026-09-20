---
slug: "haven-536r1q"
url: "https://devpost.com/software/haven-536r1q"
title: "Haven"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 722
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/transcript_audio"
---

# Haven

> Hospital command center powered by context-aware agentic AI that alerts nurses, unifies EHR data, and answers patient questions, improving understanding and reducing response delays and clinical error

[Devpost](https://devpost.com/software/haven-536r1q) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[privacy_tech]] [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]] [[medical_record]] [[transcript_audio]]

**stack** claude, fetch.ai, grok, livekit, openai, opencv, photoplethsymography, websocket, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments
- what we learned
- next steps

## Body

GIF Emergency Detection Dashboard GIF Live 3D Hospital Map Tech Stack Inspiration David's great-uncle was in the hospital this year. He noticed that his great uncle often waited over an hour to find a nurse to answer his questions due to understaffing. When someone finally arrived, they had to bounce across multiple systems to refamiliarize themselves. It felt like the information was there, just not there when we needed. Hospitals have more data than ever, yet nurses spend up to 50% of their shift on documentation instead of patient care. What if the moment a patient calls, an intelligent system helps manage nurse distribution throughout the hospital and flags concerning patterns and prepares exactly what the nurse needs to attend to their patient right away? That's why we built Haven. What it does Haven is a multi-agent hospital command center that transforms how nurses access critical patient information. Instead of hunting through fragmented systems, Haven provides three integrated intelligence layers: 1. HavenAI Voice Assistant via LiveKit Patients and families speak naturally to Haven using LiveKit and OpenAI's realtime voice API. Haven asks clarifying follow-up questions, pulls validated EHR data, and delivers nurse-ready summaries and action items—turning a 20-minute wait into an instant, documented interaction. 2. Autonomous Monitoring Dashboard via fetch.ai agents Fetch.ai agents continuously monitor patient vitals, detect concerning patterns, and coordinate with alert-response agents to flag issues before they escalate. Our computer vision pipeline uses facial photoplethysmography (FPPG) to non-invasively track heart rate and stress indicators, feeding real-time data to the monitoring network. 3. Live 3D Hospital Map via Claude agents Powered by an Anthropic Claude chain-tool-calling agent, nurses see a spatial view of the entire floor with real-time alert-based room coloring. They can ask natural language questions like "Tell me about Dheeraj's alerts and questions from the last 6 hours" and instantly understand which patients need attention and why—no system-hopping required. In addition, nurses can generate summary reports from their patients' discussions with Haven AI, so they do not need to turn to fragmented sources to familiarize themselves with the patients' current situation. Together, these agents create a cohesive intelligence network where information flows to the right person at the right time, automatically. How we built it Haven is a multi-agent hospital intelligence platform built on three core systems using LiveKit, Fetch.ai, and Claude agents : Voice Interface: HavenAI uses LiveKit for WebRTC streaming, OpenAI Whisper for speech-to-text, and OpenAI Realtime API for fully duplex conversation. The agent streams transcriptions and responses simultaneously, automatically triggering structured prompts to fill missing clinical details and pushing validated data to our backend. Monitoring & Alerts: Fetch.ai agents handle autonomous patient monitoring—a vitals-tracking agent communicates with an alert-response agent to raise or dismiss issues based on real-time thresholds and historical patterns. We also built a computer vision pipeline using OpenCV and facial photoplethysmography (FPPG) to extract heart rate and stress indicators from live video, feeding results directly into the Fetch agent network. Spatial Intelligence: Our live 3D hospital map is powered by an Anthropic Claude chain-tool-calling agent. It interprets natural language commands ("Show me which rooms have active alerts"), autonomously executes multiple tools to query patient data, and dynamically updates room colors and overlays in real-time based on the agent network's events. Challenges we ran into Natural voice interaction: Fine-tuning turn-taking, silence detection, and handling dropped connections to make conversations feel human, not robotic. Multi-stream synchronization: Coordinating concurrent WebSockets from LiveKit, Fetch agents, and Claude while running computer vision without blocking the UI. Context management: Long patient conversations exceeded LLM limits. Built a summarization pipeline to compress transcripts while preserving critical clinical details. Accomplishments Built a cohesive multi-agent ecosystem where Fetch.ai, LiveKit, and Claude agents autonomously coordinate. Implemented Claude's multi-tool-calling to interpret natural language and update the 3D hospital map in real-time. Created a facial photoplethysmography (FPPG) pipeline for non-invasive heart rate monitoring integrated with voice and spatial intelligence. What we learned Specialized agents outperform monolithic systems—focused tasks are more scalable despite coordination complexity. Low-latency architecture requires deep system design when streaming video, analyzing behavior, and raising real-time alerts. Next Steps New Agents: Medication Reconciliation: Prevent dangerous drug interactions Discharge Planning: Coordinate patient transitions Resource Allocation: Optimize room and staff assignments Technical Improvements: Reinforcement learning from nurse feedback Computer vision for fall detection and behavioral monitoring Federated learning across hospitals while preserving privacy <div