---
slug: "kiru"
url: "https://devpost.com/software/kiru"
title: "kiru"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 743
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "substrate/transcript_audio"
---

# kiru

> Hate waiting on hold? kiru is a voice agent that actually calls companies, talks to customer support, and negotiates your bills down. Just type what you want and watch the live transcript

[Devpost](https://devpost.com/software/kiru) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**substrate** [[transcript_audio]]

**stack** asyncio, fast-api, nextjs, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for kiru

## Body

our cover page landing page chat summary ui chat concurrent calls ui landing page animation modals for hype Mobile App Inspiration Let's be honest, nobody enjoys calling their cable company. You know the drill: 45 minutes on hold, getting transferred three times, and somehow ending up with a worse deal than you started with. Negotiation is one of those skills everyone wishes they had but few people actually do. And even if you're decent at it, who has the time? So we asked ourselves: what if you just… didn't have to do it? What if an AI could pick up the phone, call the company, and haggle for you while you sit back and watch? That's kiru. What it does You tell kiru what you want ("get my internet bill lower," "talk them into waiving that fee," whatever) and it takes it from there. Before the call even starts, it does its homework: researching the company, pulling competitor pricing, finding leverage. Then it places a real phone call through Twilio and starts negotiating. Live. With its voice. Against a real human on the other end. The whole thing streams to a dashboard where you can follow the transcript in real time, peek at the agent's internal reasoning, and kill the call if things go sideways. Once it's over, kiru breaks down the entire conversation: what tactics it used, what concessions it pulled off, the final outcome, and what you should do next. How we built it The brain of the operation is a FastAPI backend in Python that orchestrates everything. Twilio handles the actual phone call and streams audio back to us. Deepgram transcribes it in real time. The negotiation engine constructs dynamic system prompts and streams responses from an LLM (we wired up support for OpenAI, Anthropic, and local vLLM endpoints). WebSockets keep the frontend and backend glued together so everything updates live. On the frontend, we built a Next.js app with a dark glassmorphic UI, because if you're going to watch an AI negotiate your bills, it should at least look cool. The dashboard shows live transcripts, call status, and post-call analysis with full audio playback. We also added a pre-call research layer using Perplexity and Bright Data so the agent walks into every conversation armed with actual data: competitor offers, market rates, that kind of thing. It's hard to negotiate without leverage, even if you're an AI. Challenges we ran into Real-time audio streaming nearly broke us. Getting Twilio's media streams to cooperate with our transcription and LLM pipeline, while keeping latency low enough that the conversation doesn't feel like a bad Zoom call, took a lot of iteration. And there are so many edge cases you don't think about until they blow up: voicemail detection, call status callbacks, making sure the agent doesn't accidentally talk over someone mid-sentence. Prompt engineering for negotiation was its own beast. The agent has to be firm without being rude, flexible without caving immediately, and it needs to shift strategy depending on what phase of the negotiation it's in (opening, midgame, endgame). Getting that balance right took endless tuning. Concurrency was the 3am villain. Multiple WebSocket connections, async audio processing, session state flying everywhere. Keeping all of it in sync without race conditions meant careful locking and a lot of coffee-fueled debugging. What we learned Telephony APIs are deceptively complex. TwiML, media streams, status callbacks... there's an entire universe behind "just make a phone call" that we had to speed-run our way through. We also learned that negotiation is surprisingly hard to formalize. Humans rely on tone, timing, gut feeling, things that don't translate neatly into a prompt. Building a system that captures even a fraction of that intuition forced us to think deeply about what actually makes negotiation work. And maybe the biggest lesson: building something truly end-to-end (from a live phone call to a real-time dashboard to post-call analytics) during a hackathon is an exercise in knowing what to cut and what to keep. What's next for kiru We've got plans. Inbound call handling is the big one. Imagine kiru picking up robocalls and wasting their time for a change. We also want to add multi-turn memory so it can reference past conversations ("Last time I called, your rep offered me…"), and expand beyond bills into things like appointment scheduling and customer service disputes. Longer term, we're looking at fine-tuning smaller models specifically for negotiation to shave down latency even further. <div