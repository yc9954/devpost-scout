---
slug: "iris-ojrmnv"
url: "https://devpost.com/software/iris-ojrmnv"
title: "Iris"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 737
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Iris

> Changing lives, one blink at a time :)

[Devpost](https://devpost.com/software/iris-ojrmnv) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]]
  <sub>weak: supply_logistics</sub>
**user** [[patient_family]]
**substrate** [[geospatial]] [[transcript_audio]] [[web_dom]]

**stack** electron, eyetrax, fastapi, git, javascript, kalman, letta, letta-client, letta-cloud, manifest-v3, node.js, numpy, opencv, pydantic

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for iris

## Body

System Design Inspiration Iris takes action for those who cannot. People with paralysis, as well as those in hands-free situations like surgeons, chefs, and mechanics, can all benefit from a browser that truly listens. Even in cases of severe paralysis, eye movement often remains one of the few ways people can still interact with the world. That simple truth inspired us to build Iris. One of our teammates has a family member who lost feeling in their hands. Watching them navigate a webpage using only their eyes reminded us that accessibility is not a feature, it is freedom. What It Does Hands-Free Control Using Eye Tracking, Voice, and AI Real-time gaze tracking highlights elements you look at Voice commands fill in text fields and control navigation AI agent predicts and executes your next action Works universally on any webpage without modifications Learns personal preferences over time (such as name, email, or address) Eye gestures enable clicks, tab switching, and scrolling Iris transforms the web into an adaptive, intelligent interface that moves at the speed of your gaze. How We Built It Real-Time Eye Tracking with Machine Learning Models We trained and deployed custom regression models (SVR, Ridge, Elastic Net, and a Tiny MLP) to predict gaze position from real-time webcam input. Combined with optimized OpenCV and MediaPipe pipelines, Iris achieves sub-100ms latency for seamless visual control. Advanced Kalman and KDE Filtering Pipeline Raw eye data is noisy. To stabilize motion, we implemented a Kalman filter for trajectory prediction and a Kernel Density Estimation (KDE) layer for adaptive smoothing. This multi-stage filter stack eliminates jitter and enables natural cursor flow. Multi-Modal Calibration System Calibration defines precision. Iris supports five- and nine-point calibration as well as continuous Lissajous-curve calibration, dynamically adjusting accuracy during runtime based on user behavior. WebSocket-Based Real-Time Gaze Streaming The Python backend streams gaze coordinates to the Chrome Extension through WebSockets with continuous synchronization and auto-recovery. Every blink, movement, and pause is captured and reflected instantly. Chrome Extension with DOM Element Snapping Iris detects DOM elements under gaze coordinates using a visual feedback system that highlights what you are looking at. Elements snap smoothly under the cursor through adaptive interpolation and dwell-time confirmation. Hybrid Speech Recognition System We combined Whisper.cpp (for local inference) with Vosk for fast, privacy-friendly transcription. The Electron-based speech service handles real-time dictation, enabling continuous speech-to-text input and command execution. Letta Agent Integration with Browser Actions Letta serves as Iris’s cognitive layer, a memory-driven agent that interprets voice commands and gaze context to perform browser automation such as form filling, navigation, and clicking. Virtual Keyboard with Gaze and Voice Input Users can type without hands using a multimodal keyboard that combines gaze focus detection (via Swift native helpers) and speech recognition for character input across applications. Swift Native Focus Watcher A macOS-native accessibility bridge detects active text fields and injects text directly into system-level inputs, allowing Iris to operate beyond browsers, across any desktop application. Custom Gaze Auto-Scroll System Looking near the edge of the screen triggers smooth auto-scrolling, controlled by gaze velocity and viewport position. It feels less like commanding a browser and more like moving through space. Element Highlighting with Adaptive Colors Every highlight adjusts dynamically for contrast and readability using CSS-injected adaptive color algorithms, ensuring accessibility in any theme or website layout. Challenges We Ran Into Our original plan was to use EEG signals for click gestures, but hardware delays forced a pivot toward eye and voice input. That shift was tough mid-hackathon, but it ultimately led to a more stable, scalable, and accessible foundation. Balancing real-time performance with accuracy was another major hurdle. Building a smooth filtering pipeline required countless iterations and fine-tuning. Accomplishments We’re Proud Of Achieved sub-100ms gaze latency for real-time interaction Built a universal browser integration that works without page modifications Implemented a memory-driven Letta agent for context-aware actions Designed a multi-stage filtering and calibration pipeline that rivals research-grade setups What We Learned Filtering is everything. Raw gaze data is unusable without strong temporal smoothing. Calibration defines trust. If the system drifts even slightly, users lose confidence. Accessibility inspires innovation. Designing for people with disabilities makes technology better for everyone. What’s Next for Iris Integrate EEG input for hybrid mind-eye control Expand Letta agent templates for scalability Extend native support beyond browsers to all operating systems Partner with accessibility foundations to deploy Iris at scale Empower millions of users with motor disabilities to regain independence <div