---
slug: "flabs"
url: "https://devpost.com/software/flabs"
title: "Flabs"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 514
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
---

# Flabs

> flabs turns any browser into an interactive physics lab with an AI assistant. No hardware, no installation, no cost. Students explore real physics by doing, not watching.

[Devpost](https://devpost.com/software/flabs) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[developer_tools]] [[education]]
  <sub>weak: transportation</sub>
**user** [[educator_student]]
  <sub>weak: frontline_worker</sub>
  <sub>weak: structured_db, web_dom</sub>

**stack** 2d, api, canvas, css3, csv, emet, express.js, github, heygen, html5, hyperframes, json, localstorage, node.js

## Body

landing section space view of the project The false start I originally planned something completely different. A tool that helps students catch up on missed material. It was generic, it was boring, and deep down I knew it was bad. Scrapped the whole thing three days ago. ** What actually happened** I started fresh. Three days to build something that matters. The space system — isolated iframes for experiments — was directly inspired by space agents I'd seen in other projects. The idea of clean, isolated workspaces where an AI can build freely without breaking anything else clicked instantly. I chose physics because I genuinely love it. Not because it's trendy or because "AI x STEM" is the hackathon theme. Because watching a water rocket fly with real pressure-thrust physics, then asking an AI why it flew that way, is genuinely exciting to me. I built the backend with pi SDK ( @earendil-works/pi-coding-agent ) because pi is my daily driver. I use pi for everything — all my project work, all my research, all my coding. So when I needed an AI agent that could control simulations, write files, and search physics formulas in real time, the pi SDK was the natural choice. For grounded research , I used emet ( @black-knight.dev/emet ) — it lets the agent fetch cited, authoritative sources when the local formula library isn't enough. Every physics claim the agent makes can be traced back to a real source. The server, the agent engine, the custom tools, the WebSocket bridge, the space system — I built all of it myself in these three days. Everything you see is hand-crafted for this project. What I learned Scope is everything. My first idea died because it was too vague, too generic, too big. flabs worked because I picked one concrete thing (physics experiments in the browser) and built it properly. AI still produces a lot of garbage. You cannot just let a model loose and expect great results. The agent needs strong guidance — clear tool definitions, strict rules about what it can and cannot write, validation steps (the space_verify_current tool exists for exactly this reason). Freedom works, but only within carefully designed constraints. The agent builds surprisingly well. When the boundaries are right — clear prompt, sharp tools, validated output — the agent writes real, working simulation code. It designs experiment parameters. It checks its own work. It explains physics to students. It's not magic, but it is genuinely useful. ** The core tension** flabs exists at a specific point on the spectrum: guided freedom . The agent has powerful tools ( sim_set_param , space_write_current_file , emet for live research) but it also has hard rules (no building controls in HTML, must call space_verify_current after every write, must check licenses before copying code). This balance — powerful enough to be creative, constrained enough to be safe — was the hardest and most important thing to get right. The result? An AI physics lab that actually works. Not because the AI is smart, but because the system around it is well-designed. <div