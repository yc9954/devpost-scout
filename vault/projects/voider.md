---
slug: "voider"
url: "https://devpost.com/software/voider"
title: "Voider"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 537
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "user/educator_student"
  - "substrate/financial_record"
---

# Voider

> Voider is a voice-first shopping brain that orchestrates cross-platform price comparisons and secure, agentic payments to make buying as effortless as setting a timer.

[Devpost](https://devpost.com/software/voider) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[education]] [[finance_payments]] [[immigration_refugee]] [[labor_employment]] [[retail_commerce]]
**user** [[educator_student]]
**substrate** [[financial_record]]

**stack** claude, elastic, fetch.ai, langchain, mcp, nextjs, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for voider

## Body

Inspiration Ten years ago, setting a timer on an iPhone required unlocking the device, finding the Clock app, and manually scrolling through wheels of numbers. Today, that feels like ancient history - we just ask Siri. We believe commerce is currently stuck in that "manual" phase. Shopping today still requires endless scrolling, multi-step checkouts, and constant context-switching for routine purchases that shouldn't require that much cognitive load. We built Voider to bridge this gap, moving retail away from tedious manual labor toward an instant, zero-friction experience. Our goal is to make "buying" as effortless as "asking." What it does Voider is a universal, voice-first shopping agent that eliminates the "app-hopping" tax. Instead of checking three different apps to find the best delivery fee, you just speak. Voider searches DoorDash, Walmart, and Amazon simultaneously, identifies the lowest price, and completes the transaction autonomously. The app operates in two distinct modes: Direct Orders: "Get me a 12-pack of Red Bull."* The agent benchmarks prices across all platforms, selects the cheapest total (including fees), and executes the payment via Visa instantly. Smart Recommendations:"I’m hungry, I'm in Palo Alto-find me something." Leveraging Elasticsearch, Voider analyzes your location, order history, and dietary preferences to suggest personalized dining options with real-time price comparisons. The "Set and Forget" Layer Voider doesn't just buy; it manages. It remembers your favorites, understands "the usual," and operates within user-defined budget guardrails to ensure the agent never spends more than you’ve authorized. How we built it Voice: ElevenLabs Conversational AI (WebRTC) for low-latency, real-time speech. Brain: Claude 3.5 Sonnet orchestrates tool selection and complex reasoning. Commerce: Pluggable MCP architecture-DoorDash and Uber Eats are queried in parallel. Data: Bright Data scrapes live prices, indexed in Elasticsearch with Jina embeddings. Memory: Elasticsearch stores preferences and order history for hyper-personalized recommendations. Payments: Visa Agent Payment Protocol with tokenized credentials and strict budget limits. Agent Network: Fetch.ai uAgents for ASI:One discovery and payment protocol ($1 USDC/order). Frontend: Next.js 16 on Vercel with Generative UI product cards. Challenges we ran into Reducing the latency of voice models was our biggest hurdle; achieving a "human" response time requires intense optimization of the inference pipeline. We also focused heavily on the UX of "eyes-free" shopping. Ensuring the agent could accurately filter through hundreds of results to find the one correct item without a visual confirmation required fine-tuning our ranking logic and tool-calling accuracy. Accomplishments that we're proud of Despite starting later than planned, we are incredibly proud of the end-to-end integration we achieved. Moving from a voice command to a verified, tokenized Visa payment across multiple third-party platforms in under 10 seconds was a massive technical win for us. What we learned We dove deep into the world of AI agents, from mastering multi-turn orchestration to implementing the Fetch.ai uAgent protocol. We also learned the intricacies of real-time data scraping and how to handle structured data in a high-concurrency environment. What's next for Voider We believe Voider solves a massive friction point in the modern "on-demand" economy. Moving forward, we want to expand our agent's reach to include travel booking and subscription management. As students, we're excited to keep iterating on this to see how far we can push the boundaries of autonomous commerce. <div