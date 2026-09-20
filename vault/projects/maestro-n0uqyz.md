---
slug: "maestro-n0uqyz"
url: "https://devpost.com/software/maestro-n0uqyz"
title: "Maestro"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 614
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Maestro

> Turn an everyday object into infinite instruments.

[Devpost](https://devpost.com/software/maestro-n0uqyz) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** gx10, nvidia, perplexity, qwen2.5-vl, suno, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for maestro

## Body

Inspiration We’re an international team, and music is one of the few languages everyone on our team shares. No matter where we’re from, we’ve all used everyday objects, desks, bottles, and brooms to make rhythm or pretend instruments. We wanted to build something that lets anyone express themselves musically and develop their musical skills without needing expensive gear or formal training. What it does Maestro turns a broom into a playable guitar and music studio. Using a camera, hand tracking, and sound mapping, we detect a broom and map your hand movements to musical notes so you can instantly play it like a real instrument. An iPhone companion detects pressed “strings,” letting you form chords and control pitch while strumming in the air. If you have a broom, you have an instrument. Maestro also acts as a music coach and generator. After you play, the system analyzes your posture, timing, and sound, then gives short, actionable feedback through an AI tutor. In generation mode, what you play on the broom becomes the seed for a fully produced track: your performance is analyzed and expanded into new music. The goal is to make music creation accessible, expressive, and global, from a single everyday object to unlimited instruments and songs. How we built it We built Maestro as a real-time multimodal system combining computer vision, hand tracking, audio analysis, and multi-agent AI. Instrument mapping + tracking: MediaPipe hand tracking provides 21 landmarks per hand each frame Wrist + strum fingertip are smoothed to form a virtual guitar “neck” Magenta tape on the broom pole is detected with OpenCV Fretting hand position projected along the pole gives a 0–1 value that drives pitch/octave Strums are detected when the strumming fingertip crosses the neck line with enough velocity An iPhone app detects pressed “strings” and sends chord data to the system Real-time system + web interface: A Python server streams webcam frames over WebSocket Browser UI sends commands (like “get coaching”) and recorded audio The system captures sound-to-feature data and maps gestures to notes live Dual-agent AI coaching: On “stop playing,” the latest fra:me and audio are sent to a GX10 server Qwen2.5-VL analyzes posture and technique from video NVIDIA Music Flamingo analyzes rhythm, timing, and musical style Both agents run in parallel and return structured feedback Feedback is merged into a single script and delivered via on-screen text and TTS Hardware + generation pipeline: Models run on an ASUS GX10 with an NVIDIA Blackwell GPU Separate services handle vision+audio and audio-only flows In generation mode, Music Flamingo analyzes your performance The output is passed to a Suno API pipeline to generate a full track based on what you played Challenges we ran into Getting low-latency tracking so strums feel instant and musical Making hand tracking stable across lighting, camera angles, and different brooms Mapping gestures to notes in a way that feels intuitive Syncing iPhone string detection with webcam tracking in real time Running vision + audio models together without slowing feedback Designing short, useful coaching instead of overwhelming users Accomplishments that we're proud of Turning a literal broom into a playable guitar that feels responsive Creating a system anyone can understand in seconds Making something expressive across cultures and skill levels Getting real-time interaction working end-to-end What we learned Latency matters more than model size for musical interaction Multimodal AI (vision + audio) creates much richer feedback Real-time systems require tight coordination between frontend, backend, and models The best demos are immediately understandable and fun What's next for Maestro Support more objects beyond a broom Add multiplayer and collaborative jam mode Personal practice tracking and adaptive coaching Expand generation mode into full song creation tools <div