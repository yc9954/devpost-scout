---
slug: "project-kisan-fuxag4"
url: "https://devpost.com/software/project-kisan-fuxag4"
title: "Project Kisan:"
hackathon: "Student Innovators Without Borders Hacks (Students; Open Ended)"
organization: "Batch 09"
winner: true
words: 405
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/agriculture_food"
  - "user/frontline_worker"
  - "substrate/video_visual"
---

# Project Kisan:

> AI Agent Powered IoT- Enabled Agricultural Real Time Monitoring and Marketing System

[Devpost](https://devpost.com/software/project-kisan-fuxag4) · hackathon [[Student Innovators Without Borders Hacks -Students- Open Ended-]]

## Facets

**mechanism** [[on_device_local]] [[privacy_tech]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[agriculture_food]]
**user** [[frontline_worker]]
**substrate** [[video_visual]]

**stack** agent, ai, builder, chart.js, cloud, d3.js, db, esp8266, firebase, flask, gemini, iot, mobilenetv2, mqtt

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for project kisan:

## Body

Inspiration As the son of a farmer, I’ve seen firsthand how smallholder farmers struggle with unpredictable weather, pests, water shortages, and lack of access to real-time market information. Many still rely on guesswork for irrigation, fertilization, and crop management. We wanted to build a solution that brings smart agriculture technology to every farmer — affordable, accessible, and impactful. What it does Our system integrates IoT sensors + AI models + Agentic AI assistants to create a digital farming assistant for rural and urban agriculture. It: Monitors soil moisture, temperature, humidity, nutrients, pH, CO₂, and light in real time. Uses AI models (MobilenetV2, Random Forest, Gemini multimodal) to detect crop diseases and predict yields. Sends multilingual alerts (via SMS, mobile app, and dashboard) for irrigation, fertilization, and pest control. Provides AI-driven crop recommendations based on soil/seasonal conditions. Forecasts market prices to help farmers sell strategically. Supports waste-to-market solutions (animal dung, crop waste). Works both online (Firebase dashboards) and offline (SMS in low connectivity). How we built it IoT Layer: Sensors (DHT11, FC28 soil, NPK, BH1750, pH, CO₂, camera) → ESP8266/Raspberry Pi → MQTT. Backend: Node.js + Flask APIs, Neon DB + Firebase Firestore for real-time data. AI Layer: MobilenetV2 for crop disease detection, RandomForest for predictions, Gemini + Vertex AI Agents for intent detection and multilingual support. Frontend: React Native (Mobile) + React.js (Web) dashboards with Chart.js & D3.js for visualization. Notifications: Firebase Cloud Messaging + Twilio SMS. Challenges we ran into Ensuring low-cost hardware for farmers with limited resources. Building an offline-first system for poor network regions. Integrating multimodal AI (voice, image, text) into a farmer-friendly UX. Maintaining scalability while supporting rural devices with low power. Accomplishments that we're proud of Built 90% of the product, with a working prototype and live demos. Integrated IoT + AI + Agentic AI into one unified agriculture platform. Created a multilingual voice-based assistant for farmers in Kannada, Hindi, etc. Forecasted market prices + disease detection on the same platform. Got early validation with farmers and mentors. What we learned Real-world IoT systems must handle unreliable internet and hardware failures. Farmers value simple, multilingual interfaces more than flashy dashboards. AI models must be lightweight and run efficiently for rural deployment. What's next for Project Kisan: Digital Twins for farms (virtual replicas of fields & crops). Drone-based crop monitoring for large-scale deployments. Blockchain-based traceability of produce. Federated learning for community-driven model improvements. Scaling to smart villages and peri-urban ecosystems. <div