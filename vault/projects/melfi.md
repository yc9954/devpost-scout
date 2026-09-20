---
slug: "melfi"
url: "https://devpost.com/software/melfi"
title: "Melfi"
hackathon: " GenAI Genesis 2026"
organization: "GenAI Genesis"
winner: true
words: 520
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/mental_health"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Melfi

> A custom RLHF fine-tuned AI agentic therapist that calls your phone and builds an interactive 3D terrain out of your conversations. Because everyone needs someone to talk to.

[Devpost](https://devpost.com/software/melfi) · hackathon [[GenAI Genesis 2026]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[voice_speech]]
**domain** [[mental_health]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[transcript_audio]]

**stack** deepgram, nextjs, postgresql, python, pytorch, supabase, twilio, typescript, vapi

## How they structured the write-up

- inspiration: human empowerment!
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for melfi

## Body

Landing Page Dashboard Insights Emotional Terrain Inspiration: Human Empowerment! Melfi started with our own personal challenges: needing support and someone to talk to. Traditional therapy is often expensive and inaccessible for many, and there was a need for a tool that fills this gap while feeling real and present. With Melfi, users can feel more empowered in their lives by having a safe space to process their emotions. What it does Melfi is an AI therapist that calls you on your phone for a conversation. It remembers what you've talked about across sessions, adapts its approach based on what you share, and visualizes your emotional history as a navigable 3D terrain. This allows you to zoom out and visually see your low points, breakthroughs, all the slow, hard work in between. How we built it The core model that you talk to is a Qwen3-8B model fine-tuned with Reinforcement Learning from Human Feedback (RLHF), using the Direct Preference Optimization (DPO) algorithm on the Psychotherapy-LLM dataset (36k rows). It is served via vllm and is hosted on our own server, i.e. self-hosted, and exposed over a Cloudflare Tunnel. For the phone calls, we use Vapi. Vapi handles the outbound dial through Twilio, speech-to-text via Deepgram, and voice synthesis via ElevenLabs. After each call, Groq (Llama 3 specifically) analyzes the transcript to extract mood scores, themes, and a memory summary. That summary gets embedded locally and stored in Supabase's pgvector index via a call to the Hugging Face Inference API using the sentence-transformers/all-MiniLM-L6-v2 model, so the next call starts with context and Melfi remembers all your past conversations. The frontend is Next.js with a Three.js terrain that maps time, mood, and emotional volatility into a 3D landscape you can orbit and explore. Challenges we ran into Getting low-latency voice to feel natural was harder than expected. The model's chain-of-thought output was causing Vapi to drop calls before we caught it and disabled thinking at the server level. Wiring the full pipeline, i.e. call initiation, real-time transcription, post-call analysis, memory storage, and live terrain updates without any single piece breaking took most of the time. Deploying a self-hosted model and keeping it reliably reachable was something new for us. Accomplishments that we're proud of Melfi makes real phone calls. It's not like every other chat interface. Your phone rings, you pick up, and there's a model on the other end you can actually converse with. We're also proud of the fact that we fine-tuned an open-source model using RLHF on a sizable dataset instead of simply making API calls to a proprietary LLM. What we learned We learned to work with voice models and APIs (Vapi, Twilio, Elevenlabs) and that voice is a fundamentally different medium than text, and also the future of apps that feel real and human. The therapeutic value of the format (like the commitment of answering a phone and the absence of a screen to hide behind) is worth building around. What's next for Melfi Implementing a cron job so that the agent autonomously performs daily calls at the user's preferred time. Also, launching Melfi as a product. <div