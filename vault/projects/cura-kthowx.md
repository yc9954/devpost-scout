---
slug: "cura-kthowx"
url: "https://devpost.com/software/cura-kthowx"
title: "Cura"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 333
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
---

# Cura

> AI Medical Assistant: Intelligent Symptom Checker and Care Connector

[Devpost](https://devpost.com/software/cura-kthowx) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]]

**stack** chromadb, creao, fastapi, livekit, mongodb, python, swift

## How they structured the write-up

- 🩺 project story: cura

## Body

🩺 Project Story: Cura About the Project Cura is an AI-powered medical voice assistant designed to make healthcare more accessible and responsive. It listens to patient symptoms, provides personalized guidance, connects users to doctors, and schedules appointments — all through natural, human-like conversation. We were inspired by how difficult it can be to access immediate medical advice, especially when clinics are overwhelmed or unavailable. Our goal was to create an intelligent assistant that supports both patients and healthcare professionals by automating symptom triage, appointment scheduling, and follow-up care. Through building Cura, we learned how to integrate real-time voice AI , generative language models , and healthcare data systems into one cohesive workflow. We explored challenges in conversational design, natural language understanding, and securely managing patient interactions. Cura’s architecture combines: 🎙️ LiveKit Agents — for real-time voice calls and natural dialogue ⚙️ FastAPI and MongoDB — for backend data storage and healthcare logic 🧠 Chroma — as a vector database for symptom similarity search and matching, which diagnose patient's issue and give advice based on healthcare service's internal data 📅 CreaoAI — for intelligent scheduling and calendar integration 💻 Creao (React web) and Swift (mobile) — for patient and provider dashboards Gmail API for appointment booking confirmation * Challenges Faced Building Cura presented several key challenges: Designing natural and empathetic voice conversations that adapt to user tone and intent Managing speech latency for real-time responses Algorithm to match the most similar symptoms from user's input. We separate each symptom from healthcare data and embed each of them to count the number of matching symptoms and get average cosine similarity that receives best result * Structuring a scalable database that connects patients, clinicians, and appointment data Integrating multiple APIs (LiveKit, Chroma, Gmail) into a seamless workflow Ensuring that AI-generated responses remain medically cautious and privacy-aware Despite these challenges, we successfully created a working prototype that listens to patients, identifies symptoms, connects them with doctors, and schedules appointments — all through an intelligent voice interface. <div