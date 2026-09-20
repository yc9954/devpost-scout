---
slug: "pipeheal"
url: "https://devpost.com/software/pipeheal"
title: "DocSync"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 1239
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# DocSync

> A GitLab Duo Flow that automatically detects and fixes stale documentation the moment code changes merge.

[Devpost](https://devpost.com/software/pipeheal) · hackathon [[GitLab AI Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]]

**stack** duo, express.js, flow, gitlab, javascript

## How they structured the write-up

- inspiration
- what we built
- how we built it
- challenges we faced
- what we learned

## Body

DocSync Inspiration Every developer has lived through this: you join a team, open the README, follow the setup guide step by step — and it doesn't work. The API endpoint documented as GET /api/users/:id was renamed months ago. The config says the default port is 3000 but the code uses 8080 . You end up reading the source to figure out what the docs should say. Studies suggest 50–70% of internal documentation goes stale within six months. Stale docs aren't just useless — they're actively harmful . They cause bugs, waste onboarding time, and erode the trust that makes documentation worth writing in the first place. We kept asking: why does documentation rot happen so reliably? The answer is simple — updating docs after a code change is a manual step with no enforcement. Tests catch broken code; linters catch broken style; nothing catches broken docs . We wanted to change that. What We Built DocSync is a GitLab Duo Flow that triggers after a merge request lands and orchestrates three specialized AI agents in a pipeline: MR Merges ──diff──> Detector ──drift report──> Writer ──fix details──> Reviewer ──> Done Each agent has a distinct role and a strict security boundary: Detector (14 read-only tools) — Reads the MR diff, scans every documentation file, and cross-references them. Produces a structured JSON drift report classifying each finding into one of five drift types ( contradiction , omission , stale_example , stale_reference , version_mismatch ) with a confidence score between 0 and 1. Writer (16 read+write tools) — Consumes the drift report and makes a decision: Any drift confidence >= 0.5 → create a doc-fix MR All drifts below 0.5 → create an Issue for human review No drifts → no action It reads actual source code to verify behavior, edits only documentation files, commits to a new branch, and opens a merge request — or files an issue for low-confidence cases where a human should decide. Reviewer (12 review tools) — Verifies the Writer's changes against the real codebase. It never trusts the drift report alone — it reads the source, checks accuracy, completeness, and quality, then posts a verdict: approved , changes_requested , or rejected . Agents communicate through structured JSON passed via GitLab's context:{agent}.final_answer system. No free-form text leaks between stages. We defined formal JSON Schema (Draft 7) contracts for each agent's output, making the inter-agent protocol explicit and validatable. How We Built It The project didn't start as DocSync. Our first attempt — PipeHeal — was a four-agent CI pipeline repair system that would diagnose and fix broken builds. We built the agents, the flow, and the demo app, but realized the problem was too broad: pipeline failures have hundreds of root causes, and an agent that tries to fix arbitrary build errors ends up guessing. We pivoted to issue-to-MR automation (investigate an issue, write a fix, open a PR), but that was too open-ended too. The breakthrough was narrowing to a specific, well-scoped problem : documentation drift after code merges. The input is constrained (MR diff + doc files), the output is constrained (updated docs), and the verification is tractable (does the doc match the code?). That focus made the agents reliable. We started by defining agent boundaries before writing a single prompt. The key architectural insight was separation of concerns: detection, correction, and verification should be independent agents with independent toolsets. A monolithic "find and fix docs" agent would be tempted to trust its own analysis — splitting the Reviewer out forces a second opinion grounded in source code. We built a Node.js demo app (Express API with math endpoints, user routes, and config) with intentionally driftable documentation. This gave us a controlled environment to test all five drift types: renaming endpoints, changing function behavior, adding new features without updating docs, and bumping versions. The development was iterative. Our git history tells the story: Started with a single-agent flow to validate the Duo Flow mechanics — context passing, tool scoping, prompt templates Expanded to the three-agent pipeline once we understood how context:{agent}.final_answer wiring worked Ran real drift scenarios — the /api/divide endpoint addition and user route rename (MR !12) produced our first fully autonomous doc-fix MR Tested repeatability with the /api/power endpoint (MR !14) and a version + port bump (MR !20) — three successful end-to-end runs The CI pipeline ( validate > install > lint > test > security > deploy ) validates the YAML definitions, runs Jest tests against the demo app, and performs a deploy health check — ensuring the demo app itself stays honest. Challenges We Faced Getting context passing right. The hardest part wasn't writing prompts — it was wiring agents together. GitLab Duo Flows pass data between agents via context:{agent_name}.final_answer , but early on, the Detector's output wasn't reaching the Writer correctly. We had to debug the inputs mapping ( from: "context:detector_agent.final_answer" ) and ensure the routers block was properly defined. Our first flow deployment failed silently because we'd omitted the routers section entirely. Project ID injection. The Detector needs the numeric GitLab project ID to call tools like get_merge_request . We initially hardcoded it in the prompt, then realized the flow needed to inject it dynamically. This required adding project_id as an explicit input parameter threaded through the prompt templates — a fix that took several iterations to get right. Prompt engineering for structured output. Each agent must output only valid JSON — no preamble, no markdown fences, no commentary. Getting Claude to reliably produce clean JSON while still performing complex multi-step tool use (reading diffs, grepping files, cross-referencing code) required careful prompt structure. The key was leading with "Output ONLY valid JSON. Begin with { ." and defining the exact schema inline. The Writer's dual path. Implementing the MR-vs-Issue decision logic was subtle. A naive threshold on confidence isn't enough — if a documentation file needs a >50% rewrite, even high-confidence drifts should be deferred to an issue for human review. We encoded this as a rule in the Writer's prompt, but tuning the boundary took real test cases. Keeping the Reviewer honest. The whole point of the Reviewer is to catch the Writer's mistakes. But if the Reviewer simply reads the drift report and rubber-stamps the fix, it adds no value. We explicitly instructed it to always read the actual source code and verify independently — the drift report is context, not truth. What We Learned Scope beats ambition. We pivoted twice before landing on DocSync. PipeHeal tried to fix any CI failure; DocSync fixes one specific thing well. Narrowing the problem made the agents reliable instead of impressive-but-brittle. Agent separation matters more than prompt quality. Three focused agents with clear contracts outperform one powerful agent trying to do everything. The Reviewer caught real issues that the Writer introduced. Structured inter-agent contracts are essential. JSON schemas between agents prevent hallucination from propagating. If the Detector's output doesn't match the schema, the Writer fails fast instead of hallucinating fixes. Safety by design, not by prompting. The Detector literally cannot modify files — it has only read-only tools. The Writer cannot touch source code — its tools are scoped to documentation. This is enforced at the toolset level, not just the prompt. Documentation drift is a CI problem. Just like tests and linters, doc freshness should be checked in the pipeline. DocSync treats stale docs as a defect to be caught automatically, not a chore to be remembered. <div