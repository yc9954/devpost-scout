---
slug: "motivio"
url: "https://devpost.com/software/motivio"
title: "Motivio"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 539
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/voice_speech"
---

# Motivio

> Motivio lets you enter your personal goals and receive personalized daily motivation to keep you focused and moving forward.

[Devpost](https://devpost.com/software/motivio) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[voice_speech]]

**stack** expo.io, firebase-authentication, firebase-firestore, firebase-functions, react-native, typescript

## How they structured the write-up

- 🚀 inspiration
- 🔎 what it does
- 🛠️ how i built it
- ⚡ challenges
- 🏆 accomplishments
- 📚 what i learned
- ✨ what's next for motivio

## Body

🚀 Inspiration Most motivation apps give generic quotes that feel good for five seconds and then get ignored. I built Motivio to be a lightweight AI coach that learns each user's goal and coaching style, then nudges them toward real action. Instead of passive inspiration, every interaction is designed around micro-steps and immediate reflection. 🔎 What It Does Motivio is a React Native app that delivers personalized daily motivation based on each user's progress. Core Features: Actionable AI Content: Every generated quote includes a micro-step and reflection question, so users can act right away. Adaptive Coaching: Daily check-ins drive behavior-based coaching. The AI intelligently switches between three modes: reinforce , accountability , and reshape . Smart Scheduling: Quotes are sent at each user's local preferred time via an hourly background dispatcher. Offline-First UX: Users can view history and use the app offline, with a local SQLite cache that syncs to the cloud in the background. 🛠️ How I Built It This project uses a mobile-first stack with a cloud AI backend: Frontend: React Native + Expo, TypeScript, and Jotai state management. Backend: Firebase Cloud Functions (v2) for scheduled quote generation, adaptive logic, goal validation, and safety checks. AI Engine: Amazon Bedrock (Nova Lite) for structured JSON generation and goal evaluation. The same model also screens new goals for safety. Data Layer: Firestore for cloud profiles/history + Expo SQLite for on-device persistence. ⚡ Challenges AI Quality Control: To prevent repetitive outputs, the backend loads recent quote history, runs similarity checks, and retries generation when needed: similarity > threshold => retry generation (max 3 attempts) Goal Safety: The same model is used for both goal quality checks and safety screening to catch harmful or unsafe intent at goal creation. 🏆 Accomplishments Adaptive Behavior State: A trigger-based system ( checkinWritten ) updates agent state from real-world user consistency. Timezone-aware Dispatcher: scheduledQuoteGeneration reliably finds users whose local time matches their notification hour, worldwide. Secure AI Integration: Transitioned from client-only logic to a full server-side AI pipeline via Bedrock. 📚 What I Learned This project has been a major bridge in my development journey, especially with Amazon services. As this was my first time using any Amazon service for personal use, I gained significant experience with: Amazon Console & Permissions: Learning to navigate and manage the console, set service permissions, and handle credentials securely. Amazon Bedrock: Developing a deep understanding of Amazon Bedrock, leveraging the Amazon Nova Lite ( amazon.nova-lite-v1:0 ) model for Motivio. ✨ What's Next for Motivio MVP Deployment & Feedback I plan to deploy the MVP and gather real-world user feedback. This will help guide improvements and refinements based on actual usage. Improved Quote Generation I'll keep refining model output. Adaptive modes ( reinforce , accountability , reshape ) will provide deeper, more relevant insights as the user progresses. Smart Notifications To make notifications "smart", I plan to use Amazon Nova Lite to reason about each user's specific goal. The model will determine optimal content and timing, rather than relying on a fixed user setting. Voice Motivation with Amazon Polly I aim to integrate Amazon Polly as a Text-to-Speech (TTS) feature. Motivation via voice is often more impactful than text, so users will be able to hear their daily quotes. <div