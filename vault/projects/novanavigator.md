---
slug: "novanavigator"
url: "https://devpost.com/software/novanavigator"
title: "NovaNavigator: Voice-Driven AI Agent"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 613
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# NovaNavigator: Voice-Driven AI Agent

> Voice-driven AI agent using Amazon Nova to control desktop and web applications.

[Devpost](https://devpost.com/software/novanavigator) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[human_in_the_loop]] [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[code_repository]] [[document_pdf]] [[sensor_telemetry]] [[structured_db]]

**stack** ai, amazon, amazon-nova-2-sonic, aws-bedrock, human-in-the-loop, python, security

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- built with
- what's next for novanavigator

## Body

NovaNavigator Terminal: Processing voice commands and executing web tasks in real-time. Code Overview: Integrating Amazon Nova with Boto3 for intelligent agentic reasoning Project Repository: Organized source code and documentation on GitHub Inspiration The inspiration for NovaNavigator comes from the gap between traditional AI chatbots and true autonomous agents. While most AI can provide information, they cannot "act" on the PC or web. I wanted to build a Virtual Assistant that doesn't just talk but executes tasks—like opening apps, searching the web, or playing music—using only voice commands. By leveraging Amazon Nova's advanced reasoning, I aimed to create a seamless, hands-free computing experience. What it does NovaNavigator is an intelligent agentic system that transforms spoken words into system actions. Voice-First Interface: Powered by Amazon Polly, the agent talks back to the user, creating a natural dialogue. Intelligent Reasoning: Uses Amazon Nova Lite to understand complex user intent (e.g., distinguishing between a general question and a command to open an app). Desktop & Web Automation: Can automatically open local applications (like Notepad), play specific videos on YouTube, or perform targeted Google searches. Real-time Monitoring: A dedicated dashboard built with CustomTkinter provides live logs of the AI's "thinking" process via Amazon Bedrock. How I built it The Brain: Amazon Nova Lite (via Amazon Bedrock) serves as the core reasoning engine. The Voice: Amazon Polly handles the Text-to-Speech (TTS) conversion for low-latency, high-quality audio responses. The Backend: Developed in Python, utilizing the boto3 SDK for AWS integration and SpeechRecognition for capturing user input. The UI: A modern, dark-themed GUI designed with CustomTkinter to show real-time interactions and system status. Challenges I ran into A major challenge was managing the latency between voice capture and AI response. Integrating multi-threading was essential to ensure the UI remains responsive while the Amazon Nova model processes the request. Another hurdle was refining the prompt engineering to ensure Nova correctly identifies when to trigger a system command versus when to just provide information. Accomplishments that I'm proud of I am proud of successfully creating a "closed-loop" system where a voice command is understood by Amazon Nova and translated into a real-world action (like opening a browser) in seconds. Achieving a stable connection with Amazon Bedrock and seeing the agent respond accurately to diverse commands was a huge milestone. What I learned Building this project taught me the true power of Agentic AI. I learned how to move beyond simple "input-output" patterns and design "intent-to-action" workflows. I also gained deep experience in optimizing AWS Bedrock calls and managing real-time audio streams in Python. Built With Amazon Nova Lite (Reasoning) Amazon Bedrock (Model Hosting) Amazon Polly (Voice Synthesis) Python (Core Language) CustomTkinter (UI Framework) Boto3 (AWS SDK) What's next for NovaNavigator While the current version of NovaNavigator successfully bridges voice commands with desktop actions, the journey has just begun. My future roadmap includes: Multi-Step Autonomous Planning: Moving beyond single commands to complex goals. For example, "Plan a trip to Paris" would allow Nova to research flights, find hotels, and create a summary document—all in one flow. Multimodal Capabilities: Integrating Amazon Nova's Multimodal features to allow the agent to "see" the screen. This would enable the AI to navigate websites that don't have search bars by visually identifying buttons and menus. Enhanced Security (HiLV): Implementing a more robust Human-in-the-Loop verification system with biometric or secondary voice confirmation for sensitive actions like file deletions or online payments. Cross-Platform Support: Expanding NovaNavigator from a Windows desktop tool to a mobile companion and a browser extension, creating a unified AI agent across all devices. Memory & Personalization: Adding a local database so Nova can remember user preferences and past interactions, making the assistant truly personalized over time. <div