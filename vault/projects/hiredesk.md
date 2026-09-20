---
slug: "hiredesk"
url: "https://devpost.com/software/hiredesk"
title: "HireDesk"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 633
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/labor_employment"
  - "user/developer"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# HireDesk

> HireDesk is an ML-powered hiring platform that intelligently streamlines job postings, ranks candidates, and optimizes recruitment workflows with a secure, scalable system.

[Devpost](https://devpost.com/software/hiredesk) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[labor_employment]]
**user** [[developer]] [[government_staff]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** django-rest-framework, firebase-authentication, flask-api, gemini-2.5, hugging-face, postgresql, react, render, spacy, tailwind-css, tensorflow, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hiredesk

## Body

Home page with dynamic ui (using lucide react) Explains workflow and features Candidate modal giving brief summary about candidate Candidate side jobs page showing status of jobs applied Inspiration Hiring today is inefficient and breaks at scale. Recruiters receive 1,000+ applications per role and spend nearly 60–70% of their time screening resumes. This process is slow, inconsistent, and biased. At the same time, applicants have no visibility into their application status, leading to frustration and poor candidate experience. We were inspired to build HireDesk to solve this gap by combining automation, AI, and structured workflows to make hiring faster, fairer, and more transparent. What it does HireDesk is an AI-powered recruitment automation platform. Job Listings – Recruiters can post jobs with detailed descriptions and requirements for candidates to apply. Upload Resume – Candidates can upload resumes in PDF, DOC, or image format. Bulk Upload – Recruiters can upload multiple resumes at once using CSV files. Resume Analyzer – Analyzes resumes and gives the skills which candidates can improve. Chat Assistant – Built-in chat feature for queries and communication. Dashboard – Separate dashboards for Recruiters and Candidates to manage jobs, applications, and track progress. How we built it Tech Stack for my project: Frontend: React + Tailwind CSS for a fast, responsive UI Authentication: Firebase for secure, role-based access Backend: Django + Django REST Framework for APIs and business logic ML Engine: spaCy and PyTorch for resume parsing, skill extraction, and candidate scoring Database: PostgreSQL for secure data storage Deployment: Frontend - Vercel, Backend - Render, ML-Service - HuggingFace Challenges we ran into One of the biggest challenges was designing a fair and intelligent candidate scoring system. For example, if an engineer applies for a clerk position, the system should recognize that the engineer already possesses the required skills and should not be rejected simply because the profile appears “overqualified.” Building this kind of contextual understanding required more than simple keyword matching - we had to carefully design the skill-matching logic so that higher qualifications did not negatively affect relevance scoring. Another practical challenge was handling resumes in different formats such as images, PDFs and .docx files, each with different structures and layouts. Extracting consistent, structured data from unstructured documents required fine-tuning our NLP pipeline. We also faced integration challenges while connecting the ML engine with the backend APIs to ensure that scoring, parsing, and dashboard updates happened smoothly and in real time. Accomplishments that we're proud of We trained our resume parsing and scoring model on Google Colab and deployed it using Hugging Face and Render so that it works on production with scalability. We kept three separate repositories - one for the frontend, one for the backend, and one for the ML service, so each part of the system stays clean and independent. I also made sure no API keys or sensitive data were pushed to GitHub, and all secrets were handled through environment variables to keep the system secure. We successfully integrated the deployed ML service with the backend APIs, enabling real-time resume parsing, candidate scoring, and dashboard updates - making HireDesk a fully functional, cloud-deployed AI recruitment platform. What we learned We learned that building a scalable, production-ready system is equally as important as making a perfect solution. A solution only creates real impact when it can be deployed, integrated smoothly into a production environment, and sustained over time. What's next for HireDesk Next, we plan to integrate an in-platform interview system so recruiters can conduct interviews directly within HireDesk. We also aim to introduce AI-based monitoring using facial movement analysis to detect suspicious behavior, such as looking away frequently or reading from another screen, to reduce cheating during remote interviews. The goal is to make HireDesk not just a hiring management tool, but a complete end-to-end recruitment platform. <div