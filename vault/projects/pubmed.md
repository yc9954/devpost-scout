---
slug: "pubmed"
url: "https://devpost.com/software/pubmed"
title: "Pubmed"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 620
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/media_journalism"
  - "domain/scientific_research"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Pubmed

> Your Scientific Filter in a World of Viral Myths.

[Devpost](https://devpost.com/software/pubmed) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[vision_ocr]]
**domain** [[education]] [[media_journalism]] [[scientific_research]]
**user** [[researcher]]
**substrate** [[structured_db]] [[video_visual]]

**stack** backend, fastapi, flask, framework, langchain, natural-language-processing, node.js, openai-api, python, react, vue.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pubmed

## Body

Inspiration Social media has unfortunately transformed into a breeding ground for unverified health advice and baseless scientific myths. What is most alarming is that this misinformation spreads far quicker than actual scientific truths. In a domain that directly impacts human lives, the answer to the critical question—"How do I find the truth?"—has remained trapped behind the heavy, jargon-filled walls of academic papers. We realized that an everyday internet user cannot spend hours conducting literature reviews just to fact-check a viral post. This is exactly where the idea for Pubmed was born: to build a bridge between the chaos of the digital world and the safe harbor of science, making rigorous fact-checking accessible to everyone. What it does Pubmed is an intelligent AI shield that instantly debunk or validates questionable medical and scientific claims encountered on social media. When a user uploads a controversial text, tweet, or screenshot found on platforms like X or Instagram, Pubmed’s backend AI engine goes to work. It analyzes the core assertions, translates them into structured queries, and cross-references them against real-world papers from the world's most prestigious, peer-reviewed academic databases (such as PubMed). Instead of returning dense academic jargon, it delivers a clear verdict—such as "True," "False," or "Misleading"—accompanied by a simplified, easy-to-understand summary explaining the scientific reality behind the claim. How we built it At the heart of our project lies an advanced Natural Language Processing (NLP) architecture capable of translating complex academic data into everyday language. For the frontend, we designed a clean, modern web prototype where users can effortlessly paste copied social media content. Due to the limited timeframe of the hackathon, our current prototype is functioning deterministically, providing specific, pre-defined, and optimized answers to a set of core questions. This controlled setup ensures that the system generates highly accurate, manipulation-free verification reports in its initial stage. Challenges we ran into Our greatest hurdle during development was bridging two entirely contrasting worlds: the superficial, sensationalized language of social media and the dense, technical vernacular of academia. Training the AI to condense multi-page, complex medical papers into simple, public-friendly summaries—without losing a single shred of factual accuracy—proved to be an immense challenge. Furthermore, ensuring absolute neutrality and preventing AI hallucinations required us to implement strict guardrails and execute meticulous prompt engineering throughout the hackathon. Accomplishments that we're proud of Within the tight constraints of a hackathon, we are incredibly proud to have delivered a living, breathing prototype that addresses a profound societal pain point rather than just a theoretical concept. Witnessing that breakthrough moment—where a chaotic piece of social media text was analyzed and accurately verified with real-world scientific citations in mere seconds—was deeply rewarding. We succeeded in positioning AI not just as an entertainment novelty, but as a protective shield designed to elevate public scientific literacy. What we learned This intense journey demonstrated to us the immense, transformative power that AI holds within STEM education and social good initiatives. We gained valuable hands-on experience interfacing with academic APIs and synthesizing vast pools of data into meaningful insights. Above all, we learned that what truly makes a technical product great isn't just the complexity of the code running in the background, but the profound sense of trust and clarity a user feels the moment they interact with it. What's next for Pubmed This prototype is merely the opening chapter for Pubmed. Moving forward, we aim to develop native browser extensions and mobile widgets so users can cross-check claims instantly while scrolling through X, Instagram, or TikTok—without ever needing to open a separate app. Additionally, by integrating computer vision, we plan to automatically analyze video clips and infographic images, scaling Pubmed into a global ecosystem dedicated to fighting digital misinformation at its source. <div