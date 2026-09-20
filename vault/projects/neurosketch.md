---
slug: "neurosketch"
url: "https://devpost.com/software/neurosketch"
title: "NeuroSketch"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 517
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/video_visual"
---

# NeuroSketch

> NeuroSketch: An AI-powered screening tool that helps paramedical workers detect early signs of Parkinson’s through simple motor, voice, and movement tests anywhere and anytime.

[Devpost](https://devpost.com/software/neurosketch) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[elder_child_care]] [[health_clinical]] [[labor_employment]]
**user** [[clinician]] [[patient_family]]
**substrate** [[video_visual]]

**stack** computer-vision-models, gemini, numpy, opencv, pandas, python, scikit-learn, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for neurosketch

## Body

finger tapping test of Healthy patient finger tapping test of parkinson patient Inspiration The inspiration for NeuroSketch comes from a very personal place. My grandfather showed early signs of Parkinson’s with slight tremors and stiffness, but they were repeatedly dismissed as normal aging. By the time he received a proper diagnosis, the disease had already progressed, limiting the effectiveness of treatment and affecting his independence. This experience made us realise that the real problem is not the absence of symptoms, but the absence of early, accessible screening, especially in regions with limited neurologists. NeuroSketch was born from the desire to ensure that families like mine don’t have to wait too long for answers and that paramedical workers can play a stronger role in identifying early warning signs. What it does NeuroSketch is an AI-powered early screening tool for Parkinson’s disease. It uses three simple, non-invasive diagnostic tests: Spiral drawing analysis Voice assessment Motor movement tracking The system generates an overall risk indication that helps paramedical staff decide when a patient should be referred to a neurologist for further evaluation. How we built it We built NeuroSketch using Python as the core programming language and Streamlit for the user interface. Each diagnostic test was developed as an independent pipeline: Spiral Test: Image processing and feature extraction techniques are used to detect tremor-related irregularities in drawn spirals. Voice Test: Audio features such as pitch variation and frequency instability are extracted to identify speech anomalies linked to Parkinson’s. Motor Test: Computer vision methods analyze movement speed, rhythm, and consistency using camera input. The outputs from all three models are combined to produce a single early-detection signal. We also explored cloud-based tools and APIs, including Gemini, to support scalability and chatbot-based guidance for users and paramedical staff. Challenges we ran into Our biggest challenges were access to high-quality medical data and achieving reliable model accuracy. Parkinson’s datasets are limited, and collecting diverse real-world samples requires significant time and coordination. We also faced difficulties in fine-tuning models to generalize well across different users. Balancing technical development with designing a simple, elderly-friendly interface required continuous iteration and testing. Accomplishments that we're proud of Designing a complete diagnostic workflow that combines three different tests Building a functional prototype that demonstrates real-world usability Creating a solution focused on paramedical assistance rather than only research use Developing a scalable roadmap despite limited resources and time What we learned We learned that data quality matters more than model complexity. This project gave us hands-on experience in: Multimodal AI Computer vision Audio signal processing Most importantly, we learned that healthcare technology must be built around real users, real constraints, and real environments, especially when working with elderly populations and frontline health workers. What's next for NeuroSketch Next, we plan to: Train our models on larger and more diverse datasets to improve accuracy Add additional diagnostic tests, such as gait analysis and facial expression tracking Improve validation and robustness for real-world deployment With mentorship and partnerships, we aim to scale NeuroSketch into a deployable national screening tool that strengthens early Parkinson’s detection and supports paramedical workers across India. <div