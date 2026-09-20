---
slug: "sentinel-way5bd"
url: "https://devpost.com/software/sentinel-way5bd"
title: "Sentinel"
hackathon: "OpenAI Build Week"
organization: "OpenAI"
winner: true
words: 1267
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "mechanism/measured_ablation"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Sentinel

> Catch security holes in your MCP server before you ship it. Static rules, GPT-5.6 review, and Docker-sandboxed probes-every finding mapped to the OWASP Agentic Top 10.

[Devpost](https://devpost.com/software/sentinel-way5bd) · hackathon [[OpenAI Build Week]]

## Facets

**mechanism** [[deterministic_policy]] [[human_in_the_loop]] [[measured_ablation]] [[multi_agent]] [[provenance_signing]] [[retrieval_grounding]] [[structural_withholding]]
**domain** [[developer_tools]] [[retail_commerce]] [[security_privacy]] [[supply_logistics]]
**user** [[legal_professional]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** codex, docker, github-actions, gpt-5.6, hatchling, jsonschema, mcp, model-context-protocol, mypy, openai, owasp, pydantic, pytest, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for sentinel

## Body

Inspiration I've been building agentic AI systems for a while now — RAG pipelines, multi-agent orchestration, the whole stack — and MCP servers are quickly becoming the default way agents get real capabilities: filesystem access, APIs, databases, shell commands. Every one of those servers is code you're trusting an agent to invoke without a human in the loop reading it first. The problem is nobody's really looking at that code. I'd come across MCP servers shared as gists, quick-start templates, half-finished side projects — a shell call with unsanitized input here, a hardcoded API key there, a tool with no auth boundary at all. None of that is unusual for a fast-moving ecosystem. What was unusual is that an agent will use all of it without hesitation, because agents don't know to be suspicious. There are plenty of security scanners for web apps and general codebases. I couldn't find one that understood what makes an MCP server specifically dangerous — tool schemas, declared permissions, the agent-shaped attack surface where a malicious tool result can hijack behavior just as easily as a malicious input can. So I built one. Sentinel is the build-time piece of a bigger idea I'm calling SecureMCP — a security suite that treats MCP the way real infrastructure gets treated: static analysis before deploy, a policy-enforcing gateway at runtime, and short-lived workload identity instead of long-lived credentials. Sentinel is the first piece. The other two are their own problems for later. What it does You point Sentinel at an MCP server and it tells you what's wrong with it. It works in three layers. Deterministic static analysis goes first — seven rules built on Python AST parsing plus Semgrep, covering things like unsafe execution, hardcoded credentials, missing input validation, excessive permissions, insecure prompt construction, missing auth, and unverified manifests. Then GPT-5.6 reviews each candidate finding in its actual source context — corroborating it, marking it a false positive, or flagging it for human review, with every decision required to cite real line ranges from the code. It also orders and parameterizes a plan for the next layer, but it can't write executable probe code or invent new findings — it's a reviewer, not an author. Then a Docker-isolated sandbox actually runs the server and fires four probes at it: out-of-scope tool access, oversized arguments, injection payloads, and malformed schema input. That's real behavior, not a guess about behavior. Every finding maps to the OWASP Agentic Top 10 and comes out as a console report, structured JSON, or validated SARIF 2.1.0 — which plugs straight into GitHub code scanning, so there's a GitHub Action that can fail a PR the moment someone adds an unsafe tool. How I built it I used Codex as my implementation partner throughout, but the architecture, security boundaries, and scope calls were mine. Before writing any code I spent a long session working through the design: what's MVP versus deferred, how findings map to OWASP categories, the allowed state transitions for a finding, and whether GPT review should be optional. It isn't — making it a toggle would have made it decorative instead of load-bearing. That planning session became the backbone everything else was built against. From there, Codex built the rule engine, the Docker sandbox, the reporting pipeline, the SARIF validator, and the cross-platform test matrix. I wrote an AGENTS.md with explicit instructions to ask rather than assume, which cut down a lot of the usual guessing you get when an AI is doing the typing. GPT-5.6 isn't just a build-time convenience — it's inside the shipped product. It runs through the OpenAI Responses API with strict Structured Outputs against a versioned schema, store: false , and redacted, capped context. Every review is host-validated: it can't cite a line of code that doesn't exist, can't invent a finding outside the rule set, and can't write probe code — it can only order and parameterize four fixed, inert probe templates. That constraint was the actual design problem: let the model genuinely change the output without letting it become the thing you have to blindly trust. Challenges I ran into GitHub silently disagreeing with my SARIF. Reports validated cleanly against the SARIF 2.1.0 schema and still didn't render right in code scanning. Took two separate fixes — one for location formatting, one for how dynamic-rule descriptors get declared. Semgrep on Windows. Output parsing behaved differently, and Semgrep's own runtime files collided with the scan workspace. Two commits and most of an evening for something that had worked first try on Linux and macOS. Paying for a demo. A scanner that calls a model costs real money every run — bad in CI, worse if a judge runs it repeatedly. I built a replay mode: real, previously captured GPT-5.6 responses replayed through the production parser, validators, and merge logic, still executing all four real Docker probes. No API key required to try it, and live artifact refreshes are hard-capped at $0.50. Deciding what happens when GPT is unavailable. Failing open means the scanner lies to you by staying quiet. So degraded mode is explicit and loud instead: candidates get parked in needs_review , and they still count toward the failure threshold rather than disappearing. Accomplishments that I'm proud of The demo runs with no API key and no source checkout — download a wheel, run one command, get real Docker probes and a validated SARIF report out the other end. There's a live GitHub code-scanning alert on a demo repo that Sentinel filed against itself. I'm also proud that fork pull requests never receive the API secret — they run visibly degraded and skip the code-scanning upload entirely. It would have been easy to quietly skip that edge case; I didn't. Beyond that: seven static detectors and four isolated dynamic probes, all mapped to the OWASP Agentic Top 10; all eleven expected findings demonstrated against a deliberately vulnerable fixture server while a hardened counterpart stays clean; a published, tested wheel with Linux/macOS/Windows CI; and a versioned ablation artifact that actually measures how much each layer — static rules, GPT review, dynamic confirmation — contributes, instead of just asserting that layering helps. What I learned Constraining a model is a lot harder than prompting one. Most of the GPT work in this project wasn't prompt engineering — it was building the cage: schema validation, source-range checks, inert probe templates, and provenance tracking on every finding so you can always tell what came from a deterministic rule and what came from the model. I also learned, the slow way, that "it validates against the schema" and "the platform actually accepts it" are two different claims — and that failure behavior is itself a security design decision. A scanner that silently skips GPT review, drops Semgrep results, or emits invalid SARIF isn't safer for staying quiet about it; it's creating false confidence. Sentinel distinguishes real findings from configuration and infrastructure failures on purpose, and refuses to present incomplete analysis as complete. What's next for Sentinel Publishing to PyPI is the near-term goal, along with more static rules — especially around tool-manifest verification and inter-agent communication — and support for scanning remote repository URLs and non-Python MCP servers. The bigger stretch goal is fixture-scoped exploit confirmation: using GPT-5.6 to generate a context-specific exploit plan for a known finding, running it inside the existing sandbox, and recording whether it's confirmed or a false positive. And eventually, the rest of SecureMCP: a runtime gateway and a short-lived credential broker, so the same policy that Sentinel enforces at build time follows a server all the way into production. <div