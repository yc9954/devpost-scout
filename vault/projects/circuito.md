---
slug: "circuito"
url: "https://devpost.com/software/circuito"
title: "Amperon"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 541
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Amperon

> Prompt-Based Circuit Design Platform

[Devpost](https://devpost.com/software/circuito) · hackathon [[NexHacks]]

## Facets

**mechanism** [[graph_reasoning]] [[multi_agent]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[health_clinical]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** devswarm, firebase, firestore, kicad, openrouter, overshoot, react, socket.io, typescript, webrtc, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- ⚠️ challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what’s next for amperon

## Body

Collaborate with coworkers live Learn along the way AR integration Inspiration With the strong experience in robotics found within our team, we know that circuit design is always a major barrier when working with robotics and putting into practice other physically technical ideas. To avoid builders wasting precious time on their projects, we were inspired to create a tool that makes circuit design interactive, collaborative, and accessible. What it does Amperon is an AI-powered, collaborative circuit design and learning platform. Users can describe a circuit in natural language, and Amperon automatically generates a valid schematic. Circuits can then be manually edited, simulated, and explained in real time. Amperon also supports interactive tutorials, real-time collaboration, and AR-powered breadboard analysis, allowing users to scan physical circuits with their phone to detect wiring mistakes and receive step-by-step guidance. How we built it Tech Stack Frontend: React 19, TypeScript, Vite, React Flow, Tailwind CSS, Framer Motion State & Logic: Zustand Backend: Node.js, Express, Socket.io, DevSwarm Cloud & Storage: Firebase Authentication, Firestore AI & Vision: OpenRouter API, Overshoot AI SDK Other APIs: GitHub API (KiCad symbols), WebRTC AI Circuit Generation Used OpenRouter (Claude/GPT models) to convert natural language into structured circuit actions AI places components, connects them correctly, and explains their purpos Supports 60+ components including sensors, logic gates, op-amps, and microcontrollers Circuit Design & Simulation Built an infinite drag-and-drop canvas using React Flow Implemented a custom simulation engine using graph traversal Detects short circuits, open circuits, missing power/ground, and invalid connections AR Breadboard Analysis Integrated Overshoot AI SDK for real-time video inference Supports webcam or phone streaming via WebRTC Detects components, reads resistor color bands, identifies polarity issues, and suggests fixes Collaboration & Persistence Enabled real-time multi-user editing with Socket.io Projects saved using Firestore with localStorage fallback Supports shared sessions and live AR collaboration ⚠️ Challenges we ran into Translating vague natural-language prompts into valid, structured circuit designs Building a real-time simulation engine that works for many circuit types Integrating computer vision for physical breadboard analysis within browser constraints Synchronizing real-time collaboration without conflicting edits Managing multiple APIs and real-time data flows under tight hackathon deadlines 🏆 Accomplishments that we're proud of Built a fully functional AI-driven circuit design platform in under 24 hours Successfully combined AI generation, simulation, AR vision, and collaboration into one system Enabled real-world circuit validation using live camera input Integrated 10,000+ professional KiCad symbols for industry-accurate schematics Created a tool that lowers the barrier to learning electronics and hardware prototyping 📚 What we learned Hardware education improves drastically when feedback is instant and visual AI is most powerful when it assists, validates, and explains, not when it replaces learning Real-time collaboration introduces unique state management challenges Computer vision can meaningfully bridge physical and digital engineering workflows Building agentic AI systems requires careful structure and validation 🚀 What’s next for Amperon We want to expand Amperon into a full hardware development platform. Future plans include deeper simulation support, microcontroller firmware integration, more advanced AR diagnostics, and expanded component libraries. We also aim to improve accessibility for classrooms and makerspaces, enabling instructors to create guided lessons and students to collaborate remotely. Long-term, Amperon could become the “GitHub + Copilot” of electronics, making hardware as approachable, collaborative, and iterative as software development. <div