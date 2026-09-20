---
slug: "lavoe"
url: "https://devpost.com/software/lavoe"
title: "Lavoe"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 525
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Lavoe

> Cursor for Music Production

[Devpost](https://devpost.com/software/lavoe) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]]
**substrate** [[structured_db]] [[transcript_audio]]

**stack** ai-sdk, claude, cohere, python, react, vercel, windsurf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lavoe

## Body

Lavoe 🎶 Lavoe is Cursor for music production — an AI-powered environment that lowers the barrier to music creation, making it easier for anyone to express themselves through sound. Inspiration Lavoe comes from the simple desire to make music. We wanted to lower the barrier for people to access music production. AI enhances everyone’s abilities, but in the creative industry, tech hasn’t given as much attention to accessibility. Our goal is to make it easier for others to express themselves and take the first step toward facilitating music production for everyone , not just those with years of technical training. What it does Lavoe provides an intuitive and AI-augmented DAW interface with features designed to streamline creativity: 🎵 AI-generated beats – Instantly create drum patterns and rhythms tailored to your track. ✂️ Agentic chopping of beats – Automatically slice, rearrange, and re-contextualize loops. 🎚 Agentic sorting of sounds – Organize samples, instruments, and recordings intelligently. 🎛 Agentic music engineering – AI suggestions for mixing, EQ, and sound design. 🎤 Live audio recording – Record vocals and instruments seamlessly within the workflow. How we built it We combined modern web frameworks with audio processing and ML tooling: Frontend : React + TypeScript + Next.js for a responsive DAW-style UI. AI SDK : Vercel AI SDK for seamless prompt orchestration. Backend : Python + FastAPI to handle audio processing and serve the AI pipeline. Audio Processing : Librosa for beat detection, tempo analysis, and waveform manipulation. Cohere/Anthropic/OpenAI : Cohere for language modeling, Pandas + Scikit-learn for dataset wrangling and prototyping. Challenges we ran into ⏱ Getting audio to play in sync with the time marker . 🤖 Designing the agentic workflow and making agents communicate with each other. 🔗 Connecting the backend audio pipeline to the frontend in real-time. ✂️ Deciding how to chop audio into meaningful segments for remixing. 📝 Figuring out the best way to describe audio to LLMs in a way they can understand and act on. Accomplishments that we're proud of 🌍 Taking a step toward democratizing music production with AI-driven tools. 🎨 Bringing a creative lens to the tech community , showing AI is not just for code or text. 🏗 Pushing design engineering to new heights by combining DAW workflows with agentic AI. 🥪 And importantly: we are NOT just a GPT wrapper — we’re a sandwich , layering multiple agents, models, and workflows into something truly new. What we learned 🎧 The complexities of audio processing beyond just waveforms. 🌀 Exploring different types of “vibecoding” — making the interface feel musical, not mechanical. 🖥 How to implement AI agents directly into a UI , balancing usability and power. 🔊 Handling audio playback in a browser environment, with all its quirks and limitations. What's next for Lavoe 🚀 Deployment – making Lavoe available for real musicians to use and test. 💸 Monetization strategies – exploring models for subscriptions, plugins, and creator marketplaces. 🌱 Y Combinator application – taking Lavoe beyond a hackathon project and into a scalable startup. Lavoe is about making music production more accessible, intelligent, and collaborative. Just as Cursor changed coding, Lavoe aims to change music creation. <div