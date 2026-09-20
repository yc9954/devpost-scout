---
slug: "stemify-uwtyx6"
url: "https://devpost.com/software/stemify-uwtyx6"
title: "STEMIFY"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 876
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/mental_health"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# STEMIFY

> Stemify is an AI-powered STEM tutor that adapts question difficulty, reinforces weak concepts, and provides guided hints instead of answers, helping students build true understanding and mastery.

[Devpost](https://devpost.com/software/stemify-uwtyx6) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[runtime_tool_creation]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[mental_health]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[web_dom]]

**stack** api, css, flask, gemini, git, google, html, javascript, python, render

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stemify

## Body

STEMIFY Choose a topic you want to study. Pressing start starts a 10 question session. If you get a question right. If you get a question wrong, it explains the steps to the answer instead of giving answer outright. Actively track your score. Inspiration As a student, I've spent countless hours practicing STEM subjects, especially mathematics. One thing that always frustrated me was how learning platforms handled mistakes. If I got a question wrong, I was usually shown the correct answer immediately. For instance, if I miscalculated the derivative of a function: $ $ d/dx(3x^2 + 5x) = 6x + 5 $$, an answer key would just show me $6x + 5$ and move on. While that solved the immediate question, it didn't help me understand why I missed the power rule or the constant rule. It didn't address my conceptual gap. I started wondering: What if a learning platform behaved more like a human tutor than a rigid answer key? Instead of simply telling students they were wrong, what if it could identify weak areas, provide adaptive guidance, and scaffold the learning process? That idea became Stemify. My goal was to build a platform that focuses on deep understanding rather than rote memorization, helping students see what they truly know and where they need more practice. What it does Stemify is an AI-powered, adaptive STEM learning platform designed to create a personalized workflow for every student. Students are presented with practice questions generated around a specific topic. Throughout a learning session, the platform tracks performance, records incorrect answers, and identifies concepts that require reinforcement. The platform adapts to student performance in several key ways: Dynamic Difficulty: Problem complexity scaling increases automatically when students demonstrate mastery. Targeted Reinforcement: Concepts that are repeatedly missed are flagged and revisited through similar, alternative questions. Performance Summaries: Session performance is tracked, aggregated, and summarized for the user. Guided Explanations: Instead of revealing the final answer immediately, the AI provides strategic hints and intermediate steps to encourage independent problem-solving. How we built it I built Stemify as a full-stack web application designed for a seamless, responsive user experience: Backend: Python and Flask managed the core server routing and session logic. Frontend: HTML, CSS, and vanilla JavaScript handled the dynamic UI and real-time state changes. AI Engine: Google Gemini was integrated to dynamically generate educational content, generate variations of math problems, and provide intelligent, conversational hints. Deployment: The application was deployed on Render to make it publicly accessible online. Challenges we ran into Building the project entirely on my own meant wearing every hat simultaneously—from product designer to DevOps engineer. Integrating generative AI into a live educational workflow introduced several strict technical obstacles. I encountered deployment bottlenecks, API quota limitations, environment variable configuration issues, and severe response formatting inconsistencies. Because LLMs can be unpredictable, ensuring the AI consistently returned clean, parseable JSON data for the frontend was a massive hurdle. Another major challenge was pedagogical rather than technical. It is surprisingly difficult to prompt an AI to give good hints without giving away the answer. Writing a prompt that forces the AI to act like Socrates—guiding the student via questions—required a massive amount of prompt engineering and trial-and-error. Accomplishments that we're proud of -Building a Functioning EdTech Prototype Solo: Successfully designing, developing, and deploying a full-stack application completely from scratch. Translating an abstract educational philosophy into working software was a massive personal milestone. -Creating a "Socratic" AI Tutor: Engineering a robust prompting framework that successfully restrains the LLM from simply giving away answers. Getting the AI to reliably guide students through hints rather than handing them an easy out was a major win for the core mission of the project. -Dynamic Feedback Integration: Building a functioning adaptive loop that responds to user input in real time. Seeing the system successfully detect a student's struggle and automatically pivot to generate customized reinforcement questions felt like a true proof of concept. -Bridging Code and Pedagogy: Designing an application where the technical features directly serve a human outcome—helping students overcome math anxiety and focus on mastery over speed. What we learned Building Stemify taught me much more than software engineering. Through this journey, I learned how to: -Build, containerize, and deploy a full-stack application independently. -Implement structured outputs and error-handling guardrails for LLMs in production. -Debug live cloud deployment and API integration issues under constraints. -Design software architecture around user learning outcomes rather than just cool technical features. Perhaps the most important lesson was realizing that technology alone does not improve education. The real engineering challenge is designing experiences that help students build genuine confidence and intuition. What's next for STEMIFY This prototype represents the first step toward a much larger vision. Future iterations of Stemify will include: Persistent Profiles: Student accounts with long-term data persistence. Advanced Analytics: Predictive analytics to map a student's learning decay curve over time. Gamification: Achievements, milestones, and learning streaks to boost daily engagement. Broader Curriculum: Expanding STEM coverage into physics, chemistry, and computer science. Algorithmic Adaptivity: Moving beyond simple threshold logic to a more advanced Bayesian knowledge tracing algorithm for precision personalization. Stemify started with a belief that students deserve more than static answer keys. This project is my first step toward turning that belief into a reality. <div