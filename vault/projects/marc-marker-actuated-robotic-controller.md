---
slug: "marc-marker-actuated-robotic-controller"
url: "https://devpost.com/software/marc-marker-actuated-robotic-controller"
title: "MARC: Marker Actuated Robotic Controller"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 808
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# MARC: Marker Actuated Robotic Controller

> Meet MARC, the robot that turns text prompts into crisp drawings. In minutes, MARC uses LLM & LinAlg-based framework to drive a robot arm, ready for any setting where ink, motion, & imagination meet.

[Devpost](https://devpost.com/software/marc-marker-actuated-robotic-controller) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]]

**stack** hugging-face, lerobot, opencv, python, pytorch, stable-diffusion

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for marc: marker actuated robotic controller

## Body

3 Minute Overview IRL Setup Inspiration The MARC Transformation Inverse Kinematics Our Challenges Going Forward Inclusivity Usability Inspiration Our inspiration behind MARC stems from wanting to close the gaps between imagination and creation. Today, turning a digital idea into something physical can take hours of calibration and setup, killing spontaneous creativity. High costs also make creative robotics inaccessible. For example, many precision robot arms cost over $10,000, putting them far beyond the reach of students, artists, and hobbyists. And perhaps most importantly, over 285 million people with visual impairments are excluded from visual creation tools; while AI-generated art continues to evolve, those who can’t see it are still unable to feel what it creates. Our project aims to change that by making the process of turning ideas into tangible, touchable art faster, cheaper, and more inclusive. What it does The system takes natural language text prompts and optional image references to generate original artwork, then automatically translates these digital creations into precise physical drawings executed by a robotic arm. Through advanced coordinate transformation and real-time motion control, MARC bridges the gap between AI-generated images and tangible art, delivering sub-2mm positioning accuracy as it brings digital designs to life on paper. How we built it The system architecture consists of four integrated stages. First, AI generation uses a Stable Diffusion XL pipeline with SD 1.5 fallback to create artwork from text prompts. Next, smart vectorization converts PNG outputs to SVG format using Portrace and SVGpathtools while fitting the artwork into 15 cm x 17.3 cm page dimensions. The third stage handles precise coordinate transformation by detecting paper corners via camera vision to build a homography matrix that maps pixels to millimeters, then applies 2D affine transformation formulas to convert page coordinates into the robot's base frame. Finally, robotics execution is achieved through a 6-DOF SO-ARM 101 with degrees-mode control, a custom 3-link planar IK solver, and real-time joint angle streaming for smooth, accurate drawing movements. Challenges we ran into We encountered three major technical challenges during development. First, inaccurate motors caused servo backlash, USB packet loss, and position error accumulation. We solved this by implementing a closed-loop inverse kinematics controller with real-time error correction, achieving sub-2mm accuracy. Second, integrating three frameworks with incompatible APIs (LeRobot using degrees, RustyPot using 0-1, and PySerial using bytes) cost us over 20 hours in rewrites. We built a thin abstraction layer under 200 lines, prototyped all three approaches in 6 hours, and selected LeRobot for its community support and degrees-native interface. Finally, marker physics issues like nib compression and inconsistent ink flow limited us to one marker shape. We designed a universal 3D-printed spring-loaded adapter with 5-18mm diameter compatibility that maintains consistent pressure while absorbing vibrations. Accomplishments that we're proud of We're incredibly proud of building a system that accurately translates drawing coordinates into precise robotic movements, achieving pinpoint accuracy within 2mm. Figuring out how to convert real-world positions into instructions the robot could understand was a major breakthrough, requiring us to use camera vision to map the physical paper space to the robot's coordinate system. Beyond the technical work, we're proud of handling the pressure and rapid problem-solving of our first hackathon, transforming an ambitious idea into a working system that takes a text prompt and produces a physical drawing on paper in minutes. What we learned This project taught us invaluable lessons about collaboration and resourcefulness. We discovered the power of open-source communities, finding extensive documentation and ready-to-use tools like LeRobot that accelerated our development and saved us countless hours of building from scratch. We learned the importance of parallel experimentation, testing multiple approaches simultaneously rather than betting everything on a single solution, which proved crucial when we had to evaluate three different frameworks in just six hours. Most importantly, we realized that constant communication is essential in a fast-paced hackathon environment. Keeping everyone aligned on goals, progress, and challenges minimized confusion and prevented wasted effort from misunderstandings. Working under pressure taught us to balance ambitious technical goals with practical time constraints, and that success comes from both individual problem-solving and effective teamwork. What's next for MARC: Marker Actuated Robotic Controller Looking ahead, we plan to expand MARC's capabilities in several exciting directions. First, we'll add multi-color support to enable more vibrant and complex artwork. We're committed to open-source publishing, making our code and designs available for others to build upon and learn from. To make MARC more accessible, we'll develop a remote control system with a queue feature, allowing multiple users to submit drawing requests from anywhere. We also envision an adaptive learning system that improves drawing quality over time by learning from past movements and corrections. Finally, we want to transform MARC into a multi-modal fabrication platform that goes beyond drawing, potentially supporting different tools and creative outputs to bridge the gap between digital creativity and physical making. <div