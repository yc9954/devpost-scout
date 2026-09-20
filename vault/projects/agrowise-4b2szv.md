---
slug: "agrowise-4b2szv"
url: "https://devpost.com/software/agrowise-4b2szv"
title: "AgroWise"
hackathon: "AI For Good"
organization: "connecting-dreams foundation"
winner: true
words: 1263
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "user/developer"
  - "user/educator_student"
  - "user/frontline_worker"
  - "user/government_staff"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# AgroWise

> AgroWise fuses low-cost root-zone sensors with AI and IVR to provide precision farming via any phone. It blocks banned chemicals and cuts water use by 40%, reaching the 50% of farmers without 4G.

[Devpost](https://devpost.com/software/agrowise-4b2szv) · hackathon [[AI For Good]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[voice_speech]]
**domain** [[accessibility]] [[agriculture_food]] [[civic_government]] [[climate_energy]] [[education]] [[health_clinical]] [[housing_homeless]]
**user** [[developer]] [[educator_student]] [[frontline_worker]] [[government_staff]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[transcript_audio]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** chromadb, claude, esp32, expo.io, fastapi, firebase, firestore, gemini, google-cloud, html/css, javascript, langchain, lora, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agrowise

## Body

Inspiration Indian farmers are making life-or-death crop decisions blind . Root-zone moisture deficits, pH imbalances, and early fungal infections happen underground, invisible to the naked eye. By the time a crop wilts, the physiological damage is already permanent. The farmer then over-waters or under-waters, triggering a vicious cycle of root rot or stunting. The numbers tell a brutal story: 146 million smallholder farmers in India 1 extension officer per 1,000+ farmers Soil testing takes days and costs money Weather apps give 20km averages , missing the micro-climate that triggers blight on a specific field Most agritech apps need a smartphone + 4G . Half of rural India has neither. We started AgroWise with a simple question: What if every farmer, smartphone or feature phone, could see what's happening underground, in real time, in their own language? What it does AgroWise is a three-layer phygital precision agriculture system that bridges the digital divide: Layer 1: AgroSense Spike (Hardware) A solar-powered, deploy-and-forget IoT sensor (ESP32-based) that sits in the root zone measuring soil moisture, temperature, and humidity every 30 minutes. Under ₹800 BOM. No buttons, no battery swaps, no maintenance. Spikes communicate via LoRa long-range radio to a shared village gateway hub with a single SIM card, one hub serves 50–100 farmers. Layer 2: AgroWise App (Software + AI) A Progressive Web App featuring: "Soil Thirst" gauge , visual, intuitive, no jargon Action cards , "Water Field Today" or "Hold Off" (not percentages) AI-powered disease diagnosis that combines leaf photos WITH soil sensor data for higher accuracy. A yellowing leaf might look like nutrient deficiency, but if soil humidity is high, it's actually fungal stress, our system catches this. AgroMind conversational agent that remembers your farm history across sessions, crop stage, past diagnoses, seasonal patterns CIBRC safety filter , every AI response is checked against a government database of 448 chemicals (88 banned). Banned substances are architecturally blocked , not just flagged. Layer 3: Kisan-Vani IVR (Voice) Toll-free voice alerts in Hindi, Bengali, and Odia for feature-phone farmers. Zero internet, zero app required. The system proactively CALLS the farmer when soil crosses critical thresholds. Works on any phone that can receive a call, even a ₹500 feature phone on a 2G network. How we built it AI Architecture We use an agentic architecture with intent-based tool binding, not a simple chatbot. Intent Classifier (Claude 3.5 Sonnet via TrueFoundry, ~8 tokens) categorizes farmer queries into 11 intent categories Based on intent, only relevant tools are bound to the main agent (Gemini 2.5 Flash via Vertex AI). A weather query can't accidentally trigger pesticide recommendations. The agent runs a tool loop (max 6 iterations) gathering data from IMD weather APIs, Agmarknet mandi prices, ICAR knowledge base, and 221K KCC farmer Q&A transcripts indexed in ChromaDB A mandatory CIBRC post-filter scans every response for banned chemicals using regex word-boundary matching before it reaches the farmer For disease diagnosis, Gemini 2.5 Vision analyzes leaf photos alongside real-time soil sensor data, this neuro-symbolic fusion is what distinguishes us from image-only solutions like Plantix. RAG Pipeline Intent-aware retrieval across two ChromaDB collections: ICAR knowledge base (soil testing manuals, crop nutrition guides) KCC transcripts (221K+ real farmer Q&As from data.gov.in, licensed under GODL-India) Embeddings: Vertex AI text-embedding-005 (768 dimensions). Relevance threshold: 0.3. Deduplication by first 100 characters. IoT & Connectivity Spike → Hub : LoRa 868 MHz radio (2–5 km range in open fields) Hub → Cloud : 4G/2G cellular (Jio IoT SIM, ₹49–99/month) Hub serves : 50–100 spikes. Cost per spike per month: ₹1–2. Offline resilience : Spike buffers 7 days of readings locally. App uses Redux Persist for offline caching. Mobile React Native + Expo for cross-platform delivery. Action-card UI designed for low-literacy farmers, icons over text, voice readout for alerts. Voice (IVR) Sarvam AI for text-to-speech in Indic languages. Threshold-triggered outbound calls via toll-free number. Testing 272 unit tests (all passing), deliberately mocked (no live API calls). Separate integration scripts for live IMD/Agmarknet connections. Tests validate intent routing, safety filtering, tool binding logic. Challenges we ran into Hardware survivability across Indian climates : India ranges from 48°C Rajasthan deserts to -15°C Kashmir winters to 3000mm Kerala monsoons. We solved this with IP67-sealed ABS housing, capacitive sensors that read through the housing wall (never touching soil directly), and supercapacitors instead of lithium batteries. Connectivity in rural India : WiFi is useless in open fields (30m range). Putting a SIM in every spike costs ₹100/month/spike. Our breakthrough was the hub-and-spoke LoRa architecture , spikes use long-range radio to a shared gateway. One SIM serves an entire village. Building farmer trust : Sontu Da told us directly, "I have seen people come with tablets and apps before and nothing ever worked." What convinced him was the spike physically going into his soil and showing data he couldn't see. The physical device creates trust that software alone cannot. Language accessibility : 7 of 12 test farmers rated English-only screens as unusable . We defaulted to Hindi/Bengali from login and made language our highest-priority design decision. It became our highest-rated feature (4.7/5). LLM safety in agriculture : An AI hallucinating a banned chemical name could cause real harm, poisoned soil, health damage. We built two independent safety gates : the CIBRC tool-level check AND a post-response regex filter. Even if the LLM hallucinates, the filter catches it. Accomplishments that we're proud of Field-tested with 12 real farmers in Kharagpur, West Bengal, in Hindi and Bengali Trust rating: 4.6/5 (memory feature was highest rated) Language accessibility: 4.7/5 , our highest-rated feature Intent to continue using: 83% (10 of 12 farmers said yes) Sontu Da's story : Was about to buy unnecessary fertilizer. Our system combined his leaf photo with soil data and correctly identified fungal stress from humidity, not nutrient deficiency. Saved his money. Saved his crop. 272 unit tests passing on the backend Won NSCIF 2026 (National Student Change Initiatives Fest), 1st place, ₹50,000 prize, organized by Connecting Dreams Foundation & Ashoka at EMPI Business School, New Delhi Spike BOM under ₹800 , less than a bag of DAP fertilizer What we learned The biggest lesson wasn't technical, it was entrepreneurial . We walked into NSCIF 2026 as engineers who built a working prototype. On Day 1, the jury grilled us on hardware feasibility across Indian climates, sensor deployment density, rural connectivity, and business model viability. We stumbled on some answers. We corrected course overnight, rebuilt our hardware narrative, designed the hub-and-spoke connectivity model, and mapped the distribution strategy through existing Krishi Vigyan Kendra networks. Day 2, we came back with answers grounded in reality, not just code. Key learning : Engineers build systems. Entrepreneurs build trust. The spike physically going into a farmer's soil creates more trust than any demo deck ever could. We also learned that Responsible AI isn't a feature you add, it's how you architect from day one. The CIBRC safety filter, the mandatory tool enforcement, the source-cited responses, these aren't afterthoughts. They're structural decisions that make the difference between a research project and a system farmers can actually trust with their livelihoods. What's next for AgroWise Pilot deployment : 500 spikes across 3 villages in West Bengal (Month 1–6) Injection-molded housing + PCB assembly , moving from hand-soldered prototypes to production hardware with IP67 certification LoRa gateway firmware and hub management dashboard B2G district dashboards , aggregated soil health data for agricultural extension officers Expand language support via Sarvam AI to cover more Indic languages Nutrient sensing module (NPK add-on, ₹400 extra) in v3.0 Target: 50,000+ farmers through KVK networks across West Bengal and Odisha within 36 months <div