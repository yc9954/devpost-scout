---
slug: "memoria-the-biographer-agent"
url: "https://devpost.com/software/memoria-the-biographer-agent"
title: "Memoria: The Biographer Agent"
hackathon: "AI Partner Catalyst: Accelerate Innovation"
organization: "Google"
winner: true
words: 400
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/elder_child_care"
---

# Memoria: The Biographer Agent

> A voice-first app designed for the elderly to preserve their life stories without needing to type or use complex interfaces.

[Devpost](https://devpost.com/software/memoria-the-biographer-agent) · hackathon [[AI Partner Catalyst- Accelerate Innovation]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
  <sub>weak: realtime_stream</sub>
**domain** [[elder_child_care]]
  <sub>weak: developer_tools</sub>
  <sub>weak: structured_db, video_visual</sub>

**stack** cloud-build, cloud-run, elevenlabs, gcp, google-cloud, node.js, python, react, vertex-ai

## Body

Memoria Interface 🌟 Inspiration Memoria was born from a desire to bridge the gap between generations. As our elders age, their stories—the tapestry of our shared history—often fade away. We wanted to create a tool that isn't just a database, but an empathetic companion that listens, remembers, and helps transform fleeting memories into a lasting legacy. The goal was to make technology "invisible" so that the focus remains entirely on the human story. 🧠 What I Learned Building Memoria was an intensive journey into the cutting edge of AI: Conversational AI Engineering : Learning to manage state and context in real-time voice interactions using the ElevenLabs SDK. Advanced RAG (Retrieval-Augmented Generation) : Implementing a "Infinite Memory Engine" to ensure the AI maintains continuity across multiple interview sessions. Senior-Centric UX : Understanding that for the elderly, "high-tech" must feel "low-effort." This meant prioritizing high-contrast dark modes, large interactive areas, and minimal menu structures. Multimodal Orchestration : Coordinating visual analysis (Vertex AI Vision) with verbal story extraction. 🛠️ How I Built It The project is built on a modern, high-performance stack: Frontend : Developed with React 19 and Vite for a snappy experience, styled with Tailwind CSS 4 for a premium, custom aesthetic. Backend : A Python FastAPI server that acts as a custom LLM bridge, orchestrating the intelligence of the system. AI Core : Powered by Google Vertex AI , utilizing Gemini 1.5 Flash for deep reasoning, text-embedding-004 for the memory search, and Imagen 3 for generating cinematic illustrations for the memoir. Voice : Integrated ElevenLabs for industry-leading text-to-speech and speech-to-text with extremely low latency. Persistence : SQLite serves as our vector and fragment store, keeping everything lightweight yet powerful. 🚧 Challenges Faced Latency vs. Intelligence : One of the biggest hurdles was performing RAG lookups and complex LLM reasoning fast enough to keep the voice conversation feeling natural. We solved this with background tasks and optimized prompt chaining. Contextual Continuity : Ensuring the AI remembers that "Aunt Martha" mentioned in the first session is the same person mentioned in the fifth required a robust entity extraction and linking system. Senior Accessibility : Designing a dark mode that was "premium" yet highly readable for users with visual impairments involved many iterations on typography and color contrast. Multimodal Integration : Syncing uploaded photos with specific timestamps in a conversation to create the "Audible Storybook" feature was a complex state management challenge. <div