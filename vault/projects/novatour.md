---
slug: "novatour"
url: "https://devpost.com/software/novatour"
title: "NovaTour"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 930
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# NovaTour

> NovaTour: Your AI Travel Companion That Talks, Plans, and Books — All by Voice.

[Devpost](https://devpost.com/software/novatour) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: deterministic_policy</sub>
**domain** [[developer_tools]]
**substrate** [[geospatial]] [[transcript_audio]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** amazon-bedrock, amazon-dynamodb, amazon-nova-act, amazon-nova-lite, amazon-nova-multimodal-embeddings, amazon-nova-sonic, amazon-web-services, fastapi, google-gemini, google-places, google-routes-api, maplibre-gl, next.js, openweather-api

## Body

Inspiration Every year, travelers spend an average of 5+ hours researching and planning a single trip — juggling flight aggregators, hotel sites, weather apps, maps, and review platforms across dozens of browser tabs. We asked: what if you could just talk to someone who handles all of it? NovaTour was born from the vision of a voice-first travel intelligence — an AI companion that doesn't just answer questions but actively orchestrates your entire trip in real-time conversation. Inspired by the way a seasoned travel concierge works — listening to your preferences, pulling together options, adjusting the plan on the fly — we set out to build the world's first fully voice-driven, end-to-end travel planning and booking agent powered entirely by Amazon Nova. The launch of Amazon Nova Sonic (bidirectional speech-to-speech) and Nova Act (autonomous browser control) made this vision technically possible for the first time: a single AI system that can hear you , reason about your trip , search real-time travel data , generate a visual itinerary , and book your flights — all in one seamless voice conversation. What It Does NovaTour is a full-duplex voice AI travel assistant that: Listens & Understands — Real-time speech recognition via Amazon Nova Sonic with barge-in support (interrupt the AI mid-sentence, just like a real conversation) Searches & Reasons — Orchestrates 8 specialized travel tools in real-time: flights, hotels, attractions, routes, weather, and more Plans & Visualizes — Generates day-by-day itineraries with Amazon Nova Lite, rendered as interactive timelines and maps with route polylines Books Autonomously — Uses Amazon Nova Act to navigate Google Flights and complete real bookings through browser automation Adapts Verbosity — A novel Level-of-Detail (LOD) system with 60+ bilingual trigger patterns lets users dynamically control response depth — from quick facts to immersive podcast-style narration How We Built It Architecture: Browser (Next.js 16 + React 19) ↕ WebSocket (full-duplex audio + events) FastAPI Backend (Python 3.13) ├── Strands BidiAgent (Nova Sonic wrapper) ├── 8 Travel Tools (@tool decorated) ├── LOD Adaptive System (60+ patterns) └── 3-Tier Resilience Engine AWS Services ├── Amazon Nova Sonic (voice) ├── Amazon Nova Lite (reasoning) ├── Amazon Nova Act (booking) └── DynamoDB + S3 (persistence) Voice Pipeline: We built a custom bidirectional audio streaming pipeline using the Strands Agents SDK's BidiAgent class. The browser captures microphone audio, resamples from native rate → 16 kHz PCM, base64-encodes it, and streams it over WebSocket at ~85ms intervals. The backend feeds this into Nova Sonic and simultaneously streams back 24 kHz audio responses, transcripts, and tool call events. The result is a sub-second voice interaction with full barge-in support. Tool Orchestration: Each of our 8 travel tools is built as a Strands @tool -decorated function with: Primary API integration (Google Places, Google Routes, OpenWeather, Gemini Search, Nova Lite, Nova Act) Automatic mock fallback for resilient demo/testing @retry_api_call() decorator with exponential backoff Error classification ( is_recoverable() ) for intelligent retry vs. fail-fast decisions LOD System: Our most innovative feature — a 3-level verbosity control system: LOD 1 (Brief): 15–40 words, quick answers for time-pressed travelers LOD 2 (Standard): 80–150 words, conversational recommendations LOD 3 (Narrative): 400–800 words, immersive podcast-style storytelling with sensory details The system uses 60+ bilingual (English/Chinese) trigger patterns with priority-based signal classification (explicit > implicit) and confidence scoring. Users can switch modes naturally: "tell me more" → LOD 3, "keep it short" → LOD 1. System prompts are dynamically interpolated without restarting the voice session. 3-Tier Resilience: Every component follows our fallback architecture: Primary path (BidiAgent + real APIs) Retry with exponential backoff MockAgent fallback (ensures the app never crashes) Plus: idle timeout detection (45s), WebSocket auto-reconnect (3 attempts), and TTS sanitization (strips markdown for natural speech). Frontend: Built with Next.js 16 and React 19 — no external UI libraries. The interface features: Real-time voice transcript display with interim/final states Interactive itinerary timeline with activity photos MapLibre GL map with day-coded markers and route polylines Nova Act booking progress overlay with live screenshots LOD selector for manual verbosity control Challenges We Faced Full-Duplex Audio Synchronization — Achieving gapless 24 kHz audio playback while simultaneously streaming 16 kHz input required careful AudioContext scheduling and buffer management. We solved this with scheduled AudioBufferSourceNode chains and a nextStartTime tracker. Barge-In Handling — When the user interrupts the AI mid-sentence, we need to instantly clear the audio playback buffer, cancel pending responses, and transition the voice state machine. This required a custom VoiceStateMachine with 4 states and validated transitions. Nova Act Dependency Conflict — Nova Act requires strands-agents ≤1.23.0 , but BidiAgent (Nova Sonic) needs ≥1.30.0 . We solved this with isolated installations ( --no-deps ) and runtime ImportError handling. Tool Result Enrichment — Itineraries generated by Nova Lite lack coordinates for activities. We built a places cache that stores coordinates from search_places calls and automatically injects them into itinerary activities, enabling map visualization. Bilingual LOD Detection — Supporting both English and Chinese trigger patterns required careful priority ordering and confidence scoring to avoid false positives from ambiguous phrases. What We Learned Amazon Nova Sonic's bidirectional streaming is remarkably low-latency — achieving near-human conversational feel The Strands Agents SDK's BidiAgent abstraction elegantly handles the complexity of voice + tool orchestration Adaptive verbosity (LOD) dramatically improves voice UX — users instinctively adjust detail level Resilience engineering is non-negotiable for voice applications — any dropped frame or timeout breaks the conversational illusion What's Next Multi-language expansion beyond English and Chinese Persistent trip memory using DynamoDB sessions (infrastructure already provisioned) Collaborative planning — multiple travelers in one voice session Nova Multimodal Embeddings for destination-aware recommendations (model configured, integration planned) <div