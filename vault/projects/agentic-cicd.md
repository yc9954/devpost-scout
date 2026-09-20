---
slug: "agentic-cicd"
url: "https://devpost.com/software/agentic-cicd"
title: "Agentic CICD"
hackathon: "AI in Action"
organization: "Google"
winner: true
words: 425
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
  - "substrate/code_repository"
---

# Agentic CICD

> Your DevOps Sidekick - Automate, Analyze, and Accelerate with AI Agents for GitLab and Google Cloud

[Devpost](https://devpost.com/software/agentic-cicd) · hackathon [[AI in Action]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** express.js, gemini-2.5-pro, gitlab, gitlab-mcp, googlecloud-mcp, langchainjs, langgraphjs, mcp, node.js, react, supabase, typescript, vectorstores

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agentic cicd

## Body

Landing page Chat Page Repo and pipeline created by the agent Inspiration Over the past year, I’ve been deeply immersed in the world of AI agents — building, experimenting, and learning how they can assist with real-world tasks. After graduating this May and starting my journey as a DevOps intern, I found myself constantly thinking: “What if AI agents could handle most of the DevOps workload?” Driven by that curiosity and passion, I decided to build a platform where DevOps automation is not just scripted — it's intelligent. And that's how Agentic CICD was born: a step toward fully autonomous DevOps pipelines powered by agentic systems. What it does Agentic CICD is a modular, multi-agent platform designed to automate and manage CI/CD workflows using AI agents. Each stage of the DevOps lifecycle — from code validation, testing, deployment, to monitoring — is handled by a specialized agent. These agents can: Analyze pull requests and suggest improvements Monitor pipelines and fix common CI/CD issues Integrate with tools like GitLab, Jenkins, and Prometheus Perform reasoning over system states and logs Adapt workflows dynamically based on project context All with the help of GitLab MCP Server How we built it Tech Stack: 🧠 LLM Backbone: Gemini + LangGraph for agent orchestration 🛠️ Tooling: GitLab MCP Server, Jenkins, Prometheus, Ansible 🧱 Architecture: Multi-Agent System (MCP) with each tool exposed as a separate GitLab MCP server 🔌 Integration: LangChainJS + Tavily for enhanced search and context-aware decisions Challenges we ran into Designing a scalable agent orchestration system without losing performance Maintaining context across asynchronous events in CI/CD pipelines API rate limiting and authentication with GitLab and Jenkins Streaming SSE-based communication between the React agent and MCP servers Debugging tool interop across independently running agents Accomplishments that we're proud of Built a fully functional agentic CI/CD platform in a hackathon timeline Successfully integrated multiple DevOps tools under a single agentic interface Created a modular system where agents can be plugged/unplugged without rewriting orchestration logic Developed a live demo showcasing autonomous pipeline diagnosis and resolution What we learned How to apply agentic reasoning to real-world DevOps tasks Deep understanding of LangGraph, LangChainJS, and Gemini APIs Techniques for designing multi-agent communication using SSE and MCP Importance of context windows and embedding choices in long-running workflows What's next for Agentic CICD Add support for AWS/GCP resource orchestration using agents Implement real-time dashboards with agent recommendations Expand to include Incident Response and Security Compliance agents Package the entire system as a developer-friendly toolkit Open-source it to invite contributions from the DevOps + AI community <div