---
slug: "greenguardian-microfarm"
url: "https://devpost.com/software/greenguardian-microfarm"
title: "Sprout"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 553
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Sprout

> Your mini robot microfarm.

[Devpost](https://devpost.com/software/greenguardian-microfarm) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**user** [[legal_professional]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** arduino, claude, cuda, disk-paging, gpio, gpio/i2c, i2c, jetson-nano, linux, memory-management, ollama, python, qwen

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned

## Body

Frame Riveting & Assembly Pt1 Working on Jetson Nano Assembly Test Demo for Rails Assembled Gantry System Control Circuity Planning Cutting Sheet Metal for the Frame Assembled Base Frame Frame Riveting & Assembly Pt2 Assembly Test Demo with Jetson Nano and Arduino Final Working Model Inspiration We wanted to bridge the gap between rigid, industrial robotics and the organic beauty of nature. The idea was to create a "gardener" that doesn't just automate a task, but feels like a companion to the plants it cares for. We were inspired by the precision of 3D printers and CNC machines but wanted to apply that technology to something living, creating a system that is both high-tech and deeply aesthetic. It's also an excellent application of applying systems like these towards tangible social good. What it does Sprout is an autonomous, AI-controlled robotic garden powered by edge computing. Intelligent Vision: A camera mounted directly to the gantry moves over the garden bed, feeding live video to an onboard NVIDIA Jetson Nano. Edge AI Analysis: Instead of just seeing "green," our custom Edge AI model analyzes the footage in real-time to identify the specific plant species and assess its health status. Smart Watering: Based on the plant type and its current health, Sprout calculates exactly how much water is needed and pumps that precise amount, ensuring optimal growth without waste. How we built it We approached this as a full-stack robotics challenge, combining mechanical engineering with edge computing: Hardware & Mechanics: We designed a 3-axis gantry frame (similar to a 3D printer) to provide full coverage of the microfarm. We used machining tools (mill and lathe) to fabricate custom structural components and prototyped parts to ensure smooth motion. Compute & Vision: The system's "brain" is an NVIDIA Jetson Nano. We mounted a camera to the gantry head to give the AI a close-up, top-down view of every leaf. Software: We developed an Edge AI pipeline that processes visual data locally on the Jetson. The model classifies plants and determines health metrics, which then triggers the pump system via Python scripts. Aesthetics: To give Sprout personality, and because vinyl wraps rock, we wrapped the chassis in vinyl. ## Challenges we ran into Edge Optimization: Running complex computer vision models on the Jetson Nano required optimizing our code to ensure real-time performance without lag. Dynamic Watering Logic: Training the model to not just recognize a plant, but judge its health and decide on a water volume, was significantly harder than simple object detection. Hardware Integration: Calibrating the gantry system so the physical nozzle aligned perfectly with what the camera was seeing required precise coordinate mapping. Accomplishments that we're proud of Edge AI Implementation: Successfully deploying a health-assessment model on the Jetson Nano that runs entirely offline/on-device. Functional Gantry: Building a reliable CNC-style motion system from scratch over the weekend. What we learned Systems Integration: We learned the complexities of marrying high-level AI (Jetson) with low-level hardware control (motors and pumps). Computer Vision on the Edge: We gained deep experience in optimizing neural networks for embedded devices. Rapid Prototyping: We honed our skills in machining and fabrication under pressure, making quick design decisions to keep the build moving. At many points - especially in wiring - realizations about the underlying logic of certain components forced us to quickly pivot. <div