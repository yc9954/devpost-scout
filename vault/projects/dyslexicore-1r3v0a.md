---
slug: "dyslexicore-1r3v0a"
url: "https://devpost.com/software/dyslexicore-1r3v0a"
title: "DyslexiCore"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 1050
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# DyslexiCore

> Empowering neurodivergent learners through personalized skill-quests and intelligent screening tools

[Devpost](https://devpost.com/software/dyslexicore-1r3v0a) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[accessibility]] [[developer_tools]] [[education]] [[health_clinical]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]]

**stack** fastapi, framer, jwt, next.js, passlib, python, react, sqlalchemy, sqlite, tailwind, typescript, uvicorn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dyslexicore

## Body

Register for new users Login Page Bubble game = Smart Companion Bubble game assessment page CVC Word Explorer Dashboard Skill quest( typing game) Phonics Adventures Family Support Hub Typing game Dashboard Star Tracker( Readiness Check) Star Tracker Inspiration The inspiration for DyslexiCore stems from a critical flaw in the current educational landscape: the "Wait to Fail" model. In many school systems, children with dyslexia aren't identified until they have already fallen significantly behind their peers, leading to a loss of confidence and academic frustration. As I researched the problem, I realized three things that drove me to build this ecosystem: Accessibility Gap: Clinical assessments are often expensive and have long waiting lists. I wanted to build a tool that provides immediate, preliminary screening at no cost. Engagement Deficit: Standard literacy interventions can feel like "extra work" or "drills" for a child who is already struggling. I was inspired to turn these exercises into Skill-Quests, using gamification to transform a source of stress into a source of achievement. The Need for a "Core" Hub: Most tools are fragmented—one app for testing, another for reading, and a separate one for tracking. I envisioned DyslexiCore as a unified engine where the data from the screening directly informs the learning path, all while being supported by an encouraging AI companion. I built DyslexiCore to prove that technology can do more than just digitize paper tests; it can create a supportive, permanent environment that grows alongside a child’s literacy journey What it does DyslexiCore is an integrated, full-stack literacy engine designed to transform the journey of neurodivergent learners from early identification to mastery. It functions as a cohesive ecosystem that bridges the gap between clinical screening and daily classroom support: Precision Screening & Risk Profiling: Using the screening and assessment modules, the platform identifies early indicators of dyslexia through interactive phonological tasks. The backend calculates a Risk Level based on accuracy and naming speed, providing immediate clarity for parents and educators. Targeted Skill-Quests: DyslexiCore converts assessment data into a personalized intervention path within the skill-quest and learn modules. Students embark on missions like Phoneme Peak and CVC Kingdom, which break down complex reading skills into manageable, gamified "Quests." Intelligent Learning Companion: In the chat module, a specialized AI tutor provides 24/7 support. It acts as an encouraging partner that offers positive reinforcement, explains tricky word patterns, and ensures students stay motivated through a "success-first" approach. Persistent Progress Architecture: Through the dashboard, the platform provides high-fidelity visualization of a student's growth. Unlike temporary tools, I built DyslexiCore with a persistent SQLite database, ensuring every "Achieved Badge" and mastery milestone is saved securely and permanently. Comprehensive Support Hub: The support module serves as the platform’s resource center, offering parents and teachers structured literacy guides and community tools to support the student's development outside of the app. How we built it I chose a modern, high-performance stack to ensure DyslexiCore is fast, secure, and capable of handling persistent data for educational growth. Next.js (App Router): Used for the frontend to create a modular, SEO-friendly, and highly responsive user interface across all modules (screening, dashboard, learn). FastAPI: Powering the backend with high-performance asynchronous logic to handle complex assessment scoring and data processing. SQLAlchemy: The Object-Relational Mapper (ORM) used to translate Python code into database logic, allowing for seamless data management. SQLite: The persistent database engine that stores all user records, test scores, and quest progress permanently in a single file (dyslexia_app.db). JWT (JSON Web Tokens): Implemented for secure, token-based authentication in the (auth) folder to protect sensitive student assessment data. Passlib (sha256_crypt): Used for military-grade password hashing to ensure user security. Tailwind CSS: Utilized for rapid, responsive UI development, ensuring the platform looks professional on both tablets and desktops. Pydantic: Used for strict data validation between the frontend and backend to prevent errors during assessment submissions. Challenges we ran into The "Mock-to-Real" Transition: The biggest technical hurdle was moving from a simple in-memory mock system to a persistent database. I had to refactor the entire backend to ensure that when a student finishes a quest, the data travels through the API and is saved permanently in SQLite via SQLAlchemy. Synchronizing the Ecosystem: With a frontend structure containing over seven distinct modules (Screening, Assessment, Skill-Quest, etc.), I initially faced several 404 Not Found errors. I had to meticulously map every Next.js folder to a corresponding FastAPI endpoint to ensure the "handshake" between frontend and backend was seamless. Security for Sensitive Data: Implementing JWT (JSON Web Tokens) as a solo developer was challenging. I had to ensure that private assessment results were securely tied to a specific user ID, preventing any data leaks during the demo. Accomplishments that we're proud of Full-Stack Persistence: I successfully built a backend where data actually "lives." Restarting the server doesn't erase a child’s progress, which is critical for an educational tool. Unified Architectural Design: I am proud of how I organized the project into a clean, modular hierarchy. The folder structure makes it easy to see the user journey—from initial screening to daily support. Local AI Integration: I successfully implemented a specialized "Smart Companion" logic that provides instant, positive feedback to users, making the app feel like a supportive tutor rather than a cold testing tool. What we learned API Design Patterns: I learned the importance of strict data validation using Pydantic. This prevented the frontend from sending "junk" data that would crash the scoring algorithm. State Management in Education: I discovered that for neurodivergent learners, the "State" (their current progress, badges, and streaks) is a huge motivator. Learning how to manage this state in a database was a massive takeaway. Solo Agile Development: Building an entire ecosystem alone taught me how to prioritize features—focusing first on the "Happy Path" (Login → Screening → Dashboard) to ensure a winning demo. What's next for DyslexiCore Advanced Analytics: I plan to implement more complex math for naming-speed assessments, using $Words\ Per\ Minute$ (WPM) tracking to show parents detailed fluency graphs.Multi-User Roles: I want to expand the (auth) module to include a "Teacher Portal," where an educator can monitor the progress of an entire classroom of students from one dashboard.Voice Integration: To further assist children with reading difficulties, I aim to integrate a text-to-speech engine that can read the "Skill-Quests" aloud, making the platform even more accessible. <div