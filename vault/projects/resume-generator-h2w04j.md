---
slug: "resume-generator-h2w04j"
url: "https://devpost.com/software/resume-generator-h2w04j"
title: "Resume Generator"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 254
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/labor_employment"
  - "substrate/document_pdf"
---

# Resume Generator

> Creating a resume is like filling a form now!

[Devpost](https://devpost.com/software/resume-generator-h2w04j) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

**domain** [[labor_employment]]
**substrate** [[document_pdf]]

**stack** axios, document, express.js, foxit, generation, handlebars.js, kendo, kilo, kilocode, node.js, pdf, progress, react, services

## Body

Inspiration Job hunting is time-consuming. Tailoring resumes for every job posting takes hours. We wanted to automate that paste a job description, get a tailored resume instantly. What it does ResumeForge AI generates personalized, job-tailored resumes in one click. Users enter their details, paste a job description, and the app uses You.com API to enrich the resume with live job context, Foxit Document Generation API to create a professional DOCX, and Foxit PDF Services API to export a downloadable PDF — all wrapped in a Progress Kendo UI interface built with Kilo Code. How we built it React + Vite frontend with Kendo UI components, a Node.js/Express proxy server for secure API calls, You.com for AI job enrichment, Foxit for document generation and PDF export, and Kilo Code as our AI coding assistant throughout the entire build. Challenges we ran into CORS restrictions required us to build a backend proxy server. Foxit's OAuth token authentication flow and managing multiple API credentials across two services added unexpected complexity. Accomplishments that we're proud of We built a fully working end-to-end product — not just a prototype — that generates real, professional PDFs tailored to real job descriptions using live web data. What we learned How to build secure full-stack architecture with server-side API proxying, Foxit's OAuth flow, and how AI-assisted coding with Kilo Code can take you from idea to working product incredibly fast. What's next for ResumeForge AI Cover letter generation, LinkedIn profile import, ATS compatibility scoring, multiple resume templates, and full cloud deployment. <div