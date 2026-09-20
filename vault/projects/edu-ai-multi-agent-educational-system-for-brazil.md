---
slug: "edu-ai-multi-agent-educational-system-for-brazil"
url: "https://devpost.com/software/edu-ai-multi-agent-educational-system-for-brazil"
title: "Edu.AI – Multi-Agent Educational System for Brazil"
hackathon: "Agent Development Kit Hackathon with Google Cloud"
organization: "Google"
winner: true
words: 703
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Edu.AI – Multi-Agent Educational System for Brazil

> Edu.AI democratizes Brazil's education with autonomous AI agents that evaluate essays, generate personalized study plans, and create interdisciplinary mock exams, all in one intelligent system.

[Devpost](https://devpost.com/software/edu-ai-multi-agent-educational-system-for-brazil) · hackathon [[Agent Development Kit Hackathon with Google Cloud]]

## Facets

**mechanism** [[multi_agent]] [[simulation_digital_twin]] [[vision_ocr]]
  <sub>weak: on_device_local, realtime_stream</sub>
**domain** [[education]]
**user** [[educator_student]]
  <sub>weak: researcher</sub>
**substrate** [[geospatial]] [[video_visual]]
  <sub>weak: structured_db, web_dom</sub>

**stack** adk, cloud-vision, fastapi, google-cloud, google-storage, nextjs, python, sql, tailwindcss, typescript

## Body

Landing Page Essay Evaluation Agents Essay Evaluation Results - 01 Essay Evaluation Results - 02 Simulator Exam Generator Educational Content Generator Flashcards Dashboard Inspiration In Brazil, ENEM (Exame Nacional do Ensino Médio) is the most important standardized test for students finishing high school. It’s taken by over 3.9 million students every year and serves as the main gateway to public universities , scholarships (via ProUni ), and student financing (via FIES ). For many low-income students, performing well on ENEM is not just about academic achievement. It’s a chance to access higher education and radically transform their lives. However, access to high-quality ENEM preparation remains highly unequal . Students from private schools often have tutors, simulated exams, and essay feedback, while millions in public schools lack structured preparation, especially in rural or underserved areas. I was inspired to bridge this gap using AI. Our goal was to democratize access to ENEM preparation , using intelligent multi-agent systems to replicate (and expand) the support traditionally offered by elite preparatory courses — but for everyone . With Edu.AI, I aim to level the playing field, offering personalized, high-quality support powered by AI agents that understand ENEM’s structure, correct essays, generate realistic simulations, and adapt to each student's learning needs. What it does Edu.AI is a multi-agent educational platform that: Corrects essays based on official ENEM scoring criteria, with detailed feedback. Generates simulated ENEM exams and interdisciplinary questions. Suggests personalized learning paths. Creates didactic content (e.g., summaries, flashcards). Enables students to rewrite essays with AI guidance. Tracks student progress through interactive dashboards. Helps the student prepare for the most exam of their lives. How I built it I used the Agent Development Kit (ADK) to design and orchestrate specialized AI agents. Each agent was responsible for a specific educational task and communicated with others via the orchestrator. Agents: EssayEvaluatorAgent (evaluates student essays based on the official ENEM rubric (five competencies) PromptBuilderAgent (generates ENEM-style essay prompts with thematic context, motivational texts, like those used in the real exam, and a question that simulates the actual proposal) SimulatedExamAgent (creates customized ENEM-style multiple choice questions across subjects) InterdisciplinaryAgent (generates cross-discipline questions, combining areas) ContentGeneratorAgent (creates didactic material based on the student's needs, such as summaries, flashcards, video suggestions) RephraserAgent (helps the student rewrite their essays or answers) ProgressTrackerAgent (consolidates all performance data) PersonalTutorAgent (analyzes the full history and builds personalized learning paths) Other technologies Frontend: Built with Next.js and TailwindCSS, hosted on Vercel. Storage: Essays and images uploaded by users are saved to a Google Cloud Storage bucket. OCR: Used Google Cloud Vision API to extract text from image-based essays. Database: Essay feedback and scores are persisted to allow users to revisit their history. Cloud: The whole stack runs locally for now, but is designed for scalable deployment on GCP. Challenges I ran into Session and state management: Understanding how ADK handles user sessions and orchestrator routing required deep dives into documentation and experimentation. Parsing structured output: I had to rework several output schemas to avoid additionalProperties errors with Gemini. File uploads and OCR integration: Handling base64-encoded images, temporary file saving, and public URL generation for OCR proved more complex than expected. CORS and Frontend Integration: Because ADK auto-generates routes, integrating with Next.js required custom handling for sessions and CORS preflight. Accomplishments that I'm proud of Successfully integrated 8 autonomous agents in a cooperative architecture. Built a full-stack app with a clean UI and real-time AI interactions. Structured outputs via ADK schemas to ensure consistency and user-friendly frontend rendering. Built a platform that has real potential to help millions of Brazilian students. What I learned How to orchestrate multiple agents with ADK and transfer context between them. The power of structured outputs and how to design schemas for LLM responses. How to integrate AI tools like Cloud Vision into an educational product. How to debug low-level issues in AI platforms and how ADK manages stateful sessions and artifacts. What's next for Edu.AI – Multi-Agent Educational System for Brazil Add voice-based essay feedback for accessibility. Deploy the full system on Google Cloud Run. Allow students to log in and access a history of their evaluations and study paths. Integrate gamification and social learning features. Thank you for this opportunity. <div