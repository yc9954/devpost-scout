---
slug: "wiiwork-8u1x62"
url: "https://devpost.com/software/wiiwork-8u1x62"
title: "WiiWork"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 499
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "substrate/web_dom"
---

# WiiWork

> Everyone is hyped about AI agents that can interact with the world. Problem: Websites weren't built with LLMs in mind What would it look like if a website was built ground up with Agent usage first?

[Devpost](https://devpost.com/software/wiiwork-8u1x62) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]]
**substrate** [[web_dom]]

**stack** anthropic, convex, deepseek, elevenlabs, framer-motion, nvidia, openai, porkbun, react, shadcn, tailwind, typescript, vercel, whisper

## How they structured the write-up

- why:
- how
- agent
- cool features
- what's next

## Body

Agent successfuly interpreting and fulfilling complex requests Agent handling large amounts of visual information WiiWork home screen WiiWork external device pairing screen WiiWork companion app audio input screen WiiWork: Making AI-Native Websites Why: Everyone's excited about AI agents interacting with the world. Companies are pouring billions into development. But there's a problem: websites weren't built with AI in mind. Over this weekend, I sought to answer: what would it look like to build a website from the ground up to be AI-native? How I built WiiWork solo over the weekend, drawing inspiration from web accessibility patterns. Just like screen readers use ARIA labels, I created a context-rich system where AI agents can understand and interact with web elements naturally. The core innovation is a Higher Order Component (HOC) system that wraps around UI elements and communicates their purpose, appearance, and location to the agent. This "Agentic Web Component" system is paired with a comprehensive global state manager (using Zustand) that synchronizes user and agent interactions in real-time and prevents errors from getting out of control. Agent The agent system is especially interesting. Instead of using a one-size-fits-all approach, I built a multi-model router that classifies user requests into categories: Simple tasks → GPT-4-mini (fast & efficient) Medium → Claude 3.5 Sonnet (more thoughtful) Complex Logic → NVIDIA DeepSeek (specialized reasoning) Conversational → GPT-4 (natural interaction) Malicious messages get flagged and a AI alignment model interferes Each category has its own carefully engineered system prompt, optimizing for both performance and cost. I prompt engineered all the models using Theo, and prompt engineering tool I built over winter break: https://trytheo.dev Cool Features Real-time voice interaction using ElevenLabs for speech synthesis and Open AI whisper for speech regognition Mobile-desktop pairing system for voice input Virtual cursor system with smooth animations Tool calling framework using regex parsing Reading list demo app Oh yeah, and the whole Wii thing. I was just feeling nostalgic. ## Technical Challenges The biggest challenge was maintaining state synchronicity between user and agent interactions. I solved this by creating a central state management system that handles both input streams consistently. Another tricky part was getting the voice interaction just right - dealing with audio streams and buffers, especially managing faulty recording features on mobile phone browsers, was a learning experience for me. ## What I Learned This project pushed my full-stack skills to the limit. I got deep experience with: Building complex AI orchestration systems Swapping between multiple LLM providers and maintaining chat history Real-time audio processing Low level web component code Accessibility-inspired design patterns What's Next I believe this pattern of AI-native web development is the future. In a few years, I expect many websites will use similar patterns to make themselves agent-friendly. WiiWork is just the beginning, a proof of concept showing what's possible when we make websites with Agents in mind from the start. Built solo at TreeHacks 2025 using React, TypeScript, Convex, Zustand, and working about 25/36 possible hours. Check it out at https://WiiWork.dev <div