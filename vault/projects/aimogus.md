---
slug: "aimogus"
url: "https://devpost.com/software/aimogus"
title: "aimogus"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 355
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/education"
  - "user/legal_professional"
---

# aimogus

> Can AI agents in multi-agent systems deceive, deduce, and stay aligned?

[Devpost](https://devpost.com/software/aimogus) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[education]]
**user** [[legal_professional]]

**stack** flask, modal, openrouter, python, pytorch, transformers, wandb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aimogus

## Body

Inspiration Future AI systems will collaborate in multi-agent settings, but we lack evals for how they behave when deception is incentivized Models may appear aligned in isolation but exhibit misaligned behaviors (blackmail, manipulation) when placed in competitive social environments Among Us is a natural testbed: it rewards deception, deduction, and persuasion simultaneously What it does Full Among Us simulation where LLM agents play as crewmates and impostors with task completion, meetings, and voting Capabilities evals: win-rate, deception/deduction ELO, persuasion benchmarks Alignment evals: TruthfulQA, LLM-as-a-judge for detecting emergent misalignment (blackmail, sycophancy, deceptive alignment) GRPO post-training loop that improves agent game performance and reveals alignment degradation as a side effect Inoculation prompting during post-training that recovers alignment without sacrificing capabilities How we built it Python game engine with parallel agent execution, proximity-based communication, and action resolution Agents backed by local models (Qwen 7B, etc.) and API models (GPT, Gemini, Grok, etc.) with shared prompt architecture Batched inference pipeline on Modal A100s for concurrent game rollouts GRPO with group-normalized advantages and KL-regularized policy updates, logged end-to-end on WandB GUI with real-time visualization and agent voice audio Challenges we ran into Multi-agent RL is expensive: 10 concurrent games with mixed local/API inference required custom batching to avoid GPU serialization bottlenecks On-policy GRPO means no replay buffer: every training step needs fresh rollouts Balancing rollout speed (API latency) against training throughput on limited GPU budget Accomplishments that we're proud of End-to-end pipeline: environment → rollouts → GRPO training → evals, all running on cloud GPUs Demonstrated measurable alignment degradation from capability-focused post-training. Then fixed it with inoculation prompting Built a generalizable multi-agent eval framework What we learned Capability improvements and alignment can directly trade off in multi-agent RL. You can't just train for performance and hope alignment holds Inoculation prompting is a lightweight but effective alignment intervention during post-training Multi-agent environments surface misaligned behaviors that single-agent benchmarks completely miss What's next for aimogus Generalize beyond Among Us to arbitrary multi-agent social games Integrate into post-training mixes alongside standard capability benchmarks Explore interpretability (SAEs, linear probes) to detect deceptive reasoning internally Scale to more agents, longer games, and self-play curricula <div