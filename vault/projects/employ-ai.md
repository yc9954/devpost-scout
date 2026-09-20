---
slug: "employ-ai"
url: "https://devpost.com/software/employ-ai"
title: "Employ AI"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 514
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Employ AI

> Whether you're trying to get a change or find your first job, a daunting application lays before you. Employ AI helps you clear this challenge by making this process easier and more efficient.

[Devpost](https://devpost.com/software/employ-ai) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** css, dotenv, ffmpeg, firebase, flask, gmail-api, google, google-gmail-oauth, groq, html, javascript, numpy, pymupdf, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for employ ai

## Body

Inspiration As computer science students, we are all too familiar with the challenges of breaking into the job market. The modern application process is time-consuming, repetitive, and often demoralizing, especially when juggling coursework, internships, and personal responsibilities. We wanted to build something that would genuinely help students and job-seekers like us: a tool that removes friction from the process, boosts confidence, and actually provides value. That’s how Employ AI was born. What it does Employ AI streamlines two of the most daunting tasks in the job search process: Personalized Cold Email Generator Upload your resume, and we’ll extract your key experiences using AI. Then, with just a few inputs (company name, recruiter name, email), we generate a polished, personalized cold outreach email—ready to send via Gmail integration. Mock Interview Coach with Feedback Upload your resume and specify your target job. We generate 10 intelligent interview questions tailored to your resume and career goals. You can record your spoken responses, and we’ll analyze your delivery using acoustic features (energy, entropy, ZCR) and provide real-time feedback—helping you improve both your content and communication. How we built it Backend: Built using Flask, Firebase (Firestore, Auth, and Cloud Storage), and PyMuPDF for PDF processing. Authentication: Google OAuth 2.0 for Gmail integration and Firebase Auth for signup/login. Audio & AI Features: Audio processing with FFmpeg and feature extraction using signal processing techniques. Natural language understanding with LLaMA-3 through Groq API for both email generation and mock interview logic. Frontend: HTML templates rendered via Flask’s Jinja2 with custom UI for uploading, form inputs, and dynamic question flows. Challenges we ran into Audio File Processing in Flask: Supporting webm-to-wav conversion on the fly required careful integration with FFmpeg. Session Management: Keeping track of resume uploads, question progression, and user state across multiple endpoints was tricky in Flask. Gmail API Integration: Setting up OAuth scopes and redirect URIs while keeping user tokens secure was non-trivial. Groq/OpenAI Rate Limits: Ensuring fast and consistent generation from a third-party API required retry logic and error handling. Accomplishments that we're proud of Built a full-stack AI-driven product in a short time that feels useful and personal. Integrated multiple technologies (PDF parsing, audio analysis, generative AI, OAuth) in a cohesive, user-friendly flow. Successfully deployed a working end-to-end Gmail integration that sends real cold emails. Designed a feedback system that’s both data-driven and user-friendly for mock interviews. What we learned How to build robust, session-aware web applications with Flask. Real-world use of OAuth 2.0 with multiple scopes (profile, email, Gmail send). How to extract meaningful insights from raw audio signals using ZCR, entropy, and energy The value of iteration, especially in natural language prompts and generative outputs What's next for Employ AI Voice Tone Feedback: Incorporate sentiment and tone analysis into audio feedback Job-Specific Cold Emails: Add job scraping or integration with platforms like LinkedIn or Indeed to auto-tailor the cold email Question Difficulty Tuning: Let users choose beginner, intermediate, or expert mock questions Progress Tracking: Save user feedback over time to show improvement Mobile Optimization: Bring the full experience to mobile so users can practice on-the-go. <div