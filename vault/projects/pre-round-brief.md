---
slug: "pre-round-brief"
url: "https://devpost.com/software/pre-round-brief"
title: "Pre-Round Brief"
hackathon: "Agents Assemble - The Healthcare AI Endgame"
organization: "Prompt Opinion (Darena Health)"
winner: true
words: 723
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/provenance_signing"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Pre-Round Brief

> An AI chief-of-staff for hospital physicians, a proactive PromptOpinion agent that delivers a prioritized morning briefing of every patient on the doctor's panel, before the commute is over.

[Devpost](https://devpost.com/software/pre-round-brief) · hackathon [[Agents Assemble - The Healthcare AI Endgame]]

## Facets

**mechanism** [[benchmark_measured]] [[provenance_signing]]
**domain** [[health_clinical]] [[housing_homeless]] [[transportation]]
**user** [[clinician]] [[patient_family]]
**substrate** [[geospatial]] [[web_dom]]

**stack** a2a-protocol-v1, better-sqlite3, cloudflared, croner, docker, elevenlabs-conversational-ai, express.js, fhir-r4, node.js, openai, railway, resend

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments
- what we learned
- system architecture
- what's next

## Body

Architecture What it does A doctor adds Pre-Round Brief to her PromptOpinion workspace and configures it in plain English: "Brief me at 7 AM on Mondays and Wednesdays, and at 9 PM on Fridays, Europe/Rome time. Send to dr.lupo@example.com . Prioritize patients with new acute events overnight, and always flag potential drug-allergy interactions." From that moment on, while she sleeps, an autonomous scheduler wakes up at each configured slot, reads the workspace's FHIR data, builds a clinically-prioritized brief, and emails it before her shift. The email contains both a written brief and a one-tap link that opens a two-way voice conversation with the agent, she can listen to the brief on the commute, interrupt, and ask follow-up questions about any patient ( "What's Maria's lactate trend?" ), answered live from her real FHIR data. The brief adapts to her stated preferences (style, priority, tone) without ever suppressing clinically critical findings, thanks to a safety override clause baked into the LLM prompt. How we built it Protocols & platform Built as an A2A 1.0 external agent on PromptOpinion. Agent card declares the FHIR-context extension with SMART scopes ( patient/*.rs ) and offline_access All Po → Agent calls authenticated with a signed JWT (RS256) verified against PromptOpinion's JWKS endpoint via jose Multi-tenant identity derived from the verified JWT ( sub , po_ws_id , po_a2a_id ) Data & autonomy FHIR client reads Patient , Encounter , Observation , Condition , MedicationRequest , AllergyIntolerance , DiagnosticReport from Po's workspace-scoped FHIR R4 server offline_access refresh-token flow mints fresh access tokens overnight — the autonomous core. Rotated on every refresh Croner-based scheduler runs every minute, evaluates each doctor's multi-slot schedule against their local timezone, fires per-slot with idempotency tracking Brain & voice Brief composition: GPT-4o with JSON-schema structured outputs, clinical priority heuristics, doctor-preferences injection with safety override Voice script: separate GPT-4o pass humanizes the structured brief into conversational clinical prose Voice channel: ElevenLabs Conversational AI (Gemini 2.5 Flash backend) with system_prompt + first_message overrides per session Email delivery: Resend with HTML brief layout + talk-page link Infrastructure Node.js + Express, modular src/ layout (routes, handlers, libs, jobs, db) SQLite ( better-sqlite3 , WAL mode) for prefs, FHIR connections, talk sessions Dockerized, deployed on Railway with persistent volume for the SQLite file GitHub repo with gh -managed credentials Challenges we ran into Reverse-engineering the A2A 1.0 Task response shape , Po uses gRPC-style enums ( TASK_STATE_COMPLETED , ROLE_AGENT ) and wraps the result in { task: ... } . The spec wasn't fully searchable; figured it out through iterative error messages. PromptOpinion's offline-access capability didn't exist when I started building. I asked for it on the Devpost forum, the team shipped it days later, which let the autonomous part of this project exist. Accomplishments A genuinely proactive agent on PromptOpinion, most submissions are chat-driven; this one delivers before being asked Two-way voice Q&A with full FHIR context as overrides, the doctor can interrupt the brief, ask anything, get a grounded answer Per-doctor preferences (style, priority, tone) shape the brief without compromising clinical safety Multi-slot scheduling with per-slot fire tracking and IANA timezone support, handles real shift patterns Cryptographic JWT verification against Po's JWKS, proper identity, not trust-by-URL What we learned The A2A 1.0 protocol, the SMART-on-FHIR scope model, and how PromptOpinion's FHIR context flows through it How to design overrides for ElevenLabs Conversational AI so the same agent serves thousands of contextually-different conversations The non-obvious cost of running clinically-meaningful LLM prompts under voice latency budgets — and the architectural tricks (compact reference context, eager turn-taking, low-latency models) that make it work System architecture What's next Memory of past briefs and conversations, the agent currently treats each day independently. With prior context it could say "the same patient you flagged yesterday is still…" Outbound phone delivery via Twilio + ElevenLabs Twilio bridge, for doctors who prefer a ringing phone over a tap-to-talk CareTeam-aware patient filtering , surface only the patients assigned to this doctor, not the whole workspace HIPAA-compliant production deployment , ElevenLabs BAA via Enterprise tier, refresh-token encryption at rest, audit logging Native PromptOpinion integration , this concept (async + email + voice) might belong inside the platform as a first-class agent capability ## Links 📦 Source : github.com/domingosl/pre-round-brief 🛒 PromptOpinion Marketplace : https://app.promptopinion.ai/marketplace/agent/019e209f-280e-77a0-9a31-6c35f377de71 🎬 Demo video : https://youtu.be/XkCpb6Kpzfo 💬 The forum post that made this possible : https://agents-assemble.devpost.com/forum_topics/43458-can-data-inside-prompt-opinion-be-retrived-externally-in-async-mode <div