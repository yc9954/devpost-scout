---
slug: "dum-e-kgx6at"
url: "https://devpost.com/software/dum-e-kgx6at"
title: "DUM-E"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 829
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
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# DUM-E

> DUM-E is an NLP-powered robotic arm that uses CV and fast inference to perform actions.

[Devpost](https://devpost.com/software/dum-e-kgx6at) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**substrate** [[geospatial]] [[video_visual]]

**stack** arduino, c++, cad, groq, opencv, python, raspberry-pi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dum-e

## Body

Photo of DUM-E! Our homography and CV in action! (Segmentation model and hand joint model) the og dum-e arm from iron man Inspiration Inspired by Iron Man’s DUM-E , we set out to build a robotic arm that could act as a versatile assistant on the workspace. Most robotic arms are limited to pre-programmed routines, but we wanted something intelligent, an arm that could understand natural language commands, reason about its environment, and execute complex tasks on demand. Our goal was to combine NLP, computer vision, and real-time robotics control into a single, responsive system. Initially, we thought of using VLAs. However, they are limited in their context and are also an active area of research. Thus, we designed our own pipeline which combines fast inference with reverse-IK and homography to achieve similar results that can scaled much better. What it does DUM-E can interpret both spoken and typed commands to manipulate objects with precision. Some of the things it can do include: Sorting parts on a cluttered table. Holding tools while the user works. Executing multi-step tasks based on natural language instructions. Waving, showing sentiment, and other actions. By integrating NLP with computer vision, DUM-E doesn’t just react, it understands the scene and decides the best way to interact with objects. Its design is highly generalizable, meaning it can handle new tasks without requiring custom programming. How we built it The arm itself has 3 standard servos and 3 microservos , controlling yaw, three levels of pitch, roll, and the claw. The pipeline works as follows: Object Detection: A webcam captures the workspace, and OpenCV draws bounding boxes using a segment model onto a birds-eye warped frame through homography. LLM Analysis: Pre-processed images are sent to a multimodal LLM (via Groq) for fast inference. The LLM analyzes object positions and decides which actions the arm should take. It can even access APIs or online data to enhance its reasoning. Command Execution: The LLM sends the instructions to a Flask server on the Raspberry Pi, which communicates with the Arduino Uno. Servo movements are calculated using inverse kinematics to ensure smooth and precise actions. 5DOF IK Arm: The Arm consists of 5 degrees of freedom (1 yaw, 3 pitch, 1 roll + a claw), where we use inverse kinematics to map our arm onto a 3D Cartesian plane for movement. Combining this with homography for accurate 2D Cartesian alignment allows us to open up more potential actions DUM-E can do. NLP stack: The LLama Maverik 109B multimodal was used through Groq so that we can pass in homography and CV detections with cords directly into the model. The Whisper Large V3 was used for speech-to-text capabilities. The system uses a feedback loop: real-time arm positions are sent back to the LLM, ensuring consistent and accurate manipulation. Challenges we ran into Building DUM-E was far from straightforward. Some of the biggest hurdles included: Translating natural language into precise movements across multiple degrees of freedom. Ensuring robust object detection under variable lighting and cluttered environments. Integrating multiple software and hardware layers (LLM, Raspberry Pi, Arduino, CV, voice interface) while keeping latency low. Fine-tuning inverse kinematics to make movements smooth and accurate. Adding conversions and bounds to zero our servos to work with the IK effectively and intuitively. Working with the circuitry as each of the large servos could take up to 2A and small servos 1A, meaning 9A of current running in total. Managing wiring with a 5DOF arm with essentially full rotation capabilities. Each challenge required iterative testing and creative problem-solving, but overcoming them made the system much stronger. Accomplishments that we're proud of Successfully combining NLP, computer vision, and robotics hardware into a seamless system. Achieving low-latency, smooth arm movements across multiple degrees of freedom. Creating a generalizable platform capable of executing diverse commands without extra programming. Implementing a feedback-based control loop that improves accuracy and reliability. It’s incredibly rewarding to see DUM-E respond in real-time to voice commands and perform tasks with precision. What we learned Through this project, we gained experience bridging advanced NLP with physical robotics. We learned about modular software design, real-time object detection, homography-based localization and vision, and inverse kinematics. Perhaps most importantly, we discovered the value of feedback loops for ensuring consistent and precise execution in multi-layered systems. We also learned that the breadboard can surprisingly handle a lot of current relatively well, and that sometimes adding four extra power supplies isn't too bad of an idea! What's next for DUM-E Looking forward, we plan to: Add adaptive grasping for irregular and fragile objects. Expand NLP understanding to handle multi-step, context-aware instructions. Implement autonomous task planning for DUM-E to sequence actions independently. Optimize the pipeline for faster inference and lower latency. Explore additional sensors like force or tactile feedback. Develop a portable, standalone version for broader deployment. Use a depth camera for more accurate 3D object processing. With these improvements, DUM-E will become an even more intelligent, versatile assistant for any workspace. <div