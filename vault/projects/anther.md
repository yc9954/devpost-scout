---
slug: "anther"
url: "https://devpost.com/software/anther"
title: "ANTHER"
hackathon: "NextGenHacks"
organization: "NextGenHacks"
winner: true
words: 393
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/runtime_tool_creation"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# ANTHER

> AETHER takes any public GitHub repository and instantly maps its entire architecture using AI-generated interactive Mermaid.js diagrams

[Devpost](https://devpost.com/software/anther) · hackathon [[NextGenHacks]]

## Facets

**mechanism** [[runtime_tool_creation]]
**domain** [[developer_tools]] [[finance_payments]]
  <sub>weak: developer</sub>
**substrate** [[code_repository]] [[geospatial]] [[structured_db]]

**stack** ai, api, github, medo, mermaid.js, next.js, platform, rest, tailwind, typescript

## How they structured the write-up

- the challenge
- how it works (the fix)
- how i built it with medo
- challenges we faced (and conquered)
- what we learned

## Body

Home Screen GIF Diagram Tired of Manual Onboarding? Meet AETHER. This is ANTHER, an AI-powered Developer Onboarding & Scoping Assistant built for Work & Productivity track. The Challenge Ever joined a new project, looked at the repository, and realized you're going to lose the next three days just figuring out how the files connect? We’ve all been there. Manually mapping data flows and component hierarchies is a total productivity killer. I built ANTHER to solve this. How it works (The Fix) AETHER takes any public GitHub repository and instantly maps its entire architecture using dynamically generated, interactive Mermaid.js diagrams. It turns a massive, confusing codebase into a visually digestible system design map in seconds. To make this a true productivity tool, it includes three critical features: Impact Analysis Mode: Type a feature request (e.g., "Replace the dog 3D model with the new earth model" ). ANTHER analyzes the repo structure, visually highlights the exact files that need modification in orange, and generates a detailed Implementation Checklist. Context Pruning: Users can filter the diagram to show only the Frontend, Backend, or Database models to focus on the work that matters. One-Click Auto-Documentation: Instantly generate and download a comprehensive, formatted ARCHITECTURE.md file ready to be committed to the repository. How I built it with MeDo Building this pushed MeDo to its limits, but it handle the orchestration perfectly. The app is wired together with advanced multi-turn MeDo Skills, including an HTTP Request Skill (with custom header settings for user-provided GitHub tokens to bypass rate limits!) and a Data Processing Skill to clean massive file trees and protect the LLM's context window. Challenges we faced (and conquered) Handling large GitHub repo file trees without breaking the LLM’s input limit was a major hurdle. Even worse, the AI initially struggled with Mermaid.js syntax hallucinations, often hitting token limits mid-generation and cutting off the end tags of subgraphs, which crashed the visualizer. I solved this by increasing the MeDo output token limit and engineering highly strict system prompts that forced the AI to optimize tokens by grouping minor files and strictly following a bulletproof Mermaid syntax structure. What we learned We learned that MeDo isn't just for chatbots; with the right skills and orchestration, it can build powerful full-stack productivity tools that solve real-world engineering friction. We also became experts in "Vibe Coding" and Mermaid.js prompt engineering! <div