---
slug: "my-voice-w67t8v"
url: "https://devpost.com/software/my-voice-w67t8v"
title: "My Voice"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 715
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# My Voice

> Your AI Voice

[Devpost](https://devpost.com/software/my-voice-w67t8v) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[finance_payments]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, elevenlabs, gemma, html, javascript, mediapipe, python, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for my voice

## Body

Thumbnail Recreate your voice with help from ElevenLabs! Get suggested medical phrases from Gemma4! Keyboard Input 3D Eye Tracking enabling Dwell Control Dependancy Chart Inspiration Every year, 800,000 people in the US suffer a stroke. Up to 40% lose their ability to speak, and up to 75% suffer severe motor impairment. They are locked in, having lost traditional forms of communication. However, functional eye movement remains highly preserved in the vast majority of patients. This is My Voice : a zero-friction, augmented and alternative communication (AAC) dashboard and eye-tracking software that uses the one reliable motor function patients have left to give them their voices back. What it does My Voice is a webcam-based Augmented Accessible Communication(AAC) platform that empowers users to control their computer and communicate entirely through their gaze. By mapping the user's eye movements to an on-screen cursor, individuals can navigate an anticipatory user interface to construct sentences. To ensure the platform is truly universally accessible, we integrated a real-time, two-way translation system. This allows users to seamlessly communicate across language barriers, with full support for English, Mandarin Chinese, and Spanish, converting their selected thoughts into localized text and speech. How we built it We built our gaze-tracking pipeline entirely from scratch using Python, OpenCV, and MediaPipe. Instead of relying on simple 2D pupil tracking, which is highly sensitive to head movement, we engineered a true 3D geometric face and eye model: Pose Estimation : We utilized MediaPipe Face Mesh to extract the facial topology, facial orientation, and absolute position from the camera's perspective. We also used this mesh cloud to isolate the eyelid contours and iris centers. 3D Gaze Estimation : We projected the 2D iris landmarks onto a mathematically modeled 3D eyeball (assuming an average eyeball radius of 1.2 cm) using exact line-sphere intersection. By calculating the vector between the center of this 3D eyeball and the surface of the iris, we generated a true 3D gaze ray. Calibration & Control : We built a custom calibration sequence that uses dual ridge regression to map these 3D gaze vectors to the user's exact logical screen resolution in 2D space. We further refined this input with Kalman Filtering, deadzoning, saccade limits, and grid partitioning. On-Device-Compute : We built this app with the intention of running all Generative AIs, other transformers, and image processing all on-device. We believe applications should distill the best from frontier models to give users the best secure, low-latency experience possible. Challenges we ran into Hardware Limitations : Most eye-tracking software uses custom IR cameras. Developing a robust eye-tracking system on a standard, low-resolution, and low-refresh-rate webcam so it remains accessible to the masses was by far the most technically challenging part of this project. Mathematical Stability : Operating in a 3D metric space using a 2D camera feed introduced severe error drift and high-frequency noise. We had to heavily filter the coordinate data to stabilize the cursor and prevent it from jumping erratically without introducing too much input lag. Accessible UI/UX : Designing an interface that is space-efficient while easy to use. We had to design an anticipatory UI that predicts the user's next action to minimize eye fatigue. Linguistic Architecture : Accommodating seamless two-way communication between languages with vastly different syntax and structures (Mandarin and Spanish) required careful handling of the text-to-speech and translation routing. Furthermore, custom data processing of conversations in native languages to create Markov Chains. Accomplishments that we're proud of Successfully building a free, self-contained platform that genuinely enables people to communicate and interact without needing their hands. Engineering our own 3D gaze-estimation math from scratch, successfully deprojecting 2D pixels into a functional 3D camera space. Achieving a level of cursor control smooth enough to actually navigate an interface, overcoming the massive limitations of standard webcam hardware. What we learned Building My Voice required deep knowledge in computer vision, linear algebra, and filtering. We also learned a tremendous amount about accessible design, specifically, creating software for users with motor disabilities requires completely rethinking standard UI/UX. Instead, design must prioritize minimal movement and high-intent actions. What's next for My Voice Expand language compatibility and support to over 30+ languages and dialects. Create/generate more advanced Markov chains in specific languages Refine eye-tracking technology to be more accurate and more precise. Utilize more advanced filters. <div