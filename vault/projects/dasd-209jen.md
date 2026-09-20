---
slug: "dasd-209jen"
url: "https://devpost.com/software/dasd-209jen"
title: "Intelligent Meeting Assistant"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 329
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Intelligent Meeting Assistant

> AI-powered meeting assistant that transcribes speech in real-time, detects action items, and generates decision-focused summaries — all built with Kiro AI.

[Devpost](https://devpost.com/software/dasd-209jen) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**substrate** [[transcript_audio]] [[web_dom]]
  <sub>weak: code_repository</sub>

**stack** ai, browser, css, html, kiro, node.js, recognition, speech, typescript, websockets

## Body

Inspiration Meetings often consume valuable time, and key details get lost in endless notes or go undocumented. We wanted to build an assistant that helps teams focus on conversations instead of note-taking — turning raw speech into structured action items and decisions in real time. What I built I created the Intelligent Meeting Assistant , an AI-driven tool that: Transcribes speech directly from the browser in real time Detects action items like tasks, deadlines, and assignments automatically Tracks decisions with confidence scores Summarizes discussions into professional meeting notes Provides dual modes: Demo (with sample data) and Real Speech (via microphone input) The interface is simple and responsive — just start a meeting, grant microphone access, and watch tasks appear automatically as people speak. How I built it Kiro AI-assisted development was central: Spec-driven development : Kiro generated the entire architecture from specifications Agent hooks : Automated workflows for testing and deployment Intelligent code generation : Full-stack TypeScript with Express, WebSocket, and browser speech APIs Real-time features : WebSocket integration ensured low-latency transcription and updates The project structure is clean and modular: ├── .kiro/ # Kiro specs, hooks, and steering ├── src/ # TypeScript source code ├── index.html # Main interface ├── script.js # Frontend logic ├── server.js # Express server └── package.json # Dependencies What I learned How to effectively collaborate with an AI IDE like Kiro to go from idea → spec → production-ready code in record time How to design real-time features that rely on browser APIs and WebSockets Balancing AI-driven generation with custom refinements for UX polish Challenges I faced Speech transcription quality varies with accents and background noise — tuning detection was tricky Building smooth real-time syncing between speech recognition, task detection, and the UI Designing fallback Demo Mode so the app could be showcased even without live microphones Impact On average, this tool saves 2+ hours per week per team member by automating meeting documentation and ensuring that action items are never missed. <div