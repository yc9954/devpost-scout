---
slug: "unpark-fjwrd4"
url: "https://devpost.com/software/unpark-fjwrd4"
title: "UnPark"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 743
team_size: 0
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/government_staff"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# UnPark

> AI-Powered Real-Time Parking Violation Detection & Automated Reporting System

[Devpost](https://devpost.com/software/unpark-fjwrd4) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[civic_government]] [[finance_payments]] [[transportation]]
**user** [[government_staff]]
**substrate** [[structured_db]] [[video_visual]]

**stack** augmented-reality, css, deepsort, fastapi, javascript, mongodb, natural-language-processing, ocr, opencv, python, react, restapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for unpark

## Body

Inspiration Growing up in India, I’ve constantly experienced the frustration of illegal roadside parking. Cars and bikes are often parked on sidewalks, forcing pedestrians to walk on the road. Emergency lanes get blocked. What should be a simple walk or drive turns into daily chaos. In busy markets, malls, and commercial areas, parking rules exist — but enforcement is inconsistent. Security guards manually monitor spaces, which is inefficient and often ineffective. I realized this isn’t just an inconvenience; it directly affects safety, accessibility, and urban discipline. Why should pedestrians adjust for poorly parked vehicles instead of the system preventing it in the first place? That question inspired me to build an automated, intelligent parking surveillance system — one that detects violations in real time, generates evidence, and brings accountability without requiring constant human supervision. I wanted to create a solution that addresses a problem I see every single day — not just a technical challenge, but a real societal issue. What it does Detects vehicles using YOLO. Tracks them across frames using multi-object tracking. Assigns an urgency score based on time, location, and vehicle type. Uses OCR (ANPR-ready) to extract number plate details. Stores violation data and evidence clips in MongoDB. Uses NLP to intelligently interpret violation data, generate context-aware summaries, turn violation data into context-aware summaries and alert messages tailored to urgency levels (low, medium, high). Conceptually *integrates AR to overlay vehicle and violation details directly onto live camera feeds. * How we built it Used YOLO (You Only Look Once) for real-time vehicle detection. Integrated DeepSORT tracking to monitor vehicle movement across frames. IoU=(Area(B_pred ​∪ B_gt​))/(Area(B_pred ​∩ B_gt​)​) Designed a logic system to calculate an urgency score for violations based on time, location, and vehicle type. Urgency=αT+βL+γV Where: T = duration of violation L = location severity weight V = vehicle type weight 𝛼,𝛽,𝛾= weighting factors Implemented OCR (ANPR-ready pipeline) to enable automatic number plate recognition. Built a FastAPI backend to handle video uploads and process violations. Stored violation data (vehicle ID, timestamp, clip evidence) in MongoDB. Enabled automated reporting workflows to simulate sending evidence to authorities or management. Designed a conceptual AR-assisted interface for authorities, where officers can view live overlays of vehicle details and violation history directly on camera feeds — transforming passive monitoring into interactive enforcement. Challenges we ran into Real-Time Performance Issues: Processing video while maintaining detection accuracy was computationally intensive. I optimized frame handling and processing logic to balance speed and precision. Tracking Consistency: Maintaining stable vehicle IDs during occlusions and crowded scenes required careful tuning of tracking parameters. OCR Errors : Number plates were sometimes misread due to blur, lighting conditions, angled plates, or similar-looking characters (e.g., 0/O, 1/I). Backend Integration: Connecting AI inference output smoothly with database storage and API responses required structured system design. Data Storage & Evidence Handling: Managing video clips efficiently while storing metadata in MongoDB required designing a clean and scalable storage pipeline. Deployment & Scalability Considerations: I had to think beyond a prototype — considering how the system could scale to multiple cameras and larger environments. What we learned Real-Time Object Detection: I worked extensively with YOLO for vehicle detection and learned how optimizing inference speed, frame processing, and confidence thresholds directly impacts system performance. Multi-Object Tracking: I explored and compared different tracking algorithms: SORT – Fast but less robust during occlusions. DeepSORT – Uses appearance features for better re-identification. ByteTrack – Improves tracking by handling low-confidence detections effectively. OCR Integration: ** I learned how Optical Character Recognition (OCR) can be integrated for Automatic Number Plate Recognition (ANPR), enabling automated vehicle identification and violation history tracking. ** Backend Development with FastAPI: I built a scalable backend to handle video uploads, process inference results, store structured violation data, and expose APIs for future integrations. Database Design & System Architecture: I structured MongoDB collections efficiently to store violation metadata, timestamps, and evidence references while keeping the system scalable. Augmented Reality (AR) for Authorities: I explored how AR could assist authorities by overlaying vehicle details and violation history in real time — turning passive surveillance into interactive enforcement. End-to-End System Thinking: Most importantly, I learned how to connect AI models, tracking systems, OCR, backend services, and databases into one cohesive, deployable pipeline. What's next for UnPark Integrate full Automatic Number Plate Recognition (ANPR) with higher OCR accuracy. Integrate payment or fine management systems for automated penalty workflows. Collaborate with municipalities and commercial complexes. Integrate AR-powered enforcement tools for real-time officer assistance. <div