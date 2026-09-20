---
slug: "dose-ebmo9z"
url: "https://devpost.com/software/dose-ebmo9z"
title: "Dose"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 344
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
---

# Dose

> Modern care in a bottle - IOT medication tracker + web dashboard

[Devpost](https://devpost.com/software/dose-ebmo9z) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[patient_family]] [[researcher]]
**substrate** [[medical_record]] [[sensor_telemetry]]

**stack** 3dprinting, esp32, next.js, pla, react, supabase, tal220

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dose

## Body

Inspiration Medication non-adherence is a silent but massive issue. Studies show that 30–50% of patients with chronic conditions fail to follow their prescribed regimens, and nearly half of study participants intentionally skip doses. The impact is staggering: non-adherence costs the U.S. healthcare system an estimated $100–$300 billion annually in avoidable expenses. Dose was born from the need for a smarter, scalable solution to address this challenge. What it does Dose is a smart medication adherence system that pairs a sensor-enabled pill bottle with an interactive web dashboard. The pill bottle uses a load cell sensor to detect pill movements in real time, producing an accurate, tamper-resistant record of medication usage. On the software side, the dashboard visualizes this data with patient profiles, adherence scores, dosing windows, anomaly detection, and pill count trends. By uniting reliable hardware with intuitive analytics, Dose empowers clinicians, caregivers, and researchers to monitor adherence, reduce trial errors, and ultimately improve patient outcomes. How we built it Rapid prototyping with 3D printing and protoboards Clear, orange, and white PLA plastics for design and usability Xiao ESP32-C3 for compact footprint and connectivity TAL220 load cell for precision pill detection HX711 ADC I2C converter for sensor-to-data translation ESP32 Wi-Fi for real-time telemetry into the dashboard Challenges we ran into Translating raw sensor readings into meaningful metrics and visualizations Dealing with late-stage hardware malfunctions under time pressure Accomplishments that we're proud of Creating a hardware-software product that feels intuitive and polished Seamlessly integrating diverse skill sets across our team Overcoming setbacks with resilience and adaptability What we learned Building rich, responsive web dashboards using tools like RadixUI Engineering enclosures for both functionality and aesthetics Prototyping hardware quickly with iterative testing and validation Using Supabase for smooth, real-time data integration into our dashboard What's next for Dose Validate Dose as a reliable tool for clinical and research data collection Integrate into existing research and healthcare workflows Expand analytics for deeper EMR integration and insights Continue refining the product through iterative development Contribute to a future where patients are healthier, more adherent, and better supported <div