---
slug: "roboshade"
url: "https://devpost.com/software/roboshade"
title: "RoboShadow"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 724
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "user/educator_student"
  - "substrate/web_dom"
---

# RoboShadow

> The Art of STEM in Every Shadow

[Devpost](https://devpost.com/software/roboshade) · hackathon [[SpurHacks]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** arduino, css, hardware, node.js, react, tsx

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for roboshadow

## Body

Wiring Diagram CAD Of Pivot Arm CAD Of Base Torque Calculation Inspiration As high school students passionate about robotics and creativity, we often noticed a growing divide between STEM and the arts. While our FRC team focused heavily on technical problem-solving, we realized that many students felt disconnected from engineering due to its lack of artistic expression. Inspired by shadow puppet storytelling and the desire to make robotics more creative and inclusive, we built RoboShadow — a toolkit that brings art and engineering together. What it does RoboShadow is a 4-axis robotic arm mounted with a flashlight, designed to perform shadow puppet shows. It allows students to program movements and create stories using shadows, blending engineering with artistic storytelling. It serves as both an engaging STEAM learning tool and a bridge between creative thinking and technical skills. How we built it Hardware: We designed and built a 4-axis robotic arm using low-cost servo motors and a lightweight 3D-printed frame. The structure is optimized for affordability, classroom durability, and ease of replication by students. Innovation: One of our most innovative features is the compact spherical ball end-effector, powered by two micro servo motors. This design allows smooth and precise control of the flashlight angle in two axes, enabling dynamic shadow casting with easy programming control. Electronics: An Arduino board controls the servos, allowing programmable or real-time movement. Light System: A compact flashlight is mounted at the end-effector to project puppet shadows onto a screen or wall. To ensure smooth and stable movement, the power system for the light is housed at the base of the arm, significantly reducing the torque load on the wrist motors. This design follows a torque-optimized approach, allowing lightweight components at the top and more mass near the base — improving both performance and control efficiency. Software: Example code to automate the arm’s movements, integrated with a custom UI/UX interface built on a Framer-based website. This interface allows users to control light angles and create animated sequences for storytelling. Future development plans include block-based visual programming, digital twin simulation, and advanced features such as teleoperation and VR-based control for a more immersive learning experience. Design: All components were CAD-modeled and optimized for affordability and school use. Challenges we ran into Turning the spherical end-effector from concept to reality was a major challenge. Designing a compact, dual-axis mechanism that could house two motors and allow smooth rotation required multiple iterations in CAD and 3D printing. Minimizing the weight of the flashlight at the end of the arm was also critical. We had to carefully select lightweight components and relocate the power system to the base to reduce torque strain on the motors. Fine-tuning the movement precision while keeping the cost low Balancing artistic storytelling with the engineering complexity Managing time during school, robotics season, and competitions Accomplishments that we're proud of Developed an idea that encourages interdisciplinary STEAM learning Successfully designed, CAD, built a working prototype that combines robotics and art in two days Created a pitch and visual materials for a real-world startup track Inspired peers and educators with a novel approach to robotics education What we learned CAD design, servo control, digital twin simulation, and Arduino programming How to pitch an idea, define a market, and build a unique value proposition The importance of storytelling in both technical presentations and product design That bridging the gap between STEM and the arts creates more inclusive learning experiences What's next for RoboShadow Expanding RoboShadow into a full educational ecosystem by developing a diverse library of modular “puppets” and story packs. These swappable attachments will allow students to explore new narratives, characters, and educational themes — from cultural tales to physics demos — while contributing their own designs to a shared community platform. Creating a digital twin simulator for students to learn programming and controls Developing a block-based coding interface for younger students Partnering with schools and camps to bring RoboShadow into classrooms Expanding the idea into a full STEAM curriculum with lesson plans and storytelling workshops Conduct market research and gather customer feedback through surveys and pilot programs to refine the product, validate classroom impact, and better understand the needs of educators and students. Seeking funding opportunities to support large-scale production, classroom pilot programs, and continued development of advanced features such as visual programming, VR control, and an open-source content-sharing platform. <div