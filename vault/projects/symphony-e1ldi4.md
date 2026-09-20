---
slug: "symphony-e1ldi4"
url: "https://devpost.com/software/symphony-e1ldi4"
title: "Symphony"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 725
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Symphony

> Five Qwen-powered specialist agents debate, vote, and veto over scarce disaster resources, the only setup that stays within budget where a lone agent overspends money it doesn't have.

[Devpost](https://devpost.com/software/symphony-e1ldi4) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[multi_agent]] [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[health_clinical]] [[supply_logistics]]
**user** [[patient_family]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]]

**stack** alibaba-cloud-ecs, alibaba-cloud-model-studio, alibaba-tablestore, apsaramq-for-kafka, docker, fastapi, neo4j, next.js, pytest, python, qwen-(qwen-turbo-/-qwen-max-via-dashscope), redpanda, tailwind-css, terraform

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for symphony

## Body

Symphony System Architecture Benchmarks Section Conflicts Section Overview Section Ledger Section Live Section Inspiration We've all watched a single AI assistant confidently make a bad call, and then had no way to ask why . For a chatbot that's annoying; for a crisis it's dangerous. In a wildfire, the same helicopter can fight the fire, fly out critical patients, or reach people trapped with minutes to spare. Real emergency operations don't hand that to one voice, they put specialists in a room and make them argue, on the record. I wanted to know what an AI system would look like if it worked like that room instead of like one all-knowing assistant. What it does Symphony simulates a wildfire spreading across two districts over twenty time-steps, with helicopters, medics, rescue crews, comms towers, and a fixed budget all running short. Five specialist agents : Logistics, Medical, Comms, Finance, and Search & Rescue, each powered by Qwen , allocate those resources together. Each proposes only in its own domain. When two of them want the same helicopter, a structured Parliament Protocol resolves it: propose → debate → vote →escalate → commit, with Finance holding a veto over spending the society can't afford. Every decision is written to a ledger you can replay and a conflict graph you can explore, and a live dashboard shows the whole thing unfolding map, command matrix, deliberations, and a benchmark against a single-agent baseline. How we built it The backend is Python: a seeded simulator, five agents with fixed expertise weights, and the Parliament Protocol as a real state machine. The guiding rule is "agents propose, deterministic code adjudicates" ,Qwen writes the proposals, rebuttals, and persuasiveness scores, but conflict detection, the weighted vote, the veto, and the commit are all plain, unit-tested Python, so the same seed always produces the same run. Every external service sits behind an adapter with a zero-cost local default and a cloud backend you switch on with one environment variable: Qwen via DashScope for the LLM, Tablestore for state, ApsaraMQ for Kafka for the event bus, Neo4j for the conflict graph. Specialists run on qwen-turbo ; the Coordinator that breaks deadlocks runs on qwen-max . The frontend is a Next.js dashboard. The backend was deployed and run on Alibaba Cloud ECS with live Qwen. Challenges we ran into The hardest one was honest, not technical: my first benchmark said the five-agent society and the single agent were identical . Instead of shipping the flattering tie, I dug in and found that the scenario's budget was so generous that Finance's veto, one of my two core mechanisms, never fired in any real run. Fixing that took three careful budget tunings, each documented, until the constraint genuinely bound. Only then did the real result appear: the lone agent "wins" 100% of objectives only by overspending $35,000 it doesn't have, in every trial, while the society stays within budget every time. Getting the PowerShell-to-SSH deployment onto Alibaba Cloud working, and proving the running process was actually calling live Qwen (not silently falling back to the mock), were the other two real fights. Accomplishments that we're proud of The society is the only configuration that produces an executable plan 20 out of 20 trials finish within budget, versus 0 out of 20 for the baseline. Both conflict resolution mechanisms (the weighted vote and the Finance veto) are visible in one real seeded run, including a moment where an agent wins the vote and still doesn't get the helicopter because the society can't afford it. And the whole system runs offline at zero token cost on a deterministic mock, so all 87 tests pass with no API key then the exact same code runs live on Qwen. What we learned Determinism is a feature, not a limitation: drawing a hard line between "propose" (the model) and "decide" (the code) is what made Symphony both trustworthy and debuggable. A benchmark that flatters you is a bug report. And good multi-agent design is mostly about the boundaries the protocol between agents and the adapter seams far more than the agents themselves. What's next for Symphony Time-aware rescue scoring (a rescue one tick too late shouldn't count the same as one on time), a second non-wildfire scenario to prove the protocol is domain-agnostic, and running the Coordinator's qwen-max rulings under full live load. <div