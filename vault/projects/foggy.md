---
slug: "foggy"
url: "https://devpost.com/software/foggy"
title: "pFOG: Parkinson's Medical Aid Device"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 356
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
---

# pFOG: Parkinson's Medical Aid Device

> Patients with Parkinson’s often suffer from Freezing of Gait (FOG). Using a 1D-CNN and LSTM, we predict FOG and deliver targeted stimulation via wearable robotics to regain ability

[Devpost](https://devpost.com/software/foggy) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]] [[health_clinical]] [[labor_employment]]
**user** [[patient_family]]
**substrate** [[sensor_telemetry]]

**stack** esp32, flask, google-cloud, next.js, python, pytorch, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

Web interface Model architecture Inspiration Someone we know has Parkinson’s disease, and like many patients, he suffers from Freezing of Gait (FOG) — a sudden, involuntary inability to walk. Recent research (N.E. Ibrahim, Nature, 2024) has shown that targeted muscle stimulation can effectively eliminate FOG. Inspired by this, his family noticed that gently poking the back of his leg with a stick during an episode helped him move again. This simple action inspired us to develop an automated, predictive solution. What it does Our project, pFOG, is a wearable device that predicts Freezing of Gait using sensor data and machine learning. Once FOG is detected, it gives targeted muscle stimulation to the frozen leg, mimicking the effect of a physical "poke" and helping the patient resume walking. We also built a web interface for easy data collection and labeling, which allows users to fine-tune a model using their own walking data—essential for adapting to gait variability across patients. How we built it We collected accelerometer and gyroscope data using an Adafruit MPU-6050 IMU mounted on a wearable module. A 1D Convolutional Neural Network (1D-CNN) extracts rich spatial features, which are fed into a Long Short-Term Memory (LSTM) model with learned temporal patterns. Together, these are able to recognize the onset of FOG from real-time motion data. Upon detection, a servo-actuated mechanism delivers localized muscle stimulation to the leg using a robotic arm, replicating the therapeutic “poke.” Challenges we ran into Our challenges began before the hackathon even started—we didn’t have a 3D printer! Huge thanks to Nour and Team AR Glasses for letting us run a quick print on theirs! From there: We had to improvise wiring and mechanical assemblies with whatever was available (true hacker spirit!). UART communication was not as “plug and play” as advertised—serial timing issues cost us a lot of debugging hours. Training a machine learning model that didn’t overfit and could generalize across different walking styles was tricky, especially with limited, noisy data. Accomplishments that we're proud of We are very proud to demonstrate a working prototype that successfully detects FOG episodes with >90% accuracy and responds in real time! <div