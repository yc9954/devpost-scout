---
slug: "morph-jcot4m"
url: "https://devpost.com/software/morph-jcot4m"
title: "Morph"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 512
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
---

# Morph

> Vibe CAD to 3D print the solutions to everyday problems in your environment, Tony Stark style, no design experience required.

[Devpost](https://devpost.com/software/morph-jcot4m) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]

**stack** fastapi, javascript, mongodb, next.js, python, snapos, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for morph

## Body

Inspiration We realized that CAD tools suck for creativity. The barrier to entry is high, the tools feel clunky and slow, and working in 2D on a screen limits how naturally people can create in 3D. We wanted to break free of those constraints and make the process as seamless as sketching on paper — but in 3D space, grounded in the real world. What it does Morph lets you design in real life, not on a screen. You can dimension objects in context (e.g., look at your bike, gesture at a gear, and resize it with your voice). You can describe objects verbally, and our system reconstructs them in 3D. Gestures let you select, move, and edit objects naturally in space. Collaboration support means multiple people can build together. Finished models are automatically stored in a frontend STL library , where you can browse all your creations, manage versions, and prep them for printing. It’s like having a live AI design assistant that merges physical context with digital creativity , all the way through to a print-ready workflow . How we built it LLM companion (GPT/OpenAI) to handle live prompting, pick up context, and translate natural language into design instructions. Snap 3D API for generating base objects from prompts. Voice + gesture inputs for hands-free interaction and real-world dimensioning. Trimesh + STL pipeline for mesh processing and file export. Frontend STL browser built with Vite/React to manage models and prep them for 3D printing. MongoDB backend for storing encrypted models, metadata, and embeddings. Built-in pipeline for exporting to 3D printers or integrating with CAD software. Challenges we ran into Translating voice/gesture input into precise 3D edits tied to physical objects. Maintaining real-world scale across the design pipeline. Handling mesh libraries and file compatibility (STL, GLB). Building a frontend file manager that feels intuitive but still supports print-ready detail. Real-time collaboration synchronization. Accomplishments that we're proud of A working pipeline that goes from voice prompt → real-world dimensioning → 3D model → STL export → print-ready library in under a minute. Built an integrated frontend STL browser that makes Morph useful beyond the hackathon demo. Lowered the barrier for 3D design, making it accessible for anyone, not just CAD experts. Proved that physical + digital hybrid design can feel natural and intuitive. What we learned End-to-end usability matters — a frontend file manager turned Morph from a cool demo into a real tool. Context matters: dimensioning in the real world makes design faster and more accurate. AI + 3D workflows can dramatically simplify prototyping when grounded in physical space. How to bridge AI generation with practical outputs that actually print. What's next for Morph Expand the STL library into a shared cloud workspace with search, tagging, and version control. Add real-time multi-user editing in AR/VR spaces. Integrate physics + material simulation so models behave realistically before print. Build out a library of reusable parts for faster prototyping. Long term: make Morph the default way to dimension, design, and manage 3D models end-to-end . Check out what people think of Morph! https://www.youtube.com/watch?v=32oY_iV8jRo <div