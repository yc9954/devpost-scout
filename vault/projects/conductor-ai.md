---
slug: "conductor-ai"
url: "https://devpost.com/software/conductor-ai"
title: "Conductor AI"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 535
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Conductor AI

> Agentic routing at scale for 66x cheaper and 4x faster — Powering the Agentic Future

[Devpost](https://devpost.com/software/conductor-ai) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[legal_justice]]
  <sub>weak: developer</sub>
**substrate** [[code_repository]] [[geospatial]] [[structured_db]]

**stack** agents, ai-agents, contrastive-learning, knn, python, pytorch, recommendation-systems

## How they structured the write-up

- agentic routing at scale: the cornerstone of an agentic future
- conductor composer
- codegen developer tool: swe-bench agent harness & evaluator
- team

## Body

GIF our team Agentic Routing At Scale: The Cornerstone of an Agentic Future Enterprises run a large number of agents, and being able to choose which agent to run a query on is a complex and expensive task. Routers exist today that can handle O(10) agents, but what about O(1000). Salesforce has O(10000) agents and — in a future where agents seem poised to replace many jobs — organizations may come to rely on the orchestration of O(1,000,000) agents with O(100,000,000) prompts/day . If we want a future driven by agents, with companies formed of agents, and to maximize performance/$ for inference, we need to solve the large-scale routing problem. The routing space is large and continuing to explode, and there exist no systems that can scale to the size that is needed. We develop a novel recommendation-system based algorithm for prompt routing, drawing inspiration from the TikTok algorithm Fortunately, our team (check below) is adept at handling matching problems at scale. Taking inspiration from the recommendation system at TikTok, ConductorAI matches queries and routers through a two-stage embedding approach, learning prompt and agent embeddings from exploring the interaction between the two and without manual encoding or intensive processing of either. Check out the technical details in our slides! ConductorAI: 66x cost savings, 4x latency reduction, better than any single AI model , and exponentially better performance with many agents ConductorAI provides unheard of speed and cost reduction at reasonable accuracy for an agent-driven future. Conductor implicitly learns a mapping between a semantic-embedding space and an agentic-embedding space, where coordinates correspond to features such as problem difficulty, tools required, and context that may be relative when deciding between agents. Additionally, adding agents to the system requires no hard-coded rules or descriptions, Conductor can naturally learn agent embeddings that exceed human performance. With A agents and P prompts, a traditionally LLM based router has inference scale on the order of O(PA), as each agent needs to be referenced in context, a classification-based router scales on the order of O(PA), and the theoretical perfect router scales at O(P). We scale at O(P log A) amortized, being the only neural-network based approach to do so. With the Intersystems vector search system, this O(log A) term is practically unnoticed. Conductor Composer To showcase the power of ConductorAI routing on practical problems, we have orchestrated an Agentic Suite around ConductorAI, incorporating agents for: Perplexity Search Code Generation Customer Service Database Management Executive Assistant HR Questions Legal Advice Software QA Web Automation Calendar Agent Here is our github repo containing our router, completely open-source: https://github.com/shloknatarajan/ariadne-routing Codegen Developer Tool: SWE-Bench Agent Harness & Evaluator For our code generation service, we extended it to provide a dev tool for Codegen users to run SWE-Bench on. We've made it very easy to run, test, and evaluate on SWE-Bench using Codegen's SDK, and included our own Codegen Agent that works on SWE-Bench. Here is the pull request containing the addition: https://github.com/codegen-sh/codegen-sdk/pull/521 Team Shlok Natarajan - Stanford University, Routing Research with Prof. Azalia Mirhoseini and Prof. Roxana Daneshjou Devan Shah - Princeton, Recommendation Systems at TikTok Advay Goel - MIT, Building @ Prod Victor Cheng - vly.ai , a Y Combinator company for Coding Agents <div