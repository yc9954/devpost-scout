---
slug: "remindar-94vnz5"
url: "https://devpost.com/software/remindar-94vnz5"
title: "RemindAR"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 671
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/elder_child_care"
  - "user/patient_family"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# RemindAR

> RemindAR is an assistive AR system that helps people with memory challenges recognise faces and recall relationships in real time using voice, AI, and contextual overlays.

[Devpost](https://devpost.com/software/remindar-94vnz5) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[voice_speech]]
**domain** [[elder_child_care]]
**user** [[patient_family]]
**substrate** [[transcript_audio]] [[video_visual]]

**stack** firebase, gemini, gsap, mediapie, python, react, sqlite, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- changelog
- what's next for remindar

## Body

Landing Page Try demo section Demo Dashoard view with add later notification Our vision How it works Inspiration RemindAR was inspired by how deeply memory affects human connection. For people living with dementia or cognitive decline, not recognizing familiar faces can be confusing, distressing, and isolating. These moments affect memory, confidence, dignity, and relationships. We wanted to explore how technology could support memory at the moment it’s needed, rather than testing or correcting the user afterwards. The idea of subtle AR overlays - similar to future smart glasses felt like a natural, non-intrusive way to assist recognition while preserving independence. What it does RemindAR is a real-time assistive AR prototype that helps people recognise faces and recall relationships during live interactions. Using a webcam, it detects faces, recognises known individuals, and displays contextual information such as names, relationships, and shared memories as floating AR-style labels. Users can register new people and query their memory using natural voice input in English, Hindi, & other languages (powered by Gemini). How we built it RemindAR is built as a real-time system with a modern frontend and an AI-powered backend. Face detection runs in-browser using MediaPipe for fast, low-latency performance. Face recognition uses InsightFace embeddings on the backend, matched using cosine similarity: Gemini 3.0 Flash is used for voice transcription, structured data extraction, and contextual memory queries in a single API call. WebSockets enable real-time communication between the frontend and backend. SQLite provides fast local storage, with Firebase Firestore used for cloud sync and persistence. The frontend is built with React, TypeScript, and Vite, using subtle GSAP animations to reinforce an AR-like experience. Challenges we ran into Keeping face recognition fast in real time without reducing the quality and accuracy of face embeddings. Making sure updates to a person’s details are reflected instantly during live face recognition. Supporting multiple languages reliably, which was difficult with local models and was solved using Gemini. Allowing instant face re-scans without causing UI lag or interrupting the user experience. Bringing together live camera, AR overlays, voice input, and dashboards into a smooth and cohesive frontend. Accomplishments that we're proud of Building a fully real-time face recognition pipeline with live AR overlays. Implementing voice-first person registration and memory queries using Gemini 3.0 Flash. Supporting multilingual input (English, Hindi, Hinglish) without separate pipelines. Designing an assistive, low–cognitive load UI instead of a purely technical demo. Creating a reliable hybrid storage system using SQLite and Firebase Firestore. What we learned Building for memory challenges requires an accessibility-first approach, where reducing cognitive load matters as much as model accuracy. Real-time system design benefits from splitting responsibilities: MediaPipe for in-browser detection and InsightFace for backend recognition. Using Gemini 3.0 Flash for transcription, structured extraction, and memory queries in a single pipeline simplifies multimodal AI workflows. Combining SQLite (local) and Firebase Firestore (cloud) improves reliability and graceful degradation in assistive applications. Changelog Over the past few days RemindAR has received significant updates!! Here's whats changed: Updated frontend to be more informative with a "splash screen" to guide you through the process when trying the demo. Context history per person, updates as you update the details and get saved in the dashboard. Can be accessed by clicking on the person's card in dashboard. Region selector for more language support and more accurate Speech-to-text. Add later feature. RemindAR notifies you if you want to add a person whom you've been talking to for more than 3 minutes. You can click 'later' and their temporary entry will be saved in dashboard. Native language support. RemindAR will now infer from the spoken content which language you mostly talk in and show the entries in that language only for a more inclusive experience. What's next for RemindAR Future work includes optimising RemindAR for wearable AR devices, improving on-device processing for privacy, and expanding accessibility features such as gesture-based interaction and personalised memory cues to make users' lives easier. I also plan to explore collaborations with caregivers to evaluate real-world usability and refine the system based on real user needs. <div