---
slug: "healthier-w0baus"
url: "https://devpost.com/software/healthier-w0baus"
title: "Healthier"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 1155
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Healthier

> AI-powered elderly care app. Seniors scan pills/meals and chat with a voice agent. Healthcare providers get dashboards that flag risks early. 3D facility tracking for senior homes.

[Devpost](https://devpost.com/software/healthier-w0baus) · hackathon [[NexHacks]]

## Facets

**mechanism** [[human_in_the_loop]] [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**domain** [[agriculture_food]] [[elder_child_care]] [[health_clinical]] [[mental_health]] [[scientific_research]]
  <sub>weak: disaster_emergency</sub>
**user** [[clinician]] [[patient_family]] [[social_worker]]
**substrate** [[genomic_bio]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** apple-coreml, cerebras, claude, cuda, fastapi, huggingface, infisical, livekit, mediapipe, next.js, overshoot, render, smplrspace, supabase

## How they structured the write-up

- tech stack
- what it does
- how we built it
- challenges we ran into
- accomplishments
- what we learned
- next steps

## Body

Healthier Tech Stack longer form video: https://youtu.be/taJw4XDSlKU As the global population ages, elder care is becoming one of the most critical and under-supported challenges in healthcare. Care happens across two settings: in-clinic stays where clinicians set the plan, and at-home care. Clinicians only see snapshots in the care home, and small misses, including late meds, improper nutrition, and skipped exercises, can compound into avoidable disasters. That’s why we built Healthier: a care continuity layer designed for both in-clinic and at-home care, so clinicians can prescribe and adjust with confidence in the clinic, and patients can rehabilitate with support at home. Tech Stack What it Does 1) Overshoot & LiveKit: Multimodal at-home capture with LiveKit voice, and CV/pose estimation Patients log what actually happened via multimodal check-ins rather than typing. LiveKit-powered WebRTC voice streams audio for automatic speech recognition in structured journal logs with medication, symptom, and adherence context. For exercises, streamed video is analyzed with computer vision and pose estimation via Overshoot and MediaPipe to extract keypoints and joint angles generating form quality assurance and realtime guidance. 2) Real-time adherence telemetry, risk scoring, and triage alerting Healthier maintains a system of record for real-time telemetry across meals, medication logs, exercises, and journal logs, using event-sourced timelines. A plan-vs-behavior engine compares the patients' actions with their caregivers' instructions and computes risk scores and prioritized alerting for cross-setting triage. 3) Live 3D care map and AI chat for natural language plan updates Healthier includes a spatial intelligence layer of the care setting that makes patient status and risk scoring instantly visible through room/area coloring, active alerts, and recent events. Clinicians and caregivers can use an AI chat interface to ask natural language questions and safely modify care plans in place (e.g., adjust medication schedules, change exercise prescriptions, update diet targets, tune alert thresholds). 4) iOS pill guidance with on-device vision and timing guardrails We guide elders through a pill flow that ensures the right pills, the right number, and the right time. The iPhone scans pills using an on‑device model, cross‑checks the prescribed schedule, and explains why a pill is due now vs later (e.g., why a 3pm pill should not be taken at 8pm or out of order). A Claude-based analysis layer translates detections into simple, human‑readable instructions and flags adherence risks for caregivers and clinicians. 5) Live agent assistance for pill intake For elders who prefer a human in the loop, a live agent can guide them step‑by‑step through pill identification, dosage confirmation, and timing, while still recording structured adherence data for clinicians. 6) Exercise view with feedback and progress Exercise is critical for muscle and bone health as people age. The iOS exercise view helps patients follow prescribed movements and capture adherence data, reinforcing clinically proven benefits. Medication Analysis, CUDA/Pytorch Journaling with Voice, Livekit/Overshoot Exercise Tracking, Mediapipe/Cerebras 7) Meal planning and nutrition scoring Patients receive meal plans from their doctor, scan meals, and send results back to the clinician. The system scores meals on gut health, protein, and other recovery signals. Meals are a key window into recovery progress and long‑term health maintenance. 8) Journal + live agent for mental health and cognition Patients can journal and talk to a live agent trained to act as a medical professional and therapist. Regular conversation supports mental dexterity, memory, and emotional wellbeing, helping prevent cognitive decline while keeping clinicians informed. How we built it On‑device pill detection for privacy and low latency : We trained a custom YOLOv8 object detection model for pill recognition using a purpose‑built dataset of pill images sourced from Google. The dataset was annotated using Nano Banana Pro, resulting in ~700 labeled images split across training and test sets. Model training was performed on an NVIDIA A100 GPU. The trained model was then converted to Apple’s Core ML (.mlmodel) format and runs fully on‑device on iPhone, enabling low‑latency, privacy‑preserving pill detection without cloud inference. This powers the product requirement: right pill, right count, right time, with clear explanations when a pill is out of order or taken too late. Intuitive Voice Interface with LiveKit : Healthier uses LiveKit for low-latency WebRTC voice experiences so older adults can capture daily check-ins by speaking naturally instead of typing. Voice sessions produce structured journal logs and caregiver-ready summaries, reducing documentation overhead while preserving the signal clinicians need for follow-up. Multimodal Capture + Pose Estimation for Exercises with Overshoot: Healthier uses Overshoot to run real-time computer vision inference over streamed video for exercise form and symmetry analysis (and pill/medication vision workflows where applicable). This turns raw video into actionable quality signals (form QA, asymmetry deltas, safety flags) that clinicians can review during in-clinic visits and that caregivers can monitor in at-home settings. Realtime Adherence Telemetry and Risk Scoring: Healthier contains a system of record for multimodal telemetry (meals, exercises, medication logs, journal logs) and plan artifacts. Clinicians author structured plans in the web dashboard (med schedules, prescribed exercises, diet targets) and time-specific reminders are sent to the patients' phones at home via local notifications. A plan-vs-behavior engine compares the patients' actions with their caregivers' instructions and computes risk scores and prioritized alerting for cross-setting triage. Challenges we ran into Natural voice interaction: Fine-tuning turn-taking and background noise handling so LiveKit WebRTC voice check-ins feel natural for older adults. Real-time multimodal streaming: Keeping end-to-end latency low while streaming video for exercises and running Overshoot computer vision + pose estimation inference without dropped frames, drift, or UI freezes. Context management: Daily check-ins can get long. We built a summarization pipeline to convert raw sessions into structured journal logs and caregiver-ready summaries while staying within LLM context limits. Accomplishments Shipped a LiveKit-powered WebRTC voice experience that produces structured journal logs and caregiver-ready summaries from natural speech. Built an exercise workflow that streams video to Overshoot for pose estimation and returns actionable quality signals like form QA, asymmetry deltas, and safety flags. Implemented a system of record for real-time telemetry (meals, medication logs, exercises, journal logs) plus a plan-vs-behavior engine that computes adherence deltas, risk scoring, and prioritized alerting for cross-setting triage. What We Learned Multimodal capture is only useful if it lands in a clean schema; without structured telemetry, trends, adherence, and triage fall apart. Risk scoring and alerting must be explainable and grounded in concrete adherence deltas, otherwise clinicians and caregivers won’t trust it. Agentic AI works best when it’s context-aware but constrained to safe tools and clear actions Next Steps Care transition / discharge planning for home rehab : Generate a clear, structured transition plan from in-clinic to at-home care (exercises, diet targets, medication schedules, follow-ups) and keep it updated as plan-vs-behavior deltas change. Exercise progression agent: Based on form QA, asymmetry deltas, and safety flags from Overshoot pose estimation , recommend when to regress/progress exercises for clinician approval. Model evaluation + feedback loop: Build a clinician/caregiver feedback signal (approve/dismiss alerts, correct summaries) to improve triage quality over time (without brittle “reinforcement learning” claims unless implemented). <div