---
slug: "firstwaveai"
url: "https://devpost.com/software/firstwaveai"
title: "FirstWaveAI"
hackathon: "United Hacks V6"
organization: "Hack United"
winner: true
words: 469
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/social_worker"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# FirstWaveAI

> AI-powered emergency intake with human oversight for dispatchers

[Devpost](https://devpost.com/software/firstwaveai) · hackathon [[United Hacks V6]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[health_clinical]] [[transportation]]
**user** [[social_worker]]
**substrate** [[geospatial]] [[transcript_audio]]

**stack** fastapi, groq, langchain, langgraph, next.js, python, typescript

## How they structured the write-up

- 💡 inspiration
- 🚨 what it does
- 🛠️ how i built it
- ⚠️ challenges i ran into
- 🏆 accomplishments i’m proud of
- 📚 what i learned
- 🚀 what’s next for firstwaveai

## Body

System Architecture Agentic AI System 💡 Inspiration 📞 Over 240 million emergency calls are made in the United States each year (National Emergency Number Association), putting extreme pressure on dispatchers in life-or-death situations. In those critical first moments, key details can be missed, delayed, or misunderstood when callers are panicking. FirstWaveAI was built to rethink the emergency intake process. I created an AI-powered call assistant that speaks directly with callers, asks clarifying questions, and structures critical information in real time. The system then visualizes the situation on a live map, identifies nearby resources, and generates an AI-assisted dispatch recommendation, all while keeping a human dispatcher in full control with an approval override. 🚑 🚨 What it does FirstWaveAI is a real-time emergency dispatch assistant that combines speech recognition, multi-agent AI, and interactive visualization to help dispatchers work faster and more accurately. 🔧 Core Features 🎙️ Voice-First Interface Callers can speak naturally using the Web Speech API , while the system transcribes the conversation in real time and maintains a full transcript. 🧠 Multi-Agent AI Pipeline (LangGraph + LLaMA 3.3 70B) Six specialized AI agents work together to analyze the call: 📝 Extraction Agent – Captures key details (location, injuries, hazards, people count) 🚦 Triage Agent – Assigns priority levels (P1–P4) ❓ Next-Question Agent – Suggests clarifying follow-ups 🚓 Dispatch Planner – Recommends EMS, Fire, or Police 🗺️ Resource Locator – Finds nearest available units with ETAs 🛡️ Safety Guardrail – Ensures ethical RECOMMENDATIONS 🖥️ Interactive Dashboard A clean three-column interface shows: Live chat transcript 💬 AI-generated emergency summary 📝 Dispatch recommendations with approve/cancel controls ✅❌ 🗺️ Resource Mapping An interactive Leaflet map displays nearby hospitals, fire stations, police, and pharmacies with distances and travel times. 🛠️ How I built it Frontend Next.js 16 + React 19 Tailwind CSS 4 (custom emergency theme) shadcn/ui components Leaflet + Openstreetmap Web Speech API TypeScript Backend FastAPI LangGraph (multi-agent orchestration) Groq + LLaMA 3.3 70B Fish Audio API (TTS) Server-Sent Events (SSE) for real-time updates ⚠️ Challenges I ran into Building AI for real emergencies is hard . 🔁 Avoiding redundant questions – The AI kept asking things the caller already said, so I had to add strict memory rules. ⏱️ Speed vs. accuracy – P1/P2 emergencies required immediate action, while P3/P4 allowed more questioning. Encoding this logic took serious prompt tuning. ⚖️ Ethical safety – I carefully designed guardrails to prevent harmful questions. 🏆 Accomplishments I’m proud of 🎯 This was my first fully solo hackathon project ! 📚 What I learned 🗂️ Solo project management — better scoping, prioritization, and focus 🐞 Debugging under pressure — isolating issues across multiple systems quickly 🚀 What’s next for FirstWaveAI 🔗 MCP Integration - Replace mock data with real Model Context Protocol servers for: Live emergency unit locations Hospital availability Real-time traffic conditions <div