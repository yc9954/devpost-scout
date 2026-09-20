---
slug: "booboo-buddy"
url: "https://devpost.com/software/booboo-buddy"
title: "BooBoo Buddy"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 646
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# BooBoo Buddy

> 🩹 BooBooBuddy: Your Health Companion That Takes Action! Ever been sick and spent hours calling clinics, only to find out they're full? BooBooBuddy takes the wheel booking appointments while you rest!

[Devpost](https://devpost.com/software/booboo-buddy) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[health_clinical]]
**substrate** [[medical_record]] [[structured_db]] [[transcript_audio]]

**stack** google-directions, nextjs, openrouter, react, twilio, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for booboobuddy

## Body

Chat page Sign in page GenAI disclosure Inspiration Healthcare shouldn't require you to be healthy enough to navigate it. We've all been there: sick, exhausted, and stuck making call after call to find a clinic that can see us today. We built BooBooBuddy because we believe AI can take action on your behalf when you need it most. What if your health assistant could actually call the clinic for you? What if it understood not just your symptoms, but your preferences, your history, and your urgency, and then acted? What it does BooBooBuddy is an AI-powered health agent that bridges the gap between symptom assessment and actual care. It: Triages your condition through natural conversation, progressively assessing severity Detects emergencies and immediately advises 911 when needed Finds nearby clinics using Google Places API and your location Calls clinics automatically via Twilio to check walk-in availability or appointment slots Presents time slots when appointments are required, letting you pick what works Books appointments on your behalf with a follow-up call confirming your selected time Understands context—synthesizing your symptoms into clear, medical-appropriate language for the clinic How we built it Frontend: Next.js 14 with React, TypeScript, and Tailwind CSS for a responsive, accessible interface AI/LLM: OpenRouter API (GPT-4o-mini) for intelligent conversation, symptom analysis, and transcript interpretation Voice Input: Web Speech API for hands-free interaction when you're too sick to type Telephony: Twilio for automated outbound calls with recording and transcription Location Services: Google Places API for finding nearby clinics with real-time data State Management: Custom workflow engine managing conversation states from greeting through clinic booking Database: Prisma with SQLite for user profiles and health preferences The architecture follows an agentic pattern—the LLM doesn't just respond, it decides when to trigger tool calls (clinic search, phone calls, bookings) based on conversation context. Challenges we ran into Twilio transcription timing: Transcripts aren't immediately available after a call ends. We built a polling system with callback support to reliably retrieve responses Symptom synthesis: Raw conversation text includes noise ("find clinics near k1j9a1"). We added an LLM preprocessing step to extract only relevant medical symptoms Walk-in vs. appointment detection: Clinics respond differently. We tuned our transcript analysis prompts to accurately distinguish "come on in" from "we need to book you" Time slot extraction: Parsing "we have openings between 2 and 5" into clickable 30-minute slots required careful prompt engineering and fallback logic Voice input edge cases: Handling microphone permissions, browser compatibility, and the "listening" UX state across different devices Accomplishments that we're proud of End-to-end automation: From "my throat hurts" to a confirmed appointment—without the user making a single phone call Intelligent escalation: The system knows when to keep chatting, when to search for clinics, and when to say "call 911 now" Real phone calls: Not simulated. BooBooBuddy actually calls real phone numbers and interprets real human responses Time slot selection UI: A clean grid of available times generated from natural language like "between 2 PM and 5 PM" What we learned Agentic AI is harder than chat: Deciding when to act (not just what to say) requires careful state management. Moreover, working with databases can be tricky, and ensuring context stays relevant for a given user requires understanding how to handle persistence at a system level. Telephony is fallible: Real-world phone systems have holds, voicemails, and unclear responses. Robustness matters more than perfection What's next for BooBooBuddy User health profiles: Remember past conditions, medications, and preferences to personalize recommendations Multi-language support: Serve diverse communities with translated conversations and calls Integration with health records: Pull from Apple Health, Google Fit, or EHR systems for richer context SMS confirmations: Send appointment details to the user's phone after booking Pharmacy integration: Extend the agent to call pharmacies for prescription availability Voice-first mode: Full conversation via speech for completely hands-free operation Dialogue API integration: Connect directly with Dialogue's platform for seamless virtual-to-physical care handoffs <div