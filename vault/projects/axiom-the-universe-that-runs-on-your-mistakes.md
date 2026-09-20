---
slug: "axiom-the-universe-that-runs-on-your-mistakes"
url: "https://devpost.com/software/axiom-the-universe-that-runs-on-your-mistakes"
title: "AXIOM — The Universe That Runs On Your Mistakes"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 814
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# AXIOM — The Universe That Runs On Your Mistakes

> Every AI tutor corrects you. AXIOM makes your physics misconception the LAW of a live universe, running beside a ghost of reality — until your wrong idea visibly breaks. Offline, one HTML file.

[Devpost](https://devpost.com/software/axiom-the-universe-that-runs-on-your-mistakes) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[provenance_signing]] [[retrieval_grounding]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[education]] [[health_clinical]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** anthropic-api, canvas, claude, css3, html5, javascript, localstorage, python, reportlab

## How they structured the write-up

- 💡 inspiration
- ⚛️ what it does
- 🛠️ how we built it
- 🧗 challenges we ran into
- 📚 what we learned
- 🚀 what's next
- ♿ accessibility

## Body

💡 Inspiration Forty years of physics-education research — Halloun & Hestenes' Force Concept Inventory — proved something uncomfortable: students don't fail physics because they know nothing. They fail because they arrive with a coherent wrong physics (Aristotle's "heavier objects fall faster," the medieval impetus theory of projectiles), and being told the correct answer demonstrably does not dislodge it . What works is the predict → observe → explain cycle: commit to a prediction, then confront the evidence. Yet almost every AI education tool ever built does the one thing the research says doesn't work: it corrects the student. So we inverted the pattern. AXIOM doesn't tell you you're wrong — it makes your wrong idea executable, and lets you live in it until it breaks. ⚛️ What it does ⚖️ The Law Forge — Pick a belief card ( "a cannonball flies straight until its force runs out" ) or bend the law sliders directly: mass-dependent gravity \( a = g \cdot m^{\gamma} \), impetus drain, gravity's distance law \( F = GMm/r^{\beta} \), drag. AXIOM compiles your belief into the physics engine. Your misconception is now law . 👻 The Ghost — Every experiment (tower drop, cannon, planetary orbit) runs in two universes simultaneously : yours (solid orange) and reality (dashed teal ghost) — same initial conditions, one shared integrator, two law-sets. A live Reality Divergence meter quantifies how wrong you are, in metres. 🔮 Forced prediction — You cannot press RUN until you commit to a prediction. Predictions are graded against reality — not your universe — and logged forever in an auto-kept Lab Notebook : a measurable record of your intuition improving. 🧠 ECHO, the misconception engine — A fully offline AI layer maps your position in "law space" onto documented historical misconceptions (Aristotelian gravity, Buridan's impetus, non-inverse-square gravity ↔ Bertrand's theorem) and responds only Socratically — questions and evidence, never the answer first. 🤖 Claude deep mode (optional) — Paste an Anthropic API key and ECHO upgrades: it reads your free-text explanations , diagnoses the physical intuition behind your words, and replies with one pointed Socratic question. The app is 100% functional without it. 🛰️ Anomaly Files — The inverse game: five universes where a law is secretly corrupted and the Forge is sealed. You must design experiments, compare against the ghost, and file a diagnosis — i.e., actually do science . This is literally the loop that found Neptune and broke Newton at Mercury. 🛠️ How we built it The entire product is one ~46 KB HTML file — HTML5 Canvas, CSS, and vanilla JavaScript, zero dependencies. One numerical integrator advances both universes each frame with different law parameters, so "your" universe is never a canned animation — it's the same solver with your constants. Orbits use a falloff-normalized central force: $$ a(r) = \frac{GM}{r_0^2}\left(\frac{r_0}{r}\right)^{\beta} $$ so changing \( \beta \) isolates exactly the concept being taught — \( \beta \neq 2 \) produces genuine precessing rosettes (Bertrand's theorem), the same signature that made Mercury famous. The misconception engine is a rule-based diagnostic over law-space backed by a database of misconceptions from the physics-ed literature; the optional Claude integration calls the Anthropic Messages API directly from the browser with a Socratic-only system prompt grounded in the live simulation state. 🧗 Challenges we ran into Making wrong physics behave . Naively changing gravity's exponent changes the force constant's units, so planets just plummeted into the star. Normalizing the force at the starting radius fixed it — now the exponent changes only the falloff , which is the actual concept. Modeling a belief, not an equation. Impetus theory isn't a formula anyone wrote down rigorously — we had to design a law (gravity suppressed while "motion-fuel" remains, then draining) that reproduces the exact flat-then-drop trajectory ~80% of first-year students draw. Keeping the AI Socratic. Both the offline engine and the Claude prompt are hard-constrained to never state the answer first — and in Anomaly mode the diagnosis engine had to be suppressed entirely so it wouldn't leak the case solution. 📚 What we learned That the most powerful thing an AI can do in education is not be right — it's to make the student's wrongness visible and falsifiable . The simulation is the argument; the AI just asks the question that makes the evidence undeniable. 🚀 What's next More misconception domains (circuits: "current gets used up"; thermodynamics: "cold flows"), classroom dashboards built on the Lab Notebook data, and shareable "broken universe" challenge links so students can corrupt a universe for their friends to diagnose. ♿ Accessibility No login, no install, no internet, no data leaves the device. Runs on any school Chromebook or shared phone. Keyboard operable (Space = run, R = reset, 1–3 = scenarios), respects prefers-reduced-motion . The AI core needs no API key — so it reaches exactly the under-resourced classrooms AI ed-tech usually leaves behind. <div