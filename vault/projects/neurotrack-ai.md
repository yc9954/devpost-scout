---
slug: "neurotrack-ai"
url: "https://devpost.com/software/neurotrack-ai"
title: "NeuroTrack AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 541
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# NeuroTrack AI

> AI-Powered Cognitive Fatigue & Focus Detection System

[Devpost](https://devpost.com/software/neurotrack-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]] [[labor_employment]] [[mental_health]] [[supply_logistics]]
**user** [[developer]] [[educator_student]]
**substrate** [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** css, fastapi, git, github, html, javascript, machine-learning, numpy, pandas, python, react, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for neurotrack ai

## Body

Inspiration Many people today spend long hours working or studying in front of a computer. Students, developers, and remote workers often continue working even when they are mentally exhausted, which reduces productivity and can lead to burnout. Most productivity tools focus on tracking tasks or time, but they rarely consider the mental state of the user. This inspired us to explore whether everyday behavioral signals such as typing patterns and interaction speed could help estimate cognitive fatigue. NeuroTrack AI was created as an experiment to see if behavioral data and machine learning could provide insights into a person's focus and mental fatigue. What it does NeuroTrack AI is a prototype system that monitors behavioral interaction signals like typing speed, typing variability, and idle time. These signals are analyzed using a machine learning model to estimate the probability of cognitive fatigue. The system generates a NeuroScore between 0 and 100 that represents the user’s cognitive focus level. When the fatigue level increases, the system can suggest short breaks to help users maintain productivity and reduce the risk of burnout. A dashboard displays fatigue trends and focus insights so users can understand how their cognitive state changes during a work session. How we built it We built NeuroTrack AI as a full stack prototype combining behavioral data tracking, machine learning, and a visualization dashboard. Behavioral signals are captured from user interactions and processed through a backend API. From this data, features such as typing speed and typing variability are extracted and passed into a machine learning model using logistic regression to estimate fatigue probability. The results are then displayed in a frontend dashboard that shows fatigue trends, NeuroScore metrics, and focus insights in real time. Challenges we ran into One of the biggest challenges was the lack of publicly available real world datasets related to cognitive fatigue and behavioral interaction patterns. To address this, we simulated behavioral patterns based on research in human computer interaction and fatigue detection studies. Another challenge was building a system that could demonstrate real time monitoring while remaining lightweight and easy to run during the limited time of a hackathon. Accomplishments that we're proud of We are proud that we were able to build a working prototype that demonstrates how behavioral interaction data can be used to estimate cognitive fatigue. The system integrates data collection, machine learning, and visualization into a single platform. Creating a real time dashboard with meaningful insights like the NeuroScore and fatigue probability was a key milestone for our team. What we learned During this project we learned how behavioral interaction data can be converted into useful features for machine learning models. We also gained experience in integrating frontend interfaces, backend services, and machine learning pipelines into a unified system. The hackathon environment also helped us improve our rapid prototyping and problem solving skills under time constraints. What's next for NeuroTrack AI NeuroTrack AI is currently a prototype and there are many opportunities to improve it. Future versions could include more advanced machine learning models, integration with webcam based fatigue detection, and support for wearable device data. We also envision expanding the platform into a productivity and wellbeing tool that helps individuals and organizations better understand cognitive workload and maintain healthier work habits. <div