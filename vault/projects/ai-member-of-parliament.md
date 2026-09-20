---
slug: "ai-member-of-parliament"
url: "https://devpost.com/software/ai-member-of-parliament"
title: "AI Member of Parliament"
hackathon: "TiDB AgentX Hackathon 2025"
organization: "TiDB"
winner: true
words: 522
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "user/general_public"
  - "substrate/structured_db"
---

# AI Member of Parliament

> An event-driven agentic system that reimagines how Meet-the-People sessions can work!

[Devpost](https://devpost.com/software/ai-member-of-parliament) · hackathon [[TiDB AgentX Hackathon 2025]]

## Facets

**mechanism** [[retrieval_grounding]] [[simulation_digital_twin]]
**user** [[general_public]]
**substrate** [[structured_db]]

**stack** celery, fastapi, kimi, redis, tidb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what we learned
- what's next for ai member of parliament

## Body

Task pipeline: tasks are placed into a queue, which are then polled by an agent for classification, decision-making, and execution Event-driven design: events are placed into a queue and agents update outstanding tasks. Inspiration Singapore has Meet-the-People Sessions , where Members of Parliament and their volunteers collate issues that residents bring up and write to organisations to appeal on their behalf. These sessions often have long queues. The question that I want to explore is: can an agentic system make this process more manageable? What it does AI Member of Parliament (AI-MP) is an event-driven agentic system that reimagines how Meet-the-People sessions can work. Its primary function is to automate the case-handling workflow. Residents submit cases via an online form. For each case, an agent categorises it, looks up similar past cases and relevant events (policies, news, parliamentary updates) to decide on an action. Actions can include writing an appeal letter, replying directly to the resident, and escalating the issue to Parliament. When organisations reply, or when new events occur, pending cases are automatically processed again to see if they can be closed. This workflow is systematic, which yields faster and more consistent results. In particular, the referencing of previous cases mimics MP's knowledge of past cases. The event-driven design of the system allows issues to be revisited given policy changes. In addition, AI-MP has several features (shown in demo): Parliament speech generation - MPs can generate draft speeches for Parliament based on a custom prompt and outstanding issues in the database. Event ingestion - Policies, news, and parliamentary updates can be ingested as event sources, giving the agent additional context when processing cases. Furthermore, AI-MP has two experimental features (verified, but not shown in demo). Raising to supervisor - Cases can be escalated to a supervisor agent with a higher privilege level, and hence access to a broader set of cases. Unsafe exec - To process a case, the agent can choose an action that generates and executes arbitrary code with soft guardrails in place. At best, AI-MP can automate much of the Meet-the-People session workflows. At minimum, it provides MPs with a reliable bookkeeping system to check case statuses and follow-ups. From the technical perspective, this project also explored how an agentic system can effectively interact with a database, and I believe an event-driven design is a decent approach. How we built it This application consists of several components: Two distributed queues that temporarily store tasks and events respectively. An agentic backend that polls from the queues, processes tasks and events, and makes decisions. Two vector databases (TiDB) with indices for storing and updating the statuses of the tasks and events. A SMTP server to simulate the sending of appeal emails and capture them in a user interface. What we learned A lot of real-world workflows can be decomposed into guardrailed pipelines instead of free-form agent planning. Most "agentic pre-plannning" can be broken down into a finite number of structured decision steps (e.g. LLM as a classifier), chained together with guardrailed pipelines to ensure reliability and control. What's next for AI Member of Parliament More data ingestion (synthetic data). <div