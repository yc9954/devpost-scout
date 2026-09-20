---
slug: "i-imo"
url: "https://devpost.com/software/i-imo"
title: "I-IMO"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 484
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# I-IMO

> Intelligent IRL Meeting Organizer - A conversational AI agent designed with the busiest people in mind.

[Devpost](https://devpost.com/software/i-imo) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**substrate** [[code_repository]] [[geospatial]] [[transcript_audio]]

**stack** chromadb, convex, digtalocean, express.js, fastapi, groq, openai, react, shadcn, tailwind, typescript, vite, yolo

## How they structured the write-up

- inspiration
- what is i-imo?
- our tech stack
- architecture
- challenges we ran into
- important lessons
- what's next

## Body

I-IMO Architecture Pipeline Future Calendar Event Assistant Custom Query Interface Custom Query Interface With Response Profile Summary Interface Profile Summary Interface with Future Events Profile Summary Interface with Webcam Inspiration Ever had an incredibly busy day and can't remember all the people you've met, or all the tasks you've got planned for the future? We're humans! Our memory is imperfect and that's difficult, but it doesn't need to be: so we built I-IMO! I-IMO is a conversational AI agent designed with the busiest people in mind. I-IMO scans both visual input (webcam) and aural input (OMI devkit2) throughout your day to organize and summarize profiles for everyone you meet, while maintaining task lists and tracking important events so you never forget anything important from your meetings. N.B: We originally wanted to do this app on any smart glasses, but unfortunately due to supply constraints we couldn't get one. In the future, the plan is to adapt our project to run off of in-built webcams in devices like the Omi Glass. What is I-IMO? I-IMO is a personal conversational intelligence assistant that is an always-on second-in-command: Captures conversations through real-time audio transcription Recognizes faces via webcam to identify meeting participants Builds personal profiles automatically from conversation context Extracts action items and creates task lists from discussions Maintains conversation history with semantic search capabilities Never lets you forget important details about the people you meet Generates context to infer insightful predictions/aids for upcoming events in your calendar. Our Tech Stack React + Typescript + Vite, FastAPI + Custom YOLO11n model for face detection, Tailwind + Shad/CN UI, Convex Backend, Express.js Backend for NLP, Groq-hosted gpt-whisper for audio transcribing, Digital Ocean AI Gradient for GPU intense task, ChromaDB for vectorised queries and semantic search, OpenAI Text Embedding. Architecture Challenges We Ran Into connection issues 😡, streaming raw audio data from Omi (with low latency), high accuracy face classification that remains consistent (tagging id and tag name with it), deduplication of misspellings of names and mistranscriptions, nature of audio streaming: 5 second chunks clipping certain transcribed words, syncing vectorised ChromaDB with traditional Convex backend, minimising non-deterministic nature of profile summaries and task predictions, Important Lessons Learnt how to integrate a lot of different technologies and choose/route between the best models for unique workloads, Designed ways to sync between multiple backends and frameworks, especially with fundamental infra differences between vectorised semantic-search db's and traditional backends, Balanced the benefits lightweight, fast inference models with the lower completion accuracy, Developed a lot of ad-hoc teamwork skills while working on the same project with time-pressure (minimising merge-conflicts, documenting pull-requests using tools like CodeRabbit, keeping commit tree clean...) What's Next Deep integration with glasses (Meta Raybans, Omi Glass, Snapchat Spectacles), Potentially link 3rd party MCP providers, Connect with social media platforms for deeper context / automated actions based on the user's day, Time-sensitive summaries, Mobile, watch, and native versions of the dashboard. <div