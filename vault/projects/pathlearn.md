---
slug: "pathlearn"
url: "https://devpost.com/software/pathlearn"
title: "PathLearn"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 626
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# PathLearn

> PathLearn uses DRL, RNNs, and RAG with Arch-Router-1.5B to create a deeply personalized, career-aligned learning path tailored to each student.

[Devpost](https://devpost.com/software/pathlearn) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[education]] [[health_clinical]]
**user** [[clinician]] [[developer]] [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[web_dom]]

**stack** javascript, katanemo, node.js, python, pytorch, react, sentence-transformers, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pathlearn

## Body

Actual AI chatbot tutor (trained myself) Home Screen Math Topics (example, there are many more) All topics AP Calc AB units and lessons First lesson in AP Calc AB Currently working on generating questions/answers Resources for your career path Main Page people see when entering the website. Main Page people see when entering the website. Main Page people see when entering the website. Main Page people see when entering the website. Main Page people see when entering the website. Inspiration I’ve always noticed how students struggle with learning independently—especially at home. Time management, stress, gaps in understanding, and the lack of a truly personalized tutor make studying harder than it needs to be. Existing tools like Khan Academy and AI chatbots help, but they don’t adapt to you, your pace, or your goals. I wanted to build something that understands each student as an individual learner and shapes a learning path around who they are and who they want to become. That idea became PathLearn. What it does PathLearn is an adaptive AI tutor that builds a completely personalized, career-aligned curriculum for every student. It models each student's thinking using an RNN-based memory system, tracks mastery over time, and learns the student’s learning style through a Deep Reinforcement Learning teacher agent that continuously adjusts difficulty, pacing, and concept order. All explanations, examples, and practice problems are generated through a RAG pipeline powered by katanemo/Arch-Router-1.5B, ensuring every step is grounded, accurate, and tailored. Students start by choosing both a course (Physics Honors, Algebra 2, Biology, Chemistry, etc.) and a future career (doctor, astrophysicist, biomedical researcher, engineer…). PathLearn fuses these two choices to build a dynamic curriculum that evolves with every attempt, mistake, and success. Instead of generic lessons, students receive a skill map tailored to the knowledge required for their career path. It becomes a true one-on-one tutor that adapts continuously—something no static platform or chatbot can replicate. How we built it I combined three core machine learning systems: RNN Learning Memory Model Models the student’s pace, retention, misconceptions, and improvement over time. DRL Curriculum Orchestrator A reinforcement-learning agent selects the next topic, difficulty, explanation type, and career-aligned examples based on ongoing performance. RAG + katanemo/Arch-Router-1.5B Retrieves curated textbook content, prior attempts, and example templates to generate personalized explanations, steps, and practice problems. A backend pipeline integrates these components, while the frontend adapts to each student with mastery maps, learning diagnostics, and personalized practice flows. Challenges we ran into Designing a reward function that balances difficulty, mastery, and frustration. Getting the RNN to meaningfully predict retention curves based on sparse data. Integrating RAG with Arch-Router-1.5B in a way that consistently produced career-aligned explanations. Ensuring the DRL agent didn’t overfit to a single learning pattern early on. Making the system feel “human” instead of just algorithmic. Accomplishments that we're proud of Built a genuinely adaptive learning system that goes far beyond Q&A chatbots. Got the DRL agent to meaningfully personalize topic sequencing. Created a career-driven learning experience that feels truly unique to each student. Integrated Arch-Router-1.5B into a full RAG pipeline for high-quality explanations. Developed a model that adjusts to student weaknesses in real time. What we learned I learned how powerful multi-model AI systems can be when each component plays a specific role. DRL and RNNs together can create deeply personalized learning dynamics that LLMs alone simply cannot achieve. I also gained experience building RAG pipelines, designing reward signals, and engineering scalable, adaptive education tools. What's next for PathLearn Add more courses and specialized career tracks. Train a larger student-behavior model using anonymized interaction data. Integrate more modalities like drawings, graphs, and math handwriting. Deploy PathLearn as a full online learning platform. Build student communities with AI-guided peer collaboration. Expand to college-level and professional certification tracks. <div