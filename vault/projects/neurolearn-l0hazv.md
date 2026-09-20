---
slug: "neurolearn-l0hazv"
url: "https://devpost.com/software/neurolearn-l0hazv"
title: "NeuroLearn"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 436
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
---

# NeuroLearn

> `1 in 5 students is neurodivergent. NeuroLearn uses AI to instantly adapt any STEM explanation for dyslexia, ADHD, or autism so every brain can actually learn.`

[Devpost](https://devpost.com/software/neurolearn-l0hazv) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
  <sub>weak: web_dom</sub>

**stack** 2.5, css, flash, gemini, html, javascript, node.js, vercel

## How they structured the write-up

- the problem: stem wasn't built for every brain
- what we built
- how we built it
- what makes it different
- challenges
- what we learned
- what is next

## Body

The Problem: STEM Wasn't Built for Every Brain 1 in 5 students is neurodivergent. Yet most STEM resources are written for one type of learner: neurotypical, text-heavy, and linear. For students with dyslexia, dense paragraphs become walls of unreadable text. For students with ADHD, long explanations lose them before they reach the point. For autistic students, vague metaphors create more confusion than clarity. Brilliant minds opt out of STEM, not because they cannot understand it, but because STEM was never explained their way. What We Built NeuroLearn is an AI-powered web app that adapts any STEM explanation to match how your brain actually works. Pick your profile. Type any topic. Get an explanation built for you. 📖 Dyslexia-Friendly: Short sentences, highlighted keywords, generous spacing ⚡ ADHD-Friendly: Key point first, numbered chunks, zero filler 🔬 Autism-Friendly: Literal structure: IS / DOES / WHY After every explanation, a 4-option comprehension quiz reinforces the concept with instant feedback. How We Built It The frontend is intentionally vanilla: no frameworks, no build steps, fast and accessible. A Vercel serverless function acts as a secure API proxy to Gemini 2.5 Flash, keeping the API key server-side and solving CORS entirely. Each profile has a carefully engineered system prompt that constrains Gemini's output to structured JSON with two fields: explanation and quiz. A custom parseJSON() function handles edge cases in model output gracefully. What Makes It Different Most AI education tools give everyone the same explanation. NeuroLearn starts from the premise that the explanation itself needs to change, not just the font size. The three profiles produce structurally different outputs. Dyslexia mode surfaces key terms for visual anchoring. ADHD mode front-loads the takeaway before attention drifts. Autism mode strips ambiguity using a strict IS / DOES / WHY scaffold. Challenges Getting Gemini to return clean, parseable JSON consistently required significant prompt iteration. Profile authenticity also took research: dyslexia design follows British Dyslexia Association guidelines, ADHD patterns draw on cognitive load research, and autism-friendly structure uses literal language principles. We also chose deliberately to do three profiles well rather than five profiles adequately. What We Learned Building NeuroLearn showed us how much educational content implicitly assumes a neurotypical reader. Every word in a system prompt matters when the goal is genuine cognitive adaptation, not just surface-level styling. Accessibility in STEM is not a niche problem. It is a systemic one, and AI is one of the few tools flexible enough to address it at scale. What Is Next More profiles: dyscalculia, ELL students, gifted learners Subject-specific modes: lab reports, proofs, word problems Voice input and text-to-speech output Progress tracking and spaced repetition <div