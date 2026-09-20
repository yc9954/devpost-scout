---
slug: "sayso"
url: "https://devpost.com/software/sayso"
title: "SaySo"
hackathon: "Adobe Express Add-ons Hackathon"
organization: "Adobe"
winner: true
words: 1129
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# SaySo

> Feedback that sticks before it slips

[Devpost](https://devpost.com/software/sayso) · hackathon [[Adobe Express Add-ons Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]]
**substrate** [[document_pdf]] [[geospatial]] [[transcript_audio]]

**stack** documentapi, fastapi, gpt-4, javascript, mediarecorder-api, openai, python, react.js, sandboxapi, vite, web-audio-api, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sayso

## Body

Wireframes Demo (Part 1) Demo (Part 2) Pre-exisitng User Flows Features System Architecture Data Flow Sequence Inspiration As a design intern this summer, I experienced both sides of the feedback problem and neither was easy. On one hand, it was hard to give feedback. I’d notice small things like spacing that felt off or a color that didn’t quite work, but saying it out loud meant switching between tools, writing it out, finding the right frame, and hopping on unnecessary design critique calls. By the time I got around to sharing the feedback, I’d either lost the thought or decided it wasn’t worth the hassle. On the other hand, it was just as hard to get feedback. Input came in through Slack threads, Zoom calls, voice notes, or random conversations. It was never centralized, rarely specific, and almost never tied directly to the design. I’d spend more time chasing down what people meant than actually making changes. That’s when I realized the feedback loop was broken on both ends: too much friction to share thoughts, and too much chaos to act on them. I built SaySo to fix exactly that. What it does SaySo is an Adobe Express Add-on that transforms how creative teams give and receive feedback. Instead of manually writing long, individual comments, juggling tools, or hopping on meetings, SaySo lets users record voice feedback in the moment, and instantly turns those into actionable, design-linked tasks, right inside Adobe Express. Here’s what it does: Voice-first feedback: Users hit “Start Recording” and speak their thoughts naturally while reviewing a design. Instant transcription: SaySo uses OpenAI’s Whisper to transcribe speech to text in real-time. Actionable summaries: The transcript is processed by GPT to extract clear, concise feedback and suggested tasks. Context-aware feedback: All comments are tied back to the canvas, showing which element or component the feedback relates to. Reviewers don’t need to stop to structure their thoughts and designers don’t need to guess what comments mean. SaySo closes the feedback loop between designers, reviewers, and clients by turning messy, multi-platform communication into a streamlined, intelligent system that integrates directly into existing creative workflows. How we built it I built SaySo as a fully functional Adobe Express Add-on with three core components: a React frontend, a sandbox bridge script, and a Python backend. Audio is recorded directly in the browser using the Web Audio API. When users click “Start Recording” in the SaySo panel, I use MediaRecorder to capture audio from the user’s microphone. The recording is saved as a .webm or .wav file in-memory, without uploading it anywhere.Once recording stops, the file is passed to the backend for processing. The fronend was built using React and Adobe’s React Spectrum design system for UI consistency. The panel interface lets users record/upload audio, displays live transcriptions, and shows extracted feedback as individual task cards. The Sandbox script (Javascript) acts as a bridge between the panel and the Express canvas. It handles communication with the backend and help map feedback to specific canvas elements via Adobe’s Document APIs. This is done by pulling real-time element selection history and sectioning it as per the transcript segments. The backend is written in Python using FastAPI. It uses OpenAI Whisper to transcribe audio and “gpt 4-0” to extract actionable design feedback from the transcript It returns structured JSON to the frontend with titles, descriptions, and metadata for each feedback point. I prioritized privacy and simplicity: no data is stored, and all processing happens in-memory. Challenges we ran into Adobe Express Add-ons run in an iframe sandbox, which blocks direct microphone access. This meant I couldn’t record audio using native Express APIs. To work around this, I implemented a custom recording system using the Web Audio API entirely within the panel but this limited some of the tighter integrations I had initially envisioned. One of our core goals was to make voice feedback context-aware tied to the exact elements a user was referencing in their design. While I was able to access real-time element metadata via the sandbox script, Adobe Express Add-ons cannot create native comments or annotations directly on the canvas. This meant I couldn’t simply attach feedback to elements the way users typically would in a built-in review flow. To work around this I captured the element selection history while recording and then matched transcript segments to selected elements based on timestamps and interaction patterns. This allowed users to infer which design element each piece of feedback referred to. While GPT was powerful for summarizing feedback, some transcripts led to ambiguous or overly general tasks. This was especially true when users spoke in non-linear ways, feedback referred to unnamed elements (“this part,” “that section”) and especially when tasks required assigning responsibility to team members by name. I had to fine-tune prompts, test multiple output formats, and in some cases allow user edits to clarify intent. Accomplishments that we're proud of I challenged the assumption that design feedback has to be slow, scattered, and manually written. SaySo introduces a new paradigm: voice-first critique that feels faster than typing, and just as precise, something no existing tool offers natively within Adobe Express. Despite strict sandboxing constraints in Adobe Express Add-ons, I successfully built a fully functional in-browser audio recording system using the Web Audio API. All recording and processing happens locally and securely, with no external uploads or storage. I engineered a lightweight pipeline that takes raw voice input and outputs structured, editable feedback cards, thanks to a combination of OpenAI Whisper and GPT. This lets SaySo distill even messy, spontaneous commentary into clear next steps with no need for manual transcription. What we learned Working within the Adobe Express Add-on environment forced us to think around API strengths and limitations, especially around audio input, persistent storage, and comment creation. I gained deep experience in sandbox tools and constraints, and learned how to prototype features that feel native even when they’re not supported out of the box. What's next for SaySo Over the next 2–3 weeks, I plan to launch SaySo as a public beta, focusing on polishing the UI and implementing a feedback summary dashboard that lets users view, edit, and organize all voice-generated feedback across projects. I’ll be actively testing the tool with two pilot design teams, gathering weekly insights to iterate quickly and uncover edge cases. If Adobe expands its SDK capabilities, I intend to integrate SaySo’s feedback directly into the Express canvas as native comments, removing the need for heuristic mapping and creating a truly seamless user experience. Beyond this initial rollout, I’m exploring support for uploading Zoom or Meet recordings, allowing teams to extract feedback from calls asynchronously. I also plan to build threaded comment functionality into each feedback item, so teams can collaborate without needing to meet live. <div