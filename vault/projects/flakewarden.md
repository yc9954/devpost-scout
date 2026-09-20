---
slug: "flakewarden"
url: "https://devpost.com/software/flakewarden"
title: "FlakeWarden"
hackathon: "UiPath AgentHack"
organization: "UiPath"
winner: true
words: 914
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# FlakeWarden

> Agentic flaky-test triage for UiPath Test Cloud: a deterministic scorer and a grounded AI classifier separate real defects from flaky tests, with a human approving every fix.

[Devpost](https://devpost.com/software/flakewarden) · hackathon [[UiPath AgentHack]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]]
**domain** [[health_clinical]] [[housing_homeless]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[web_dom]]

**stack** anthropic-claude, claude-code, github, pytest, python, uip-cli, uipath-action-center, uipath-agent-builder, uipath-ai-trust-layer, uipath-automation-cloud, uipath-coded-agents, uipath-context-grounding, uipath-for-coding-agents, uipath-maestro

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments i'm proud of
- what i learned
- what's next for flakewarden

## Body

FlakeWarden: agentic flaky-test triage for UiPath Test Cloud. Is a red build a real defect, a flaky test, or an environment problem? Architecture: a deterministic flake-scorer handles the clear cases; a grounded Agent Builder classifier reasons over the ambiguous ones. Live agent verdict: real defect (selector change at the break). It proposes no fix, because you never auto-heal a real bug. Live agent verdict: flaky (stale-element timing, no code change). It proposes a selector/wait fix, gated for human approval. Live agent verdict: environment (503 from an upstream service). Re-run on clean infrastructure; don't blame the test or the code. Measured on a 150-case labeled corpus: 90.7% accuracy and a 0% safety false-positive rate, enforced by a mechanism, not planted. UiPath Maestro orchestrates the flow: failing test to Triage Classifier to a verdict gateway that routes each class to the right action. The Triage Classifier, published v1.0.0 and deployed as a live Orchestrator process on UiPath Automation Cloud. Built with a coding agent: Claude Code drives the UiPath uip CLI to deploy the agent and author the Maestro orchestration. The Maestro BPMN was authored through the uip CLI and passes uip maestro bpmn validate cleanly. The problem, grounded: Google reported ~16% of tests showed flakiness and ~84% of pass-to-fail transitions came from flaky tests. Inspiration Flaky tests are the most corrosive failure mode in CI. When a build goes red, an engineer often cannot tell a real regression from noise, so they either burn 15 to 45 minutes triaging every failure or, worse, start ignoring red builds until a genuine regression ships. Google's continuous-testing data (J. Micco, Google Testing Blog, 2016; corroborated by Memon et al., ICSE-SEIP 2017) reported about 16% of their tests showed some flakiness and about 84% of pass to fail transitions came from flaky tests. I wanted an agent that answers the only question that matters: real defect, flaky, or environment. It never hides a real bug, and it keeps a human in charge of every change. What it does FlakeWarden triages a failing test and routes it to the right action: A deterministic, auditable flake-scorer (exact statistics over run history) resolves the confident cases and never guesses. A grounded UiPath Agent Builder classifier reasons over the messy evidence (stack trace, DOM/selector diff, commit message, runner logs) only for the ambiguous failures, and labels each one real_defect, flaky, or environment. It proposes a selector/synchronization fix only for flaky tests, and every quarantine, heal, or baseline change is a human-gated proposal, never an autonomous mutation. It runs under a hard safety contract: a real regression is never auto-quarantined as flaky. On a 150-case labeled corpus it yields 90.7% accuracy and a measured 0% safety-direction false-positive rate, enforced by a mechanism, not planted in the data. How I built it The whole solution was designed and built with Claude Code through UiPath for Coding Agents, combining a coded agent with a low-code Agent Builder agent: Deterministic flake-scorer, grounded classifier interface, evaluation harness, and labeled corpus authored as Python (a UiPath Coded Agent). The Triage Classifier built in UiPath Agent Builder (Studio Web): grounded context, a structured output schema, and an evaluation set, running on the UiPath Automation Cloud. UiPath Maestro orchestrates the scorer, the classifier, and a human-review Action Center task; the deterministic-vs-generative split keeps exact math where it belongs and spends the model only on the ambiguous middle. Challenges I ran into An early version of the evaluation was circular: the corpus encoded the exact signals the model read back. I caught it in an adversarial self-review and de-rigged the corpus (noisy signals, decoupled vocabulary, genuine conflict cases), re-measuring at an honest 90.7% instead of a tautological number. Making the 0% safety rate real, not designed: it is now enforced by a flaky-band regression guard plus a tie-break toward real_defect, so a real bug can never be silently healed. UiPath platform learning curve: binding prompt arguments uses the @ picker (not {{ }} typed text), and the in-product agent evaluator could not route its model in the EU tenant (HTTP 417 data-residency). The agent itself runs fine; the evaluator model routing is a real gap I am submitting as product feedback. Accomplishments I'm proud of A grounded classifier agent running live on UiPath that classifies real_defect, flaky, and environment with correct, evidence-cited reasoning, published v1.0.0 and deployed as an Orchestrator process. A Maestro BPMN orchestration authored end to end through the UiPath uip CLI (Claude Code), validating clean against uip maestro bpmn validate . A measured 0% safety-direction false-positive rate that is earned by a mechanism, with a negative-control gate that proves no real defect is ever auto-healed. A clean deterministic-vs-generative architecture that spends the LLM only where it adds value (about a third of failures resolve with no model call). What I learned Evaluation-driven development is only honest if the eval set is decoupled from the model under test. Self-review and de-rigging mattered more than the headline number. Where rules belong versus where generative reasoning belongs: exact statistics for structured history, grounded LLM reasoning for messy multi-source context. Practical UiPath Agent Builder, Maestro, Context Grounding, and the uip CLI for coding agents, including data-residency constraints in EU tenants. What's next for FlakeWarden Wire the full Maestro process and Action Center human gate end to end. Connect the live Test Manager results API in place of the seeded corpus, then run a shadow-mode prospective study to report real-world accuracy. Add drift monitoring so the scorer thresholds re-tune as the suite evolves. <div