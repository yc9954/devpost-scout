---
slug: "astrosim-ai-interactive-gravity-sandbox-ai-stem-tutor"
url: "https://devpost.com/software/astrosim-ai-interactive-gravity-sandbox-ai-stem-tutor"
title: "AstroSim AI — Interactive Gravity Sandbox & AI STEM Tutor"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 519
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
---

# AstroSim AI — Interactive Gravity Sandbox & AI STEM Tutor

> An interactive 2D gravity simulation sandbox with a real-time math chalkboard and an integrated, voice-narrated AI STEM Tutor to make learning orbital mechanics intuitive and engaging.

[Devpost](https://devpost.com/software/astrosim-ai-interactive-gravity-sandbox-ai-stem-tutor) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[education]] [[scientific_research]]
**user** [[educator_student]]

**stack** css3, gemini-api, github, html5, javascript, mathjax, web-audio-api, web-speech-synthesis

## How they structured the write-up

- 🌌 inspiration
- 🛰️ what it does
- 🛠️ how we built it
- 🚧 challenges we faced
- 🎉 accomplishments we're proud of
- 📚 what we learned
- 🔮 what's next for astrosim ai

## Body

AstroSim AI - Interactive Physics Sandbox & AI STEM Tutor Project Banner Mission Control Onboarding Tour guiding students through the simulator layout Real-time Kepler's Ellipse simulation with active force vectors and math board calculations 🌌 Inspiration Physics education often suffers from a "visualization gap." Abstract formulas like Newton’s Law of Universal Gravitation (\(F_g = G \frac{M_1 \cdot M_2}{r^2}\)) and Kepler's Laws are memorized by students without true physical intuition. We wanted to build a specialized system that bridges this gap—translating static textbook equations into a dynamic, beautiful orbital sandbox where students can experiment, see the math update live at 60 FPS, and learn directly from an AI tutor. 🛰️ What it does AstroSim AI is an interactive gravitational simulation laboratory designed for STEM students. Interactive Gravity Sandbox: Students can click and drag to launch planets, moons, or stars, observing orbit trails and real-time gravity and velocity vector lines. Dynamic Math Blackboard: As planets orbit, this panel calculates and displays formulas with live simulation values dynamically substituted in at 60 FPS. AI Lab Partner (Tutor): A voice-narrated assistant (powered by Google Gemini / local rules) that tracks the sandbox state, explains orbital physics, reacts to collisions, and assigns interactive missions. Accretion & Collisions: Colliding bodies merge using conservation of momentum, generating shockwaves and synthesized audio crunch. Guided Labs: Structured scenarios for Elliptical Orbits, Slingshots, Binary Stars, and Lagrange L1 balance points. 🛠️ How we built it AstroSim AI is built using a zero-dependency vanilla architecture to ensure maximum compatibility and zero load errors: HTML5 Canvas & JavaScript: Powering the custom 60 FPS vector physics engine. CSS Glassmorphism: Creating a futuristic space dashboard layout, fully responsive on mobile/tablets. Web Audio API: Programmatically synthesizing sound waves (whooshes, collision crunches, clicks) using oscillator nodes. Web Speech Synthesis API: Giving the AI assistant a voice to read explanations out loud. MathJax Library: Compiling and rendering gorgeous LaTeX math equations in-browser. Gemini 1.5 Flash API: Enabling dynamic, context-aware AI tutoring responses. 🚧 Challenges we faced Performance Balance: Calculating gravity vectors ($O(N^2)$ complexity) and updating trails at 60 FPS while keeping canvas rendering smooth. We optimized this by caching vector math and using efficient path rendering. Browser Audio Policies: Browsers block text-to-speech before user interaction. We resolved this by building an interactive welcome card so the user activation initializes audio context seamlessly. Responsive Canvas Grid: Making the canvas auto-scale for High-DPI (Retina) screens and collapse vertically on small screens without stretching the rendering coordinate grid. 🎉 Accomplishments we're proud of Creating a fully functional, zero-dependency educational laboratory that runs instantly on any device by double-clicking a single file. Designing a code-based synthesizer to generate sound effects without loading heavy audio assets. Synchronizing live math calculations side-by-side with visual physics. 📚 What we learned We learned advanced techniques in Web Audio synthesis, MathJax LaTeX typography, high-DPI canvas handling, and the pedagogy of making complex STEM subjects engaging for students. 🔮 What's next for AstroSim AI We plan to expand AstroSim AI into a full virtual STEM kit, adding 3D gravity simulations, multiplayer collaborative space rooms, and extending the model to simulate electrostatics and chemistry particle labs. <div