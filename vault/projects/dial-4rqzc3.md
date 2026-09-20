---
slug: "dial-4rqzc3"
url: "https://devpost.com/software/dial-4rqzc3"
title: "DIAL(*)"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 291
team_size: 5
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "substrate/structured_db"
---

# DIAL(*)

> How we booked an SF Luxury Hotel for $158

[Devpost](https://devpost.com/software/dial-4rqzc3) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[finance_payments]] [[housing_homeless]] [[transportation]]
**substrate** [[structured_db]]

**stack** duckdb, elevenlabs, express.js, ngrok, node.js, sql, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dial (*)

## Body

More on SQL Optimizations Inspiration We were stranded in San Francisco on Saturday night without housing, and decided to let a fleet of AI agents find us a room. What started as a quick experiment turned into a full-stack system for autonomous negotiation, data-driven decision making, and natural communication. What it does DIAL (*) is an optimized customer service agent designed for data-heavy use cases. It makes phone calls, speaks naturally, queries live databases, and learns from every conversation to improve future performance. How we built it Customer Service Agent Functionality Phone Call Capability – Twilio Custom Voice + State Machine – ElevenLabs API Gateway – ngrok (for Express/TypeScript backend) Backend Logic – Express server managing call flow and SQL queries SQL Optimizations Created specialized query plans tailored for repetitive agent tasks Cached common lookups and indexed query-heavy tables for >100× faster response times Challenges we ran into Building a robust state machine that avoided hallucinations while staying conversational was hard. Integrating ElevenLabs’ voice with live Twilio calls also required solving real-time latency issues. Accomplishments that we're proud of Our agent called over 100 hotels and got real human responses from 40+ of them. It negotiated room prices down to $158 + tax — and landed us a bed for the night. Our SQL optimizations cut decision latency from seconds to milliseconds. What we learned We learned how to merge LLM-style intelligence with deterministic systems. We also saw firsthand how structured databases and state machines can ground AI behavior, creating a system that’s both smart and reliable. What's next for DIAL (*) We plan to scale DIAL into a general-purpose customer service infrastructure — allowing businesses to plug in their own data and voice models for seamless, human-like service automation. <div