---
slug: "tracer-2cx0ei"
url: "https://devpost.com/software/tracer-2cx0ei"
title: "Tracer"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 644
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Tracer

> Functional and Visualizer

[Devpost](https://devpost.com/software/tracer-2cx0ei) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** css, fastapi, next.js, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tracer

## Body

Inspiration The inspiration came from my own experience studying Algorithms and Data Structures. Every time I encountered a new algorithm, I had to draw out each step on paper just to understand what was happening to the data. I kept thinking there had to be a better way to visualize this interactively, so I built Tracer to be the tool I wished I had when I was learning. What it does Tracer is an interactive algorithm visualizer that lets students watch algorithms execute one step at a time on custom input data. It covers 12 algorithms across sorting, searching, and data structures. Each step highlights the active elements in the data structure and simultaneously highlights the corresponding line in the pseudocode panel, creating a direct visual connection between the logic and the execution. Users can pause, step forward, step backward, and control playback speed. How we built it The backend is a FastAPI Python service that computes every algorithm step ahead of time and returns a structured list of snapshots, each containing the full state of the data, which indices are active, and which elements were just modified. The frontend is built with Next.js and TypeScript, using CSS Modules for styling. The pseudocode panel maps each step to the correct line using a custom mapping function that reads the step description and phase to determine which line to highlight. The backend is deployed on Render and the frontend on Vercel. Challenges we ran into The biggest challenge came from my original vision for the project. I wanted Claude AI to generate a unique natural language explanation for every single step of every algorithm. I built and shipped this feature and it worked well, but it created two problems. First, with 24 steps in a bubble sort alone, a single run consumed a significant number of API calls. Second, the rate limit kicked in during testing and broke the experience entirely for users who stepped through algorithms quickly. I made the decision to replace the AI explanation layer with a synchronized pseudocode panel instead, which turned out to be a better product decision. It is faster, always accurate, never rate limited, and more directly educational since students can see exactly which line of code produced the visual change they just watched. Accomplishments that we're proud of The pseudocode synchronization is the feature I am most proud of. Getting every step of every algorithm to map correctly to the right pseudocode line required building a custom mapping function that reads the step description, phase, and active indices to determine context. It works seamlessly across all 12 algorithms without any hardcoded step numbers. I am also proud of the data structure renderers — seeing a binary search tree render correctly as a proper tree diagram with nodes and connectors was a satisfying moment. What we learned I learned that product decisions made early in a project can have real consequences later. The AI explanation feature felt like the right call at the start but turned out to be unsustainable at scale. Replacing it with pseudocode was a pain since I already planned and taught me that constraints often lead to better solutions. I also deepened my understanding of FastAPI, Next.js architecture, and how to design a backend that serves structured step data efficiently to a frontend that needs to render it in real time. What's next for Tracer The next step is adding more algorithms, particularly graph algorithms like BFS and DFS which are highly visual and would benefit from this kind of step-by-step treatment. I also want to add a complexity panel that shows the time and space complexity of the current algorithm and explains how it changes at each phase. Longer term, I would like to add a quiz mode where students are shown a step mid-execution and asked to predict what comes next. <div