---
slug: "conjure-ai-5vcgu4"
url: "https://devpost.com/software/conjure-ai-5vcgu4"
title: "Conjure AI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 413
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/formal_verification"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "user/educator_student"
---

# Conjure AI

> Ask "what happens when a cricketer hits a six?" and Conjure turns it into a live simulation you can play with. Any science or math question becomes hands-on intuition, free, in your browser.

[Devpost](https://devpost.com/software/conjure-ai-5vcgu4) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[formal_verification]] [[simulation_digital_twin]]
**domain** [[education]]
**user** [[educator_student]]

**stack** caching, gpt-4o-mini, html5, openai, playwright, survey, typescript, vercel, vite, zod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for conjure ai

## Body

Oscillation | Admin Basketball Arc Human Speech Guitar String Binary Search Sine Wave | Admin Inspiration Textbooks and videos are passive. You read that a pendulum's period depends on its length, but you never feel it. We wanted any student to be able to ask a question in plain words and immediately get something they can poke at and explore. What it does Conjure turns any science or math question into a live, interactive simulation. Type "what happens when a cricketer hits a six?" and you get a real projectile-motion simulator with sliders for speed, angle, and gravity, a live graph, a plain-language explanation, and a quick quiz. It covers physics, math, and CS through eight simulation types: oscillation, projectile motion, circuits, waves, function plotting, binary search, the normal distribution & vector addition. How we built it The key design choice: the AI never writes fragile simulation code. It reads your question and returns a small, structured JSON "spec" that picks one of several hand-built, physically-correct simulation primitives and fills in its parameters. The browser then runs the real math at 60fps. Every spec is validated, auto-repaired if the model returns something off, and falls back gracefully so the app never crashes on bad input. Results are cached, so it is fast and costs almost nothing. There is also a Studio page where educators can tune any sim and share it as a link, no code needed. Challenges we ran into Reliability. An open-ended "AI makes a simulation" demo breaks on stage. We solved it with the spec-plus-primitives architecture and a validate → repair → fallback pipeline, and we hardened it with adversarial testing that caught real bugs (NaN and Infinity slipping past validation, a corrupt-cache crash, an XSS in shareable links). The physics is unit-tested so the formulas are provably correct. Accomplishments that we're proud of A genuinely reliable AI product: the AI gives you "any question," the tested primitives give you "never breaks." It runs free in any browser, works on mobile, and a shared link opens straight to a customized sim with no account. What we learned Constraining the AI to a structured output over a trusted engine beats letting it free-form. The hard part of an AI product is not the model call, it is everything around it: validation, repair, caching, and failure handling. What's next for Conjure AI More simulation primitives (chemistry, geometry), an in-browser model so it works with no API key, and richer educator tools. <div