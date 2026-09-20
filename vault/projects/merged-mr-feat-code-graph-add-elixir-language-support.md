---
slug: "merged-mr-feat-code-graph-add-elixir-language-support"
url: "https://devpost.com/software/merged-mr-feat-code-graph-add-elixir-language-support"
title: "Merged MR: feat(code-graph): add Elixir language support"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 468
team_size: 1
has_repo: true
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
---

# Merged MR: feat(code-graph): add Elixir language support

> On the Contribute Track, I have submitted this merge request !1694 which closed this eligible hackathon issue: #766 on adding Elixir language support to the v2 code indexer.

[Devpost](https://devpost.com/software/merged-mr-feat-code-graph-add-elixir-language-support) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[graph_reasoning]] [[on_device_local]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** elixir, rust, tree-sitter

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for merged mr: feat(code-graph): adding elixir language support

## Body

What it does The merge request adds Elixir language support to the GitLab Knowledge Graph (Orbit) v2 code indexer. Before this change, .ex and .exs files were skipped entirely. Now the indexer extracts module and function definitions, alias/import/use/require imports, and resolves function calls across files into the property graph, so Knowledge Graph queries work on Elixir codebases. How we built it I cloned the Orbit community fork locally and worked on a new branch following the repo's adding-a-language guide. Elixir's tree-sitter grammar is unusual because every construct parses as a call node, so, instead of matching node kinds like other languages, the rules dispatch on the call's target text using when(...) predicates, with a hook for the import forms. Before writing any rules, I verified the grammar's real shapes against tree-sitter-elixir 0.3.5 by dumping ASTs of sample Elixir code locally. I also used AI agents to explore the indexer's rule engine and to adversarially review my diff, which caught two real bugs my tests had missed before any human reviewer saw them. Challenges we ran into The issue was flagged as the hardest of the five new-language issues, and the grammar earned it. Arguments looks like a tree-sitter field on call nodes but is actually a plain child, so the obvious extraction silently returns nothing. Bare struct field access like user.name parses identically to a zero-arity remote function call, which initially produced phantom call edges. Function definition heads are themselves call nodes, so every def greet(name) emitted a fake reference to itself until I added exclusions. On top of that, another language (Bash) merged into main while my MR was in review, so I had to resolve a merge conflict in the docs. Finally, keeping scope discipline was its own challenge: I cut my diff roughly in half to match the acceptance criteria exactly and saved the extras for follow-ups. Accomplishments that we're proud of The MR merged with an approving review and zero blocking comments. I'm proud of shipping the indexer's 14th language end-to-end with 8 unit tests plus 3 integration fixture suites with exact-count assertions that guard against over-extraction, and correctness guards (field access vs. calls, special forms, def heads) that were each verified against real parsed code rather than assumptions. What we learned I learned to verify a grammar against real ASTs before trusting documentation or intuition, and to read the engine code before writing rules for it: two of the trickiest bugs came from plausible assumptions that the parse tree quietly violated. I also learned that a smaller, criteria-exact diff is genuinely easier to review, and that deferred scope isn't lost work if you write it down. What's next for Merged MR: feat(code-graph): adding Elixir language support The maintainer requested a follow-up issue for the remaining coverage gaps, which I've drafted at https://gitlab.com/gitlab-org/orbit/knowledge-graph/-/work_items/857 <div