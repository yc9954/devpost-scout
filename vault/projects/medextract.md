---
slug: "medextract"
url: "https://devpost.com/software/medextract"
title: "MedExtract [Biotech theme]"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 232
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/clinician"
  - "substrate/medical_record"
---

# MedExtract [Biotech theme]

> "Turning messy clinical notes into structured medical intelligence, instantly"

[Devpost](https://devpost.com/software/medextract) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]] [[labor_employment]] [[mental_health]]
**user** [[clinician]]
**substrate** [[medical_record]]

**stack** fastapi, langextract, react, vite

## How they structured the write-up

- about medextract

## Body

The output The uploaded file The upload section About MedExtract Inspiration Medical documentation is notoriously unstructured, leading to clinician burnout. We built MedExtract to turn complex physical and digital narratives into structured medical intelligence instantly, improving accuracy and saving lives. What it does MedExtract uses Gemini 2.0 Flash to parse clinical text and categorize critical medical entities—including Subjective notes, Objective vitals, Assessments, and Plans—presenting them in a high-fidelity dashboard. How we built it Intelligence: Orchestrated Gemini 2.0 with few-shot prompting to handle medical shorthand. Infrastructure: Built a high-performance FastAPI backend with asynchronous workers. Logic: We used LANGEXTRACT to extract unstructured data into structured data Real-time: Integrated Socket.io for instant streaming of extraction status. Frontend: Designed a premium "glassmorph" UI using React and Tailwind CSS. Challenges we ran into Ensuring zero-hallucination in clinical entity extraction was our biggest hurdle. We optimized extraction accuracy by iterating on prompt schemas to handle non-standard medical abbreviations Accomplishments that we're proud of We achieved near-instant extraction from "noisy" medical notes while maintaining a UI that feels like a premium, next-gen clinical tool. What we learned We mastered Structured Output Modeling with LLMs and refined our skills in building real-time, event-driven architectures between Python and React. What's next for MedExtract Vision Integration: Extracting data from handwritten scrawls via Gemini Vision. EHR Export: One-click integration with FHIR-compliant health records. Decision Support: AI-driven risk alerts based on extracted vitals. <div