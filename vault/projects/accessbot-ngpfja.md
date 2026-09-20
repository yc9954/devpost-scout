---
slug: "accessbot-ngpfja"
url: "https://devpost.com/software/accessbot-ngpfja"
title: "AccessBot"
hackathon: "Dev Season of Code "
organization: "DSOC Official"
winner: true
words: 545
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# AccessBot

> AccessBot - AI-powered smart glasses that help blind and deaf individuals navigate the world safely through real-time obstacle detection and optimized path guidance.

[Devpost](https://devpost.com/software/accessbot-ngpfja) · hackathon [[Dev Season of Code]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[accessibility]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** flask, html5, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for accessbot

## Body

Real world implementation...trying product in real world Smart Glasses Inspiration AccessBot was inspired by the visible gap between technological advancement and real-world accessibility. While navigation systems optimize for time and distance, they rarely account for accessibility constraints such as ramps, elevators, or obstacle-heavy environments. We observed that people with visual, hearing, or mobility impairments often rely on assistance for tasks that should be independently manageable. The goal was to design a system where accessibility is treated as a core routing constraint, not a secondary feature. We wanted to build a scalable, AI-driven platform that improves independent mobility using practical hardware and optimized algorithms. What it does AccessBot is an AI-powered accessibility navigation system that combines smart glasses, accessible route optimization, and crowdsourced mapping. The system: Detects real-time obstacles using onboard computer vision Provides haptic and audio feedback for safe navigation Computes accessibility-aware routes using weighted path optimization Integrates AR overlays for guided movement Allows users to map and validate accessibility features Traditional routing minimizes: $$ \min \sum_{i=1}^{n} w_i $$ AccessBot modifies this to: $$ Cost = \alpha \cdot d + \beta \cdot a $$ Where: ( d ) = distance ( a ) = accessibility penalty ( \alpha, \beta ) = priority weights This ensures routes are both efficient and usable. How we built it Hardware We developed a wearable prototype using: ESP32-S3 / ESP32-CAM INMP441 microphone MAX98357A amplifier Vibration motor module OLED display Bone-conduction speaker The device performs lightweight edge inference and syncs with a mobile application. Software Optimized computer vision pipeline for obstacle detection Distance estimation using projection geometry: $$ d = \frac{f \cdot H}{h} $$ Accessibility-aware routing algorithm Crowdsourced accessibility database with validation scoring Mobile interface for navigation and AR overlays The architecture separates edge inference (micro-level awareness) from mobile-based route planning (macro-level navigation). Challenges we ran into Hardware Limitations Running real-time inference on ESP32-class hardware required aggressive model optimization and memory management. Latency Constraints Navigation feedback must satisfy: $$ Latency \leq 100 \text{ ms} $$ Maintaining this under variable lighting and movement conditions was challenging. Environmental Variability Detection accuracy fluctuated in low-light or cluttered environments. Data Reliability Accessibility data is often incomplete. We implemented a confidence scoring model: $$ C = \frac{\sum r_i}{n} $$ to improve trustworthiness. Multimodal UX Design Designing a unified system for blind, deaf, and wheelchair users required careful abstraction of feedback mechanisms. Accomplishments that we're proud of Successfully built a working smart glasses prototype. Implemented accessibility-aware routing instead of simple shortest-path logic. Achieved low-latency obstacle detection on embedded hardware. Designed a scalable crowdsourced accessibility validation system. Integrated hardware and mobile software into a synchronized ecosystem. What we learned Accessibility is fundamentally a systems engineering problem. Edge AI requires balancing model accuracy with computational constraints. In assistive technology, reliability and predictability are more important than feature complexity. Real-world deployment demands robust fallback mechanisms. User-centered thinking significantly improves system design decisions. What's next for AccessBot Replace geometric distance approximation with depth estimation models optimized for edge deployment. Integrate SLAM for improved indoor navigation accuracy. Expand the accessibility dataset through structured partnerships. Improve power efficiency and wearable ergonomics. Deploy pilot testing with real users to collect feedback and iterate. Our long-term goal is to evolve AccessBot into a standardized accessibility intelligence layer that can integrate with existing navigation ecosystems. <div