---
slug: "math-sat-browser-extension-tutor"
url: "https://devpost.com/software/math-sat-browser-extension-tutor"
title: "Math SAT Browser Extension Tutor"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 549
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
---

# Math SAT Browser Extension Tutor

> Democratizing SAT excellence through local models

[Devpost](https://devpost.com/software/math-sat-browser-extension-tutor) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[vision_ocr]]
  <sub>weak: deterministic_policy, realtime_stream</sub>
**domain** [[education]] [[labor_employment]]
  <sub>weak: finance_payments</sub>
**user** [[educator_student]]
  <sub>weak: video_visual, web_dom</sub>

**stack** html, javascript

## Body

Inspiration The inspiration for this project comes from the frustration of studying for the SAT in isolation with the lack of help, and the desire to bridge the gap between encountering a difficult problem and understanding the "why" behind its solution. I built this as a lightweight, in-browser assistant that functions across any SAT site, ensuring students have immediate, AI-driven guidance wherever they practice. By running all models locally, the extension provides students with the freedom to scan an infinite number of problems without facing the common hurdles of subscription costs or API rate limits. What it does The Math SAT Browser Extension Tutor is an AI-powered study companion that operates directly within the browser. It allows students to scan homework or practice problems and provides step-by-step AI-guided hints. Key features include deterministic LaTeX repair for clear mathematical output, an automated pipeline for solving and validating linear equations, and a personalized tracking system that monitors user problems attempted across different SAT math categories and then provides links for further help after the study session. How we built it We architected the extension using a multi-stage pipeline: Vision Extraction: Utilized qwen2.5vl:7b via Ollama for stage-one image-to-text extraction of math problems. Math Processing: Developed a robust LaTeX repair pipeline in TypeScript to fix model-generated JSON escape corruption, delimiter gaps, and multiline equation fragmentation. Tutor Engine: Implemented a stateful backend (background service worker) that tracks student sessions, applies "plant health" gamification mechanics to encourage focus, and manages chat interactions using qwen2.5:7b. Frontend Integration: Built a side-panel interface that communicates with the background worker to provide real-time hints and display formatted step-by-step solutions Challenges we ran into LaTeX Corruption: Local models frequently produced "glued" prose or broken LaTeX syntax when outputting math symbols, which required creating regex-based repair modules to normalize text and equation formatting. JSON Reliability: Model responses were often truncated or invalid. A robust JSON repair utility was made that tracks parser state (delimiters and string escapes) to safely close and parse partial responses, ensuring the tutor doesn't crash on incomplete outputs. Mathematical Context: Distinguishing between prose and complex mathematical equations in a single stream of text proved difficult but was solved with "Math Region" protection patterns to isolate and correctly format expressions while keeping instructional text human-readable. Accomplishments that we're proud of I successfully had a pipeline that transformed messy error-prone model output into clean, standard-compliant LaTeX for SAT-level math problems. User Engagement: The integration of session-based tracking and the "plant health" focus mechanism provided a gamified incentive for students to stay on task. Performance: By utilizing local Ollama models with a multi-stage extraction and cleanup process, we achieved a high-speed tutoring experience that functions locally without heavy reliance on external API latency What we learned Building this extension taught me that AI is effective for educational tools when paired with rigorous post processing. I had to handle the "noise" of local model outputs and the importance of structural integrity when building conversational interfaces for technical subjects like mathematics. What's next for Math SAT Browser Extension Tutor Our next steps include are to have the tutor suggest problems based on the student's historical error patterns. We also plan to expand the visual feedback system with interactive graph animations for geometry and function-based problems to further help with conceptual understanding <div