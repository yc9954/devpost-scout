---
slug: "wolframination"
url: "https://devpost.com/software/wolframination"
title: "Wolframination"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 242
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
---

# Wolframination

> Math Visuals Made Simple.

[Devpost](https://devpost.com/software/wolframination) · hackathon [[ShellHacks 2025]]

## Facets

**domain** [[finance_payments]]

**stack** manim, numpy, python, wolfram-technologies, wolframscript

## How they structured the write-up

- inspiration
- what i learned
- how i built it
- challenges i faced

## Body

About the Project Inspiration Math is powerful but often abstract I wanted to make those invisible concepts tangible. By combining the symbolic power of the Wolfram Language with the visual storytelling of Manim , I set out to turn complex integrals into clear, animated experiences. What I Learned How to integrate Wolfram Language into a Python pipeline to compute exact symbolic integrals and generate LaTeX. How to use Manim to render smooth 3D animations of solids of revolution. How symbolic math and visualization can complement each other to deepen understanding. How I Built It Wolfram Language : I wrote WolframScript ( .wls ) files to parse functions, compute symbolic integrals, and determine key values like y_max. Python + Manim : I built a ThreeDScene that takes functions f(x), intervals [a, b], and Wolfram outputs, and then animates the solid of revolution with rotation, slicing, and radius visualization. Integration : A lightweight Python bridge calls Wolfram, retrieves JSON results, and feeds them directly into the Manim scene. Challenges I Faced Bridging two ecosystems : Ensuring Python and Wolfram communicated smoothly via wolframscript and JSON. Dynamic parsing : Handling functions entered in Python syntax (exp(x), sin(x)) and translating them to Wolfram syntax (Exp[x], Sin[x]). Scaling visuals : Automatically computing axis limits and ranges so any function from sin(x) to e^x looks clean in 3D. Time pressure : Balancing learning Wolfram tools, Manim’s API, and hackathon deadlines while still producing a polished final demo. <div