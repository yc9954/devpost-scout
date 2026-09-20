---
slug: "sage-dtukeb"
url: "https://devpost.com/software/sage-dtukeb"
title: "SAGE"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 428
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
---

# SAGE

> Understand, don't just recall. SAGE is a Gemini-powered Socratic study companion. Instead of answers, it gives you the right questions -dismantling assumptions until real understanding remains

[Devpost](https://devpost.com/software/sage-dtukeb) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]

**stack** css, figma, framer, gemini, javascript, openai, postgresql, sql, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sage

## Body

SAGE Inspiration We noticed most AI tutors behave like answer engines—students ask, AI explains, and the learning stops at passive understanding. Real learning happens differently: through questioning, confusion, and discovery. SAGE was inspired by the idea of turning AI into a thinking partner that teaches the way great teachers do. What it does SAGE is an AI tutor that guides students through a 5-stage learning process: Elicit, Destabilize, Bridge, Build, and Stress Test. Instead of giving direct answers, it uses Socratic questioning, analogies, and adaptive challenges to help students construct their own understanding and test it through edge cases. How we built it We built SAGE using a conversational AI pipeline with structured prompting for each learning stage. The system dynamically adapts based on student responses, combining misconception handling, analogy generation, and difficulty adjustment. We also integrated cognitive science principles like scaffolding and retrieval-based learning into the interaction flow. Challenges we ran into The hardest part was preventing the AI from defaulting to giving direct answers. Designing prompts that consistently enforce questioning over explanation required multiple iterations. Another challenge was balancing confusion and clarity—keeping students challenged without overwhelming them. Accomplishments that we're proud of We successfully designed a multi-stage AI tutoring system that doesn't just explain concepts but actively builds understanding. We also embedded principles from philosophy and psychology (Socrates, Piaget, Vygotsky, Feynman, Bjork, Ebbinghaus) into a working interaction loop that adapts in real time. What we learned We learned that effective learning is not about information delivery but about mental model formation. The best teaching moments happen when students struggle productively and arrive at answers themselves. We also learned how difficult it is to override an AI’s natural tendency to “help” by explaining. What's next for SAGE Next, we plan to add deeper personalization through long-term memory of student misconceptions, subject-specific tutoring modes (math, physics, programming), and real-time emotional state detection. We also aim to expand SAGE into a full learning platform that supports adaptive curricula and spaced reinforcement. Its design is grounded in: Socrates → learning through questioning instead of instruction Piaget → knowledge grows through cognitive conflict (disequilibrium) Vygotsky → adaptive scaffolding within the Zone of Proximal Development Feynman → understanding through intuitive analogies Bjork → learning improves through desirable difficulty and struggle Ebbinghaus → memory strengthens through active retrieval Together, these ideas show that real learning happens when students are challenged to think, not when they are given answers. This philosophy directly shaped SAGE’s 5-stage learning loop, making it a system designed around reasoning, struggle, and self-construction of knowledge rather than passive explanation. <div