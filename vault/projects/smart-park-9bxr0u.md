---
slug: "smart-park-9bxr0u"
url: "https://devpost.com/software/smart-park-9bxr0u"
title: "Vision Guide – Smart AI Assistant for the Visually Impaired"
hackathon: "FusionHacks 2"
organization: "FusionHacks"
winner: true
words: 431
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/disaster_emergency"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Vision Guide – Smart AI Assistant for the Visually Impaired

> Vision Guide is an AI-powered mobile assistant that helps visually impaired users navigate their environment using real-time object detection, voice interaction, and safety alerts.

[Devpost](https://devpost.com/software/smart-park-9bxr0u) · hackathon [[FusionHacks 2]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[disaster_emergency]] [[transportation]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** gemini, github, google, mongodb, next.js, opencv, python, speechapi, tailwindcss, text, to

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vision guide – smart ai assistant for the visually impaired

## Body

Inspiration During summer, visually impaired individuals face unique challenges while navigating outdoor environments — from intense heat and dehydration to crowded public spaces filled with unpredictable obstacles. As someone passionate about accessible technology and AI, I wanted to build something meaningful that helps bridge the gap in daily mobility support for the visually impaired, especially during these difficult months. That’s how the idea for Vision Guide was born — an AI-powered companion that speaks, sees, and supports users wherever they go. What it does Vision Guide is a voice-enabled smart assistant that helps visually impaired users move safely and independently. It uses a mobile device’s camera to detect and describe nearby objects, obstacles, and people through real-time voice feedback. Key features: Object Detection with Voice Alerts: Identifies and announces objects like vehicles, people, stairs, and pets. Summer Safety Mode: Provides heatwave alerts and hydration reminders based on live weather. Emergency Voice Trigger: Users can say “Help me” to send their location to a saved emergency contact. Conversational Assistant: Powered by Gemini Flash 2.0, it answers contextual questions about the environment. How we built it Backend: Python + Flask for server-side logic Computer Vision: YOLOv5 + OpenCV for real-time object recognition Voice Assistant: Google Text-to-Speech API for speaking outputs Frontend: Next.js and TailwindCSS (demo UI) Mapping & Location: Leaflet.js for geolocation mapping (optional) QR Code Tools: Integrated react-qr-code and html5-qrcode Database: MongoDB for storing emergency contacts and user preferences Testing & Deployment: Ngrok for live testing, GitHub for collaboration Challenges we ran into Optimizing real-time object detection for performance on lower-end devices Ensuring the voice assistant works well in noisy or busy environments Managing fast response times from camera to voice without noticeable lag Designing an interface that's accessible but doesn't rely on visuals Accomplishments that we're proud of Built a low-latency object detection system with reliable voice feedback Implemented an emergency response system that works on voice alone Added summer-specific features that enhance real-world safety Developed a complete AI-powered prototype for accessibility use cases What we learned How to fine-tune vision models for mobile and real-time usage The importance of inclusive design in assistive technologies Managing real-time audio processing with camera and detection outputs Designing with empathy by considering real user needs and contexts What's next for Vision Guide – Smart AI Assistant for the Visually Impaired 🌍 Regional language support (Tamil, Hindi, Telugu, etc.) 🧠 Integration with wearable devices like smart bands and glasses 🔒 Offline support and stronger privacy controls 🏥 Field testing in partnership with NGOs and community centers 🚶 Enhanced crowd detection and voice-guided outdoor pathfinding <div