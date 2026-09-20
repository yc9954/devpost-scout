---
slug: "aegis-jtde8o"
url: "https://devpost.com/software/aegis-jtde8o"
title: "Aegis"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 784
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# Aegis

> A real-time 911 dispatch co-pilot that transcribes, translates, and protocol-grounds every call, then spins up secure AI agents to handle mass emergencies.

[Devpost](https://devpost.com/software/aegis-jtde8o) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[multi_agent]] [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]] [[structural_withholding]] [[voice_speech]]
**domain** [[developer_tools]] [[disaster_emergency]] [[health_clinical]] [[transportation]]
**user** [[small_business]]
**substrate** [[financial_record]] [[geospatial]] [[transcript_audio]]

**stack** armoriq, carto, claude, cloudfair, deepgram, leaflet.js, nextjs, node.js, osrm, react, redis, sentry, tailwindcss, the-token-company

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for aegis

## Body

UI Tech stacks Inspiration 911 call centers buckle under mass-casualty events, earthquakes, mass shootings, multi-vehicle pileups — when hundreds of calls arrive in languages dispatchers don't speak, all at once. I wanted to build the co-pilot that lets a single human dispatcher do the work of ten, without ever letting an AI give freelance medical advice. What it does Aegis is a real-time dispatch console. A caller speaks in any language; Aegis live-transcribes, translates, classifies the incident, pulls up the correct vetted protocol card (CPR, choking, childbirth, structure fire, etc.), finds the nearest available unit by real road routing, and speaks instructions back in the caller's own language, all in under a few seconds, with a live latency breakdown per pipeline stage. When the system detects a mass emergency (e.g. our earthquake demo), it goes autonomous: every caller gets their own AI dispatch agent, grouped under area "manager" agents that allocate ambulances/police/fire across a zone with no double-booking, all reporting up to a main coordinator agent that keeps global situational awareness, while a human stays one tap away. ArmorIQ secures every agent at every level : each agent's plan is captured and cryptographically authorized via ArmorIQ's Intent Intelligence SDK before it can act, and any deviation from protocol is blocked, not just logged. We also built a live phone-to-laptop demo: open the app on your phone over a Cloudflare tunnel, hit "Talk," and watch the call appear live on the dispatcher dashboard, exactly like a real incoming 911 call. How we built it Frontend: Next.js 16 (App Router) + React 19 + TypeScript + Tailwind CSS v4, a dark "operations console" design system, Leaflet + CARTO dark-matter tiles for the live incident map. Gateway: a standalone Node.js + ws WebSocket server brokering mic audio and orchestrating the whole pipeline, separate from the Next.js process for clean real-time streaming. Speech-to-text: Deepgram nova-3 with language=multi , streamed over a raw WebSocket, with PII redaction and interim results for sub-second feedback. LLM: Anthropic Claude, claude-haiku-4-5 on the hot path using structured outputs to guarantee valid JSON for translation, incident classification, and structured-field extraction; claude-sonnet-4-6 to compile the post-call incident report. Prompt compression: The Token Company compresses every prompt before it hits Claude, visible live on the latency meter. Text-to-speech: ElevenLabs multilingual voices speak instructions back to the caller in their own language. Data layer: Redis Stack — RediSearch vector search to confirm the right protocol card, GEOSEARCH for nearest unit/hospital, Streams for the per-call audit trail, Pub/Sub for the live supervisor board — with a zero-dependency in-memory fallback so the whole stack runs without Docker. Routing: OSRM for real road-network routing and ETA to the dispatched unit. Security: ArmorIQ's Intent Intelligence SDK ( capturePlan + getIntentToken ) signs and authorizes every agent's plan at the caller, manager, and main-coordinator level, with a local protocol-grounded guardrail as a safe fallback. Observability: Sentry traces every call as a transaction with a child span per pipeline stage, retries once on failure, and fires an SLA alert if the loop exceeds 4 seconds. Phone-as-caller: a Cloudflare Tunnel plus a custom Node reverse proxy puts the page and WebSocket gateway behind one HTTPS origin, so a real phone (which requires a secure context for mic access) can be the live caller while the laptop runs the dispatcher view. Challenges we ran into Keeping caller-facing instructions safe by construction : Claude only selects and translates a pre-vetted protocol card; it never invents medical advice. That constraint shaped almost every other design decision. Streaming raw mic audio reliably from a phone, over a tunnel, into Deepgram, while keeping the dispatcher's dashboard perfectly in sync, including a tricky React bug where an unstable callbacks object caused an infinite re-render loop on the caller page, traced back to a missing useMemo . Allocating units across simultaneous incidents in an area without double-booking the same ambulance was solved with a greedy nearest-unit assignment inside each area-manager agent. Securing a 3-tier agent hierarchy with ArmorIQ rather than a single agent, so verification happens independently at the caller, manager, and main-coordinator levels. Accomplishments that we're proud of A full, real (non-mocked) pipeline: live Deepgram transcription, live Claude extraction, live ElevenLabs speech, live Redis geo/vector search, live OSRM routing, all wired together end to end. A working phone-as-911-caller demo that's indistinguishable from a real emergency call coming into the dashboard. A genuine multi-agent hierarchy, not a single LLM call dressed up as "agents", with cryptographically signed, ArmorIQ-verified intent at every level. What's next for Aegis Wire ArmorIQ's blocking path into a live "agent paused, human takeover required" UI state. Auto-resolve background/demo calls so the supervisor board self-cleans over time. Expand the protocol library and add real multi-jurisdiction unit data. <div