---
slug: "chessmate-nwygvq"
url: "https://devpost.com/software/chessmate-nwygvq"
title: "ChessMate"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 461
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/immigration_refugee"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/video_visual"
---

# ChessMate

> ChessMate is a smart chess companion: play on a web app or real board with motorized pieces, get instant coaching, and voice controls for accessibility, making chess inclusive and interactive.

[Devpost](https://devpost.com/software/chessmate-nwygvq) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[immigration_refugee]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[video_visual]]

**stack** agents, ai, arduino, groq, nextjs, python, raspberry-pi, react

## How they structured the write-up

- 🌍 inspiration
- ♟️ what it does
- 🛠️ how we built it
- ⚡ challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for chessmate

## Body

Logo Team Computer Vision Contraption Chessboard Group Photo Wiring Cutting Stand 🌍 Inspiration All of us come from immigrant families and wanted to relive the experiences of playing chess with family abroad. ChessMate brings the joy of real chess to people separated by distance. Where one person plays virtually, and the pieces move on the board in real-time. We also wanted to make chess more inclusive and accessible, especially for those who may struggle with mobility or vision. ♟️ What it does ChessMate is a smart chess companion and assistant that helps you improve at chess, whether playing alone or virtually with others It blends physical and digital gameplay by moving pieces on a real chessboard through a robotic gantry system. Features accessibility options such as voice commands to move pieces and AI guidance for coaching and practice. 🛠️ How we built it ChessMate is powered by a 2D, dual-axis gantry that perceives, reasons, and executes chess moves on a physical chessboard. The gantry runs on two NEMA 17 stepper motors controlled by DRV8825 drivers. The Raspberry Pi 5 serves as the brain: Uses a computer vision (CV) model with a webcam to detect piece movements. Runs a chess engine to reason and decide the next move. Executes a pathfinding algorithm to determine the best way to move pieces without collisions. Instructions are sent to an Arduino, which translates them into motor movements. Chess pieces are magnetized and moved using an electromagnet attached to the gantry. On the software side, the web app integrates AI agents, coaching features. ⚡ Challenges we ran into The two biggest challenges we can into were building the 2nd axis of the gantry, and the Computer Vision system to detecting chess pieces. In addition, calibrating the pathfinding algorithm for smooth, collision-free piece movements was tricky and time-consuming. Integrating multiple hardware and software components (Pi, Arduino, motors, CV, chess engine) into a seamless system. Our two most significant issues took up to majority of the hackathon period to solve, and only worked as we worked simultaneously and collaborated 🏆 Accomplishments that we're proud of The finished product looks good and the 2d gantry works flawlessly. Successfully merged AI agents with both the physical board and web app, providing live coaching and guidance. Built a system that is both functional and user-friendly, despite the short hackathon timeframe. 📚 What we learned Hardware hacks require significant planning, testing, and take more time than anticipated. Importance of team collaboration and parallel problem-solving to meet deadlines. 🚀 What's next for ChessMate Adding a built-in camera system so that remote players can appear via webcam, allowing the physical player to see and talk to them directly during gameplay. Exploring self-learning AI that adapts to a player’s style and provides tailored coaching. <div