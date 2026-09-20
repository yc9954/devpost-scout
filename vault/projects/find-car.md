---
slug: "find-car"
url: "https://devpost.com/software/find-car"
title: "CallForYou – AI That Finds Cars, Calls Dealers, Books Drives"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 995
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# CallForYou – AI That Finds Cars, Calls Dealers, Books Drives

> CallForYou learns what you want, finds your best-fit cars, calls every dealership, books your test drives, and gives you a personalized inspection guide — all automatically. Zero hassle.

[Devpost](https://devpost.com/software/find-car) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[retail_commerce]] [[supply_logistics]] [[transportation]]
**substrate** [[document_pdf]] [[geospatial]] [[transcript_audio]] [[video_visual]] [[web_dom]]

**stack** deepgram, docker, fastapi, foxit, langchain, langgraph, linode, marketcheck, mongodb, openai, python, react, twilio, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- foxit pdf services
- akamai (via linode)
- deepgram voice agent
- architecture diagrams
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cardeal dial - ai that calls dealerships on your behalf

## Body

high level architecture voice pipeline user flow QR code to live demo Inspiration Car shopping is tedious: scrolling through dozens of listings, comparing prices, and calling dealerships to ask about availability. Many people avoid it or feel stressed by the back-and-forth. We built CarDeal Dial so an AI could learn what you want and do the heavy lifting—search, curate, and call dealers for you. What it does CarDeal Dial is an AI car-shopping assistant that: Collects preferences via chat — Tell it what you want (make, model, budget, zip) in natural language. Scrapes car data from the web — Uses MarketCheck API to find listings matching your criteria. Curates results — Scores and ranks vehicles; you shortlist the ones you like. Calls dealerships for you — An AI voice agent dials dealers, asks about availability, pricing, and condition, and summarizes what it learns. Shows a dashboard — You get a ranked shortlist with key takeaways (availability, best quoted price) so you can act. Test drive bookings — When you confirm a vehicle, the AI can place a follow-up call to the dealer to schedule a test drive. We use Foxit PDF Services to generate recommendation reports you can download and share. How we built it Frontend: React (Vite) + TypeScript for the chat UI, preferences form, search results, and call-progress screen. Real-time updates use Server-Sent Events (SSE). Backend: Python + FastAPI, with MongoDB (Beanie) for sessions and search history. AI & voice: OpenAI GPT-4 — Conversational agent with structured output, real-time transcript summarization, and multi-factor ranking Twilio — Programmable voice (PSTN) for outbound calls and Media Streams for real-time audio Deepgram — Voice agent for real-time, bidirectional conversations with dealership staff via streaming speech-to-text (STT) and text-to-speech (TTS) Data & APIs: MarketCheck — Aggregated vehicle listings and market data Foxit PDF Services — On-demand document generation for recommendation reports Deployment: Hosted on Akamai-connected Linode for low-latency, reliable access. Voice pipeline: Twilio places the call → streams audio to our backend → we bridge it to Deepgram via WebSocket → Deepgram does STT → LLM → TTS and streams audio back through Twilio to the dealer Foxit PDF Services We use Foxit’s Document Generation API to produce downloadable PDF reports from dashboard data. Template-based PDF generation — We create a Word template with token placeholders for dynamic content (report summary, dealer call results, vehicle tables). Foxit merges our JSON data into the template and returns a ready-to-send PDF. Vehicle Research Reports — Each export includes a summary of contacted vs. shortlisted vehicles, a Dealer Call Results table (availability, verdict, notes from dealer calls), and an All Vehicles table with price, mileage, and dealer info. On-demand exports — When a user exports from the dashboard, we send the current session’s data and template to Foxit in a single request and stream the resulting PDF back for download. Akamai (via Linode) The app is deployed on Linode infrastructure connected to Akamai’s global network. Low-latency access — Requests are routed through Akamai’s edge network, so users get faster responses regardless of where they are. Reliable hosting — Docker Compose defines backend and MongoDB services with health checks, resource limits, and restarts, tuned for stable production use on Linode. Simplified deployment — The stack runs as containerized services on Linode, using Akamai-connected connectivity for dependable, scalable hosting. Deepgram Voice Agent We use Deepgram’s Voice Agent API to run real-time, AI-driven calls to dealerships on behalf of buyers. Real-time bidirectional voice — Twilio streams dealer audio to our backend; we forward it to Deepgram over WebSocket. Deepgram performs STT (Nova) and TTS (Aura), and streams synthesized agent speech back through Twilio so the dealer hears a natural conversation. Context-aware conversations — Each call uses an agent prompt tailored to the vehicle (title, price, features) and user context (budget, location, financing interest). The agent asks about availability, condition, pricing, financing, and test drives in a natural, conversational way. Transcript capture and summaries — We record the full conversation (dealer and agent turns), persist it when the call ends, and use it for dashboard notes and follow-up so buyers can review what was discussed. Architecture diagrams The following diagrams are attached as images to the devpost submission: High Level System Architecture Real-Time Voice Pipeline User flow Challenges we ran into Twilio webhooks — Twilio needs a public URL to reach our server; we used ngrok for local dev and configured SERVER_BASE_URL so Twilio could fetch TwiML and connect the Media Stream. Twilio–Deepgram bridge — We had to connect the Twilio Media Stream WebSocket to Deepgram's Voice Agent API and route audio in both directions. Real-time UI updates — We switched from polling to SSE so the frontend could show call progress as calls progressed. Call context — We had to pass the right vehicle context (price, features) into the voice agent prompt so it could ask useful questions and summarize results. Accomplishments that we're proud of Full voice pipeline — AI that actually calls real dealerships and conducts realistic conversations. Cohesive UX — Chat → search → shortlist → call flow in one app. Live call progress — UI shows per-dealer status (dialing, connected, finished). Report generation — Foxit for PDF recommendation reports. Deployable stack — Backend and frontend run on a single Akamai Linode server with Docker. What we learned How to bridge Twilio Media Stream and Deepgram’s voice APIs for real-time, low-latency voice AI. Why a stable public base URL matters for webhooks and how to handle it across dev (ngrok) and production. Why SSE beats polling for live progress and real-time UI updates. How to design prompts that let a voice agent stay on-context and turn open-ended calls into structured insights. What's next for CarDeal Dial - AI that calls dealerships on your behalf SMS outreach — Let the AI text dealers for quotes or scheduling. Broader listing sources — Add more APIs or scraping for dealer inventory. Mobile app — Native app for car shopping on the go. <div