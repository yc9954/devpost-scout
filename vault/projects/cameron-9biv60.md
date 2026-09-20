---
slug: "cameron-9biv60"
url: "https://devpost.com/software/cameron-9biv60"
title: "Cameron"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 1109
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Cameron

> Cameron turns any camera into an active AI agent — observing, understanding, and acting in real time. It’s the orchestration layer that makes the physical world ready for intelligent systems.

[Devpost](https://devpost.com/software/cameron-9biv60) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[labor_employment]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[transcript_audio]] [[video_visual]]

**stack** claude, gemini, groq, letta, mcp, onnx, opencv, vapi

## How they structured the write-up

- 🌟 inspiration
- 🧠 what it does
- 
- 🛠️ how we built it
- 🧩 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for cameron

## Body

Cameron Landing Page Camera Dashboard Camera Interface Just describe what to look out for and what to do MCP + Tools Integration Chat with 1 or more cameras Workflow Logs 🌟 Inspiration AI has already transformed the digital world — language, image generation, and coding. But the physical world remains largely untouched . Cameron was born from the belief that the next great leap for AI is in making our environments programmable . With AGI and ASI on the horizon , it’s no longer enough for cameras to passively record. Most real-world monitoring tasks follow a simple loop: observe, interpret, and act — yet today’s devices stop at step one. Now, with LLMs capable of reasoning and tool use, we can finally complete that loop. Cameron is our attempt to build the orchestration layer between cameras, sensors, LLM logic, and real-world tools — transforming passive hardware into active AI agents . It enables cameras to detect events, understand their context, and take immediate action — no human review, no delay . Just real-time intelligence, deployed in the physical world . 🧠 What it does Cameron is a smart camera orchestration platform that transforms any ordinary camera into an intelligent, real-time AI agent . It bridges the gap between seeing and acting — automating surveillance, monitoring, and response . Just describe what to look out for and what to do, and Cameron builds the logic, watches the video, and takes action when it matters . Whether it’s detecting strange breathing , spotting unusual events , or triggering alerts , Cameron combines live video analysis with large language model reasoning and multimodal outputs like email, SMS, and voice calls . You can build workflows visually through a drag-and-drop interface or even speak them into existence using natural language . Cameron connects seamlessly to your tools and services, giving you a flexible, scalable way to make the physical world more intelligent, responsive, and safe . One framework, infinite applications: Cameron adapts to any environment — from manufacturing and retail to elder care, warehouses, and animal care, to name just a few — empowering smarter, safer spaces everywhere . 🛠️ How we built it We built Cameron with a modular, scalable architecture designed to bridge perception, reasoning, and action. The system connects live video streams, LLM-powered logic, and real-world tools — all orchestrated through a visual workflow editor. 🤖 AI & ML We used a combination of models and tools to enable real-time, intelligent camera analysis: YOLOv8 (ONNX) for fast, on-device object detection and bounding box generation OpenCV for image segmentation, frame manipulation, and preprocessing Gemini Video Model for high-level video analysis, enabling richer contextual understanding of scenes and events ArcFace (ONNX) for identity recognition via facial embeddings ONNX Runtime Web to run these models directly in the browser, eliminating the need for backend inference On the language side, we integrated: Gemini Speech-to-Text for converting live or recorded audio streams into transcripts Gemini 2.5 for generating full node graph configuration files from natural language Letta with Groq API for ultra-fast reasoning and LLM-based control flow Claude MCP for orchestrating multiple AI agents that handle perception, planning, and action simultaneously This hybrid system lets Cameron operate with multimodal awareness — combining sight, sound, and structured reasoning to power intelligent, real-time decisions. 📢 Comms & Alerts Cameron supports a wide range of real-world actions. We used the VAPI SDK for smart voice calls with AI-generated summaries and EmailJS for email notifications. We also included browser push notifications and speech synthesis as a fallback layer for local alerts. 🧩 Data & Logic Workflows are stored as JSON-based node graphs , which can be exported or imported easily. We use LocalStorage to persist user configuration between sessions. At the heart of it all is a visual node graph editor that lets users connect events to actions — whether through drag-and-drop or natural language. 💻 Frontend We used React 19 + TypeScript to build a modern, scalable interface. Tailwind CSS gave us rapid, consistent styling across components, while Lucide React provided clean, elegant icons. Navigation is handled via React Router , with real-time video rendered using the Canvas API and WebRTC . To offload compute-heavy tasks, we used Web Workers to run inference models in the background without blocking the UI. This setup makes Cameron highly responsive, even when running live detection. This combination of real-time video processing, in-browser AI, and multimodal orchestration allows Cameron to turn any ordinary camera into an intelligent, autonomous agent — ready to observe, understand, and act. 🧩 Challenges we ran into One of the biggest challenges was building a flexible system that could scale across diverse environments — from elder care facilities to industrial warehouses. Designing a workflow engine that balances simplicity (for non-technical users) with power (for advanced automation) was a constant push and pull. We also faced technical hurdles around real-time video processing, integrating LLMs for reasoning without introducing lag, and ensuring the system could act on outputs reliably — whether that meant triggering an alert, sending a message, or controlling IoT devices. 🏆 Accomplishments that we're proud of We’re proud of turning passive cameras into something truly interactive — creating a no-code platform where anyone can build smart monitoring workflows using natural language. We successfully integrated multimodal AI reasoning, built a visual editor, and demonstrated real-time detection-to-action loops — all in a lightweight system that works on top of existing camera hardware. Cameron isn't just a proof-of-concept — it's a working prototype ready to make real spaces smarter, safer, and more responsive. 📚 What we learned We learned that the future of AI isn’t just digital — it’s physical. Real-world applications require bridging perception, reasoning, and action, all in real time. We also gained deeper appreciation for UI/UX challenges in AI systems. Giving users power while keeping things intuitive takes more than just engineering — it takes thoughtful design. And finally, we saw firsthand how LLMs can unlock entirely new interfaces — ones where logic can be spoken, not just coded. 🚀 What's next for Cameron ⏩ Short-Term Improved model support (more classes, re-identification, better tracking) Mobile app for remote monitoring and workflow editing More node types (geofencing, sensor fusion, anomaly detection) 🔮 AI/ML Features Predictive alerts: “This person returns every night at 3 AM” Training user-specific models based on environment and faces Multi-language natural language support for voice and UI 🧱 Platform Upgrades IoT integrations: Smart locks, alarms, and sensors Cloud sync & remote deployment options API & plugin system for third-party integrations 🌍 Community Focus Open source core: Let others build modules, tools, and models Developer documentation and starter templates Community-built alert packs and workflow presets <div