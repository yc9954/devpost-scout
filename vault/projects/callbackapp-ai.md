---
slug: "callbackapp-ai"
url: "https://devpost.com/software/callbackapp-ai"
title: "CallbackApp AI"
hackathon: "The AI Champion Ship "
organization: "LiquidMetalAI"
winner: true
words: 627
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# CallbackApp AI

> Sometimes you need a call… and no one's there. Loneliness hits 20–60% of adults worldwide, and life rarely waits—Introducing "Personas as a Service"; your AI companions just a phone call away.

[Devpost](https://devpost.com/software/callbackapp-ai) · hackathon [[The AI Champion Ship]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]] [[mental_health]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]]

**stack** cerebras, cloudflare, deepgram, elevenlabs, liquidmetal, raindrop, stripe, twilio, vultr, workos

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for callbackapp ai

## Body

WorkOS Login (both user and admin use WorkOS) and phone verification User flow (assumes verified number and minutes available) Admin Persona Designer Voice call flow Prompt compilation and injection Smart Memory Placement Inspiration Sometimes you need someone to talk to — but no one’s around. Loneliness affects a huge portion of adults, and beyond that, life just happens at inconvenient times. The 3am anxiety. The last-minute pep-talk before an interview. The moment you just need to think out loud. We wanted something that could call you back like a real person , remember you, and be there when you need it. What it does CallbackApp AI gives you AI companions you can talk to over real phone calls — and they remember you over time. Key features: Real-time phone calls you answer just like any other call Persistent memory of your identity, history, interests, and ongoing life events Scheduled callbacks (daily check-ins, wakeups, accountability reminders, affirmations) Custom personas with chosen personalities and conversational style Low-latency voice pipeline enabling natural back-and-forth conversation Secured on user and admin side with WorkOS + AuthKit Stripe payments and coupons How we built it Frontend: Vue 3 SPA with Pinia + Tailwind CSS, deployed on Vercel Backend: API gateway on Cloudflare using Raindrop Workers, with SmartMemory + KV cache Voice Pipeline: Running on a Vultr VPS using WebSocket streaming with Twilio telephony Speech + AI stack: Deepgram Flux for STT & turn-taking, Cerebras LLM for sub-200ms inference, ElevenLabs for natural TTS Database: PostgreSQL for users, personas core prompts, calls, histories, credits Scheduler: Cron-based service to trigger reminders and scheduled callbacks Challenges we ran into Getting clean, real-time audio working was tricky — sample-rate mismatches caused static and took a long debugging session with raw PCM inspection to fix Interrupting the AI mid-sentence is technically difficult with streaming + multi-service orchestration Cloudflare Workers can’t make outbound WebSocket connections, so we had to split the system between Raindrop's edge and a Vultr VPS Late-in-the-game development environment breakdowns (WSL crashes) emphasized the importance of frequent commits and safe tooling Accomplishments that we're proud of Achieved sub-1000ms latency for voice-to-voice communication Built a full end-to-end system that handles auth, personas, memory, calls, scheduling, voice pipeline, and payments Assembled everything into a working product within a hackathon timeframe Created a layered memory + prompt architecture to maintain context across calls and let the AI “know you” like a friend Produced comprehensive documentation describing the design and operation of the tech stack What we learned Real-time audio + LLMs + memory is non-trivial — latency and interruption handling are the biggest hurdles Edge functions are great for APIs, but not for full-duplex audio; infrastructure must adapt around platform limitations Persistent memory extraction and handling transforms AI from a chatbot into a long-term companion Rapid iteration requires discipline: commit often, document decisions, use AI tools to not only assist with code but to continually assist in appraising priorities, minimize environment fragility What's next for CallbackApp AI Improve persona depth, memory recall, and context scaffolding (no limit with well-designed use of the SmartComponents) Build more "intelligent interruptions" with improved voice gestures and context-tracking UX polish: onboarding, scheduling UI, conversation history, improved persona editor Potential fine-tuning using synthetic conversational data to enhance emotional intelligence and personalization Expand use-cases (social features, group calls, coaching knowledge, therapy-like reflective session support, productivity companions ) CI/CD pipeline setup Voice-command integrations ("Brad, set a follow-up call about this for two days from now at noon") Represent diversity in the selection of personas (every persona gets its own Twilio number, which is why we are able to have them in our contacts separately; otherwise I would build a persona designer for users as well, but for now "core sets" of internally-developed personas are what need engineered.) <div