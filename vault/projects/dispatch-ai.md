---
slug: "dispatch-ai"
url: "https://devpost.com/software/dispatch-ai"
title: "Dispatch AI"
hackathon: "UC Berkeley AI Hackathon 2024"
organization: "Cal Hacks"
winner: true
words: 1014
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "user/government_staff"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Dispatch AI

> An empathic agent eliminating 911 wait times during critical emergencies.

[Devpost](https://devpost.com/software/dispatch-ai) · hackathon [[UC Berkeley AI Hackathon 2024]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[civic_government]] [[disaster_emergency]] [[health_clinical]]
**user** [[government_staff]] [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[transcript_audio]]
  <sub>weak: financial_record</sub>

**stack** fastapi, framer-motion, hume, intel, next.js, react, retell, shadcn, tailwindcss, twilio

## How they structured the write-up

- 🚨 inspiration
- 🎯 what it does
- 🛠️ how we built it
- 🧗 challenges we ran into
- 🏆 accomplishments that we're proud of
- 💡 what we learned
- 🚀 what's next for dispatchai

## Body

Closing Ceremony Thumbnail dark mode Systems Design Architecture landing page problem statement Thumbnail light mode user flow DispatchAI An empathetic AI dispatcher for 911: real-time transcripts, emotion-aware triage, and a live operator cockpit. 36 hr build time $64k prizes won 3× awards won 4 builders 518 open transcripts 1st of 293 at Cal Hacks AI 🚨 Inspiration A major earthquake hits. Thousands call 911 at once. A handful of operators face every line ringing, every second counting, and not enough people to answer. This is not hypothetical. US 911 systems lose roughly 80% of their staff within a year, and centers run about 30% understaffed. When seconds mean lives, that shortage becomes a survival problem. We built DispatchAI to take the parts a human should not have to do alone at 3 a.m.: listen calmly to a panicking caller, type the address, score the severity, and hand the dispatcher a tight, factual brief. 🎯 What it does DispatchAI is a 911 dispatcher copilot . A caller phones a Twilio number, a Retell voice agent (running our custom LLM over a websocket) handles the conversation, a fine-tuned Mistral-7B drafts the incident report, and Hume EVI tracks the caller's emotional state. A Next.js operator cockpit shows the live transcript, a severity-coded map pin, the AI summary, and Street View. A human dispatcher is always in the loop on the actual response. 📞 Real-time call handling Twilio to Retell websocket to a custom LLM at FastAPI. Sub-second response latency on the conversational loop. 💛 Empathy as a first-class signal Hume EVI emotion telemetry feeds the LLM context, so wording calibrates to the caller's distress, not just their words. 🧠 AI-assisted, human-dispatched A fine-tuned Mistral-7B on Intel Dev Cloud drafts severity, title, summary, and recommendation. The dispatcher accepts, edits, or rejects. The AI never closes the loop. 🗺️ Operator cockpit Severity-coded incident queue, a synced map with pins, the live transcript, a caller emotion gauge, and pre-baked Google Street View. How it changes the call center Without DispatchAI With DispatchAI Calls answered first-come, first-served Calls ranked by severity, most critical first Operator types the address under pressure Location, time, and emotion pulled from the live call Dispatcher decides with no support AI drafts a brief and a recommendation to confirm Overloaded lines go unanswered Every call gets triaged so none falls through AI black box you cannot trust Assist-only: the human accepts, edits, or rejects 🛠️ How we built it The caller reaches Twilio ; Retell runs the voice agent over a websocket against the FastAPI orchestrator. FastAPI streams audio to Hume EVI for emotion, prompts the Mistral-7B LoRA on Intel Dev Cloud (optimized with IPEX-LLM), geocodes the incident with Google Maps + Street View , and pushes everything to the Next.js operator cockpit on a short polling loop. A human dispatcher remains the final authority on dispatch. End-to-end call flow: Retell connects to the custom LLM websocket for the call. The backend creates a Call record and an empty analytics row, then identifies the registered user. Retell streams transcript updates over the websocket. The backend replies to the caller immediately, then runs analytics in the background. Analytics fills in severity, title, summary, recommendation, location, latitude, longitude, and Street View. The frontend polls the calls API and reflects the active call on the dashboard map and detail panels. The Retell webhook handles lifecycle events (especially call ended) as a backup source of truth. Layer Tools Telephony Twilio (inbound PSTN) · Retell (voice agent + websocket) Inference Fine-tuned Mistral 7B (LoRA) on Intel Dev Cloud with IPEX-LLM Emotion Hume EVI streaming emotion telemetry Orchestrator FastAPI + Prisma (Python) + PostgreSQL Frontend Next.js 16 · TypeScript · TailwindCSS · shadcn/ui · Framer Motion · MapTiler / Leaflet Auth Clerk with phone-based dispatcher routing Maps Google Maps API + Street View Retrieval / search LlamaIndex · You.com Hosting Backend on Google Cloud Run · frontend on Vercel 🧗 Challenges we ran into Building the dataset. There is no off-the-shelf 911 corpus, so we curated 518 dispatcher transcripts ourselves to fine-tune on. Stitching many services into one live loop. Twilio, Retell, Hume, the maps APIs, and the model all had to cooperate in real time on a single call. Teaching the model the domain. Fine-tuning Mistral-7B to score severity and write a clean brief took careful iteration and evaluation. Empathy without latency. Responses had to feel human without slowing the dispatcher down, which is where Intel IPEX-LLM mattered. 🏆 Accomplishments that we're proud of Won the Grand Prize at the UC Berkeley AI Hackathon 2024 , first of 293 submissions, plus the AI For Good and Best Use of Intel AI awards. The Grand Prize included a $25k Berkeley SkyDeck Fund investment and a Golden Ticket to SkyDeck Pad-13. Fine-tuned a Mistral-7B LoRA for emergency response and open-sourced both the model and the dataset on Hugging Face. Built a full live call loop (telephony to emotion to LLM to cockpit) in 36 hours with 4 people. Cut model inference time dramatically using Intel's IPEX-LLM optimizations. Metric Before (baseline) With Intel IPEX-LLM Improvement Model inference time 2 min 53 sec under 10 sec ~80% faster Usable in a live call? No, too slow Yes, real time Unblocked Awards Award Sponsor / Track Grand Prize UC Berkeley AI Hackathon 2024 · $25k Berkeley SkyDeck Fund investment + Golden Ticket to SkyDeck Pad-13 AI For Good Academic Innovation Catalyst (AIC) Best Use of Intel AI Intel 💡 What we learned How to stitch many independent realtime services into one coherent system under a deadline. How much AI can augment, rather than replace, a critical public service when a human stays the final authority. How a small, uneven dataset (518 transcripts) limits a model, and what a real deployment would need: demographic-stratified evals across accents, dialects, and forms of distress. 🚀 What's next for DispatchAI Expand the dataset with more diverse, stratified emergency scenarios. Partner with local PSAPs for real-world testing, with NENA / CJIS / SOC 2 alignment in mind. Integrate with legacy CAD and i3 NG911 systems for a credible path to deployment. <div