---
slug: "mindguard-ai-9fjt23"
url: "https://devpost.com/software/mindguard-ai-9fjt23"
title: "MindGuard AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 695
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/mental_health"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "user/legal_professional"
---

# MindGuard AI

> AI That Protects Your Focus.

[Devpost](https://devpost.com/software/mindguard-ai-9fjt23) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**domain** [[education]] [[mental_health]] [[supply_logistics]]
**user** [[educator_student]] [[legal_professional]]

**stack** express.js, extension, javascript, mediapipe, mongodb, node.js, react, tailwindcss, yolo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mindguard ai

## Body

Landing Page Dashboard Live preview Site block Session Timer 🧠 MindGuard AI AI-powered focus intelligence that measures attention — not just time. Inspiration Timers measure time. They don’t measure attention. As students, we realized something frustrating: You can run a 30-minute study timer… and still scroll your phone for 15 minutes. Most productivity tools assume discipline. We wanted to build something that understands behavior. MindGuard AI was inspired by a simple question: What if your study timer could actually see when you're distracted? Not to judge you. Not to spy on you. But to help you become aware. And we wanted to do it without sending any video data to the cloud . So we built an AI-powered focus companion that runs entirely in your browser. What it does MindGuard AI is a privacy-first AI study focus tracker that: 👁 Detects focus using real-time face & gaze tracking 📱 Detects phone usage using on-device object detection (YOLOv8) ⏸ Automatically pauses sessions when distraction persists 📊 Tracks cognitive analytics across sessions 🔥 Calculates burnout risk and focus trends 🏆 Gamifies productivity with XP, streaks, and achievements 🚫 Blocks distracting websites via a Chrome extension Everything runs locally. No video ever leaves your device. After each session, users receive: Focus score Per-minute focus heatmap Distraction frequency Recovery time Burnout risk level Cognitive health score Phone-distraction correlation insights MindGuard AI doesn’t just track time. It tracks attention . How we built it We built MindGuard AI as a full-stack AI-powered web platform . Frontend React 18 Tailwind CSS Custom lightweight state management Animated SVG-based timer Canvas-confetti celebrations Vision System (100% On-Device AI) We implemented a two-loop AI architecture inside the browser. Loop 1 — Face & Gaze Detection MediaPipe FaceLandmarker (WASM) 478 face landmarks Custom iris-based gaze direction algorithm Frame-based smoothing & hysteresis logic Loop 2 — Phone Detection YOLOv8-nano ONNX model (~6MB) ONNX Runtime Web Custom non-max suppression Sliding window persistence to prevent flickering No frames are stored. No pixels are transmitted. The backend only receives boolean signals like: { "focused": true } { "phoneDetected": false } Backend Node.js + Express MongoDB + Mongoose JWT authentication Helmet + rate limiting Cron jobs for streak resets & zombie cleanup We built a Cognitive Engine that: Buckets focus per minute Detects behavioral patterns (Fatigue, Warm-Up, Fragmented Attention) Computes Burnout Risk (0–100) Computes Cognitive Health Score Measures Phone-Distraction Correlation Chrome Extension (Manifest V3) Polls active sessions Syncs blocklist Blocks distracting sites only during active sessions Redirects to a motivational blocked page This bridges real-world behavior with browser control. Challenges we ran into 1️⃣ Phone detection instability YOLO predictions fluctuated heavily. Phones would appear and disappear across frames. We solved this using: Sliding window persistence Separate appearance and dismissal thresholds Confidence weighting for similar object classes 2️⃣ Detection flickering Face detection fluctuated due to lighting and micro-movements. We implemented: Consecutive frame counters Grace periods Hysteresis-based state transitions 3️⃣ Performance optimization Running two AI models in-browser is resource intensive. We: Throttled detection loops (350ms & 500ms) Used singleton model loading Reduced React re-renders 4️⃣ Designing meaningful analytics We didn’t want random numbers. We carefully designed weighted formulas for: Burnout Risk Cognitive Health Focus Volatility Weekly trend slope Accomplishments that we're proud of 🚀 Running two AI models fully in-browser 🔒 Zero video leaves the device 📱 Real-time phone detection + session enforcement 🧠 A complete cognitive analytics engine 🔌 A working Chrome extension integrated with backend 🏆 Gamification system with XP, streaks, and 16 achievements 🎨 Production-ready SaaS-level UI 📄 Fully documented API and architecture Most hackathon projects are prototypes. MindGuard AI is deployable. What we learned AI in the browser is viable with optimization Stability logic matters more than raw model accuracy UX matters more than features Behavioral analytics require thoughtful weighting Privacy-first AI builds trust We also learned how complex human attention really is. What's next for MindGuard AI ⏳ Pomodoro mode with adaptive breaks 👥 Collaborative study rooms 📬 Weekly AI-generated focus reports 📈 Improved burnout prediction models 🌐 Firefox & Edge extension support 📱 Mobile companion app 🎵 Adaptive focus music Long-term Vision MindGuard AI becomes a behavioral intelligence layer for productivity — not just a timer. <div