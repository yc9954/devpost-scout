---
slug: "rovo-autonomous-team-orchestrator"
url: "https://devpost.com/software/rovo-autonomous-team-orchestrator"
title: "Rovo Autonomous Team Orchestrator"
hackathon: "Codegeist 2025: Atlassian Williams Racing Edition"
organization: "Atlassian"
winner: true
words: 619
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "domain/transportation"
  - "user/developer"
---

# Rovo Autonomous Team Orchestrator

> Rovo Autonomous Team Orchestrator transforms Jira from a passive system of record into an Agentic Command Center, designed specifically to help software teams perform like a finely tuned pit crew.

[Devpost](https://devpost.com/software/rovo-autonomous-team-orchestrator) · hackathon [[Codegeist 2025- Atlassian Williams Racing Edition]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[structural_withholding]]
**domain** [[developer_tools]] [[mental_health]] [[transportation]]
**user** [[developer]]

**stack** atlassian-forge, bitbucket, confluence, glassmorphism-ui, jest, jira, jira-cloud, mcp, mermaid-js, node.js, react, rovo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- the math behind smart assign
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next

## Body

Rovo Autonoumous Team Orchestrator Team Orchestrator dashboard Report dashboard Project-Infographic Inspiration The inspiration for Rovo Autonomous Team Orchestrator came from a universal pain point in software engineering: friction . High-velocity teams rarely fail because they lack technical skill. They fail because they drown in administrative toil that slows execution and erodes trust. We repeatedly observed three recurring patterns: The “Lazy Ticket” Syndrome Developers waste hours interpreting one-line bug reports such as “Fix login,” with no context, steps, or acceptance criteria. Burnout by Assignment Tech leads manually assign work and unintentionally overload their strongest engineers, while others remain underutilized. Silent Failures Critical alerts buried in Jira, email, or Slack go unnoticed until SLAs are already breached. This led us to ask a fundamental question: What if Jira were not just a record of work, but an active team member? What if an AI agent could act as both a “pre-flight check” for tickets and a “traffic controller” for team workload? What It Does Rovo Autonomous Team Orchestrator is an agentic intelligence layer that sits on top of Jira, transforming it from a passive tracking system into a proactive teammate. It provides three core capabilities: Auto-Fix Agent (The “Pre-Flight Check”) The system listens for newly created tickets. If a ticket lacks sufficient detail, the agent autonomously rewrites it using Rovo’s LLM, generating: User stories Acceptance criteria Structured implementation steps This happens before a human engineer ever sees the ticket. Smart Assign (The “Load Balancer”) Instead of static or manual assignment, the system evaluates the live cognitive load of every developer. It filters out automation accounts and assigns the ticket to the engineer with the most available bandwidth, reducing burnout and balancing work distribution. Incident War Room A localized React dashboard embedded inside Jira visualizes: Active incidents SLA risk indicators System health signals This creates a single, real-time operational view for the entire team. How We Built It The project was built as a Model Context Protocol (MCP) -powered application using Atlassian Forge . Architecture Overview The system is designed as a decoupled intelligence layer over Jira. Frontend React dashboard embedded directly in Jira Uses @forge/bridge for secure communication Custom Glassmorphism UI to distinguish intelligence from standard Jira tables Backend (Forge Resolvers) A modular, multi-agent system implemented in Node.js: auto-fix.js – Expands vague tickets using Rovo’s LLM auto-assign.js – Computes workload-aware assignment decisions chaos-monkey.js – Injects controlled faults for resilience testing Agent Communication Agents follow Model Context Protocol (MCP) principles to standardize how they read Jira state and write actions back. The Math Behind Smart Assign To balance workload fairly, we implemented a weighted scoring model: $$ Score_u = \frac{1}{(W_u + 1)} \times \mathbb{I}(u \in Humans) $$ Where: \(W_u\) is the number of active tickets assigned to user \(u\) \(\mathbb{I}\) filters out automation and bot accounts Challenges We Ran Into Jira Indexing Latency Tickets created via API are not immediately searchable through JQL. Solution: Adaptive client-side polling and optimistic UI updates masked eventual consistency delays. Structuring LLM Output Producing consistently formatted user stories from vague inputs was difficult. Solution: Few-shot prompting with a strict Markdown template enforced output structure. Safe Chaos Engineering We wanted fault injection without risking production data. Solution: The Chaos agent operates only on tickets prefixed with [CHAOS] . Accomplishments We’re Proud Of 100% Unit Test Coverage for agents and resolvers Production-Grade UI with a custom Glassmorphism dashboard Latency Masking that makes Auto-Fix feel instant What We Learned Agents > Chatbots – Users want Jira to act, not converse The Power of Forge – Serverless deployment without infrastructure overhead Transparency Builds Trust – Explaining assignment decisions increased adoption What’s Next Predictive SLAs using historical signals Git Integration to account for PR review load Multi-Team Orchestration across Jira projects <div