---
slug: "healthplan-ai"
url: "https://devpost.com/software/healthplan-ai"
title: "HealthPlan AI"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 416
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/finance_payments"
---

# HealthPlan AI

> A web app with an AI voice agent that helps users understand and find the right health insurance plan for them, using real-time data from the federal marketplace.

[Devpost](https://devpost.com/software/healthplan-ai) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[civic_government]] [[finance_payments]]

**stack** bolt.new, cms-api, elevenlabs, netlify, react, supabase, tailwind, vite

## How they structured the write-up

- inspiration
- what i built
- how i built it
- what i learned
- challenges
- watch the demo

## Body

HealthPlan AI – the AI Health Insurance Marketplace Assistant Inspiration Dealing with health insurance is one of the most frustrating parts of American life - and the challenges can start the moment you try to sign up. Inspired by my boyfriend’s negative experience trying to find a decent plan, I built this app to offer a better experience. The AI agent helps you explore real options, explains confusing terms, and doesn’t try to sell you anything. What I Built This is a simple web app (React Vite) with a voice assistant that helps people look through real federal marketplace health insurance data and plans. It currently only works for 1-person households. The app uses: ElevenLabs for the AI voice assistant Supabase Edge Functions to fetch and filter live plan data from the CMS federal marketplace A UI that updates alongside what the agent is saying Bolt.new to build the whole thing without needing to set up a local dev environment Netlify to deploy it with no hassle How I Built It Built the whole stack in Bolt.new – super fast, runs in the browser, no setup Used Supabase Edge Functions to handle the API calls to CMS Created a Conversational AI Agent in ElevenLabs with knowledge and clear instructions on how the complicated conversation flow is supposed to happen Wrote some tools (webhooks + client-side functions) so the AI agent can update the page and trigger backend logic Frontend: React + Tailwind Deployed to Netlify – no issues, dev and prod behave the same What I Learned How to connect a real-time voice agent to live government data using serverless functions Designing a user experience that doesn’t add more stress to an already stressful topic like healthcare Building Supabase Edge Functions Making custom tools for the AI agent to use, including webhook tools and client-side tools that manipulate the page in response to the conversation Bolt is amazing for full-stack prototyping! I like that it's all in the browser, which means no setup problems or dealing with dependencies or package installs Super easy deployment with Netlify — everything works exactly like it does in development without surprises (unlike for me often with, say, Vercel) Challenges The CMS API is complex Handling eligibility rules and edge cases across states (e.g., Medicaid expansion gaps) Ensuring the voice assistant could both speak clearly and show relevant content on-screen Keeping the app lightweight while integrating multiple services (Supabase, ElevenLabs, etc.) Watch the Demo Watch the quick walkthrough here: https://www.youtube.com/watch?v=H17kkGFKVtI <div