---
slug: "crosscut"
url: "https://devpost.com/software/crosscut"
title: "CrossCut"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 599
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# CrossCut

> Run What Matters !!

[Devpost](https://devpost.com/software/crosscut) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[structural_withholding]]
**domain** [[developer_tools]]
**substrate** [[code_repository]]

**stack** duckdb, framer, gitlab, mypy, next.js, orbit, pytest, python, pyyaml, react, recharts, rest, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for crosscut

## Body

Inspiration Me and my partner both have open source contribution experience, so we have sent a lot of PRs and watched CI gate every one. As a contributor( https://github.com/rahulgunwanistudy-2005 ) on The Honeynet Project, that problem got bigger... CI runs the full suite on every MR, even for a one line change, and most of those tests never touched what you changed. The reason nobody fixes it is you need the call graph of the whole codebase to know which tests a change can reach. That is exactly what GitLab Orbit builds, so instead of guessing, we just ask the graph. What it does When you open an MR, Crosscut finds the code you changed, asks Orbit which tests call back to it, and runs only those instead of the whole suite. It then comments on the MR with what it ran, what it skipped, and why, plus a one click way to run everything. The selection is deterministic, no model decides, and when the graph cannot prove a change is safe to narrow, it runs the full suite. How we built it A small, plain Python engine: read the MR diff for changed symbols, index the repo with the Orbit Local CLI, query the graph for every caller leading back to them, keep the ones that are tests (by file path, since Orbit has no "test covers code" edge), then generate a child pipeline that runs only those and post the result. It ships as a GitLab Duo Agent Platform skill plus a .gitlab-ci.yml job, so it runs inside GitLab with no extra server. Challenges we ran into Orbit was nothing like we assumed. We expected Cypher style queries, but Orbit Local is plain SQL over a DuckDB file, so the lesson was to read orbit schema before writing one query. CI had sharp edges too: the generated YAML had to stay valid in every case, like a change with zero impacted tests or a changed test file that has to run itself. Cross file calls do not point straight at the target either, so we resolve them by name and over include on purpose, since running a few extra tests is fine but skipping one is not. Accomplishments that we're proud of The whole thing is real, with no fake demo data. It queries a live Orbit graph, and on its own repo a one helper change runs 8 of 78 tests in 0.24s instead of 0.50s. The part we are proud of is the trust moment: a change to a shared model correctly widens to 26 of 78, the files that actually use it, so it computes the real blast radius instead of replaying a number. The selection logic has its own tests, and types and lint both pass. What we learned Never guess the shape of a system you build on, reading Orbit's real schema first saved us from queries built on a graph that does not exist. We also learned this is about trust, not speed: skipping tests is easy, being safe enough that a team lets you is the hard part, which is why the whole engine follows one rule, never skip a test that should run. What's next for Crosscut Cross repo is the clear next step: the same backward walk spans every repo in a group on Orbit Remote, so a shared library change can pick impacted tests across all the services using it. After that, real time savings reported straight from the pipeline, more languages through Orbit's parsers, and smarter handling of dynamic calls a static graph cannot see. <div