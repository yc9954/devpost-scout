---
slug: "lore-living-organizational-record-engine"
url: "https://devpost.com/software/lore-living-organizational-record-engine"
title: "LORE - Living Organizational Record Engine"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 1335
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/multi_agent"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# LORE - Living Organizational Record Engine

> MR decisions get lost. LORE gives your codebase memory, captures review decisions, predicts failures, enforces feedback, and stops repeated mistakes. 8 agents, 5-layer MR review, 43 tests

[Devpost](https://devpost.com/software/lore-living-organizational-record-engine) · hackathon [[GitLab AI Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[multi_agent]] [[revocation_withdrawal]]
**domain** [[developer_tools]] [[health_clinical]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[web_dom]]

**stack** agent, anthropic, ci/cd, claude, duo, gitlab, mermaid.js, pages, platform, python

## How they structured the write-up

- inspiration
- what it does
- the pre-mortem — predicting failures before code exists
- the five-layer mr review
- key features
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for lore

## Body

Architecture Diagram : LORE - Multi Agent Router Architecture Architecture Diagram : LORE: Memory System - How Decisions are stored and enforced Architecture Diagram : LORE - Lifecycle from Issue to Onboarding Architecture Diagram : LORE - 5 Layer MR review 5-layer MR review - comment by teammate 5-layer MR review comment - LORE started 5-layer MR review comment - LORE using past memories to identify issues Pre-mortem on the issue -page1 Pre-mortem on the issue -page2( LORE using past memories) Pre-mortem on the issue-page3 ( LORE using past memories) Pre-mortem on the issue -page4 ( making an acceptance criteria for a good task) Pre-mortem on the issue -page 5 - ( LORE reminding of all memories/issues till now that could be related) Teammate replying to LORE, LORE using that to rethink LORE Memory Index stored in wiki LORE ask and LORE Migrate Agents LORE - Dashboard Summary LORE - Decision Graph LORE - Carbon Impact & File Coverage Map LORE - Security Inventory and Code pattern Rules LORE - Memory Details Terminal with 43 tests passing LORE - Living Organisational Record Engine Your codebase remembers. Even when your team forgets. Inspiration Here's a story every developer knows. September 2025. Auth service goes down. Two hours. Someone cached auth tokens in Redis. Password resets didn't invalidate the cache. Users authenticated with revoked credentials for 120 minutes. The team debates, argues, learns. The decision: "Never cache auth responses." It gets written in a comment on MR !42. Everyone agrees. Everyone moves on. Six months later, a new developer joins. She opens an issue: "Add Redis caching to auth." Nobody remembers September. Nobody remembers MR !42. She ships the same bug. We've been on these teams. We've watched the same decisions get made, forgotten, and repeated. Not because anyone was careless - because decisions live in MR threads nobody will ever reopen, in the heads of engineers who've already left. Every "Architecture Decision Record" tool requires someone to manually write things down. Nobody does. So we built LORE. What It Does LORE is a multi-agent system on the GitLab Duo Agent Platform that gives your codebase institutional memory. It follows features from issue to production and gets smarter with every merge. Your team's situation What LORE does Developer creates an issue Searches past failures, generates pre-mortem + full engineering spec Developer answers LORE's questions Evaluates answers, assigns risk level, records every promise MR opened 5-layer review: memory conflicts, promise check, security, code intelligence, pattern enforcement Developer responds to conflict Three options: override with reasoning, revert, or discuss with original decision makers MR merged Extracts decisions from code AND comments, captures reviewer rules, generates changelog Commit pushed Structured ledger entry: files changed, domains, breaking risk Team wants a health check Decision health, carbon metrics, security inventory, dependency graph New developer joins Complete onboarding briefing: security first, past incidents, key people Anyone has a question @mention LORE Ask: "What decisions govern auth?" — answers from memory Project adopts LORE LORE Migrate scans past MRs, imports decisions retroactively The Pre-Mortem — Predicting Failures Before Code Exists A developer creates an issue. LORE searches the entire project history, finds past incidents, and generates a pre-mortem with hard questions and a full engineering spec: "When you implement bcrypt, you'll be tempted to cache the hash comparison for performance. Don't. This team learned the hard way." That's not a template. That's Anthropic Claude reasoning about your team's specific history. The Five-Layer MR Review Every MR gets five layers of analysis in a single comment: Memory Conflicts : Semantic analysis against stored decisions. LORE recognizes that "in-memory dict caching" IS "Redis caching on auth tokens" because the failure mode is identical. Not keyword matching — reasoning about equivalence. Promise Verification : "You said 30-second TTL on the issue. Your code says 30 minutes. That's 60x longer than promised." Security Sentinel : SQL injection, MD5 for passwords, eval on untrusted data. Cross-referenced against past security decisions. Code Intelligence : New dependencies, architectural patterns, technology drift detected from the actual diff. Pattern Enforcement : A past reviewer said "don't use Optional." LORE captured it as a rule. Every future MR is checked. Reviewers never repeat themselves. Then three options: lore: intentional (override with reasoning), lore: accidental (fix the code), or lore: discuss (bring in the original decision makers). Key Features Memory Evolution When a developer overrides a decision, LORE updates the memory, and then checks whether the code matches the new commitments. "You promised bcrypt, but line 37 is still MD5." Your commitments become institutional memory. Living, evolving, accountable. Conversational Search @mention LORE Ask: "What decisions govern authentication?" It answers like a teammate who was there - specific decisions, dates, people, reasoning. Onboarding New developer? LORE generates a complete briefing: security decisions first, architecture by file, past incidents, key people table, recent changelog. Cold-Start Import LORE Migrate scans past MRs and imports decisions retroactively. One command, instant institutional memory. Visual Dashboard lore dashboard generates a self-contained HTML page with Mermaid.js decision graphs, carbon impact tables, security inventory, and file coverage maps. How We Built It Multi-Agent Router Architecture on GitLab Duo. A triage router classifies context and dispatches to one of eight specialized agents: Agent Trigger Purpose Pre-Mortem Issue assigned Failure prediction + spec Follow-Up Developer replies Evaluates answers, tracks promises MR Review MR opened 5-layer analysis Reply Handler lore: command Memory evolution Decision Extractor MR merged Decisions + patterns + changelog Health Auditor "health audit" Carbon, security, dependency graph Onboarding "onboard" New member briefing Commit Keeper Push event Commit ledger Plus two standalone agents: LORE Ask (conversational search) and LORE Migrate (retroactive import). Python CLI ( lore-cli ) with four commands: lore validate : format checking, dependency integrity, circular dependency detection (DFS) lore stats : JSON: memory counts, carbon totals, security inventory lore sync : reads memories from issues, writes wiki pages, builds LORE-INDEX lore dashboard : HTML with Mermaid.js graphs, carbon tables, security inventory 43 passing tests. Validation logic, carbon math, dependency graph traversal, dashboard generation. CI/CD Pipeline - YAML validation, 64 KiB catalog size enforcement, pytest, AI Catalog sync on tags, memory sync, GitLab Pages deployment. Anthropic Claude powers every agent. This isn't "plug in any LLM": Semantic equivalence - recognizes in-memory caching IS the same pattern as Redis caching Promise verification - reads issue commitments, checks code line-by-line Decision vs noise - distinguishes "we chose X because Y" from "LGTM" Security regression - understands when a "simpler" auth check is not equivalent Voice - speaks as a senior engineer who has seen things break. Developers actually read warnings with personality. Challenges We Ran Into GitLab auto-links #N to issues - LORE writes "Memory #1" but GitLab turns it into an issue link. Fixed by switching to LORE-MEMORY-001 format. Duo agents can't write to wiki - LORE reads from wiki, writes to issues. Built lore sync CLI to bridge the gap. 64 KiB catalog limit - Full prompts are 87 KiB. Condensed to 31 KiB for catalog, full version runs internally. CI validates size on every push. Consistent persona across 8 agents - "Slightly haunted senior engineer" voice took iteration, but it makes warnings effective. Accomplishments We're Proud Of Semantic analysis that catches pattern equivalence, not just keywords Promise verification that holds developers to their own words Reviewer corrections that become permanent, automatically enforced rules Memory evolution with accountability - "you promised bcrypt, line 37 is still MD5" 43 tests in a hackathon 10 agents, one coherent system What We Learned Most architectural decisions are never discussed- someone just writes the code. If you only capture from discussions, you miss 80%. Personality makes agents effective. "I won't block this merge. But I won't forget you saw this." gets read. "3 potential issues found" doesn't. Carbon tracking needs honest methodology over precise numbers you can't defend. What's Next for LORE Wiki write access when Duo supports it Cross-project memory sharing IDE integration : surface memories while coding Memory confidence decay over time Real carbon measurement via cloud provider APIs LORE Ask in Slack/Teams <div