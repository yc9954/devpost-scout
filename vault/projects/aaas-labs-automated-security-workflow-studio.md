---
slug: "aaas-labs-automated-security-workflow-studio"
url: "https://devpost.com/software/aaas-labs-automated-security-workflow-studio"
title: "AaaS Labs: Automated Security Workflow Studio"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 712
team_size: 0
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# AaaS Labs: Automated Security Workflow Studio

> AaaS Labs lets you talk to your code and domains, then run no‑code security workflows that trigger OWASP/SANS checks, scans, and AI‑generated remediation flowcharts

[Devpost](https://devpost.com/software/aaas-labs-automated-security-workflow-studio) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[developer_tools]] [[health_clinical]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]]

**stack** 25, django, github-api, gobuster, mongodb, nmap, node.js, owasp-top-10, python, react, reactflow, sans, shadcn-ui, sqlmap

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aaas labs: automated security workflow studio

## Body

Inspiration Modern apps ship faster than ever, often with AI‑generated code and complex cloud setups that quietly introduce new security risks.[web:105] Traditional scanners assume deep security expertise and force developers to juggle CLIs, dashboards, and scattered reports.[web:109] We wanted a way for teams to talk to their code and domains , then have security workflows assemble themselves—scans, explanations, and remediation paths included. That led to AaaS Labs: an automated attack and security lab where OWASP/SANS checks, network scans, and AI explanations all live behind a simple, no‑code workflow canvas. What it does AaaS Labs is an automated security workflow studio for codebases and deployed domains. It allows users to: Authenticate with GitHub and securely select repositories for scanning. “Talk to their code” using conversational AI to surface vulnerabilities and understand them in plain language. Build no‑code workflows that chain together OWASP Top 10 and SANS 25 checks, static analysis, and external security tools like Nmap, Gobuster, SQLMap, and WPScan. Generate AI‑driven remediation flowcharts that visually walk through how to fix each issue. Route results as Slack alerts, GitHub Issues, or email reports, with full report history and one‑click regeneration. Users can design separate workflows for code‑based scans and domain‑based scans , mixing and matching nodes based on what they care about most. How we built it We structured AaaS Labs as a set of collaborating services: Backends: Node.js and Django services manage authentication, workflow execution, and integration with security tools.[page:1] Security engine: Wrappers around Nmap, Gobuster, Nkito, SQLMap, WPScan, and custom OWASP/SANS checks handle both code and domain vulnerability detection. Frontend: A React + TypeScript interface with React Flow powers the no‑code canvas where users drag, drop, and connect nodes like Trigger, Scan, Flowchart, and Report.[page:1] AI layer: Conversational AI explains findings, answers “why is this bad?” questions, and turns raw scanner output into step‑by‑step remediation flowcharts. Integrations: GitHub OAuth for repo access, plus connectors for Slack, email, and GitHub Issues to deliver results where teams already work. We modeled workflows as directed graphs so they can be executed programmatically and visualized as UML/flowcharts for reports. Challenges we ran into Real‑time vs. accuracy: Running multiple scanners in parallel while keeping turnaround time low and false positives manageable required careful orchestration and batching.[page:1] Unifying diverse tools: Each security tool has its own CLI, output format, and quirks, so normalizing results into a single schema for AI and reporting was non‑trivial.[page:1] No‑code UX: Giving users powerful options (OWASP, SANS, network scans, domain scans) without overwhelming them on the workflow canvas took several iterations.[page:1] AI explanations: Translating noisy scanner logs into understandable explanations and actionable flowcharts demanded prompt tuning and output structuring.[page:1] We also had to optimize long‑running tools like Gobuster to bring scan times down from ~15 minutes to under 5 where possible. Accomplishments that we're proud of Built an end‑to‑end platform where a non‑expert can log in, connect a repo or domain, and ship an automated security workflow in minutes. Turned multi‑tool scans (OWASP/SANS, Nmap, SQLMap, WPScan, etc.) into a single , coherent report with AI‑generated remediation flowcharts.[page:1] Implemented conversational “talk to your code” support so developers can ask questions about vulnerabilities directly instead of decoding raw logs.[page:1] Delivered flexible reporting: Slack alerts for quick triage, GitHub Issues for backlog tracking, and email summaries for stakeholders. What we learned We learned how fragmented the security tooling ecosystem can feel when you’re not a specialist, and how much value there is in orchestration plus explanation .[web:105] Integrating classic tools (Nmap, WPScan, SQLMap) with AI made it clear that security isn’t just about detection; it’s about helping developers understand and act quickly.[web:107] Building a no‑code engine also taught us to think in graphs—how triggers, checks, and reports flow together to reflect real‑world security workflows. What's next for AaaS Labs: Automated Security Workflow Studio Add more security nodes and scanners, including cloud configuration checks and container security. Improve the AI layer with richer remediation suggestions and risk scoring across entire projects. Introduce team features: shared workflows, role‑based access, and scheduled scans integrated into CI/CD. Explore live monitoring modes that run lightweight checks continuously and surface regressions before they reach production.[web:105][page:1] AaaS Labs aims to make security automation feel less like a chore and more like a collaborative assistant that watches over your code and infrastructure. <div