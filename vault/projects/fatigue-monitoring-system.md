---
slug: "fatigue-monitoring-system"
url: "https://devpost.com/software/fatigue-monitoring-system"
title: "ProxErgo: Fatigue Monitor"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 705
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/scientific_research"
  - "user/developer"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ProxErgo: Fatigue Monitor

> ProxErgo, a privacy-first smart monitor using front-facing webcams to prevent poor ergonomics. Here, we turn clinical "surgery stories" into real-time digital health for the office athlete.

[Devpost](https://devpost.com/software/fatigue-monitoring-system) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[structural_withholding]] [[vision_ocr]]
**domain** [[accessibility]] [[health_clinical]] [[labor_employment]] [[scientific_research]]
**user** [[developer]] [[patient_family]]
**substrate** [[geospatial]] [[video_visual]]

**stack** mediapipe, opencv, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fatigue monitoring system
- faq

## Body

App Page App Page - in use Analytics Board Monitor Inspiration Upper crossed syndrome (UCS) is a public health issue across the globe especially prevalent among adults in the workforce. Many individuals in this group are involved in intensive computer usage both for work and for leisure. These people are at high risk of UCS-related neck pain (55-69%) and shoulder pain (15-52%) (Russin et al. 2026). The review has also pointed out the reduction in working efficiency in UCS patients including disability and decreased productivity. UCS affects a large percentage of the global population and has negative impacts on the workers as well as enterprises. Therefore it motivated us to make ProxErgo, which is designed to assist UCS prevention and alleviation. What it does ProxErgo is a real-time, privacy-first ergonomic guardian. Using only a standard front-facing webcam, it monitors the "Office Athlete" for signs of musculoskeletal strain and cognitive fatigue. Postural Analysis: Detects Forward Head Posture (FHP) and shoulder asymmetry using biomechanical proxy markers. Fatigue Tracking: Utilizes PERCLOS (Percentage of Eye Closure) and Postural Sway analysis to identify when a user is becoming "neuromuscularly exhausted." Proactive Intervention: Instead of passive data collection, it provides real-time "Bio-Feedback," suggesting specific corrective exercises (like chin tucks) before pain sets in. How we built it The Engine: Built on Python using MediaPipe for high-fidelity landmark extraction and OpenCV for real-time video processing. The Clinical Logic: Our Biomedical Lead mapped 3D anatomical landmarks to 2D webcam coordinates, establishing Craniovertebral Angle (CVA) proxies based on peer-reviewed literature. The Intelligence: We developed a hybrid model. A XGBoost model to identify posture states, while a Temporal Analysis module tracks "sway" and "blink rates" to predict fatigue. Parameters were tuned based on scientific research. The Interface: A Streamlit dashboard that visualizes a user's "Health Score" without storing raw video, ensuring HIPAA-compliant privacy standards. Challenges we ran into The Perspective Problem: Standard ergonomic models require a side-view camera. We had to mathematically engineer "Front-View Proxies" that remain accurate despite different camera angles. Environmental Noise: Webcam "jitter" can trigger false alerts. We solved this by implementing a One-Euro Filter to smooth coordinate movement without adding lag. Accomplishments that we're proud of Zero-Hardware Solution: We successfully moved health monitoring from expensive medical labs to a standard laptop. Privacy-First Design: Our system never records or uploads video; it only "sees" numbers, making it safe for corporate and medical environments. What we learned Interdisciplinary Communication: We learned how to translate "Anatomical Strain" into "Mathematical Ratios", a vital skill for the future of MedTech. Team Science Approach: We bridge the gap between Data Science and Clinical Research to study spinal biomechanics with computer vision. What's next for Fatigue Monitoring System Mobile Integration: Porting the logic to iOS/Android to monitor posture while using smartphones (the primary cause of "Text Neck"). FAQ 1. Can ProxErgo run in the background while I work? Yes. ProxErgo is designed to be a "set and forget" utility. Once the initial Calibration is complete, the engine runs as a lightweight background process. You can minimize the dashboard, and the system will only notify you via a gentle desktop alert if your posture or fatigue levels cross the "Clinical Danger Zone" defined by our BME lead. 2. Is my video data safe? Absolutely. This is a core pillar of our "Privacy-By-Design" philosophy: Local Processing: All video frames are processed in real-time on your local RAM and are immediately discarded. No Cloud Uploads: Raw video never leaves your device. Landmark-Only Storage: If you choose to save your progress, the system only stores mathematical coordinates (skeleton points), which are useless to anyone without our specific biomechanical decoder. 3. Does the app work if I wear glasses or a headset, or clothes? Yes. Our use of the MediaPipe Face Mesh and Pose models is robust against common office accessories, just remember to calibrate your posture to fit the best of you. 4. Why does the app focus on the front view instead of the side? While side-view monitoring is the "gold standard" in labs, it is impractical for real-world offices. No one wants to set up a second tripod next to their desk. By engineering Front-Facing Proxies , we’ve made professional ergonomic monitoring accessible to anyone with a standard laptop. <div