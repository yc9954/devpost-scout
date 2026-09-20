---
slug: "just-replay"
url: "https://devpost.com/software/just-replay"
title: "Just Replay"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 444
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/video_visual"
---

# Just Replay

> Just Replay helps seniors with limited mobility relive favorite activities via low-intensity guided motion, real-time pose feedback, fall detection, and AI coaching with progress reports.

[Devpost](https://devpost.com/software/just-replay) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[video_visual]]
  <sub>weak: geospatial, web_dom</sub>

**stack** css, html, javascript, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for just replay

## Body

Avatar Model Exercise Selection User Mapping + Avatar Model + Live Vocal Coach Session Summary Statistics Inspiration Something that we’re all really concerned about is our grandparents and how they struggle to go about their daily lives when they have limited mobility or health complications. So we wanted to find a way for them to improve their health while finding fun in movement again. That's why we created our project Just Replay, which aims to help those facing physical barriers replay their favorite activities with low-intensity versions. What it does Just Replay starts off with intaking user information on their age and mobility limits to generate a safe, personalized session with a guiding video demo. An AI chatbox with text and voice features guides users as their movements are tracked with computer vision and compared with the guiding avatar's motions. How we built it Video demonstration: joint movements are stored in a pre-recorded JSON file of 33 trainer landmarks at 30 FPS. Leveraging online strategies, we used a mediapipe-pose engine to classify human-body joints from media input.Using this engine, we input .mp4 videos for accurate joint data for the video demonstrations, and run the engine through a live camera feed. A comparison using a mean between the normalization of distance of joints vs the angle of joints was used to compare accuracy. Using ElevenLabs, we leveraged their API to create a live-vocal coach for the elderly users to talk to through STS, with Google Cloud Gemma powering the responses. Using Vultr, we implemented a cloud-based backend to store information for the high-data json files resulting from demonstration videos and login info for users, where their progress can be downloaded to share with doctors, clinicians, and family members. To ensure safety, if a fall is detected and the user is unresponsive, a call system will contact an emergency number. At the end, you get a simple summary describing the session, your overall score, as well as any areas to improve. This includes a downloadable report of your exercise sessions and health data to send to medical professionals for further review. Challenges we ran into balancing accuracy and speed in real-time pose tracking, handling varied lighting/camera quality, simplifying feedback for seniors, and building reliable fall detection without false alarms. Accomplishments that we're proud of implementing live joint tracking, AI coaching, fall alerts, and session reports to be accessible and engaging for low-mobility users. What we learned how to optimize pose estimation pipelines, normalize movement data, design for accessibility, and integrate real-time AI feedback with user-friendly UX. What's next for Just Replay improving accuracy with more joints expand activity library integrate wearable data helping real users <div