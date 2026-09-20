---
slug: "docuguard"
url: "https://devpost.com/software/docuguard"
title: "RepoWarden"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 1245
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# RepoWarden

> The first AI that captures why code was written, not just what it does. A Living Specification that grows smarter with every merge.

[Devpost](https://devpost.com/software/docuguard) · hackathon [[GitLab AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[security_privacy]]
**user** [[developer]] [[legal_professional]]
**substrate** [[code_repository]] [[geospatial]]

**stack** anthropic-claude, gitlab, gitlab-ci/cd, gitlab-duo-agent-platform, markdown, restapi, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next

## Body

RepoWarden - Devpost Submission Inspiration In 1996, Linus Torvalds created Git to track what code changed and who changed it. In thirty years, nobody built what comes next. I kept running into the same problem on every team I worked with. A senior engineer would spend weeks making critical decisions - why a fraud threshold was set at 30%, why a webhook function used constant-time comparison instead of simple equality, why a particular status distinction existed that downstream systems depended on. Then they'd leave. The code stayed. The reasoning didn't. Six months later, a new developer would see something that looked overcomplicated. Simplify it. And silently reopen a vulnerability that was already exploited in staging. This isn't a documentation problem. It isn't a security problem. It's a deeper problem that nobody has solved in 70 years of software engineering: software is the only engineering discipline where the blueprint and the artifact are the same object. When the bridge breaks, the blueprint breaks with it. Nobody knows what the bridge was supposed to look like. I wanted to build the blueprint that exists independently of the bridge. What It Does RepoWarden is the first Living Specification Engine - an AI system that captures why code was written, not just what it does. Every time a merge request is merged, RepoWarden reads everything - the diff, the MR description, the issue discussions, the review comments - and extracts five layers of institutional knowledge: Intent - What problem was the developer solving? What behavior did they explicitly intend? Contracts - What does this code promise? What inputs does it accept, what outputs does it guarantee, what will it never do? Decisions - What architectural choices were made and why? What alternatives were rejected? What constraints drove the chosen approach? Dangers - What could go wrong? What has already broken? What must future developers never do? Evolution - How does this change fit the trajectory of the codebase? What is this system becoming? These five layers are written automatically to a SPEC/ directory - a living specification that grows smarter with every commit. This specification then powers eight flows: Documentation Guard - After every merge, analyzes the changed code and opens an MR with complete docstrings written from the specification context. No human intervention required. Specification Guardian - Before any MR merges, validates it against the living specification. Catches intent violations, contract breaks, and danger pattern recurrences before they ship. In our demo, it caught a timing attack vulnerability (SEC-2024-441) being silently reintroduced - citing the exact specification entry, the original incident reference, and the precise reasoning from the developer who originally fixed it. Specification Oracle - Answers any question about the codebase from the living specification. "Why does this function use hmac.compare_digest instead of == ?" Answer: HIGH CONFIDENCE, sourced directly from the specification, citing the MR number, the date, and the 16,000-request attack vector that motivated the decision. Specification Drift Reporter - Weekly analysis comparing the current codebase against the specification. Scores each component 0–100. Flags orphaned knowledge - code where the original decision-makers have all left and nobody knows why it works the way it does. Security Guard - Explains vulnerabilities in plain English and opens auto-fix MRs for critical issues. Health Reporter - Weekly repository health score across documentation coverage, security posture, and specification alignment. Specification Onboarding - Generates a completely personalized onboarding guide from the living specification. Turns six months of learning into six days. How We Built It RepoWarden is built entirely on the GitLab Duo Agent Platform using custom YAML flows and system-prompted agents powered by Anthropic Claude. The architecture is nine agents organized into eight flows. Each flow defines agent components, their toolsets, their system prompts, and the routing between them. The agents use GitLab's built-in tools - get_merge_request , list_repository_tree , read_file , find_files , gitlab_blob_search , create_file_with_contents , create_commit , create_merge_request , and create_issue_note - to interact with the repository without any external infrastructure. The entire system runs on GitLab's platform compute. No servers. No local setup. No API keys to manage. No external dependencies. The most critical engineering work was the system prompts. Getting Claude to reliably extract structured institutional knowledge from unstructured MR discussions required significant iteration. The key insight was that Claude needed to be prompted to extract intent - not just what the code does, but what the developer meant it to do - and that these are fundamentally different things. The gap between them is where all bugs live. The second key insight was the specification format itself. The five-layer structure (intent, contracts, decisions, dangers, evolution) mirrors how senior engineers actually think about code. It's not arbitrary - it's the mental model that separates engineers who can safely modify any part of a system from engineers who are afraid to touch anything. Challenges We Ran Into Persistent memory on a stateless platform. The GitLab Duo Agent Platform has no persistent state between sessions. Every agent run starts fresh. The solution was the SPEC/ directory itself - the living specification is the memory. Every agent reads it before acting and writes to it after. The specification becomes the shared context that makes every subsequent run smarter than the last. Committing directly to main. The platform's create_commit tool behaves differently depending on whether a branch already exists. When creating new files on a non-existent branch, the tool works correctly. When updating existing files, direct commits to protected branches require careful parameter handling. The Documentation Guard flow required multiple iterations to reliably create branches and open MRs that judges could review and merge. Extracting intent from incomplete context. Not every MR description is rich with reasoning. When developers write "fix bug" or "update function," there is little to extract. The solution was training the agents to infer intent from the code itself when the MR description is sparse, and to explicitly flag inferred entries so future developers know to confirm them. Distinguishing intentional evolution from accidental violation. The Specification Guardian needed to understand that not every change that contradicts the specification is wrong - sometimes the specification itself needs to evolve. Getting Claude to reliably distinguish "this developer is intentionally changing the architecture" from "this developer doesn't know what they're breaking" required careful prompt design around evidence of deliberateness: does the MR description mention the change? Does it reference the existing specification? Does it provide justification? What We Learned The most important lesson: Claude's ability to read ambiguous human communication and synthesize structured meaning is not a parlor trick. It is genuinely load-bearing infrastructure. Every flow in RepoWarden depends on Claude understanding what developers meant from what they wrote - and these are rarely the same thing. The second lesson: the best AI applications are not chat interfaces. They are systems that watch, remember, and act - invisibly, automatically, and with increasing accuracy over time. RepoWarden does not ask developers to change their workflow. It watches the workflow they already have and makes it smarter. What's Next The living specification is just the beginning. Future directions include real-time blast radius prediction before merge, cross-repository specification sharing for microservice architectures, and automatic ADR generation that feeds directly into architecture review processes. But the core insight stands regardless of what gets built next: software engineering has been missing its blueprint layer for seventy years. The tools to build it now exist. RepoWarden is the first demonstration that it works. "Your code remembers what it does. RepoWarden remembers why." <div