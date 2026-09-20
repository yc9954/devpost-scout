---
slug: "personal-study-guide-and-test-generator"
url: "https://devpost.com/software/personal-study-guide-and-test-generator"
title: "Personal Study Guide and Test Generator"
hackathon: "AmpliCode Hackathon 2025"
organization: "AmpliCode"
winner: true
words: 381
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Personal Study Guide and Test Generator

> Smarter Study, Reliable Results — AI-powered tests grounded in real knowledge

[Devpost](https://devpost.com/software/personal-study-guide-and-test-generator) · hackathon [[AmpliCode Hackathon 2025]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** css, embedding, fastapi, flask, groq, huggingface, javascript, languages-html, llm, mongodb, postgresql, python, rag, react

## How they structured the write-up

- 💡 inspiration
- 🧠 what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🔮 what's next for personal study guide and test generator

## Body

Home Page 💡 Inspiration We were inspired by the growing challenge students face in filtering trustworthy study content and preparing for tests efficiently. Most AI-powered tools often hallucinate facts, which is risky for academic learning. We wanted to create a solution that not only generates questions but ensures they're rooted in verified, human-curated material. This led to the idea of combining Large Language Models (LLMs) with Retrieval-Augmented Generation (RAG) to build a reliable and intelligent study companion. 🧠 What it does The Personal Study Guide and Test Generator is a web-based platform that: Allows students to upload study material (PDFs, images, notes) Extracts and classifies key concepts and image-caption pairs Uses RAG and LLMs to generate context-aware, accurate test questions Displays interactive dashboards showing progress and weak areas Helps users self-evaluate with reliable, source-backed content 🛠️ How we built it Frontend: Built with React, HTML, and Tailwind CSS for responsive design Backend: Implemented using Python (FastAPI & Flask) to handle logic and API routes Document Processing: Parsed PDFs/images using OCR and structured extraction Database: Used MongoDB and PostgreSQL to manage content and user analytics LLM Integration: Connected HuggingFace models with a custom RAG pipeline to generate grounded questions 🚧 Challenges we ran into Handling various PDF/image formats and extracting clean, structured content Preventing hallucination in LLM-generated outputs — required careful tuning of the RAG pipeline Managing performance and latency when generating questions from large documents Designing a user interface that’s both informative and intuitive for students and educators 🏆 Accomplishments that we're proud of Successfully integrated a working RAG pipeline to eliminate hallucinated outputs Built a full-stack prototype capable of parsing real educational documents Delivered high-quality, relevant MCQs aligned with uploaded study content Created a foundation for personalized learning analytics through dashboards 📚 What we learned Practical implementation of Retrieval-Augmented Generation in educational tools Best practices in OCR and text/image parsing for academic content Structuring LLM prompts and embeddings to ensure context relevance Full-stack development from frontend UI to backend API and database operations 🔮 What's next for Personal Study Guide and Test Generator Add support for handwritten notes and textbook scans via advanced OCR Enable collaborative study groups and shared test sets Integrate with LMS platforms (e.g., Moodle, Google Classroom) Launch mobile support for on-the-go test generation and revision <div