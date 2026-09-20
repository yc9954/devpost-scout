---
slug: "healthme-cshbay"
url: "https://devpost.com/software/healthme-cshbay"
title: "HealthMe"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 452
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/clinician"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/transcript_audio"
---

# HealthMe

> Health.me is an AI that calls doctors' offices for you. Tell it what you need, it finds nearby clinics, picks up the phone, talks to the receptionist, and books your appointment.

[Devpost](https://devpost.com/software/healthme-cshbay) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: voice_speech</sub>
**domain** [[health_clinical]]
  <sub>weak: finance_payments</sub>
**user** [[clinician]]
**substrate** [[geospatial]] [[medical_record]] [[transcript_audio]]

**stack** elevenlabs, express.js, firebase, gcp, gemini, mapbox, node.js, react, twilio

## Body

Health.me is a voice-first AI health assistant that: Chats with context — Understands your health history, current vitals, and symptoms to provide personalized guidance Finds care nearby — Displays clinics on an interactive map based on your location and needs Calls clinics for you — Our AI agent actually phones the clinic, navigates the conversation with the receptionist, and books your appointment while you watch a live transcript Handles emergencies — Emergency calling when every second counts Speaks and listens — Fully voice-enabled so you can talk naturally, hands-free How we built it Frontend: React + TypeScript with Tailwind CSS for a clean, medical-grade UI Voice AI: ElevenLabs for natural text-to-speech and AI phone agents that sound human Chat Intelligence: Google Gemini for context-aware health conversations Real-time: Socket.io for live call transcripts and instant updates Maps: Mapbox for clinic discovery and location visualization Backend: Python/Flask orchestrating the AI agents and phone calls Data: Firebase/Firestore for secure chat history and user profiles Challenges we ran into Real-time sync — Keeping the UI, call transcript, and backend state in sync during live calls was tricky Audio handling — Managing browser audio permissions, voice input, and TTS playback simultaneously without conflicts Google Gemini integration — Configuring Gemini to maintain conversation context across multiple turns while keeping responses concise and medically appropriate took significant iteration. We had to carefully craft system prompts to prevent the AI from giving overly generic advice or being too verbose. -ElevenLabs voice agents — Getting the AI phone agent to handle real-world receptionist conversations was harder than expected. Receptionists don't follow scripts—they interrupt, and ask unexpected questions. Accomplishments that we're proud of It actually calls people — Not a mockup, not a demo. Our AI picks up the phone and has real conversations End-to-end voice — Speak your symptoms, hear the response, watch the AI book your appointment—no typing required Live transparency — Users see exactly what the AI is saying in real-time, building trust Polished UX — A calming, professional interface that feels like a premium healthcare product What we learned ElevenLabs' conversational AI is incredibly powerful for phone-based agents Real-time WebSocket state management gets complex fast—plan your event architecture early Healthcare UX needs to balance efficiency with reassurance; people need to feel in control Voice-first interfaces require rethinking traditional UI patterns entirely What's next for Health.me Insurance integration — Auto-verify coverage before booking Prescription management — Refill requests handled by AI agents Multi-language support — AI agents that can speak to clinics in multiple languages Family accounts — Book appointments for dependents with proper authorization EMR integration — Connect directly with electronic medical records for seamless context Proactive health nudges — Remind users about checkups, vaccinations, and follow-ups <div