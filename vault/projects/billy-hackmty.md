---
slug: "billy-hackmty"
url: "https://devpost.com/software/billy-hackmty"
title: "Billy - HackMTY"
hackathon: "HackMty 2025"
organization: "TEC ACM"
winner: true
words: 390
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/small_business"
  - "substrate/structured_db"
---

# Billy - HackMTY

> Smart CRM for small businesses that combines powerful analytics, intuitive management, and an AI assistant that understands your business conversations.

[Devpost](https://devpost.com/software/billy-hackmty) · hackathon [[HackMty 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[small_business]]
**substrate** [[structured_db]]

**stack** aiven, elevenlabs, gemma, llm, mysql, react, render

## How they structured the write-up

- inspiration
- what we learned
- how we built it
- challenges we faced
- the result

## Body

About the Project Inspiration The inspiration for Billy came from observing how small businesses often struggle with fragmented tools for sales, inventory, and financial tracking. Many rely on spreadsheets or manual processes, which makes decision-making slow and error-prone. We wanted to build something that not only centralized their operations but also understood their business language — an AI-driven assistant that could turn daily conversations into structured insights. Our goal was simple: make business management as intuitive as talking to a teammate. What We Learned Throughout development, we learned how powerful it is to combine structured data systems with conversational interfaces. Integrating an AI model (via LocalAI/Ollama ) taught us about prompt engineering, context management, and how to make an AI sound more business-aware . We also strengthened our understanding of: Full-stack integration (React + TypeScript + Express + MySQL) Real-time communication between multiple APIs Deployment and orchestration of AI services locally Designing intuitive UI/UX for non-technical business users How We Built It Frontend: CRM for Billy App — Built with React (TypeScript) using Tailwind CSS and shadcn/ui for styling. Handles all user interactions and visual analytics. Web API: API for Billy Web — Node.js + Express + MySQL backend for managing business data, analytics, and user sessions. AI API: API for Billy AI — Integrates LocalAI/Ollama models for text understanding, summarization, and conversational intelligence. The architecture allows each service to communicate independently, making the system modular and scalable. $$ \text{Total Insight} = \text{Data Management (Web API)} + \text{AI Understanding (AI API)} + \text{User Interaction (Frontend)} $$ Challenges We Faced Context retention for AI conversations: Keeping long conversation histories without overloading the model required careful pruning and dynamic summarization. Synchronizing APIs: Ensuring that the AI API and Web API stayed in sync during parallel requests was a technical challenge that involved debugging CORS, latency, and JSON payload issues. Performance under local environments: LocalAI provided flexibility, but managing GPU/CPU memory constraints and model response times was non-trivial. Designing an approachable UX: Translating complex analytics into simple dashboards while keeping the UI responsive across devices took significant iteration. The Result Billy is now a complete ecosystem — a smart CRM that brings together analytics, operations, and AI-driven decision support. It gives small businesses the same technological leverage as large enterprises, but in a tool that feels natural, personal, and effortless to use. <div