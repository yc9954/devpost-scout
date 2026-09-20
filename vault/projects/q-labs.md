---
slug: "q-labs"
url: "https://devpost.com/software/q-labs"
title: "Q Labs"
hackathon: " GenAI Genesis 2026"
organization: "GenAI Genesis"
winner: true
words: 621
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Q Labs

> Autonomous QA sandboxes powered by AI agents, test any app, catch every bug.

[Devpost](https://devpost.com/software/q-labs) · hackathon [[GenAI Genesis 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** claude, db2, docker, faker.js, fastapi, ibm, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for q labs

## Body

Q Labs Dashboard QA View Sandbox View Inspiration QA is one of the most critical yet tedious parts of shipping software. Setting up test environments, writing smoke tests, reproducing bugs, and verifying fixes all demand significant time and infrastructure expertise. We asked ourselves: what if you could upload any Docker image and have AI agents automatically explore your app, find bugs, and prove they're fixed — all without writing a single test script? What it does Q Labs transforms any Docker image into an on-demand QA sandbox. Users upload their app, define test scenarios, and let AI agents do the rest: Sandbox provisioning — Spin up isolated Docker containers from any app version in seconds Auto QA — Automatic smoke testing across all app routes with pass/fail reporting and severity classification AI agent navigation — AI agents that intelligently browse your app, fill forms, click buttons, and find broken flows Multi-agent orchestration — Generate and run multiple test tasks in parallel across focus areas like checkout, search, and input validation State capture — Snapshot a broken sandbox state, fix the bug, re-run QA, and show the before/after Versioned test history — Track regressions over time with detailed per-endpoint results How we built it Frontend: Next.js 16 with React 19, Tailwind CSS, and shadcn/ui for the control panel dashboard Backend: FastAPI (Python) handling sandbox orchestration, QA execution, and AI agent coordination AI: Anthropic Claude API — Haiku for real-time agent navigation decisions, Opus for intelligent test task generation Infrastructure: Docker Python SDK for container lifecycle management, port mapping, and volume mounting Database: IBM Db2 for metadata and scenario state Architecture: The agent system uses DOM analysis and CSS selectors ( data-testid , aria-label ) to navigate apps without any hardcoded test scripts Challenges we ran into Container orchestration at speed — Managing port allocation, health polling, and parallel sandbox launches required careful concurrency handling with threading and async HTTP AI agent reliability — Getting Claude to consistently produce valid CSS selectors and avoid infinite action loops took significant prompt engineering and retry logic State preservation — Capturing and restoring full app state (including SQLite WAL files) across container restarts was tricky to get right Generalization — Making the platform work with any Docker image rather than a single hardcoded app required flexible config injection and environment variable passthrough Accomplishments that we're proud of A fully working end-to-end flow: upload an app, introduce a bug, watch AI find it, fix it, and verify the fix — all in minutes Multi-agent orchestration that can probe different areas of an app in parallel without any pre-written test scripts Clean sandbox state capture that lets you freeze a broken state and hand it to a developer for debugging A polished dashboard that makes complex container orchestration feel simple What we learned AI agents are remarkably effective at exploratory QA when given the right DOM context and action primitives Container orchestration is the unsexy backbone that makes or breaks a platform like this — reliability matters more than features Prompt engineering for structured JSON output (action types, selectors, reasoning) is an art that directly impacts agent success rates Building for generalization from day one (any Docker image, any app) forces better architecture decisions than building for a single use case What's next for Q Labs Visual regression testing — Screenshot comparison between QA runs to catch UI regressions CI/CD integration — GitHub Actions / GitLab CI hooks to run Q Labs on every PR Collaborative debugging — Shareable sandbox URLs with real-time co-browsing for distributed teams Custom agent workflows — Record and replay agent flows as reusable test suites Expanded AI capabilities — Multi-modal agents that can analyze screenshots and validate visual correctness alongside functional testing <div