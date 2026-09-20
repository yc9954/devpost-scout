---
slug: "quen"
url: "https://devpost.com/software/quen"
title: "Quên"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 678
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/measured_ablation"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "user/legal_professional"
  - "substrate/sensor_telemetry"
---

# Quên

> A Qwen-powered agent memory that knows what to forget, says how sure it is, and verifies before it asserts.

[Devpost](https://devpost.com/software/quen) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[deterministic_policy]] [[measured_ablation]] [[retrieval_grounding]]
**domain** [[finance_payments]] [[housing_homeless]]
**user** [[legal_professional]]
**substrate** [[sensor_telemetry]]

**stack** fast-api, python, qwen, react, typescript

## How they structured the write-up

- project description

## Body

Memories — live FSRS decay Memory detail — forgetting curve & validity Dream log Recall trace Vitals How it work Architecture Fama by config Budget curve Confidence by freshness Retention calibration Project description The problem The sharpest failure mode of agent memory isn't forgetting too much — it's being confidently wrong from stale memory . Stale memory rarely fails at retrieval; it fails by making the agent act confidently on invalidated assumptions. Memora/FAMA measured it: agents frequently reuse invalidated memories. What Quên does Quên (Vietnamese for "to forget", sounds like Qwen ) treats trust as a runtime decision, not a stored property : Write the delta : Qwen extracts facts and (s,r,o) triples; a salience gate skips what a base model already knows; confidence comes from source authority (PR > doc > chat). Real forgetting math : retention state is FSRS-4.5 (the spaced-repetition equations, imported verbatim). Reviews come from three places: use-in-answer judged good/bad, dream self-tests, and verification outcomes — the closed loop nobody else ships. Dream consolidation : episodics re-abstract into generalizations; contradictions resolve deterministically first (same-(s,r)-new-o slot rule for functional relations — zero LLM calls, fully auditable) with a Qwen NLI fallback where augmentation never supersedes . Unused memories evict (R<θ ∧ TTL ∧ not pinned). Tombstones only — never hard-delete. Verify-before-answer : at answer time, trust = f(confidence, freshness, status). Low-trust memories get checked against the live source before the agent asserts them: confirmed → confidence rises + FSRS good review; refuted → tombstoned on the spot + fail review; unverifiable → the answer hedges explicitly. Measured honesty : stated answer confidence is scored with freshness-stratified calibration (ECE), and the headline metric is FAMA = presence-of-valid ∧ absence-of-invalidated. Results (live on Qwen via Alibaba Cloud DashScope, canonical run) Code-staleness probe (n=30) : FAMA 0.933 [0.79, 0.98] vs 0.40 append-only RAG / 0.43 full-context (paired McNemar p = 3×10⁻⁵); forgetting precision/recall 0.842/0.938; verify ablation +0.13 FAMA. Paraphrase-frozen probe : 0.933 — no drop; the mechanism, not our phrasing, carries the result. LongMemEval (n=229, external anchor with no staleness) : we lose knowledge-update to turn-level append-only RAG (0.31 vs 0.54, p=0.0015) and tie on temporal reasoning and abstention — reported, not hidden. Forgetting is a tax on staleness-free recall and a large win the moment the world changes. Budget curve: baselines flat at every budget (their failures are trust failures); Quên holds 0.87–0.93 from a 30-token budget up. The whole canonical live eval cost ≈ $1.6 (usage counters × DashScope pricing — the cost table is in the README). We also ran an adversarial audit of our own algorithms — 11 biases found, fixed, and regression-tested (over-forgetting multi-valued facts, recency bias in trust, eviction starvation, strawman baselines, self-serving scoring…). The full table is in the README. How it's built (all Qwen, all Alibaba Cloud) qwen-flash (extraction/salience/judging) + qwen3.5-plus (reader/NLI/re-abstraction) + text-embedding-v4 , all through one client ( alibaba_client.py ) on the DashScope international endpoint. Backend = FastAPI + SQLite (WAL, audit-logged, tombstones only) on an Alibaba Cloud ECS instance that also serves the React dashboard same-origin. A thin FastMCP server (8 tools — remember/recall/ask/judge/dream/verify_hint/ pin/inspect — closing both the per-memory verification loop and the per-answer retention loop) drops the same engine into any MCP harness, and a Claude Code hooks kit ( integrations/claude-code/ ) loads memories at SessionStart and captures the conversation at SessionEnd/PreCompact. Everything — 176 tests and the full eval — also runs 100% offline (deterministic scripted LLM + hashing embedder), so judges can reproduce without a key. What's next Temporal-hierarchical digests (TiMem-style graduated compression), a Letta-style sleep-time dream scheduler, FSRS weight re-fit from the calibration events the store already records, and context-cache-aware prompt ordering (DashScope bills cached prefixes at ~10% of fresh input — our usage counters already track the hits). Full roadmap: docs/ROADMAP.md . Recent flag-gated additions already measured offline: compact trust tags (−35% delivered tokens/query at identical FAMA) and spaced self-test scheduling (52-week sim: 221 vs 427 tokens/query against append-only from an active store 6× smaller, 203 evictions/yr, stale-free rate 1.0). Links Live demo (Alibaba Cloud ECS, Singapore): http://47.236.141.124/ Repo: https://github.com/phamthanhhang208/quen <div