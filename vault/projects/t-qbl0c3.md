---
slug: "t-qbl0c3"
url: "https://devpost.com/software/t-qbl0c3"
title: "SwiftER"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 417
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# SwiftER

> AI-powered ambulance & multi-hospital management system for faster (swifter), smarter care

[Devpost](https://devpost.com/software/t-qbl0c3) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[geospatial]] [[structured_db]] [[transcript_audio]]

**stack** docker, fastapi, javascript, maplibre, node.js, openai, openrouteservice, osrm, python, react, supabase, tailwindcss, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what's next for swifter

## Body

Home dashboard Transcription section of ambulance dashboard Navigation section of ambulance dashboard Hospital dashboard Hospital map dashboard Inspiration Thousands of lives are lost each year. Not because an ambulance wasn't fast enough, but because outdated radio systems led it to the wrong hospital. When an ambulance arrives, the ER may be full or poorly equipped to handle the patient’s condition, so we aim to replace traditional communication methods with intelligent, real-time coordination. What it does swiftER is an intelligent ambulance–hospital coordination system that automatically assigns ambulances to hospitals that best fit the patient. On the ambulance’s side, we use voice transcription to extract patient data and symptoms. This data is then best matched with a hospital’s data, and the ambulance’s navigation system is automatically assigned to the designated hospital. On the hospital’s end, we track ambulances incoming as well as bed capacity and specialist availability to accommodate future patient-hospital fit. Finally, we have a global GPS system to track all hospitals and ambulance movement on a map in real-time and ensure ambulances reach hospitals safely. How we built it Frontend: Built with React, TypeScript, Vite, and TailwindCSS. This includes the Ambulance App (tablet), a centralized Maps Dashboard (using MapLibre GL JS), and individual Hospital Dashboards. Backend: Python-based agents (FastAPI) handle the logic. This includes a Reasoning Agent for NLP extraction and a Woodwide Reasoning Agent for routing logic. Database: Supabase (PostgreSQL) acts as the central source of truth for patient incidents and hospital data. AI & Logic: We integrated Wispr Flow for voice-to-text, Wood Wide AI for the routing decision model, and OSRM (Open Source Routing Machine) to calculate accurate road distances and ETAs. Accomplishments that we're proud of I think a non-technical accomplishment we are proud of is group coordination and multi-tasking. We each had dedicated pages of the project we worked on while periodically discussing seamless integration to ensure no errors. We are also proud of our full project architecture and the framework workflow we have developed as things flow very well together and update concurrently. What's next for swiftER A main area we hope to target in the future is hospital-to-hospital transfers. Currently, no such prevalent system for doing this exists, and we hope to be the first to develop a concrete solution. Therefore, we hope to have a system that can manage and track all current patients waiting before being attended to in the hospital with a feature to transfer a patient with a hospital decision system similar to our current implementation. <div