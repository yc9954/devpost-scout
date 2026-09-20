---
slug: "visionify"
url: "https://devpost.com/software/visionify"
title: "Visionify"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 831
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/elder_child_care"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Visionify

> A proactive real-time AI wearable that helps the visually impaired navigate safely—at a price under $100, making smart mobility finally accessible to all.

[Devpost](https://devpost.com/software/visionify) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[accessibility]] [[elder_child_care]] [[security_privacy]] [[transportation]]
**user** [[patient_family]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** gemini, hardware, langchain, next.js, opencv, python, tailwindcss, tensorflow, unify, vapi

## How they structured the write-up

- inspiration 🤔
- what it does + how we built it 🛠️
- challenges we ran into 😿
- accomplishments that we're proud of 💯
- what we learned 💭
- what's next for visionify
- built with

## Body

dashboard 2 3 Inspiration 🤔 Have you ever considered how visually impaired people navigate everyday dangers? Crossing busy roads, avoiding potholes, or noticing imminent hazards like moving vehicles can be incredibly risky. Consider these staggering statistics: Approximately 253 million people globally have a form of visual impairment; around 36 million are completely blind. [WHO Source] 40% of visually impaired individuals report frequent collisions or accidents when navigating daily. [VisionAware Source] Blind pedestrians are nearly twice as likely to be involved in accidents or injuries related to road navigation. [Journal of Visual Impairment & Blindness Source] Driven by these realities, we developed visionify. What it does + How we built it 🛠️ Visionify is an advanced wearable that combines the best aspects of Waymo’s real-time obstacle detection with the precise location tracking features of Life360, tailored specifically for the visually impaired community. At its core, Visionify provides continuous, real-time spatial awareness using advanced sensor fusion - Camera, accelerometer, Ultrasonics sensor and GPS module. A Raspberry Pi serves as our onboard computing platform, integrating sensor data from a camera, ultrasonic sensor, microphone, and ADXL345 accelerometer. We developed a three-tier intelligent safety system: Local Guardian: Instant (<50ms) detection and alert for critical dangers such as sudden obstacles, falls, or collisions, providing immediate haptic and audio feedback. VAPI AI phone calls: When it detects any unusual activity like a fall of the person through our accelerometer sensor, our voice AI agent automatically calls the emergency contacts of the person. Cloud Intelligence: Utilizing powerful cloud-based AI via REST APIs, we employ Gemini Vision and GPT-4 Turbo for detailed scene description, obstacle classification, and intelligent route guidance. Natural Interaction: Leveraging ElevenLabs VAPI for seamless and natural voice interaction, providing precise and understandable guidance. Indoor Navigation Agent: A real-time voice-activated navigation system that helps users navigate indoor spaces using computer vision and AI. Built specifically for the TAN OAK conference room on the 4th floor of the MLK building. We optimized our pipeline by aggressively tuning models for inference latency, adopting network quantization, and leveraging accelerated matrix multiplication via optimized PyTorch configurations. Our custom lightweight REST protocol ensures rapid transmission of sensor data and AI-driven instructions between the device and cloud services. Built on a scalable Flask backend, Vefficiently processes simultaneous streams from multiple sensors and integrates seamlessly with mobile and web dashboards, giving caregivers real-time visibility into the user’s environment and safety. Challenges we ran into 😿 Real-time performance was non-negotiable; even minimal latency could be dangerous. We dedicated extensive effort to refining our data processing pipeline. Despite aggressive model tuning and kernel optimization, initial tests showed bottlenecks due to hardware constraints. Leveraging cloud GPUs, we dramatically reduced inference times. Our data transmission initially used standard JSON, which significantly slowed real-time data exchanges. Recognizing milliseconds matter, we engineered a bespoke lightweight protocol, eliminating redundant metadata and ensuring rapid, efficient communication between edge devices and cloud servers. Hardware affordability posed another major challenge. Existing market solutions are often priced prohibitively (\$800+), inaccessible to many visually impaired users. To address this, we selected widely available, inexpensive components such as the Raspberry Pi, ultrasonic sensors, and affordable haptic motors, assembling a robust wearable at under \$100 total. Accomplishments that we're proud of 💯 Visionify started as a response to a real, pressing need: making safe, intelligent navigation affordable for all visually impaired individuals. The end result was a powerful, fully operational wearable device capable of: Instantaneous (<50ms) hazard detection and alerting Real-time cloud-based contextual navigation guidance Seamless integration of multimodal sensor data for comprehensive situational awareness Affordable construction and accessibility, priced below \$100 per unit We successfully integrated advanced AI models like GPT-4 Turbo and Gemini Vision with an intuitive interface powered by ElevenLabs VAPI, providing clear, actionable navigation guidance through both haptic and audio cues. What we learned 💭 This project expanded our understanding of low-latency AI inference, sensor fusion, and efficient hardware design. We grappled deeply with PyTorch and TensorRT optimizations, pushing the limits of Raspberry Pi’s hardware capabilities. Through rigorous testing and iteration, we found strategies to reduce inference latency significantly, ensuring reliability and speed critical for real-time danger detection. Additionally, the hardware design required precision engineering. Initial prototypes revealed vulnerabilities in durability and comfort, leading to iterative refinements in material choices and sensor placements to optimize usability and robustness. What's next for Visionify We’re just beginning our journey. The roadmap ahead is exciting: Enhanced directional haptic feedback system, providing intuitive physical navigation cues. Integration of indoor mapping solutions for seamless indoor-outdoor navigation experiences. Customizable object and scene recognition to personalize the experience for individual users. Expanded testing and user feedback sessions with visually impaired communities to refine and perfect usability. We aim to partner with organizations and healthcare providers to broaden accessibility and ensure that SentientSight reaches those who need it most, transforming the independence and daily lives of millions globally. Built With Raspberry Pi Python (Flask, PyTorch, Requests, smbus2) ElevenLabs VAPI Gemini Vision & GPT-4 APIs Ultrasonic & ADXL345 accelerometer sensors Affordable haptic hardware <div