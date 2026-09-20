---
slug: "voice-baby-night-companion"
url: "https://devpost.com/software/voice-baby-night-companion"
title: "Nova Baby Guardian"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 647
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/social_worker"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Nova Baby Guardian

> An agent-driven baby care copilot that turns parent voice and text into real-time baby logs, safe next steps, and trusted medical guidance.

[Devpost](https://devpost.com/software/voice-baby-night-companion) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[social_worker]]
**substrate** [[transcript_audio]] [[video_visual]]

**stack** css, fastapi, nova2lite, nova2sonic, novaact, vite, websocket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that i'm proud of
- what we learned
- what's next for nova baby guardian

## Body

Project Story Inspiration Night caregiving is one of the most exhausting parts of early parenthood. Parents often need to make quick decisions while half awake: how much the baby drank, when the last diaper change happened, whether a fever requires attention, and what to do next. Most baby apps focus on passive tracking or simple chatbots. I wanted to build something more practical: a system that can listen, understand, record events, and guide parents through daytime and nighttime caregiving workflows . My goal was to create an AI assistant that acts less like a chatbot and more like a real-time caregiving co-pilot . What it does Nova Baby Guardian is a web-based AI assistant designed to help parents manage baby care through natural interaction. Users can interact with the system through text or voice to log caregiving events and receive guidance. Key capabilities include: Voice or text logging Parents can say things like “baby drank 200ml” or “changed diaper,” and the system records the event automatically. Care timeline tracking Milk intake, diaper changes, and caregiving activities are stored in a live timeline and summarized for quick review. Trusted medical guidance mode If users ask questions like “baby has fever,” the system provides guidance and trusted official resources. Day and night workflow support The assistant keeps track of caregiving activities across both daytime and nighttime contexts. Overall, the system turns casual inputs into structured caregiving data and actionable insights . How we built it The system is built as a lightweight AI web application with real-time interaction. Frontend Vite + vanilla JavaScript + CSS Chat-based interface with a full-screen Voice Mode Live caregiving timeline and structured logs Backend FastAPI server with WebSocket support Event parsing and structured log storage Workflow orchestration for model calls Amazon Nova models Nova 2 Lite Handles reasoning, intent understanding, and structured responses. Nova 2 Sonic Powers real-time voice conversations and speech interactions. Nova Act Used for workflow scaffolding to retrieve trusted guidance links when medical questions arise. Interaction pipeline Voice or text input → intent parsing → structured event logging → AI reasoning → UI updates and suggested actions This architecture allows the system to combine conversation, memory, and actions into a single workflow. Challenges we ran into Voice-to-logging accuracy Speech recognition transcripts can be noisy (for example: “m l”, fragmented phrases). I added transcript normalization and fallback parsing to improve logging reliability. Dependency conflicts The Nova Act SDK introduced dependency conflicts with the main FastAPI runtime. I resolved this by isolating Nova Act in a separate virtual environment and configuring explicit runtime paths. UI complexity Early versions included too many modules and confused users. I simplified the interface into a workflow-first UI with clearer logs, status indicators, and actions. Accomplishments that I'm proud of Built a working voice-enabled AI caregiving assistant Successfully integrated multiple Amazon Nova models in a single system Implemented structured event logging from natural language input Designed a real-time caregiving timeline Created a system that combines conversation, memory, and actions Most importantly, the prototype demonstrates how AI agents can assist with real-world caregiving workflows , not just conversations. What we learned I learned that AI assistants become significantly more useful when they combine: Reasoning Memory Actions rather than functioning as simple chat interfaces. In caregiving scenarios, structured logging and clear escalation guidance are just as important as model intelligence. I also learned that real-time voice systems require careful handling of transcripts, turn boundaries, and fallback behavior to maintain reliability. What's next for Nova Baby Guardian Future development could expand the system into a full caregiving platform: Persistent cloud storage for caregiving history Pediatric guideline integration for smarter recommendations Smart reminders for feeding schedules and medication Image-based features such as diaper rash or symptom checking Ultimately, I envision Nova Baby Guardian evolving into an AI-powered caregiving companion that helps parents stay informed, organized, and less stressed during early parenthood. <div