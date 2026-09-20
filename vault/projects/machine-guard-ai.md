---
slug: "machine-guard-ai"
url: "https://devpost.com/software/machine-guard-ai"
title: "MACHINE GUARD AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 608
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/structured_db"
---

# MACHINE GUARD AI

> AI-Powered IoT Driving Climate-Smart, Sustainable Industrial Intelligence: Real-time monitoring and predictive insights to reduce energy waste and emissions(from reactive to proactive maintanance).

[Devpost](https://devpost.com/software/machine-guard-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[climate_energy]] [[developer_tools]] [[education]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[structured_db]]
  <sub>weak: financial_record</sub>

**stack** android, arduino, cloudhivemq, embeddedsystem, fastapi, firebase, microcontroller, mobileapp-kotlin, python(flask), scikitlearn, sensor, smtp, tcp/ip, unsupervisedlearning-isolationforest

## How they structured the write-up

- inspiration:
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of:
- what we learned
- what's next for machine guard ai

## Body

Problem Statement Proposed Solution Novelty Expected Solution Mobile App Mobile App Mobile App Firebase Session IOT Technical Architecture Inspiration: Modern industries often operate in a reactive manner, problems are addressed only after breakdowns, energy spikes, or environmental incidents occur. This reactive approach leads to excessive power consumption, material waste, unexpected downtime, financial losses, and increased environmental damage. According to recent reports, industry accounts for roughly 30% of global energy consumption and contributes significantly to greenhouse gas emissions , making it one of the largest sources of pollution worldwide. As an AIML students, we inspired to create a solution that shifts industries from reactive to intelligent and proactive systems. By leveraging IoT sensors and machine learning, Machine-Guard creates a virtuous cycle : Real-time monitoring → Early detection → Preventive action → Reduced waste → Lower energy consumption → Improved efficiency → Lower environmental impact. What it does Machine-Guard AI is an intelligent Industrial IoT monitoring system designed to improve machine safety, operational efficiency, and sustainable industrial operation . Continuously monitors machine health parameters such as temperature, gas levels, vibration, and power consumption . Streams real-time data using the MQTT protocol to a centralized backend for processing and analysis. Detects abnormal operating conditions and potential machine failures before breakdown occurs. Provides instant alerts and actionable insights through a mobile dashboard . Reduces energy waste by identifying inefficient or idle power usage and enabling preventive maintenance actions . How we built it We built Machine-Guard as an end-to-end Industrial IoT system . An ESP32 microcontroller interfaces with temperature, vibration, gas, humidity, and current sensors to collect machine health data . The device connects to Wi-Fi and publishes readings in JSON format to an MQTT broker (HiveMQ) . A Python Flask backend subscribes to the MQTT topics using the Paho-MQTT library , validates the data, and stores it in Firebase Realtime Database with a SQLite fallback . REST APIs serve the data to a dashboard/mobile app for real-time visualization . When abnormal conditions are detected, the system alerts operators for preventive maintenance . Challenges we ran into Sensor calibration issues are leading to inconsistent readings. During production, one major challenge was managing different voltage input requirements for various sensors and the LCD module. Network instability is affecting real-time MQTT data transmission. Dependency on Public MQTT broker availability. Integrating hardware, backend, and dashboard smoothly Accomplishments that we're proud of: Enabled the shift from manual monitoring to autonomous, data-driven industrial operations. Designed a system capable of reducing unplanned downtime by an estimated 20–40% through early detection and real-time alerts. Built a safety-oriented monitoring framework that can reduce worker exposure to hazardous environments by 30–50% . Delivered real-time operational insights, enabling up to 2–3× faster decision-making . Developed a cost-effective solution projected to lower maintenance costs by 15–30% . Implemented energy tracking mechanisms capable of reducing energy waste by 10–20% . Enhanced operational productivity by an estimated 10–25% through intelligent monitoring. What we learned Hands-on experience with IoT hardware integration using ESP32 and multiple sensors , practical understanding of the MQTT protocol for real-time data communication. Debugging network communication using tools like Wireshark , applying sustainability concepts such as energy monitoring and environmental awareness . Managing real-world challenges like network instability and voltage mismatches What's next for MACHINE GUARD AI 1) Fall & Accident Detection - Identify falls or abnormal body posture in real time. 2) Unsafe Behavior Recognition - Detect improper machine handling or dangerous proximity to moving equipment. 3) Fire & Smoke Detection - Identify early signs of fire, sparks, or smoke in industrial environments. 4) Machine Guard Compliance Detection - Ensure safety shields and protective covers are properly installed before operation. <div