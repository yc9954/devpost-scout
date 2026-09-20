---
slug: "de-3vjpt4"
url: "https://devpost.com/software/de-3vjpt4"
title: "STEMViz"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 457
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/runtime_tool_creation"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "user/educator_student"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
---

# STEMViz

> Visualize the formulas: AI-generated interactive sandboxes designed to repair student misconceptions

[Devpost](https://devpost.com/software/de-3vjpt4) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]] [[runtime_tool_creation]] [[simulation_digital_twin]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[genomic_bio]] [[geospatial]]

**stack** canvas-api, css3, docker, fastapi, google-cloud-run, html5, hugging-face-api, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stemviz

## Body

Inspiration In STEM education, students are often taught "formula-first". They are forced to memorize equations before they understand the underlying physical behavior: Kinetic equations of projectile motion: $$y(t) = y_0 + (v_0\sin\theta)t - \frac{1}{2}gt^2$$ Ohm's law: $$I = \frac{V}{R}$$ Slope-intercept line coordinates: $$y = mx + b$$ For visual or hands-on learners, this abstract presentation is a major barrier. I wanted to build STEMViz: a tool that does not simply output static chatbot text, but instead creates a dynamic visual sandbox where students can isolate variables, see parameters move, and construct an intuitive mental model. What it does STEMViz builds personalized micro-learning labs matching a student's exact confusion: Student Setup: The student specifies their topic, grade band, and confusion (e.g., "I mix up velocity, acceleration, and gravity."). AI Lesson Plan: The app dynamically generates a learning goal, highlights the core misconception, and designs a 3-step experiment. Interactive Simulation: An interactive canvas-based sandbox updates instantly as students move physical sliders (e.g., launch speed, angle, resistance, intercept). Targeted Misconception Check: The student is asked a conceptual question, inputs their explanation, and receives short, constructive tutoring feedback to repair their understanding. How we built it Frontend: Built with vanilla HTML5, CSS3, and JavaScript, leveraging for high-performance physics and coordinate math rendering. For projectile motion, the system calculates the path using: $$R = \frac{v_0^2 \sin(2\theta)}{g} \quad \text{and} \quad H = \frac{v_0^2 \sin^2\theta}{2g}$$ Backend: Built with FastAPI (Python 3.11). AI Engine: Integrated via the Hugging Face Inference client for inferencing LLMs to dynamically generate targeted JSON lesson schemas and evaluate explanations. Deterministic Fallback: Features pre-defined template routers to keep the app fully functional in offline or credential-less judging environments. Deployment: Containerized with Docker and deployed serverless to Google Cloud Run. Challenges we ran into Aligning LLM outputs with interactive simulations. If the AI suggests a concept the simulation cannot draw, the learning loop breaks. We solved this by parsing responses using structured JSON templates and routing the topic key to dedicated sandbox components (Ohm's Law circuit meter, Projectile motion physics engine, Linear equations coordinate graph). Accomplishments that we're proud of Developing a zero-latency canvas simulation that responds instantly to sliders. Implementing a reliable local fallback system that guarantees the app works during offline judging. Designing a sleek, premium dark-themed user interface centered around student interaction. What we learned We learned that visual anchors are crucial for educational AI. Chatbots alone are insufficient. When LLM prompts are connected to physical sliders, students learn the actual relationships, not just strings of text. What's next for STEMViz Expanding Libraries: Add chemistry molecule balancing and biology cell osmosis/diffusion simulations. Teacher Mode: Allow teachers to configure specific sandboxes, monitor common classroom misconceptions, and assign tasks. State Persistence: Add student profiles to track conceptual progression over time. <div