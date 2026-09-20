---
slug: "spatial-math"
url: "https://devpost.com/software/spatial-math"
title: "SpatialMath AI"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 980
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# SpatialMath AI

> Your personal 3D math tutor — flat questions become explorable scenes

[Devpost](https://devpost.com/software/spatial-math) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]] [[transcript_audio]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** amazon-nova, css, html, javascript, matlab, python, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spatial math ai

## Body

Spatial Math AI Spatial Math AI — Multimodal 3D tutoring that turns flat questions into interactive spatial understanding Inspiration I studied IB Mathematics AA Higher Level. The algebra and calculus were manageable — the three-dimensional problems were not. I had to mentally unfold from a flat textbook diagram. I had no way to properly understand the 3D scene, I just had a static sketch and a formula to memorise. Spatial reasoning is the single strongest predictor of performance in advanced mathematics — and the hardest to develop from a page. The tools that actually build it (physical manipulatives, specialist tutoring, dedicated software) are expensive, inaccessible, or static. When Amazon Nova's multimodal understanding and real-time voice became available, I saw a way to build what I needed at 17 and couldn't find anywhere. What it does Spatial Math AI turns a maths problem into a live 3D scene you can explore and learn from. Type a question or photograph a worksheet. Amazon Nova Multimodal Embeddings reads the image and text together, extracts the mathematical relationships, and understands the problem across text and image simultaneously. A 3D scene builds automatically from what Nova extracted. Instead of staring at a flat diagram, students see the problem in space. Vectors, planes, and angles can be rotated and inspected from any perspective. Amazon Nova Lite guides the learner through the reasoning — asking what they think first, then adapting the explanation in real time based on their response. If a student is on the right track, Nova advances. If they're partially there, it redirects. If they're lost, it breaks the problem down differently. The scene updates alongside the explanation so the student always sees what Nova is responding to. Amazon Nova Sonic completes the loop: students can speak their answer and Nova responds in speech, with the same real-time adaptation running whether input is typed or spoken. Core capabilities 📸 Photo or text → 3D scene generated automatically 🧠 Scene-aware tutoring that adapts in real time to how the student is thinking 🎙️ Full bidirectional voice via Nova Sonic 🔷 Interactive Three.js scene with rotation, zoom, pan and net unfolding ✋ Freeform spatial sandbox with mouse or hand gestures How I built it Multimodal retrieval : Amazon Nova Multimodal Embeddings maps worksheet photos and text into a unified vector space for cross-modal semantic retrieval Lesson planning : Amazon Nova Lite reads the source image, extracts the mathematical structure, and generates the full lesson plan that drives the 3D scene Adaptive tutoring : Nova Lite evaluates every response in real time and adapts — advancing, redirecting, or escalating to a full worked solution with every step shown Voice : Amazon Nova Sonic runs bidirectional speech-to-speech — PCM in, transcript and spoken reply out, same evaluation pipeline as typed input Hand tracking : MediaPipe Tasks Vision lets learners manipulate the scene with hand gestures Backend : Node.js · Hono · Amazon Bedrock · Server-Sent Events · automatic model failover Frontend : Vanilla JavaScript · ES modules · Three.js · KaTeX · MediaPipe Challenges we ran into Generating valid 3D geometry from AI output: Nova produces scene plans describing objects and spatial relationships, but translating those into Three.js geometry that is visually correct and mathematically accurate required a strict schema and mesh normalisation pipeline. Reliable structured output from Nova: Nova Lite must produce complex lesson JSON. A single malformed response can break the entire scene pipeline. We implemented token-budget retry escalation and a normalisation layer that repairs common schema violations before rendering. Camera choreography during lessons: The camera must move to the right viewpoint at the right teaching moment without feeling jarring. This required a bookmark and transition system tuned specifically for spatial learning. Stable hand interaction: MediaPipe hand tracking is noisy at real-time frame rates. We applied smoothing, pinch detection thresholds, and jitter filtering so gestures feel intentional rather than accidental. Accomplishments that we're proud of Getting Nova Multimodal Embeddings to reliably map a photo of a hand-drawn diagram to the correct 3D lesson type — not through OCR or keyword extraction, but through genuine cross-modal semantic understanding. Building an adaptive tutoring loop that actually works. Nova reads a learner's response, identifies what they understood and what they missed, and adjusts both the explanation and the 3D scene in real time. Writing deterministic analytic geometry solvers for problems like skew line distance and line-plane intersection so the visuals are mathematically exact and the tutor never hallucinates when the answer should be precise. Running the entire app directly in the browser — Three.js, MediaPipe, KaTeX, and three Amazon Nova models coordinated through vanilla JavaScript and SSE streaming with no bundler, no build step, and no database. What we learned Multimodal AI works best when it understands relationships, not just text. Treating maths problems as objects, vectors, and spatial constraints made Nova far more reliable at generating the correct 3D scenes from both typed questions and worksheet photos. Generating visuals from AI requires strict structure. Without schemas, validation, and normalization layers, even a small formatting error in a model response can break the entire 3D rendering pipeline. Students engage differently when they can see and manipulate the mathematics. Rotating planes, highlighting vectors, and moving around the scene makes spatial concepts click much faster than static diagrams. Building everything directly in the browser meant learning how to combine multiple real-time tools. Integrating Three.js (3D rendering), MediaPipe (hand tracking), KaTeX (math typesetting), and Amazon Nova models through streaming APIs taught us how to coordinate complex systems inside a browser using vanilla JavaScript. What's next for Spatial Math AI Learner memory across sessions — Nova Multimodal Embeddings indexing past performance to surface targeted practice on weak concepts Expanded curriculum — calculus, physics, mechanics, and statistics; mapped to IB, A-Level, and AP syllabus Mobile — the Three.js scene and Nova Sonic pipeline are both browser-native; a PWA wrapper is the next step <div