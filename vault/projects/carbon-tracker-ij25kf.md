---
slug: "carbon-tracker-ij25kf"
url: "https://devpost.com/software/carbon-tracker-ij25kf"
title: "Carbon Tracker"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 1061
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/retrieval_grounding"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Carbon Tracker

> An AI agent on GitLab Duo that automatically tracks CO2 emissions from every CI/CD pipeline run and delivers Claude-powered sustainability reports with actionable optimization tips.

[Devpost](https://devpost.com/software/carbon-tracker-ij25kf) · hackathon [[GitLab AI Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[retrieval_grounding]]
**domain** [[climate_energy]] [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]]

**stack** anthropic-claude, gitlab-api, gitlab-duo-agent-platform, gitlab-flows, markdown, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for carbon tracker

## Body

First MR Merged Tool Fix MR !4 Carbon Report on MR !1 Optimization Tips with Code Per-Job Breakdown on MR !4 Carbon Report on MR !1 CO2 Distribution + Waste Patterns Inspiration I was reviewing a failed CI/CD pipeline when a thought hit me — this pipeline just retried 3 times. How much electricity did that waste? I searched for a tool that could answer that. Nothing existed. No GitLab feature. No third-party plugin. No open source project. Developers obsess over pipeline speed, test coverage, and code quality — but the carbon footprint of their infrastructure is completely invisible. The software industry contributes roughly 2–3% of global carbon emissions . CI/CD pipelines are a silent, measurable part of that number. A team of 10 developers running 20 pipelines a day emits close to 1 tonne of CO2 per year — just from pipelines. Nobody knows. Nobody tracks it. That gap is what inspired Carbon Tracker. What It Does Carbon Tracker is a 3-agent flow built on the GitLab Duo Agent Platform that automatically calculates the carbon footprint of every CI/CD pipeline run and posts a sustainability report powered by Claude (Anthropic). 🔁 Triggered by mentioning the flow in any Issue or Merge Request 📊 Calculates CO2 emissions per job using a physics-based energy model 🤖 Uses Claude to detect waste patterns and generate actionable tips 💬 Posts a formatted sustainability report as an MR/Issue comment automatically Carbon Calculation Model Energy consumed per job: $$ E_{kWh} = \frac{t_{seconds}}{3600} \times \frac{P_{runner}}{1000} $$ CO2 emitted per job: $$ CO_2 \, (g) = E_{kWh} \times I_{carbon} $$ Where: \( P_{runner} = 150W \) — typical shared GitLab runner power draw \( I_{carbon} = 475 \, gCO_2/kWh \) — global average carbon intensity (IEA 2024) Waste multiplier for retried jobs: $$ CO_{2_{total}} = CO_{2_{job}} \times (1 + N_{retries}) $$ A job emitting \( 44g \) that retries 3 times silently wastes an additional \( 132g \) — completely invisible without this tool. Sample Report Output 🌱 Carbon Tracker Report — Pipeline #4821 | ⚡ Energy | 💨 CO₂ | 🚗 Equivalent | |-----------|--------|----------------| | 0.43 kWh | 204g | ~1.36 km driven| 📋 Job Breakdown | Job | Duration | CO₂ | Status | |---------------|----------|-----|--------| | test:unit | 45m | 89g | ✅ | | build:docker | 38m | 75g | ✅ | | test:e2e | 22m | 44g | ❌ | 💡 Optimization Tips: 1. Fix flaky e2e tests → saves ~132g per pipeline 2. Skip docker build on doc-only commits → saves ~75g/run 3. Parallelize test:unit → cuts runtime by ~60% 🤖 Carbon Tracker · GitLab Duo + Claude (Anthropic) How We Built It Carbon Tracker is built entirely on the GitLab Duo Agent Platform using two YAML configuration files — no external servers, no databases, no infrastructure to maintain. Architecture User mentions @ai-carbon-tracker-flow ↓ Agent 1: pipeline_fetcher Tools: get_merge_request, list_merge_requests → Retrieves job names, durations, statuses ↓ Agent 2: carbon_calculator → Applies energy model, detects waste, builds report ↓ Agent 3: report_publisher Tools: create_merge_request_note, create_issue_note → Posts report as MR/Issue comment ↓ Report Live ✅ Files flow.yml — defines the 3-agent orchestration with: 3 AgentComponent steps connected via routers from/as input passing between agents Dedicated prompt_template per agent Claude as the AI model (GitLab Duo default) agent.yml — defines a standalone agent for on-demand use directly from GitLab Duo Chat. The entire project is 2 YAML files — lightweight, portable, and fully native to the GitLab Duo Agent Platform. Challenges We Ran Into 1. Learning GitLab Duo from zero I had never used GitLab before this hackathon. Learning the Agent Platform, Flow schema, YAML configuration, and tool system simultaneously within a tight deadline was the steepest part of the build. 2. YAML schema validation errors The toolset format in flow.yml was undocumented for custom flows. I went through multiple iterations — plain strings, tool_name: keys, nested objects — before landing on the correct format that passed the CI schema validator. Each attempt was a full commit-pipeline cycle. 3. No official runner energy data GitLab's API doesn't expose runner power consumption. I researched cloud compute energy benchmarks and settled on \( 150W \) as a physically grounded constant — accurate enough to be meaningful without overclaiming precision. 4. Prompt engineering for consistent output Getting Claude to produce a clean, consistently formatted markdown table on every single run — with specific actionable tips, not generic advice — required significant iteration on the system prompts across all 3 agents. Accomplishments That We're Proud Of ✅ Built a fully working multi-agent flow on GitLab Duo with zero prior GitLab experience ✅ Designed a physics-based carbon model grounded in real energy consumption data ✅ Created what is (to our knowledge) the first per-job CO2 breakdown tool for GitLab CI/CD pipelines ✅ Implemented genuine 3-agent orchestration — not a chatbot, a real multi-step automated workflow ✅ Made sustainability completely frictionless — developers get carbon data without changing their workflow at all ✅ Shipped from zero GitLab knowledge to a validated, catalog-published flow within the hackathon window What We Learned How to architect and deploy a multi-agent flow on GitLab Duo end-to-end from scratch How from/as input passing works between AgentComponent steps in a GitLab Duo Flow How to model real-world energy consumption from software infrastructure using publicly available carbon intensity data How Claude's system prompts can enforce structured, consistent output formats across automated multi-step pipelines The surprisingly large hidden cost of flaky tests: $$ CO_{2_{wasted}} = CO_{2_{job}} \times N_{retries} $$ A single flaky job retrying just twice per pipeline, running 20 times a day, wastes: $$ 44g \times 2 \times 20 = 1{,}760g = 1.76 \, kg \, CO_2/day $$ That's over 440 kg CO2 per year — from one flaky test. What's Next for Carbon Tracker Region-aware carbon intensity — use runner location metadata to replace the global \( 475 \, gCO_2/kWh \) constant with location-specific values for higher accuracy Project carbon dashboard — a Wiki page tracking cumulative monthly emissions with trend graphs Carbon budget alerts — notify teams when monthly pipeline emissions exceed a configurable threshold MR carbon diff — predict how a code change affects pipeline emissions before merging Real runner wattage detection — use GitLab runner metadata to get per-runner power draw instead of a fixed constant Weekly carbon digest — Slack or email summary of team-wide pipeline emissions and top savings opportunities <div