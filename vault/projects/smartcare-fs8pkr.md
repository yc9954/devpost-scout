---
slug: "smartcare-fs8pkr"
url: "https://devpost.com/software/smartcare-fs8pkr"
title: "SmartCare"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 579
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# SmartCare

> A vital signs monitoring platform using Explainable AI to instantly assess patient health risks and prioritize care for caregivers.

[Devpost](https://devpost.com/software/smartcare-fs8pkr) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]] [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[developer]] [[general_public]] [[patient_family]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** fastapi, framer-motion, next.js, postgresql, prisma, python, react, tailwind-css

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for smartcare

## Body

SmartCare Landing Page - Simple access to both patient and caregiver portals. Secure Login - Pre-configured demo accounts for quick access. Patient Dashboard - Personal health trends and recent AI assessments. Patient Interface - Easy-to-use form for logging daily vital signs. Instant AI Assessment - Dynamic Explainable AI insights based on submitted vitals. Caregiver Dashboard: Centralized dashboard showing patients prioritizing by critical AI risk alerts. Caregiver Interface - Easily register and add new patients to the system. Patient Details - AI risk breakdown and visualized health trends. Historical Health Records and Caregiver Observation Notes. Export Medical Report - Generate professional PDF summaries for doctors. Demo Live : https://smartcare-phi.vercel.app/ Inspiration In many healthcare settings, caregivers are overwhelmed with monitoring multiple patients simultaneously. Often, it's difficult to quickly identify which patient's condition is deteriorating and why. I wanted to build a system that not only collects health data but actively assists caregivers by prioritizing patients based on risk, while simultaneously empowering patients to understand their own health through Explainable AI (XAI). What it does SmartCare is a bilingual (English/Thai) decision support system designed for remote patient monitoring. For Patients: It offers an intuitive dashboard to log daily vital signs (temperature, heart rate, blood pressure, and symptoms). An AI model instantly assesses their health risk (Low, Medium, High) and provides dynamic, human-readable insights explaining exactly why that risk level was assigned. For Caregivers: It provides a centralized dashboard that automatically ranks patients by their current risk level. Caregivers can view detailed trends, add observation notes, and generate professional PDF medical reports to share with doctors. How I built it As a solo developer, I built SmartCare using a modern microservices architecture: Frontend & Core API: Built with Next.js (App Router) and React 19. I used Tailwind CSS for styling and Framer Motion for smooth UI animations to ensure a highly accessible experience. Database: PostgreSQL managed via Prisma ORM. AI Service: The risk assessment engine operates as a separate Python microservice using FastAPI. It features a Random Forest Classifier trained with scikit-learn. The service includes a custom Explainable AI (XAI) module to translate model outputs into clear, actionable insights in both English and Thai. Reporting: Implemented custom print layouts using react-to-print for exporting professional clinical data. Challenges I ran into The biggest challenge was designing an AI system that wasn't just a "black box." In healthcare, knowing why an AI made a decision is crucial. Developing the dynamic rule-based XAI engine to accurately map vital signs to readable insights—and ensuring accurate bilingual translations—required meticulous logic tuning. Furthermore, maintaining an extremely simple UI/UX for elderly patients while handling complex background data processing was a persistent design challenge. Accomplishments that I'm proud of I am incredibly proud of successfully designing and developing a complete, end-to-end ecosystem alone. Bridging a responsive Next.js frontend with a robust Python AI microservice, and integrating Explainable AI that directly scales down medical jargon into actionable patient feedback, are technical milestones I am very proud of. What I learned Building SmartCare significantly deepened my knowledge in architecting multi-language (Next.js + Python) systems. I learned practical ways to implement Explainable AI in consumer-facing applications, and improved my skills in UI/UX design focusing on accessibility and data visualization for non-technical users. What's next for SmartCare I plan to integrate real-time API connections with wearable devices (e.g., Apple Watch, Fitbit) to automate vital sign logging. Additionally, I aim to expand the ML model from immediate classification to predictive forecasting for long-term health trends. <div