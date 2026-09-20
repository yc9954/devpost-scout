---
slug: "digitwin-hsf378"
url: "https://devpost.com/software/digitwin-hsf378"
title: "Digitwin"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 729
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Digitwin

> An autonomous "Ambient Guardian" using VLMs and MoveNet. It blends vision, emotion, and web data to proactively track ADLs, update medical profiles, and nudge movement. Care that understands!

[Devpost](https://devpost.com/software/digitwin-hsf378) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[elder_child_care]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** firebase, gemini, html5, movenet, react, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for digitwin

## Body

Inspiration We were frustrated by the "reactive" nature of modern healthcare. Most assistive tech sits idle, waiting for a crisis or a specific voice command to act. We envisioned DigiTwin as the bridge between physical reality and digital intelligence. Our goal was to create an Ambient Guardian, a system that doesn't just wait for instructions but "looks out" for the user by understanding movement, intent, and emotional nuance as fluently as a human caregiver, but with the tireless precision of a 24/7 computer vision engine. What it does DigiTwin is an autonomous, vision-first wellness ecosystem that operates entirely hands-free. The moment you enter the frame, the system performs a Zero-Touch Biometric Auth, instantly loading your unique Digital Twin Profile which includes clinical history, personality preferences, and emotional baselines. Key Features: 1) Multimodal Data Fusion: The AI doesn't just "chat"; it mixes raw video data, real-time emotion metrics, and your existing profile with live web searches, current location, and time-of-day context to provide hyper-personalized responses. 2) Contextual Visual Intelligence: The AI "sees" your environment. It knows if you are reading, drinking water, or exercising, allowing it to initiate natural, context-aware dialogue. 3) Active Safety & Hazard Detection: It identifies risky behaviors (e.g., holding a sharp object too close to the eye) and triggers proactive, urgent warnings. 4) Emotional Prosody Matching: Using real-time facial sentiment analysis, the AI detects happiness, sadness, or frustration and modulates its Neural TTS voice to match. It might use an energetic tone for encouragement or a soothing, empathetic voice if it detects distress. 5) ADL Tracking: It monitors Activities of Daily Living (Sitting, Standing, Lying Down) to detect physical patterns and triggers automated sedentary alerts (customizable) to keep the user active. How we built it The architecture is a sophisticated fusion of edge-processing and deep reasoning. 1) Movement: We used TensorFlow MoveNet (Lightning) for sub-millisecond human pose estimation and posture tracking. 2) Biometrics: A CNN-based face-api handles distinct user recognition and facial landmarking. 3) The "Brain": We integrated a Multimodal Large Language Model (VLM) that consumes visual context tags to manage a Dynamic Long-Term Memory. 4) The Persona Engine: This is the heart of DigiTwin. The system treats the user profile as an evolving Persona. By analyzing conversation and visual cues, it updates likes, dislikes, and medical notes (e.g., a new symptom or a change in diet) in real-time, effectively "writing" the user's medical history as life happens. Challenges we ran into A major hurdle was ADL Model Inconsistency. In early iterations, the model struggled to differentiate between sitting and standing, leading to "state flickering." To solve this, we developed a proximity-based logic gate: if the user's face occupies a specific percentage of the camera frame, the system defaults to a "Seated/Stationary" state. We then mapped shoulder-point elevation and lateral pixel movement as the high-confidence triggers to transition into "Standing." Additionally, syncing high-speed vision data with the deep reasoning of a VLM while fetching external web data (like weather or health news) required a highly optimized asynchronous data pipeline to maintain a "real-time" conversational feel. Accomplishments that we're proud of We are incredibly proud of DigiTwin’s Autonomous Synthesis. It doesn't just process data; it blends it. The system can suggest an indoor activity because it "sees" you are restless (vision), detects a "bored" emotional state, knows you have a mobility goal (profile), checks your current location/time, and fetches a web result showing it is raining outside. We successfully moved the needle from a "tool you use" to a "system that understands," culminating in a proactive loop that updates your clinical profile and keeps you moving. What we learned We learned that the most powerful AI in healthcare is the one you don't have to talk to. Context is everything. Building DigiTwin taught us that "intelligence" is measured by the reduction of friction. Passive observation, combined with a self-evolving persona, provides a high-fidelity longitudinal health record that is far more accurate than any manual log. What's next for Digitwin Our roadmap focuses on "Multi-User Dynamics" allowing the system to understand the relationship between a patient and a caregiver in the same room. We also plan to integrate Sensor Fusion or rppg (correlating wearable heart-rate data with our visual emotion analysis) to create a truly 360-degree digital twin of human health. We want DigiTwin to be the definitive operating system for proactive, empathetic care in every home. <div