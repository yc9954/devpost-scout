---
slug: "jiggle-wiggle"
url: "https://devpost.com/software/jiggle-wiggle"
title: "jiggle wiggle"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1440
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# jiggle wiggle

> any move, any coach, anytime.

[Devpost](https://devpost.com/software/jiggle-wiggle) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[accessibility]] [[developer_tools]] [[education]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** elevenlabs, grok, heygen, mediapipe, openai, perplexity, python, render, typescript, zoom-sdk

## How they structured the write-up

- inspiration
- what it does
- why now
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for jiggle wiggle

## Body

Inspiration We’ve all tried learning a dance from TikTok or YouTube, rewinding, pausing, squinting at our reflection, and still not knowing if we’re doing it right. Your timing feels off, your arms look strange, but you can’t tell why. And this problem is much bigger than dance. It’s golf swings, tennis serves, yoga poses, lifts at the gym, martial arts, physical therapy, millions of physical skills where the internet gives us infinite demonstrations but zero correction. You can watch experts in slow motion or replay them frame by frame, but information isn’t coaching. Without someone telling you what to change, progress is slow, frustrating, and can even lead to bad habits or injury. We wanted to build the thing we wished existed. We personally want it to finally nail the choreographies I learn online. Someone else might use it to stay engaged and improve during a Zoom class, rehearse a presentation, or practice rehab exercises correctly. An AI coach that can watch any reference, from YouTube, a live instructor, or even an AI-generated demo, can watch you at the same time and give real-time, precise, actionable feedback. Not just “good job,” but “your left elbow is dropping 15 degrees,” “your hips are opening too early,” or “hold the pose a little longer.” Instead of passive watching, learning becomes interactive. Instant feedback, infinite patience, always available. We believe movement education should be as accessible as opening a browser tab. What it does Jiggle Wiggle is a real-time AI movement coach that works with three input modes: YouTube mode : Paste any dance or fitness video URL. The app downloads it, extracts reference poses frame-by-frame, and compares your webcam feed against the dancer in real-time with a split-screen view, skeleton overlays, and per-body-part scoring (arms, legs, torso). Zoom mode : Join a live Zoom call with a dance instructor or friend. The app captures their video feed, runs pose detection on both of you simultaneously, and coaches you through matching their moves — like having an AI mirror in a private lesson. Generation mode : Describe what you want to learn and AI generates the reference for you. Across all modes, an LLM-powered voice coach gives you adaptive spoken feedback in real-time ("Raise your left arm higher!", "Great match — keep it locked in!"). It adapts its personality based on whether you're doing dance (hype, rhythmic) or gym/fitness (form-focused, technical). You can also control playback with hand gestures — wave to pause, hands above your head to restart. Why Now The demand is massive. Online fitness and sports instruction already reaches hundreds of millions of people worldwide. The global fitness industry is estimated at $250B+, with digital fitness alone projected to surpass $60B in the next few years. Meanwhile, more than 500 hours of video are uploaded to YouTube every minute, and platforms like TikTok have made short-form skill tutorials one of the most consumed categories on the internet. But despite unlimited access to demonstrations, the missing layer has always been personalized feedback at scale. Watching is passive. Improvement is active. We’re building the bridge between the two — turning any video into an interactive coach. How we built it Frontend : Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS 4 Pose detection : MediaPipe Pose running entirely in-browser via WASM — no server-side GPU needed for real-time tracking. We load the model from CDN and process frames through offscreen canvases for reliability. We also use a segmentation model—specifically SAM2 by Meta, hosted on serverless GPUs—to help the user match the motion better. Scoring engine : Custom geometric pose comparison that normalizes for different aspect ratios and camera angles, with per-limb scoring (arms, legs, torso). We blend this with Groq vision-based scoring for an "anchor" score and apply EMA smoothing for stable display. AI coaching : OpenAI GPT-4o-mini with mode-specific system prompts, conversation history, and adaptive throttling. Audio feedback via OpenAI TTS. The coach sees the full geometric comparison data so it can give specific limb-level corrections. Zoom integration : Zoom Meeting SDK embedded in an isolated iframe (React 18) for joining calls, plus getDisplayMedia screen capture with a shared singleton MediaPipe Pose instance and a mutex to serialize WASM calls across video sources. Gesture control : Hand gesture recognition using MediaPipe Pose landmarks — wave to play/pause, swipe to skip, hands above head to restart. Chrome extension : One-click to open any YouTube video in the coaching app. AI Video Generation Pipeline : Perplexity Sonar Pro researches the movement across the web to gather accurate descriptions and context. Bright Data lets us fetch reference material, tutorials, and blog posts. Finally, HeyGen's Avatar API generates a high-fidelity AI avatar of the movement, and we use Grok Imagine to animate it. Challenges we ran into The biggest challenge was running MediaPipe Pose on two live video sources simultaneously . MediaPipe's WASM backend only supports a single Pose instance per page. We tried multiple approaches — shared round-robin managers, independent instances, separate onResults callbacks — and discovered that creating two new Pose() objects causes the second to silently stomp the first. The solution was making loadPose() return a singleton and having each panel set its onResults handler atomically inside a mutex lock right before each send() call. This took many iterations to get right. Screen capture via getDisplayMedia also had quirks — MediaPipe couldn't reliably process raw HTMLVideoElement frames from screen capture streams, so we had to draw each frame to an offscreen canvas first, then send the canvas to MediaPipe. And preferCurrentTab for tab capture was a dead end because MediaPipe would detect poses from the entire page (including the webcam panel and its own skeleton overlay), creating a feedback loop of wrong detections. We ran into platform-specific binary issues while deploying on Render. Native Node.js addons ( lightningcss , @tailwindcss/oxide ) ship platform-specific binaries, and npm ci from a macOS-generated lockfile silently skips Linux binaries. We fixed it by explicitly installing Linux native bindings in the Dockerfile build stage. Accomplishments that we're proud of Real-time dual-source pose comparison running entirely in the browser — no server-side GPU needed for the core experience. MediaPipe Pose, skeleton overlays, geometric comparison, and scoring all run client-side at interactive frame rates. Three input modes (YouTube, Zoom, generation) all feeding into the same comparison and coaching engine — the architecture is genuinely flexible. The AI coach actually gives useful, specific feedback — it's not generic encouragement, it knows which limb is off and by how much because we pipe the full geometric comparison data into the LLM context. Hand gesture controls that let you interact with the app while dancing without touching the keyboard. Aspect ratio normalization in pose comparison — comparing a 16:9 Zoom feed against a 4:3 webcam "just works" because we correct the coordinate space before comparison. What we learned LLM coaching is only as good as the context you give it. Generic pose summaries produced generic advice. Once we started feeding per-limb geometric comparison data with specific scores, the coaching quality jumped dramatically. Context is everything. MediaPipe's WASM backend is powerful but has hard constraints around concurrency that aren't well documented. We learned to treat it as a shared resource with careful serialization. The gap between "pose detection works" and "pose detection works well enough to be useful" is enormous. Raw landmarks are noisy, and without smoothing, visibility thresholds, and garbage frame rejection, the skeleton overlay is unusable. LLM coaching is only as good as the context you give it. Generic pose summaries produced generic advice. Once we started feeding per-limb geometric comparison data with specific scores, the coaching quality jumped dramatically. Browser APIs like getDisplayMedia have subtle differences across capture sources (tab vs window vs screen) that significantly affect what pixels you actually get. What's next for Jiggle Wiggle Progress tracking over time — save sessions, track improvement across days and weeks, and surface trends ("Your arm placement improved 15% this week"). AI-generated reference videos — describe a move in text and get a generated video reference to learn from, closing the loop on the generation mode. Progress tracking over time — save sessions, track improvement across days/weeks, and surface trends ("Your arm placement improved 15% this week"). Mobile support — the core MediaPipe pipeline works on mobile browsers, but the UI needs adaptation for single-screen use. Multi-person support — detect and compare against multiple people in a Zoom call or video (e.g., follow the instructor, not the other students). Community library — share and discover pose sequences, routines, and challenges created by other users. Expanded movement domains — physical therapy rehabilitation tracking, martial arts kata scoring, sign language learning. <div