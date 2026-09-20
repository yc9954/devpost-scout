---
slug: "sentinel-ai-powered-stroke-predictor"
url: "https://devpost.com/software/sentinel-ai-powered-stroke-predictor"
title: "Sentinel: AI Powered Stroke Predictor"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 1151
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Sentinel: AI Powered Stroke Predictor

> Strokes take 7,000,000 lives every single year, making it the second leading cause of death. However, these lives could have been saved if a stroke was treated sooner. That's why we created Sentinel.

[Devpost](https://devpost.com/software/sentinel-ai-powered-stroke-predictor) · hackathon [[Youth Code x AI]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
  <sub>weak: on_device_local, sensor_fusion</sub>
**domain** [[health_clinical]]
  <sub>weak: disaster_emergency, elder_child_care</sub>
  <sub>weak: clinician, patient_family</sub>
**substrate** [[structured_db]] [[video_visual]]
  <sub>weak: sensor_telemetry</sub>

**stack** camera, fastapi, google-gmail-oauth, next.js, postgressql, python, raspberrypi, react, supabase, yolo

## Body

Landing page Dashboard preview Login Card Extra check: Glucose. Hypoglycemia can mimic stroke symptoms, so it's necessary to rule it out! Stroke causation infographic Stroke data Stroke death rate data Stroke deaths to year info Stroke campaign image Number of stroke cases data Inspiration A few years ago, my grandmother had a stroke, and it permanently changed her life. She lost the ability to walk independently, struggles to speak clearly, and has significant vision loss. I still think about what would've happened if she'd gotten treatment even one second sooner. As a result, we decided to build Sentinel. Every minute a stroke goes untreated, millions of brain cells are lost. Early recognition can dramatically improve a person's chances of recovery, but most people don't catch the warning signs until it's already too late. We wanted to build something that catches those signs earlier and gets help moving faster, before the window closes. This wasn't built to fit a hackathon theme. It came out of one of our own families, and we built it hoping it might do for someone else's family what we wished had happened for ours. What it does Sentinel is an AI-powered stroke detection and health monitoring system built to catch the warning signs of a stroke before it's too late. Instead of relying on one symptom or one signal, it combines several at once (facial movement, speech, and health data) to make a more reliable call than any single check could on its own. What's under the hood: Feature Description Real-time facial analysis Powered by a Raspberry Pi Camera Module 3 Speech analysis Catches slurred or abnormal speech patterns Blood glucose tracking Logging and interpretation Emergency email alerts Sent automatically when conditions look dangerous Secure dashboard Camera feeds, health history, speech analysis, past incidents Secure authentication JWT, Google OAuth, and Two-Factor Authentication To be clear: Sentinel isn't trying to replace a doctor or a 911 call. It's meant to notice something's wrong before either of those happens. How we built it Sentinel runs as three systems talking to each other in real time. 1. Hardware: Raspberry Pi 5 A Raspberry Pi 5 with the official Camera Module 3 captures snapshots and sends them to the backend for analysis. For this build, the Pi handles capture, not inference, the actual model runs on our FastAPI server. 2. Backend: FastAPI This is the part doing all the thinking: AI inference, speech analysis, auth, emergency alerting, and the database, all wired together. The YOLOv8 model itself runs here, on one of our own machines, rather than directly on the Pi. 3. Frontend: Next.js Where users actually live: live camera feeds, speech analysis results, blood glucose logs, incident history, account settings. The computer vision piece was the trickiest. We trained a custom YOLOv8 model to pick up on facial asymmetry, one of the classic stroke tells. After 50 epochs (just under 41 minutes on a Tesla T4), it landed at: Metric Score mAP50 (all classes) 99.4% mAP50-95 (all classes) 81.4% Stroke class mAP50 99.4% Inference speed ~1.7ms per image That's fast enough that snapshots from the Pi get analyzed almost instantly once they hit the server. For this version, the Pi sends snapshots over rather than running the model on-device, but moving inference onto the Pi itself is one of the first things we want to tackle for a production version. Speech goes through Whisper plus some extra audio feature extraction to catch slurring. Put the vision, speech, and health data together, and you get something a lot more trustworthy than any one of them alone. Supabase handles the data layer: users, incident history, auth. We layered in JWT, Google OAuth, Two-Factor Authentication, and automated emergency emails on top of that. Challenges we ran into Getting the Pi, backend, AI models, database, and frontend all talking to each other reliably while handling live video, speech, auth, and emergency alerts at the same time was the hardest part by a wide margin. We ran into plenty of small failures along the way that only showed up once everything was running together. Running multiple models also meant constantly trading off speed against accuracy. We didn't want a system that was right but too slow to matter, or fast but wrong often enough to be dangerous. And because stroke detection is serious territory, we were careful the whole way through to frame Sentinel as an early warning system, not a diagnosis. The goal was always to get someone to call for help sooner, never to replace the people who actually treat strokes. Accomplishments that we're proud of We're extremely proud that we were able to create an app in a week that can actually help people and save lives. Additionally, we're proud that we were able to collaborate as a team and build complex systems! Live Raspberry Pi camera streaming AI-powered facial analysis: 99.4% mAP50 , ~1.7ms inference time per frame Speech analysis using Whisper Blood glucose tracking Emergency email notifications Secure authentication with JWT, Google OAuth, and Two-Factor Authentication A dashboard that actually tells you what happened and when However, what makes us most proud isn't even on that list: It's that this came from a real experience, and not something we picked to win a prize or hackathon. What we learned Real-time healthcare tech is a lot harder than it looks from the outside. Things that sound simple on paper, like "just send an alert email," turn into actual design problems once you think about what needs to be in that email and why. We also learned that no single signal tells the whole story. Stroke symptoms don't look the same on everyone, which is exactly why combining face, speech, and health data matters more than nailing any one of them perfectly. We also learned that building something tied to a real person you care about feels completely different and is significantly more engaging than creating something just to win money. What's next for Sentinel We're just getting started and have a lot more ideas as to how we can build onto the project and grow it. However, hardware isn't cheap which is where a good chunk of money would go if we won. Near term: moving model inference onto the Raspberry Pi itself instead of a separate server, more data, more real-world testing, sharper detection across a wider range of symptoms, and a UI that matches how polished the backend already is. Long term: wearable integration, caregiver dashboards, and eventually a direct line into emergency response systems where it makes sense. The end goal is simple: an affordable, accessible stroke warning system that families can actually use at home, every day, without a learning curve. Sentinel started as a hackathon project. To us it's something closer to a promise: if this helps even one person notice the signs a little sooner, it was worth every hour we put into it. <div