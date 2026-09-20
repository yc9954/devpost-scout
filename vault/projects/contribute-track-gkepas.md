---
slug: "contribute-track-gkepas"
url: "https://devpost.com/software/contribute-track-gkepas"
title: "Contribute Track @gkepas"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 89
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/code_repository"
---

# Contribute Track @gkepas

> Contributions to the orbit/knowledge-graph repository.

[Devpost](https://devpost.com/software/contribute-track-gkepas) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**substrate** [[code_repository]]

**stack** bash, rust

## How they structured the write-up

- details
- mr link

## Body

Details The vendored ICON_TYPES list in icon_types.rs had no real drift guard. Introduced a two-layer protection, mirroring the Iglu schema pattern: Build time: config/vendored/system_note_metadata.actions becomes the source of truth (one action per line, pinned SHA in the header). crates/indexer/build.rs generates ICON_TYPES from it, so the Rust constant can't drift from the vendor file, it's derived from it. CI: scripts/check-system-note-actions.sh fetches app/models/system_note_metadata.rb from gitlab-org/gitlab at the pinned SHA and diffs it against the committed vendor file. The new system-note-actions-check lint job runs it on every MR. MR Link https://gitlab.com/gitlab-org/orbit/knowledge-graph/-/merge_requests/1665 <div