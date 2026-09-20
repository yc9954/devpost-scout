---
slug: "stembridge-nigeria"
url: "https://devpost.com/software/stembridge-nigeria"
title: "STEMBridge Nigeria"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 586
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "user/developer"
  - "user/educator_student"
---

# STEMBridge Nigeria

> Free AI-powered WAEC tutor for Nigerian students — personalized explanations, past questions, misconception detection & progress tracking across Maths, Physics, Chemistry and Biology.

[Devpost](https://devpost.com/software/stembridge-nigeria) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[agriculture_food]] [[developer_tools]] [[education]] [[health_clinical]]
**user** [[developer]] [[educator_student]]

**stack** faiss, fastapi, github, gpt-4o-mini, javascript, json, openai, orompt-engineering, python, rag, render, rest-api, streamlit, web-scraping

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments
- what we learned
- what's next

## Body

STEMBridge Nigeria Tagline: Bridging the Educational Gap with Accessible, AI-Powered WAEC Preparation. Inspiration Nigeria produces over 1.5 million WAEC candidates every year. Yet, only about 50% pass five or more subjects. The reason is not a lack of intelligence—it is a lack of access. Private tutors in Lagos charge between ₦5,000 and ₦20,000 per hour. For the average Nigerian family, that is simply out of reach. While free online resources exist, they often fail to align with the WAEC syllabus, neglect local context, and lack the ability to provide formative feedback when a student makes a mistake. I built STEMBridge Nigeria because every student in Borno, Kano, Delta, or Anambra deserves the same quality of STEM tutoring as a student in a top-tier private school. The only fair equalizer is AI . What it does STEMBridge Nigeria is an adaptive, AI-powered WAEC/NECO tutor for Nigerian SS1–SS3 students, covering Mathematics , Physics , Chemistry , and Biology . AI Chat Tutor: Explains concepts step-by-step using relatable Nigerian examples (e.g., Naira, NNPC, Dangote refinery, local geography, and agriculture). WAEC Quiz Generator: Auto-generates multiple-choice questions at official WAEC difficulty levels, providing instant, detailed feedback. Misconception Detector: When a student answers incorrectly, the AI identifies the specific conceptual gap rather than just marking the answer wrong. It diagnoses the error and corrects the student’s thinking process. Progress Dashboard: Tracks accuracy per subject and topic, generating personalized study tips to target weak areas. RAG Knowledge Base: Utilizes Retrieval-Augmented Generation over curated WAEC past questions (2016–2023). Mobile-First Design: A lightweight UI optimized for 3G connectivity, acknowledging that most students study on mobile devices. How we built it Frontend: Streamlit (lightweight and efficient for low-bandwidth environments). AI Model: OpenAI GPT-4o-mini (cost-effective and high-quality responses). RAG Pipeline: Keyword-based retrieval over curated WAEC past questions (Zero heavy ML dependencies; runs within 512MB RAM on Render's free tier). Data: Scraped and curated 60+ real WAEC past questions across four subjects (2016–2023). Deployment: Render.com (auto-deploy from GitHub). Nigerian Context Layer: Custom system prompts inject local examples, currency, geography, and encouraging Pidgin phrases into every interaction. Challenges we ran into Python 3.13 Compatibility: ChromaDB and sentence-transformers failed to install. Solution: Replaced the vector DB with a lightweight, pure-Python keyword retrieval system. Memory Limits: The 512MB limit on Render crashed when using heavy models. Solution: Removed transformer models entirely in favor of keyword scoring. API Quotas: Encountered early limitations with initial keys. Solution: Switched to OpenAI GPT-4o-mini to ensure stability. Development Environment: Navigated system-specific file creation issues systematically to ensure code integrity. Accomplishments Built a fully deployed AI tutor in under 3 weeks as a solo developer. Created a "Nigerian Context Layer" that delivers culturally resonant learning experiences. Developed a high-impact Misconception Detector that functions as a personal tutor. Achieved zero-cost access for students by leveraging free-tier infrastructure. What we learned Python version compatibility and library availability are critical constraints. Lightweight, optimized solutions often outperform heavy, complex ML pipelines in real-world deployment. The Nigerian educational market is significantly underserved by current specialized AI solutions. What's next Voice Mode: Enable students to speak questions and hear answers in Nigerian Pidgin or local languages. Offline Mode: Develop downloadable content packs for areas with limited internet access. JAMB Integration: Expand coverage to include UTME subjects and past questions. Teacher Dashboard: Provide tools for schools to track class-wide performance. Regional Expansion: Adapt the platform for Francophone West Africa, addressing similar educational gaps in countries like Côte d'Ivoire, Cameroon, and Senegal. Built solo in Nigeria. Driving educational equity, one student at a time. <div