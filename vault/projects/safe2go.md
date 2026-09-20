---
slug: "safe2go"
url: "https://devpost.com/software/safe2go"
title: "Safe2Go"
hackathon: "Student Innovators Without Borders Hacks (Students; Open Ended)"
organization: "Batch 09"
winner: true
words: 363
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "substrate/sensor_telemetry"
---

# Safe2Go

> Turning ordinary helmets into life-saving devices with instant accident detection and emergency alerts

[Devpost](https://devpost.com/software/safe2go) · hackathon [[Student Innovators Without Borders Hacks -Students- Open Ended-]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]]
**substrate** [[sensor_telemetry]]

**stack** arduino, c++, esp32, gps, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for safe2go

## Body

IoT Based Smart Helmet Device Circuit Diagram Real Time Dashboard Navigation System for guiding the riders Real time Alert Through Whatshapp Alert Log in Arduino Prototype Inspiration The idea grew from observing how many road accidents go unnoticed or receive delayed help. I wanted to design something small yet impactful—something that could sit inside any helmet and call for assistance when the rider cannot. The thought that a few seconds could save a life became the core motivation behind Safe2Go. What it does Safe2Go is a compact IoT-based module that fits into any helmet and monitors motion, impact, and rider activity. When a crash is detected, it instantly sends alerts to emergency contacts via WhatsApp or email along with live GPS location. The system works offline for accident detection and uses network connectivity for alerts. A dashboard visualizes real-time sensor data and activity logs. How we built it We started by researching accident dynamics and exploring sensors like: -Accelerometer and Gyroscope -Sound and Vibration sensors -GPS and Emergency Communication APIs Using an ESP32 microcontroller, we captured multi-sensor readings and set impact thresholds We created a Node.js backend to process incoming data, integrated Twilio for WhatsApp alerts, SMTP for email notifications, and built a lightweight React dashboard for visualization. Challenges we ran into Setting correct impact thresholds without false triggers Achieving stable communication during high-speed movements Power optimization to keep the device small and battery-efficient Designing the module to fit inside any helmet without discomfort Debugging real-time data flow between ESP32 → Server → WhatsApp/Email Accomplishments that we're proud of Built a working prototype capable of detecting accidents reliably Successfully sent automated WhatsApp and email alerts with location Created a live monitoring dashboard with continuous sensor streaming Ensured the system remains compact, low-cost, and helmet-agnostic What we learned We learned about IoT workflows, real-time sensor calibration, backend-to-device communication, and emergency automation. This project strengthened our skills in embedded systems, cloud integration, and data visualization. What's next for Safe2Go We plan to add fall-detection AI, fatigue monitoring, and voice-based SOS triggers. Future upgrades include integrating eye-state detection, navigation instructions, improved power efficiency, and launching Safe2Go as a universal plug-and-use safety device for everyday riders. <div