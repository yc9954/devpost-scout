---
slug: "ai-steam-lab"
url: "https://devpost.com/software/ai-steam-lab"
title: "Ai Steam Lab"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 587
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# Ai Steam Lab

> "AI-STEAM-Lab adapts to every student in real time — Socratic AI tutoring, computer vision engagement tracking, and RAG-powered STEM knowledge, all in one platform."

[Devpost](https://devpost.com/software/ai-steam-lab) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[health_clinical]]
**user** [[educator_student]] [[patient_family]]
**substrate** [[document_pdf]] [[geospatial]] [[transcript_audio]]
  <sub>weak: sensor_telemetry</sub>

**stack** 18, actions, api, ci/cd, css, docker, events, fastapi, gemini, github, jwt, langchain, numpy, opencv

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai steam lab

## Body

GIF Interactive Prediction Interface - User-friendly interface for generating AI-powered insights and results GIF AI Analytics Dashboard - Real-time monitoring of AI model performance, predictions, and system metrics GIF Anomaly Detection Results - Visualization of detected events, alerts, and confidence scores GIF Building Intelligent Systems with AI, Computer Vision & Machine Learning Inspiration Most STEM students don't fail because they lack ability — they fail because the tools available to them don't adapt. Textbooks are static. Videos don't pause when you're confused. Tutors are expensive. We built AI-STEAM-Lab because we believe every student, regardless of background or location, deserves a learning experience that meets them exactly where they are. What it does AI-STEAM-Lab is an agentic STEM learning platform that personalizes education in real time. A student asks a question — the system doesn't just retrieve an answer, it reasons through it using a ReAct agent loop, pulling from a curated STEM knowledge base via pgvector RAG, and responds with Socratic dialogue calibrated to the student's demonstrated level. Key capabilities: Adaptive Socratic tutoring powered by Gemini 2.5 Flash RAG-based knowledge retrieval over a structured STEM corpus (pgvector) Real-time engagement tracking via OpenCV at 60+ FPS — detects attention and adjusts pacing Streaming responses via FastAPI SSE for a fluid, conversational feel Progressive Web App built in React 18 — works on any device, including low-end hardware How we built it The architecture is fully Dockerized with CI/CD across four core services: Agent layer : ReAct loop with Gemini 2.5 Flash — plan, retrieve, reason, respond Knowledge layer : pgvector on PostgreSQL for semantic STEM document search Vision layer : OpenCV pipeline for real-time student engagement detection Frontend : React 18 PWA with Server-Sent Events for live streaming output Every component was built for production — not a demo. The system handles concurrent sessions, graceful fallback when retrieval confidence is low, and mobile-first rendering for accessibility in low-resource environments. Challenges we ran into Latency in the agentic loop : chaining retrieval + reasoning + streaming without blocking the UI required careful async orchestration in FastAPI OpenCV on varied hardware : achieving consistent 60+ FPS tracking across different webcam qualities and lighting conditions required adaptive preprocessing RAG quality over STEM content : generic embeddings performed poorly on mathematical and scientific text — required domain-specific chunking strategies and retrieval tuning Accomplishments that we're proud of Built a fully production-grade agentic system — not a wrapper, not a demo Achieved real-time vision-based engagement detection running alongside live LLM inference without performance degradation Designed a system accessible on low-end devices as a PWA — making it viable for students in underserved regions End-to-end Dockerized deployment with CI/CD — ready to scale What we learned Building AI-STEAM-Lab taught us that personalization in education isn't just about content — it's about pacing , tone , and awareness . The hardest engineering problem wasn't the AI; it was making the AI feel like a patient collaborator rather than a search engine. We also learned how fragile RAG pipelines become at the edges of a domain — STEM content demands precision that general-purpose embeddings don't provide out of the box. What's next for AI Steam Lab Knowledge graph layer : prerequisite mapping so the system can detect conceptual gaps and recommend foundational topics automatically Multi-modal content ingestion : lecture video → Whisper transcription → CLIP frame embeddings → unified STEM knowledge graph Collaborative study rooms : shared sessions where the agent facilitates group problem-solving Offline mode : cached knowledge base for students with unreliable internet <div