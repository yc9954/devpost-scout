---
slug: "gait-pro"
url: "https://devpost.com/software/gait-pro"
title: "ADL Pro"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 811
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/patient_family"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# ADL Pro

> Turn any webcam into an autonomous 24/7 caregiver. Our browser-based AI tracks daily activity, detects falls instantly, and generates clinical mobility reports—zero wearables or hardware required.

[Devpost](https://devpost.com/software/gait-pro) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[elder_child_care]] [[health_clinical]] [[mental_health]]
**user** [[patient_family]]
**substrate** [[genomic_bio]] [[geospatial]] [[sensor_telemetry]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** gemini, html, movenet, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for adl pro

## Body

Inspiration With a rapidly aging global population, the demand for continuous health monitoring is skyrocketing. However, current solutions are polarized: they are either expensive, intrusive specialized hardware (cameras with monthly subscriptions) or wearable devices that elderly users frequently forget to charge or wear. We were inspired by the concept of "Invisible Care." We wanted to build a system that requires zero active participation from the user. No wearables, no buttons to press, and no expensive proprietary sensors. We asked ourselves: Can we turn a standard, 2010-era laptop webcam into a clinical-grade gait and safety lab using only the browser? What it does 1) ADL Monitor Pro V17 is a privacy-first, browser-based surveillance system that analyzes Activities of Daily Living (ADLs) in real-time. 2) AI Motion Tracking: It uses a deep learning model to map the human skeleton at 30+ frames per second. 3) State Recognition: It automatically classifies user activity into semantic states: Standing, Sitting, Walking, or Lying Down. 4) Fall Detection: It monitors vertical velocity and geometric compression to detect sudden falls, triggering an immediate visual alert and logging the critical event. 5) Clinical Gait Analysis: It counts steps, estimates gait intensity, and tracks "transitions" (e.g., Sit-to-Stand), which are vital biomarkers for frailty. 6) Deep Insight Reporting: At the end of a session, it generates a comprehensive medical report with radar charts, metabolic estimates, and AI-generated textual advice based on the user's specific movement patterns. How we built it The core of the application is built on the Edge AI philosophy—processing data locally to ensure privacy. Computer Vision: We utilized TensorFlow.js with the MoveNet (Thunder) model. This provides high-accuracy keypoint detection (17 points) directly in the web browser. Geometric Logic: Instead of training a secondary "black box" classifier, we built a transparent heuristic engine based on biomechanics. We calculate vector angles for the spine and thighs using trigonometry to determine the posture state. For example, if the thigh angle is less than 45 degrees relative to the vertical axis, the system registers "Standing," while an angle greater than 55 degrees registers as "Sitting." Lying down is detected based on the aspect ratio of the body. Fall Detection: We implemented a velocity-based trigger. We track the vertical position of the nose over time. A fall is flagged if the downward velocity exceeds a specific threshold while the bounding box aspect ratio simultaneously indicates vertical compression (i.e., the person is close to the floor). Frontend: The UI was built with Tailwind CSS for a responsive, "medical-dashboard" aesthetic, and Chart.js for rendering real-time data visualizations in the final report. Challenges we ran into The "Jitter" Problem: Raw keypoint data from webcams is noisy. A person sitting still would sometimes register as "micro-walking." We solved this by implementing a smoothing buffer and a movement threshold filter, effectively applying a low-pass filter to the coordinate data. Distinguishing Falls from Sitting: Rapidly sitting down looks mathematically similar to falling. We had to implement a "Floor Proximity" check (checking ankle vs. nose coordinates) and a "Shoulder Width Zoom" factor to distinguish a controlled descent from a collapse. Performance vs. Accuracy: We initially tried heavier models that lagged the browser. We optimized by switching to the SinglePose Thunder model and using requestAnimationFrame to decouple the UI rendering from the inference loop, ensuring the video feed remained fluid even if the AI skipped a frame. Accomplishments that we're proud of Zero-Server Architecture: The entire app runs client-side. No video data ever leaves the user's device, solving the massive privacy concern inherent in home monitoring. The "Deep Insight" Engine: We didn't just dump numbers. We wrote a logic engine that interprets the data into natural language (e.g., "Your active ratio is below recommended targets"), mimicking the advice a physiotherapist would give. Fall Detection Latency: We achieved a detection latency of under 300ms, allowing for near-instantaneous alerts. What we learned Biomechanics is Math: We learned that human movement can be effectively modeled with simple Euclidean geometry and trigonometry, reducing the need for massive labeled datasets for basic state detection. The Power of WebGL: We gained a deep appreciation for the capabilities of modern browsers. Running complex tensor operations via WebGL allows web apps to perform tasks previously reserved for native desktop applications. Context is King: Knowing that someone is moving isn't enough; knowing how they are moving (transitions per hour, gait cadence) provides the real picture of their health. What's next for ADL Pro Telehealth API: Integrating Twilio or EmailJS to automatically send an SMS to a caregiver when a fall is detected or if the user has been sedentary for >4 hours. Longitudinal Tracking: Using localStorage or PouchDB to save session data over weeks, allowing the system to spot long-term trends in mobility decline. 3D Pose Estimation: Upgrading to MediaPipe BlazePose to gain Z-axis depth perception, which would vastly improve the accuracy of gait speed estimation and slump detection. <div