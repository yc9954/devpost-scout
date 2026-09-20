---
slug: "careloop-agentverse-care-companion"
url: "https://devpost.com/software/careloop-agentverse-care-companion"
title: "CareLoop Agentverse Care Companion"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 636
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "user/clinician"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# CareLoop Agentverse Care Companion

> CareLoop coordinates prescriptions, appointments, OTC medicine, FET payments, calendars, and caregiver updates through Fetch.ai agents

[Devpost](https://devpost.com/software/careloop-agentverse-care-companion) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[vision_ocr]]
  <sub>weak: deterministic_policy, multi_agent, provenance_signing</sub>
**domain** [[elder_child_care]] [[finance_payments]] [[health_clinical]] [[retail_commerce]]
  <sub>weak: supply_logistics</sub>
**user** [[clinician]] [[patient_family]] [[social_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** agentverse, asi:one, browser-use, fet, fetch.ai, ocr, python, telegram, uagents

## Body

Inspiration Care coordination is still too hard for older adults and caregivers. A simple task like "I have a cough and need help" can turn into five separate workflows: finding a doctor, scheduling the visit, understanding prescriptions, checking medicine options, paying service fees, and keeping family updated. CareLoop was inspired by the idea that an older adult should not need to know which app, pharmacy, doctor, calendar, or agent to use. They should be able to say what is happening in plain English and let a trusted agent system coordinate the next step. What It Does CareLoop is a bottom-up Fetch.ai/uAgents care-coordination system. It includes a main orchestrator plus specialist agents: Agent What It Does careloop-orchestrator Main ASI:One entrypoint, routing, state, timeline careloop-appointment-assistant Paid provider search and booking handoff careloop-doctor-office Agentverse doctor-office booking with Google Calendar careloop-pharmacy-assistant OTC medicine search, price comparison, FET service fee, checkout handoff careloop-prescription-explainer Prescription photo/PDF/text scanning and plain-language explanation careloop-caregiver-notifier Caregiver SMS/email drafts and Gmail sending careloop-triage Intent routing and emergency escalation Users can interact through ASI:One or Telegram. In ASI:One, CareLoop uses native Fetch.ai payment protocol cards for FET service fees. In Telegram, CareLoop demonstrates an OmegaClaw-style external channel with doctor booking, prescription image intake, testnet FET payment commands, Google Calendar, and caregiver email. How We Built It We built CareLoop as a set of Python uAgents and registered them on Agentverse. Each specialist agent is independently runnable and testable, and the orchestrator composes them into a visible care timeline. The system uses: Fetch.ai uAgents for agent runtime and messaging. Agentverse registration for discoverability. ASI:One Chat Protocol for conversational use. uAgents Payment Protocol for FET service-fee cards in ASI:One. Telegram Bot API for the OmegaClaw-style external channel. Google Calendar API for doctor-office booking. Gmail API for caregiver email sending. OCR/PDF parsing for prescription intake. Browser/search adapters and public data sources for pharmacy/appointment handoffs. The hardest part was making the system feel stateful and natural. Older adults do not speak in perfect API commands. CareLoop uses ASI:One/LLM classification where useful, but keeps deterministic flows for payment, safety, and booking actions. Challenges Getting native ASI:One FET Pay/Reject cards working required using the payment protocol exactly, not just showing payment text. Telegram does not render ASI:One payment cards, so we built a separate testnet payment flow using /pay and /paid <tx-hash> . Prescription intake had to be safe: the agent must explain readable labels but refuse to guess from unclear images. Real provider and pharmacy systems do not always expose open booking/status APIs, so CareLoop clearly separates real calendar booking, real/public handoff links, and mocked/fallback data. Statefulness mattered a lot. Follow-up questions like "which one is closest?" or "is there any order?" need to use the prior result, not restart the chat. What We Learned We learned how to build a practical multi-agent system around Fetch.ai primitives: discoverability through Agentverse, conversational UX through ASI:One, and economic actions through FET payments. We also learned that healthcare agents need careful boundaries: logistics and explanation are useful, but diagnosis and medication changes must stay with clinicians and pharmacists. What Is Next Add real pharmacy partner integrations for prescription readiness. Add more provider booking APIs for confirmed external bookings. Add a Telegram Web App wallet checkout for a more polished FET payment UX. Add caregiver permission controls and audit logs. Add HIPAA-grade storage/security hardening. Expand reminder/adherence workflows. ASI:One chat link: https://asi1.ai/shared-chat/1848a0f6-b625-43d6-bab8-8f2061de1f6b agents: Main: @careloop-orchestrator Others: careloop-orchestrator — main ASI:One coordinator and demo entrypoint careloop-pharmacy-assistant — OTC medicine search, price comparison, FET payment, checkout handoff careloop-prescription-explainer — prescription/PDF/photo explanation support careloop-appointment-assistant — live provider and appointment search with FET payment careloop-doctor-office — Agentverse doctor office that can book a demo appointment + Google Calendar invite careloop-caregiver-notifier — caregiver SMS/email-style update writer careloop-triage — emergency-safe router to the right specialist careloop-adherence — medication reminder and missed-dose plan agent <div