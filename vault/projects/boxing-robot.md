---
slug: "boxing-robot"
url: "https://devpost.com/software/boxing-robot"
title: "MIRAI"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 580
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
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# MIRAI

> Teaching robots to see, listen, and move like us. MIRAI is an experimental human-robot interaction framework that enables natural motion and voice-based control of robots.

[Devpost](https://devpost.com/software/boxing-robot) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]]
**substrate** [[geospatial]] [[video_visual]]

**stack** mediapipe, opencv, pinocchio, python, sdk2, speechrecognition, unitree

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for mirai

## Body

Inspiration We were inspired by the idea of making robots move more naturally — not through pre-programmed motions or scripts, but by understanding and reacting to human movement the same way humans do. Watching fighters and athletes move made us wonder: what if a robot could learn to mirror that instinctively, using only vision and sound? That curiosity turned into MIRAI — Machine Interaction through Real-time Awareness and Imitation, a system that lets a robot see you, follow you, and even understand your voice. What it does MIRAI allows a Unitree G1 humanoid robot to perceive, imitate, and respond to human behavior in real time. Using a camera and microphone, the robot can: Detect and mirror human upper-body movements with natural motion. Follow the user’s position as they move through space. Respond to voice commands such as “follow me,” “stop,” or “mirror mode.” The result is a robot that doesn’t just move — it interacts. How we built it We combined several cutting-edge tools and frameworks to bring MIRAI to life: MediaPipe and OpenCV for fast, real-time human pose detection and tracking from a camera feed. Pinocchio for inverse kinematics, converting human joint angles into robot joint configurations. SpeechRecognition for our speech-to-action pipeline, translating voice commands into behaviors that the robot executes. A lightweight Python control layer built on Unitree SDK2, which sends motion commands directly to the robot’s motors. Finally, we added motion smoothing and timing filters to eliminate jitter and make the robot’s imitation feel human — fluid, balanced, and reactive. Challenges we ran into Human-to-robot mapping: Translating human motion data into robotic joint space was a major challenge, given that human anatomy doesn’t directly match the robot’s structure. Latency issues: Early tests showed slight delays in movement response, which we mitigated through data smoothing and async pipelines. Balance and stability: The G1 needed custom calibration to maintain stability while performing large arm movements during imitation. Speech reliability: Background noise often interfered with command recognition, requiring dynamic audio filtering. Accomplishments that we’re proud of Achieved real-time motion imitation with minimal lag. Built a working speech-to-action system that allowed natural control of the robot. Developed a human-aware following mode, enabling the robot to track user position while maintaining a safe distance. Created an integrated control loop that combines vision, audio, and motor control — a step toward unified human-robot interaction. Seeing the robot shadow our movements and respond to our voice felt like the start of something bigger — almost like watching fiction turn into reality. What we learned The importance of synchronizing multimodal systems (vision + audio + actuation). Fine-tuning inverse kinematics requires both math and intuition. Smooth motion is more impactful than just accuracy — a small delay feels more human than a perfect but robotic response. Combining multiple AI pipelines (speech and pose) is surprisingly powerful when done in real time. Most importantly, we learned that true human-robot interaction isn’t just about sensors — it’s about creating presence. What’s next for MIRAI We’re looking to expand MIRAI beyond shadowing and speech commands into intent recognition — where the robot predicts motion or responds emotionally to interaction cues. Our next milestones: Add gesture-based control and multi-person tracking. Port MIRAI to more robot platforms for teleoperation and rehabilitation robotics. Integrate LLMs for contextual speech understanding, allowing conversational coordination. Explore industrial and healthcare applications where intuitive motion mirroring could enhance safety and collaboration. MIRAI started as a boxing robot. It’s quickly becoming a framework for natural human-robot symbiosis. <div