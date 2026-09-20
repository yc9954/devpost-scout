---
slug: "aegis-jbdfrp"
url: "https://devpost.com/software/aegis-jbdfrp"
title: "Aegis"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 599
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Aegis

> Turn your webcam into a lab technique trainer.

[Devpost](https://devpost.com/software/aegis-jbdfrp) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** git, mediapipe, numpy, opencv, pyinstaller, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aegis

## Body

Inspiration Lab techniques are physical skills that require muscle memory—like riding a bike or playing an instrument. However, unlike learning guitar at home, students can't practice lab techniques outside of a physical lab due to the cost of equipment, safety hazards of chemicals, and lack of space. We wanted to build a tool that democratizes lab training, allowing anyone to practice critical scientific skills like pipetting and titration safely in their own home using just a webcam and a household object What it does AEGIS turns your computer into a virtual lab coach. It uses computer vision to track your hand movements in real-time and provides immediate feedback on your technique. Micropipetting: Uses a pen as a proxy. It tracks the angle of your "pipette," ensuring you hold it vertically, and monitors hand stability. Titration: Uses a water bottle. It checks for a controlled pouring motion and steady holding. Sterile Technique: It monitors your palm orientation and ensures your hand stays within a designated "safe zone" on the screen. The app gamifies the experience with a scoring system, progress bars, and streaks, making scientific training feel like a video game. How we built it We built the entire application in Python using three main libraries: MediaPipe: We used the Hands solution to extract 21 distinct 3D landmarks of the hand. OpenCV: We handled video capture and created a custom graphical interface (UI). Instead of using a standard UI framework, we drew our own buttons, cards, and progress bars directly onto the video frames to make it feel integrated. NumPy: We performed mathematical calculations (trigonometry) to calculate angles between finger joints and calculate variance to detect hand shakiness. We also implemented a Smoothing Algorithm (Exponential Moving Average) to filter out the natural jitter from the webcam feed, making the feedback accurate and readable. Challenges we ran into Hand Jitter: Raw webcam data is incredibly noisy. A user standing still would often trigger "shaking" warnings. We implemented a deque-based smoothing system to average the last 20 frames of movement, stabilizing the readings. Packaging: Bundling MediaPipe models into a standalone .exe was tricky because the models are external binary files. We had to manually map these assets using PyInstaller flags. Accomplishments that we're proud of Real-Time Math: We successfully calculated complex angles (like the tilt of a pen) in real-time (30fps) without lagging the UI. Zero-Cost Simulation: We proved that you can simulate expensive lab equipment effectively using a $0.50 marker or a water bottle. Custom UI: We are proud of the "Cyberpunk/Sci-Fi" aesthetic we achieved without using external game engines. The UI looks polished and responsive. Executable: We successfully compiled the project into a standalone executable, meaning users don't need to install Python or run command lines to use it. What we learned We learned a ton about Computer Vision geometry specifically how to translate X/Y pixel coordinates into meaningful physical data like "degrees of tilt." We also learned the importance of UI feedback loops; if the feedback isn't immediate, the user doesn't correct their posture. Finally, we learned the complexities of dependency management in Python when trying to distribute a script to non-technical users What's next for Aegis In the future, we plan to expand AEGIS to include: Two-Handed Tracking: Simulating holding a test tube in one hand while pouring with the other. Audio Cues: Adding voice feedback so the user doesn't have to look at the text instructions constantly. Mobile Port: Porting the code to iOS/Android, as MediaPipe works great on phones, allowing for even more portable training. More Courses: Adding techniques like Gloving/Gowning and Microscope slide preparation. <div