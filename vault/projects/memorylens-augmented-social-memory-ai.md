---
slug: "memorylens-augmented-social-memory-ai"
url: "https://devpost.com/software/memorylens-augmented-social-memory-ai"
title: "MemoryLens : Augmented Social Memory AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 534
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# MemoryLens : Augmented Social Memory AI

> MemoryLens uses computer vision and speech AI to recognize faces and recall past conversations in real time, ethically augmenting human memory so you never forget a name or context.

[Devpost](https://devpost.com/software/memorylens-augmented-social-memory-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[education]] [[mental_health]]
**user** [[educator_student]] [[researcher]]
**substrate** [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** deepgram-speech-intelligence-api, face-recognition-(128-dim-facial-embeddings), mongodb-atlas-(vector-based-memory-storage), next.js-15-+-typescript, numpy, openai/gemini-llm-apis, opencv, python-(fastapi-backend), tailwind-css, websockets-(real-time-streaming)

## How they structured the write-up

- the problem
- our solution: memorylens
- technical architecture
- impact & usefulness
- privacy & ethical design
- challenges & innovation
- future roadmap
- why this project matters

## Body

Real-time face recognition overlay displaying name, last meeting date, and conversation context instantly. View stored contacts, last meeting dates, and AI-summarized conversation history in a structured memory dashboard. The Problem Human memory is powerful, but unreliable. In professional, academic, and social environments, forgetting names, context, or previous discussions can lead to lost opportunities, awkward interactions, and increased anxiety. Networking events. Conferences. Team collaborations. We constantly rely on memory.. yet biological memory has limits. What if AI could extend human memory responsibly? Our Solution: MemoryLens MemoryLens is a real-time multimodal AI system that augments human social memory. Using a camera interface (webcam for this prototype, wearable-ready architecture for future smart glasses), MemoryLens: Detects a face in real time Matches it using facial embeddings Retrieves the last recorded interaction Displays contextual information instantly After each conversation, users can record a short voice note. The system: Transcribes speech using Deepgram Extracts key topics Summarizes the conversation Detects emotional tone Securely links the memory to that individual The next time you meet them, context reappears seamlessly. Technical Architecture MemoryLens is a multimodal AI system combining: Computer Vision OpenCV for real-time face detection face_recognition for generating 128-d facial embeddings Cosine similarity matching for identification Optimized frame downscaling to reduce CPU load Speech Intelligence Deepgram API for high-accuracy transcription LLM-based summarization (OpenAI/Gemini) Automatic topic extraction Emotional tone classification Intelligent Memory Storage MongoDB Atlas for structured memory storage Vector-style embedding matching In-memory embedding caching for low-latency performance WebSocket streaming for near real-time recognition Frontend Experience Next.js 15 + TypeScript Tailwind CSS Live webcam feed Dynamic bounding box overlays Context cards rendered in real time The system processes lightweight frames every 1.5 seconds to balance performance and accuracy. Impact & Usefulness MemoryLens is assistive AI. It benefits: Students building professional networks Professionals managing hundreds of contacts Neurodivergent individuals who struggle with social recall Individuals with mild cognitive memory challenges Beyond networking, this has implications for: Assistive cognitive healthcare tools Wearable AI companions Context-aware IoT systems This is AI augmenting humans, not replacing them. Privacy & Ethical Design Privacy is core to MemoryLens. No external identity databases No scraping of third-party facial data User-controlled embedding storage No mass surveillance architecture Designed for personal, ethical augmentation only We believe the future of AI must be responsible and human-centered. Challenges & Innovation Building a real-time multimodal AI system required solving: Frame optimization to avoid CPU overload Real-time embedding matching at low latency Stable WebSocket communication Accurate recognition under varied lighting Designing overlays that feel natural and non-intrusive We implemented: Frame downscaling Embedding caching in RAM Similarity threshold tuning Lightweight WebSocket payloads The result is a stable, responsive prototype. Future Roadmap MemoryLens is wearable-ready. Future developments include: Meta Smart Glasses integration On-device encrypted embedding storage Calendar & CRM integration Smart follow-up reminders Multi-person conversation tracking Edge-device offline optimization MemoryLens could evolve into a personal AI memory operating system. Why This Project Matters AI is increasingly capable of seeing, hearing, and understanding. The key question is not: Can we build it? The real question is: Can we build it responsibly? MemoryLens demonstrates a frontier application of multimodal AI that enhances human connection while respecting privacy. Not for surveillance. Not for manipulation. But for meaningful human interaction. <div