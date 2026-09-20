---
slug: "selfheal-qa"
url: "https://devpost.com/software/selfheal-qa"
title: "SelfHeal QA"
hackathon: "UiPath AgentHack"
organization: "UiPath"
winner: true
words: 927
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# SelfHeal QA

> An autonomous UiPath agent that heals brittle UI tests but refuses to heal real bugs, filing a defect instead. The testing agent that knows when not to heal.

[Devpost](https://devpost.com/software/selfheal-qa) · hackathon [[UiPath AgentHack]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]]
**domain** [[accessibility]] [[developer_tools]] [[health_clinical]] [[housing_homeless]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[transcript_audio]]

**stack** api, claude-code, playwright, python, restapi, typescript, uipath, uipath-coded-agents, uipath-orchestrator, uipath-test-manager

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for selfheal qa

## Body

Self-documenting test runs reported to UiPath Test Manager. The money moment: the agent self-heals the brittle locator, then refuses to heal a real regression (REAL_BUG) and flags it as a defect. On a real bug, a defect is filed in Test Manager instead of a silent heal. Live on the UiPath hackathon tenant (hackathon26_975): both runs complete Successfully on Cloud Serverless. The Coded Agent published to the hackathon tenant package feed (selfheal-qa-agent v0.2.2). Built as a UiPath Coded Agent (Python, uipath SDK/CLI). A genuinely brittle locator: self-healed #login-btn → #sign-in-btn and the test passes. Adversarial benchmark: 0% false-negative across 16 cases, including look-alikes built to fool it. Inspiration Brittle UI tests are the #1 reason teams give up on test automation. Someone renames a button, the whole suite goes red overnight, and an engineer loses a morning figuring out whether anything is actually broken. Self-healing was supposed to fix this, and it does, right up until you hit the worst problem it creates. A test that blindly heals itself can heal right past a real bug. It patches around the failure, turns green, and quietly ships the regression. You find out when a customer does. So I wanted something past "tests that fix themselves." I wanted a testing agent that knows the difference between the locator moving and the product being broken. UiPath's Autopilot already self-heals, so I didn't try to out-heal it. I went straight at its blind spot: the over-healing that masks real bugs. What it does You hand SelfHeal QA a code change and a plain-English description of what should work. From there it's on its own: Runs only what's at risk. It maps your changed files to the suites they touch and runs just that slice, not all four. Writes and runs the test in a real browser, and the moment a step fails it asks the real question: flaky locator, or genuine bug? Brittle locator: it reads the live page, rewrites the selector, and re-runs until green. Nobody touches it. Real bug: it refuses to heal, and files a defect in UiPath Test Manager with its reasoning attached, so a human sees the regression instead of it getting buried. The entire loop runs as a UiPath-coded agent deployed to Orchestrator. Restraint, knowing when not to act, is the whole point. Validated: 0% false-negative rate across 8 real regressions, 100% triage accuracy on a 16-case adversarial benchmark including look-alikes designed to fool it. How we built it A ** UiPath-coded agent** (Python, scaffolded, run, and published with the uipath CLI) that calls UiPath Identity and Test Manager v2 REST APIs directly: select, generate, run, triage, heal or file, report. Claude makes the bug versus brittleness triage call and proposes the new selector from the page's live elements, with a deterministic fallback if the model is unavailable. UiPath Test Manager is the system of record: test cases, sets, executions, logs, and the auto-filed defects. A Playwright executor drives a real browser for the live demo. Deployed to Orchestrator and verified end to end by running the published package as a serverless job, which completed Successful . Built start to finish with Claude Code , through UiPath for Coding Agents. Challenges we ran into Scope discovery was painful. invalid_scope is all or nothing, so one wrong scope name fails the whole token with no hint which one. I had to probe Test Manager scopes one by one ( TM.TestExecutions , plural, is required and easy to miss). A test execution requires a test set. Posting test cases alone returned a 500, not a helpful 400. Cloudflare blocked the default urllib User-Agent (403, error 1010) on the Identity token endpoint. Coded agents using stdlib HTTP hit this immediately, and a User-Agent header fixed it. Headless publish via client credentials kept returning 403 on a personal-workspace read until I switched to uipath publish --tenant . Trusting the "refuse to heal" decision was the hardest part. An agent that is confidently wrong is dangerous, so I built an adversarial benchmark to prove it. Accomplishments that we're proud of A 0% false-negative rate across 8 real regressions and 100% triage accuracy on a 16-case benchmark, including adversarial look-alikes built to fool it, a real bug where the button still exists, and a harmless change dressed up as an error. The full per-case transcript is committed in the repo and regenerates on every run. It doesn't just say it files defects. It really writes a defect into UiPath Test Manager (with real execution and defect IDs), and the whole agent runs as a Successful serverless Orchestrator job, verified end to end. Built solo as my first UiPath project, scoped deliberately to prove one thing end-to-end: that restraint is more valuable than healing everything. Verified from first commit to a successful Orchestrator job, entirely with Claude Code. What we learned The hard part of autonomous QA isn't the healing. It's the restraint. The most valuable thing an agent can do is know when not to act. UiPath coded agents and the Test Manager API are a genuinely powerful base for agentic testing once you get past scope discovery. You can't ask people to trust an agent's judgment on faith. Adversarial benchmarking is what turns "trust me" into a number. What's next for SelfHeal QA Run it as a pre-merge check on every pull request, so brittle versus real triage happens before code lands. Move browser execution onto UiPath's own UI automation. Teach triage a third category for flaky versus environmental failures, detecting infra noise before it reaches the triage decision. <div