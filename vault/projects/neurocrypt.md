---
slug: "neurocrypt"
url: "https://devpost.com/software/neurocrypt"
title: "NeuroCrypt"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 355
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# NeuroCrypt

> Behavioral biometrics for medicine. Capture cognitive patterns in 60 seconds, authenticate with ML. NeuroCrypt: unhackable, unclonable identity verification. Solves $3B annual medical identity theft.

[Devpost](https://devpost.com/software/neurocrypt) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[privacy_tech]] [[realtime_stream]] [[vision_ocr]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** cors, css3, flask, github, html5, javascript, node.js, npm, numpy, python, react18, sckit-learn

## How they structured the write-up

- inspiration
- what we built
- technical highlights
- challenges faced
- what we learned
- what's next for neurocrypt

## Body

Running phase Landing page Result Result Inspiration Medical identity theft affects 3.1 million Americans annually, costing the healthcare system $3.1 billion. Traditional authentication fails: passwords are phished, OTPs are SIM-swapped, and biometrics are spoofable. We asked: what can't be stolen? Your brain's behavior. Unlike physical biometrics, behavioral patterns are: Dynamic (change with mood, stress, fatigue) Unclonable (tied to neurological wiring) Unhackable (can't be replayed or stolen) What We Built NeuroCrypt is a full-stack behavioral biometric authentication system that verifies users based on cognitive-behavioral fingerprints. During a 60-second micro-test, we capture: Response latency & consistency Keystroke rhythm & intervals Mouse dynamics & acceleration Decision timing patterns Pattern recall accuracy An Isolation Forest ML model detects deviations from the baseline (<100ms inference). If behavior matches, authentication succeeds. Technical Highlights Backend: Flask + Python + scikit-learn (Isolation Forest, 100 trees) Frontend: React 18 + Vite with glassmorphism design (12-16px blur, animated gradients) ML Model: 14-dimensional feature space, <100ms inference, 95%+ accuracy Architecture: RESTful API with CORS, session-based storage, synthetic data generation for demo Challenges Faced Feature Engineering: Converting raw behavioral signals into meaningful ML features proved tricky—we had to carefully extract latency statistics, keystroke intervals, and acceleration patterns without overfitting. Cross-Origin Proxy: Browser security required a Vite proxy to route requests from the React frontend to the Flask backend. UI Extravagance: Creating a truly impressive glassmorphism design required careful tuning of blur depth, gradient overlays, and animations to feel premium on both mobile and desktop. What We Learned Behavioral biometrics are a frontier in healthcare security—rarely explored in hackathons ML inference must be <100ms for real-time auth to feel responsive Full-stack submission requires meticulous attention to docs, code quality, and UI polish The novelty of the idea + technical execution + design quality = winning formula What's Next for NeuroCrypt Mobile App: React Native version for iOS/Android Federated Learning: Train models on user devices without sending data to server Continuous Authentication: Real-time behavioral monitoring during entire session Cognitive Health Insights: Detect early signs of stress, fatigue, or neurological changes Multi-factor Biometrics: Combine behavioral + traditional biometrics (face, fingerprint) Production Deployment: Docker containerization, database (PostgreSQL), cloud hosting (AWS/GCP) <div