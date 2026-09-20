---
slug: "schema-assist"
url: "https://devpost.com/software/schema-assist"
title: "Nirbhay"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 495
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/disaster_emergency"
  - "substrate/structured_db"
---

# Nirbhay

> An automated SOS app for public safety using AI

[Devpost](https://devpost.com/software/schema-assist) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[disaster_emergency]]
**substrate** [[structured_db]]

**stack** ai, expo.io, fastapi, gru, native, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nirbhay

## Body

SOS location Inspiration Incidents of harassment and unsafe situations often happen suddenly, leaving victims with little time or ability to manually call for help. Most safety apps depend on pressing an SOS button, which may not be possible during panic or physical struggle. Our team wanted to build a system that detects danger automatically instead of waiting for the user to react. Inspired by real-world safety challenges and the need for faster emergency response, we created Nirbhay, an AI-driven personal safety system that can detect abnormal motion patterns and trigger alerts in real time. What it does Nirbhay is a smart safety platform that monitors motion patterns and detects potential panic situations automatically. Key features: Detects abnormal movement using phone sensors (accelerometer and gyroscope) Uses AI models to predict panic or distress behavior Sends automatic SOS alerts to guardians Shares live location during emergencies Works even if GPS is temporarily lost using cellular triangulation Provides safety analysis and risk detection during trips The goal is to reduce response time during emergencies and provide proactive safety assistance. How we built it We built Nirbhay as a mobile-first AI safety system with a scalable backend. Architecture: Mobile sensors capture motion data (accelerometer & gyroscope) Data is processed to detect abnormal activity A backend system evaluates safety risks and triggers alerts Location tracking works through GPS and cellular fallback Key components: FastAPI backend for safety event processing MongoDB database for trip and motion tracking AI/ML models for activity prediction SMS alerts and push notifications for emergency communication Location tracking using GPS and cellular triangulation Challenges we ran into Building a reliable safety system required solving several technical challenges: Distinguishing between normal movements and panic behavior Reducing false alerts while maintaining sensitivity Handling location tracking when GPS signals are weak Managing real-time data streams from sensors Designing a system that works efficiently on mobile devices We solved these challenges by combining rule-based safety detection with machine learning models. Accomplishments that we're proud of Built a fully functional backend safety engine Implemented automatic panic detection logic Integrated real-time location tracking Designed a scalable system architecture Developed a prototype that demonstrates autonomous safety alerts Most importantly, we built a system that focuses on preventing danger instead of reacting after incidents occur. What we learned Through this project we learned: How to process and analyze sensor-based motion data How to design real-time event-driven systems The importance of human-centered safety technology How AI models can be applied to predict real-world behavior patterns The value of teamwork when building complex systems quickly. What's next for Nirbhay We plan to expand Nirbhay into a complete intelligent safety platform. Future plans include: Deploying GRU/LSTM models for advanced activity prediction Running AI models directly on-device for faster response Integrating with wearable devices and smart bands Building partnerships with campuses, NGOs, and city safety programs Creating a large dataset for training more accurate safety models Our vision is to make proactive personal safety technology accessible to everyone. <div