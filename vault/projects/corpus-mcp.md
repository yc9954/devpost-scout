---
slug: "corpus-mcp"
url: "https://devpost.com/software/corpus-mcp"
title: "Corpus Formation Autopilot"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 701
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/retail_commerce"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Corpus Formation Autopilot

> An open-source Qwen agent that turns "I sell sourdough from my apartment" into a cited launch checklist grounded in regional laws and a real, human-approved LLC filing.

[Devpost](https://devpost.com/software/corpus-mcp) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[deterministic_policy]] [[retrieval_grounding]]
**domain** [[civic_government]] [[developer_tools]] [[finance_payments]] [[legal_justice]] [[retail_commerce]]
**user** [[legal_professional]]
**substrate** [[document_pdf]] [[geospatial]] [[regulation_legal_text]] [[structured_db]] [[web_dom]]

**stack** alibaba-cloud, aurora, function-compute, mcp, next.js, node.js, openai-sdk, pgvector, postgresql, preact, qwen-cloud, qwen-flash, qwen3.7-max, serverless-devs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges
- what we learned
- what's next

## Body

Autopilot Formation Process Inspiration Ask a chatbot how to start a business and you get a confident listicle — no statutes, no local rules, and at the end, nothing exists. The two halves of the problem: AI that talks about law without reading it (50 states, ~19,000 municipalities, most of it never in training data), and AI that acts without accountability (nobody wants an LLM autonomously spending money and filing state documents). We'd already built the first half: Corpus (corpuslaw.us) indexes 491K+ provisions of US federal, state, and municipal law from official sources, vector + full-text searchable. This hackathon was the second half: an autopilot agent that acts — and the design question that consumed us was not "how much can it do?" but "where must it stop?" What it does The Formation Autopilot takes an ambiguous founder — "I sell sourdough from my apartment in Gulfport, make it official" — and drives a real business formation: it researches live against the hosted corpus, resolves the NAICS code, produces a launch checklist where every line carries a statute citation (Miss. Code Ann. § 75-29-951, the $20K cottage-food cap, the labeling rules), and then emits a prefilled handoff into a production checkout — where payment locks the filing payload to a SHA-256 hash , and exactly one human approves that exact hash or nothing happens. The agent never touches money. It never files. That boundary is architectural, not prompted. It also works for international founders: no US citizenship or SSN is required to form a US LLC, the registered agent ships bundled, and the agent refuses to accept ID numbers in chat — by rule. How we built it corpus-agent-kit (Apache-2.0): a thin TypeScript autopilot, a zero-dependency stdio MCP server, and an embeddable Preact widget (~12 kB) — all thin clients of the hosted platform. Open the connectors, never the organs. Two-lane Qwen Cloud routing : qwen-flash runs every conversational turn; qwen3.7-max wakes for exactly one — the pre-handoff draft review, where an error is expensive. Cost-shaped criticality, in routing.ts , not in a slide. Backend on Alibaba Cloud Function Compute 3.0 (us-west-1, custom runtime + Node20 layer, Serverless Devs config in autopilot/deploy/alibaba/s.yaml ), with a hard public spend cap (120 turns/hr). Guardrails in code, not prompts : a code-enforced search budget, a repeat-call guard, a fabricated-email dropper, an unknown-tool redirect, and a deterministic cited-checklist card that renders whether or not the model echoes it. Challenges The judge-killer we almost shipped: Function Compute's default domain injects Content-Disposition: attachment on HTML — curl checks passed for days while every real browser downloaded the demo instead of showing it. Fixed with CORS on the FC API + a hosted judge page (corpuslaw.us/autopilot). Prompts are UX; code is law. qwen-flash would search-spiral past its prompted budget, so budgets and guards moved into the loop itself. Late in the project we re-learned it: adding a large facts block to the system prompt measurably degraded rule-following (the agent stopped finalizing handoffs). Compressing it to one conditional rule restored the behavior. Prompt budget is a real budget. npm workspaces vs serverless packaging: the SDK hoisted to the root node_modules , the deploy packaged only the function directory, and the function died with ERR_MODULE_NOT_FOUND . A workspace-free staging install fixed it. Cold-start economics: our serverless database auto-pauses to control burn — first search after idle cost ~37s. We keep it warm through the judging window; the agent degrades gracefully (cites what it has, never fabricates) when search is slow. What we learned Trust in autonomous agents is architectural . The flagship-model review lane improves the draft, but the guarantee is the gate: payment hash-locks the payload, one human approves that exact hash, and a single byte of drift is rejected. Judges — and customers — don't have to trust the model's behavior, only the system's shape. What's next The MCP server is the distribution play: every AI client that installs it becomes a storefront for cited legal answers with a formation handoff at the end. More jurisdictions, the no-SSN EIN path for foreign founders productized, and the same gate pattern applied to every consequential action we let agents near. Coming to Smithery and other platforms before July 25th. <div