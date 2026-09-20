---
slug: "n-gqhkio"
url: "https://devpost.com/software/n-gqhkio"
title: "Pyra"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 351
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
---

# Pyra

> Pyra is the secure execution layer for crypto AI. It enables developers to let agents fulfill smart contracts and trades by enforcing security runtime gates and deterministic guardrails.

[Devpost](https://devpost.com/software/n-gqhkio) · hackathon [[NexHacks]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** ens, ethers.js, etherscan, kairo, livekit, node.js, react, typescript, vite, zod

## How they structured the write-up

- our inspiration came directly from kairo's whitepaper.

## Body

Landing Page Our Product in Action Our inspiration came directly from Kairo's whitepaper. Under Current Market Challenges, Point #5 states: "AI and autonomous agents are emerging faster than security infrastructure." We noticed that while Kairo has solved security for human developers via the IDE, their whitepaper lists 'AI Agent Security Infrastructure' as a phase 3 roadmap item. That was our lightbulb moment. With the explosion of agentic frameworks like LiveKit and the rise of autonomous financial agents, we realized the industry cannot wait for phase 3. We were inspired to build Pyra to fill that gap today. We took Kairo's powerful analysis engine and created a runtime infrastructure required to secure the autonomous agents that Kairo predicted would need protection. Kairo correctly identifies that security for AI agents is inevitable—but today, most protection is still developer-centric (IDE checks, static analysis, pre-deployment safeguards). Pyra takes the next logical step: securing agents after they are deployed, when they are autonomous, stateful, and capable of acting in the real world. Pyra is a runtime security infrastructure for autonomous AI agents. It operates at the execution layer, continuously monitoring agent behavior, decision flows, tool usage, and external interactions in real time. Instead of assuming agents behave as intended once deployed, Pyra treats them as living systems that require ongoing oversight. At its core, Pyra: Observes agent actions at runtime, not just code at build time Detects anomalous or unsafe behavior (prompt drift, goal hijacking, tool abuse, financial overreach, unauthorized API calls) Enforces programmable guardrails that can pause, constrain, or terminate agent actions instantly Creates auditability and accountability for agents operating in sensitive environments like finance, operations, and infrastructure By adapting Kairo’s powerful analysis philosophy to the agent runtime layer, Pyra becomes the missing infrastructure that allows autonomous agents to operate safely at scale. Where Kairo secures the developer’s intent, Pyra secures the agent’s execution. In a world rapidly adopting agentic frameworks like LiveKit—and where autonomous financial and operational agents are already making real decisions—the industry cannot afford to wait for security to catch up later. Pyra exists so autonomous agents can be trusted today. <div