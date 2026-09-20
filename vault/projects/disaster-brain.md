---
slug: "disaster-brain"
url: "https://devpost.com/software/disaster-brain"
title: "Disaster Brain"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1324
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "user/frontline_worker"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Disaster Brain

> When the internet dies and lives are on the line, Disaster Brain is the only AI that still works.

[Devpost](https://devpost.com/software/disaster-brain) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[structural_withholding]]
  <sub>weak: voice_speech</sub>
**domain** [[climate_energy]] [[disaster_emergency]] [[health_clinical]]
**user** [[frontline_worker]] [[general_public]] [[patient_family]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** bases, chromadb, fastapi, gguf-quantization, knowledge, next.js, node.js, ollama, pwa, python, react, sqlite, typescript, web-speech-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for disaster brain

## Body

Here's everything, ready to copy-paste section by section: Inspiration It started with a single question: what happens when a field medic needs AI help — and there's no internet? We kept finding the same answer: nothing. Every AI tool ever built requires a cloud connection. And the first thing that dies in any disaster — earthquake, flood, airstrike — is the internet. Cell towers fall. Power grids fail. Signal vanishes. 170 million people live in active conflict zones right now. In Ukraine, Sudan, Gaza, Afghanistan — field medics are making life-or-death triage decisions alone, overwhelmed, with nothing but a paper manual that gets wet, burns, or gets destroyed by the same blast that caused the casualties. Triage — deciding who gets treated first, who can wait, who cannot be saved — has to happen in seconds, under extreme cognitive load, with zero support. We didn't build Disaster Brain because it was a cool technical challenge. We built it because this gap is real, it's deadly, and nobody had filled it. What it does Disaster Brain is an offline-first AI co-pilot for disaster first responders and conflict zone field medics. It runs a full AI model entirely on the device — no API calls, no cloud, no internet connection required. Ever. Voice Triage — The medic describes a patient's symptoms out loud. The AI returns a structured, color-coded triage card (RED / YELLOW / GREEN / BLACK) in under 5 seconds, offline. It automatically detects whether the situation is a disaster (START triage) or combat (TCCC with full MARCH breakdown) — no manual switching required. Photo Assessment — Point the camera at any wound. On-device multimodal vision analyses blast wounds, burns, crush injuries, and gunshots, returning a severity rating and immediate action steps. The image never leaves the device. Patient Queue — All triaged patients are automatically sorted by priority in real time, giving the medic full situational awareness across all casualties at a glance. Protocol Knowledge — Ask any medical question — drug dosages, procedure steps, protocol order — and get answers grounded in real WHO emergency protocols, FEMA guidelines, and NATO TCCC manuals via offline RAG. SITREP Generator — One tap generates a military-standard Situation Report from all patient data in 8 seconds. The same report takes a field commander 20 minutes to write manually. Comms Bridge — Bilingual voice translation across 11 languages — English, Hindi, Tamil, Arabic, Ukrainian, Dari, Pashto, French, Bengali, Telugu, and Swahili — entirely offline, for when the medic and survivor don't share a language. How we built it The core stack is built around one constraint: everything must work with zero network connectivity, on consumer mobile hardware, under real field conditions. Local LLM — We run a quantized language model via Ollama using GGUF quantization, tuned to fit on a mobile device while preserving enough reasoning quality for medical triage decisions. Offline RAG — ChromaDB is embedded fully on-device, seeded with WHO emergency protocols, FEMA disaster response guidelines, and NATO TCCC manuals. All retrieval is local — no vector server, no API. Frontend — A Next.js PWA, installable on any Android or iOS phone or tablet. Voice input uses the Web Speech API. All patient records are stored in local SQLite. Nothing is ever transmitted. Vision — On-device multimodal image analysis for wound assessment, running inference locally without any cloud vision API. Translation — Offline multilingual voice translation supporting 11 languages including low-resource languages like Dari, Pashto, and Swahili, with no external translation service. Protocol Auto-detection — A context classification layer that automatically distinguishes disaster scenarios (START triage) from combat scenarios (TCCC/MARCH) from the medic's voice input alone. Challenges we ran into Quantization vs. quality tradeoff — Shrinking an LLM small enough to run on a phone while keeping it medically reliable was brutal. Too small and the triage reasoning breaks. Too large and it won't run on field hardware. A hallucination in a drug dosage recommendation doesn't fail gracefully — it kills. We went through many quantization configurations before finding the right balance. Offline RAG without infrastructure — Getting ChromaDB to run fully embedded and locally — with accurate, grounded retrieval from real medical documents — was one of our hardest problems. Standard RAG setups assume a server. We had none. We had to rearchitect the entire pipeline to be self-contained on the device. Protocol auto-detection — Building a system that reliably distinguishes a disaster scenario from a combat scenario from raw, noisy voice input — without any manual toggle from the medic — required significant prompt engineering and classification work. Low-resource language support offline — Most offline translation libraries simply don't support Dari, Pashto, or Swahili. Finding and integrating models that could handle these languages on-device, at acceptable speed, took far longer than we expected. Multimodal vision at the edge — Running wound assessment vision inference on-device with enough accuracy to be medically useful, within real hardware constraints, meant abandoning several approaches entirely before finding one that actually worked. Accomplishments that we're proud of The demo is the accomplishment. Turn on airplane mode. Open the app. Describe a patient injury out loud. Get a triage decision back in under 5 seconds. No internet. No server. No API key. Just a phone and an AI that works. Beyond that: A fully offline RAG pipeline grounded in WHO, FEMA, and NATO TCCC documents — running entirely on-device Auto-detection of disaster vs. combat protocol from voice context alone, with no manual input from the medic Offline multilingual voice translation across 11 languages, including Dari, Pashto, and Swahili A SITREP generator that turns all patient data into a military-standard report in 8 seconds A system architected entirely around the hardest constraint in AI deployment: zero connectivity We set out to build something that works when everything else doesn't. It does. What we learned We learned that "offline AI" is not just a feature flag you toggle. It is an entirely different architecture. Every assumption that modern AI tooling is built on — cloud APIs, vector servers, remote inference, hosted models — has to be thrown out and rebuilt from scratch. We learned that the hardest part of building for extreme environments isn't the AI. It's the constraints. Hardware limits, no network, noisy voice input, low-resource languages, real medical accuracy requirements — each one alone is manageable. All of them together, simultaneously, is a completely different problem. We learned that when the use case is high enough stakes, "good enough" is not a standard you can accept. A triage AI that hallucinates a protocol step or gets a drug dosage wrong isn't a failed product — it's a dangerous one. That raised the bar for everything we built. And we learned that the problems worth solving are almost never the ones that are easy to demo. What's next for Disaster Brain Field validation — We want to get Disaster Brain into the hands of real NGO medics, combat casualty care trainers, and disaster response organizations for live feedback. The architecture is right. The protocols need real-world stress testing. Expanded protocol library — Adding more medical knowledge bases: MSF (Médecins Sans Frontières) field guides, ICRC emergency manuals, and country-specific disaster response protocols. Wearable integration — Hands-free operation via smartwatch or bone-conduction audio for medics who can't hold a phone while treating a patient. Mesh networking — Enabling multiple Disaster Brain instances to share patient data peer-to-peer over Bluetooth or local Wi-Fi mesh when a team of medics is operating in the same area — still with zero internet dependency. More languages — Expanding the Comms Bridge to cover additional conflict-zone languages, with a focus on the most underserved linguistic regions. Official certification pathway — Working toward alignment with WHO and NATO medical standards so Disaster Brain can be formally adopted by humanitarian and military medical organizations. The goal from day one was never to win a hackathon. It was to build something that saves lives. That work doesn't stop here. <div