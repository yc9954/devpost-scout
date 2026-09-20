---
slug: "repend"
url: "https://devpost.com/software/repend"
title: "Repend"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 892
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Repend

> Repend turns any topic into an interactive 2D/3D learning lab where users can predict, experiment, and discover concepts through hands-on simulations instead of passive studying.

[Devpost](https://devpost.com/software/repend) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[web_dom]]

**stack** css, html, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for repend

## Body

Inspiration Learning today is too traditional to the most part, all around us things change but learning and school instruction stay the same with repetitive videos, slides and readings activities. As a teen in school, our team noticed and experienced that we were often understanding concepts better when we stimulated ourselves by experimenting and getting the outcome. Whether it's physics, math, engineering, or abstract ideas, interaction helps develop a deeper understanding rather than memorizing facts that you may forget in the future. For example, if I was taught a math skill and I didn't use it in my career once I grew up, I would most likely forget the skill, however if I use an interactive lab to help me understand the real-world example my mind will remember, yielding a unique result. Essentially, we as a team wanted to make learning feel less like consuming information and overloading your brain to make it more like discovering it. That idea became Repend. What it does Repend turns any topic into a self-contained interactive learning lab. Users add in a concept they want to learn such as the physics of a basketball bouncing, and Repend generates a personalized 2D or 3D experience designed around that topic. The learning flow follows, Predict - Play - Explain, users should hypothesize or commit to an answer or expectation before interacting, they then should understand the live simulation and use it to explain the outcomes and how it reinforced their learning. How we built it We built Repend as an AI-powered educational generation pipeline that transforms a simple text prompt into a complete interactive learning experience. Instead of generating everything in one step, we separated the system into multiple stages to improve reliability, quality, and scalability. Users begin by entering a topic they want to learn. The backend then processes that request through a structured pipeline while streaming progress updates to the frontend using Server-Sent Events (SSE) so users can see generation happen in real time. Concept Reasoning The first stage uses OpenAI to understand the topic and determine how it should be taught. Rather than forcing structured output immediately, this step generates free-form reasoning to: Identify the core concept Determine important variables and relationships Select effective visual metaphors Anticipate misconceptions Design meaningful interactions This reasoning serves as the educational foundation for the rest of the pipeline. Structured Lab Specification Next, a second OpenAI stage converts the reasoning into a validated JSON specification. The specification defines: Interactive variables Learning objectives Prediction prompts Visual structure Simulation behavior User interaction requirements Creating a strict data contract between stages ensures outputs remain modular and independently testable. Interactive Lab Generation Using the validated specification, Gemini generates a fully self-contained interactive HTML learning lab. Each generated lab includes: Interactive controls and sliders Real-time simulation updates Dynamic visualizations Predict - Play - Explain learning flow Reflection questions and explanations The output is designed to function independently without requiring additional assets or external requests. Validation and Repair One of our biggest technical challenges was making generated labs dependable. After generation, each lab is automatically validated against required criteria including: Functional rendering and animation Interactive controls Presence of all learning phases Reflection components Security and structural requirements If validation fails, the system performs a targeted repair pass using the failed checklist before delivering the final result. Streaming, Security, and Performance To improve responsiveness, every pipeline stage streams updates back to the frontend over SSE instead of making users wait for a single final response. Generated labs are rendered inside sandboxed iframes to isolate generated code and protect the host application. For performance optimization, completed labs are cached using Supabase when configured, with an in-memory fallback for local development and repeat requests. By separating reasoning, specification, generation, validation, and delivery into independent modules, Repend is able to generate scalable, interactive educational experiences from a single user prompt. Challenges we ran into One major challenge was making generated labs reliable rather than visually impressive, because the labs had to have relevant content. AI-generated interactive content can break easily as we coded it, so we had unexpected repairs to enforce requirements such as simulation rendering and complete learning phases. Another challenge was maintaining responsiveness while generating multiple stages of output. Streaming pipeline updates helped keep the experience interactive. Accomplishments that we're proud of We are proud that we built an end-to-end AI pipeline that converts topics into educational interactive labs. We are also proud of our predict - play - explain learning framework rather than traditional content generation separating ourselves. We also added validations and repaired our project to improve consistency, and created an engaging user experience and tested it. And we love our 3D landing page. What we learned We learned that educational AI is more than generating answers, it requires structure, feedback loops, and interaction design. We also learned how important strong interfaces between AI stages are for reliability and scalability. What's next for Repend Our next goals are to support richer 3D environments and collaborative labs along with a library, so people don't have to make new labs for existing ideas. We also want to add adaptive difficulty based on performance, build progress tracking and learning paths, expand subject coverage and integrate in classrooms for students to use in the end. Our vision is to make learning feel less like studying and more like experimenting. <div