---
slug: "smart-planner"
url: "https://devpost.com/software/smart-planner"
title: "Kiro and Smart Planner ✅"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 454
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Kiro and Smart Planner ✅

> Planner that help you to do anything, built with cutting-edge IDE - Kiro! 🚀

[Devpost](https://devpost.com/software/smart-planner) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** amazon, claude, fastapi, gpt-oss-20b, javascript, kiro, llm, ollama, python, react, tailwind, typescript

## How they structured the write-up

- 🌟 inspiration
- 🧠 what it does
- 🏗️ how i built it
- 🧩 challenges i ran into
- 🏆 accomplishments i proud of
- 📚 what i learned
- 🚀 what's next for "planner that guides you to do anything" ✅

## Body

🌟 Inspiration I wanted a planner that actually helps you move from idea to action—without sending data anywhere. 🤖 AI-Powered Development This project was developed with significant assistance from Kiro IDE , an AI-powered spec-to-code development environment that helped: 📋 Requirements Analysis - Generated comprehensive project requirements and user stories 🏗️ Architecture Design - Created detailed system architecture and component design documents ✅ Task Planning - Broke down development into structured, manageable tasks 💻 Feature Development - Implemented most of the core application features including: React 19 frontend with TypeScript and modern hooks FastAPI backend with proper async patterns Database models and API endpoints AI integration with Ollama for task generation Real-time chat interface and task management The project was built from scratch with 99% made by Kiro. I've decided to attend 2 hackathons same time: OpenAI Open Model Hackathon Code with Kiro Hackathon Existing task tools are - either overcomplicated or could not provide guidance. I combined a local gpt-oss-20b + local application + calendar to create a planner that feels like a pusher instead of a passive checklist and used KIro IDE as assistant. 🧠 What It Does Planner turns natural language into steps and keeps them actionable: Write your ideas→ get generated tasks Local-first — no data leaves your machine Smart status lifecycle Frontend optimized for fast iteration: React 19 + Vite + React Query + Zustand 🏗️ How I Built It Layer Tech Notes IDE Kiro AI first IDE that helped to plan and develop application UI React 19, TypeScript, Tailwind, Zustand, React Query Fast dev loop + clear separation of server vs client state API FastAPI (async) Clean routing, dependency injection, OpenAPI docs Data SQLAlchemy + Alembic Migrations + enum modeling DB SQLite (dev) / PostgreSQL (ready) Simple local spin‑up; scalable path AI Ollama local models Deterministic prompt shaping; privacy preserved Calendar Google Calendar API Optional integration via service layer Validation Pydantic (backend) + Zod (frontend) Dual runtime + compile‑time safety 🧩 Challenges I Ran Into Kiro is always forgetting context Connecting Ollama to API How to work with old and newly created task lists Handling errors on each step 🏆 Accomplishments I Proud Of Fully local AI workflow — can work without internet Clean UI - it's easy to start planning new goals I will actually use it to generate tasks and add it to my Google Calendar 📚 What I Learned How to create AI empowered full stack application Prepare AI model response for API Local-first application development 🚀 What's Next for "Planner That Guides You To Do Anything" ✅ Analyzing if goal is currently achievable Learn previous goals and actually propose new ones Made with ❤️ for builders who want AI superpowers without surrendering privacy. <div