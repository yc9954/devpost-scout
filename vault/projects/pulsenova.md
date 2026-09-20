---
slug: "pulsenova"
url: "https://devpost.com/software/pulsenova"
title: "PulseNova"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 802
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# PulseNova

> PulseNova is an AI medical assistant powered by Amazon Nova that helps users understand symptoms, scans, labs, prescriptions, and find the right care faster.

[Devpost](https://devpost.com/software/pulsenova) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**domain** [[developer_tools]] [[education]] [[health_clinical]]
**user** [[clinician]] [[developer]] [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** alexa-skills-kit, amazon-bedrock, amazon-nova, amazon-web-services, aws-cognito, css, fastapi, html, javascript, postgresql, python, rppg

## How they structured the write-up

- inspiration
- what it does
- how i built it
- where amazon nova helped
- challenges i ran into
- what i learned
- what’s next for pulsenova
- final thoughts

## Body

Inspiration As an international student in the United States from India, I have always had to be careful about my health because medical care and medications here can be extremely expensive. That experience made me realize how difficult it can be to make informed medical decisions quickly and confidently. When people feel sick, they are often forced to navigate symptoms, handwritten prescriptions, complex lab reports, scans, and provider searches across many different apps and websites. The experience is fragmented, stressful, and time-consuming. I wanted to create a platform that could bring all of this together in one place. A system that securely stores medical history, uses that context to provide more informed guidance, and makes healthcare support more accessible. I also wanted it to connect with everyday devices and workflows, such as medication reminders, so it could support users beyond a single interaction and become a practical part of their daily care journey. That’s why I built PulseNova , a multimodal AI medical assistant powered by Amazon Nova . What it does PulseNova is an intelligent healthcare companion. It helps users: Understand symptoms: AI-powered triage available in multiple languages Interpret and simplify: Translates handwritten prescriptions and dense lab reports into simple, accessible language Analyze medical scans: Extracts insights from complex imagery such as X-rays Navigate care: Locates nearby hospitals, urgent care centers, doctors, and pharmacies Centralize health data: Manages profile information, medical history, and interactions in one secure place Estimate vitals: Uses the smartphone camera to estimate pulse and provide an instant summary The application analyzes facial video feeds using remote photoplethysmography (rPPG). The estimated heart rate (HR), in beats per minute, is calculated using the dominant frequency $f_{HR}$ obtained from the Fast Fourier Transform (FFT) of the filtered blood volume pulse signal: $$ HR = 60 \times f_{HR} $$ where $$ f_{HR} = \arg\max_{f} \left| \mathcal{F}{s(t)} \right| $$ within the physiological frequency band of $[0.75, 4.0]$ Hz. How I built it PulseNova combines modern web development with the multimodal capabilities of Amazon Nova. Drawing on my background in backend and full-stack application development, I designed an architecture focused on low latency, reliability, and usability. Core architecture Frontend: An interactive web interface designed for a seamless flow between triage, vitals scanning, and care discovery Backend and APIs: Application logic built with Python and REST APIs to handle requests, manage user flows, and securely interact with AI models AI layer: Amazon Nova through Amazon Bedrock powers text understanding, multimodal analysis, and intelligent medical guidance Integrations: Location-based APIs for care search, secure databases for user profile and history management, and device-connected reminder workflows Where Amazon Nova helped Amazon Nova was the cornerstone of this project. It allowed me to build a single, cohesive assistant that can handle: plain text voice interactions handwritten prescriptions lab reports medical scans and imagery Nova powered multilingual symptom triage, document summarization, scan understanding, and natural user interaction. It helped PulseNova feel like a unified intelligence instead of a patchwork of disconnected tools. Challenges I ran into The biggest challenge was designing a product that felt both helpful and responsible. Healthcare-related applications require clarity, trust, and careful communication. Some of the main challenges included: Multimodal input handling: Routing text, images, and medical documents through the right model workflows while preserving context Medical translation: Converting dense clinical language into clear, easy-to-understand explanations without losing important meaning User experience: Building an interface that felt practical and trustworthy rather than like a generic chatbot demo Device connectivity: Using the Alexa Developer Console to create a skill, link it with the user account, sync medical history and medications, and enable reminder based medication support What I learned Building PulseNova was a strong learning experience in applied multimodal AI and user centered design. I learned: how to anchor technical features to real-world human problems how powerful Amazon Nova can be when integrated into structured application workflows how important UX and responsible AI guardrails are in healthcare technology how to combine multimodal AI, backend systems, and product design into one cohesive experience Most importantly, I learned that the strongest AI products are not just about impressive model outputs — they are about helping users make better decisions with confidence. What’s next for PulseNova PulseNova was built to be more than a hackathon prototype. Going forward, I plan to expand it with: deeper personalized health history and longitudinal insights expanded multilingual support for more global users automated medication and appointment reminder workflows a follow-up feature that checks in with users and tracks their progress over time Final thoughts PulseNova shows how Amazon Nova can power a meaningful, human centered healthcare experience. My goal was to build something that is not only technically impressive, but also practical, accessible, and genuinely useful. A platform that helps people better manage their health and make more informed decisions from anywhere. <div