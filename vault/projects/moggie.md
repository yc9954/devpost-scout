---
slug: "moggie"
url: "https://devpost.com/software/moggie"
title: "MOGGIE"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 893
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/mental_health"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MOGGIE

> QNX-powered, computer-vision-driven viral arcade system. Compete in instant 1v1 battles from online trends like six-seven and mogging. Portable and optimized gaming on Raspberry Pi.

[Devpost](https://devpost.com/software/moggie) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]] [[finance_payments]] [[mental_health]] [[transportation]]
**user** [[developer]] [[frontline_worker]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** mediapipe, opencv, pika, pygame, python, qnx, raspberry-pi, redis, sdl2

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for moggie

## Body

Inspiration We've seen many recent trends, like looksmaxxing, and have realized that they often encourage harmful behavior. We believe the solution is to foster open conversation and break down the stigma surrounding these topics, thereby promoting healthy decisions. When people can get together and feel comfortable sharing their struggles, they can find support and encouragement from those they value and whose opinions matter. What better way to break the ice than with a party game? What it does Moggie is a portable AI party-game kiosk running on a Raspberry Pi 5 with QNX. Players stand in front of the camera and compete in fast physical and facial-expression mini-games, including hand-motion challenges, face mirroring, and emoji expression matching. The games can be understood instantly, leading to quick, accessible, and fun viral gameplay. Moggie lets people bond over the latest trends and socialize rather than isolate, helping address a major factor in the mental health issues and stigma associated with these internet phenomena. On a more technical level, we are running pygame on a Raspberry Pi 5, very generously provided by QNX, along with their real-time, microkernel-architecture operating system designed to handle time-sensitive applications. We wrote a custom camera driver from scratch to enable the provided camera to connect with our pygame pipeline. Each frame is passed through MediaPipe to produce body landmarks and geometry detection. Results are then timestamped and polled by the game frame by frame. A SQLite database stores per-game sessions and keeps track of the top scores in a leaderboard. Moggie is made to be shareable. Innately, it leads to viral shareable clips as the games are trendy and instant. Similar to other viral games, players get a ready-to-share clip after a MOGGIE session. Hit a high score or make a smart play? Pika + MOGGIE backend has a clip ready for your social media. How we built it We brainstormed extensively as a team, then drafted up a design document with LLM tooling. We mainly used Codex 5.5 for most of the code implementation while focusing on what human brains still do best: ideation and creativity. We used our complimentary Claude credits to build the most complicated part of our application: the camera driver. We spent our time making UI/UX design choices, identifying ways to solve problems we encountered during implementation, and ensuring our project remained cohesive as multiple developers worked in parallel. The QNX camera path was the deepest systems work. We configured the QNX Sensor Framework for the Raspberry Pi Camera Module 3 / IMX708 stack, then wrote moggi_camgrab, a small C program that uses CamAPI’s read-only viewfinder path to receive NV12 frames. The grabber emits frames through a custom lightweight MGF1 wire format. A Python backend reads the stream on a background thread, keeps only the newest frame to avoid latency buildup, converts NV12 to BGR with OpenCV, and hands frames to the Pygame game screens. We also optimized the game around the Pi’s constraints. For example, we disable face tracking during the hand-motion game, use a faster, lightweight hand-motion fallback where needed, decimate camera frames in native code, and keep scoring/rendering independent from slower CV updates. Challenges we ran into One of the main goals of our product is to keep it as lightweight and performant as possible; thus, we opted to test out the QNX operating system. However, because there was no existing camera functionality, we spent much of our time programming a C driver to enable our game to capture frames from the attached camera module. Additionally, the performance on a Pi is obviously not as powerful as on a MacBook Pro, but, because of our commitment to portability and affordability, we continuously iterated and optimized, like removing unnecessary face-tracking during a hand-movement-oriented game, to ensure that it still ran on the Pi. Accomplishments that we're proud of We got a real Raspberry Pi Camera Module 3 feed running inside a Pygame game on QNX, a use case in uncharted territory for QNX. That required: Configuring the QNX Sensor Framework for the Pi 5 camera path Building a native CamAPI frame grabber in C Designing a tiny custom NV12 stream protocol Bridging native camera frames into Python/OpenCV/Pygame Running local hand and face CV on constrained hardware Tuning the game so rendering and scoring stay responsive even when CV is slower We are especially proud that Moggie is not just a web mockup. It is a real embedded kiosk running on sponsor hardware with a live camera, HDMI display, local CV, and persistent gameplay state. We are able to play CV games at near-60 fps! Also, Moggie auto-clips and generates fun UGC-ready videos using Pika to increase virality. Hit a clip in Moggie and share with your friends! What we learned By focusing on optimization, we can run compelling applications even on simple hardware. In an age when the answer to every problem seems to be throwing more compute or RAM at it, we proved that it's still possible to craft well-designed, performant software that maximizes hardware utilization and the onboard OS. What's next for moggie We plan on expanding moggie to include more games. Eventually, we plan on creating a custom container and peripherals to actually sell as a party game! You can take Moggie to your friend's house, fun parties, mixers, and more! It attracts attention instantly and creates fun shareable moments. <div