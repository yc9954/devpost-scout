---
slug: "velroi-general-autonomy"
url: "https://devpost.com/software/velroi-general-autonomy"
title: "Velroi General Autonomy"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 721
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/labor_employment"
  - "domain/transportation"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Velroi General Autonomy

> AI employees that actually work. Agents autonomously execute business workflows across your digital workspace with real-time progress visibility.

[Devpost](https://devpost.com/software/velroi-general-autonomy) · hackathon [[NexHacks]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[provenance_signing]] [[realtime_stream]] [[voice_speech]]
**domain** [[labor_employment]] [[transportation]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for velroi general autonomy

## Body

Google Slides Integration Asana Project Tracking Dashboard Asana Statement of Work Inspiration We asked a simple question: Why are AI assistants still single-threaded employees? While companies deploy dozens of human workers who coordinate, delegate, and track progress across tools—AI remains trapped in isolated chat windows, forgetting context and requiring constant hand-holding. We built Velroi General Autonomy to shatter that paradigm. VGA transforms AI from chatbots into an autonomous workforce—AI employees that manage projects in Asana, draft documents in Google Docs, send emails, schedule meetings, and report progress without human babysitting. The future of work isn't AI assistance—it's AI labor. What it does VGA deploys autonomous AI employees that complete real business workflows end-to-end. A Supervisor Agent orchestrates a fleet of specialized Worker Agents, each equipped with exactly the tools they need. Agents execute Statements of Work (SOWs)—structured task breakdowns with deliverables, success criteria, and progress tracking. For long-horizon projects spanning days or weeks, our Mission System tracks 50+ targets (contacts, leads, entities) through complete lifecycles. Every action syncs automatically to three systems in parallel: timestamped entries in Google Docs, structured rows in Google Sheets, and rich visual comments in Asana with emoji status indicators and progress bars. Blocked? The Supervisor detects it, alerts humans, and waits for intervention. 85+ Google Workspace tools (Gmail, Calendar, Docs, Sheets, Drive, Slides) plus full Asana integration means agents operate across your entire digital workspace autonomously. How we built it Python 3.10+ with async-first architecture. Every I/O operation—API calls, tool execution, progress syncing—runs asynchronously. We integrated Azure OpenAI's GPT-5.2 with full function-calling support: the LLM decides which tools to invoke, our Tool Registry executes them, and results feed back for the next decision. The agent hierarchy uses composition over inheritance: BaseAgent handles core logic (message history, tool execution loops, status tracking), while SupervisorAgent composes it with orchestration capabilities. We implemented dynamic tool assignment—agents receive only the capabilities their role requires, minimizing attack surface and cognitive load. Our Statement of Work system (~500 lines) models real project management: objectives cascade to deliverables, deliverables to tasks, tasks to targets. Status flows through state machines (PENDING → IN_PROGRESS → BLOCKED → COMPLETED) with automatic Asana synchronization maintaining visual workflow sections. Challenges we ran into Parallel progress synchronization nearly broke us. Updating Google Docs, Sheets, and Asana simultaneously while handling rate limits, partial failures, and maintaining consistency required careful async orchestration and graceful degradation patterns. Tool explosion management was another battle. With 85+ Google Workspace tools, keeping the LLM's context window manageable while preserving capability required selective tool injection based on agent roles. Blocker detection proved philosophically tricky: when does "working slowly" become "blocked"? We implemented periodic check-ins where the Supervisor queries agents about their state, combined with explicit blocker-reporting tools agents can invoke. Accomplishments that we're proud of 29,000+ lines of production-quality Python with clean separation across agents, integrations, and tools. Our Supervisor Agent alone spans 1,407 lines of battle-tested orchestration logic. Real autonomous workflows: agents send emails, create documents, update spreadsheets, and manage Asana tasks without human intervention—then report exactly what they did with visual progress indicators. The Mission System enables week-long campaigns: track 50+ outreach targets, collect structured responses, maintain persistent state across sessions, and generate automatic progress documentation. Three-way progress sync with emoji status (🔄 WORKING, 🚫 BLOCKED, ✅ COMPLETED), text progress bars [████████░░], and timestamped audit trails across Docs, Sheets, and Asana. What we learned AI orchestration is fundamentally different from AI prompting. Single-agent systems optimize for response quality; multi-agent systems optimize for coordination, progress visibility, and failure recovery. Tooling matters more than model intelligence. A well-instrumented agent with 85 carefully-designed tools outperforms a genius model with vague instructions. Function calling transforms LLMs from oracles into operators. Humans don't want AI autonomy—they want AI autonomy with visibility. The aggressive progress tracking we built isn't overhead; it's the product. Managers trust AI workers only when they can see exactly what's happening. What's next for Velroi General Autonomy Web-based dashboard for real-time fleet visualization—see all agents, their SOWs, blockers, and progress at a glance. Voice interface for supervisor commands. Composio MCP integration for expanded tool ecosystems. Team collaboration with shared agent pools across organizations. Enterprise deployment with RBAC, audit logging, and compliance controls. The endgame: VGA becomes the operating system for AI labor—where deploying an AI employee is as simple as describing what you need done. <div