---
slug: "gitlab-orbit-knowledge-graph-contributions"
url: "https://devpost.com/software/gitlab-orbit-knowledge-graph-contributions"
title: "GitLab Orbit Knowledge Graph Contributions"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 167
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
---

# GitLab Orbit Knowledge Graph Contributions

> Contributed 5 merged MRs to GitLab Orbit Knowledge Graph: Go test fixtures for generics and special functions, ontology fixes, skill doc improvements, and data model cleanup.

[Devpost](https://devpost.com/software/gitlab-orbit-knowledge-graph-contributions) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[graph_reasoning]]

**stack** gitlab-ci, go, rust, tree-sitter, yaml

## How they structured the write-up

- inspiration
- what i learned
- how i built it
- challenges

## Body

Inspiration I was inspired by the GitLab Transcend Hackathon to contribute to the GitLab Orbit Knowledge Graph — a Rust service that builds a property graph from GitLab data. The project had well-scoped L1 difficulty issues perfect for first-time contributors. What I learned How Go's init() and main() special functions are indexed as graph nodes How FQNs (Fully Qualified Names) work in Go's package-scoped system How tree-sitter based code graph fixtures are structured and validated GitLab's contribution workflow including CI, bot reviews, and rebase conflict resolution How I built it I contributed 5 merged MRs across different areas: Added Go integration test fixtures for generics and special functions Fixed ontology YAML to remove invalid WorkItem states Clarified skill documentation for max_depth vs max_hops Removed stale edge names from the data model docs Challenges Resolving repeated merge conflicts as main branch moved fast during the hackathon Understanding Go's package-scoped FQN behavior vs byte-range-based node identity Passing the strict CI checks including cargo fmt, clippy, and bot reviews <div