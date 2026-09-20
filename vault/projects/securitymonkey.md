---
slug: "securitymonkey"
url: "https://devpost.com/software/securitymonkey"
title: "SecurityMonkey"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 851
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "substrate/code_repository"
---

# SecurityMonkey

> Your AI DevSecOps Team

[Devpost](https://devpost.com/software/securitymonkey) · hackathon [[GitLab AI Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]]
**domain** [[accessibility]] [[health_clinical]] [[security_privacy]]
**substrate** [[code_repository]]

**stack** git, gitlabs, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for securitymonkey

## Body

Issue board - Scanner Monkey Merge Request - Policy Monkey Scan Reports - Policy Monkey Scan Reports - Scanner Monkey Scan Reports - Remediation Monkey Inspiration A green pipeline doesn't mean secure code. We kept seeing teams assume their security was handled because a SAST stage existed in their .gitlab-ci.yml . But in reality, misconfigurations — excluded paths, disabled analyzers, outdated rules, allow_failure: true — create silent blind spots that persist for months. The Uber 2022 breach started with hardcoded credentials that scanners should have caught. Mercedes-Benz leaked a GitHub token for 4 months while their security tools were "running." These weren't tool failures — they were configuration failures. We asked a simple question: "Are our security scanners actually catching what they should?" No existing tool answers this. So we built one, inspired by Netflix's Chaos Engineering philosophy — but applied to security tooling instead of infrastructure. What it does SecurityMonkey is a multi-agent system that automates the full security audit loop: ScannerMonkey — Creates a test branch, injects 15 known vulnerable patterns (SQL injection, XSS, hardcoded secrets, weak crypto), triggers the pipeline, and checks if scanners catch them. Produces a Scanner Confidence Score and raises an issue with the full detection report. PolicyMonkey — Audits GitLab project settings: branch protection, MR approval rules, scanner templates, Dockerfile security. Creates a compliance report and opens fix MRs for critical gaps. TriageMonkey — Reads real pipeline findings, analyzes actual code to classify true vs false positives, assigns priority (P0–P3), resolves the code author from git history, and creates assigned child issues for critical findings. RemediationMonkey — Verifies if merged fixes actually resolved the vulnerability by reading patched code, confirming the vuln pattern is gone, and posting verification comments. Every agent run produces visible GitLab artifacts — issues, merge requests, comments — not just chat responses. How we built it We built SecurityMonkey entirely on the GitLab Duo Agent Platform using Agents, Flows, Skills, and Triggers. Each of the 4 agents is defined as a Duo Agent YAML with a system prompt and a specific toolset (GitLab API tools like create_commit , list_security_findings , create_issue , gitlab_api_get , etc.). The agents are orchestrated in a Duo Flow that chains them in sequence — ScannerMonkey's output feeds into PolicyMonkey, then TriageMonkey, then RemediationMonkey. We used Claude (Anthropic) as the underlying AI model for all agent reasoning — analyzing code, classifying vulnerabilities, generating fix recommendations, and verifying patches. The test payloads cover 10 CWE categories across OWASP Top 10, split into 10 SAST patterns and 5 Secret Detection patterns. Each payload is a minimal Python file with exactly one vulnerability to ensure clean signal. Challenges we ran into Agent system prompt size limits — We initially embedded all 15 payload file contents directly in the agent's system prompt. This made the prompt too large and the agent would silently fail to respond. We fixed this by providing just file paths and CWE descriptions, letting the LLM generate the vulnerable code itself. Getting agents to act, not just suggest — Early versions of our agents would describe what they "would" do instead of actually calling tools. We rewrote all prompts to be imperative ("You MUST create an issue", "Call create_commit") and switched all flow components to AgentComponent for multi-tool reasoning. CWE mismatch in scanner results — GitLab's scanners sometimes classify findings under different CWE IDs than expected. A SQL injection file might get flagged as CWE-943 instead of CWE-89. We handled this by implementing partial match scoring. Pipeline timing — Agents need to wait for CI pipelines to complete before analyzing results. We had to design the flow to handle cases where the pipeline is still running. Accomplishments that we're proud of All 4 agents producing real GitLab artifacts — branches, commits, issues, merge requests, and comments — entirely autonomously The Scanner Confidence Score concept — a single number that tells you how well your security setup actually works Building a multi-agent orchestration flow where each agent's output meaningfully feeds into the next Making the chaos engineering philosophy work for security validation — something we haven't seen done before on GitLab What we learned Multi-agent systems are harder to debug than single agents — when agent 3 fails, is it agent 3's fault or did agent 2 pass bad context? LLM agents need extremely precise prompts to take actions instead of just talking about actions GitLab's Duo Agent Platform is powerful but has undocumented constraints around prompt size and tool call limits Security scanner misconfigurations are far more common than we expected — even our own test project scored only partial matches on basic patterns What's next for SecurityMonkey DAST and Container Scanning support — Expand beyond SAST and Secret Detection to validate all GitLab scanner types Scheduled runs — Trigger SecurityMonkey on a weekly cron to catch configuration drift over time Custom payload packs — Let teams define their own vulnerability patterns specific to their tech stack Cross-project benchmarking — Compare Scanner Confidence Scores across multiple projects in an organization Auto-remediation — Have RemediationMonkey not just verify fixes, but generate and propose code patches automatically <div