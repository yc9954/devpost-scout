---
slug: "devops-commander"
url: "https://devpost.com/software/devops-commander"
title: "DevOps Commander"
hackathon: "Codegeist 2025: Atlassian Williams Racing Edition"
organization: "Atlassian"
winner: true
words: 313
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/sensor_telemetry"
---

# DevOps Commander

> DevOps Commander app is an AI powered DevOps copilot in jira that turns Natural Language requests into actionable incident response guidance for software teams.

[Devpost](https://devpost.com/software/devops-commander) · hackathon [[Codegeist 2025- Atlassian Williams Racing Edition]]

## Facets

**domain** [[developer_tools]] [[health_clinical]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[sensor_telemetry]]

**stack** atlassian, forge, jira, kubernetes, node.js, rovo, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for devops commander

## Body

Inspiration Running Kubernetes clusters and GitOps pipelines for real teams and understanding the architectures, incident impact, Health, is really hard. So, I have built DevOps Commander an forge-based Rovo agent that brings AI-powered automation directly into Jira. What it does It reads Kubernetes and GitOps signals, that generates clear remediation plans, incident summaries and Jira ready action items. It helps software teams turn noisy dashboards into structured, and production-ready guidance in a few clicks. How we built it We built DevOps Commander as an Atlassian Forge app using the rovo:agent module and Node.js/TypeScript functions to handle custom actions. A CKA Health Dashboard running on Kubernetes provides real cluster metrics, which the agent uses as context to reason about health, incidents, and deployment risk. Challenges we ran into Getting the Forge manifest and modules configured correctly with rovo:agent and custom action handlers caused several validation and bundling errors that we had to debug. Connecting realistic Kubernetes signals into a short hackathon timeline while keeping the UX simple inside Jira was another big challenge. Accomplishments that we're proud of I went from a blank Forge project to a working AI SRE copilot that deploys successfully to the Forge production environment. The app can already analyze cluster health, summarize incidents, review GitOps status, and propose next steps directly from a Jira issue. What we learned I learned how to design and ship a production‑ready Forge app, including environments, deployments, and diagnostics in the Atlassian Developer Console. We also deepened our understanding of how Rovo agents can orchestrate external tools and data sources to assist software and SRE teams. What's next for DevOps Commander Next, I am planning to replace placeholder handlers with real integrations to Kubernetes clusters, Git providers, and observability tools. We also want to add playbook templates, auto‑generated runbooks, and richer analytics so teams can continuously improve their incident response and deployment strategies. <div