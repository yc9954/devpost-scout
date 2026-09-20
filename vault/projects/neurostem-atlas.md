---
slug: "neurostem-atlas"
url: "https://devpost.com/software/neurostem-atlas"
title: "Neurostem Atlas"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 574
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Neurostem Atlas

> NeuroSTEM Atlas turns your handwritten notes, diagrams, voice explanations, and code into a personalized STEM mastery map with AI‑driven reasoning analysis and adaptive lessons.

[Devpost](https://devpost.com/software/neurostem-atlas) · hackathon [[DSH Hacks V1]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]]
  <sub>weak: video_visual</sub>

**stack** bolt.new

## Body

About the Project What Inspired NeuroSTEM Atlas NeuroSTEM Atlas grew out of a simple observation: real STEM learning is messy. Students sketch diagrams in notebooks, talk through problems out loud, write bits of code, and try to piece together concepts that don’t always click right away. Yet most digital tools only look at final answers, not the thinking behind them. I wanted to build something that respected the way students actually learn — something that could take raw, imperfect work and turn it into clarity. The idea of a multimodal AI tutor that could see, hear, and interpret a student’s reasoning felt both exciting and meaningful. That spark became NeuroSTEM Atlas. How I Built It The project combines several moving parts that work together like a small ecosystem: 🧠 Multimodal AI Pipeline I built a reasoning engine that can analyze: Handwritten math steps Physics diagrams Voice explanations Code snippets The AI reconstructs the student’s reasoning and identifies conceptual gaps. For example, if a student misapplies the chain rule, the system can detect that 𝑓(𝑔(𝑥))≠𝑓′(𝑥)⋅𝑔′(𝑥) and explain the correct form 𝑓′(𝑔(𝑥))⋅𝑔′(𝑥) . 📊 Concept Atlas I designed a dynamic graph where each node represents a STEM concept — like limits, Newton’s laws, or recursion. As the AI analyzes more work, the atlas updates to show strengths, weaknesses, and relationships between ideas. 📚 Adaptive Micro‑Lessons For every conceptual gap, the system generates a personalized micro‑lesson with: Step‑by‑step explanations Visualizations Practice questions Clear, targeted feedback These lessons are built directly from the student’s own work, not generic templates. 🖥️ Full‑Stack Integration I connected everything through a clean, modern interface where students can: Upload multimodal work View reconstructed reasoning Explore their concept atlas Work through guided sessions The goal was to make the experience feel smooth, intuitive, and visually engaging. What I Learned Building NeuroSTEM Atlas taught me a lot — technically and creatively. 🔍 Understanding AI’s Strengths and Limits I learned how multimodal AI models interpret images, audio, and text differently, and how to guide them to produce structured, reliable outputs. 🧩 System Design Connecting the frontend, backend, and AI pipeline helped me understand how complex systems communicate and how to design clean data flows. 🎨 UX for Learning I discovered how important visual clarity is in education. The concept atlas, color coding, and micro‑lesson layout all came from iterating on what makes learning feel intuitive. 📐 STEM Pedagogy I deepened my understanding of how students form misconceptions — and how targeted explanations can help correct them. Challenges I Faced Every part of the project came with its own challenges: 🖼️ Interpreting Handwritten Work Handwriting varies wildly. Getting consistent reasoning reconstruction required careful prompting and fallback logic. 🎧 Audio Reasoning Students explain ideas in different ways. Turning natural speech into structured reasoning was harder than expected. 🕸️ Concept Mapping Designing a concept atlas that felt meaningful — not just decorative — took time. I had to think deeply about how STEM ideas connect. ⚙️ Full‑Stack Coordination Ensuring the frontend, backend, and AI service stayed in sync was a constant balancing act. Despite the challenges, each one pushed the project to become more robust and thoughtful. Final Thoughts NeuroSTEM Atlas is more than a tool — it’s an experiment in what learning can look like when AI doesn’t just grade answers but understands reasoning. Building it taught me how powerful multimodal AI can be when paired with thoughtful design and a genuine desire to help students learn. <div