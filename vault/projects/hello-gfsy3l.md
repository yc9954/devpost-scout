---
slug: "hello-gfsy3l"
url: "https://devpost.com/software/hello-gfsy3l"
title: "Hello"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 375
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Hello

> Video chat web app powered with real-time ASL transcription.

[Devpost](https://devpost.com/software/hello-gfsy3l) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[finance_payments]]
**substrate** [[code_repository]] [[transcript_audio]] [[video_visual]]

**stack** agora, deepgram, gemini, heroku, hume, hyperbolic, react, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for hello

## Body

Inspiration Only a small percentage of Americans use ASL as their main form of daily communication. Hence, no one notices when ASL-first speakers are left out of using FaceTime, Zoom, or even iMessage voice memos. This is a terrible inconvenience for ASL-first speakers attempting to communicate with their loved ones, colleagues, and friends. There is a clear barrier to communication between those who are deaf or hard of hearing and those who are fully-abled. We created Hello as a solution to this problem for those experiencing similar situations and to lay the ground work for future seamless communication. On a personal level, Brandon's grandma is hard of hearing, which makes it very difficult to communicate. In the future this tool may be their only chance at clear communication. What it does Expectedly, there are two sides to the video call: a fully-abled person and a deaf or hard of hearing person. For the fully-abled person: Their speech gets automatically transcribed in real-time and displayed to the end user Their facial expressions and speech get analyzed for sentiment detection For the deaf/hard of hearing person: Their hand signs are detected and translated into English in real-time The translations are then cleaned up by an LLM and displayed to the end user in text and audio Their facial expressions are analyzed for emotion detection How we built it Our frontend is a simple React and Vite project. On the backend, websockets are used for real-time inferencing. For the fully-abled person, their speech is first transcribed via Deepgram, then their emotion is detected using HumeAI. For the deaf/hard of hearing person, their hand signs are first translated using a custom ML model powered via Hyperbolic, then these translations are cleaned using both Google Gemini and Hyperbolic. Hume AI is used similarly on this end as well. Additionally, the translations are communicated back via text-to-speech using Cartesia/Deepgram. Challenges we ran into Custom ML models are very hard to deploy (Credits to https://github.com/hoyso48/Google---American-Sign-Language-Fingerspelling-Recognition-2nd-place-solution ) Websockets are easier said than done Spotty wifi Accomplishments that we're proud of Learned websockets from scratch Implemented custom ML model inferencing and workflows More experience in systems design What's next for Hello Faster, more accurate ASL model. More scalability and maintainability for the codebase. <div