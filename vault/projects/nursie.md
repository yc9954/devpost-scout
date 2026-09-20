---
slug: "nursie"
url: "https://devpost.com/software/nursie"
title: "Nursie"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 746
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/educator_student"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Nursie

> Nursie: The Invisible Safety Net — Dignity-First AI Surveillance for the Next Generation of Care.

[Devpost](https://devpost.com/software/nursie) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[education]] [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[educator_student]] [[general_public]] [[patient_family]]
**substrate** [[sensor_telemetry]] [[transcript_audio]] [[video_visual]]

**stack** c++, elevenlabs, fastapi, flask, javascript, mongodb, python, react, ros2

## How they structured the write-up

- tl;dr
- design principles
- system overview
- backend + dashboard
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nursie

## Body

Dashboard Building an “AI Nurse” for Long-Term Care: mmWave Fall Detection + Sensor Fusion + Voice Support Falls among older adults are a major public-health issue in Canada. They’re a leading cause of injury-related hospitalizations and deaths for people 65+, and the trend is moving in the wrong direction. National surveillance data shows fall-related hospitalizations for older adults rising 47% between 2008 and 2019 (from 49,152 to 72,392 ). :contentReference[oaicite:0]{index=0} On the mortality side, the burden is also climbing (e.g., 5,581 older adults died due to a fall in 2019 , and deaths due to falls increased strongly in recent years). In Québec long-term care settings (CHSLD), the problem is often amplified by two realities: Falls can happen unwitnessed (especially at night). Staffing shortages can delay assistance. Those delays matter. When someone remains on the floor for a prolonged period (“long lie”), the complications can be severe—hypothermia, dehydration, tissue damage, rhabdomyolysis, pressure injuries, kidney failure, and more. This post explains our prototype system: an AI nurse assistant that combines privacy-preserving room sensing , wearable vital signs , and a voice interface , all connected through a local on-site network. TL;DR We’re building an on-premises assistant for long-term care that: Detects falls using mmWave radar + a floor vibration mat Tracks context with door open + presence/occupancy Monitors vital signs via a smartwatch Sends immediate alerts (phone call + dashboard) to staff on emergencies Builds a resident profile over time in MongoDB to flag unusual behavior (e.g., leaving the apartment at night) Provides a voice interface for residents (questions, appointment reminders, medication prompts) Design Principles 1) Fast, reliable detection > fancy features If a fall is detected late, the system fails its core mission. Our priority is high confidence + fast alerting . 2) Sensor redundancy to reduce false positives No single sensor is perfect: Radar can confuse some edge cases (e.g., abrupt sitting, blankets, furniture occlusion). Vibration sensors can trigger on dropped objects. Wearables can be off-wrist or missing. So we fuse signals to improve confidence. 3) Privacy by architecture We keep everything inside the facility’s LAN : No “always-streaming camera” No raw data leaving the network by default Local processing wherever possible System Overview At a high level: * Room module Ipad * : the “AI nurse” endpoint in the resident room for voice interaction. mmWave radar : continuous position/activity sensing + fall detection Floor vibration mat (prototype currently cardboard): detects “impact/vibration signature” when something hits the floor ESP32 sensor nodes running FreeRTOS : ESP32 #1: vibration mat sensor → ROS 2 messages ESP32 #2: door magnetic sensor + PIR presence sensor → ROS 2 messages Wearable (smartwatch) : heart rate monitoring (vital signs) Local network : our own router flashed with OpenWRT , hosting a private LAN for all devices Backend + Dashboard Emergency alert workflow: call nurse + dashboard alert Resident behavior profile + anomaly detection stored in MongoDB AI workflow (Gemini + ElevenLabs + webhooks) ElevenLabs posts send_event webhooks to the backend over HTTPS Gemini triages transcripts into structured priority / intent / summary The backend persists triage + events in MongoDB Triggers escalations when critical Challenges we ran into Integrating mmWave radar was difficult due to environmental noise; distinguishing a human heartbeat from a moving curtain required careful signal-processing tuning. We had to solve “Connection Errors” in our live telemetry stream so the dashboard stays updated even when local Wi-Fi fluctuates. Accomplishments that we're proud of A system that is compliant by design with Québec’s privacy framework (Law 25 / Act respecting the protection of personal information in the private sector).[^5] A local AI agent that can differentiate between a “soft landing” on a bed and a critical fall on the floor. Bridging the gap between hardware ( LiDAR, Radar ) and a professional-grade nurse dashboard that prioritizes alerts. What we learned The importance of Edge Computing —processing data where it’s collected to maximize privacy and speed . As mechanical and software engineering students, we learned that the best medical tech is “invisible” : it provides the most protection when it requires the least intervention from the user. We gained deeper insight into the ethical implications of AI in geriatric care. What's next for Nursie Refine our Apple Watch integration as a secondary “gold-standard” validator for high-risk patients. Explore predictive models that analyze gait patterns to estimate fall risk before the first fall occurs. Scale the hardware into a sleek, medical-grade casing that can be deployed across CHSLDs throughout Québec. <div