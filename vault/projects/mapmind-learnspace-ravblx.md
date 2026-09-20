---
slug: "mapmind-learnspace-ravblx"
url: "https://devpost.com/software/mapmind-learnspace-ravblx"
title: "Mapmind Learnspace"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 733
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Mapmind Learnspace

> MapMind turns messy topics into a structured learning path you can actually follow. Fully opensource & web native

[Devpost](https://devpost.com/software/mapmind-learnspace-ravblx) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** ai, python, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mapmind learnspace

## Body

showoff 1 showoff 2 showoff 3 agentic pipeline real ops panel for production real ops panel for production real ops panel for production real ops panel for production Inspiration Most learning tools still fall into one of two categories: rigid courses or AI chatboxes. Courses give structure, but they are static. Chat gives flexibility, but it quickly becomes messy, forgetful, and hard to trust. We wanted to build something closer to “Obsidian for learners” but much more approachable for people who are not trying to become power users of a note-taking system. With just a few clicks, you can clearly see the structure of a subject, how topics connect, what depends on what, and where to go next. That idea became MapMind Learnspace : a graph-first agentic workspace where AI helps learners turn goals and messy topic dumps into a clear, reviewable knowledge path. What it does MapMind turns vague learning goals into a visual path with prerequisites, next steps, and reinforcement. Instead of hiding everything inside chat, MapMind keeps the knowledge graph as the main interface. Users can: turn rough topic lists into a connected learning graph expand a graph toward a specific goal explore prerequisites and weak points visually ask the AI for contextual help inside the workspace use quizzes and topic closure loops to reinforce understanding The core product idea is simple: AI should help build and improve the map, but the learner should always stay in control. Changes are proposed, reviewed, and reversible. How we built it We built MapMind as a fully working MVP , not just a concept demo. The product combines: React + TypeScript + Vite on the frontend FastAPI on the backend SQLite for local durable workspace state support for OpenAI and Gemini providers typed contracts for safe graph proposals and structured AI flows We focused on making the graph the actual product surface, not a decorative visualization. The backend handles orchestration, proposal validation, persistence, snapshots, and study flows, while the frontend gives a clear workspace experience that also works in a mobile-friendly format . We also designed it with scalability in mind: the system is already structured as a real product foundation, with clean API boundaries, provider abstraction, and an architecture that can grow beyond a hackathon prototype. Challenges we ran into The hardest part was balancing AI usefulness with user trust. It is easy to make an “AI learning tool” that looks magical but silently mutates information or invents structure. We wanted the opposite: a system that feels smart, but stays legible. That meant designing proposal-based graph edits, validation steps, and reversible snapshots instead of letting the model act like an unchecked black box. Another challenge was handling messy inputs. Real learners rarely start with perfect curricula. They start with vague goals, half-formed topic lists, and uncertainty. Turning that into a clean dependency graph without fake precision was one of the toughest parts of the build. Accomplishments that we're proud of We are proud that MapMind already feels like a real product, not just a hackathon mockup. A few things we are especially proud of: the graph-first UX makes complex subjects feel immediately more understandable the Obsidian-like knowledge model is much more user-friendly for learners AI suggestions are reviewable instead of silently applied accepted changes are reversible through snapshots the MVP is already usable across desktop and mobile-friendly layouts the architecture is strong enough to scale into a real startup product What we learned We learned that in education, clarity beats magic . Users do not just want an answer from AI. They want to understand the structure behind what they are learning, see their path, and trust that the system is not making invisible decisions for them. We also learned that graph-based learning is much more powerful when paired with controlled AI. The best experience was not “full autonomy,” but structured assistance: AI helps generate, expand, and explain, while the learner keeps ownership of the map. What's next for MapMind Learnspace Our next step is to turn MapMind from a strong MVP into a full startup-ready learning platform. We want to improve onboarding, strengthen prerequisite inference, expand study and mastery loops, and make collaboration easier for mentors, teams, and learning communities. The long-term vision is to make learning feel more like navigating a living knowledge system: visual, structured, adaptive, and actually owned by the user instead of buried in chat history. <div