---
slug: "agroguard-1ylp8j"
url: "https://devpost.com/software/agroguard-1ylp8j"
title: "AGROGUARD"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 382
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "user/frontline_worker"
  - "substrate/video_visual"
---

# AGROGUARD

> AI-powered crop health, straight from the field.

[Devpost](https://devpost.com/software/agroguard-1ylp8j) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
  <sub>weak: on_device_local</sub>
**domain** [[agriculture_food]]
**user** [[frontline_worker]]
**substrate** [[video_visual]]
  <sub>weak: sensor_telemetry</sub>

**stack** bhuvan, fastapi, ml, model, python, react

## Body

demo page of showing disease detected //Inspiration Farmers often detect crop diseases only after visible damage has already spread across the field. Manual inspection is time-consuming, expert advice is not always accessible, and overuse of pesticides increases cost and environmental harm. We were inspired to build AGROGUARD to provide early, automated, and affordable crop disease detection directly from the field using IoT and AI, without depending on smartphones or constant expert intervention. // What it does AGROGUARD is an IoT-enabled AI crop monitoring system that: Automatically captures crop leaf images using ESP32-CAM Collects temperature, humidity, and soil moisture data Detects diseases in rice and sugarcane crops using a deep learning model Provides crop-specific treatment and prevention recommendations Displays real-time crop health insights through a web-based dashboard Alerts users when disease risk or environmental stress is detected //How we built it Hardware Layer: ESP32-CAM for image capture ESP32 with DHT and soil moisture sensors for environmental data Communication Layer: Wi-Fi-based data transmission to the backend AI Layer: Trained a deep learning model on labeled crop disease images Optimized the model for CPU-based inference Backend Layer: REST API for receiving sensor data and images Disease prediction and recommendation engine Frontend Layer: Web application displaying disease status, confidence score, and actionable recommendations //Challenges we ran into Handling image quality issues under varying outdoor lighting conditions Managing limited processing power of edge devices Ensuring reliable connectivity in agricultural environments Balancing model accuracy with real-time performance Designing recommendations that are simple and farmer-friendly //Accomplishments that we're proud of Built a fully automated system without using farmer smartphones Successfully integrated IoT + AI + recommendation system Achieved early-stage disease detection in real field conditions Designed a low-cost and scalable architecture suitable for small farms Created a solution with real social and agricultural impact // What we learned Real-world AI systems require hardware-software co-design Data quality is as important as model complexity Agriculture needs simple, actionable outputs, not just predictions Edge and cloud systems must work together efficiently Technology adoption depends on usability and trust // What's next for AGROGUARD Add support for more crops and diseases Integrate weather forecasting for predictive disease alerts Enable offline edge inference for low-connectivity areas Introduce multilingual voice-based recommendations Deploy pilot projects in real farming communities Collaborate with agricultural departments and NGOs <div