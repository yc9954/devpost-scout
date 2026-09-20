---
slug: "hardening-gitlab-orbit-schema-docs-code-graph-tests"
url: "https://devpost.com/software/hardening-gitlab-orbit-schema-docs-code-graph-tests"
title: "Hardening GitLab Orbit: schema, docs & code-graph tests"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 479
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/code_repository"
---

# Hardening GitLab Orbit: schema, docs & code-graph tests

> Three merged MRs that keep Orbit's context truthful - ontology schema guardrails and code-graph test coverage - plus a real data-loss bug discovered, filed, and informing the indexer's redesign.

[Devpost](https://devpost.com/software/hardening-gitlab-orbit-schema-docs-code-graph-tests) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[supply_logistics]]
  <sub>weak: developer_tools</sub>
**user** [[developer]]
**substrate** [[code_repository]]

**stack** cargo-nextest, ci/cd, clickhouse, gitlab, go, json, markdownlint, rust, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Inspiration GitLab Orbit's promise is giving AI real context - which only works if the ontology, its docs, and the code indexer can be trusted. I picked hackathon issues that attack one theme from different angles: keeping Orbit's structured context truthful. What it does Schema guardrails (2 merged MRs). The ontology JSON schema allowed node properties without descriptions, and allowed enum-style values: mappings on non-enum types (exactly how Job.when was once mistyped). Both gaps are now closed: CI rejects either mistake at validation time. Code-graph test coverage (1 merged MR). A negative-assertion fixture proving Rust closures are intentionally NOT extracted as Definition nodes - a documented ra_ap_hir limitation that previously had no regression guard. The fixture pins the complete Definition set, so an accidentally extracted closure fails the test no matter what synthetic name it lands under. A real bug, found and fixed. While building a Go fixture for init() functions, I discovered that multiple init() in one file collide on the FQN main.init - under ClickHouse's ReplacingMergeTree dedup, all but one silently vanish from the graph. I filed it (issue #843), then implemented an opt-in disambiguation fix with ordinal suffixes ( main.init , main.init#2 ), designed so overload-capable languages (C++, Java, Kotlin) keep their legitimate shared FQNs - the full 181-test suite passed with zero fixture changes. The maintainers are folding the limitation into a planned DSL rework, with #843 as a concrete case it must cover. How we built it Each issue shipped as its own conventional-commit MR through the community fork, validated locally before submission: jsonschema positive AND negative tests over all 90 ontology files, and cargo-nextest runs of every new fixture. All merged MRs passed the full 31-job CI suite. Challenges we ran into The issue specs contained traps documented nowhere: the suggested row_count_gte assertion doesn't exist in the test harness, fixtures silently never run unless registered in tests/suites.rs , and Rust fixtures need a Cargo.toml for manifest resolution. Each correction is documented in the MRs. Review feedback became a feature: when the AI review bot suggested hardening my closure fixture's negative assertion, I verified and adopted it within the hour - and pushed back with evidence on its second suggestion (rustfmt disagreed with the bot's cosmetic advice). Accomplishments that we're proud of First MR merged within hours of the hackathon opening. Three merged MRs across two subsystems. One genuine data-loss bug discovered through test-writing and now shaping the indexer's redesign. What we learned How Orbit's ontology drives everything from ClickHouse DDL to query validation, how the code-graph indexer extracts definitions via tree-sitter and ra_ap_hir, and how strict JSON-schema conditionals (if/then) can encode semantic rules - plus the practical craft of getting community MRs through GitLab's review machinery fast. What's next Following the DSL rework that will resolve #843, and continuing to contribute to Orbit's ontology tooling and code-graph test coverage beyond the hackathon. <div