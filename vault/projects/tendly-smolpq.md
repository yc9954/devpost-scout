---
slug: "tendly-smolpq"
url: "https://devpost.com/software/tendly-smolpq"
title: "Tendly"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 1151
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/transcript_audio"
---

# Tendly

> Tendly gives elderly patients one button to speak any need. Claude triages it in real time, caregivers get a live priority feed, and Simular automates the rest.

[Devpost](https://devpost.com/software/tendly-smolpq) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]] [[realtime_stream]] [[voice_speech]]
**domain** [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]] [[medical_record]] [[transcript_audio]]
  <sub>weak: web_dom</sub>

**stack** claude, css, fastapi, html, javascript, next.js, pydantic, python, react, redis, typescript, uvicorn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tendly

## Body

Tendly Tendly patient dashboard. Tendly caretaker dashboard. Inspiration The Silent Crisis in Elder Care Every day, millions of elderly patients in care facilities struggle to communicate even their most basic needs. Call buttons go unanswered. Nurses juggle dozens of patients with no intelligent triage. Families wait days for updates. The tools haven't changed in decades, and the human cost is enormous. A 2023 study found that 28% of adverse care events stem directly from communication failures between patients and caregivers. A Personal Urgency We wanted to build something that actually matters. Elder care sits at the intersection of AI's greatest potential: understanding natural language, acting on it autonomously, and keeping humans in the loop for what matters most. The question we kept asking was simple: what if every patient had an AI that listened instantly, every time? That question became Tendly. What it does Two Interfaces, One Intelligence Layer Tendly is an AI-powered care platform with two complementary interfaces. The patient voice interface is radically simple: one tap, speak any need, hear a spoken confirmation back. No typing, no menus, no complexity. The caregiver dashboard is a real-time, urgency-ranked queue of every patient request across the facility, updating live via WebSocket as new requests come in. Caregivers see what's critical at a glance and can update request status with a single click. AI That Listens, Triages, and Acts Under the hood, every patient utterance flows through a Claude-powered triage pipeline that classifies requests into six categories (from urgent_medical emergencies to general_conversation ) and assigns one of four urgency levels. For digital tasks (play music, look up a recipe, send a message), Tendly generates a TypeScript Simulang script and executes it directly on the desktop via Simular, no caregiver required. Redis stores patient history so every triage decision is enriched with personal context. At day's end, Claude writes a warm family summary: a human-readable digest of the patient's day sent to loved ones. How we built it Architecture $$ \text{Patient} \xrightarrow{\text{voice}} \text{Deepgram STT} \xrightarrow{\text{transcript}} \text{Claude Triage} \xrightarrow{\text{alert}} \text{Caregiver Dashboard} $$ $$ \text{Claude Triage} \xrightarrow{\text{confirmed task}} \text{Simular Automation} \xrightarrow{\text{executed}} \text{Result} $$ The backend is a FastAPI application with a WebSocket endpoint that broadcasts new requests to all connected caregiver dashboards in real time. Every patient utterance hits Deepgram's streaming STT API, producing a transcript in under 300ms. That transcript, enriched with patient context from Redis, is sent to Claude Sonnet with a strict safety system prompt and few-shot examples, returning a structured JSON triage result. Confirmed automation tasks are handed to Simular, which executes TypeScript scripts against the live desktop. Core Tools We Used Deepgram powers the patient voice interface, turning spoken requests into low-latency transcripts so elderly patients can simply speak instead of navigating forms or menus. Redis stores patient context and request history, giving the triage pipeline memory so every decision can account for preferences, prior symptoms, and recent activity. Simular enables desktop automation. When a patient asks for a safe digital task, Tendly generates and runs a TypeScript automation script so the request can be completed without adding work to the caregiver queue. Frontend & Desktop The frontend is a Next.js 14 app packaged as a cross-platform desktop application via Electron . The patient and caregiver views are completely separate routes sharing a single API client. Voice recording uses the Deepgram API with Opus encoding. Challenges we ran into Safety by Design The hardest design challenge wasn't technical, it was ethical. An AI triage system for elderly patients carries real stakes. We spent significant time on the safety system prompt, settling on a core rule: false positives are acceptable; false negatives are not. Any medically ambiguous utterance escalates. The system never suppresses a request, even chit-chat. Getting Claude to reliably return structured JSON and gracefully recover when it didn't required careful prompt engineering and a robust extraction fallback. Real-Time Coordination at the Edges Keeping the caregiver dashboard perfectly in sync across multiple concurrent sessions while new patient requests arrive, get triaged, and trigger Simular automations is a distributed systems problem in miniature. WebSocket reconnection logic, highlight animations for new high-urgency cards, and race conditions between optimistic UI updates and server state all required careful handling. We also discovered that Electron's Accessibility permissions on macOS are silently denied in certain sandbox configurations, which cost us several hours before we identified the cause. Accomplishments that we're proud of A Full End-to-End Flow That Actually Works The complete loop (patient speaks, Deepgram transcribes, Claude triages, caregiver dashboard updates live, Simular executes) runs in under 2 seconds end-to-end. That's not a demo; it's a real working system. We're proud that every layer has a deterministic mock fallback, so the entire experience can be demonstrated without a single API key. A Safety Architecture Worth Trusting We built a system where the AI is genuinely accountable. Every triage decision is logged to Arize with its full reasoning chain. The safety rules are non-negotiable and enforced at the prompt level. Sensitive automations require explicit patient confirmation, spoken aloud and responded to by voice. This isn't AI replacing caregivers. It's AI making caregivers more effective while keeping humans in control of every critical decision. What we learned LLMs as Triage Engines We learned that Claude is remarkably good at medical triage when given the right constraints . The combination of a well-structured system prompt, few-shot examples, and a forced JSON output schema produces consistent, clinically reasonable classifications across a wide range of patient utterances — including ambiguous ones. The key insight was that the system prompt's safety rules function more like invariants than suggestions: Claude honors them reliably when they're stated as non-negotiable. The Compound Value of Memory Redis patient memory changed the character of the product more than any other single feature. When Claude knows that a patient has a history of dizziness, prefers classical music, and usually asks for water in the evenings, every triage decision becomes richer and every caregiver alert more actionable. We learned that personalization at this level doesn't require complex retrieval. A well-structured context string prepended to each prompt is enough to meaningfully shift Claude's outputs. What's next for Tendly Clinical Validation & Compliance The immediate next step is a structured beta with three assisted living facilities, instrumenting Tendly's triage accuracy against caregiver ground-truth labels. From there, the path to production requires HIPAA compliance , audit logging that meets CMS standards, and EHR integration via HL7 FHIR so Tendly's requests and summaries can flow into existing clinical workflows rather than alongside them. Expanding the Intelligence Surface On the product side, we want to add a family mobile app that surfaces daily summaries and allows family members to initiate check-ins. On the AI side, we're exploring multi-turn patient conversations — moving beyond single-request interactions toward a persistent, context-aware companion that can detect longitudinal patterns (declining mood, new pain, changing sleep) and surface them proactively to the care team before they become emergencies. <div