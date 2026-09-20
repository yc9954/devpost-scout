---
slug: "working-memory"
url: "https://devpost.com/software/working-memory"
title: "Working Memory"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 564
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
---

# Working Memory

> Working Memory is an agentic workflow that passively observes your coding sessions, summarizes your progress, and reconstructs context from your history, enabling seamless re-entry into any project.

[Devpost](https://devpost.com/software/working-memory) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
  <sub>weak: web_dom</sub>

**stack** axios, conda, fastapi, git, github, gitpython, gpt-4.1-mini, html, javascript, mcp, npm, openai-agents-sdk, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for working memory

## Body

Inspiration As students who juggle between coding projects for classes, clubs, research, or personal work, we often face the problem of constantly switching between contexts. Every time we switch, we lose fragments of our working memory, which encompasses the reasoning behind decisions, pending tasks we may have, and the overall mental model of the code. For this reason, we created Working Memory , an agentic workflow that passively observes your work and automatically reconstructs context, enabling seamless re-entry into any project. What it does Working Memory connects your VS Code workspace to an AI-powered backend that continuously records and interprets your development sessions. Start a session : Initialize a coding session directly within the web dashboard. Code as usual : Any modified or newly created files are tracked. Stop the session : The changelog is gathered and fed into an AI data-processing pipeline, producing: A natural-language summary containing a high-level overview and actionable insights. Structured metadata containing the git status output. View History : The results appear in the web dashboard under Past Workflows, complete with a search engine for re-entering context later. How we built it Working Memory is composed of three coordinated layers: Frontend UI Built with TypeScript, React, and Tailwind CSS. Employs elegant glassmorphism UI components ( GlassCard , Pill ) and minimalist design. Handles session creation, workflow history, and theme preferences. Implements vector search for instant retrieval of past sessions. Model Context Protocol (MCP) Server Built with TypeScript in the form of a VS Code extension. Exposes an HTTP endpoint to return the active project path. Backend Agent Built with Python, FastAPI, and GitPython. Calls MCP server to retrieve active project path Scans the file tree and structures the changelog Feeds changelog into GPT-4.1-mini (selected as a fast, cheap model for general-purpose reasoning with 1 million token context window for large changelogs) Challenges we ran into Component Integration : Integrating between the front-end UI, backend agent, and MCP server required coordination across different environments, protocols, and data formats, so we needed to ensure consistent data flows and communication for seamless session tracking. OpenRouter Inference Inconsistencies : LLMs would frequently (and silently) fail, returning an empty string even on successful API calls, so we needed to create a robust fallback layer for exception handling before accepting a response. Context Window Limitations : Large changelogs would often exceed the model's context, so we needed to establish a tradeoff between model capability and token efficiency in our selected model. Accomplishments that we're proud of Designing and configuring a three-layer architecture into a single, cohesive application. Created a clean, minimal frontend experience mirroring the aesthetics of modern productivity tools. Integrated lightweight vector search for a searchable timeline of developer sessions (with list/calendar formats). Integrated Model Context Protocol (MCP) for VS Code to capture context directly from the developer environment What we learned Integrating LLM reasoning into real-world developer workflows beyond chat interfaces. Capturing context efficiently through iterative agent loops (reasoning → summarization → storage) Safeguarding against LLM failures (most commonly low-quality or empty responses) by validating content (not just status code) What's next for Working Memory Cloud Sync/Authentication : Allow users to securely store and access sessions across devices. Deeper IDE integration : Extend beyond VS Code (JetBrains, PyCharm, Eclipse, etc.) using the same scalable MCP architecture. Additional App Integrations : Extend beyond coding workflows in VS Code to writing essays, problem-solving, etc. <div