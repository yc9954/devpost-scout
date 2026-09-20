---
slug: "im-telligent"
url: "https://devpost.com/software/im-telligent"
title: "IM-TELLIGENT"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 528
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
---

# IM-TELLIGENT

> "IM-TELLIGENT is the AI study companion that helps you learn how to think, not just what to answer."

[Devpost](https://devpost.com/software/im-telligent) · hackathon [[DSH Hacks V1]]

## Facets

  <sub>weak: realtime_stream, simulation_digital_twin, vision_ocr, voice_speech</sub>
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]]
  <sub>weak: geospatial, structured_db, transcript_audio, web_dom</sub>

**stack** claude, css3, groq, html5, openai

## Body

homepage of the site Inspiration Every student knows the feeling — it’s 11 PM, the exam is tomorrow, and you're stuck on a problem. You search online, find the answer, copy it, and learn nothing. Or you might attend a school without a lab, equipment, or a chance to run a real chemistry experiment. We created IM-TELLIGENT because we believe every student deserves a top-notch tutor, no matter where they live, what school they go to, or what time it is. What We Built IM-TELLIGENT is a multi-tool AI-powered STEM education platform with 13 specialized tools: Tool What It Does Math Helper Guides you with Socratic hints, never just gives the answer Explain This Breaks down any STEM concept at your level Essay Feedback Reviews scientific reasoning, not just grammar Diagram Labeller Upload any diagram, and the AI labels every part Compound Reactor Simulates chemical reactions with real predictions Equation Balancer Shows step-by-step chemical equation balancing Graph Plotter Plots any function or describes a graph in simple terms Note Structurizer Transforms messy notes into clean structured study material Audio to Notes Records a lecture and provides structured notes instantly Problem Simplifier Rewrites confusing problems in plain language Quiz Generator Creates quizzes based on your own notes Syllabus Analyzer Provides a personalized day-by-day study plan Project Feedback Scores your project on feasibility, impact, and originality The platform also has a Learning DB, a continuous record of everything the student has worked on. The AI uses this information to tailor responses and pinpoint areas for improvement over time. How We Built It Frontend: Pure HTML, CSS, Bootstrap 4 — no frameworks, no build tools AI Providers: Supports Groq (Llama 3.3), Google Gemini, OpenAI GPT-4o, and Anthropic Claude — users supply their own key Vision: OpenRouter (Llama 3.2 Vision) for diagram image analysis Graphing: Plotly.js for real-time function plotting Audio: Web Speech API for live lecture transcription Storage: localStorage for maintaining learning history across sessions Markdown: marked.js for clean formatted AI output Every tool uses the same universal askAI() function, just with a different system prompt. The entire platform runs in a browser with no backend, no database, and no server costs. What We Learned How to design AI prompts that help guide rather than just answer — the toughest challenge was making the math tutor useful without being overly so How vision-language models process image inputs using base64 encoding How to keep conversation history during multi-turn interactions so the AI retains context The effectiveness of a universal API that supports four different AI providers with one function Challenges We Faced Diagram labeling accuracy — getting a vision model to provide precise coordinates proved unreliable, so we switched to numbered list explanations that are always accurate DB context issues — early versions sent the entire learning history to every tool, leading the simplifier to refer to chemistry when asked about philosophy. We fixed this by injecting context only where it’s truly useful. Markdown rendering — AI responses appeared as walls of asterisks without a parser; integrating marked.js and structured system prompts resolved this Multi-provider compatibility — each AI API has a different message format, especially for vision and conversation history <div