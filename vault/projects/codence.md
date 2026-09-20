---
slug: "codence"
url: "https://devpost.com/software/codence"
title: "Codence"
hackathon: "HP & NVIDIA Developer Challenge"
organization: "HP"
winner: true
words: 290
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
---

# Codence

> Codence is an AI agent that turns meeting decisions into enforceable specs by syncing Jira tickets and validating GitLab code against agreed rules.

[Devpost](https://devpost.com/software/codence) · hackathon [[HP - NVIDIA Developer Challenge]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** ai-studio, docker, flask, hp, openai, python

## How they structured the write-up

- 🧠 about the project

## Body

🧠 About the Project What inspired us Modern product development moves fast, but alignment often lags behind. Now, with AI tools writing code faster than ever, we’re seeing an ironic gap: speed has increased — but product quality hasn’t. Teams can generate code in seconds, but if that code doesn’t reflect the latest meeting decisions, it's just fast wrong work. We were inspired by this growing mismatch between decision-making and implementation . PMs spend hours manually checking Jira tickets. Developers unknowingly violate specs that were never updated. We asked: What if an AI could watch over these processes and enforce alignment? That’s how Codence was born — to make sure product consensus becomes code reality. What we learned We learned that: Meeting notes are messy, but full of hidden structure. Developers don’t ignore specs—they often never see them. The gap between decisions and delivery is often process, not intent. We also realized how powerful LLMs can be when paired with source-of-truth systems like Jira and GitLab. How we built it Frontend : A minimal web interface for uploading meeting notes and reviewing suggestions. Backend : Python + FastAPI with GitLab webhook integration. AI : GPT-based models extract decisions and rules from unstructured meeting notes. DevOps : GitLab Webhook triggers Codence to validate PRs against extracted rules. Jira Integration : Syncs ticket updates through REST APIs after human approval. Challenges we faced Parsing casual, non-standard meeting notes into structured intent. Mapping natural language decisions to specific Jira tickets and code actions. Avoiding false positives in code rule checks while keeping responses fast. Making the AI explain why something violates a rule in human-readable terms. Despite the constraints of time and scope, we’re proud that Codence brings alignment closer to automation. <div