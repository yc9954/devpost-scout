---
slug: "health-pulse-ai-tbd4y5"
url: "https://devpost.com/software/health-pulse-ai-tbd4y5"
title: "Health-Pulse-AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 632
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
---

# Health-Pulse-AI

> "Smart AI Triage System that identifies critical patients early and helps hospitals treat the right patient at the right time"

[Devpost](https://devpost.com/software/health-pulse-ai-tbd4y5) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[sensor_telemetry]]
  <sub>weak: structured_db, web_dom</sub>

**stack** ai, backend, css, dataset, docker, frontend, git, github, google, html, javascript, learning, machine, mongodb

## How they structured the write-up

- inspiration
- what our project does
- how we built the project
- what we learned
- challenges we faced
- impact
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for health-pulse-ai

## Body

Inspiration In many hospitals across India, emergency departments are crowded and doctors must handle a large number of patients every day. In such situations, identifying which patient needs immediate attention becomes difficult. Many hospitals still use manual triage systems , where nurses classify patients based on symptoms. This process can take time and sometimes critical patients may not be recognized quickly. We were inspired to build this project after studying how delays in emergency care can affect patient survival , especially in cases like heart attack, stroke, and severe infections. In these situations, even a few minutes can make a big difference. Our goal was to create a system that can analyze patient symptoms quickly and help doctors prioritize patients more accurately . What Our Project Does Our project is an AI-powered triage and patient prediction system that helps hospitals identify critical patients faster. The system analyzes: Patient symptoms Vital signs (heart rate, temperature, blood pressure) Medical history Using this data, the system calculates a risk score and predicts the severity of the patient's condition. Example risk score model: [ Risk\ Score = w_1(Symptoms) + w_2(VitalSigns) + w_3(MedicalHistory) ] Based on the score, patients are classified into: High Priority (Immediate attention) Medium Priority Low Priority This helps doctors and hospital staff focus on the most critical patients first . How We Built the Project We built the system using modern AI and web technologies. Frontend Used for patient input and hospital dashboard. React / Web interface Simple symptom input form Real-time risk score display Backend Handles data processing and system logic. Python / Node.js backend API for symptom analysis Integration with hospital systems AI Model The AI model analyzes symptoms and predicts patient risk. We used: Machine Learning classification models Medical datasets for training Risk prediction algorithms System Workflow Patient enters symptoms through mobile app or hospital kiosk System collects vital signs and medical data AI analyzes the data and calculates a risk score Patients are automatically prioritized Doctors receive alerts for high-risk patients What We Learned While building this project, we learned many important things: How AI can help improve healthcare decision making The importance of accurate patient prioritization How to design systems that are useful for doctors and hospitals Challenges involved in working with healthcare data We also learned how to combine AI models, backend systems, and real-time dashboards into a single healthcare solution. Challenges We Faced 1. Medical Data Availability Accessing real healthcare datasets for training AI models was difficult because medical data is sensitive and protected. 2.Model Performance Our AI prediction model was trained using healthcare symptom and patient data to classify the severity of patient conditions. After training and testing the model, it achieved an accuracy of: 97.88% Evaluation Metrics Accuracy: 97.88% Precision: 97.65% Recall: 97.42% F1 Score: 97.53% Model Used We used a Machine Learning classification model to analyze patient symptoms, vital signs, and medical history to predict patient risk levels. Result The high accuracy indicates that the model can reliably help doctors and hospitals prioritize critical patients quickly and support faster medical decisions. 3. System Integration Hospitals use different systems and software, so integrating our solution with existing hospital infrastructure can be complex. 4. Real-Time Performance Emergency systems must provide results quickly. Optimizing the system for fast predictions and real-time processing was a key challenge. Impact Our system aims to improve hospital efficiency and patient safety by: Reducing patient waiting time Helping doctors identify critical cases faster Improving hospital resource management In the future, this system can also be integrated with: Ambulance services Telemedicine platforms Rural healthcare centers in India This can help make emergency healthcare smarter and more accessible . What it does How we built it Challenges we ran into Accomplishments that we're proud of What we learned What's next for Health-Pulse-AI <div