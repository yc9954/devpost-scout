---
slug: "legendide"
url: "https://devpost.com/software/legendide"
title: "legendIDE"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 482
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# legendIDE

> An AI-powered Web IDE where you can vibe code with your team and share context effortlessly in real time.

[Devpost](https://devpost.com/software/legendide) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: retrieval_grounding, sensor_fusion, structural_withholding</sub>
  <sub>weak: sensor_telemetry</sub>

**stack** claude, coderabbit, elasticsearch, letta, python, react

## Body

Inspiration We’ve all hopped between tabs—editor, terminal, Slack, PR reviews—just to keep teammates in sync. We wanted a place where context travels with the code: live collaboration, AI that remembers decisions, and instant search over what changed and why. What it does legendIDE (aka VibeCode) is a collaborative AI Web IDE that: • Lets teammates live-edit files, chat with AI, and run code in a shared workspace. • Shares context automatically (recent edits, intent, decisions) via Letta so everyone stays aligned. • Runs a review chain: CodeRabbit → Letta context, then stores findings. • Indexes changes in Elasticsearch so you can ask “who changed X and why?” and get instant answers. • Ships with a file explorer, terminal, code editor, AI side panel, and an embeddable live preview tab. How we built it • Backend: FastAPI service orchestrating sessions, Git clone, code-change detection, review pipeline, Letta updates, and Elasticsearch indexing. • AI Context Brain: Letta stores global/team memory (code changes, reviews, decisions) and answers context queries. • Code Review Chain: Tries CodeRabbit first; if unavailable, falls back to a Claude analysis; finally summarizes via Letta. • Search & Telemetry: Elasticsearch indexes every change (who, what, why, snippet) with time filters and aggregations. • Frontend: React app with collaborative editor, tabs, terminal, AI chat panel, live preview, theme toggle, and onboarding. • Dev UX: Auto-save with debounce, “open preview” tab, per-user cursors/colors, quick toggles for terminal & AI chat. Challenges we ran into • Reliable collaboration state across editor/terminal/AI without race conditions. • Context coherence (decisions, reviews, diffs) and making it queryable without noise. • Handling tool fallbacks cleanly when CodeRabbit/Claude aren’t available. • Indexing at the right granularity so search is useful but not spammy. • Keeping latency low while streaming AI responses and updating shared state. Accomplishments that we’re proud of • A smooth “live, shared IDE” feel with instant context—no tab-hopping. • A multi-stage review pipeline that degrades gracefully yet still informs the team. • Ask-the-IDE: natural-language questions answered from Letta + Elasticsearch evidence. • Clean workspace bootstrap (clone → edit → run → preview) with minimal setup. • Thoughtful UX: autosave, user color-coding, theme presets (including a Cal Hacks vibe). What we learned • Teams don’t just need an AI; they need a memory that ties code, reviews, and decisions. • Context capture must be automatic—manual notes never scale. • Search is only useful when tied to why not just what changed. • Fallbacks are essential; resilience > a single best tool. What’s next for legendIDE • WebRTC live sessions for low-latency co-editing and voice/screenshare. • Secure sandboxes (Docker/Firecracker) for per-tab run/build tasks. • PR-aware agent that opens/syncs PRs and posts structured review summaries. • Org-level memory (team/space scoping) + redaction rules for sensitive data. • Vector search across repos/issues/PRs; “jump to the decision” navigations. • Plugin API so teams can add linters, test runners, or custom agents. <div