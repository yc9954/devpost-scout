---
slug: "mavn"
url: "https://devpost.com/software/mavn"
title: "MAVN"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 755
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/provenance_signing"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# MAVN

> One who understands: your healthcare, handled

[Devpost](https://devpost.com/software/mavn) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[provenance_signing]] [[voice_speech]]
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[transportation]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]

**stack** elevenlabs, expo.io, fastapi, playwright, python, railway, react-native, tavily-api, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- design
- challenges we ran into
- what we learned
- accomplishments that we're proud of
- what's next for mavn

## Body

Inspiration Finding a doctor shouldn't be harder than the recovery process. Yet for many of us on the team, that's exactly how it felt. Whether it was navigating a new city without knowing which clinics took insurance, putting off a specialist visit because the booking process felt impossibly difficult, or a family member with limited mobility who couldn't easily make phone calls to track down an appointment, the number of obstacles encountered delayed care. We wanted to build the tool we wished existed: one that could handle the entire finding and booking workflow on your behalf, and do it through a voice interface accessible to everyone. What it does Our app is a voice-controlled healthcare assistant that: Finds in-network providers near you based on your specialty, insurance, location, and urgency Automatically books appointments online by navigating clinic websites, filling out contact forms, and submitting booking requests. Supports medicine delivery so users can request medication refills or delivery as part of the same conversation. Works entirely by voice via a natural language ElevenLabs conversational AI agent, making the experience accessible to people with limited mobility, vision impairments, or anyone who struggles to focus for long periods. How we built it The stack is a monorepo with two main components: Backend (FastAPI / Python 3.12) A REST API deployed on Railway that handles provider search (powered by Tavily), ranking, booking detection, and a headless Playwright-based form-filling agent that navigates real clinic websites and submits appointment requests autonomously Mobile app (Expo / React Native): A cross-platform mobile client with onboarding, user profiles (insurance, address, phone), and a voice interface built on the ElevenLabs React Native SDK over WebRTC ElevenLabs Conversational AI: The voice agent collects patient context dynamically (name, insurance, zip code, etc.) and calls our backend webhook tool to trigger full end-to-end outreach Patient profile data (name, insurance, address, phone) is injected as dynamic variables at conversation start so the agent can fill forms and personalize every interaction without the user having to repeat themselves. Design https://docs.google.com/document/d/e/2PACX-1vR_Z5ynQXesOuvCW02BbivkPQVdIutd0gnnMTzn0r9AqPu-EjLv5tM-Z9IsuzkYcrXThBZlHHZjnhSV/pub ^^^ Design Images We used Figma Make to go from idea to interface fast, prompting our way to first-pass layouts for onboarding, the voice interface, and provider results instead of starting from blank artboards. Generating multiple variants let us pick a direction in minutes rather than debating it in the abstract. From there, we refined the screens we liked by hand: tightening spacing, dialing in an accessible color system, and reworking the voice interaction states (idle, listening, speaking, booking) so status was clear without requiring users to look at the screen. AI for speed, human judgment for the details. Challenges we ran into Voice + async booking: The booking process can take some time. Keeping the voice conversation alive and informative while a headless browser works in the background requires careful use of asynchronous execution and pre-tool speech. Accessibility first: Designing the entire experience to work purely by voice, with no required screen interaction, meant rethinking every user flow from the ground up ElevenLabs tool schema: Wiring up the webhook tool to match ElevenLabs' exact UI validation schema (the value_type, dynamic_variable, constant_value per-property format) took several iterations Web form diversity: Every clinic website is different. Some use Calendly, some LeadConnector, some custom Jotforms, some just static HTML. Building a single form-filler that worked across all of them required a layered approach: preflight HTML parsing, known-platform handlers, smart CSS selector scoring, iframe jumping, and fallback chatbot detection. What we learned Headless browser automation at scale is more difficult than we expected. (The web is not a structured API) Voice-controlled UX requires a fundamentally different information architecture than tap/touch design ElevenLabs' dynamic variable system is a powerful primitive for personalizing agent behavior at runtime Healthcare accessibility is both a technical and a human problem, so the best interface is one that gets out of the way entirely Accomplishments that we're proud of End-to-end “voice-booked” flow: went from a spoken request to a real API call that triggers automated outreach/booking attempts. Personalized care context: captured patient profile details once and reused them across the conversation, booking steps (location, insurance, contact info), and medicine delivery. What's next for MAVN Care follow-ups: after booking, guide prep steps (documents, insurance card, pre-visit forms), and automated reminders. Async booking + notifications: run outreach in the background and notify users via SMS/email/push when an appointment is confirmed, needs verification, or requires a phone call. Safety + compliance: add guardrails for medical advice, stronger data handling, and a privacy-first audit trail (plus HIPAA-aware storage paths for data safety). <div