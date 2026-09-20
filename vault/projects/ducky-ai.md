---
slug: "ducky-ai"
url: "https://devpost.com/software/ducky-ai"
title: "Ducky.AI"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 250
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
---

# Ducky.AI

> An LLM Rubber Ducky. Never worry about being unprepared for a presentation ever again.

[Devpost](https://devpost.com/software/ducky-ai) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[structured_db]]

**stack** amazon-web-services, deno, docker, mongodb, nginx, pulumi, rabbitmq, redis, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ducky.ai

## Body

demo architecture diagram Inspiration Sometimes it's hard to find the right person to practice your presentation with. Maybe you're presenting to a grad class about distributed systems, or you're presenting in your anthropology class about a presentation you made at 4am and you have no idea of what you're saying, or maybe you're a startup presenting to an AI accelerator. In all of these situations -- it's quite hard to find someone who's an accurate representation of your audience member, and sometimes the feedback that people can give us doesn't really match what we need for preparation. After all, how can your dog ask you if Paxos is deployed in an asynchronous, partially synchronous, or synchronous model What it does Ducky.AI is a platform for you to upload, present, and persist your presentations. It's very simple. 1) Upload a presentation 2) Upload configurations like what you're presenting about, who you're presenting to, and what kind of tone you want the presentation to be -- is it casual? or is it as serious as talking to a C-level executive How we built it Front-End: Vite, Nginx Back-End: Deno, AWS S3/Lambda, RabbitMQ Databases: Redis, MongoDB Infra, Pulumi (IaC), Docker Challenges we ran into Integration + those pesky bugs that you can only test in a full run through of the pipeline Accomplishments that we're proud of A completely working prototype. What we learned too much to write here What's next for Ducky.AI series A, real-time AI questions, posture and expression analysis <div