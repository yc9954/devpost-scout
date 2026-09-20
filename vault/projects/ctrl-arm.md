---
slug: "ctrl-arm"
url: "https://devpost.com/software/ctrl-arm"
title: "Ctrl-ARM"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 498
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "substrate/geospatial"
---

# Ctrl-ARM

> Your muscles. Your moves. Your control!

[Devpost](https://devpost.com/software/ctrl-arm) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**substrate** [[geospatial]]

**stack** css3, electron, gemini, google-a2a, google-adk, html5, matplotlib, myoware-2.0, numpy, pandas, python, react, scikit-learn, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ctrl-arm

## Body

EMG Accesibility ML Decision tree ADK Dynamic modes Our own gesture data Inspiration Traditional input methods like keyboards and mice are limiting, especially for accessibility, gaming, or hands-free computing scenarios. We set out to build a more natural way to interact with computers using the most intuitive interface of all: our own bodies. Turning muscle flexes and arm movements into commands opens up new possibilities for accessibility and immersive experiences. What it does Ctrl-ARM is a muscle-controlled interface that translates bicep flexes and body movements into computer input. Using an EMG or electromyography sensor, we record the small electrical signals muscles produce when they contract using MyoWare EMG sensors and combine them with accelerometer and gyroscope readings from a Seeed Studio XIAO Sense. By fusing these inputs, we capture both the intent of a flex and the motion of the arm. We built a decision tree classifier that learns each user’s unique patterns during calibration and maps them to commands. On top of that, we integrated Whisper for speech-to-text and Gemini for natural language processing, creating a multimodal overlay interface. How we built it We collect EMG activity at 200Hz and stream it alongside IMU data for real-time processing. Our system extracts features that reveal whether a gesture is a quick tap, a sustained hold, or a twist, and passes them through a decision tree optimized for speed and interpretability. We designed the calibration process to adapt to each user’s muscle variability and fatigue. The software ties everything together with a Python backend and an Electron React overlay UI. Challenges we ran into EMG signals vary across people and even change over time. At first, we built a hybrid CNN and gradient-boosted neural net that hit 98.6% accuracy, but it introduced too much latency for real-time use. We solved this by engineering a decision tree pipeline that sacrificed a little accuracy for far better responsiveness. We also had to carefully tune our feature extraction and fuse EMG with IMU signals to reduce false positives and keep inference stable at 200Hz. Accomplishments that we're proud of We engineered a multimodal interface that combines muscle control with voice in real time. With calibration, the system consistently hits nearly 90 percent accuracy, runs smoothly, and reliably distinguishes intentional gestures from background motion. What we learned We learned that calibration is essential for EMG-based systems, and that combining multiple inputs like muscle activity, body motion, and voice produces a more natural and reliable experience. We also learned how important it is to design lightweight ML pipelines that can run in real time on embedded systems, and how sensor fusion strengthens classification. What's next for Ctrl-ARM We plan to expand the gesture set, add support for more muscle groups, and build specialized applications for gaming, accessibility, and professional use. Our roadmap includes haptic feedback, full 3D gesture recognition, and cloud-based training to make the system adaptable to a wider range of users. Made with ❤️ for the future of human-computer interaction :) <div