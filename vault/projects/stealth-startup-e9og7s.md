---
slug: "stealth-startup-e9og7s"
url: "https://devpost.com/software/stealth-startup-e9og7s"
title: "Swish"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 422
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/legal_justice"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Swish

> Swish turns your laptop into an elite AI shooting coach. We use Overshoot, LiveKit, and Gemini to analyze mechanics and provide real-time voice fixes—no smart hoop required.

[Devpost](https://devpost.com/software/stealth-startup-e9og7s) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[legal_justice]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** gemini, livekit, next.js, overshoot, python, react, tailwindcss, tensorflow, three.js, typescript, webspeechapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stealth startup

## Body

Starting Page Perfomance Analysis Shooting Position Selection Shooting Drill Inspiration Through our previous involvement in playing basketball, we found that learning proper shooting form was difficult and often required a personal coach to ensure that bad habits are not learned. What it does As a result, we wanted to democratize the learning of proper shooting habits in basketball by creating an AI-powered form coach. Swish achieves this by allowing users to select from where they want to run simulated shots with their form. The application then proceeds to track the user's joints and obtains several biometric data like elbow pitch angle, arm velocity, and user orientation, which allows us to create a 3D reconstruction and simulate whether the user's shot would go in on an actual court. How we built it On the front-end we use React and TailwindCSS and on the backend we utilize Next.js. We also utilize an array of AI-powered tools to ensure that the data presented to the user is accurate. In providing feedback to the user through their shot video, we use overshoot to analyze the video and provide personalized feedback. Additionally, realtime, we utilize LiveKit as the voice agent to provide feedback to the user. Challenges we ran into One central challenge to our produce was the detection of joints in a way that can easily run in a browser. We first attempted to utilize MediaPipe, however, we ran into several issues regarding the frame-per-second of the model--it was unable to track the joint effectively enough to get velocity data. To fix this, we instead utilized a light-weight tensor flow model to that was specifically fine-tuned to run on light-weight devices. As a result, we saw an over 15x increase in joint-detections per-section while retaining accuracy. Another challenge we ran into was getting realtime commentary to the user. Traditional methods like that of Google's voice API were unnatural and utilize an LLM model's API would be too slow. As a result, we ended up using LiveKit for realtime coach feedback. Accomplishments that we're proud of 3D reconstruction & simulation based upon joint data Realtime joint detection with Tensorflow Realtime user feedback w/ LiveKit What we learned We learned greatly about utilizing LiveKit agents to add voice-commentary along with integrating Overshoot for live video/image analysis into our project. Additionally, we learned about constructing 3D graphics in the web & running simulations at the same time. What's next for Stealth Startup We are looking to expand this to other sports and activity to further democratize form coaching. <div