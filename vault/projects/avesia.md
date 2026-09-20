---
slug: "avesia"
url: "https://devpost.com/software/avesia"
title: "Avesia"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 993
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Avesia

> Making Cameras Smart

[Devpost](https://devpost.com/software/avesia) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[transportation]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, fastapi, geminiapi, html, javascript, json, mongodb, node.js, opencv, overshoot, pytest, python, react, shadcn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for avesia

## Body

Landing Page Project Page AI Node Maker Analytics Inspiration With the world of LLMs and agentic AI thriving, we were excited to find a new application with the hope to benefit humanity by providing a tool to assist in everyday lives. If I had a nickel for every time I had to run around the house to get the door for the deliveryman, I'd be rich! But this has the potential to be much more than just ring doorbells. With crime rates skyrocketing in my neighbourhood, it'd be extremely useful if our camera system could automatically detect car theft and burglary to create a safer world for me and my siblings to grow up in. With the growing popularity of surveillance methods, whether it be ring cameras, driveway cameras, or mall and grocery store cameras, there are vast applications for providing a simple method to program any camera with the help of our AI agent workflow. We hope to inspire and protect all users, regardless of technological experience, to take security into their own hands through Avesia. What it does Avesia is a visual, no-code video monitoring platform that enables users to build intelligent surveillance workflows using a drag-and-drop node editor, inspired by great engine-based tools such as Unity and n8n. Users create workflows using three types of nodes: Conditions (when/how): Define thresholds like specific counts, lighting conditions, time constraints, or custom criteria Listeners (what to detect): Monitor for objects, people, motion, faces, license plates, or custom events Events (actions to take): Trigger email, SMS notifications and control your Smart Home environment when critical milestones are met. The system processes live video feeds using Overshoot SDK's vision AI, generates structured JSON outputs, and automatically triggers actions when listener conditions match their connected condition thresholds. Everything runs in real-time through the browser, with no complex setup required. And the best part? It can solve a range of use cases, from matters of national security to detecting the success of your local bake sale. How we built it Frontend: React with Vite for the main application React Flow for the visual node editor interface Overshoot SDK for real-time video processing in the browser Custom hooks ( useOvershootVision , useOvershootVideoFile ) for video stream management Modern UI components with Tailwind CSS Backend: FastAPI (Python) for the REST API MongoDB Atlas for persistent project, node storage and general analytics Gemini-powered AI Agent to guide new users to easily set up camera workflows Node.js service for browser-based vision processing coordination Real-time result validation and a Boolean correction system Structured output schema generation for typed JSON responses Key Features: Visual workflow builder with drag-and-drop nodes Real-time video analysis with structured outputs Project-based node management (save and load workflows) Automatic prompt generation from node configurations Result validation to ensure boolean values match descriptions Challenges we ran into Model Inconsistency : Due to high traffic on Overshoot's API, we faced hours of challenges, where the only way we could gain a consistent model analysis was through simple, concise prompts that may often not reflect the initial goals our team had. To mitigate this, we spent hours fine-tuning to find the correct balance between token optimization and effectiveness. Motion Monitoring : To save on API usage, we had to build a motion detection system that would throttle API usage based on whether there was movement in the environment. However, just detecting if the frames were equal was not sufficient. There may be minor changes in the camera, such as camera shake or lighting changes, which would cause very little optimization to be made. To combat this, we use a frame matching algorithm and finetuned a similarity threshold to ensure it could detect slow movements but would not detect vibrations from the environment, causing the laptop screen to shake. Node development : Due to the high variety of node combinations, output types and unique conditions, building the nodes to be a drop-and-drag, graph-esque system offered unique algorithmic challenges as well as a tedious amount of work, the problem being solved through hours of collaboration. Accomplishments that we're proud of Visual Workflow Builder : Created an intuitive drag-and-drop interface that makes complex video monitoring workflows accessible to non-technical users. AI Agent : Built an intelligent agent that could build unique detection paths allowing for a stronger user experience and control. Seamless Integration : Successfully integrated Overshoot SDK with a custom backend, enabling real-time video processing with structured outputs. System Architecture : Implemented a full project system with MongoDB persistence, allowing users to save and manage multiple monitoring workflows, connected to a FastAPI backend with roughly 10 unique endpoints and an aesthetic React frontend with fully implemented user interaction feedback. What we learned Async Coordination : Managing real-time data flow between browser, Python backend, and Node.js services requires careful and thorough error handling with timeout management to prevent the application's websockets or connections from disconnecting and dropping down. Visual Programming UX : Building intuitive node-based editors requires thoughtful UX design - connection rules, node types, and visual feedback all matter for usability. What's next for Avesia More Node Types : Add support for more rule-based environmental condition types (time of day, surrounding temperature, wind speed), listener types (sound, gesture recognition, facial recognition), and event types (Slack notifications, Google Maps integration). - Multicamera Systems and Camera Control : Add support for multiple cameras to act as both event type nodes and listener nodes, allowing for cameras to interact simultaneously like a hive mind system. Additionally, adding more camera features, allowing for night vision modes, zoom-ins, and speaker/microphone support. Advanced Threshold Logic : Support for complex boolean logic (AND, OR, NOT), to combine multiple conditions in unique and interesting ways. Mobile App : Create mobile apps for iOS and Android to receive notifications and manage workflows on the go. Machine Learning Improvements : Fine-tune prompts and validation logic based on real-world usage patterns to improve accuracy, working with a huge database of already trained YoloV8 models. <div