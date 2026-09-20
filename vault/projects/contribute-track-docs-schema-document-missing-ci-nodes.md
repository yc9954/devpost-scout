---
slug: "contribute-track-docs-schema-document-missing-ci-nodes"
url: "https://devpost.com/software/contribute-track-docs-schema-document-missing-ci-nodes"
title: "Contributions to GitLab Orbit codebase"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 166
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# Contributions to GitLab Orbit codebase

> Made contributions to the GitLab Orbit codebase, solving two orbit::hackathon labelled issues.

[Devpost](https://devpost.com/software/contribute-track-docs-schema-document-missing-ci-nodes) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[code_repository]]

**stack** markdown, ruby, rust

## Body

Solved two orbit::hackathon labelled issues: Documented the four CI/CD node types that are indexed and queryable but were missing from the schema reference: Deployment, Environment, JobMetadata, and Runner. Also corrected the total node count from 24 to 28. Before, docs/source/remote/schema.md listed only Pipeline, Stage, and Job under CI/CD, so users couldn't discover the other four entities or build valid queries against them from the docs alone. Properties for each new node were sourced from config/ontology/nodes/ci/{deployment,environment,job_metadata,runner}.yaml . Indexed Ruby lambda and Proc assignments as named Lambda definitions instead of opaque Constant s, so the graph can answer "what callable constants exist?" and "which files reference TRIPLE ?". Before, every constant assignment — MAX = 2 and TRIPLE = ->(x) { x * 3 } alike — was emitted as a generic Constant , and a lowercase handler = ->{} was not indexed at all. Now all four Ruby callable forms (stabby lambda, Lambda block, Proc block, Proc.new ) become Lambda definitions keyed on the LHS name. <div