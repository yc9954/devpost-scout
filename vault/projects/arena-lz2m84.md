---
slug: "arena-lz2m84"
url: "https://devpost.com/software/arena-lz2m84"
title: "Arena"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 461
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Arena

> Arena makes agents compete to write the software that best serves you.

[Devpost](https://devpost.com/software/arena-lz2m84) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**user** [[legal_professional]]
**substrate** [[code_repository]] [[web_dom]]

**stack** express.js, github-api, next.js, node.js, probot, smee.io, typescript, vercel, vercel-api, warp-oz-agent-sdk

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for arena

## Body

Home Page (Jobs Running) Warp Agent View Page Inspiration AI coding agents are powerful, but for frontend work they’re unreliable and hard to evaluate from diffs. We wanted a workflow where you can run multiple attempts in parallel and judge them by live UI previews , not PR spam. What it does Arena lets you define a “job”, spawns multiple Warp Oz agents to implement the same frontend task on separate branches, monitors progress, and surfaces Vercel preview URLs of their attempts. You're able to try out each attempt on Vercel to see what you like, and then pick winner(s) that will open PRs to your repo. (Either for code review and approval or, with multiple candidates, to scrutinize their implementation approach and quality to pick a final winner). How we built it Backend: Probot GitHub App + REST API for webhooks, getting data out of GitHub, and job management Agent execution: Warp Oz SDK to spawn and monitor parallel agent runs Deployment discovery: Polls GitHub deployments/workflows/commit statuses to detect Vercel preview URLs (optional Vercel API token to resolve dashboard URLs) Frontend: Next.js dashboard showing agent status, Warp session links, and iframe previews; selection UI + “Create PRs” action Challenges we ran into Reliably detecting preview URLs across different GitHub/Vercel signals (deployments, workflow runs, commit statuses) Making sure our integrations (with Vercel and our custom GitHub App) were in place Orchestrating multiple long-running agent runs and deciding when a job is “done” in the presence of flakiness (We used a majority + idle timeout approach inspired by how to cook microwave popcorn) Accomplishments that we're proud of End-to-end workflow: job → parallel agents → monitoring → previews in the dashboard → PR creation from selected candidates Clean “preview-first” review experience (side-by-side iframes) that’s meaningfully better to use than clicking around a bunch of draft PRs Built a real orchestration layer around Warp agents with a clear architecture and extensible hooks What we learned For frontend tasks, the best review artifact is a live deployment , not a diff Orchestrating agents is as much about observability and integration as it is about prompting Real-world reliability comes from handling messy edge cases in CI/deploy signals and timeouts What's next for Arena Richer GitHub integration. Let users give an issue link instead of a prompt, for example, or leave comments on a draft PR to have the responsible agent make some changes. More control over agents. If you want something different, it should be easy to update the agents with more instructions or start over with changes to your prompt. Add persistence (DB) + branch cleanup + agent cancellation Enforce automated verification (running tests, but also tools like Stagehand by Browserbase to exercise UIs) to keep broken candidates from taking up human review <div