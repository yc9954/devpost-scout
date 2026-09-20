---
slug: "interviewar"
url: "https://devpost.com/software/interviewar"
title: "InterViewAR"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 584
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
---

# InterViewAR

> InterViewAR: Empathy-Driven Hiring Through ARHelping interviewers detect stress, tension, and burnout cues in real time and coach candidates toward calmer, fairer, and more human interviews.

[Devpost](https://devpost.com/software/interviewar) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[labor_employment]] [[mental_health]]
**substrate** [[sensor_telemetry]] [[transcript_audio]]
  <sub>weak: web_dom</sub>

**stack** asi:one, augmented-reality, chroma, conversion.ai, groq, html, javascript, llama, python, react, three.js, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for interviewar

## Body

🧠 InterViewAR Empathy-driven VR interview coaching system that helps recruiters detect and respond to candidate stress signals in real time, powered by Groq Whisper + LLaMA , FastAPI , and Meta Quest 3 WebXR . Inspiration We’ve all seen it happen: a talented candidate freezes mid-interview, not because they’re unqualified, but because anxiety takes over. Recruiters often don’t realize the stress levels rising in real time, and candidates leave with their best potential unseen. InterViewAR was born to fix that. We wanted to build a tool that empowers recruiters with empathy through data , enabling them to notice stress cues, respond calmly, and create fairer, more human interviews. What it does 🕶️ InterViewAR is a VR-based interviewer assistant that: Captures real-time audio from a Meta Quest 3 headset Streams it to a FastAPI backend Uses Groq Whisper to transcribe speech instantly Analyzes voice patterns to compute: Pace (WPM) Tension level (0–1 scale) Filler count (um, uh, like…) Pause frequency (> 2 s gaps) Feeds those metrics to Groq LLaMA , which generates: Coaching suggestions (“Nod and reassure”, “Offer a short pause”) Follow-up questions (“Can you elaborate on that?”) Displays everything as a 3D heads-up display (HUD) inside the VR view, updated every 1.5 seconds Logs the full conversation and metrics in JSON for post-session feedback In short: it’s an AI empathy lens for interviewers, augmenting emotional awareness without bias. How we built it 🧩 Architecture Overview Frontend (WebXR + React.js) Renders the 3D HUD inside Meta Quest 3 Connects to backend through secure WebSockets ( /ws/audio , /ws/hud ) Backend (FastAPI) Handles audio ingestion, speech-to-text, metrics computation Calls Groq Whisper for transcription Calls Groq LLaMA for real-time suggestions & next questions Maintains thread-safe shared state and pushes updates every 1.5 s Logs sessions to JSON + ChromaDB Networking Secure HTTPS + WSS over local LAN (Mac ↔ Quest 3) Self-signed SSL certs for in-lab demos Stack FastAPI · Groq API · Three.js · WebXR · Python · JavaScript · ChromaDB Challenges we ran into 🎧 Audio streaming in VR browsers : Quest 3 WebXR and mic permissions were tricky to align over HTTPS. ⚡ Low-latency processing : achieving < 1.5 s turnaround for transcription + AI inference required optimization and queue management. 🔐 SSL and WebSocket trust : local certificates had to be accepted manually for secure WSS communication. 🧠 Groq LLaMA prompt tuning : balancing technical insights with human coaching tone took experimentation. 🎨 HUD design in 3D space : ensuring readability while keeping immersion was a design challenge. Accomplishments that we're proud of Built a fully functional real-time VR pipeline : from mic capture to live HUD updates. Designed empathy-driven AI coaching integrated into recruiter workflow. Achieved consistent 1.5 s feedback latency using Groq inference. Created a replayable session log system with stress-recovery tracking. Delivered a working demo entirely over LAN on Meta Quest 3 . What we learned How to synchronize asynchronous FastAPI tasks (audio ↔ AI ↔ broadcast). The nuances of WebXR development and VR browser permissions . Designing ethical AI for sensitive contexts like interviews. Optimizing real-time data visualization inside constrained VR environments. That small interaction cues, nodding, pausing, offering water , can profoundly change candidate experience. What's next for InterViewAR 🚀 Upcoming Goals 🧑‍💼 Recruiter analytics dashboard (Warp or Streamlit) 🎞️ Post-interview replay and heatmap of stress points 🤝 Multi-user support (panel interviews) 🧩 Integration with LinkedIn / ATS platforms 📧 Automatic feedback email summaries via Conversion AI ❤️ Adaptive empathy models fine-tuned from real recruiter data <div