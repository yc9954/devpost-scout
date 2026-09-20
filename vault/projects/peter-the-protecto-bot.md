---
slug: "peter-the-protecto-bot"
url: "https://devpost.com/software/peter-the-protecto-bot"
title: "PETER the ProtectoBot"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 493
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "substrate/video_visual"
---

# PETER the ProtectoBot

> PETER: a *True* Full Stack smart Sentry Robot. While most teams built an app, we built a smart physical Machine. PETER. (No acronym) From fundamental hardware to Applied Imitation-learning AI

[Devpost](https://devpost.com/software/peter-the-protecto-bot) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
  <sub>weak: provenance_signing</sub>
  <sub>weak: developer_tools</sub>
**substrate** [[video_visual]]
  <sub>weak: sensor_telemetry, structured_db</sub>

**stack** autodesk-fusion-360, c++, cuda, esp32, imitationlearning, love, passion, python, pytorch

## Body

prototype build poster board final build1 final build2 maze build for training speaker system compact design Sentry mode camera view MAZE p1 Maze p2 Maze p3 Maze p4 -Inspiration PETER. A Sentry Robot to secure our house in our absence is a dream, but more importantly, we wanted to showcase what True Full-Stack Robotics looks like. We were inspired by the challenge of bridging the gap of Physical Ai and hardcore electronics. We combined raw electrical engineering with high-level computer vision in a single 24-hour sprint. All to showcase our Proof of concept of a our Sentry Robot PETER. -What it does PETER is a 2-wheel mobile robot equipped with a camera, a custom speaker system, and a predictive AI brain. It operates in three distinct modes: -> Teleoperation Mode: Full manual control via our Python app, recording input and camera flow in real-time. -> Gesture Control: The robot identifies and physically follows your index finger using computer vision. -> Sentry Mode : The robot navigates autonomously. It uses a custom trained AI model to predict the environment's state up to 1 second in the future to overcome camera transmission lag and was trained using real collected data. Bonus Feature: It features a custom-soldered speaker system that gives PETER a distinct personality -> specifically, he sounds exactly like an idling diesel car. -How we built it We divided the work into three layers: Hardware, Electronics, and Intelligence. (Hardware): We CADed the chassis from scratch to fit our specific components found arround the electronics zone and 3D printed the body. (Electronics): instead of using a pre-made audio module (coz we didnt have any), we designed and soldered our own Operational Amplifier (Op-Amp) circuit to drive the speaker ( we found a random chip and proceeded to have 10h of straight elec debugging) . We used an ESP32s3-Sense for the vision and control system. (AI & Software): We built a Python application via UDP and a Local network for the Realtime video feed. Model Architecture: We utilized a ResNet architecture. We started with pretrained weights on geometric forms (Transfer Learning) and then fine-tuned the model on a custom dataset we collected during the hackathon by moving the robot in the Maze. -Challenges we ran into The Latency Gap: Streaming video over Wi-Fi introduced a lag that made real-time control impossible at high speeds. This forced us to develop the model with "Future Prediction". The "Diesel" Audio: Building a custom Op-Amp from scratch with a randomly found chip was hard. Our first iteration introduced significant signal noise, which is how PETER accidentally acquired his signature "diesel engine" purr. It's a feature tho. An endless nightware of Hardware and software integration of feature. -Accomplishments that we're proud of Reliable Remote control with video stream and data collection pipeline. Custom Op-amp circuit for a speaker Custom Cads -What we learned AI implementation on physical robot is the coolest thing to see. Hardware never stops being a nightmare <div