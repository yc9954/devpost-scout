---
slug: "carbonlint"
url: "https://devpost.com/software/carbonlint"
title: "CarbonLint"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 892
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# CarbonLint

> An AI agent that lints your GitLab CI/CD pipelines for carbon waste — scoring sustainability, flagging inefficient jobs, and recommending fixes that cut compute time, costs, and CO2 emissions.

[Devpost](https://devpost.com/software/carbonlint) · hackathon [[GitLab AI Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]]
**domain** [[climate_energy]] [[developer_tools]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** ai-catalog, ci/cd, duo-agent, gitlab, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned
- what's next for carbonlint

## Body

Thumbnail Repository Inspiration Every day, millions of CI/CD pipelines run across the world — and most of them are wasteful. Teams use oversized Docker images, skip caching, run redundant jobs on every branch, and let artifacts pile up forever. It's invisible waste: no one sees the extra compute minutes burning through cloud resources and generating unnecessary carbon emissions. We asked a simple question: what if your pipeline had a linter — not for code quality, but for carbon efficiency? That's how CarbonLint was born. Just like ESLint catches code smells and Stylelint catches CSS issues, CarbonLint catches sustainability smells in your CI/CD configuration. What it does CarbonLint is an AI-powered pipeline sustainability auditor built on the GitLab Duo Agent Platform. It comes in two forms: CarbonLint Advisor (Agent) — a chat-based agent in GitLab Duo Chat. You ask it to analyze a project's pipeline, and it performs a deep audit across five categories: redundant execution, Docker image waste, caching failures, artifact bloat, and pipeline structure. It delivers a Green CI Score (1-10), a before vs. after comparison of pipeline time, compute, and CO2, before/after YAML fix snippets for every finding, and an org-wide projection showing what the savings would look like across 10+ repositories. It also features an Auto-Fix Mode — say "fix my pipeline" and it generates an optimized .gitlab-ci.yml , validates it, and opens a merge request with all fixes applied. After analysis, it offers to add a sustainability badge to your README showing your Green CI Score. CarbonLint Analyzer (Flow) — an automated multi-agent flow you trigger by @mentioning it on any issue or merge request. It chains two AI agents: a Scanner that reads all CI/CD config files and analyzes job performance data, and a Reporter that validates every suggested fix with ci_linter and posts a beautifully formatted report directly as a comment — complete with emoji severity indicators, a before/after impact table, org-wide projections, and a suggested sustainability badge. No manual work required — just tag the bot and get your sustainability audit. How we built it CarbonLint is built entirely on the GitLab Duo Agent Platform using custom agents and flows defined in YAML configuration files. The Agent uses 25 GitLab tools including read_file , grep , find_files , get_job_logs , ci_linter , and action tools like create_merge_request , edit_file , and create_commit — so it can not only identify problems but also propose fixes directly. The Flow chains two specialized agents with distinct toolsets: The Scanner agent has 16 tools focused on discovery and analysis — reading files, searching repositories, checking pipeline errors, and analyzing job logs The Reporter agent has 9 tools focused on validation and action — linting YAML, posting comments, creating issues, and opening merge requests with fixes The system prompts were carefully engineered with specific heuristics: expected savings percentages per category (e.g., "caching failures typically waste 1-5 minutes per pipeline"), a standardized scoring rubric, and a sustainability formula (1 compute-minute ≈ 0.5g CO2) to quantify environmental impact in every recommendation. Challenges we faced Schema validation was tricky. The flow YAML schema has specific requirements that aren't fully documented — we discovered through trial and error that placeholder and params are not valid fields in prompts, while unit_primitives is required. Each failed pipeline took ~30 seconds to validate, so debugging was a rapid iteration cycle of commit → check → fix → repeat. Balancing prompt depth with reliability. Longer, more detailed system prompts produce smarter analysis, but they also increase the chance of the agent going off-script. We iterated on the prompt structure multiple times — moving from free-form instructions to clearly numbered steps (STEP 1, STEP 2, etc.) and structured output formats that the reporter agent could reliably parse. Testing on a project with no CI/CD config. Our hackathon project itself doesn't have a .gitlab-ci.yml , so the agent initially had nothing to analyze. We turned this into a feature — CarbonLint now detects when there's no CI config, analyzes the project structure, and offers to generate an optimized pipeline from scratch. What we learned The GitLab Duo Agent Platform is powerful but still evolving — the documentation and schema are actively being refined, which means building on it requires comfort with experimentation System prompt engineering for multi-agent flows is fundamentally different from single-agent prompts — you need to think about how output from one agent becomes input for the next Sustainability in software isn't just about the application code — the infrastructure around it (CI/CD, builds, deployments) has a real and measurable carbon footprint The tool ecosystem in GitLab is extensive (89 built-in tools) and choosing the right subset for each agent is a design decision that significantly affects capability What's next for CarbonLint Historical trending — track Green CI Score over time to show improvement as teams adopt recommendations Team dashboards — aggregate sustainability metrics across all projects in a group, giving engineering leads visibility into org-wide pipeline efficiency CI/CD component — package CarbonLint as a reusable CI/CD component that runs automatically as a pipeline job on every merge request Benchmark database — compare your pipeline's efficiency against similar projects to provide relative scoring ("your Node.js pipeline is in the top 20% for efficiency") Carbon budget alerts — set a monthly compute budget per project and get notified when a pipeline change would push you over the threshold <div