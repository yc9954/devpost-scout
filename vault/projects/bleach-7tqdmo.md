---
slug: "bleach-7tqdmo"
url: "https://devpost.com/software/bleach-7tqdmo"
title: "Bleach"
hackathon: "Agent Development Kit Hackathon with Google Cloud"
organization: "Google"
winner: true
words: 375
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/web_dom"
---

# Bleach

> Visual AI agent builder for Google ADK. Describe agents in plain English, design visually, test instantly. Open-source with complete UI editor.

[Devpost](https://devpost.com/software/bleach-7tqdmo) · hackathon [[Agent Development Kit Hackathon with Google Cloud]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** adk, gemini, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bleach

## Body

Here are the sections for your BleachAgentBuilder app: Inspiration The complexity of building AI agents shouldn't be a barrier to innovation. We saw developers struggling with Google's powerful Agent Development Kit (ADK) - writing hundreds of lines of boilerplate code, managing complex configurations, and debugging agent interactions. We envisioned a world where anyone could describe their AI agent idea in plain English and instantly get a production-ready system. What it does BleachAgentBuilder is an open-source visual agent creation platform built on Google's ADK. Users describe their agent requirements in natural language, and our AI meta-agent system automatically generates complete Python agent code with custom tools, provides a modern web interface for visual management, and enables real-time testing and iteration. How we built it Backend : Meta-agent system using Google ADK with specialized sub-agents for requirements analysis, architecture planning, agent building, and code generation. Frontend : Next.js/React interface with interactive chat, visual agent graphs, integrated code editor, and real-time configuration management. Integration : Seamless AI-powered backend connected to intuitive frontend through RESTful APIs. Challenges we ran into Complex State Management : Maintaining configuration consistency across multi-agent creation process Code Generation Accuracy : Ensuring syntactically correct, functionally complete Python code Visual Complexity : Representing complex agent architectures in intuitive UI ADK Integration : Deep understanding of Google's ADK patterns and best practices Accomplishments that we're proud of First open-source visual builder for Google's Agent Development Kit Natural language to production code pipeline with 95%+ accuracy Generated 50+ test agents across various domains Complete full-stack solution from idea to deployed agent What we learned AI-human collaboration works best when AI handles heavy lifting while humans provide direction. Deterministic code generation from validated configurations produces more reliable results than pure LLM generation. Visual representation makes complex systems approachable. What's next for Bleach Advanced ADK Features : MCP (Model Context Protocol) tools integration Advanced planners and reasoning patterns Structured output schemas with validation Built-in observability and monitoring Comprehensive evaluation frameworks Memory management and persistence Platform Enhancements : One-click deployment to cloud platforms Agent marketplace and sharing Performance analytics dashboard Enterprise security and compliance Plugin ecosystem for custom integrations Collaborative editing and version control Our vision: Make sophisticated agent systems as easy to create and deploy as building a website. <div