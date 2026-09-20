---
slug: "stepsure"
url: "https://devpost.com/software/stepsure"
title: "StepSure"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 781
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/sensor_fusion"
  - "domain/accessibility"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "user/clinician"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# StepSure

> Your AI Physiotherapist for Gait Improvement in your pocket

[Devpost](https://devpost.com/software/stepsure) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[sensor_fusion]]
  <sub>weak: cross_origin_web</sub>
**domain** [[accessibility]] [[elder_child_care]] [[health_clinical]] [[mental_health]] [[scientific_research]]
**user** [[clinician]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[video_visual]]
  <sub>weak: financial_record</sub>

**stack** camera, dart, flutter, gemini, google, google-web-speech-api, machine-learning

## How they structured the write-up

- inspiration
- about the project
- how we built it
- what we learned
- challenges we faced
- impact vision
- built with
- future improvements
- why this matters

## Body

Main Page Problem Statement Significance Snapshots System Architecture Core Features Main Feature Uniqueness Benefits Literature Survey StepSure — AI-Powered Clinical Gait Analysis from Smartphone Video Inspiration Gait is often called the “sixth vital sign” in clinical medicine. Subtle changes in walking patterns can indicate: Early neurological disorders Fall risk in elderly individuals Musculoskeletal imbalances Rehabilitation progress after injury Yet real gait analysis typically requires: Expensive motion capture labs Force plates Marker-based tracking systems Clinical supervision This creates a massive accessibility gap. We asked a simple question: What if a smartphone camera could deliver clinically meaningful gait analysis anywhere? That question became StepSure . About the Project StepSure is a cross-platform Flutter application that performs AI-powered gait analysis using smartphone video . It uses pose estimation and biomechanical signal processing to extract: Knee joint angles Cadence (steps per minute) Step symmetry Stability metrics Risk classification It then generates a full clinical-style PDF report. The goal is to bridge the gap between: Lab-based biomechanical motion analysis At-home accessible screening How We Built It 1. Pose Detection Pipeline We use on-device pose estimation to extract 33 body landmarks per frame. Each frame is processed through a custom GaitAnalysisService . For every frame: Knee angles are calculated using vector mathematics Hip alignment is analyzed Step detection logic is applied Stability and symmetry metrics are accumulated Knee angle calculation: $$ \theta = \cos^{-1}\left(\frac{\vec{AB} \cdot \vec{BC}}{|\vec{AB}||\vec{BC}|}\right) $$ Where: A = hip B = knee C = ankle This converts raw pose data into meaningful biomechanical measurements. 2. Medically Realistic Step Detection The original implementation used naive threshold logic: if (lk > 160 || rk > 160) This caused cadence values to be inflated 10–30×. We replaced it with a rising-edge state machine using 20° hysteresis : Arm state at < 140° Fire step at > 160° Per-leg independent detection Debounced transitions This produces clinically realistic cadence values. 3. Cross-Platform Camera Handling Mobile camera formats vary across platforms: Android → multi-plane YUV (converted to NV21) iOS → single-plane BGRA8888 We implemented: Platform detection Correct byte-plane handling Dynamic sensor orientation reading Rotation-aware processing Without this, pose estimation accuracy suffered significantly. 4. Skeleton Coordinate Transformation We implemented rotation-aware coordinate transforms: Axis swap for 90°/270° Inversion logic for mirrored feeds Correct scaling to preview space This ensures the skeleton aligns properly with the human body on screen. 5. Video-Based Offline Analysis Users can upload pre-recorded walking videos. Pipeline: Extract frames at 5 fps Run pose detection per frame Process frames via GaitAnalysisService Compute session metrics Generate risk analysis Safeguards include: Exception handling for short videos Minimum pose detection requirement (<5 rejected) Non-sequential frame optimization 6. AI-Powered Clinical Report Generation We implemented a full A4 PDF report including: Risk score banner 6-row color-coded metrics table AI summary section Detected abnormalities Exercise recommendations Risk classification Medical disclaimer footer Generated using: Uint8List generateSessionReport(session, report) The report can be exported via the system share sheet. What We Learned Technical Lessons Camera formats differ drastically across platforms Pose estimation is noisy, filtering is critical Frame extraction requires careful UI handling Clinical metrics require validated thresholds Coordinate transforms directly affect UX accuracy ML Lessons Naive thresholding produces unreliable biomechanics Temporal logic matters more than single-frame detection Real-world sensor data requires validation checks Clinical credibility demands explainable metrics Product Lessons Healthcare UX must feel structured and trustworthy Users want interpretation, not raw numbers Reports must look clinically formal Challenges We Faced 🔴 Inflated Cadence Naive knee-angle triggers fired multiple times per step. Solution: Rising-edge hysteresis state machine. 🔴 Skeleton Rendering Issues Landmarks appeared mirrored or rotated. Solution: Rotation-aware coordinate transformation layer. 🔴 Cross-Platform Camera Differences Android and iOS camera formats differed significantly. Solution: Platform-aware image format handling. 🔴 Video Frame Extraction Capturing frames without UI flicker was complex. Solution: Hidden RepaintBoundary mounted off-screen. 🔴 Clinical Interpretation Raw numbers lacked context. Solution: Risk scoring + structured AI summary. Impact Vision StepSure can enable: Early neurological screening Elderly fall risk detection Post-surgery rehabilitation monitoring Rural telemedicine support Remote physiotherapy assessment All using only a smartphone. Built With Languages Dart Frameworks Flutter Machine Learning On-device pose estimation Backend Supabase (session and video storage) Platform APIs Camera Video Player RenderRepaintBoundary PDF generation System share sheet Architecture Modular feature-based structure GaitAnalysisService (biomechanics core) VideoAnalysisService (offline pipeline) PDFGenerator (clinical reporting engine) Upload and results state management Future Improvements Kalman filtering for temporal smoothing Formal symmetry index modeling Fall-risk ML classifier Longitudinal tracking dashboard Clinician portal Clinical trial validation Why This Matters Gait changes often precede visible symptoms in neurological disorders. If we can measure walking objectively using only a phone camera, we reduce barriers to early screening globally. StepSure is not just a step counter. It is a step toward accessible digital biomechanics. <div