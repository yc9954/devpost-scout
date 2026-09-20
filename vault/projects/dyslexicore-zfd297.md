---
slug: "dyslexicore-zfd297"
url: "https://devpost.com/software/dyslexicore-zfd297"
title: "DyslexiCore"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 484
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "substrate/structured_db"
---

# DyslexiCore

> Turning play into early detection for learning difficulties

[Devpost](https://devpost.com/software/dyslexicore-zfd297) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[health_clinical]]
**substrate** [[structured_db]]

**stack** fastapi, javascript, mongodb, next.js, node.js, python, react.js, tailwind-css, web-speech-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dyslexicore

## Body

Profile Badges Front page Intervention Games Diagonstic Games Games Child Status Assingments Multilingual Parent Mode Inspiration Millions of children with dyslexia and other learning difficulties go undiagnosed in their early years due to lack of accessible, engaging, and affordable screening tools. Traditional assessments are often stressful, time-consuming, and not easily available to all families. We wanted to create a solution that removes fear and pressure from learning assessments by turning them into something natural and enjoyable. The idea behind DyslexiCore is simple — if children learn through play, why not detect learning patterns through play as well? What it does DyslexiCore is an AI-powered, gamified system designed to identify early signs of dyslexia in children aged 4–9. Instead of formal testing, children interact with simple games such as phoneme recognition, memory challenges, and word-building activities. While they play, the system tracks behavioral signals like response time, accuracy, sound recognition, and attention patterns. This data is analyzed to generate a basic risk profile and identify potential learning difficulties. The platform also includes: A parent-only dashboard showing skill-wise progress, risk levels, and activity insights A rule-based AI companion that guides and encourages the child Personalized recommendations based on the child’s performance How we built it We developed DyslexiCore as a full-stack prototype: Frontend: React / Next.js for interactive UI and game interfaces Backend: Node.js / FastAPI to handle data storage, scoring, and analysis Database: MongoDB for storing activity logs and child profiles Game Logic: Custom mini-games designed to capture cognitive signals Voice Integration: Web Speech API for phoneme-based interaction (e.g., “ka”, “ma”) Each game sends structured data (accuracy, response time, errors) to the backend, which processes it into skill scores and updates the parent dashboard in real time. Challenges we ran into Designing games that are both fun for children and meaningful for diagnosis Translating gameplay behavior into useful cognitive insights Ensuring the system tracks data in a structured way for analysis Balancing simplicity in UI while maintaining functional depth Simulating AI behavior using rule-based logic within limited time Accomplishments that we're proud of Successfully created a working prototype combining diagnosis + intervention Built a real-time tracking system that updates a parent dashboard Designed multiple games targeting different cognitive skills Integrated a guiding AI companion to enhance child engagement Created a solution with strong real-world impact potential What we learned How to design systems focused on user behavior, not just outputs The importance of user-centered design, especially for children How to structure data for meaningful analysis in real time The challenges of combining AI concepts with interactive UX Building a full-stack system under time constraints What's next for DyslexiCore Enhancing the AI system to move from rule-based to machine learning-based predictions Improving accuracy of risk detection using larger datasets Adding more adaptive and personalized learning pathways Expanding language support (multilingual phoneme systems) Conducting user testing with educators and parents Scaling the platform for real-world deployment <div