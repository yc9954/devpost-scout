---
slug: "brydge"
url: "https://devpost.com/software/brydge"
title: "Brydge"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 881
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Brydge

> Presenting Brydge: the AI orchestration platform that turns scattered engineering knowledge into automated workflows, transforming hours of context-switching into just minutes of autonomous execution

[Devpost](https://devpost.com/software/brydge) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[human_in_the_loop]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** claude, confluence, github, jira, nemotron, nvidia, oauth, python, slack, typescript, weaviate

## How they structured the write-up

- the problem i witnessed
- the insight
- the project
- technical challenges
- learnings
- what's next

## Body

Brydge Search Page Brydge Workflow Demo Brydge Chat Page Manage Brydges Brydge Search Example Brydge Landing Page Brydge Dashboard Project Story: Brydge The Problem I Witnessed During my internship at NVIDIA, I was surrounded by cutting-edge AI tools: ChatGPT for brainstorming, Cursor for coding, Confluence for documentation, Jira for tracking, Slack for communication. Every tool was powerful individually, but my day became an endless cycle of context-switching: copy error logs from Datadog, paste into ChatGPT, get suggestions, search Confluence for architecture docs, check Jira for related tickets, update GitHub, notify the team in Slack. A simple bug fix that should take just minutes stretched into 2+ hours...not because of coding complexity, but because of coordination overhead. I realized the problem wasn't the tools themselves. It was that they existed in isolation. Each one held a piece of the puzzle, but no one was connecting them. Engineers were spending 50-60% of their time being "human middleware, "manually shuttling information between systems. The Insight What if AI agents could do the context-switching for us? Not just answer questions, but actively orchestrate workflows across tools. Not just search documentation, but pull relevant context from everywhere, synthesize it, and take action. The key was multi-agent orchestration: specialized agents that understood each tool deeply (GitHub, Jira, Slack, Confluence) coordinated by a reasoning agent that understood the bigger picture. The Project Brydge is an AI orchestration platform where one command triggers a cascade of intelligent agents working in parallel: The Architecture: Orchestrator Agent (NVIDIA llama Nemotron reasoning model): Plans multi-step workflows, coordinates sub-agents, handles failures Tool-Specific Agents : GitHub Agent (code analysis + PR creation), Jira Agent (ticket context), Confluence Agent (docs), Slack Agent (notifications), Weaviate Query Agent (semantic search across all sources) Specialized Agents : Analysis Agent (root cause identification), Code Generation Agent (fixes via Claude Code SDK) Human-in-the-Loop Gates : Approval checkpoints before any write action Sample Flow: Manager pings in Slack: "Checkout flow is broken for mobile users" Orchestrator creates execution plan, shows it for approval Agents fan out in parallel: fetch Jira ticket, analyze recent commits, search Confluence docs, semantic search across codebase Analysis Agent synthesizes root cause from all sources Code Generation Agent writes fix using Claude Code SDK User reviews diff → approves GitHub Agent creates PR Confluence Agent updates docs → user approves Slack Agent notifies manager → user approves What took 2 hours manually now takes 3 minutes of orchestrated agent work + 2 minutes of human review. Technical Challenges 1. Multi-Agent Coordination The hardest part was getting agents to work together without stepping on each other. For this, a DAG-based execution model where the Orchestrator determines dependencies (e.g., Code Generation can't start until Analysis completes) and runs independent tasks in parallel. Used asyncio for concurrent execution and Redis for inter-agent communication. 2. Real-Time Streaming Users needed to see what agents were thinking in real-time (chain-of-thought transparency). Implemented WebSocket streaming where each agent broadcasts thoughts, actions, and results. The Claude Agent SDK's built-in streaming callbacks ( on_thought , on_tool_use ) made this much cleaner than expected. 3. Context Window Management Claude's context limits were a big issue when processing large codebases. Solution: Weaviate Query Agent with semantic search to intelligently retrieve only relevant documents (solving the "retrieve top 25 docs" limitation by using Weaviate's agentic search modes that auto-refine queries). 4. Approval Gate Design Needed human approval before any write action (code changes, PRs, notifications) without blocking the entire workflow. Implemented async approval gates: agent pauses execution, creates approval record in PostgreSQL, sends preview via WebSocket, waits for user decision, then continues or rolls back. The Claude Agent SDK's on_approval_needed hook was perfect for this. 5. Error Handling Across Distributed Agents When one agent fails mid-workflow, how do you recover gracefully? Implemented checkpoint system: each agent step is logged to agent_steps table with status. If Analysis Agent fails, Orchestrator retries up to 3 times. If Code Generation fails, repo clone is cleaned up. If user rejects at any gate, all downstream steps are cancelled and changes are rolled back. Learnings Technical: Multi-agent systems require different architecture than single-agent systems (stateful orchestration, not stateless requests) Real-time streaming is non-negotiable for transparency in agentic systems Human-in-the-loop is essential for trust (fully autonomous is scary, fully manual defeats the purpose) Vector databases (Weaviate) are crucial for context retrieval at scale Sub-agent delegation (Claude Code SDK's feature) mirrors how humans delegate tasks to specialists Product: Engineers don't want "AI magic" they want transparent, controllable automation The value isn't eliminating human judgment, it's eliminating human busywork Showing the agent's reasoning ("chain-of-thought") builds trust Approval gates feel slow but are necessary for adoption What's Next Short-term (next 3 months): Add Datadog and PagerDuty agents for incident response workflows Implement scheduled agent runs (e.g., weekly digest of PR activity) Build admin dashboard for monitoring agent performance across teams Long-term vision: Marketplace for custom agents (let companies build tool-specific agents for internal systems) Agent learning from feedback (when users reject changes, agents learn what patterns to avoid) Proactive agents (not just reactive to user commands, but monitoring for issues and suggesting fixes) The future of engineering isn't replacing developers with AI; it's giving developers AI teammates that handle the coordination busywork so they can focus on creative problem-solving. Brydge is the operating system for that future. <div