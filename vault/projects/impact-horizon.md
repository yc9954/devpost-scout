---
slug: "impact-horizon"
url: "https://devpost.com/software/impact-horizon"
title: "Impact Horizon"
hackathon: "Hacktivism II"
organization: "Politechs"
winner: true
words: 410
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/education"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# Impact Horizon

> Step into the policymaker’s seat and experience the consequences of your climate decisions in real time.

[Devpost](https://devpost.com/software/impact-horizon) · hackathon [[Hacktivism II]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[climate_energy]] [[education]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]]

**stack** javascript, json, next, openai, postcss, react, tailwind, vercel

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments
- what i learned
- what's next for impact horizon

## Body

Inspiration Climate policy is often presented in ways that feel abstract, disconnected, or oversimplified. I realized that future leaders need more than just numbers and projections: they need interactive experiences that expose them to the trade-offs, constraints, and real-world consequences of policy decisions. Most climate education focuses on awareness alone, leaving students unprepared for the complexities of civic decision-making. What it does Impact Horizon is an interactive web platform where users explore policy trade-offs through scenario-based simulations. Instead of passively reading about climate facts, users step into the shoes of decision-makers, navigating the consequences of different policies. The platform dynamically shows how choices impact jobs, emissions, energy demand, and community well-being, helping users understand the interconnected systems that underpin sustainable development and civic planning. How I built it The frontend is built in React + Next.js , delivering a fast, modular interface. A dashboard summarizes scenarios, while dynamic pages display detailed outcomes with charts and metrics. The backend integrates API endpoints for embeddings and reasoning models that generate scenario narratives and evaluate trade-offs. Similar policy contexts are grouped via the embeddings pipeline, while GPT-4o-mini provides contextualized feedback and stakeholder responses. I used TailwindCSS for rapid, clean styling, creating a structure that is scalable and ready for future AI-driven recommendations. Challenges I ran into Designing data structures so that scenarios are dynamic and comparable, not static case studies. Correctly integrating the embeddings API, overcoming multiple formatting issues. Balancing technical development with storytelling and educational clarity. Achieving a clean, intuitive UI despite limited design experience. Accomplishments Delivered a working prototype combining interactive design, AI integration, and civic education. Built a scalable, intuitive architecture ready for expansion. Translated abstract civic and climate challenges into a tangible, engaging platform. Successfully implemented OpenAI API without hardcoding responses for the MVP. What I learned AI reasoning can make complex policy trade-offs understandable. User experience is critical in educational tools; clarity can make tough concepts approachable. Simplification without losing rigor is the hardest part of civic and climate education. Deepened technical skills in React, Next.js, API integration , and balancing narrative with technical clarity. What's next for Impact Horizon Expand scenario libraries to include global civic and climate contexts. Add multiplayer or classroom modes for collaborative decision-making. Integrate real datasets from sources like IPCC and IEA for scenario accuracy. Explore deeper AI integration for adaptive feedback, making the platform both a simulator and tutor. Enhance engagement with visual characters and dynamic, interactive consequences beyond text-based simulations. <div