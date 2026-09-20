---
slug: "reverie-y01r96"
url: "https://devpost.com/software/reverie-y01r96"
title: "Reverie"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 748
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/media_journalism"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/transcript_audio"
---

# Reverie

> Conversations end. Memories shouldn’t.

[Devpost](https://devpost.com/software/reverie-y01r96) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[provenance_signing]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[education]] [[media_journalism]]
**user** [[educator_student]] [[general_public]]
**substrate** [[code_repository]] [[financial_record]] [[transcript_audio]]
  <sub>weak: web_dom</sub>

**stack** ai, css, docker, html, python, qwen, react, shell, typescript

## How they structured the write-up

- 🧠 inspiration
- ✨ what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 📊 accomplishments
- 💡 what we learned
- 🚀 what’s next

## Body

Architectural Diagram Reverie — A visible memory engine for AI agents Conversations end. Memories shouldn’t. 🧠 Inspiration AI assistants can already retain preferences and summarize prior conversations. The harder problem is making that memory trustworthy, current, efficient, and inspectable . Where did a remembered claim come from? What happens when the user corrects it? How does stale information stop influencing future responses? Why was one memory retrieved while another was ignored? Reverie treats memory as a lifecycle: observe → consolidate → forget → recall Rather than replaying every conversation, it extracts useful signals, strengthens what remains valuable, lets outdated information fade, and retrieves only what the current moment requires. ✨ What it does Reverie is a subject-agnostic memory engine for agents that interact with the same person across multiple sessions. It converts conversations into typed memories such as preferences, goals, facts, affect, misconceptions, mastery, and strategy outcomes. Every memory includes confidence, importance, strength, timestamps, subject tags, and the exact source evidence that produced it. No quote, no memory. Unsupported candidates are rejected before storage, preventing plausible but ungrounded memories from entering the system. Between sessions, Reverie runs a consolidation cycle—or “dream.” New evidence is compared with existing memory to determine what should be reinforced, distilled, deduplicated, reconciled, superseded, or allowed to decay. The model may propose these operations, but it cannot directly rewrite memory. Deterministic validation checks each proposal before committing it to the memory ledger. When a new session begins, memories compete for a fixed 1,200-token context budget based on semantic relevance, strength, recency, importance, and memory type. Only the memories that earn their place enter the assistant’s working context. The interface exposes this entire lifecycle. Users can inspect the memory graph, open provenance receipts, watch consolidation happen, see memories strengthen or fade, and understand why something was recalled. 🛠️ How we built it Each Qwen Cloud model has a distinct responsibility: Role Qwen model Conversation qwen-plus Memory observation and extraction qwen-flash Consolidation and evaluation qwen-max Semantic retrieval text-embedding-v4 All model calls use the DashScope OpenAI-compatible API on Qwen Cloud. The FastAPI backend separates model reasoning from deterministic state management. SQLite stores typed engrams, embedding vectors, provenance links, lifecycle state, consolidation events, and retrieval events. The Next.js frontend renders the memory graph, source evidence, consolidation operations, retrieval decisions, and token-budget usage directly from backend state. The complete stack—Next.js, FastAPI, Nginx, SQLite, and live DashScope connectivity—was deployed on Alibaba Cloud ECS. Reverie’s memory engine contains no scenario-specific logic. Subject vocabulary is isolated behind a replaceable subject layer, allowing the same engine to support tutoring, coaching, productivity agents, and other long-running applications. 🚧 Challenges we ran into Keeping memory grounded Models can generate reasonable-sounding memories that were never supported by the conversation. Reverie requires substantive source evidence from the current exchange and rejects candidates that cannot provide it. Consolidating without rewriting history Similar memories may differ in confidence, importance, timing, or provenance. qwen-max proposes operations from a closed set, while deterministic code verifies each operation before committing it. Forgetting at the right speed A system that never forgets becomes an expensive transcript archive. A system that forgets too quickly loses useful context. Reverie balances reinforcement and decay so valuable memories remain strong while stale information gradually loses retrieval priority. Proving memory helps “It feels more personal” is not a useful benchmark. We built an evaluation harness that runs identical multi-session workloads under three conditions: No memory Full-history replay Reverie 📊 Accomplishments In our frozen live evaluation: Result No memory Full history Reverie Personalization mean 1.0 2.5 4.7 Reply-context tokens 7,271 32,764 10,598 Reverie achieved: 4.7/5 personalization 68% fewer reply-context tokens than full-history replay All six scripted retrieval checks passed Forgetting check passed These are controlled synthetic workload results, not a user study or production benchmark. The evaluation code and frozen results are included in the public repository. 💡 What we learned Memory is not merely a prompting problem. The strongest improvements came from the engineering around the models: typed state, exact provenance, evidence gates, event sourcing, deterministic validation, deliberate decay, and budgeted retrieval. Forgetting is not a failure. A useful memory system should preserve the right information, explain where it came from, revise it honestly, and know when to let it go. 🚀 What’s next Next, we plan to expose Reverie through a subject-layer SDK, strengthen multi-user isolation, and support configurable consolidation schedules for long-running agents. The goal is not to give an agent an unlimited transcript. The goal is to give it a memory it can defend. <div