---
slug: "bugflow-ai-regression-detective-ci-optimizer"
url: "https://devpost.com/software/bugflow-ai-regression-detective-ci-optimizer"
title: "BugFlow: AI Regression Detective & CI Optimizer"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 1228
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/security_privacy"
  - "user/developer"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# BugFlow: AI Regression Detective & CI Optimizer

> Report one bug. Get ten fixes, sixty-three tests, and a faster pipeline - all from one @mention.

[Devpost](https://devpost.com/software/bugflow-ai-regression-detective-ci-optimizer) · hackathon [[GitLab AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]] [[security_privacy]]
**user** [[developer]] [[researcher]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[video_visual]]

**stack** ci/cd, claude, gitlab, go, javascript, python, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bugflow: ai regression detective & ci optimizer

## Body

the wow moment - 9 sibling bugs fixes with Before/After Test Verification Matrix CI savings Inspiration Every engineer has lived this story: a bug gets reported, you spend hours investigating, you fix it, and you ship. But three weeks later, another bug surfaces from the same code change. Then another. Then another. Each one triggers a separate investigation cycle. We discovered this pattern has a name sibling bugs - first identified in Liang et al., ESEC/FSE 2013 . When a code change introduces one bug, it almost certainly introduces others. But no existing tool proactively looks for them. GitHub Copilot fixes what you assign it. Devin and SWE-agent work on one task at a time. Code review tools like CodeRabbit catch bugs before merge, not after. BugFlow fills the gap that exists after code is merged and bugs are in production . What it does BugFlow is a 5-agent, 2-flow AI system on the GitLab Duo Agent Platform. Flow 1: Regression Detective Pipeline (4 agents): One @mention on a bug report triggers an autonomous pipeline: Detective traces the bug to the exact MR/commit that introduced it Hunter scans that MR for hidden sibling bugs (found 9 including 5 CRITICAL security vulnerabilities in our showcase) Fixer generates code fixes for ALL bugs with Before/After verification Guardian creates regression tests with a Test Verification Matrix Result: 1 bug reported → 10 bugs found → 10 fixes → 63 tests → 2 merge requests → 20 minutes → zero human effort. Flow 2: Green CI Optimizer: A separate agent that analyzes CI/CD configuration and eliminates compute waste. Reduced docs-only pipeline runs from 28 minutes to 1 minute (96% faster). Saves ~4,800 compute minutes monthly for a team of 8. How we built it BugFlow is built entirely as YAML agent and flow configurations on the GitLab Duo Agent Platform, powered by Anthropic Claude. No external infrastructure, no API keys, no servers, just @mention and go. The agents communicate through structured comments on GitLab issues. Each agent produces parseable fields ( ROOT_CAUSE_MR , HUNTER_VERDICT , FIXER_STATUS , GUARDIAN_STATUS ) that downstream agents consume. This structured protocol enables reliable multi-agent orchestration where each agent reads the previous agent's output and decides whether to proceed, halt, or skip. Key engineering decisions: Semantic deduplication : The Hunter uses Claude's natural language understanding to detect that "null items" and "missing item fields" in the same function describe the same bug, achieving 100% dedup accuracy across all tests Before/After verification : The Fixer doesn't just generate patches, it simulates code execution step-by-step to prove each fix is correct Confidence-tiered analysis : HIGH/MEDIUM/LOW findings with different actions per tier to maintain signal-to-noise ratio Re-run protection : Every agent checks for existing analysis before starting, preventing duplicate work We tested across Python (SaaS platform), JavaScript (e-commerce API), and Go with Chinese comments (task management API) - proving cross-lingual capability with zero language-specific configuration. Challenges we ran into Agent communication : GitLab Duo agents can't directly call each other. We designed a structured comment protocol where each agent reads the issue's comment thread to find the previous agent's output. This required careful formatting with parseable fields. Deduplication at scale : When the Hunter re-runs on a codebase where sibling bugs already exist, it must not create duplicates. We implemented a file::function mapping system with semantic overlap detection that achieved 100% accuracy. Branch conflicts : When Fixer and Guardian create MRs, branches may already exist from prior runs. We built automatic variant naming (-v2, -v3) to handle this gracefully. Platform limitations : We originally planned a BigQuery analytics integration but discovered that platform agents can only use GitLab's built-in tools, no external MCP servers. We pivoted to storing analytics as committed JSON files instead. Agent timeout management : The 600-second timeout required careful prompt engineering to ensure agents complete their work within limits, especially the Hunter scanning large diffs. Accomplishments that we're proud of 1 bug → 10 bugs → 10 fixes → 63 tests in 20 minutes : Our showcase run on a realistic SaaS billing platform discovered 9 hidden sibling bugs (including 5 CRITICAL security vulnerabilities) from a single bug report, all autonomously 100% duplicate detection accuracy : Across every test JavaScript re-runs, Go re-runs, cross-MR dedup, the Hunter never created a single false duplicate Before/After verification : The Fixer doesn't just patch code it shows engineers the exact input, buggy output, and fixed output with real values so they can verify every fix before merging Cross-lingual code analysis : BugFlow successfully traced bugs through a Go codebase with Chinese comments (中文注释) with zero language-specific configuration 5 agents, 2 flows, zero infrastructure : Everything runs natively on GitLab through YAML configurations. No servers, no Docker containers, no API keys. One @mention starts the entire pipeline Debunked the developer's justification : In our showcase, the Detective didn't just find the root cause — it analyzed the commit message claiming "the payment gateway handles validation" and explained why that assumption was dangerous. That's not pattern matching, that's reasoning Concrete sustainability impact : The Green CI Optimizer doesn't just claim to be green, it measures waste per pipeline pattern, calculates CO2 reduction using cited IEA data (228-684 kg CO2 per project per year), and generates the fix as a ready-to-merge MR What we learned Multi-agent orchestration through structured protocols works : The key insight was making each agent's output parseable with consistent fields (ROOT_CAUSE_MR, HUNTER_VERDICT, FIXER_STATUS). This turns unreliable LLM output into a reliable pipeline Semantic reasoning unlocks capabilities impossible with rules : Deduplication, cross-lingual analysis, code behavior simulation, and confidence calibration all depend on Claude's ability to reason about meaning, not just match patterns The "iceberg bug" problem is universal : Every engineer we described BugFlow to immediately recognized the problem. The academic research (Liang et al., 2013) validated what practitioners have felt for years Edge cases define production quality : Re-run protection, branch conflict handling, HALT/PROCEED routing, and graceful degradation on timeout these aren't features, they're the difference between a demo and a tool Platform constraints drive creativity : When we discovered agents can't call external services, we pivoted to a structured comment protocol and committed analytics as JSON files. The constraint made the architecture simpler and more portable Presentation is half the score : A clean repo, consistent screenshots, honest competitive analysis, and a focused demo video transformed BugFlow from a strong engineering project into a compelling submission What's next for BugFlow: AI Regression Detective & CI Optimizer CI test execution : Integrate generated tests into the CI pipeline so they automatically run verifying they fail on buggy code and pass on fixed code, before the Guardian's MR is approved HALT override mechanism : Allow engineers to force the pipeline to continue when the Detective incorrectly halts, with a simple reply command like @bugflow --override proceed Risk intelligence dashboard : Accumulate analytics from BugFlow runs across a project to identify which files are most regression-prone and which developers' MRs most frequently introduce sibling bugs Cross-MR correlation : Detect emergent bugs caused by the interaction of multiple MRs over time, the next frontier beyond single-MR traceability Configurable confidence thresholds : Let teams set their own HIGH/MEDIUM/LOW thresholds for issue creation based on their risk tolerance Production deployment : Package BugFlow as a reusable GitLab CI/CD component that any team can add to their project with a single include statement <div