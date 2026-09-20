---
slug: "office-rpg-the-career-training-simulator-qyfovm"
url: "https://devpost.com/software/office-rpg-the-career-training-simulator-qyfovm"
title: "Office RPG : The career training simulator"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 503
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
---

# Office RPG : The career training simulator

> Office-RPG is a gamified career simulator using Gemini 3 to build tech and soft skills through AI-driven quests, teaching productivity, balance, and real-world job readiness. Perfect for students!

[Devpost](https://devpost.com/software/office-rpg-the-career-training-simulator-qyfovm) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
  <sub>weak: vision_ocr</sub>
**domain** [[education]] [[mental_health]]
**user** [[educator_student]]
  <sub>weak: general_public</sub>

**stack** firebase, flask, gemini3, google-cloud, gsap, gunicorn, jwt, mongodb, nanobanana, python, react, render, shadcn, tailwind

## Body

Overview Zone Landing Page Workspace Zone Cafeteria Zone Profile Page Quest Rewards Page Office-RPG: Bridging the Modern Skills Gap with Gemini 3 🚀 The Inspiration Transitioning from a classroom to a corporate cubicle is often a "sink or swim" experience. While students may master theory, they frequently struggle with the multidimensional pressures of a real office—balancing technical tasks with soft skills, stress management, and deadline prioritization. We built Office-RPG to turn this daunting transition into an immersive, low-risk simulation where the next generation of professionals can "level up" before their first day on the job. 💡 The Gemini 3 Advantage Our project leverages the Gemini 3 model as the "Game Master," moving beyond static gameplay to a truly dynamic environment. Infinite Dynamic Quests: Unlike traditional simulators with hardcoded scenarios, we use Gemini to procedurally generate coding challenges, reading comprehension tasks, and workplace MCQs. This ensures no two "workdays" are the same. Contextual Feedback: Gemini analyzes player performance in real-time, providing constructive, AI-driven feedback that mimics a mentor’s guidance rather than a simple "Pass/Fail" screen. Adaptive Difficulty: The model adjusts quest complexity based on the player's evolving skill stats (Coding, Soft Skills, Problem-Solving), ensuring the game remains challenging but achievable. 🛠️ The Google Tech Stack To build a scalable, high-fidelity experience, we utilized a robust Google-centric ecosystem: Gemini API: The core engine for dynamic content and intelligent NPC interactions. Firebase Authentication: Secured, seamless onboarding via GitHub and Google login. Firebase Hosting: Optimized delivery for our high-performance React frontend. Google Cloud Functions: For serverless processing of game logic and AI prompts. 🕹️ How We Built It We adopted a modern, responsive architecture to ensure the simulation felt like a premium consumer game: Frontend: React + Vite for speed, paired with Tailwind CSS and Shadcn/UI for a sleek, corporate-themed aesthetic. State Management: Framer Motion for smooth "Zone Transitions" (Workspace to Cafeteria) to enhance immersion. Backend: A Python/Flask API layer to bridge the frontend with Gemini’s generative capabilities. Game Mechanics: A dual-axis stat system inspired by RPGs. The Performance Logic: Performance = (Skill Level * Mood) / Stress Players must balance productivity with "Mental Health" by visiting the Game Lounge or Cafeteria to prevent burnout. 🚧 Challenges & Learnings Prompt Engineering for Consistency: Initially, AI-generated quests varied too much in format. We learned to use strict JSON schema prompting to ensure the frontend could reliably parse Gemini's output. State Equilibrium: Balancing the "Stress vs. Reward" mechanic was tough. We had to iterate on the math to ensure the game felt like a challenge rather than a chore. Real-time Immersion: Integrating a live "Office Music Player" and digital clock taught us the importance of ambient UX in educational tools. 🌍 Impact & SDGs Office-RPG isn't just a game; it's a tool for SDG 8 (Decent Work & Economic Growth) and SDG 4 (Quality Education) . By democratizing "vocational training" through a free web app, we are preparing youth for a resilient future. "Office-RPG transforms the anxiety of the first job into the excitement of the first quest." <div