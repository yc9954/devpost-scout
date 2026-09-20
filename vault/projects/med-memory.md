---
slug: "med-memory"
url: "https://devpost.com/software/med-memory"
title: "Med-Memory"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 389
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/medical_record"
  - "substrate/structured_db"
---

# Med-Memory

> Med-Memory turns overwhelming medical data into actionable insights with easy-to-read visuals and AI-powered assistance. Helping doctors make smarter decisions that save lives.

[Devpost](https://devpost.com/software/med-memory) · hackathon [[ShellHacks 2024]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[medical_record]] [[structured_db]]

**stack** express.js, firebase, next, node.js, ollama, react, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for med-memory

## Body

Inspiration Introducing Med-Memory: your fast-track solution for patient data. Instead of digging through endless reports, Med-Memory delivers key insights in real time, transforming complex lab results and treatment updates into clear, actionable visuals. With just a few clicks, you get instant, AI-driven answers to your questions, allowing you to focus on what matters most—providing excellent patient care, not paperwork. Save time, make smarter decisions, and ensure better outcomes with Med-Memory, the smarter way to manage patient information. What it does Med-Memory transforms overwhelming medical reports into easy-to-read, real-time dashboards. Med-Memory leverages AI to analyze individual patient data, providing doctors with instant, AI-powered insights. The system is trained on each patient's data, enabling it to answer any questions related to the patient's history, treatment, and conditions. This ensures that doctors receive precise, personalized responses that support informed decision-making in real-time.. The tool simplifies decision-making, enabling healthcare professionals to focus on critical care, especially in time-sensitive situations. How we built it We built Med-Memory with a Node.js (Express.js) backend and a Firebase database for data storage. On the front end, we used Next.js with React for seamless user interaction. The Qwen 2.5 LLM model was fine-tuned and deployed via Ollama and tested via Streamlit for interactive data analysis. Challenges we ran into Training the Qwen 2.5 LLM to understand specific patient histories and deploying it locally with Ollama posed significant challenges, especially in optimizing the model for fast, accurate responses. also maintaining more than 4 servers on the local host and maintaining communication between these servers. Accomplishments that we're proud of Successfully integrating the AI model into the real-time dashboard, allowing doctors to ask questions and receive instant, actionable insights. We’re also proud of optimizing the tool for efficiency in handling complex medical data, making it usable in fast-paced medical environments. What we learned We gained experience working with Next.js, Firebase, and LLMs. We also learned the nuances of fine-tuning AI models to handle specific datasets like medical records, which is critical for ensuring accuracy and relevance in healthcare applications. What's next for Med-Memory We plan to deploy the fine-tuned model at scale on the cloud, making it accessible to doctors and patients alike. We’re also working on integrating an audio analysis ML model to extract key insights from doctor-patient conversations, further enhancing the tool’s utility in real-time clinical settings. <div