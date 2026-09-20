---
slug: "contributor-track-arpit-tripathi"
url: "https://devpost.com/software/contributor-track-arpit-tripathi"
title: "Orbit Compass"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 609
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/graph_reasoning"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Orbit Compass

> From ticket to first commit in seconds. A GitLab Duo Custom Agent that uses Orbit Graph Intelligence to map dependencies, rank codebase hotspots, and prescribe your first code change.

[Devpost](https://devpost.com/software/contributor-track-arpit-tripathi) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[graph_reasoning]] [[on_device_local]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** cli, custom, duo, gitlab, glab, json, markdown

## How they structured the write-up

- inspiration
- how we built it
- mathematical model (hotspot ranking)
- orbit compass automatically filters generated artifacts such as lockfiles and build outputs by assigning them a hotspot score of h(f)=0, ensuring that only actionable source files remain eligible as starting-point recommendations.
- challenges we faced
- what we learned

## Body

Orbit Compass: The Graph-Powered Contribution Strategist Inspiration Every software engineer has experienced the "cold start" onboarding problem. You pick up a bug report or feature request on an unfamiliar project, and the immediate question is: "Where do I start reading?" Traditional keyword search and vector-based codebase retrievers treat the repository as flat collections of text. They completely miss the human and structural context of the software development lifecycle (SDLC). We realized that contribution is not a keyword matching problem—it is a relationship problem . We were inspired to build Orbit Compass : a GitLab Duo Custom Agent that uses the GitLab Orbit Knowledge Graph to trace the relationships between issues, historical merge requests, code dependencies, and active experts, instantly synthesizing a strategic roadmap from ticket to first commit. How We Built It Orbit Compass is built natively on top of the GitLab Custom Agent and AI Catalog ecosystem, integrating directly with GitLab Duo Chat: GitLab Duo Custom Agents : The foundational orchestrator executing the graph traversals. GitLab Orbit Knowledge Graph : The core graph database containing nodes ( WorkItem , MergeRequest , File , Symbol , User ) and edges ( CLOSES , HAS_FILE , IMPORTS , AUTHORED ). Graph Traversals via Query DSL : Structured JSON-based query chains mapping the SDLC relationships. CLI Development : Developed and verified queries locally using the glab CLI ( glab orbit remote query ) against target project environments. Mathematical Model (Hotspot Ranking) To determine where a contributor should start, Orbit Compass calculates a qualitative Hotspot Score, denoted by H(f), for each source file f touched in historical contexts. The score is defined mathematically as: $$ H(f)=\sum_{m\in MR(f)} W(m)\cdot(1+\lambda_{out}(f)) $$ Where: MR(f) is the set of historical Merge Requests that modified file f . W(m) represents the relationship weight of a Merge Request. W(m)=1.0 when the Merge Request has a direct CLOSES relationship to the target issue. W(m)=0.5 when the Merge Request is discovered through the semantic topic-matching fallback. λout(f) represents the Dependency Fan-Out of file f , defined as the total number of outgoing IMPORTS , CALLS , and EXTENDS relationships originating from that file in the Orbit Knowledge Graph. Files with high H(f) represent codebase hotspots that are both historically active and structurally central. Orbit Compass automatically filters generated artifacts such as lockfiles and build outputs by assigning them a hotspot score of H(f)=0, ensuring that only actionable source files remain eligible as starting-point recommendations. Challenges We Faced The Duo Chat Link Resolution Bug : We discovered that standard Markdown shorthand links like #6 or !1 are intercepted by the IDE's Duo Chat UI and incorrectly resolved against the user's currently active workspace project, leading to 404s when investigating remote project history. We resolved this by querying the Project node's full_path property dynamically and forcing the LLM to construct absolute URLs (e.g., https://gitlab.com/{full_path}/-/merge_requests/{id} ). Rendering Constraints in IDE Chat : Early versions used complex HTML layouts and Mermaid diagrams. However, we found that nested HTML tables and diagrams rendered irregularly or got squished in IDE side panels. We pivoted to a clean, flat Markdown layout using simple list elements and a single 3-column table for file hotspot ranking, which renders beautifully across all Duo Chat interfaces. What We Learned Context is King : Code understanding isn't just about reading code; it's about tracing how code changed, who changed it, and why. Utilizing a knowledge graph makes this context accessible to LLMs without requiring huge context window loads. Deterministic Safety Safeguards : Custom agents perform best when given strict boundary constraints, such as explicit rules on what constitutes a "Starting File Candidate" (e.g. banning package-lock.json ), ensuring recommendations are highly actionable. <div