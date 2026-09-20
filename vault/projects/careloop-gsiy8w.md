---
slug: "careloop-gsiy8w"
url: "https://devpost.com/software/careloop-gsiy8w"
title: "CareLoop"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 255
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/geospatial"
---

# CareLoop

> CareLoop is a voice-first healthcare concierge that triages urgency, finds nearby providers, estimates cost, and helps book care from one calm conversation.

[Devpost](https://devpost.com/software/careloop-gsiy8w) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[multi_agent]]
  <sub>weak: realtime_stream</sub>
**domain** [[elder_child_care]] [[finance_payments]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[geospatial]]
  <sub>weak: web_dom</sub>

**stack** agentverse, and, asi:one, cms-nppes-api, css, deepgram, fastapi, fetch.ai-uagents, html, javascript, openai-compatible-api-client, pydantic, python, python-dotenv

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for careloop

## Body

Inspiration CareLoop was inspired by how stressful healthcare navigation can be. Even when someone knows they need care, they still have to figure out urgency, insurance, cost, providers, and booking, often while anxious or helping a loved one. What it does CareLoop lets users describe a health concern by voice or text. It triages urgency, routes emergencies to 911, finds nearby providers, estimates out-of-pocket cost, and helps guide appointment booking in one conversation. How we built it We built CareLoop with Fetch.ai uAgents, ASI:One, Deepgram voice, FastAPI, Redis, Stripe, and CMS NPPES provider data. A main orchestrator agent coordinates specialist agents for triage, provider search, cost estimation, scheduling, and payment. Challenges we ran into The hardest part was making many moving pieces feel simple: voice input, AI reasoning, agent messaging, provider data, payments, and booking. We also had to build strong safety guardrails so emergency symptoms are handled immediately. Accomplishments that we're proud of We are proud that CareLoop feels like a real healthcare access workflow, not just a chatbot. It combines voice, agents, real provider data, cost estimates, booking flow, fallback logic, and emergency routing into one usable demo. What we learned We learned that healthcare AI needs structure as much as intelligence. Clear agent roles, state management, safety rules, and honest limitations are what make the experience trustworthy. What's next for CareLoop Next, we would integrate live insurance eligibility, real appointment availability, provider booking APIs, multilingual caregiver workflows, and stronger clinical review so CareLoop can move from demo to dependable care navigation. <div