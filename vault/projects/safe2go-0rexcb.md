---
slug: "safe2go-0rexcb"
url: "https://devpost.com/software/safe2go-0rexcb"
title: "HelmSense"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 896
team_size: 0
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/transportation"
  - "user/clinician"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# HelmSense

> HelmSense turns any helmet into an AI‑powered crash guardian that detects serious impacts and auto‑alerts your loved ones with your live location in seconds.

[Devpost](https://devpost.com/software/safe2go-0rexcb) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]] [[disaster_emergency]] [[transportation]]
**user** [[clinician]] [[developer]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** arduino, c++, esp32, gps, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for helmsense

## Body

Inspiration Every time I scrolled past yet another “bike accident, no one noticed in time” headline, it felt absurd that we wear helmets but they’re basically dumb plastic shells.[web:72] I wanted to turn that dead space into something alive, something that quietly watches over you when you’re least conscious of your own safety. The idea behind HelmSense was simple and crazy at the same time: what if your helmet could become your co‑pilot, paramedic, and black box recorder—without you doing anything extra? Instead of building yet another tracking app, I wanted a system that could sit inside any helmet, survive potholes and Indian traffic chaos, and still know the difference between “I dropped my helmet” and “I just crashed at 60 km/h.” The core motivation: compress an entire emergency response workflow into a few seconds of automated intelligence, so the rider’s life doesn’t depend on whether a stranger decides to stop or not. What it does HelmSense is an ultra-compact, plug‑and‑play helmet intelligence module that turns any ordinary helmet into a smart guardian. It continuously fuses accelerometer, gyroscope, vibration, and sound data to build a live “rider state” in the background. When it suspects a serious crash or abnormal fall, it doesn’t just send a text—it: Triggers an auto‑escalating SOS pipeline : Silent self-check (to avoid false positives). Haptic + audio prompt giving the rider a few seconds to cancel if they’re okay. If no response, instant alerts to emergency contacts with live GPS, speed, and impact profile. Streams anonymized crash signatures to a backend that can map dangerous road segments over time. Pushes data to a live dashboard showing current ride, recent events, and crash heatmaps for a city. The device works offline for detection and buffering, and then syncs whenever it gets connectivity. On the dashboard side, HelmSense can show not just “rider is in trouble”, but how bad the impact was, how many Gs they took, and which direction the force came from. How we built it We started by treating crashes like a signal classification problem instead of just “if acceleration > X then accident.” The hardware stack revolves around an ESP32, a 6‑axis IMU, vibration and sound sensors, and a GPS module, all squeezed into a form factor small enough to nest inside standard helmet padding. A custom firmware loop continuously samples multi-sensor data and maintains a rolling window of recent motion history. On the software side, we built: A Node.js backend that ingests sensor streams over MQTT/HTTP, tags events, and triggers alert workflows. A rules + ML‑ready detection pipeline: thresholds handle obvious spikes, while recorded data is structured so we can later feed it into a fall/crash classification model. A React-based Safety Command Center dashboard that visualizes: Real-time telemetry (acceleration, orientation, vibrations). Live rider status (normal / risky / suspected crash). City-level crash density and near‑miss hotspots. We wired Twilio for WhatsApp, SMTP for email, and integrated reverse geocoding so SOS messages carry a human-readable location instead of just raw coordinates. Challenges we ran into Tuning impact and motion thresholds so the system doesn’t panic every time the helmet gets tossed on a table, but still reacts aggressively to real crashes. Keeping Wi‑Fi/Bluetooth/GPS stable inside a moving, vibrating shell without draining the battery in a couple of hours. Making the PCB and enclosure small and curved enough to disappear into helmet padding without poking the rider’s head. Debugging a full end‑to‑end chain where a single bug—from sensor read to backend to WhatsApp/email—could silently kill the SOS flow. Handling edge cases like tunnels, zero‑network zones, and riders who crash in areas with poor GPS lock. Accomplishments that we're proud of Built a working helmet module that can reliably detect high‑impact events and distinguish “oops I dropped my helmet” from “this rider might be unconscious.” Got hands‑free SOS working: WhatsApp and email alerts that include live GPS, current speed, and a summary of the impact pattern. Designed a live dashboard that makes raw sensor chaos look like a clean, understandable ride timeline and crash history. Achieved a compact, helmet‑agnostic form factor so riders don’t need to buy a special “smart helmet” to use HelmSense. Laid the groundwork for using aggregated crash data to help city planners and traffic authorities understand which roads are silently killing people. What we learned We went deep into how messy real‑world sensor data can be when the device is vibrating, sweating, and getting slammed around on actual roads. We learned to think like a systems engineer: firmware, power management, connectivity, backend resilience, and UX for people who will interact with the system on the worst day of their life. The project pushed us to blend embedded systems, streaming backends, data visualization, and human‑centric safety design into one coherent experience. What's next for HelmSense HelmSense isn’t just a crash detector—it’s a platform we want to evolve into a helmet OS for riders : Train a fall‑detection and crash‑severity model using the anonymized impact data we collect. Add fatigue and micro‑sleep monitoring, using motion patterns and optional eye‑state input from a visor-mounted module. Introduce voice-based SOS and quick‑cancel commands so riders can interact without touching their phone. Build navigation overlays that warn riders about historically dangerous turns, pothole zones, and accident‑prone intersections in real time. Optimize the hardware for longer battery life, wireless charging, and easier installation so HelmSense becomes a universal, plug‑and‑use safety upgrade for any helmet. <div