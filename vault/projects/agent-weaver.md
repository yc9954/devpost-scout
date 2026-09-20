---
slug: "agent-weaver"
url: "https://devpost.com/software/agent-weaver"
title: "Agent-weaver"
hackathon: "Gemini 3 Hackathon"
organization: "Google"
winner: true
words: 630
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# Agent-weaver

> Turn Gemini into a coordinated team of 5 specialized AI agents with shared memory, human-verified annotations, and real-time collaboration between teams and their agents.

[Devpost](https://devpost.com/software/agent-weaver) · hackathon [[Gemini 3 Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[realtime_stream]]
  <sub>weak: human_in_the_loop</sub>
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** 55-mcp-tools, ast-powered-indexing, eslint, express.js, git, git-native-collaboration, google-gemini-3.0-flash, human-in-the-loop-verification, json-based-persistence, model-context-protocol-(mcp), modelcontextprotocol/sdk, next.js-15, node.js, npm/pnpm

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agent-weaver

## Body

Landing Page Context Board Code Intelligence Plan In action-1 In Action-2 in-action 3 Inspiration Working with AI coding tools is frustrating. There are endless code searches, and for complex or poorly structured codebases, agents misinterpret context and make wrong decisions. Every prompt starts from scratch—agents forget what they learned, teammates duplicate AI analysis, and there's no way to verify or trust AI-generated code insights across a team. What it does Agent Weaver transforms Gemini 3 into a coordinated team of 5 specialized AI agents (Architect, Product Manager, Developer, QA Engineer, Code Reviewer) that share a persistent memory space. It provides: Shared Agent Memory: A context board where all agents read from and write to—no re-scanning, no duplicate work Human-Verified Code Annotations: Agents write detailed notes on code symbols, humans verify them, building trusted team knowledge over time Git-Based Team Collaboration: The entire .weaver/ directory commits to git—one teammate scans, the whole team benefits AST-Powered Indexing: Tree-sitter parses code, Gemini enriches every symbol with natural language descriptions Hub Sync Server: Central Express server for cross-team synchronization by git branch Real-Time Dashboard: Next.js observability dashboard with live SSE updates showing all agent activity How we built it We built a universal MCP server (55 tools across 19 modules) that connects to both Gemini CLI as a plugin and works with Claude via MCP protocol. The architecture includes: MCP Server: TypeScript + Model Context Protocol SDK for 5 specialized agent roles Hub Server: Express.js for centralized team sync (stores snapshots by git repo + branch) Dashboard: Next.js 15 + React 19 + Tailwind CSS 4 with SSE for real-time updates Code Intelligence: ast-grep (Tree-sitter) for AST parsing + Gemini API for LLM enrichment Persistent State: JSON-based .weaver/ directory with context.json, index.json, plan.json, team.json, annotations.json Every agent decision flows through Gemini's multimodal API using 2M token context windows for full codebase comprehension and function calling for all 55 MCP tools. Challenges we ran into Coming up with a good agent orchestration workflow to handle this ambitious project in just a few days was intense. We had to: Design a persistent memory system that survives across sessions Build human verification into the agent workflow without slowing them down Create git-based sharing that actually works for teams with different branches Architect 5 specialized agents that collaborate without stepping on each other Make everything fast enough to feel real-time in the dashboard Google AI Studio was not used here because of the nature of the project and its deep integration with gemini CLI. Accomplishments that we're proud of We've seen 20-30% improvement in one-shot capabilities with significantly less input token usage because agents have better context. The Architect and Product Manager ensure changes align with high-level project goals—something most coding agents completely lack. Key wins: Persistent memory eliminates agent amnesia Human-verified annotations build trust over time Git-based sharing means zero duplicate AI work across teams AST + LLM enrichment enables semantic code search Real-time dashboard makes AI agents observable and debuggable What we learned Agents can do awesome things, and multi-agent systems don't necessarily mean more expensive if we build with efficiency in mind from the start. That's the whole point of this project: make coding agents efficient. Shared memory drastically reduces token usage Human verification is key to building trust in AI systems Git integration makes AI tools actually useful for teams Specialized agents > one generalist agent trying to do everything What's next for Agent-weaver JIRA Integration: Connect agent tasks and decisions directly to project management workflows Plugin Architecture: Allow other MCP tools to integrate with the main agents efficiently—making Agent Weaver a platform, not just a tool Benchmark Suite: Quantify efficiency gains across different project types and team sizes Multi-LLM Support: Let teams use different models for different agents based on cost/performance tradeoffs <div