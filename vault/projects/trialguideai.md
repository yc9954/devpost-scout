---
slug: "trialguideai"
url: "https://devpost.com/software/trialguideai"
title: "TrialGuideAI"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 618
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/educator_student"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# TrialGuideAI

> TrialGuideAI uses AI to distill dense clinical trial protocols into accessible summaries, infographics, and videos that empower patients to understand studies and their broader impact on science.

[Devpost](https://devpost.com/software/trialguideai) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[education]] [[finance_payments]] [[health_clinical]] [[scientific_research]]
**user** [[clinician]] [[educator_student]] [[patient_family]] [[researcher]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** css, gemini, git, html, javascript, json, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trialguideai

## Body

Inspiration Our open-source clinical trial educator was created to bridge the gap between complex research protocols and the people they are meant to serve. Too often, patients and communities are left out of the scientific conversation because clinical trial information is hidden behind technical jargon and closed systems. By building an open, transparent, and interactive learning platform, we aim to make clinical research understandable, trustworthy, and empowering for everyone. Through visual explanations, AI-driven summaries, and real-world examples drawn from public trial databases, our tool helps patients, students, and clinicians alike explore how trials work, why participation matters, and how science turns data into hope. Education should never be a privilege—it should be a shared, open resource for discovery and change. What it does TrialGuideAI is an open-source tool catered for academic clinical research institutions to improve patient's knowledge and awareness of the scientific studies they can partake in. Principal investigators in charge of a clinical trial's study design can upload their lengthy protocols and receive an approachable synopsis of the trial. This enables investigators to communicate with their trial participants and explain the therapeutic's complex biological mechanisms in a more digestible manner supported with animated visuals. How we built it We built our open-source clinical trial educator using the Gemini API to transform dense clinical trial protocols into accessible, engaging learning experiences. The system ingests publicly available trial documents and uses Gemini’s advanced language understanding to extract key scientific insights—such as study purpose, interventions, eligibility criteria, and biological mechanisms. These insights are then summarized into clear educational scripts. Using additional AI APIs, we generate visuals and slideshow-style images that align with the extracted text, automatically assembling them into short, narrated video modules. The result is an interactive, multimedia learning tool that turns complex trial data into understandable, story-driven education for patients, students, and clinicians alike. Our platform shows how open AI ecosystems can make scientific transparency both beautiful and accessible. Challenges we ran into One of the biggest challenges we faced was managing image generation and API usage within the limits of free or low-cost tools. Generating consistent, high-quality visuals that matched the scientific content often required multiple API calls and fine-tuning prompts, which was difficult without paid credits. Stitching the generated images and text into smooth, coherent videos was another hurdle—especially when synchronizing voiceovers, timing, and transitions purely through code. Building automated slides and integrating them with narration required balancing creativity with technical constraints, as we had to connect several APIs for image generation, text-to-speech, and video assembly while keeping everything lightweight, open-source, and reproducible. Accomplishments that we're proud of We are super proud that we accomplished the task of building an application and website as a team. Our backgrounds are primarily within machine learning and basic science research, so we are proud that we stepped into exploring something new. We are also happy that we were able to accomplish creating an integrative generative system within a relatively short time frame. What we learned We learned how challenging yet essential clinical trials are to the long and arduous drug development pipeline. Along the way, we gained skills in agentic workflow design, full-stack development, and the effective use of generative APIs to create a more transparent and informed participant experience. What's next for TrialGuideAI We want to build a more advanced version of our platform that can generate longer, more comprehensive videos covering multiple clinical trials at once. Our goal is to create an open-source solution that academic labs, educators, and research institutions can easily use to teach or communicate trial information. By improving automation, we aim to handle complex datasets, summarize multiple protocols, and create cohesive educational narratives that connect different studies within a disease area. <div