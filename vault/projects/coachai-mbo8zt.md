---
slug: "coachai-mbo8zt"
url: "https://devpost.com/software/coachai-mbo8zt"
title: "CoachAI"
hackathon: "RevenueCat Shipyard: Creator Contest "
organization: "RevenueCat"
winner: true
words: 268
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "substrate/transcript_audio"
---

# CoachAI

> Your personal Board of Directors — AI coaches in your pocket, available 24/7

[Devpost](https://devpost.com/software/coachai-mbo8zt) · hackathon [[RevenueCat Shipyard- Creator Contest]]

## Facets

**mechanism** [[retrieval_grounding]]
**substrate** [[transcript_audio]]

**stack** expo.io, react-native, revenuecat

## How they structured the write-up

- the idea
- what it does
- how i built it
- what's next

## Body

CoachAI The Idea I've had this idea sitting in my notes for months - a personal board of advisors in your pocket. Alex Hormozi telling you to fix your offer. James Clear nudging you about your habits. Then I read Simon's brief - "Minimalist AI coaching in your pocket" — and I was like, this is a sign. Time to ship. What It Does CoachAI gives you a Board of Advisors. AI coaches modeled after top thinkers, available 24/7 in a chat interface that feels like iMessage. Pick your focus area, get a personalized advisory board, start chatting. 3 taps to your first coaching conversation. Here's the thing: coaches don't wait for you. They reach out via push notifications, follow up on previous conversations, keep you accountable. Real coaching is proactive, not reactive. You can also create your own AI coach and share it publicly. This opens the door to a creator marketplace. How I Built It React Native (Expo), LangGraph for AI agent orchestration, Claude as the LLM, Supabase for backend, RevenueCat for subscriptions, PostHog for analytics. Each coach has a crafted system prompt defining personality, methodology and values. LangGraph maintains state across sessions. Supabase Edge Functions handle scheduled proactive check-ins delivered via Expo Push Notifications. Monetization is live: $24.95/year or $7.95/week with a 3-day free trial. What's Next RAG pipeline to train coaches on actual published content (books, transcripts, videos). Premium Coach Marketplace with creator revenue sharing. Voice messages. Notion integration. Android. I'm running a public "10 Apps to $10K MRR" challenge and CoachAI is a centerpiece. Back to the grind. Back to the grind. <div