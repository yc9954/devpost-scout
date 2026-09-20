---
slug: "castanea"
url: "https://devpost.com/software/castanea"
title: "Castanea"
hackathon: "PANDA Hacks 2025"
organization: "PANDA Organization"
winner: true
words: 358
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
---

# Castanea

> Three AI agents working in sync to research, analyze, and create — freeing you to focus on ideas that matter.

[Devpost](https://devpost.com/software/castanea) · hackathon [[PANDA Hacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]]

**stack** gemini, google-adk, javascript, perplexity, python, react, vite

## How they structured the write-up

- about the project
- how i built it
- what i learned
- challenges i faced

## Body

Agentic AI Researcher Agent: ADK + Perplexity Writer Agent in ADK Web UI Researcher Agent in ADK Web UI About the project Castanea was inspired by the real challenges students face when working on academic tasks — from researching complex topics to summarizing dense texts and crafting well-structured essays. Too often, these tasks require switching between multiple tools, sources, and formats. I wanted to create a single AI-powered platform that could handle all three seamlessly, freeing up time for learning rather than tool management. The core idea was to simulate a small “AI office” with specialized agents: 🧠 ResearcherAgent for in-depth topic exploration using a Retrieval-Augmented Generation (RAG) pipeline powered by Perplexity and Gemini Pro. ⚡ AnalystAgent for lightning-fast text summarization and key point extraction using Gemini Flash. ✍️ WriterAgent for generating original content and saving it directly to files. How I built it The frontend is built with Vite , React , and JavaScript for a responsive and modern interface. The backend uses Python , Agent Development Kit (ADK) , and integrates with Gemini Pro/Flash models alongside Perplexity’s Sonar API . Architecture overview: User inputs a request. The central dispatcher determines the correct specialist agent. The selected agent executes its task: ResearcherAgent → multi-step query decomposition → Perplexity search → Gemini Pro synthesis. AnalystAgent → text analysis → concise summarization. WriterAgent → original content generation → optional file save. I also included .env configuration for secure API key management and separated frontend/backend environments for scalability. What I learned How to design an agent-based architecture that feels natural to the user. The importance of clear task routing to avoid overloading a single AI model. Practical integration of RAG workflows combining real-time search with LLM synthesis. Fine-tuning prompt engineering for consistency across multiple AI agents. Challenges I faced Time constraints : Designing, coding, and integrating multiple agents within hackathon deadlines. Balancing speed and accuracy : Finding the right trade-off between Gemini Pro’s depth and Gemini Flash’s speed. Query decomposition : Teaching the ResearcherAgent to break broad topics into precise sub-questions for better results. User experience : Making the interface intuitive while showcasing the power of three different agents. <div