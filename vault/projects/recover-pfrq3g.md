---
slug: "recover-pfrq3g"
url: "https://devpost.com/software/recover-pfrq3g"
title: "ReCover"
hackathon: "Junction 2017"
winner: true
words: 203
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
---

# ReCover

> Bridging the gap between home recovery and physiotherapist. Live feedback and remote supervision.

[Devpost](https://devpost.com/software/recover-pfrq3g) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[health_clinical]] [[mental_health]]
**user** [[patient_family]]
**substrate** [[sensor_telemetry]]

**stack** ios, iot, suunto-movesense, swift

## How they structured the write-up

- what have we built as a prototype
- what it is made to do
- challenges we ran into
- what we learned
- what's next for recover

## Body

Start screen Exercise done right Flexion exceeded maximum Sensor list What have we built as a prototype The prototype is built as a native iOS app. It tracks knee joint flexion angle in real time and displays it as an animation. The user can define minimal flexion angle and track his or hers workout precision using Suunto movesense sensors. What it is made to do Tracks a person's rehabilitation process and various type of workouts. Delivers live feedback about exercises performed and eases communication and supervision on behalf of the physiotherapist. Provides a history of workouts for patients as well as summary reports for the physiotherapists about their patients. Challenges we ran into Initially, we tried to create a react-native app, but sensor data handling and connection throughout multiple platforms were a bit too complex for the time we had. We ended up using modules from Movesense-mobile-lib for iOS. We lacked a proper documentation for the Suunto movesense mobile-lib and sensors. What we learned Connecting Bluetooth devices, MVP planning and structuring, sensor data processing and normalization. What's next for ReCover Finalize the abovementioned features, create server-side enabling physiotherapist with an option to retrieve patients data. Adopt the app for diverse rehabilitation exercises. <div