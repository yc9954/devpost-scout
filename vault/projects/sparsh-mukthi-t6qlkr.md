---
slug: "sparsh-mukthi-t6qlkr"
url: "https://devpost.com/software/sparsh-mukthi-t6qlkr"
title: "Sparsh Mukthi"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 374
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Sparsh Mukthi

> Embracing Touchless Technology

[Devpost](https://devpost.com/software/sparsh-mukthi-t6qlkr) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
**domain** [[education]] [[finance_payments]] [[health_clinical]]
**substrate** [[geospatial]] [[web_dom]]
  <sub>weak: financial_record</sub>

**stack** css, flask, html, javascript, mediapipe, numpy, opencv, pyautogui, pygame, pynput, python, sciket-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

logo website problem statement solution about UNDG alignment tech stack work flow business model prototype market competition Sparsh Mukthi Inspiration In today’s world, constant physical interaction with devices —whether keyboards, mice, or touchscreens—creates inefficiencies and hygiene concerns, especially in sensitive environments such as hospitals, VR classrooms, and shared office spaces . This inspired us to build Sparsh Mukthi , a system that enables touchless control through a combination of hand gestures and voice commands . Our vision is to create a more hygienic, accessible, and futuristic interface that reduces touch dependency and expands inclusivity for differently-abled users. What it does Sparsh Mukthi allows users to control their system without touching it , by: Recognizing voice commands to perform common actions (e.g., opening apps, sending messages, searching online). Detecting hand gestures to navigate screens, scroll, or interact with applications. Offering context-aware automation , so commands adapt based on the active screen (e.g., WhatsApp vs. Chrome). This blend of gesture and speech creates a seamless human–computer interaction model. How we built it Frontend: Minimalistic Python interface for voice & gesture command execution. Voice Recognition: Integrated speech-to-text APIs for accurate and fast command understanding. Gesture Recognition: Implemented computer vision techniques (OpenCV/MediaPipe) to map hand movements into actionable commands. Context Awareness: Designed logic to adapt voice/gesture inputs depending on the active application window . AI Layer: Ensured natural language understanding so users can interact without rigid command syntax. Challenges we ran into Noise Sensitivity in Voice Recognition: Background noise often interfered with voice commands. Solution: Applied noise cancellation filters and adjusted thresholds for accuracy. Gesture Accuracy in Low Light: Hand tracking became unstable in poor lighting conditions. Solution: Added preprocessing filters and fallback command options. Context Switching: Ensuring that the assistant understood different app environments (e.g., WhatsApp vs. browser) was non-trivial. Solution: Designed a modular context-handling engine to dynamically interpret actions. Accomplishments that we're proud of Built a working prototype that blends voice and gesture recognition into one system. Achieved cross-environment adaptability , making it usable across multiple applications. Designed with a focus on accessibility , ensuring it benefits differently-abled communities. Created a touchless, hygienic interaction model that has direct use cases in healthcare and education. What we learned The importance of human-centered design in AI projects. <div