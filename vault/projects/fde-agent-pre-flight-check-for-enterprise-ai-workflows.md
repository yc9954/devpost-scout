---
slug: "fde-agent-pre-flight-check-for-enterprise-ai-workflows"
url: "https://devpost.com/software/fde-agent-pre-flight-check-for-enterprise-ai-workflows"
title: "FDE Agent: Pre-Flight Check for Enterprise AI Workflows"
hackathon: "UiPath AgentHack"
organization: "UiPath"
winner: true
words: 453
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# FDE Agent: Pre-Flight Check for Enterprise AI Workflows

> A BPMN-orchestrated diagnosis on UiPath Maestro that scores every workflow node for AI-delegation risk — and routes the dangerous ones to a human — before you ship.

[Devpost](https://devpost.com/software/fde-agent-pre-flight-check-for-enterprise-ai-workflows) · hackathon [[UiPath AgentHack]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]] [[retrieval_grounding]]
**domain** [[finance_payments]] [[health_clinical]]
**user** [[developer]]
**substrate** [[geospatial]] [[video_visual]]

**stack** bge-m3, chroma, claude-(claude-code), crewai-(designed-backend), python, uipath-action-center, uipath-coded-agents, uipath-maestro-bpmn, uipath-orchestrator, uipath-studio-web

## How they structured the write-up

- inspiration
- what it does
- how we built it
- built with claude code (platform usage +2)
- challenges
- what's honest

## Body

07_hitl_app 02_maestro_binding 08_r2_mixed 05_heatmap_loan 03_debug_run 01_maestro_canvas 06_dossier 04_orchestration Inspiration Enterprises ship AI into loan underwriting, contract review, and claims — and find out where it breaks only after it ships, when fixes are most expensive. 95% of GenAI pilots never reach production; Klarna walked back its automation; Air Canada was held liable for a fare its chatbot invented. The pre-deployment, workflow-level risk check only exists today as bespoke Big-4 consulting: one to two senior-weeks per workflow, non-standard, not re-runnable. What it does FDE Agent is a Forward Deployed Engineer as an agent. You feed it a workflow (BPMN, Mermaid, or an image). It scores every node on three risk axes — general failure, security, and handoff — against an ontology grounded in thousands of real AI incidents (AIID), OWASP LLM Top 10, MITRE ATLAS, the MIT taxonomy, NIST AI RMF, and the EU AI Act. The output is a per-node RED / AMBER / GREEN heatmap with cited evidence and multi-option mitigations. Critically, it detects "silent over-trust" on the handoffs between nodes — where a low-confidence step feeds an over-confident next step — and when that risk crosses threshold, the agent returns hitl_required = true. How we built it The diagnosis itself runs as a UiPath Maestro BPMN process on Automation Cloud. A Python Coded Agent (Start-and-wait-for-agent) computes the three axes in one governed call. A Maestro exclusive gateway reads hitl_required and routes high-risk cases to UiPath Action Center, where a human approves, modifies, or rejects on a full dossier — and the decision is written to the audit trail. UiPath is the execution, orchestration, and governance layer; the agent reasons inside the boundary; the human decides where the risk is real. In our Korean personal-loan underwriting demo, the engine flags four critical nodes — including the automated credit-scoring decision — and the gateway routes the case to a human instead of auto-approving. Built with Claude Code (Platform Usage +2) The whole system was built with Claude Code via UiPath for Coding Agents. It wrote the diagnosis core, the Coded Agent wrapper, the BPMN 2.0 XML, and the UiPath client (including a Cloudflare-1010 User-Agent workaround), and drove the auth → init → pack → publish CLI lifecycle. See README §7. Challenges UiPath Maestro Flow's Solution-publish and cross-folder Action App binding are known platform limitations (forum-acknowledged); we drove the agent orchestration via Debug provisioning and surfaced the human gate through the deployed Action Center app. What's honest The serverless agent runs ontology-only (degraded); full-corpus scores come from the local front and are shown as such. The CrewAI 5-role crew is a designed, selectable backend, not the demo runtime path — the demo runs the deterministic in-process engine. We claim only what we run. <div