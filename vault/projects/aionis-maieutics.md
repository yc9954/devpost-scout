---
slug: "aionis-maieutics"
url: "https://devpost.com/software/aionis-maieutics"
title: "AIONIS Maieutics"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 520
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/climate_energy"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/geospatial"
---

# AIONIS Maieutics

> Every AI tutor hands you the answer. AIONIS Maieutics never does. It guides you to rebuild any STEM concept from first principles, until you reconstruct it yourself.

[Devpost](https://devpost.com/software/aionis-maieutics) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]] [[vision_ocr]]
**domain** [[accessibility]] [[climate_energy]] [[education]] [[health_clinical]] [[transportation]]
**user** [[educator_student]] [[patient_family]]
**substrate** [[geospatial]]

**stack** anthropic, claude, next.js, openrouter, railway, react, react-flow, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aionis maieutics

## Body

Inspiration Every AI tutor I tried did the same thing: I asked, it answered. I felt smart for a second and forgot everything by the next day. The problem isn't that students lack access to answers, it's that being handed one skips the only part that actually builds understanding: reconstructing the idea yourself. I wanted a tutor that refuses to do that work for you. What it does AIONIS Maieutics is a Socratic tutor that never gives you the answer . You pick a STEM concept, and it guides you with questions only, until you rebuild the concept from first principles in your own words. As you reconstruct each piece, a concept graph lights up node by node next to the conversation. If you contradict a foundation you already built, that piece is gently flagged so you can revisit it, never punished. The engine is topic-blind : the same code guides you through gas pressure, gradient descent, predator-prey cycles, and Braess's paradox. How we built it Next.js , with the engine running entirely server-side behind route handlers, so the answer key never reaches the browser. The core is a topic-blind state machine over a concept dependency graph, with a single structured LLM call per turn that classifies whether you rebuilt the mechanism, guessed, or broke a prerequisite. Claude Sonnet runs the evaluation, with dual-provider failover so a live demo never dies mid-session. The graph view uses React Flow , deployed on Railway . Challenges we ran into The hardest part wasn't the code, it was the feel . My first version was technically correct but pedantic: it took six turns to accept a right answer, and it kept dragging me back to steps I'd already mastered. I literally typed "I ALREADY TOLD YOU" three times during a test. Fixing that without breaking the soul, the refusal to ever hand over the answer, was the real work: lowering the bar to accept a clear mechanism even when poorly worded, while still rejecting bare term-naming, plus an iron rule to never retreat to an already-rebuilt node. Accomplishments that we're proud of That the engine is genuinely topic-blind, proven not claimed : the exact same code reconstructs physics, machine learning, and ecology with zero changes. And that the same structural primitives, like FEEDBACK and EMERGENCE , reappear across unrelated domains, the seed of seeing the world's structure as a shared language. What we learned That a good Socratic tutor is patient, not stubborn . Refusing to give the answer isn't the same as leaving someone stuck against a wall. The whole craft was teaching it to lower the difficulty step by step until it finds a foothold you can climb, without ever revealing the destination. What's next for AIONIS Maieutics Right now AIONIS teaches each concept as a specific instance. The real vision is the abstract pattern beneath it : Braess's paradox isn't only about traffic, it's a mechanism that reappears in power grids and markets. The next step is a tutor that shows you the pattern itself, crossing domains, turning the structure of the world into a language you can read. <div