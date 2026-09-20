---
slug: "quanta-t5rsd3"
url: "https://devpost.com/software/quanta-t5rsd3"
title: "Quanta (AP Physics tutor)"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 505
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/web_dom"
---

# Quanta (AP Physics tutor)

> The AP Physics courses are one of the hardest courses to study for in high school, but with Quanta, studying has never been easier.

[Devpost](https://devpost.com/software/quanta-t5rsd3) · hackathon [[DSH Hacks V1]]

## Facets

**domain** [[education]]
  <sub>weak: finance_payments</sub>
**user** [[educator_student]]
**substrate** [[web_dom]]
  <sub>weak: video_visual</sub>

**stack** claude-api, css, html, javascript, json, katex, latex, python

## Body

Inspiration AP Physics is one of the hardest exams a high school student can take. Before the 2025 redesign, AP Physics 1 had one of the lowest pass rates of any AP exam; under half of the students passed. I myself have taken these classes as a high schooler and struggled a lot. Throughout my journey, I tried to find a tool that could help me with these topics, but I unfortunately never really found any. That is why I made my own AP Physics Study tool. Quanta. Quanta exists to give every AP Physics student a tutor. What it does Quanta covers all four AP Physics courses - Physics 1, Physics 2, Physics C: Mechanics, and Physics C: E&M, all up to date with the 2025-2026 course framework Learn - deep, exam-focused explanations of any topic, structured into intuition, key equations, a derivation/deeper dive, a worked example, common mistakes, and exam tips. Solve - a problem tutor that takes any physics problem and returns a full worked solution that teaches the method: strategy, symbolic-then-numeric steps, a sanity check, and pitfalls. Quiz - unlimited AP-style practice questions for any unit or a mixed review, at four difficulty levels, with instant explanations, an optional AI-graded free-response question, and a study log that tracks progress. Formulas - a clean equation reference for every course. How we built it Backend: Python + Flask, with four JSON API endpoints: explain, solve, quiz, grade. AI: the Anthropic Claude API. Each endpoint uses an engineered prompt with a shared physics-tutor system prompt. The quiz endpoint asks the model for strict JSON and parses it into an interactive UI. Frontend: vanilla HTML/CSS/JS - no framework - with KaTeX for real equation rendering and marked.js for formatting. Curriculum: the unit structure and formula reference are stored as data in the backend, verified against the College Board's frameworks. Technical depth Math-safe markdown pipeline: LaTeX spans are extracted and protected before markdown parsing, then restored and rendered with KaTeX, so equations never get mangled by the formatter. Structured AI output: the quiz feature prompts for and parses strict JSON, with fence-tolerant extraction, turning a language model into a reliable question generator. Real-world impact Quanta is usable by any of the hundreds of thousands of students who take an AP Physics exam each year. Because the content is AI-generated rather than a fixed question bank, the practice material is effectively unlimited and adapts to whatever unit, difficulty, or specific problem a student is stuck on. This could help thousands of kids like me, who struggled a lot taking AP Physics. I want other students to be more successful taking AP Physics than I ever was. Challenges Getting LaTeX to survive a markdown parser cleanly. Designing prompts that produce rigorous, exam-accurate physics rather than hand-wavy explanations. Verifying the curriculum against the recent AP redesign, since most prep material online is still outdated. What's next Per-topic mastery tracking and spaced-repetition review. Diagram and free-body-diagram generation. Photo upload so students can solve a problem straight from their worksheet. <div