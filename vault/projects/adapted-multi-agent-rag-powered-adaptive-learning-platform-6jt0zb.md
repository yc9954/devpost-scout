---
slug: "adapted-multi-agent-rag-powered-adaptive-learning-platform-6jt0zb"
url: "https://devpost.com/software/adapted-multi-agent-rag-powered-adaptive-learning-platform-6jt0zb"
title: "AdaptEd: Multi-Agent RAG Powered Adaptive Learning Platform"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 998
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# AdaptEd: Multi-Agent RAG Powered Adaptive Learning Platform

> An AI-powered platform that generates personalized learning roadmaps, delivers curated lessons, conducts voice-based viva exams, and provides hands-on coding with real-time AI guidance.

[Devpost](https://devpost.com/software/adapted-multi-agent-rag-powered-adaptive-learning-platform-6jt0zb) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[cross_origin_web]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** amazon-ec2, aws-polly, aws-transcribe, css, fastapi, firebase, git, github, google-gemini-api, html, javascript, model-context-protocol-(mcp), monaco-editor, multi-agent-systems

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for adapted: multi-agent rag powered adaptive learning platform

## Body

DASHBOARD CITATIONS DYSLEXIA-MODE MCP-IDE NOTES VIVA-VOICE Inspiration Traditional learning platforms follow a one-size-fits-all approach, where every learner is given the same content, pace, and evaluation style. This often leads to inefficiency, lack of engagement, and shallow understanding. We were inspired to build AdaptEd after observing how students struggle with: Irrelevant learning paths Passive content consumption Lack of real understanding checks No hands-on or guided practice But beyond this, we identified a deeper and often overlooked issue — accessibility in education . According to research, over 700 million people worldwide are affected by dyslexia , yet most technical learning platforms are not designed with them in mind. Dense text, poor spacing, and complex layouts make it even harder for such learners to engage with content. This inspired us to not only build a smarter learning system, but also a more inclusive one . We wanted to create a system that behaves like a personal AI mentor — one that understands your goals, adapts to your knowledge, ensures real learning, and remains accessible to everyone. What it does AdaptEd is an AI-powered adaptive learning platform that transforms how individuals learn by creating a fully personalized, interactive, and continuously evolving learning experience. 🎯 Personalized Roadmaps: Generates structured learning paths based on a user’s career goals, existing skills, and weekly time commitment. Each roadmap includes modules, prerequisites, and realistic timelines. 📚 AI-Synthesized Learning Content (RAG): Instead of static notes, AdaptEd retrieves high-quality content from multiple sources like YouTube and official documentation, then uses Retrieval-Augmented Generation (RAG) to synthesize clear, structured lessons with references. 🎤 AI-Powered Viva (Oral Assessment): Moves beyond MCQs by conducting voice-based viva exams , where the system asks conceptual questions, listens to spoken answers, and evaluates understanding in real time. 💻 Hands-on Coding with MCP-IDE: Includes an in-browser coding environment where users can practice programming. The AI Shadow Tutor provides contextual guidance based on code, errors, and active files. 🤖 Multi-Agent AI System: Different AI agents collaborate to handle planning, teaching, evaluation, and assistance, making the system modular, scalable, and intelligent. 🧠 Gamified Progress Tracking: Tracks user engagement through streaks, experience points (XP), and achievements to encourage consistency and motivation. ♿ Cross-Platform Accessibility with Dyslexia Mode: AdaptEd includes a Dyslexia Mode implemented as a Chrome Extension , making it usable not just within the platform but across any website. It applies OpenDyslexic fonts, improved spacing, and contrast to enhance readability for users with dyslexia. Overall, AdaptEd creates a closed learning loop where users don’t just consume content—they actively learn, speak, practice, and prove their understanding . How we built it AdaptEd is built using a combination of modern full-stack technologies and advanced AI systems to deliver a seamless and intelligent learning experience. Frontend: Built with React (Vite) to ensure a fast, responsive, and intuitive user interface. Backend: FastAPI powers the backend, handling API requests, user flow, and orchestration between different AI components. Database & Authentication: Supabase and Firebase are used for storing user data, authentication, and real-time updates. AI & Intelligence Layer: Gemini API is used for roadmap generation, reasoning, and evaluation RAG Pipeline retrieves and synthesizes relevant learning content dynamically Multi-Agent Architecture: Planner Agent: Designs personalized learning roadmaps Content Agent: Generates structured lessons using RAG Evaluator Agent: Conducts viva and assesses conceptual understanding Tutor Agent: Provides contextual hints inside the coding environment Voice Interaction System: AWS Transcribe converts speech to text AWS Polly converts text to natural-sounding speech Development Environment (IDE): Monaco Editor is integrated with a Model Context Protocol (MCP) system, allowing the AI to understand the coding environment and provide relevant assistance. External Integrations: YouTube Data API is used to fetch high-quality educational content. Accessibility Extension: A Chrome Extension was developed to enable Dyslexia Mode across platforms, ensuring accessibility is not limited to AdaptEd but extends to the broader web. Deployment: The application is deployed on Amazon EC2 , ensuring scalability and reliability. All components are interconnected to form a continuous workflow: Plan → Learn → Evaluate → Practice → Improve Challenges we ran into ⚙️ Multi-Agent Coordination: Designing agents that collaborate effectively without overlapping responsibilities or causing inconsistent outputs. 🧠 RAG Optimization: Ensuring that retrieved content is relevant, high-quality, and properly synthesized into structured lessons. 🎤 Voice-Based Evaluation: Handling speech recognition accuracy, varied accents, and meaningful evaluation of spoken answers. 💻 Context-Aware IDE Assistance: Building a system that understands the coding environment in real time and provides useful hints without directly giving solutions. 🔄 State Management & Progress Tracking: Maintaining user progress across modules, viva results, and coding tasks in a consistent manner. ⚡ Performance & Latency: Managing multiple AI services (LLMs, speech APIs, RAG) while ensuring a smooth and responsive user experience. Accomplishments that we're proud of 🚀 Successfully built a complete adaptive learning ecosystem from planning to evaluation 🤖 Designed and implemented a functional multi-agent AI architecture 🧠 Integrated RAG for contextual, explainable, and dynamic content generation 🎤 Developed a real-time AI-powered viva system , replacing traditional MCQs 💻 Created a browser-based coding IDE with contextual AI guidance ♿ Delivered accessibility-first features like Dyslexia Mode 🔗 Seamlessly integrated multiple complex systems into a unified platform What we learned Practical implementation of multi-agent AI systems and their coordination Designing and optimizing RAG pipelines for real-world applications Handling real-time AI interactions with performance constraints Building scalable full-stack applications with AI integration Importance of accessibility and inclusivity in educational tools Challenges in evaluating deep conceptual understanding using AI What's next for AdaptEd: Multi-Agent RAG Powered Adaptive Learning Platform 📱 Developing a mobile application for improved accessibility 📊 Adding advanced analytics to track learning patterns and performance insights 🌐 Expanding to support multiple domains beyond technical education 🤝 Introducing collaborative and peer-to-peer learning features 🧠 Enhancing AI agents with long-term memory and deeper personalization 🎓 Integrating certifications, projects, and real-world assessments 🌍 Supporting regional languages to make learning more inclusive globally AdaptEd aims to evolve into a universal AI learning companion , capable of guiding any learner from beginner to expert through a fully personalized journey. <div