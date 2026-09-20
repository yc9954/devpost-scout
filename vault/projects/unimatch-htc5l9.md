---
slug: "unimatch-htc5l9"
url: "https://devpost.com/software/unimatch-htc5l9"
title: "UniMatch"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 351
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/web_dom"
---

# UniMatch

> Discover the Magic Behind Global UniMatch

[Devpost](https://devpost.com/software/unimatch-htc5l9) · hackathon [[Student HackPad 2025]]

## Facets

  <sub>weak: education, labor_employment, supply_logistics</sub>
  <sub>weak: educator_student, researcher</sub>
**substrate** [[web_dom]]
  <sub>weak: document_pdf, geospatial, structured_db</sub>

**stack** copilot, gemini, html, javascript, json, visual-studio

## Body

Global UniMatch is a festive, static‑export Next.js (App Router) application that helps students quickly discover suitable universities across multiple countries. The user starts with a short quiz: selecting academic interests (IT/Computer Science, Engineering, Business, Medicine, Design/Arts, Data/AI), budget band, preferred study format, and English level. These answers are stored in a lightweight React context (QuizContext). When the user opens the Results page, the app computes two sets of recommendations: (1) focused matches filtered by the chosen country and a “one top pick per country” list to guarantee global diversity. Under the hood each university record contains standardized numeric scores, tuition ranges, ranking info, and a match reason text. The ranking function combines interest alignment (matching selected categories to the university’s strength scores), a budget compatibility factor (penalizing tuition outside the chosen band), and a global reputation component. A fallback ensures at least one representative from each dataset even if initial filters are strict. The radar chart visualizes alignment: blue polygon = user interests; gold polygon = normalized scores of the top university across the main axes. To boost shareability, a client‑side canvas generator creates a branded PNG “share card” (title, tagline, decorative snow, and summary) without any server rendering. Users can download and post it instantly. The site ships as a Progressive Web App: manifest.json plus a simple service worker pre‑caches core assets, enabling offline revisits and an install prompt. Static export keeps deployment ultra fast on Cloudflare Pages; custom _headers enforce no-cache for HTML so new versions appear immediately while hashed assets remain long‑cached for performance. The visual layer blends themed animations (multi‑speed snowfall, aurora glow, starfield, neon sinusoidal garland) with glassmorphism panels for readability. Accessibility and performance are considered: animations respect prefers-reduced-motion, component sizes are lean, and bundle splitting reduces initial JavaScript. Overall, UniMatch transforms a complex, multi‑variable decision into an engaging, data‑driven, festive experience that is fast to load, easy to share, and simple to extend (future ideas: interactive world map, achievements, multi-language, AI Q&A, PDF report export). I used Copilot for writing 90% of Code and Gemini for creating a full plan of creating web site. <div