---
slug: "eduadapt"
url: "https://devpost.com/software/eduadapt"
title: "EduAdapt"
hackathon: "Google Chrome Built-in AI Challenge 2025 "
organization: "Google"
winner: true
words: 527
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/web_dom"
---

# EduAdapt

> Chrome extension that uses on-device Gemini Nano to turn any web page into a neurodivergent-friendly reading experience tailored for ADHD and Dyslexia students in seconds.

[Devpost](https://devpost.com/software/eduadapt) · hackathon [[Google Chrome Built-in AI Challenge 2025]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[realtime_stream]]
**domain** [[accessibility]] [[education]] [[labor_employment]] [[supply_logistics]]
**user** [[educator_student]] [[researcher]]
**substrate** [[web_dom]]

**stack** css, html, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eduadapt

## Body

extension popup extension popup original page dyslexia adapter ADHD adapter dyslexia adapter Inspiration I’ve always been fascinated by how AI can improve everyday lives, so I asked my mom, an elementary school teacher, where she struggled most. She described how many neurodivergent students slip through the cracks because schools simply can’t provide sustained support. EduAdapt grew out of that conversation: a way to give teachers and students a self service toolkit that keeps working even when individualized attention isn’t possible. What it does EduAdapt is a Chrome extension that reshapes any webpage in real time using on device Gemini Nano so students with Dyslexia or ADHD get grade-aware summaries, checklists, and simplified text, while teachers can dial in custom settings for age, profile, and support level even when they can’t stay at a student’s side. How we built it I started by interviewing my mom about the techniques she uses to keep neurodivergent kids focused and reading confidently. That sparked deeper research: I combed through academic papers and spoke with friends doing Phds in special education to validate the strategies. It quickly became clear that Chrome’s on-device Gemini APIs were the perfect fit, privacy friendly, fast, and built to rewrite text on the fly. From there, I built a Manifest V3 extension that runs entirely client-side: the popup captures grade/profile settings, the content script extracts page structure, and the service worker orchestrates Prompt API rewrites and Summarizer quick scans while caching responses for speed. Challenges we ran into Getting Chrome’s experimental AI flags working was my first hurdle, I hadn’t touched these APIs before, so the Dev/Canary setup took a few rounds (and a dive into Stack Overflow) before the extension could even talk to Gemini Nano. Once that worked, the real battle was latency: the model is fast, but when you’re designing for students with attention challenges, every second feels long. We iterated quickly, streaming the first rewritten sentences, caching summaries, and prioritizing above-the-fold paragraphs, to keep the experience feeling instant. Those tricks help, but further tuning is still on the roadmap. Accomplishments that we're proud of This challenge let me flip the usual script: instead of building AI features for a company roadmap, I got to chase a personal idea from scratch. Seeing teachers and specialists, people who face these challenges every day, light up when I showed them the prototype was incredibly motivating. It’s proof that the tools I use daily can have a real impact in classrooms, and that makes me proud. What we learned I’m only about a year into building web apps, and this was my first extension, so almost every step was new ground. From wiring up Manifest V3 to orchestrating Chrome’s Gemini APIs, I basically learned the entire stack as I built it, and that immersion was the best teacher. What's next for EduAdapt Next we want teachers to define evolving student profiles, saving age, goals, and preferred supports so the extension grows alongside each learner. On the engineering side, we’ll keep shaving latency and exploring new on-device APIs so responses feel instantaneous even on modest hardware. Then, for sure, a structured collaboration with specialist to build it <div