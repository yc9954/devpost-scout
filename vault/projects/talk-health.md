---
slug: "talk-health"
url: "https://devpost.com/software/talk-health"
title: "Talk-Health"
hackathon: "Dev Season of Code "
organization: "DSOC Official"
winner: true
words: 261
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/clinician"
---

# Talk-Health

> An AI chatbot with multilingual (English & Akan) speech and text support for health assistance.

[Devpost](https://devpost.com/software/talk-health) · hackathon [[Dev Season of Code]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[clinician]]

**stack** fastapi, mongodb, nextjs, typescript

## How they structured the write-up

- 🌍 inspiration
- 🚀 what i built
- 🧠 key challenges
- 📚 what i learned
- 🌟 impact

## Body

🩺 Akan Health Assistant 🌍 Inspiration Akan Health Assistant was inspired by the language barrier many people face when accessing digital healthcare tools. Most AI health platforms operate only in English, limiting accessibility for local language speakers. I wanted to build an inclusive AI health assistant that supports both English and Akan , while providing an engaging, human-like experience. 🚀 What I Built A full-stack AI-powered health assistant featuring: 🤖 3D AI Doctor Interface using React Three Fiber with speech synthesis 🌍 Multilingual Support (English & Akan) 🔍 Real-Time Web Search Integration via DuckDuckGo API 📊 Health Records & Analytics Dashboard 🔐 JWT-Based Authentication System 📱 Fully responsive UI 🛠 Tech Stack Frontend: Next.js 14, TypeScript, Tailwind CSS, shadcn/ui Backend: FastAPI, MongoDB, Motor, Pydantic, JWT Search Integration: aiohttp + DuckDuckGo The system processes a health query by detecting language, querying a local medical knowledge base, optionally enhancing results with real-time web data, and returning a confidence-scored response: [ Confidence = \frac{Relevance + ContextMatch + SourceReliability}{3} ] 🧠 Key Challenges Handling multilingual medical terminology in Akan Optimizing 3D rendering performance across devices Managing async operations (MongoDB + web search) efficiently Securing sensitive health data with proper authentication and validation 📚 What I Learned This project strengthened my skills in: Full-stack architecture design Async backend development with FastAPI Type-safe frontend development with TypeScript 3D web rendering and performance optimization Building inclusive, socially impactful AI systems 🌟 Impact Akan Health Assistant demonstrates how AI can bridge language gaps in healthcare, combining accessibility, real-time intelligence, and immersive interaction into a scalable digital health solution. <div