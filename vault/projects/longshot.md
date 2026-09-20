---
slug: "longshot"
url: "https://devpost.com/software/longshot"
title: "Longshot"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1146
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
---

# Longshot

> Built Minecraft in one shot - Burned $5500 running 100+ coding agents pushing at peak 1200+ commits/hr to research the future of "coding"

[Devpost](https://devpost.com/software/longshot) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[provenance_signing]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]]
**substrate** [[code_repository]] [[sensor_telemetry]]

**stack** chatgpt, claude, cursor, modal, pidev, poke

## How they structured the write-up

- inspiration
- ⚠️ problem
- 🧠 what it does
- 🛠️ how we built it
- 🤖 ai & agent logic
- ⚙️ infrastructure
- 💻 interface
- 🧩 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what’s next for longshot

## Body

Longshot technical architecture Rich GUI terminal of agents working Gorce agents visualization Planner, subplanner, worker structure Prompt structure for runtime agents and project specifications In 36 hours, we built Minecraft from one prompt using a swarm of 200 agents and $5,000 in Modal credits. Inspiration AI has already transformed the digital world by translating language to code with autonomous coding agents, but this requires human intervention. Longshot changes that by orchestrating swarms of autonomous agents. Each agent observes, interprets, and acts in real time, working in parallel while staying aligned to the project’s goal. Longshot is our architectural system curated towards spawning swarms of carefully managed long-running agents that code an end product start to finish. ⚠️ Problem Most agentic coding today like Claude and OpenClaw are iterative loops where you either supervise step by step or let a single agent run in a loop. It can handle small tasks, but on long runs it gets brittle, loses context, and drifts from the original objective. To scale, many systems “spawn subagents” but these are usually just extra LLM calls with different roles and smaller context slices. They improve parallel thinking, not parallel execution. Some newer systems give agents their own sandboxes/resources for true parallel coding. But at the scale of 100k plus LOC and 5k plus commits, they often fall apart because the work diverges from the objective. The bottleneck is maintaining global coherence, shared state, and quality across thousands of independent commits. 🧠 What it does Longshot is an autonomous coding orchestrator that manages a swarm of coding agents. Given a project specification, Longshot: Balances between GPT 5.2 and GLM 5.0 to planner to decompose the project into hundreds of granular tasks Dispatches tasks to isolated sandboxes running in parallel on Modal Runs code generation, tests, linting, and concurrently pushes commits using Git Merges results through a merge queue that detects conflicts and enforces build and test gates Self-heals via a reconciler agent that detects broken builds and spawns targeted fix tasks Visualizes the entire run in real time of each individual agent through a Rich-powered terminal UI and Gource The planner, subplanner, worker, and reconciler agent architecture lets Longshot execute long-horizon builds without losing alignment across thousands of changes. This is the future of vibecoding, where we can enter a single prompt that will code a project with long-term running agents. 🛠️ How we built it We built Longshot as a modular distributed system designed to coordinate planning, execution, validation, and reconciliation across hundreds of agents. Poke: Enables external tools with an MCP server for users to interact with the system in real time. PI.Dev Harness - Lightweight development environment that auto-provisions isolated sandboxes per agent, letting them code, test, and run tasks safely and independently. Anthropic Claude SDK - Embedded programming toolkit giving agents structured coding tools, execution APIs, and reusable skill modules. LLMs: OpenAI ChatGPT 5.2 and Zhipu AI GLM-5 coordinate planning, sub-task assignment, and code generation across agents. Modal: Serverless GPU backend that runs each sandboxed agent at scale with high-performance compute and automatic resource provisioning. Gource: Visualizes planner, sub-planner, and worker lifecycles from commit traces, producing a tree-style timelapse that shows agent progression and interaction patterns. Rich Terminal: Real-time interface displaying active agents, task progress, build health, cost metrics, and throughput in a unified monitoring view. 🤖 AI & Agent Logic Multi-agent architecture has two parts: designing the runtime agent infrastructure and refining the input specification for the project. These design choices let the swarm sustain high throughput while staying aligned to the objective. On the infrastructure side, we wrote a dedicated prompt for each agent role. The system is recursive: the planner spawns subplanners until a task is small enough for a worker to complete end to end. To avoid coordination overhead, workers never communicate with other agents. We also run a reconciler on a 5 minute cadence that checks main for regressions, rather than blocking the merge queue on perfect correctness for every commit. Agents are prompted to push at high confidence rather than 100% confidence to increase throughput. - Conflicts can be resolved by another agent. On the specification side, we separate static intent from runtime memory. The core spec is locked before the run to prevent objective drift. During execution, agents maintain an editable text file and decision log that get frequently rewritten to capture the latest priorities, assumptions, and changes. This keeps the swarm aligned over long horizons without freezing its ability to adapt. SPEC.md is intentionally goal driven rather than feature driven. It defines intent and constraints without over-prescribing implementation details, so agents can make progress without getting trapped in checklist behavior. ⚙️ Infrastructure We used Modal to spin up ephemeral sandbox environments where agents execute safely in parallel. Each container runs isolated code generation and testing pipelines. State between the orchestrator and sandboxes is passed through strict JSON protocols containing diffs, logs, and metadata. 💻 Interface We built a real-time terminal dashboard using Rich that visualizes the agent states, throughput metrics, merge queue progress, and an activity log. Additionally, we use Gource to visualize the life cycles of all planners, sub-planners, and workers across all commit traces for an agent’s lifetime. This creates a tree life structure and timelapse of its progression and how agents interact with one another. 🧩 Challenges we ran into We ran 16 GPUs on Modal and cold start and setup under high utilization. Iterating the spec prompt to stop agents from changing the objective over time. Heavy credit costs for compute time. Agents behaved conservatively by default. The agent swarm did not have enough instructions in their prompts to merge into main, so the agents continuously merged branches and resolved conflicts instead of taking action. 🏆 Accomplishments that we're proud of We created Minecraft in a single hackathon with autonomous agents We learned how to use serverless GPUs We built a high-level technical implementation of code agent planning, execution, and distribution of tasks in an efficient system 📚 What we learned Parallelism Requires Strong Coordination : Large multi-agent builds need strict spec control, merge gating, and reconciler agents to maintain alignment across thousands of commits. Serverless GPUs Change Development Workflow : Ephemeral environments enable rapid scaling but require careful cold-start handling, cost tracking, and sandbox state management. Prompt + Architecture Design Matters : Agent role prompts, recursive planning, and clear separation of static intent vs. runtime memory were critical to prevent drift 🚀 What’s Next for Longshot Agent throughput tuning: We will iterate on the agent harness to increase sustained commits per hour without sacrificing build health. This includes reducing sandbox cold-start overhead, improving task batching, and tightening the JSON diff and log protocol to cut orchestration latency. Dev observability: Add run replay, commit provenance, and a unified event timeline with failure clustering so we can debug agent behavior and CI regressions quickly without rerunning expensive compute. <div