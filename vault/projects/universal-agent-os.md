---
slug: "universal-agent-os"
url: "https://devpost.com/software/universal-agent-os"
title: "Universal Agent OS"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 446
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/human_in_the_loop"
  - "mechanism/retrieval_grounding"
  - "substrate/code_repository"
---

# Universal Agent OS

> A consultation-first governance framework giving AI coding agents strict boundaries and collective memory.

[Devpost](https://devpost.com/software/universal-agent-os) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[human_in_the_loop]] [[retrieval_grounding]]
**substrate** [[code_repository]]

**stack** bash, gitlab-ai-catalog, gitlab-ci-cd, gitlab-duo, gitlab-orbit, graphql, markdown, powershell, pytest, python, yaml

## How they structured the write-up

- inspiration
- what it does
- the demo (watch it)
- real, executable orbit usage (not just chat)

## Body

A non-technical founder describes the idea in plain English. The agent grounds itself in the Orbit Knowledge Graph and collective memory. Phase-0 alignment: the agent asks one question at a time. Human approval is required before any action runs. Real GitLab artifacts: a plan, an epic, issues and a merge request. The agent refuses to fake a result for a tool it cannot run. The generated work stays fully reviewable in GitLab. The executable Orbit CLI runs live and blocks risky auto-approval. Inspiration Most agent-driven repositories fail in predictable ways: no stable startup interview, no durable plan, no honest definition of "done," and no reliable handoff between sessions. The GitLab Transcend mission — "Give AI true context" — matched this exactly. We realized true context isn't just reading code; it's strict governance, boundaries, and collective memory. So we built a system that uses the GitLab Orbit Knowledge Graph not as a passive reader, but as an active enforcer of decisions. What it does Universal Agent OS is not another coding agent — it's a consultation-first governance layer for GitLab Duo agents. It turns a loose agent session into a governed delivery model: Phase-0 interview before any code — the agent asks one question at a time , in plain language, so even a non-technical founder can drive it. Grounded in context — every decision is aligned with the project's Orbit Knowledge Graph and a collective memory of past lessons. Human-in-the-loop — every commit, work item, and merge request happens only after explicit human approval . Nothing lands silently. Real, reviewable artifacts — a locked plan of record, an Epic, tracked Issues, and a Merge Request. Anti-hallucination by design — when asked to run a tool it doesn't have, the agent refuses to fake a result instead of inventing an official-looking output. The demo (watch it) In our 3-minute demo, a non-technical founder types one plain-English sentence — an idea for a neighbourhood driveway-sharing app ("ParkShare"). The governed Duo agent runs a full Phase-0 interview one question at a time, then produces a locked plan + an Epic + 7 tracked Issues + a Merge Request — every action behind human approval. 🎬 https://youtu.be/k06ZLksP6lI Real, executable Orbit usage (not just chat) We use Orbit in two ways: As context — the Duo agent grounds every Phase-0 decision in the project's Orbit Knowledge Graph and collective memory. As an executable tool — we built an Orbit client ( tools/orbit_client.py + a python -m tools.orbit_cli CLI) that queries the GitLab GraphQL API (the queryable surface over the Orbit graph) live . Its blast-radius check finds real open merge requests that overlap a proposed change and blocks auto-approval : <div