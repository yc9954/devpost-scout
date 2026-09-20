---
slug: "bus-factor-oracle"
url: "https://devpost.com/software/bus-factor-oracle"
title: "Bus Factor Oracle"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 124
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# Bus Factor Oracle

> Knowledge concentration risk is invisible until a person leaves. This agent tells you which parts of your codebase are only known to one person.

[Devpost](https://devpost.com/software/bus-factor-oracle) · hackathon [[GitLab Transcend Hackathon]]

## Facets

  <sub>weak: graph_reasoning</sub>
**domain** [[developer_tools]]
**substrate** [[code_repository]]

**stack** gitlab

## Body

Problem: Knowledge concentration ("bus factor") risk is invisible — teams don't know which files only one person understands until that person leaves. Solution: Bus Factor Oracle uses the GitLab Orbit knowledge graph to find files/functions touched by only one contributor, enriched with merged_at recency and ImportedSymbol import-graph analysis to surface compounding fragility, then scores and reports the risk. How we built it: Four Orbit query types (aggregation + traversal) across five node domains, validated against the live Orbit API (e.g. discovered count_distinct is unsupported, the 5-node MergeRequestDiffFile join times out at the gateway, old_path is the correct file identifier). Packaged as an AI Catalog agent, a Duo CLI skill, and a flow. What's next: CODEOWNERS auto-suggestions, scheduled drift reports, and per-module documentation-sprint prioritization. <div