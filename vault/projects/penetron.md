---
slug: "penetron"
url: "https://devpost.com/software/penetron"
title: "Penetron"
hackathon: "UiPath AgentHack"
organization: "UiPath"
winner: true
words: 815
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Penetron

> Penetron proves vulnerabilities instead of just flagging them: an AI agent exploits your running app to confirm what's real, governed end-to-end by UiPath.

[Devpost](https://devpost.com/software/penetron) · hackathon [[UiPath AgentHack]]

## Facets

**mechanism** [[provenance_signing]]
  <sub>weak: on_device_local</sub>
**domain** [[developer_tools]] [[housing_homeless]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** anthropic, claude, claude-code, cloudflared, express.js, github-actions, model-context-protocol, node.js, playwright, react, typescript, uipath, uipath-agent-builder, uipath-maestro

## How they structured the write-up

- inspiration — security tools cry wolf
- what it does
- how i built it (uipath-native)
- the coding-agent bonus — claude code
- challenges i ran into
- what i learned
- what's next

## Body

Penetron Overview GHA Layer 1 security example UI Path Test Manager Dashboard MCP server terminal showing tools/call during the agent run (proves the cloud → tunnel → MCP bridge is live Claude Code driving the build / UiPath GUI How to update: Update Remote URL for MCP Server Penetron Security Gate Run app locally with remote tunnel History of GH Event that triggered an Agent Inspiration — security tools cry wolf SAST scanners and dependency checkers flag hundreds of *possible * vulnerabilities every release, and overwhelmed teams have no time to verify which are real. Real bugs get buried under unproven noise, and security becomes a late, manual gate that slows everyone down. I wanted to flip the model: instead of flagging candidates, prove or discard each one by actually exploiting the running app — and wrap the whole thing in UiPath's orchestration and governance, so it's automated where it should be and human-governed where it matters. That's the Track 3 thesis exactly: shift quality from a late-stage checkpoint into a continuous, intelligent, governed capability. What it does Penetron is a two-layer agentic security gate : Layer 1 — SAST + change-impact. Reads the PR diff, finds risky sinks inside the changed lines , and emits candidate findings scoped to the change — it doesn't re-scan the whole app every PR. Layer 2 — dynamic exploit validation. A UiPath Agent Builder agent (Claude Sonnet 4.6) calls Penetron's exploit engine over a Remote MCP server and runs real attacks — SQL injection, reflected/stored XSS, IDOR/BOLA, broken authentication — against the running app. It asserts on a genuine exploitation signal (payload renders unescaped, auth bypassed, another user's data returned 200 ), not a string match. Exploitability gate. Only exploited == true advances. The deliberately-safe endpoint is correctly discarded — no false positives . Evidence. Every verdict syncs to UiPath Test Manager as a red (exploited) or green (resisted) result, with screenshots and Playwright traces — an audit-grade "exploit locker." Governance. UiPath Maestro orchestrates the flow and keeps the full audit trail; a human-approval checkpoint is designed in before any external action; Slack posts a prioritized summary. Dev workflow. Penetron runs on every pull request and fails the required check — blocking the merge — when it proves an exploit. Headline result on the demo PR: Flagged 7 → proved 6, discarded 1. How I built it (UiPath-native) Target: an intentionally-vulnerable Express + React app ("Acme Demo Shop") with 6 planted OWASP bugs + 1 safe control + a VULNS.md ground truth, so I can prove precision . Engine: a TypeScript + Playwright exploit runner, the exploitability gate, a two-report generator, and contract JSON schemas (finding · attack-surface · verdict). UiPath platform: Agent Builder — the "Penetron Coordinator," a Low-code Agent (Claude Sonnet 4.6, temp 0) that runs verification. (Penetron does not use UiPath Coded Agents; the engine is external code reached via MCP.) Remote MCP Server — stateful Streamable-HTTP, 7 tools, with method-scoped auth (open discovery; execution gated by bearer or UiPath org-id). Test Manager / Test Cloud — S2S sync of verdicts to a test set + execution (live on tenant hackathon26_879 , project PEN : 6 Failed / 1 Passed). Maestro (BPMN) — orchestrates Start → agent verification → exploitability gate → end, with the audit trail. Orchestrator + Studio Web — solution packaging/deploy, folders, and a client-credentials External Application identity. The coding-agent bonus — Claude Code Claude Code was used in two distinct roles: (A) Penetron's analysis/exploit brain, and (B) the build-time engineer that wrote the engine, the MCP server, and the Test Manager sync — and drove the UiPath Studio Web / Orchestrator GUI (via Playwright MCP) to register the MCP server, bind the agent, and publish + run the Maestro process. Challenges I ran into Remote MCP over a tunnel. UiPath's agenthub proxy forwards an org-id but not our bearer at discovery time, so I built method-scoped auth (open discovery, gated execution). The quick cloudflared tunnel rotates each run — a proof-of-concept convenience; the production version runs the MCP server at a permanent URL. Action Center. I built the human-approval app, but the tenant returned an AppTasks 404 (Action Center not provisioned for our debug identity), so the approval node is designed but not live in the green run — a real platform limitation I documented rather than hid. What I learned Dynamic proof beats static flagging for precision — and pairs perfectly with an LLM agent: AI proposes, execution disposes. UiPath Test Manager is a natural evidence locker for security results, not just functional tests. A stable contract (the JSON schemas) keeps the heuristic and AI versions of Layer 1 interchangeable behind the same gate. What's next Automated Jira ticketing (prototype built, gated behind approval); live regenerate Layer 1 (Claude Code generating exploits from the diff); a native PR→UiPath auto-trigger; a permanent MCP endpoint with secrets in Orchestrator Credential Assets; <div