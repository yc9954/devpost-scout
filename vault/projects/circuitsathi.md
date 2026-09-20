---
slug: "circuitsathi"
url: "https://devpost.com/software/circuitsathi"
title: "CircuitSathi"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 507
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
---

# CircuitSathi

> Stop memorizing circuits. Start experiencing them. CircuitSathi combines AI, real-time simulation, and gamification to turn electronics education into an engaging, hands-on learning journey.

[Devpost](https://devpost.com/software/circuitsathi) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]]

**stack** api, css, express.js, flow, gemini, mammoth, mongodb, mongoose, next.js, parse, pdf, pixijs, react, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for circuitsathi

## Body

Inspiration As an Electrical Engineering student , I’ve seen firsthand how difficult it is for beginners to truly understand circuits. Students often memorize formulas and solve numerical problems but still struggle to visualize how current flows or why components behave the way they do. That inspired me to build CircuitSathi —an AI-powered platform where students can build circuits, simulate them, ask questions, and learn through interactive visualization instead of rote memorization. I built CircuitSathi because I wanted future students to learn electronics the way I wish I had—through exploration, visualization, and understanding, not just memorization. ⚡ CircuitSathi – Making Electronics Come Alive What it does CircuitSathi is an AI-powered STEM learning platform that combines circuit design, simulation, tutoring, and voice assistance into one interactive workspace. Users can: Build circuits using a drag-and-drop editor Run simulations and observe circuit behavior Learn with an AI tutor that explains concepts step by step Upload PDF or DOCX lab manuals and generate structured tutorials Listen to AI-generated voice explanations Save and reload projects for future learning Instead of simply giving answers, CircuitSathi encourages students to understand why a circuit behaves the way it does. How we built it The project follows a full-stack architecture. The frontend was built with Next.js , React , TypeScript , React Flow , PixiJS , Tailwind CSS , and Zustand to provide an interactive visual workspace. The backend uses Express.js and MongoDB to manage projects, simulations, uploads, and AI services. For intelligent tutoring, we integrated large language models to generate structured explanations and learning paths. PDF and DOCX parsing allows students to convert traditional lab manuals into interactive lessons, while text-to-speech technology provides accessible voice narration. The result is a unified platform that blends education, simulation, and AI into a single learning experience. Challenges we ran into One of the biggest challenges was balancing educational value with usability. We wanted beginners to feel comfortable without sacrificing the technical depth needed for meaningful learning. Building a responsive workspace with multiple panels, real-time interactions, and project persistence required careful state management and architecture decisions. Another challenge was generating AI tutorials that explain concepts clearly rather than simply producing direct answers. Designing prompts and workflows that encourage understanding instead of memorization required multiple iterations. What we learned Throughout this project, we learned that effective educational tools are not just about adding AI—they are about designing experiences that encourage curiosity and exploration. We gained practical experience in: Building scalable full-stack applications Managing complex frontend state Integrating AI into educational workflows Designing interactive learning interfaces Combining simulation with personalized tutoring Most importantly, we learned that visualization and guided learning can make even complex engineering concepts approachable for beginners. What's next for CircuitSathi We envision CircuitSathi evolving into a complete AI-powered electronics learning ecosystem. Future plans include: Multiplayer collaborative labs AI-powered debugging assistance Classroom analytics for teachers Mobile application support AR/VR visualization of circuits Expanded curriculum covering advanced electronics and embedded systems Our mission is simple: To transform electronics education from passive memorization into interactive understanding through AI, simulation, and visualization. <div