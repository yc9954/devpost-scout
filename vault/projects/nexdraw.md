---
slug: "nexdraw"
url: "https://devpost.com/software/nexdraw"
title: "nexdraw"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 389
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "user/developer"
  - "substrate/video_visual"
---

# nexdraw

> cursor for artists

[Devpost](https://devpost.com/software/nexdraw) · hackathon [[NexHacks]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** bun, gemini, next.js, react, shadcn, supabase, tailwind, tldraw, typescript

## How they structured the write-up

- the mission
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nexdraw

## Body

cool collaborative drawing i made with nexdraw tech stack The Mission I wanted to challenge the narrative that AI will take over artists' jobs. We like AI when it's an enhancement tool, but don't necessarily want it to take our jobs. Much like how Cursor hasn't quite replaced programmers, but has become a staple in the software development community by improving engineers' workflows significantly. I built Nexdraw as that challenge; the "Artist's Cursor," if you will. What it does You draw it. Nexdraw refines it. With Nano Banana Pro and the ability to reason across several image layers, Nexdraw autocompletes your masterpieces. Nexdraw comes with both a familiar chat interface and an autocomplete system. You can either be a meticulous prompter, or a hands-free artist. How we built it Nexdraw is powered by Next.js 16 and a customized tldraw engine. At its core, I engineered a bespoke Layer Management System that uses tldraw’s side-effect engine to intercept and "tag" every shape into a centralized metadata registry. This allows the system to bind AI contributions to specific layers, giving artists the ability to toggle, reorder, or trash AI work with granular control, ensuring the "Cursor" never disturbs the artist's manual sketches. The project’s intelligence comes from Google Gemini, which handles multimodal vision tasks by analyzing high-fidelity snapshots of the canvas. I built a custom pipeline that re-projects AI-generated assets back into the canvas coordinate space to ensure perfect spatial alignment with the user's work. Supabase provides the real-time backbone, utilizing PostgreSQL and live subscriptions to synchronize every stroke and AI suggestion instantly across sessions. I also used TRAE as my primary IDE, which significantly sped up iteration, essentially being my "Cursor for code" while I built "Cursor for Artists." Challenges we ran into Unfortunately, while Nano Banana 3 is a highly performant model, inference is rather slow, taking about ~10 seconds per generation. Downgrading to previous versions degrades the quality significantly, so I kept the existing flow. Accomplishments that we're proud of Solo hacker!!1 What we learned A lot What's next for nexdraw Obviously, this can be much improved. The art canvas is rather simplistic, and modern drawing tools feature several dozen more tools. This presents the opportunity for an AI art agent, rather than a state machine, to solve the task of human learning in the art industry. <div