---
slug: "acg"
url: "https://devpost.com/software/acg"
title: "ACG"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 410
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# ACG

> We make your Multi Agent Architecture 50% less expensive!

[Devpost](https://devpost.com/software/acg) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[multi_agent]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[geospatial]]
  <sub>weak: web_dom</sub>

**stack** html, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for acg

## Body

Inspiration We’ve won 7 hackathons, and every time we hit the same wall: Agents fight over files Context gets too expensive Parallel work breaks merges Results become unpredictable and sloppy So we built ACG: Agent Context Graph. A local-first architecture layer that lets AI agents understand a codebase before they touch it. What it does ACG helps AI coding agents work in parallel without stepping on each other. It scans a codebase, builds a deterministic context graph, predicts which files each task will modify, and creates an agent_lock.json that agents can follow. In our early benchmark, ACG: Reduced prompt context by 54% Cut prompt tokens from 3,721 to 1,700 Completed 7/7 benchmark tasks Tested coordination across up to 5 parallel agent runs Make multi-agent coding feel less like chaos and more like infrastructure. How we built it We built it using: Static code graph analysis Write-set prediction DAG-based task planning Local-first MCP server ACG analyzes routes, imports, symbols, configs, tests, and file relationships. Then it predicts where agents are likely to write, compiles a safe execution plan, and validates edits before they create conflicts. Challenges we ran into The hardest part was making agent behavior predictable. Agents are messy. Codebases are messy. Parallel execution is messy. We had to turn a chaotic multi-agent workflow into something deterministic, inspectable, and safe. Other challenges: Predicting write-sets before execution Reducing context without losing accuracy Handling overlapping agent tasks Designing a simple lockfile format Building fast enough for a hackathon demo Accomplishments that we're proud of The Fact that we were able to find a niche that no one has worked on yet and got substantial improvements! We’re proud that ACG is: Agent-agnostic Insanely Fast to run Built for parallel coding Focused on reducing real engineering waste The biggest win: We proved that multi-agent coding does not need bigger prompts. It needs better coordination. What we learned We learned that multi-agent coding is not just a prompting problem. It is a systems problem. The future is not one giant agent with infinite context. The future is many specialized agents working in parallel with shared coordination rules. ACG is our bet on that future. What's next for ACG Next, we want to make ACG the default coordination layer for AI engineering teams. We want to add: Live conflict dashboards Deeper Windsurf/Cascade integration Better write-set prediction Agent performance traces Team-scale task planning Our long-term vision: Make parallel AI coding reliable enough for real software teams. <div