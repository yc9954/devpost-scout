---
slug: "miia-4dsupg"
url: "https://devpost.com/software/miia-4dsupg"
title: "miia"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 456
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/developer"
  - "user/patient_family"
  - "substrate/medical_record"
---

# miia

> Health monitoring and management platform for patients and healthcare providers

[Devpost](https://devpost.com/software/miia-4dsupg) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]] [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[developer]] [[patient_family]]
**substrate** [[medical_record]]
  <sub>weak: geospatial</sub>

**stack** express.js, fitbit-web-api, heroku, json, quickbase, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for miia

## Body

App architecture GIF Vue monitoring vitals real time from FitBit devices The backend db that controls the profiles routing Inspiration Due to the outbreak of COVID-19, non-urgent healthcare services had reduced drastically and there is an increasing demand for remote outpatient solutions. Patients’ long-term vital signs are invaluable for physicians to make better-informed decisions. Continuous monitoring of vital signs, such as respiration and heart rate, plays a crucial role in early detection and even prediction of conditions that may affect the wellbeing of the patient. Current wearable devices such as smartwatches offer a convenient alternative to traditional vitals monitoring devices, however, not all wearables are as accurate and provide visualization of health data for users. Moreover, it is hard for doctors to retrieve data collected from these devices. In light of this, we would like to build a real-time remote health monitoring system monitoring patients' vital signs through wearable devices, and visualizing data with different levels of access for different target audiences such as healthcare providers, doctors, nurses, managers, and users. Ideally, the system would aid doctors in disease diagnosis and contribute to early detection and timely treatment of illnesses. What it does The app facilitates remote health monitoring by collecting vital signs such as heart rate via connected wearable devices, updating data in QuickBase, and presenting data in the form of a data visualization dashboard. Features Health data collection Health data is collected via connected wearable devices such as Fitbit smartwatch Data visualization Health data is visualized and presented in the form of a dashboard Alert system When a value exceeded the threshold, the app will alert the corresponding healthcare provider via Microsoft Outlook Health management All data including Electronic Health Record (EHR), patient medical history, vital signs, and healthcare provider information are stored and managed via the app How we built it Data management using Quickbase All health-related data are stored and managed in QuickBase Front-end development using Vue & back-end development using Express Our developer built the app using Vue and Express and deployed using Heroku Wearables connection using Fitbit web API Fitbit smartwatch is connected to the app using Fitbit web API Challenges we ran into Time zone was a challenge, as we have 3 different time zones and not all developers are awake at the same time. However, we are able to overcome this through effective communication and planning. Accomplishments that we're proud of We have built a fully functional app . What we learned All of us had no prior experience in quickbase, we learnt a lot about quickbase app webhooks and pipelines. What's next for miia New Features Available in different platforms Make the app available on different platforms AI pre-diagnostics Trained machine learning models for AI pre-diagnostics <div