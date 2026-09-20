---
slug: "smartpt-k1d5h0"
url: "https://devpost.com/software/smartpt-k1d5h0"
title: "SmartPT"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 344
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
---

# SmartPT

> Bringing clinic-grade physical therapy feedback to patients anywhere using pose estimation.

[Devpost](https://devpost.com/software/smartpt-k1d5h0) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[developer_tools]] [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[patient_family]]
**substrate** [[sensor_telemetry]]

**stack** c++, embedded, flutter, overshoot, python, seeed-studio, woodwide

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smartpt

## Body

rendering user in 3D - RTMpose demonstration Inspiration What's worse than getting a torn ACL? Having to travel to the doctor's office for a PT appointment on a bad knee. We're helping patients recover faster and safer by giving them a more detailed level of feedback at home than they would receive in a clinic :) What it does SmartPT analyzes people's form and recovery from injuries via precision pose tracking and gives detailed analysis, providing doctors access to more quantifiable metrics from anywhere in the world How we built it Precision and reliability were non-negotiable. Our platform fuses 3D pose estimation and physical IMU sensor data to accurately determine position and angle measurements. As we record, we concurrently pass our data to Overshoot to segment the sections of the video where an exercise is being performed to identify where processing must be focused. Computer vision data is inherently messy, so we use Kalman filtering to fuse with smoother IMU data and Wood Wide AI's anomaly detection to drastically decrease visual jitter and capture stronger trends in our users movement. At the same time, Overshoot provides real-time therapy advice so the patient has a more interactive experience. Challenges we ran into Aligning noisy sensor data with CV outputs in real time was a huge challenge, and we spent hours making sure that our model reliably segments gait phases across different users, while still being able to provide strong individualized metrics. Accomplishments that we're proud of Refactored Overshoot to work with Python and Flutter instead of its native JS SDK. We're immensely proud of being able to create hardware and software that works in parallel, and we're confident in the mathematical foundations that back our modeling. What we learned Multi-modal fusion (CV + sensors) dramatically improves reliability, clinicians value interpretable metrics over raw accuracy, and real-time feedback requires careful tradeoffs between latency and model complexity. What's next for SmartPT Expand to more injury types, validate metrics with clinicians, add longitudinal progress tracking, and train personalized models using Wood Wide to adapt therapy over time. <div