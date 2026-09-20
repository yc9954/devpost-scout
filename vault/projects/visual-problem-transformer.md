---
slug: "visual-problem-transformer"
url: "https://devpost.com/software/visual-problem-transformer"
title: "Visual Problem Transformer"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 486
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/education"
  - "user/educator_student"
---

# Visual Problem Transformer

> Transforming STEM problems into visual reasoning.

[Devpost](https://devpost.com/software/visual-problem-transformer) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[education]]
**user** [[educator_student]]
  <sub>weak: web_dom</sub>

**stack** canvas, client-side, css, design, html, html5, javascript, language, math.js, mathematics, natural, nerdamer, parsing, responsive

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for visual problem transformer

## Body

Simple explanation feature View of User Input and Solution AI Reasoning Pathway Steps for User to understand Inspiration Many students can follow the steps needed to solve STEM problems, but often struggle to understand why those steps work. Existing homework tools typically provide answers instantly, which can encourage memorization rather than genuine understanding. We wanted to create a system that makes problem-solving more transparent. Instead of functioning as another answer generator, Visual Problem Transformer helps learners visualize the reasoning process behind a solution by transforming STEM problems into structured reasoning pathways, symbolic solutions, and visual graphs. Our goal was to bridge the gap between solving a problem and understanding it. What it does Visual Problem Transformer converts natural-language STEM problems into interactive visual reasoning structures. The application: Classifies the problem domain (Algebra, Calculus, Physics, Geometry, Statistics, Energy, Circuits, and more) Extracts important variables and quantities automatically Generates step-by-step reasoning pathways Solves algebraic equations symbolically Computes symbolic derivatives for calculus problems Calculates physics-based solutions for supported mechanics scenarios Displays confidence scores for generated solutions Builds visual reasoning graphs that show how information flows from inputs to final answers Rather than presenting only an answer, the platform shows the logic behind the solution. How we built it The application follows a reasoning pipeline: Problem Input ↓ Domain Classification ↓ Variable Extraction ↓ Symbolic/Numerical Solver ↓ Reasoning Path Generator ↓ Visual Reasoning Graph ↓ Final Explanation For algebra and calculus problems, Nerdamer performs symbolic computation directly in the browser. For physics problems, the system applies deterministic mechanics equations such as: $$ F = ma $$ and $$ a = g\sin(\theta)-\mu g\cos(\theta) $$ to generate solutions and explanations. The visualization engine then converts the reasoning process into graph structures displayed on a dynamic canvas. Challenges we ran into One of our biggest challenges was avoiding the temptation to build a "fake AI." Early versions attempted to generate answers for every STEM problem, but we quickly realized that providing unreliable solutions would undermine the educational value of the platform. Instead, we redesigned the system around transparency and confidence scoring. Accomplishments that we're proud of We're proud that we built a tool that doesn't just provide answers but helps students understand the reasoning behind them. Turning complex STEM problems into visual learning experiences made us realize how powerful technology can be when it's designed to teach rather than simply solve. What we learned We learned that educational technology is most effective when it focuses on explaining reasoning rather than simply providing answers. Throughout development, we gained experience in symbolic mathematics, visualization, and designing systems that make complex STEM concepts more intuitive and accessible. What's next for Visual Problem Transformer Next, we plan to expand Visual Problem Transformer with support for additional STEM domains, richer visualizations, and more advanced symbolic reasoning capabilities. Our long-term vision is to create a platform that helps students build deep conceptual understanding by making STEM thinking visible. <div