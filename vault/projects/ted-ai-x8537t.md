---
slug: "ted-ai-x8537t"
url: "https://devpost.com/software/ted-ai-x8537t"
title: "Ted.AI"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 386
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "substrate/geospatial"
---

# Ted.AI

> A multimodal AI companion that fuses emotion sensing, language understanding, and real-time biofeedback to support children’s mental wellness.

[Devpost](https://devpost.com/software/ted-ai-x8537t) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[education]] [[health_clinical]] [[mental_health]]
**user** [[clinician]]
**substrate** [[geospatial]]

**stack** amazon-web-services, arduino, docker, fetchai, firebase, flask, gemini, neurolinq, openai, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ted.ai

## Body

🧸 Ted.AI — Empathy Engineered Inspiration Every day, millions of children grow up battling unseen struggles — anxiety, ADHD, loneliness, and emotional overwhelm — in a world moving too fast to listen. We wanted to create something that not only hears them but feels with them. A companion that bridges empathy and intelligence to help them regulate emotions and feel understood. What it does Ted.AI is an emotionally intelligent teddy bear powered by multimodal AI. It senses hugs, movement, and heart rate using embedded sensors and responds with empathy through a conversational LLM. It guides children through breathing exercises, focus routines, and calming interactions while analyzing tone, language, and gestures to adapt its responses in real time. A connected dashboard visualizes emotional states, sentiment trends, and simulated brain-region activations for parents, educators, and clinicians. How we built it Ted.AI integrates: Hardware: ESP32 microcontroller, HW-502 pulse sensor, capacitive touch sensors, and MPU6050 accelerometer. Software: OpenAI Whisper for speech-to-text, RoBERTa for emotion detection, and GPT-powered dialogue through LangChain orchestration. Data Pipeline: Real-time sensor fusion via MQTT, edge inference using TensorFlow Lite Micro, and backend storage with Flask, MongoDB, and InfluxDB. Dashboard: Built with React, Flask, and D3.js to visualize emotion timelines and neural activation maps. Challenges we ran into Synchronizing real-time audio, motion, and biosensor inputs required complex sensor fusion and filtering. Integrating emotion classification with low-latency on-device inference was another major challenge. We also spent time designing dialogue flows that felt emotionally natural rather than robotic, balancing empathy with accuracy. Accomplishments that we're proud of We successfully built a fully functional prototype that detects emotion through physical and verbal cues, reacts in real time, and displays a live dashboard of emotional analytics. The seamless blend of hardware sensing, multimodal AI, and affective computing exceeded our expectations in both complexity and impact. What we learned We learned how to merge disciplines — embedded systems, AI, psychology, and human-centered design — to create technology that genuinely connects with people. Building Ted.AI taught us the importance of empathy in engineering and how emotional design can make AI feel human. What's next for Ted.AI We plan to integrate EEG-based emotional tracking, cloud-based analytics for therapists, and reinforcement learning for adaptive empathy. Our vision is to expand Ted.AI into classrooms and therapy settings to support children worldwide through emotionally aware technology. <div