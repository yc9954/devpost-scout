---
slug: "llm-cvt-analysis-of-echocardiograms"
url: "https://devpost.com/software/llm-cvt-analysis-of-echocardiograms"
title: "LLM + CvT Analysis of Echocardiograms"
hackathon: "AmpliCode Hackathon 2025"
organization: "AmpliCode"
winner: true
words: 203
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
---

# LLM + CvT Analysis of Echocardiograms

> My project takes a short echocardiogram (15-second video) and allows a clinician to analyze the data with ML using an LLM, RAG, and a Vector search, which can diagnose the patient from the video.

[Devpost](https://devpost.com/software/llm-cvt-analysis-of-echocardiograms) · hackathon [[AmpliCode Hackathon 2025]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]

**stack** data-analysis, flask, machine-learning, python

## How they structured the write-up

- inspiration
- how i built it

## Body

Presentation demo of the specific algorithms in the project Inspiration My mom is a cardiac sonographer, and I noticed that she transcribes various values manually from an echocardiogram whenever she makes a scan. I thought to myself that if she messed up with that task, the patient's outcome would be wrong, and I decided to build a system that can cross-check her values with AI. After building this part, I then went back into contemplation, and I noticed that the cardiologist at the clinic handled many cases at once. Due to this, I added a functionality to my app that uses AI to diagnose the patient. There is also the opportunity to perform a Vector Search, which gets all the cases similar in cardiac structure to the current patient. This offers a clinician as much data as possible to make a diagnosis. How I built it I built this project with ML in Python. I then developed a web-based application demonstrated in my video. Unfortunately, there isn't a public demo for this project, due to the massive server costs of running the CVT and LLM algorithms. In the future, I hope to get this down to make a free public access beta. <div