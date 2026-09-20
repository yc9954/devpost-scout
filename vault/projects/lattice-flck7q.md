---
slug: "lattice-flck7q"
url: "https://devpost.com/software/lattice-flck7q"
title: "Lattice"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 637
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
---

# Lattice

> Holographic Communication.Anytime, Anywhere.

[Devpost](https://devpost.com/software/lattice-flck7q) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** c#, c++, kinect-windows-sdk, opencv

## How they structured the write-up

- 💭inspiration💭
- 🤔what it does🤔
- 🔨how we built it🔨
- 💪challenges we ran into💪
- 🏆accomplishments that we are proud of🏆
- 🎓what we learned🎓
- 🔜what's next for lattice🔜

## Body

Banner Logo Server view, Compiled image data from three clients Regular Camera + Skeletal Pose View Depth Perception View 💭Inspiration💭 Every day, technology around us improves. We’re now in an era where we can move away from flat 2D screens and create immersive 3D experiences. VR/AR already exist, but they mostly rely on artificial creations (environment for VR, objects for AR). The next logical step in this direction is to bring the real world into the digital space. Imagine being able to scan anything, like people and objects, in real time and share it live. Technology has as many use cases as you can think of - remote collaboration, medical training, live entertainment, etc. We wanted to make this possible, and with as little expensive tech as possible. 🤔What it does🤔 Lattice is a holographic video capturing system for live 3D reconstruction. It uses multiple (three is best ) Xbox Kinect v2 for real time capture. Data from all sensors is merged into a single, 3D point cloud, creating a full reconstruction, at more than 20 FPS. Connected with the Microsoft Hololens, anybody can view this reconstruction. Essentially, Lattice enables holographic communication, similar to the holoprojector in star wars. 🔨How we built it🔨 Hardware: three Microsoft Kinect v2 Sensors, three laptops (one per kinect as per the SDK) Architecture: Client-Server design - each computer connected to the kinect runs the client app, and they are all connected a central server that synchronizes the data, and merges them to produce the output hologram. Languages: C++, C# Libraries/stack technologies: Kinect for Windows v2 SDK, OpenCV, 💪Challenges we ran into💪 Hardware limitations: The Kinect v2 SDK only supports connecting one Kinect per PC, meaning we had to use multiple laptops just to run the app, even for testing. Sensor interference: The Kinects use LiDAR for distance sensing, and if positioned weirdly, th elasers can interfere with each other, making the detection inaccurate Discontinuation of the Hololens made it hard to find good documentation for using it. It's also incompatible with most new technology since. For example, it only supports Wi-fi 4, which was (and is) a huge bottleneck for the performance of this project, and required us to use a phone as a router. This required us to also connect the computers to the same slower network. 🏆Accomplishments that we are proud of🏆 The most important thing to us is that we created a functional prototype that actually closely aligned with our initial vision. Some notable accomplishments are that we: Made a working project using the Microsoft Hololens, a product they discontinued, with limited developer documentation Achieved record FPS of 23 while running a real-time 3D reconstruction hologram Designed a working noise filter for the kinect sensors 🎓What we learned🎓 How to calibrate multiple sensors - we did lots of research for this, ended up using a visual market and used ICP (Iterative Closest Point algorithm) for refinement. Everything there is to learn about 3D graphics - calibration, error correction, point cloud rendering, etc. Big Picture: Sometimes, it doesn't take brand-new huge-scale inventions to bring us to the next step in tech. With just a few days of focused thinking and coding, we combined existing technology, some of it even old, to bring the future to the present. 🔜What's next for Lattice🔜 This project has so much potential and we've only covered a small portion of it; think of this project as a proof of concept rather than a final product. We will: Implement auto-calibration without a marker sheet Improve the noise-filtering and output a mesh instead of a point cloud to improve visualization resolution Integrate the use of newer sensors in lieu of the outdated Xbox Kinect sensors Develop the application for use with AR headsets that are not discontinued (lol), like the Magic Leap, or Rayban Metas. <div