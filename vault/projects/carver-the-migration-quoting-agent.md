---
slug: "carver-the-migration-quoting-agent"
url: "https://devpost.com/software/carver-the-migration-quoting-agent"
title: "Carver - The migration-quoting agent"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 522
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "substrate/code_repository"
---

# Carver - The migration-quoting agent

> Carver is a GitLab Duo agent that quotes a legacy migration from your Orbit dependency graph.

[Devpost](https://devpost.com/software/carver-the-migration-quoting-agent) · hackathon [[GitLab Transcend Hackathon]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[supply_logistics]]
  <sub>weak: developer</sub>
**substrate** [[code_repository]]
  <sub>weak: geospatial, web_dom</sub>

**stack** gitlab, javascript, markdown

## Body

Inspiration Every team carrying a legacy app eventually hears "let's migrate it." The next question, what will it cost and where do we start, has no honest answer. People estimate from memory, start with whatever file is easiest, and reach the service everything depends on late, after the plan has already drifted. The estimate slips because the order was a guess. I realized that sequencing and costing a migration are graph problems. The safe order depends on which units carry the most weight in the dependency graph, and GitLab Orbit already is that graph. So I built an agent that answers the question from the graph instead of from memory. What it does Carver is a GitLab Duo agent that quotes a legacy migration end to end. You ask how much, how long, and in what order to migrate a codebase, and Carver: reads the dependency graph from Orbit and ranks every unit by how many others depend on it; returns one compact quote for that codebase: a safe order (lowest-risk first, the load-bearing keystone last), the risks (memory leaks, missing trackBy, weak test coverage), the time and headcount, and the cost two ways: human effort versus AI token generation; refuses to invent numbers. Ask it to price something the graph does not contain and it asks for the real source instead of fabricating a quote. Then it acts. Mention Carver's published flow on an issue and it opens a branch and a single merge request containing a graph-ordered AGENTS.md hand-off file and a sequenced MIGRATION.md checklist. main is never modified. The order is baked in, so a coding agent or a developer runs the migration in dependency-safe sequence instead of guessing. How I built it Agent: a system prompt in the GitLab AI Catalog that encodes the quoting workflow and the discipline to ground every number in Orbit data. Skills: five intent-routed skills (quote, sequence, risk, compare, hand-off) with deliberately distinct descriptions so the right one loads from how the user phrases the request. Profiles: per-stack reference knowledge (AngularJS to Angular, AngularJS to React, Python to Rust, Python 2 to 3) for best practices and risk patterns. Sample app: a real AngularJS 1.x shopfront for Orbit to index, with a load-bearing authService (ten inbound dependents, no tests) and planted risks, an uncleaned $watch, an ng-repeat without track by, a DOM-manipulating directive, so the risk audit has true findings. Flow: an ambient flow on the GitLab Duo Agent Platform that performs the hand-off. It uses Orbit graph tools with a committed dependency-graph.json fallback, and GitLab action tools (create_commit, create_merge_request) to open the branch and the MR. Tests and CI: dependency-free Node checks that validate skill routing and verify the sample-app graph against its manifest, run on every push. Orbit queries are zero-rated, so Carver can traverse the whole graph without spending the token budget it is busy estimating. What's next for Carver Live model pricing so the generation estimate reflects current rates. Deeper live Orbit traversal inside the flow, beyond the committed manifest fallback. More source-to-target profiles. Cross-tool hand-off: mirror the checklist into issues or external trackers when the MR opens. <div