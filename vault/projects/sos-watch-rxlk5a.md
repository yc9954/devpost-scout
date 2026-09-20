---
slug: "sos-watch-rxlk5a"
url: "https://devpost.com/software/sos-watch-rxlk5a"
title: "SOS Watch"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 414
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "user/patient_family"
---

# SOS Watch

> An autonomous, edge-computing smart watch designed for asthma patients. It monitors vitals and air quality, detects attacks, and broadcasts emergency SOS alerts without needing a smartphone.

[Devpost](https://devpost.com/software/sos-watch-rxlk5a) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
  <sub>weak: deterministic_policy, voice_speech</sub>
**domain** [[health_clinical]]
**user** [[patient_family]]
  <sub>weak: sensor_telemetry</sub>

**stack** c++, embedded, esp32, hardware, internet-of-things-(iot), systems

## Body

SOS Watch working-prototype scheme 💡 The Idea & Inspiration (Our Mission) Asthma affects over 260 million people worldwide. During a sudden, severe attack, a patient experiences acute panic and physical constriction. Finding an inhaler, unlocking a smartphone, or calling for help becomes nearly impossible in these critical moments. Existing smartwatches and medical alert bands fail because they are heavily tethered to smartphones via Bluetooth. If the phone's battery dies or the connection drops, the safety net disappears. SOS-Watch was created to eliminate the smartphone from the emergency loop. It is a completely autonomous, hardware-driven smart band that processes environmental and vital data "on-edge," guides the user with voice commands during panic, and sends distress signals independently. ⚙️ How It Works SOS-Watch is powered by an optimized ESP32-C3 microcontroller running a custom, non-blocking C++ State Machine: Continuous Sensing: The device monitors air quality (harmful gases), blood oxygen saturation ($SpO_2$), heart rate (BPM), sudden impacts (fall detection), and loud acoustic patterns (coughing). Local Processing (Edge Computing): All sensor data is filtered and analyzed directly on the wearable. Pre-Alarm & Voice Guidance: If an anomaly is detected, the built-in speaker (DFPlayer Mini) plays a clear voice prompt to calm the user and starts a 5-second countdown. Physical Override (False-Alarm Protection): The user can press a prominent, tactile button on the side of the watch to cancel the alarm if they are fine. Emergency SOS Broadcast: If the countdown expires without override, the ESP32-C3 boots its Wi-Fi/Bluetooth antenna and immediately broadcasts an emergency message with vital statistics to family members, caretakers, or local receivers. 🌟 Main Features & Technical Highlights 100% Smartphone Independence: No companion app or active phone connection is required to process data or trigger local alarms. Non-Blocking Cooperative Multitasking: Designed using millis() instead of delay() , ensuring the display, sensors, and safety button remain completely responsive. Intelligent Threat Prioritization: A strict priority engine manages concurrent events (e.g., a physical Fall instantly takes precedence over High Heart Rate). Power Optimization: Wi-Fi and Bluetooth antennas are kept completely powered down, booting up only when an actual emergency SOS is triggered, drastically saving battery life. 🛠️ Hardware & Tech Stack Microcontroller: ESP32-C3 Super Mini Physiological Sensors: MAX30102 ($SpO_2$ & Heart Rate), MPU6500 (6-axis accelerometer for fall detection) Environmental & Acoustic Sensors: Sensirion SGP40 (Digital VOC/Air Quality), MAX9814 (Acoustic microphone for cough tracking) User Interface: SSD1306 OLED (128x64 pixels), DFPlayer Mini + Micro Speaker, physical tactile bypass button. Power Management: TP4056 charging IC + 3.7V 250mAh Li-ion battery. <div