---
slug: "unsent-o2xqkj"
url: "https://devpost.com/software/unsent-o2xqkj"
title: "UNSENT"
hackathon: "United Hacks V6"
organization: "Hack United"
winner: true
words: 485
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/security_privacy"
  - "substrate/geospatial"
---

# UNSENT

> What if every unsent message became a star? UNSENT maps anonymous emotion into a constellation. When two strangers resonate, they share an Ephemeral Knot, then vanish. No trace.

[Devpost](https://devpost.com/software/unsent-o2xqkj) · hackathon [[United Hacks V6]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[security_privacy]]
**substrate** [[geospatial]]

**stack** api, flask, github, html5, javascript, natural-language-processing, next.js, python, render, socket.io, supabase, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for unsent

## Body

First Hi Reply Enter the Unsent Message Enter Message Find Through Emotions Connection Request Front Page Inspiration In a world that never forgets, we are constantly curating ourselves. Social platforms reward performance, polish, and permanence, leaving little space for the raw things we never said, the apology we delayed, the goodbye we avoided, the gratitude we assumed was understood. We were inspired by the quiet weight of these unsent messages and a simple question: What if vulnerability didn’t disappear into silence, but instead found resonance? UNSENT was born from the belief that emotion is universal, and that even anonymous, fleeting connections can be deeply human and meaningful. What it does UNSENT is a global, anonymous constellation of unspoken messages. Users write an unsent message, which becomes a star on a living star map. Each star’s color reflects its AI-detected emotion, and its brightness grows as others click “I feel this too.” When two strangers resonate with the same feeling, they can enter an Ephemeral Knot, a private, real-time space to chat and draw together anonymously for a limited time. When the session ends, everything vanishes. No history. No trace. Just a moment of shared humanity. How we built it We built UNSENT as a production-ready, global MVP in 24 hours. The frontend uses Next.js with a canvas-based star map to visualize emotion at scale. The backend is powered by Flask, handling text sanitization, sentiment-to-emotion classification, language detection, and translation. Supabase stores anonymous stars efficiently, while Socket.io enables real-time Ephemeral Knot sessions. The system was deployed early and iterated safely using feature branches, continuous deployment, and strict checkpoints. Challenges we ran into Designing something emotionally safe yet technically scalable was the hardest challenge. We had to balance anonymity with abuse prevention, real-time interaction with reliability, and global access with low latency. Rendering thousands of stars efficiently while keeping interactions smooth required careful optimization. Another challenge was deciding what not to store; embracing ephemerality goes against most conventional app design. Accomplishments that we're proud of Shipping a fully deployed, end-to-end product in 24 hours Creating a unique constellation-based UI instead of a traditional feed Enabling real-time, anonymous human connection without permanence Building a clean GitHub history with production-safe deployments What we learned We learned that constraint fuels clarity. Time limits, ephemerality, and anonymity didn’t reduce connection; they deepened it. Technically, we strengthened our skills in real-time systems, NLP pipelines, and deployment discipline. More importantly, we learned that software can be quiet, gentle, and human, and still be powerful. What's next for UNSENT Next, we plan to expand the Ephemeral Knot into generative art by producing a final SVG that visually represents each shared moment. We also want to improve emotion modeling, add better moderation tools, and explore global emotion trends over time, without ever compromising anonymity. UNSENT will remain what it was meant to be: a place where feelings exist just long enough to be felt. <div