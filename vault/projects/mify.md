---
slug: "mify"
url: "https://devpost.com/software/mify"
title: "MIFY"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 606
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# MIFY

> Medical Insights For You!

[Devpost](https://devpost.com/software/mify) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]] [[scientific_research]]
**user** [[patient_family]] [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** amazon-web-services, api, chroma, claude, fetch.ai, gcp, ngrok, postman, python, treehouse, vapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mify

## Body

Inspiration We were inspired by the massive inefficiencies and ethical challenges in clinical trial patient recruitment. Over 80% of trials fail to meet their enrollment deadlines , primarily because the process of matching patients to trials is slow, manual, and relies on complex Informed Consent Forms (ICFs) and lengthy medical histories. We realized that by combining AI-driven document parsing and personalized prescreening, we could drastically cut down the time it takes for eligible patients to find the right trials, making life-saving research more accessible and efficient. What it does MIFY is an all-in-one patient recruitment platform that leverages generative AI to streamline the clinical trial pipeline for both patients and researchers. AI-ICF Generation: Users upload complex, jargon-heavy ICFs. MIFY's AI instantly parses and summarizes the eligibility criteria into clear language. AI Medical Prescreening: Patients complete a dynamic, interactive prescreening questionnaire. The AI cross-references their answers with the parsed ICF criteria, providing an instant, high-confidence eligibility score . Trial Recommendation: Based on the AI-prescreening results, the platform recommends the most relevant clinical trials, giving patients a direct path to enrollment and researchers a pipeline of qualified candidates. How we built it We designed the platform as a full-stack application. Frontend: We used React and Tailwind CSS , and Python/Streamlit to build a modern, clean, and intuitive user interface, focusing on accessibility for patients. Backend & AI: The core logic was built using Python/Flask (or Node.js/Express, depending on your actual stack). The AI functionality relies on: Large Language Models (LLMs) (specifically Claude) for document understanding (parsing ICFs and extracting structured eligibility criteria). Custom logic to map patient input from the prescreening forms to the extracted criteria for accurate matching. Database: PostgreSQL was used to store user profiles, trial data, and the structured eligibility criteria. Voice Integratiob: Vapi was used in order to develop AI agents to prescreen patients. Challenges we ran into The primary challenge was ensuring medical accuracy and reliability in the AI-driven processes. Jargon Handling: Medical terminology in ICFs is highly specific. Training the LLM to accurately distinguish between inclusion and exclusion criteria, and to correctly handle ambiguous phrasing, required significant prompt engineering and iterative testing. Rapid UI Development: Designing a complex, multi-step application with several data inputs and outputs (ICF upload, prescreening form, result display) within the hackathon timeframe pushed our front-end team to its limit. Accomplishments that we're proud of We are most proud of the AI-ICF Summarizer . In a demo, we were able to upload a sample ICF template and have the key inclusion/exclusion criteria distilled and ready for matching in under 15 seconds . This process typically takes researchers hours. We're also proud of successfully integrating a complex, multi-stage AI workflow into a simple, single-page application experience. What we learned We learned the profound power of translating unstructured data (PDFs) into structured, queryable data using modern LLMs. Specifically, we gained deep experience in: Prompt Engineering for Classification: Efficiently instructing the LLM to perform high-stakes classification (inclusion vs. exclusion) on large blocks of text. User Experience in Healthcare: The critical importance of simplifying complex workflows to build trust and encourage engagement from patients who are often dealing with challenging medical situations. What's next for MIFY Our immediate next steps for MIFY are to: Integrate Real-Time Trial Feeds: Connect the platform to publicly available trial registries (like ClinicalTrials.gov) to move from static data to a dynamic, real-world recommendation engine. Add Researcher Dashboard: Develop a dedicated interface for clinical coordinators to track the quality and volume of their prescreened patient pipeline. Enhance Patient Education: Incorporate short, AI-generated educational summaries about the medical conditions relevant to the recommended trials to further empower patient decision-making. <div