---
slug: "wingman-9xok8b"
url: "https://devpost.com/software/wingman-9xok8b"
title: "Wingman"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 484
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/disaster_emergency"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Wingman

> Wingman uses Snap Spectacles to control a robot that moves, grabs, and sees where humans can’t by pointing to navigate, gesturing to grasp, and capturing 3D scenes through depth-sensing AR.

[Devpost](https://devpost.com/software/wingman-9xok8b) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[disaster_emergency]]
**user** [[frontline_worker]] [[patient_family]]
**substrate** [[geospatial]] [[video_visual]]

**stack** fastapi, snap, websocket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wingman

## Body

Inspiration During disasters and times of crisis, first responders often face an impossible choice: risk their lives to search for survivors or stay back and lose precious time. We wanted to eliminate that choice. Wingman was born from the idea that technology can extend human presence into unreachable worlds - using wearable AR to control a robot as naturally as moving your own body. Instead of doing things that humans can already do, we wanted Wingman to fill the gaps of our abilities. What it does Wingman is a Snap Spectacles–controlled robot that brings human intuition into robotics. It combines three seamless functions: Move - Point to a location through the Spectacles’ depth-sensing AR , and the robot autonomously navigates there. Grab - Use hand tracking to control the robot’s arm and gripper. Snapshot - Capture and explore 3D depth images of the environment, rotating views to reconstruct the scene virtually. Together, these features allow people to move, manipulate, and visualize in places humans can’t safely go. How we built it We integrated Snap Spectacles , AR world data , and robotic motion control through a low-latency pipeline: Hardware: A mobile LeKiwi robot with a 6-DOF arm and gripper, paired with Snap Spectacles for spatial mapping, hand tracking, and 3D capture. Software: FastAPI + WebSocket for real-time communication. Snap Lens Studio API to extract hand-tracking data and AR anchors. OpenCV for vision processing and coordinate mapping. Three.js for 3D depth visualization. Inverse kinematics and path planning for smooth, intuitive arm control. Challenges we ran into Achieving low-latency control between the Spectacles and the robot. Translating AR spatial anchors from Snap’s coordinate system into real-world robot coordinates. Maintaining precise gesture-to-motion mapping without drift or jitter. Synchronizing depth capture and 3D reconstruction for accurate spatial visualization. Accomplishments that we're proud of Building a fully functional prototype that unites AR, robotics, and real-time control . Using Snap Spectacles not just for vision, but as a wearable interface for spatial movement, manipulation, and perception. Creating a 3D visualization system that reconstructs physical environments from depth snapshots. Designing an experience that feels more like collaboration with a companion than controlling a machine. What we learned We discovered how powerful AR becomes when combined with robotics - not as a separate layer of information, but as a natural bridge between human intent and machine action. We also learned the importance of designing for intuition over complexity : when the interface feels human, the technology disappears, and the experience becomes seamless. What's next for Wingman We plan to expand Wingman’s capabilities with: Voice commands (“Wingman, move to the doorway” or “pick up the red object”). Autonomous exploration using SLAM and AI-driven scene understanding. Edge processing on Spectacles for faster local gesture interpretation. Multi-step planning for performing complex tasks from natural language. Our ultimate goal: make Wingman a universal telepresence assistant - a true wearable-controlled companion for exploration, safety, and discovery. <div