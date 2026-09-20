---
slug: "safesign-ai-gesture-based-patient-assistance-system"
url: "https://devpost.com/software/safesign-ai-gesture-based-patient-assistance-system"
title: "SafeSign – AI Gesture Based Patient Assistance System"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 866
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/video_visual"
---

# SafeSign – AI Gesture Based Patient Assistance System

> SafeSign uses computer vision to understand gestures, facial expressions, and body movements to detect when a patient needs help.

[Devpost](https://devpost.com/software/safesign-ai-gesture-based-patient-assistance-system) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[video_visual]]
  <sub>weak: document_pdf, medical_record, web_dom</sub>

**stack** ai, css, cv, flask, html, javascript, mediapipe, ml, numpy, opencv, python, webrtc

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for safesign – ai gesture based patient assistance system

## Body

Secure multi-role login for admins, doctors, nurses, and family to access the SafeSign monitoring system. SafeSign Admin Dashboard – Real-time patient monitoring, camera feed, system health, and vital statistics overview. Central control panel showing patient status, quick administrative actions, and real-time system activity. Patient monitoring interface displaying health status, vitals, and quick communication options for caregivers. Role-based access control for doctors, nurses, family members, and system administrators. Configurable system settings including maintenance mode, user registration, data retention, and alert thresholds. Automated reporting system to generate activity, patient, and alert reports for healthcare monitoring. Administrative configuration panel for managing system policies, alert severity, and operational parameters. Real-time physiological monitoring including heart rate, oxygen level, blood pressure, and temperature. Doctor consultation panel for recording diagnoses, prescriptions, and medical notes. Appointment and rounds scheduling system for managing patient consultations and care routines. Digital medical records system for securely storing and managing patient documents. Patient management interface displaying patient status, vitals overview, and quick communication options. Doctor dashboard showing real-time patient vitals, monitoring feed, and active patient list. Nursing station dashboard showing patient priorities, vital summaries, quick response actions, and real-time care alerts. Real-time vital trends and activity timeline keeping family members informed about patient health. Family live monitoring interface showing patient camera feed and hospital AI monitoring system. Timeline view of patient updates including vitals status, medication events, and doctor rounds. Family portal dashboard providing real-time updates and health status of the patient. Simplified vitals dashboard allowing family members to monitor patient physiological data. Secure remote monitoring feed connecting family members with the hospital patient monitoring system. Direct communication panel enabling families to message or request calls with doctors and nurses. Inspiration Many patients in hospitals, elderly care homes, and post-surgery recovery rooms are often unable to speak or reach help quickly. Elderly patients, disabled individuals, or people recovering from surgery may struggle to press emergency buttons or call nurses. We wanted to build a system that allows patients to communicate without speaking . By using computer vision, SafeSign can understand hand gestures, facial expressions, and body signals and automatically notify caregivers when help is needed. Our goal was to create a simple yet powerful AI solution that improves patient safety and response time in care environments. What it does SafeSign is an AI-powered patient monitoring system that uses a camera and computer vision to detect gestures, facial expressions, and body movements that indicate a patient needs help. The system can detect signals such as: Raised hand requesting assistance Distress facial expressions Unusual body movements Gesture-based help signals Once detected, SafeSign immediately sends an alert to caregivers through a monitoring dashboard, allowing faster response and improving patient care. This solution can be used in: Hospitals Elderly care homes Post-surgery recovery rooms Rehabilitation centers Assisted living facilities How we built it SafeSign was built using computer vision and AI technologies. Main technologies used: Python OpenCV for real-time camera processing MediaPipe for hand and body landmark detection Machine learning logic to interpret gestures and signals Flask / FastAPI for backend services Web dashboard for caregiver alerts Workflow of the system: Camera captures real-time video of the patient Computer vision models detect hands, face, and body landmarks Gesture and expression signals are analyzed If a help signal or distress pattern is detected, an alert is triggered Caregivers receive the notification through a monitoring dashboard The system is designed to be lightweight so it can run on regular laptops or low-cost monitoring systems . Challenges we ran into One of the main challenges was making the system accurately detect gestures and expressions in real time. Some difficulties included: Detecting gestures in different lighting conditions Differentiating between normal movement and distress signals Ensuring the system works in real-time with low latency Handling multiple possible gestures and body signals We addressed these issues by improving detection logic, using reliable landmark detection models, and testing different gesture scenarios. Accomplishments that we're proud of We are proud that SafeSign demonstrates how AI and computer vision can improve healthcare accessibility . Key accomplishments include: Building a real-time AI monitoring prototype Successfully detecting gestures using computer vision Creating a system that can help patients communicate without speaking Designing a solution that can be applied in multiple healthcare environments The project shows how affordable AI solutions can improve patient safety and caregiver response times. What we learned Through this project we learned: How computer vision can be used for real-world healthcare applications The importance of designing AI systems that are simple, reliable, and accessible How to process video streams and detect gestures in real time The challenges involved in building AI systems that interact with human behavior This project also deepened our understanding of AI-powered monitoring systems and human-centered technology design . What's next for SafeSign – AI Gesture Based Patient Assistance System Future improvements for SafeSign include: Adding emotion and facial expression analysis Integrating mobile notifications for caregivers Adding voice detection and emergency keywords Supporting multiple patients with multi-camera monitoring Integrating with hospital management systems Using AI models to predict medical distress patterns Our long-term vision is to develop SafeSign into a smart healthcare assistant that continuously monitors patient well-being and helps caregivers respond faster to critical situations. <div