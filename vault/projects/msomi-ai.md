---
slug: "msomi-ai"
url: "https://devpost.com/software/msomi-ai"
title: "Msomi Ai"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1107
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Msomi Ai

> Every child deserves a lesson built just for them. Msomi generates fully personalised, multimodal lessons and stories streaming in real time, tailored to every learner.

[Devpost](https://devpost.com/software/msomi-ai) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[education]] [[finance_payments]] [[labor_employment]]
**user** [[educator_student]] [[general_public]]
**substrate** [[financial_record]] [[video_visual]]

**stack** python, typescript

## How they structured the write-up

- the inspiration
- frontend
- backend
- artificial intelligence stack

## Body

Msomi: Reimagining STEM Education Through Multimodal AI The Inspiration Education has evolved far more slowly than technology. Today's students learn in a world dominated by interactive applications, personalized digital experiences, and artificial intelligence. Yet most educational systems still rely on static textbooks, one-way lessons, and generic learning materials that fail to adapt to individual learners. When trying to understand a STEM concept, students often jump between textbooks, YouTube videos, diagrams, online articles, and practice questions. This fragmented learning journey creates cognitive overload and makes understanding difficult. We asked ourselves: What if learning could adapt to every student and present knowledge through stories, visuals, audio, video, and interaction—all generated in real time? That question became Msomi . The Problem Traditional educational platforms face several major challenges: Learning is often passive rather than interactive. Educational content is rarely personalized. Students learn differently, yet most systems teach everyone the same way. STEM concepts can be difficult to visualize and understand. Learners must constantly switch between multiple resources to grasp a single topic. Teachers have limited tools for providing individualized support at scale. As STEM fields become increasingly important, there is a growing need for educational tools that can make learning more engaging, accessible, and adaptive. Our Solution Msomi is a production-ready multimodal AI learning platform that transforms STEM education into an immersive and personalized experience. Instead of presenting static lessons, Msomi generates dynamic educational experiences that combine: Interactive AI storybooks Adaptive educational explainers AI-generated illustrations Narrated audio lessons Educational video generation Real-time quizzes and assessments Personalized learning pathways Every learning experience adapts to the student's progress and learning style. If a learner struggles with a concept, Msomi automatically generates alternative explanations, visual aids, examples, and reinforcement exercises until understanding improves. Learning becomes a journey instead of a task. How It Works Imagine a student learning Newton's Laws of Motion. Instead of reading a static textbook chapter, they enter an AI-generated story where they must design and launch a spacecraft. As the story unfolds: Gemini generates contextual explanations. Imagen creates illustrations of the spacecraft and physics concepts. Google TTS narrates the lesson. Veo generates educational videos. Interactive quizzes reinforce understanding. Student choices influence the direction of the story. The result is a fully immersive learning experience delivered in real time. Technical Architecture Frontend Built using modern web technologies: Next.js 14 (App Router) TailwindCSS Framer Motion React Spring React Three Fiber Zustand The frontend streams educational content live through a custom Server-Sent Events implementation, allowing lessons to appear progressively instead of waiting for complete generation. Backend The backend is powered by FastAPI and organized into modular services: Authentication Story Sessions Lesson Generation Analytics Progress Tracking Firebase Authentication secures all user access while Firebase Admin verifies every request before protected resources are accessed. Heavy AI workloads are processed asynchronously using Celery and Redis. This ensures that image generation, video creation, and audio synthesis never block the learning experience. Artificial Intelligence Stack Msomi leverages Google's latest AI ecosystem: Vertex AI Gemini 2.5 Pro Used for: Story generation Educational explanations Adaptive tutoring Quiz creation Context management Imagen 3 Used for: Educational illustrations Story scene generation Visual concept explanations Google Text-to-Speech Used for: Audio narration Accessibility support Interactive lessons Veo Used for: Educational video generation Visual demonstrations STEM concept visualization Infrastructure Msomi runs entirely on Google Cloud. Cloud Run Frontend Service Backend API Celery Worker Data Layer Firebase Authentication Firestore PostgreSQL (Cloud SQL) Redis (Cloud Memorystore) Storage & Security Google Cloud Storage Artifact Registry Secret Manager Networking Dedicated VPC Connector Private Redis Connectivity This architecture enables fully serverless deployment while maintaining scalability and reliability. Challenges We Faced Building a production-ready AI platform came with significant challenges. Deployment Issues Artifact Registry authentication initially failed because Docker Desktop could not locate docker-credential-gcloud . We ultimately authenticated using direct access tokens and Docker login workflows. TypeScript Production Builds The application worked in development but failed during Docker production builds due to strict typing requirements involving Zustand and Next.js Suspense boundaries. Celery on Cloud Run Cloud Run requires every container to expose an HTTP endpoint. Because Celery is a queue consumer rather than a web service, we built a custom Python entrypoint that launches a lightweight health server before starting Celery. Networking Creating the VPC connector initially conflicted with existing subnet ranges, causing deployment failures. We rebuilt the networking layer with new subnet allocations. Cost One of our largest challenges remains infrastructure cost. Video generation using Veo consumes significant AI credits, and maintaining a fully cloud-native AI platform as students is expensive. Despite optimization efforts, cost remains one of the biggest barriers to scaling. Accomplishments We're Proud Of Real-Time Multimodal Learning We successfully built a system where: Text Images Audio Video Quizzes are streamed together in real time. Students begin receiving educational content in under a second. Fully Serverless Architecture The entire platform runs on managed Google Cloud infrastructure without maintaining traditional servers. End-to-End AI Integration We connected: Vertex AI Imagen Veo Cloud Storage Firebase PostgreSQL Redis into a unified educational platform. Branching AI Narratives Student choices influence story progression while Gemini maintains narrative consistency across multiple interactions. Impact Msomi has the potential to fundamentally transform how young people learn STEM. Modern students are digital natives. They interact daily with highly personalized applications and immersive digital experiences. Education should meet them where they are. By combining storytelling, visual learning, audio narration, video generation, and adaptive AI tutoring, Msomi creates educational experiences that are engaging, accessible, and personalized. The platform can support: Students Teachers Schools Homeschooling environments Underserved communities Because it is cloud-based and scalable, Msomi has the potential to deliver high-quality STEM education to learners anywhere in the world. What We Learned Building Msomi taught us valuable lessons about: Cloud architecture AI infrastructure Distributed systems Real-time streaming Educational technology Product scalability We also learned that building impactful educational technology requires balancing innovation with accessibility, performance, and cost. What's Next Our roadmap includes: Custom Learning Paths Allowing teachers to create curriculum-aligned educational journeys. Voice Interactions Students will be able to speak naturally with Msomi and receive conversational guidance. Multilingual Support Making STEM education accessible across multiple languages and regions. Teacher Analytics Dashboard Providing educators with insights into: Student progress Learning bottlenecks Concept mastery Classroom performance trends AI Learning Companion Our long-term vision is to build an intelligent educational companion that grows with students throughout their learning journey. Closing Statement Msomi is more than an educational platform. It is a vision for the future of learning. A future where education is adaptive. A future where every student receives personalized support. A future where AI helps make STEM education engaging, accessible, and effective for learners everywhere. Learn through stories. Understand through AI. <div