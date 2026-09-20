---
slug: "merged-mr-test-code-graph-java-17-additions"
url: "https://devpost.com/software/merged-mr-test-code-graph-java-17-additions"
title: "Merged MR: test(code-graph): Java 17 additions"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 228
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/civic_government"
---

# Merged MR: test(code-graph): Java 17 additions

> On the Contribute Track, I have submitted this merge request !1677 which closed this eligible hackathon issue: #738 on additions towards Java 17 sealed interface and permitted class fixture.

[Devpost](https://devpost.com/software/merged-mr-test-code-graph-java-17-additions) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[civic_government]]

**stack** java, yaml

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for merged mr: test(code-graph): java 17 additions

## Body

What it does The merge request adds integration-test coverage for Java 17 sealed types (JEP 409), which the code indexer previously had no fixtures for. How we built it I cloned the GitLab Orbit community fork locally and made the changes on a new branch in VS Code. Claude Code aided in understanding the gap the indexer has. I baselined the test suite before my change and then made my merge request and applied GitLab Duo's review suggestion. Challenges we ran into A challenge I ran into was finding out where the issue's proposed test diverged from reality: the schema has no IMPLEMENTS edge kind (both inheritance and implementation produce Extends edges), and fixtures must be manually registered in suites.rs, which the issue didn't mention. Accomplishments that we're proud of I am proud I was able to solve the issue with all of the tests passing, and that the work surfaced a real gap now tracked as its own work item. What we learned I learned how the indexer works end to end: tree-sitter parses the AST, language rules extract type names, and a linker resolves them into graph edges. What's next for Merged MR: test(code-graph): Java 17 additions Future work may be done on a gap found after completing the MR. Work item #847 : Java indexer does not extract the permits clause of sealed classes/interfaces <div