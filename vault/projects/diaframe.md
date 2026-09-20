---
slug: "diaframe"
url: "https://devpost.com/software/diaframe"
title: "Sematic"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 564
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Sematic

> AI Powered Voice-Based Systems Design Tool

[Devpost](https://devpost.com/software/diaframe) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** amazon-dynamodb, amazon-web-services, amplify, auth0, gemini, reactflow, windsurf

## How they structured the write-up

- inspiration ✨
- what it does 🗣️➡️📊
- how we built it 🛠️
- challenges we ran into 🧗
- accomplishments that we're proud of 🏆
- what we learned 🧠
- what's next for sematic 🚀

## Body

GIF landing dashboard tool technology Inspiration ✨ Manually drawing diagrams during a brainstorm or technical discussion is a flow-killer. The moment someone has to stop talking to click, drag, and type, the creative momentum is lost. We wanted to build a tool that could visualize ideas as naturally as speaking, turning conversations directly into collaborative designs. What it does 🗣️➡️📊 Sematic is a spatially-intelligent, collaborative whiteboard that transforms voice commands, text prompts, and even image uploads into perfectly structured diagrams in real-time. You can simply talk to it—saying "add a user database connected to the auth service" or "delete all the nodes on the right"—and Sematic executes the command. It doesn't just blindly add elements; it understands the entire diagram's state, including the 2D coordinates and connections of existing nodes. This spatial reasoning allows it to make intelligent layout decisions, ensuring the generated diagram is clean, organized, and contextually aware. How we built it 🛠️ We built Sematic on AWS Amplify Gen 2, with AWS Lambda functions orchestrating calls to Google's Gemini 2.0 Flash API. Here's the pipeline: Multimodal Input: The React frontend captures voice commands as WebM audio, which is uploaded directly to Gemini's File Manager. Context is Key: We send Gemini more than just the audio; we provide a complete snapshot of the current diagram, including the precise coordinates, sizes, and connections of every element. AI Processing: Gemini uses its advanced multimodal capabilities to transcribe the audio and process it alongside the spatial data of the diagram. Structured Commands: The API returns a structured JSON payload containing exact commands for the frontend (e.g., createNode, connectNodes, deleteById) with precise positioning data. Real-time Execution: Our React app parses this JSON and executes the commands, updating the diagram for all collaborators instantly. Challenges we ran into 🧗 Making the AI's spatial reasoning robust was a major challenge. We had to design a custom, simplified representation of the diagram's geometry that Gemini could process effectively to make intelligent layout decisions. Additionally, ensuring the voice-to-command pipeline was fast enough for a real-time collaborative experience required significant optimization of our Lambda functions and data flow. Accomplishments that we're proud of 🏆 Implementing a true, end-to-end multimodal pipeline using Gemini 2.0 Flash to process voice, text, and spatial geometry simultaneously. Achieving genuine spatial awareness in an AI agent, allowing it to modify diagrams contextually rather than just adding elements. Building a resilient serverless backend on AWS Amplify Gen 2 that handles real-time data streaming and API calls seamlessly. Getting Gemini to reliably generate structured JSON commands that our React frontend could execute flawlessly. What we learned 🧠 We gained deep insights into the power of multimodal AI, especially how to leverage spatial data as a critical form of context for the model. We learned to design complex, event-driven systems on a modern serverless stack and, most importantly, how to build an AI tool that feels like an intuitive collaborator rather than just a static piece of software. What's next for Sematic 🚀 Vector DB Integration: We plan to use a vector database to provide the AI with context from an entire organization's past projects, enabling it to suggest relevant structures and components automatically. Platform Integrations: Native apps for platforms like Zoom and Google Meet to capture conversations where they happen. Enhanced Audio Capture: Support for capturing both system audio and microphone input for a more complete conversational context. <div