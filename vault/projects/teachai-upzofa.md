---
slug: "teachai-upzofa"
url: "https://devpost.com/software/teachai-upzofa"
title: "Nexora-AI"
hackathon: "Agent Development Kit Hackathon with Google Cloud"
organization: "Google"
winner: true
words: 905
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Nexora-AI

> Nexora – Next Gen Personalized Education. Learn through interactive lessons with visuals, quizzes, and smart AI support. Experience it now at nexora-ai.de.

[Devpost](https://devpost.com/software/teachai-upzofa) · hackathon [[Agent Development Kit Hackathon with Google Cloud]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[education]] [[finance_payments]]
**user** [[developer]] [[educator_student]]
**substrate** [[video_visual]]

**stack** chromadb, docker, fastapi, google-adk, google-cloud, javascript, mysql, python, react, vite

## How they structured the write-up

- 🎯 inspiration
- 🚀 what it does
- 🏗️ how we built it
- 🔥 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🔮 what's next for nexora

## Body

Turn any topic into a complete course with interactive visualizations. AI agents collaborate to create personalized learning paths. From single query to complete course: AI creates structured chapters with custom visuals and interactive learning experiences. Create courses tailored to you. From text to interactive simulations: AI creates engaging course content that lets students experience concepts, not just read them. Beyond static courses: AI generates interactive content + provides real-time tutoring. Ask questions, get instant expert responses. Get instant dynamic feedback on your answers to the Quizzes. And of course you can also take notes on what you have learned. Nexora-AI: Revolutionizing Education with Multi-Agent LLMs and Dynamic React Visualizations 🎯 Inspiration Traditional AI-generated educational content is static, text-heavy, and frankly boring. We've all seen LLMs produce walls of text that explain concepts without truly showing them. When we set out to build Nexora AI, we had a bold vision: create an AI-powered learning platform that doesn't just generate text-based courses, but produces rich, interactive educational experiences with dynamic visualizations, charts, and interactive components. The Google Cloud Multi-Agents Hackathon challenged us to rethink fundamental assumptions about AI output. Why should AI be limited to text when it could generate entire interactive experiences? 🚀 What it does Nexora AI transforms simple user queries like "I want to learn about the solar system" into comprehensive, interactive courses featuring: Dynamic 3D Visualizations - Watch planets orbit in real-time, explore Earth's layers, or see algorithm visualizations in action Interactive Charts & Graphs - Data comes alive with Plotly-powered scientific visualizations and Recharts components Adaptive Learning Path s - AI-generated course structures that adapt to your learning style React-Powered Interactivity - Every explanation includes interactive components you can manipulate Smart Assessment - Quizzes that also use React components for engaging, visual problem-solving Live Demo : nexora-ai.de 🏗️ How we built it Revolutionary Multi-Agent Architecture Nexora leverages the Google Cloud Agent Development Kit (ADK) to orchestrate multiple specialized agents: Course Planner Agent - Generates overall course structure and learning objectives Content Creator Agent - Produces chapter content with educational explanations Explainer Agent - Creates interactive React components with visualizations Quiz Generator Agent - Develops adaptive assessments using React components Interactive Chat Agent - Provides contextual support throughout learning Image Agent - Sources relevant visual content via external APIs Agent Structure The Breakthrough: React Code as LLM Output Instead of generating static text or markdown, we made a bold decision: Let the LLM output raw React code directly. Our agents generate React components using: Plotly for complex scientific and mathematical visualizations Recharts for data visualization and charts React-Flow for flowcharts and algorithm visualizations LaTeX rendering for mathematical equations Syntax highlighting for code examples Tech Stack Backend : Python 3.12 with FastAPI Google Cloud Agent Development Kit (ADK) Multiple Gemini models (2.5-Pro, 2.5-Flash, 2.5-Flash-Lite) MySQL + ChromaDB for data storage Docker containerization Frontend : React with Vite Mantine UI components Tailwind CSS Dynamic React component rendering Validation Pipeline : ESLint analysis for code quality Security validation to prevent code injection Multi-iteration feedback loops for code improvement 🔥 Challenges we ran into Code Generation Reliability - Getting LLMs to consistently generate valid, executable React code was initially problematic. We solved this with a sophisticated validation pipeline and iterative feedback loops. Agent Coordination - Managing state consistency across multiple agents while maintaining course coherence required careful orchestration through the ADK. Security Concerns - Executing AI-generated code posed security risks. We implemented comprehensive validation and sandboxing. Performance Optimization - Rendering complex visualizations while maintaining smooth user experience required significant optimization. Context Management - Ensuring agents maintained context about the overall course while focusing on their specific tasks. 🏆 Accomplishments that we're proud of Mastered React Code Generation - We believe to successfully have LLMs generate production-ready React components at scale Seamless Multi-Agent Orchestration - The ADK enabled us to create a complex system that feels simple to users Visual Learning Revolution - Transformed abstract concepts into tangible, interactive experiences Production-Ready Platform - Built a fully functional platform deployed at nexora-ai.de Google ADK Innovation - Pushed the boundaries of what's possible with the Agent Development Kit 📚 What we learned LLMs are more capable than expected - Modern language models can generate sophisticated, functional code when properly guided and validated Multi-agent coordination is powerful - The ADK's orchestration capabilities enabled complexity that would be impossible with single-agent approaches User experience is everything - Technical innovation means nothing without intuitive, engaging user interfaces Validation is critical - Robust testing and validation pipelines are essential when dealing with AI-generated code Visual learning works - Interactive visualizations dramatically improve comprehension compared to static text 🔮 What's next for Nexora Collaborative Learning - Multi-user courses and peer interaction features Advanced Analytics - Learning pattern analysis and personalized recommendations Mobile Applications - Native iOS and Android apps for learning on-the-go Enterprise Integration - B2B solutions for corporate training and education institutions Global Accessibility - Multi-language support and accessibility improvements Flash Cards - Utilise active recall for optimal memorisation 👥 Built with ❤️ by Team Nexora Markus Huber - Software Architect Luca Bozzetti - AI Engineer Jonas Hoerter - RAG Specialist Matthias Meierlohr - UI/UX Wizard Try Nexora AI today: nexora-ai.de Tags: #adkhackathon #GoogleCloud #AI #Education #React #LLM #MultiAgent The future of AI isn't just about generating better text — it's about generating better experiences. And with tools like the ADK making multi-agent coordination seamless, we're just scratching the surface of what's possible. <div