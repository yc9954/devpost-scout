---
slug: "orbit-59jths"
url: "https://devpost.com/software/orbit-59jths"
title: "Orbit"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 329
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# Orbit

> Real-time facial recognition that identifies connections, remembers conversations, and maps your professional network

[Devpost](https://devpost.com/software/orbit-59jths) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**substrate** [[geospatial]] [[transcript_audio]]

**stack** cerebras, deepface, fastapi, groq, langchain, opencv, python, react, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for orbit

## Body

Inspiration Networking and meetings often start with guesswork—who's in the room, what do they do, how should you start the conversation? Then afterwards, much of the context is forgotten. We wanted a tool that helps before, during, and after the conversation—giving you instant context, saving the discussion, and mapping out relationships. What it does Orbit transforms networking with real-time AI: Instant face recognition pulls public profiles the moment someone enters your view Persistent identity indexing remembers everyone across sessions with full conversation history Live transcription captures every word while generating smart follow-up suggestions Dynamic relationship mapping visualizes connections between people and shared interests Every interaction becomes structured, searchable, actionable intelligence. How we built it This is technically insane for a 36-hour hackathon: Custom computer vision pipeline with OpenCV + DeepFace + FaceCheckID handling multiple faces simultaneously through parallel processing Real-time multithreading architecture achieving sub-second latency via WebSocket connections Persistent face indexing creates searchable memory—instant recognition with full conversation history when someone reappears Live conversation intelligence using Whisper + LLMs for real-time context analysis and follow-up generation Advanced relationship mapping with Sigma.js algorithms connecting people through shared interests Polished React interface hiding massive technical complexity behind intuitive design Challenges we ran into Real-time performance while orchestrating multiple heavy AI models simultaneously Reliable face indexing across lighting conditions and multiple participants Complex data pipeline from video → recognition → scraping → analysis without latency bottlenecks Accomplishments that we're proud of Revolutionary networking experience never built before—real-time social intelligence through computer vision Technical breakthrough : Parallel face recognition, conversation indexing, and relationship mapping working seamlessly Exceptional UX : Complex AI systems hidden behind interface anyone can use instantly What we learned Real-time AI orchestration requires careful architecture—every millisecond matters for instant user experience Computer vision complexity multiplies in real-world conditions with lighting, angles, and multiple faces What's next for Orbit Enhanced recognition accuracy under challenging conditions Privacy-first architecture with comprehensive opt-in controls Enterprise deployment for conferences and professional networking at scale <div