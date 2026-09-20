---
slug: "gitlab-orbit-code-graph-test-fixtures"
url: "https://devpost.com/software/gitlab-orbit-code-graph-test-fixtures"
title: "GitLab Orbit code-graph test fixtures"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 355
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# GitLab Orbit code-graph test fixtures

> A focused integration fixture that locks in GitLab Orbit's code-graph extraction for C# structs, so regressions can't slip through CI unnoticed.

[Devpost](https://devpost.com/software/gitlab-orbit-code-graph-test-fixtures) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** gitlab, rust, yaml-test-fixtures

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gitlab orbit code-graph test fixtures

## Body

Inspiration GitLab Orbit gives AI the structured context it needs to understand a codebase — but that context is only trustworthy if the indexer's extraction behavior is well-tested. Several common language constructs had no focused test coverage, so a regression could slip through CI unnoticed. C# structs were one of those gaps. What it does It adds an integration test fixture that feeds representative C# struct source to GitLab Orbit's code-graph indexer and asserts the resulting graph: the struct is extracted as Struct , its constructor as Constructor , its auto-properties as Property , its methods as Method , and the Defines / FileToDefinition containment edges are emitted correctly. If a future change breaks C# struct extraction, CI now fails instead of silently degrading. How we built it A single YAML fixture plus its one-line registration in the integration-test suite. We studied the indexer's actual conventions in crates/code-graph/src/v2/ , wrote representative C# source, and asserted exactly what the indexer produces. Every assertion was run against the real indexer locally before opening the merge request. Challenges we ran into Making every assertion reflect the indexer's real output rather than assumptions. For example, the indexer does not emit Field definitions for bare C# struct fields, so naive assertions would have failed CI. We verified behavior empirically and asserted auto-properties (which the indexer does extract) instead. Accomplishments that we're proud of The fixture passes against the real indexer (the full code-graph integration suite is green). It was reviewed and approved by GitLab maintainers (@dgruzd and @jgdoyon1), labeled orbit::hackathon , and merged before the deadline — a clean, minimal, genuinely useful addition to Orbit's test coverage. What we learned GitLab Orbit's v2 code-graph edge-kind and definition-type conventions, and the discipline of pinning only behavior the indexer actually produces. (This contribution was created with AI assistance, disclosed in the merge request.) What's next for GitLab Orbit code-graph test fixtures Extending the same approach to the documented gaps — e.g. asserting field definitions for bare struct fields once supported — and adding parallel fixtures for other languages and constructs (enums, records, sealed hierarchies) to broaden the indexer's regression safety net. <div