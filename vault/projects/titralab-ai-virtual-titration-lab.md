---
slug: "titralab-ai-virtual-titration-lab"
url: "https://devpost.com/software/titralab-ai-virtual-titration-lab"
title: "TitraLab - AI Virtual Titration Lab"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 708
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
---

# TitraLab - AI Virtual Titration Lab

> Do a real acid-base titration in your browser - no lab needed. A live AI teacher guides each step, then auto-writes the graded lab report. Hands-on STEM for students who have no equipment

[Devpost](https://devpost.com/software/titralab-ai-virtual-titration-lab) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[simulation_digital_twin]]
  <sub>weak: realtime_stream</sub>
**domain** [[education]] [[scientific_research]]
**user** [[educator_student]]

**stack** css3, groq, html5, javascript, llama-3.3-70b, react, render, svg, tailwind-css, vite

## How they structured the write-up

- inspiration
- what it does
- the chemistry is real
- how i built it
- challenges i ran into
- what i learned
- what's next

## Body

TitraLab – AI-Powered Virtual Acid–Base Titration Lab Learn the complete titration process with real-time guidance from Aria, the AI Chemistry Teacher. Perform a virtual acid–base titration by adding NaOH to an unknown HCl solution while following guided instructions. Observe the chemically accurate phenolphthalein endpoint as the solution turns pink. Instantly generate a complete laboratory report based on the student's actual experiment data. Inspiration In thousands of under-resourced and rural schools, students are graded on a chemistry practical record — a written report of experiments like titration. The catch? Many have never touched a burette. With no lab, no chemicals, and no equipment, the "experiment" becomes an exercise in copying results they don't understand. I wanted to give those students the real thing: a way to actually perform a titration, understand every step, and produce the report they're graded on — using nothing but a browser. What it does TitraLab is a virtual acid–base titration lab with a live AI teacher. Do the experiment — dispense standard 0.100 M NaOH from a burette into a flask of unknown HCl with phenolphthalein indicator. It stays colourless, then snaps to bright pink at the endpoint. Learn it live — "Aria," an AI lab partner, reacts to every action with short, encouraging guidance. A guided Lesson Mode teaches the whole experiment step by step: theory, apparatus, procedure, the graph, and the maths. See the science — a live pH-vs-volume curve is plotted as you titrate, showing the steep jump to pH 7 at the equivalence point. Get the report — one click auto-generates the full graded lab report (Aim → Result) using your actual run numbers, ready to copy. The chemistry is real Standard 0.100 M NaOH is titrated into 10.0 mL of unknown HCl. The endpoint lands at 10.0 mL, and the report solves for the unknown with the titration formula: $$ M_1 V_1 = M_2 V_2 \quad\Rightarrow\quad M_2 = \frac{M_1 V_1}{V_2} = \frac{0.100 \times 10.0}{10.0} = 0.100\ \text{M} $$ That's about the strength of human stomach acid. The pH model is physically correct: 2 at the start, exactly 7 at equivalence (right for a strong acid–strong base), rising past 11 when over-titrated. How I built it 1.Frontend: Vite + React + Tailwind CSS — a single-page app with all state in React. The burette and flask are hand-drawn SVG, with the flask colour driven by a smooth colourless → pink interpolation keyed to titration progress. 2.Simulation: a pure, AI-free module handles the moles math, endpoint, pH curve, and colour — so the experiment works perfectly even with no internet. 3.AI:three calls to Groq(Llama 3.3 70B) power the live lab partner, the guided lesson, and the structured lab report (JSON mode). Each shows an instant local message first, then upgrades it with AI. 4.Deployment: static build deployed on Render . Challenges I ran into Getting the chemistry right. My first design had acid going into base and "turning pink" — but phenolphthalein is pink in base, colourless in acid . I flipped it to the textbook setup (standard NaOH into unknown HCl) so the dramatic pink endpoint is also chemically correct . A demo that never breaks. Judging Wi-Fi is unreliable, so I made the whole app AI-optional : if Groq fails or there's no key, the simulation, curve, lesson, and a deterministic local report all still work. The AI only ever enhances . Trustworthy numbers.** The report must use the student's real reading, never a placeholder — so every number is computed in JS, handed to the model, and validated, with a locally-built report as fallback. Floating-point drift occasionally made the endpoint miss 10.0 mL; rounding the volume fixed it. What I learned How to make an LLM dependable in a live demo by treating it as an enhancement layer over a deterministic core. Real chemistry rigor — why phenolphthalein works for strong–strong titrations even though it changes colour around pH 8. Prompt + JSON-mode design for structured, factual AI output. End-to-end shipping: Vite build → GitHub → Render deploy. What's next Support a wider range of chemistry experiments and laboratory simulations. Provide every student with access to high-quality practical science education, regardless of their location or available resources. Fill bridge the gap between theoretical learning and practical experimentation. <div