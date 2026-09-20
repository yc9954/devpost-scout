---
slug: "operation-ghost"
url: "https://devpost.com/software/operation-ghost"
title: "Operation Ghost"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 410
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/labor_employment"
  - "substrate/video_visual"
---

# Operation Ghost

> Operation Ghost is a C++ & AI gesture system using MediaPipe and Gemini. Control your PC via hand/voice with pixel-perfect knuckle tracking. It's the ultimate hands-free, accessible UI.

[Devpost](https://devpost.com/software/operation-ghost) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[labor_employment]]
**substrate** [[video_visual]]

**stack** c++, computervision, electron, gemini, google, mediapipe, node.js, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for opsghost

## Body

Inspiration Traditional input methods create barriers for people with motor disabilities, healthcare workers in sterile environments, and anyone seeking more natural human-computer interaction. We wanted to make computing accessible to everyone, regardless of physical limitations. What it does OpsGhost is an AI-powered gesture control system that lets you operate your computer using hand gestures and voice commands: Gesture Control : Move cursor by pointing, click with pinch gestures, type on a virtual keyboard in mid-air AI Vision Assistant : Google Gemini 2.0 sees your screen in real-time and executes voice commands Real Desktop Automation : C++ Windows API for instant response with no simulations How we built it Tech Stack: Computer Vision : MediaPipe Hand Landmarker (GPU-accelerated, 60 FPS) AI : Google Gemini 2.0 Live API (Multimodal) Desktop Control : C++ Windows SendInput API UI : Electron (transparent overlay) + React + TypeScript + Vite Backend : Node.js + Express bridge server IPC : Custom protocol between Electron and C++ controller Architecture: Multi-layer system with MediaPipe processing hand tracking at 60 FPS, Electron UI overlay, Node.js bridge server, and C++ executable for real-time desktop control (1-5ms response time). Challenges we ran into Cursor Drift During Gestures : Initial approach tracked fingertip → cursor moved when pinching. Solution: Track index finger knuckle for cursor position, tip only for click detection. Performance Bottleneck : PowerShell was too slow (100-500ms delay). Solution: Custom C++ executable with Windows API achieved 1-5ms response time. Multiple Click Detection : Gesture flickering caused repeated clicks. Solution: State machine with debouncing (250ms keyboard, 300ms mouse). UI Click Issues : Overlay was click-through. Solution: Dynamic mouse event handling based on hover zones. Accomplishments that we're proud of Zero cursor drift during gesture clicks (novel knuckle-tracking approach) 10-50x performance improvement over scripting alternatives 2-hand simultaneous typing like a real keyboard Multimodal AI integration combining vision + voice + automation 95%+ gesture accuracy with proper lighting What we learned Computer vision requires careful coordinate system management Performance optimization is critical for natural interaction State machines prevent race conditions in real-time systems User experience details (cursor stability) make or break adoption Multimodal AI opens entirely new interaction paradigms What's next for OpsGhost Mobile Support : Port to Android/iOS with camera control More Gestures : Swipe, rotate, pinch-zoom functionality Gesture Macros : Record and replay gesture sequences Eye Tracking : Combine with eye gaze for faster control Cloud AI : Offload processing for lower-end devices Accessibility Profiles : Customizable for different disabilities <div