---
slug: "smarttriage-ai"
url: "https://devpost.com/software/smarttriage-ai"
title: "SmartTriage AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 369
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# SmartTriage AI

> SmartTriage AI helps remote clinics prioritize patients instantly, using AI to detect urgent cases, reduce waiting times and save lives.

[Devpost](https://devpost.com/software/smarttriage-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]] [[labor_employment]]
**user** [[patient_family]] [[social_worker]]
**substrate** [[structured_db]] [[web_dom]]

**stack** ai, api, css, gemini, html, javascript, mysql, php

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for smarttriage ai

## Body

Inspiration In many remote and under-resourced clinics, patients often wait hours before seeing a healthcare worker, and critical cases can be missed due to manual triage. I wanted to create a solution that brings intelligent, AI-powered triage to clinics, helping healthcare staff prioritize patients efficiently and save lives. What it does SmartTriage AI analyzes patient symptoms, vital signs and medical history using AI (Gemini AI) to: Assign a triage level: Red (Critical), Yellow (Urgent), Green (Routine) Generate a severity score and clear AI notes for healthcare staff Provide a real-time dashboard that automatically sorts patients by urgency Suggest preliminary tests where needed It empowers clinics to reduce waiting times, improve decision-making and focus on patients who need help the most. How I built it Frontend: HTML, CSS, JavaScript: for patient intake forms and dynamic dashboards Backend: PHP: handles requests, communicates with Gemini AI, stores outputs Database: MySQL: stores patient inputs and AI results for reporting and analytics AI: Gemini AI: interprets symptoms, calculates severity, assigns triage levels and generates explainable notes Integration: Full-stack system where AI output is displayed in real-time for healthcare staff Challenges I ran into Designing an AI prompt that produces clear, structured JSON output for triage Ensuring the system is user-friendly for clinics with low technical resources Handling missing or partial patient data in a way that does not compromise triage accuracy Integrating real-time dashboard updates with minimal latency Accomplishments that I'm proud of Built a fully functional AI-assisted triage prototype Created a color-coded, real-time dashboard that clearly shows patient priority Successfully integrated Gemini AI for symptom analysis and severity scoring Developed a system that is scalable, ethical and can save lives in remote clinics What I learned How to design an AI prompt for real-world healthcare use Full-stack integration of frontend, backend, database and AI Best practices for ethical AI in healthcare, ensuring AI supports, not replaces, medical staff The importance of user-friendly dashboards for critical, time-sensitive workflows What's next for SmartTriage AI Add SMS/email notifications for critical patients Implement offline mode for clinics with unstable internet Expand to multi-clinic support with centralized dashboards Develop analytics for public health trends using collected triage data Optimize AI models for even more accurate triage predictions <div