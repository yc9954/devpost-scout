---
slug: "wingman-e0fq7i"
url: "https://devpost.com/software/wingman-e0fq7i"
title: "Wingman"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 461
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "substrate/transcript_audio"
---

# Wingman

> ..

[Devpost](https://devpost.com/software/wingman-e0fq7i) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**substrate** [[transcript_audio]]

**stack** anam-ai, css, deepgram, fastapi, google-gemini, html5, javascript, python, streaming, vanilla-js, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned
- what's next

## Body

Inspiration First dates are nerve-wracking. You're trying to be charming, read body language, keep the conversation flowing — all at once. We thought: what if you had a real-time coach whispering smart advice in your ear, like a wingman who never misses a social cue? That's how Wingman was born — an AI-powered dating coach that listens to your conversation in real time, analyzes sentiment and context, and delivers discreet behavioral nudges through a futuristic heads-up display. What It Does Date Wingman streams live audio from your date conversation, transcribes it in real time using Deepgram's nova-3 model with sentiment analysis, and feeds it into a dual-layer coaching engine: Google Gemini LLM — generates highly contextual, specific advice based on the analysis given by Deepgram. Rule-based fallback engine — provides instant nudges based on sentiment patterns, question detection, topic identification, and engagement signals The nudges appear on a frosted-glass AR-style HUD overlay, categorized as tips , boosts , warnings , or insights — so you always know exactly what to do next. How We Built It The architecture is fully real-time and modular: Browser captures mic audio and streams it over WebSocket to a FastAPI backend The backend forwards raw audio to Deepgram's streaming API (nova-3 with sentiment analysis enabled) Transcripts feed into a ConversationBuffer — a rolling 60-second window of utterances with sentiment scores A WingmanEngine evaluates the buffer on every utterance using Deepgram for contextual advice and passes it to Gemini for refined prompts, with rule-based fallbacks for instant responses. Nudges are pushed back to the browser via WebSocket and rendered on your device. The backend is fully decoupled with no web dependencies, meaning the reasoning pipeline could be deployed to edge hardware like smart glasses or wearables with zero refactoring. Challenges We Faced Real-time latency — Balancing nudge frequency with relevance. Too many nudges are distracting; too few are useless. We tuned cooldown timers and evaluation triggers to hit the sweet spot. Sentiment accuracy — Deepgram's streaming sentiment can fluctuate on partial utterances. We solved this by only evaluating on final transcripts and using a rolling window to smooth out noise. Browser audio pipeline — Capturing, resampling, and streaming mic audio in real time from the browser required careful AudioContext and WebSocket management. What We Learned How to build real-time audio pipelines from browser to backend to third-party APIs Deepgram's streaming WebSocket protocol and sentiment analysis capabilities The importance of graceful degradation — always have a fallback when external APIs fail What's Next Smart glasses integration — deploy the coaching engine to AR wearables for truly discreet advice Multi-speaker diarization — distinguish between you and your date for even more targeted nudges Post-date recap — generate a summary of how the date went with actionable improvement tips <div