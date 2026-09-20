---
slug: "first30-ai"
url: "https://devpost.com/software/first30-ai"
title: "First30.ai"
hackathon: "StartupMed"
organization: "Students"
winner: true
words: 920
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/clinician"
  - "user/developer"
  - "user/frontline_worker"
  - "user/general_public"
  - "user/patient_family"
---

# First30.ai

> Web app that tells you exactly what to do when someone needs emergency help so you can act accordingly where every minute matters the most.

[Devpost](https://devpost.com/software/first30-ai) · hackathon [[StartupMed]]

## Facets

**domain** [[civic_government]] [[disaster_emergency]] [[elder_child_care]] [[finance_payments]] [[health_clinical]] [[labor_employment]]
**user** [[clinician]] [[developer]] [[frontline_worker]] [[general_public]] [[patient_family]]

**stack** react, supabase, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- target group
- value proposition & usp
- user feedback
- business model
- implementation & feasibility
- data requirements + gdpr/dsgvo compliance
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for first30.ai

## Body

Inspiration Most people are not prepared for critical situation that take place all of a sudden, and in the moment, even simple decisions feel hard. We noticed the same pattern: people panic, freeze, or start searching random things over internet while precious minutes pass. We built First30.ai to be the calm guide in that gap, the first 30 minutes before professional help takes over. The idea is not to replace doctors or paramedics. It is to help a normal person do the next right thing without feeling lost. What it does First30.ai is a voice guided emergency helper for everyday people. You choose what situation is happening, and it walks you through clear steps one at a time It speaks the steps out loud, so you can keep your hands and eyes on the situation It can show nearby hospitals, pharmacies, and emergency services based on your location At the end, it generates a short summary you can share with responders, like what you observed and what you already did Target Group Primary: General public with no medical training (bystanders, family members) Secondary: First responders, emergency dispatchers, community health workers Tertiary: Healthcare organizations, insurance companies, public health agencies Features & Functions 15+ emergency category flows with step-by-step guidance ElevenLabs-powered voice narration in 5 languages Location-based nearby hospital/pharmacy/emergency services finder Emergency summary generator for handoff to responders Dispatcher dashboard prototype for structured triage Accessibility mode with large text and auto-voice Value Proposition & USP Traditional First Aid First30.ai Requires training or prior knowledge Built for zero training Panic often leads to freezing Calm, one step at a time guidance Language barriers limit usability Voice guidance in 5 languages Users waste time searching what to do Nearby help is located automatically No clear handoff to responders Generates a quick summary for responders User Feedback "I showed this to my elderly mother. She said for the first time she feels like she could actually help in an emergency instead of just panicking." — Beta Tester, Munich "The voice feature is a game-changer. I don't have to look at my phone while doing CPR." — Nurse, Hamburg "Finally something that works in Hindi. My parents can't read English emergency guides." — Software Engineer, Delhi Business Model Revenue Stream Description B2B Licensing White label for hospitals, insurance companies, and corporate wellness programs Freemium Core features free; premium voices, offline packs, and family accounts Public Health Grants Government and NGO funding for public deployment API Access Emergency guidance API for third party apps and platforms Training Partnerships Integration with first aid certification and training programs Implementation & Feasibility Current Status: Working prototype with all core features functional Next Steps: Medical content review by certified professionals (2 weeks) User testing with 50+ participants (1 month) Offline mode implementation (2 months) Pilot with 2–3 healthcare partners (3 months) Public beta launch (4 months) Data Requirements + GDPR/DSGVO Compliance Data Handling Data Type Collection Storage Purpose Location On request Not stored Nearby services lookup Language preference Local setting Browser only UI personalization Emergency session Temporary RAM only Summary generation GDPR Compliance ✅ No personal data collection ✅ No user accounts required ✅ No cookies beyond essential functionality ✅ Processing happens client side or in ephemeral edge functions ✅ Clear privacy policy and consent dialogs How we built it We built the app with React, and TypeScript so it is fast and easy to maintain. The emergency guidance is data driven . Each emergency category is a structured flow made of steps and safety notes. The UI reads that data and renders the experience, which makes it easy to add new categories without rewriting the app. For voice, we use ElevenLabs . To keep the API key secure, the app calls a Supabase Edge Function . The browser sends only the text, the function calls ElevenLabs using the secret key, and the audio is returned to the app. For nearby help, we use location only when the user asks for it, then show nearby services and quick directions. Challenges we ran into Designing and choosing the features were the challenge that we faced. Too many options can make people confusing. Location features needed to work even when permissions are denied or the network is unstable. Writing step by step flows that are clear and safe across many emergency types was harder than expected. Making everything accessible without making the UI feel heavy or cluttered. Accomplishments that we're proud of A working prototype with 15+ emergency flows that stays consistent and easy to follow Voice guidance that users can follow without constantly looking at the screen A clean emergency summary that supports better handoff to responders A scalable design where adding a new emergency is mostly adding data, not building new screens A privacy first approach with no accounts and minimal data handling What we learned In emergencies, clarity beats features. One good next step is better than a long guide. Voice is not just a nice add on, it changes how usable the app is under stress. Data driven design makes the project easier to grow and maintain. Privacy and security decisions affect trust, so we treated them as core requirements. What's next for First30.ai Have medical professionals review and refine the emergency content Run user testing with 50+ people and improve the flows based on real behavior Add offline support for critical flows and voice packs Expand the dispatcher view into a stronger triage and handoff tool Polish consent and privacy UX for a production ready public beta <div