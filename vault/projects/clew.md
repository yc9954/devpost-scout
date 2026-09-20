---
slug: "clew"
url: "https://devpost.com/software/clew"
title: "Clew"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 772
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Clew

> A thread through anything you're learning

[Devpost](https://devpost.com/software/clew) · hackathon [[DSH Hacks V1]]

## Facets

**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** ai, chatgpt, gemini, pydantic, python, sql, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clew

## Body

settings map map map how it works Inspiration Most learning tools still fall into one of two categories: structured roadmaps or AI chat. Roadmaps give direction, but they are static and not personal. Chat gives flexibility, but it quickly becomes messy, forgetful, and hard to follow. We wanted something simpler: a way to see a clear thread through anything you’re learning. Not a course. Not a chat. A path you can actually navigate. That idea became Clew: a personal learning workspace where AI helps turn goals, notes, and messy topic dumps into a structured path you can follow step by step. What it does Clew turns vague learning goals into a visible, interactive roadmap. Instead of hiding everything inside chat, Clew keeps the learning map as the main interface. You can click any topic and immediately see what leads into it and what it unlocks. Users can: generate a learning map from a goal or topic list follow a clear thread through topics and prerequisites expand the map toward a specific target explore what they’re missing and what comes next ask AI for contextual help directly inside the workspace review and accept AI changes instead of applying them blindly roll back changes using snapshots The core idea is simple: AI helps build the path, but the learner stays in control. How we built it We built Clew as a fully working MVP, not just a concept. The stack includes: React + TypeScript + Vite on the frontend FastAPI on the backend SQLite for local persistent state support for OpenAI and Gemini providers structured outputs for safe AI-driven updates We focused on making the map the actual product surface, not just a visualization. The backend handles orchestration, validation of AI proposals, persistence, and study flows. The frontend provides a clean workspace where users can explore, edit, and follow their learning path in a mobile-friendly interface. The system is designed with clear boundaries and can scale beyond a hackathon prototype. Challenges we ran into The hardest part was balancing AI usefulness with user trust. It is easy to let AI freely generate and modify structure, but that quickly becomes unreliable. We wanted a system where AI feels helpful, but not invisible or uncontrollable. That led us to a proposal-based approach, where changes are suggested, reviewed, and reversible instead of silently applied. Another challenge was handling messy input. Users rarely start with perfect plans. They come with vague goals, scattered topics, and uncertainty. Turning that into a clean, useful learning path without overfitting or hallucinating structure was one of the hardest problems. We also ran into a deeper technical challenge around graph reasoning. Compared to tools like Obsidian, where an agent mostly works with isolated notes and links, Clew requires understanding structure: what depends on what, what should come next, and how inserting or modifying a node affects the entire path. These are not simple edits. The model has to reason about ordering, dependencies, and consistency across the graph. Getting this to work reliably was extremely difficult. Earlier models would often produce plausible-looking but structurally incorrect graphs. It took careful schema design, constrained outputs, and extensive iteration on prompts and validation layers to make graph updates stable. In practice, this level of structured reasoning only became consistently reliable with newer generation models, which made designing the right system around them a key challenge of the project. Accomplishments that we're proud of We are proud that Clew feels like a real product, not just a demo. A few things we are especially proud of: the “click a topic, follow the thread” interaction feels intuitive and powerful learning paths are personal and adaptive, not generic AI suggestions are reviewable instead of blindly applied accepted changes are reversible through snapshots the workspace works across desktop and mobile-friendly layouts the architecture is strong enough to grow into a real product What we learned We learned that in learning tools, clarity beats complexity. Users don’t just want answers from AI. They want to understand how topics connect, what matters next, and why. We also learned that the best experience is not full AI automation, but structured collaboration. AI works best when it helps generate and improve the path, while the learner keeps ownership and control. What's next for Clew Our next step is to turn Clew into a fully scalable learning platform with users. We want to improve onboarding and get validation of idea from other learners. The long-term vision is to make learning feel like navigating a system, not searching through content. A clear path. A visible thread. From where you are to what you want to understand. <div