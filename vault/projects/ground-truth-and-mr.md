---
slug: "ground-truth-and-mr"
url: "https://devpost.com/software/ground-truth-and-mr"
title: "Ground Truth and MR"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 582
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# Ground Truth and MR

> Expose the gap between what a codebase looks like it is, and what it actually is, based on real dependency and coupling data from the GitLab Orbit knowledge graph.

[Devpost](https://devpost.com/software/ground-truth-and-mr) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[developer_tools]]
**substrate** [[code_repository]]

**stack** gitlab

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ground truth and mr

## Body

Inspiration Every codebase tells a story through its folder names. auth/ , billing/ , core/ , utils/ — these names imply boundaries, ownership, and importance. The actual architecture lives in the dependency graph: what imports what, what's truly load-bearing, where the real coupling hides. What it does Ground Truth is a GitLab Duo Agent that audits your codebase's claimed architecture against its actual architecture, using the Orbit knowledge graph as the source of truth. Point it at a repo and it will: Read the apparent structure from folder and file names State that as a falsifiable hypothesis — "this repo claims auth and billing are independent" Query the Orbit graph for real incoming dependency counts, cross-boundary imports, and circular dependencies Identify the single most counter-intuitive finding — the hidden load-bearing module, the "isolated" folder with 40 cross-boundary imports, the utils/ file that half the codebase depends on Report the full delta: claimed vs. actual, with specific file paths and real numbers throughout It doesn't restate your folder structure back at you. It tells you where your folder structure is lying. How we built it Ground Truth is a custom agent built on GitLab's Duo Agents framework and published to the AI Catalog. The system prompt encodes a strict 6-step procedure that runs every time: Step 1 — Readiness check: Orbit: Get Graph Status before anything else. Never proceed silently on stale or incomplete data. Step 2 — Schema discovery: Orbit: Get Graph Schema + Orbit: List Commands — because different projects expose different node/edge types. Hard-coding assumptions breaks things. Step 3 — Hypothesis formation: Commit to what the folder names claim before querying anything, so the comparison is explicit. Step 4 — Live graph queries: Orbit: Query Graph and Orbit: Invoke Command for centrality, cross-boundary edges, and circular dependencies. Step 5 — Lead finding isolation: Identify the single most counter-intuitive result before writing anything else. Step 6 — Delta report: Claimed vs. actual, structured, with real numbers throughout. The agent is deliberately constrained: every number it states must come from an actual query in that conversation. It cannot estimate, hedge, or invent a dependency count. Challenges we ran into The hardest challenge was for MR, finding a MR that I could do and understand was both fun and challenging. Accomplishments that we're proud of The strictness. Ground Truth won't say "module X has high coupling" without a number from the graph. It won't claim two folders are isolated if cross-boundary edges exist. And if the codebase's claimed and actual structure mostly agree, it says that plainly — it doesn't manufacture a problem that isn't there. Enforcing that constraint reliably in a prompt took more iteration than expected. Getting it to hold across varied repos and schemas is the part we're most satisfied with. What we learned The Orbit knowledge graph is a fundamentally different signal than what most static analysis tools expose. Most tools tell you what exists. Orbit tells you how things relate — and relationship data is where architecture drift actually lives. What's next for Ground Truth and MR Drift history: Track the claimed-vs-actual delta over time so teams can see exactly when their mental model started diverging from reality Ownership integration: Combine contributor ownership edges with coupling data to surface files that are architecturally central but owned by no one — or someone who left Team briefing mode: A condensed output format for architecture review meetings — one page, biggest finding first, with only the numbers that matter <div