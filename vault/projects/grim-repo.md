---
slug: "grim-repo"
url: "https://devpost.com/software/grim-repo"
title: "Grim Repo"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 507
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Grim Repo

> Your GitHub issues rise from the dead. Exorcise bugs, banish feature requests, cleanse your codebase.

[Devpost](https://devpost.com/software/grim-repo) · hackathon [[Kiroween]]

## Facets

**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]]

**stack** fast-check, framer-motion, github-graphql-api, kiro, next.js, nextauth.js, octokit, react, react-markdown, rehype-sanitize, tailwind-css, typescript, vitest, zustand

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- what i learned
- what's next

## Body

Inspiration Every developer knows the guilt of opening a repo and seeing a wall of open issues. I wanted to make that feeling tangible — and a little spooky. What if your codebase was a graveyard? Files that haven't been touched in months slowly decay into crumbling tombstones. Open issues rise from the ground as undead creatures, haunting the code they reference. And you? You're the Caretaker, armed with the power to exorcise bugs and banish feature requests. What it does Grim Repo transforms GitHub repository maintenance into an immersive necromancy experience: 🪦 Tombstones — Files appear as graves that visually decay based on code age (polished marble → weathered stone → cracked → moss-covered ruins) 🧟 Zombies & Ghosts — Open issues manifest as undead. Bugs are zombies. Feature requests are ghosts. 🔥 Exorcism — Close an issue and watch it burn in holy fire 📊 Corruption Level — A health HUD shows how "haunted" your repo really is 🎯 Smart Haunt — Issues don't float randomly. The algorithm scans issue bodies for file references and positions undead near the code they're haunting. How I built it This is where Kiro changed everything. Instead of my usual "start coding and figure it out" approach, I used Kiro's Spec workflow : Requirements — Defined exactly what "tombstone decay" meant, how issues map to undead types, the corruption formula, everything. No ambiguity. Design — Mapped out the architecture, data flow, TypeScript interfaces, and component structure before writing a line of code. Tasks — Broke implementation into 28 phases with specific subtasks, each linked back to requirements. The result? I actually knew what I was building before I built it. Revolutionary, I know. I also wrote property-based tests using fast-check. Instead of testing specific cases, I generated random inputs and verified the system behaves consistently. The Smart Haunt algorithm, corruption calculation, and tombstone variant assignment all have formal correctness properties. Challenges Isometric rendering — Getting z-index right so foreground elements properly occlude background elements. The formula zIndex = x + y sounds simple until you're debugging why a ghost is rendering behind a tombstone it should be floating over. Smart Haunt edge cases — What if an issue mentions multiple files? What if it mentions a filename that exists in multiple directories? The spec forced me to define priority rules upfront instead of discovering these problems mid-implementation. Resisting the urge to just code — Honestly, the hardest part was trusting the process. Planning feels slow when you're excited about an idea. But I didn't have to rewrite everything three times, so... worth it. What I learned Specs aren't overhead — they're scaffolding. The time spent planning saved me from the chaos I usually create for myself. Kiro's workflow isn't about AI writing code for me. It's about having a structured process that makes me a better developer. What's next Multiplayer mode where teams compete to exorcise issues Historical view showing the graveyard evolving over time Sound design (because graveyards need ambient audio) Mobile-responsive touch interactions for on-the-go exorcisms <div