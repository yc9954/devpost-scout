---
slug: "merge-queue"
url: "https://devpost.com/software/merge-queue"
title: "Merge Queue"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 526
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "substrate/geospatial"
---

# Merge Queue

> State-aware GitHub PR review on the MX Creative Console: dial through your queue, jump to failing checks, and merge only when safe (arm + confirm)

[Devpost](https://devpost.com/software/merge-queue) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]]
**domain** [[developer_tools]]
**substrate** [[geospatial]]

**stack** c#, github-api, logi-actions-sdk, oauth

## How they structured the write-up

- inspiration
- about the project
- what it does
- guardrails (the whole point)
- how we built it (application phase)
- challenges
- what we learned
- what’s next

## Body

controls usage closer look console Inspiration PR review is where work actually ships, and it’s full of tiny repeated decisions: What failed? Is this safe to merge? What’s next? Even good reviewers waste time bouncing between tabs and re-checking CI across repos. The pain isn’t typing commands — it’s the decision loop and the risk of merging at the wrong time. About the project Merge Queue (working title) is a GitHub-first Logi Actions SDK plugin concept for the Logitech MX Creative Console that turns PR review into a state-aware workflow on physical controls. This is not “shortcuts.” It’s a PR state machine : the device always shows the next safe action for the PR you’re on, based on live PR/CI/permissions state. What it does Core actions stay one touch away, but dangerous actions are gated by real state : Next actionable PR (your review queue across repos) Open PR Checks focus (jump to failing checks / failing job logs) Approve Request changes (saved reasons/templates) Copy link Merge (only appears when safe; requires confirm) On-device interaction model (assumed from the Creative Console setup) Dialpad dial rotate: move through PR queue (Prev/Next PR) Dialpad roller: scroll diff / cycle files or failing checks Dialpad back/forward: previous/next file or thread Dialpad right button: open Actions Ring for contextual actions (status, checks, merge/confirm) Keypad display keys: the 6–10 “always-used” actions (Open / Checks / Approve / Request Changes / Copy Link / Merge when eligible) (This mapping is deliberately simple so it’s immediately testable once hardware is available.) Guardrails (the whole point) “Merge” is never a dumb button: Only enabled when required checks pass , PR is up to date , and the user has permission . If state is stale / API fails, Merge disappears or disables . Merge requires a two-step confirm (arm → confirm) to prevent fat-finger merges. How we built it (Application Phase) This submission focuses on feasibility and a build plan: Defined the minimal action set and on-device layout around the reviewer workflow. Built a small GitHub API proof-of-concept to fetch a user’s PR queue plus CI / mergeability state. Sketched a realistic plugin architecture: Actions SDK plugin ↔ local companion service ↔ GitHub (keeping the Logitech layer thin and the GitHub logic isolated). Challenges Designing real safety gating: merge must reflect real CI + policy state, not just a button press. Keeping scope tight: GitHub integrations explode in surface area; we intentionally focus on queue → checks → safe merge . No device in hand yet: interaction is designed to validate quickly the moment the Creative Console is available. What we learned The credible value isn’t “git on hardware” — it’s review state + safe, repeatable actions without context switching. A plugin only makes sense if it’s dynamic (actions change with PR state) and focused (small set used all day). Reliability and guardrails are features, not polish. What’s next If shortlisted, we will: Implement the full Actions SDK plugin wired to the GitHub integration. Polish the on-device UX (labels, status cues, confirmations) and harden the gating logic. Add team-ready features: shared request-change templates, consistent review actions across repos, and optional org-level policies later. <div