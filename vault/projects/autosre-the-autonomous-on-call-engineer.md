---
slug: "autosre-the-autonomous-on-call-engineer"
url: "https://devpost.com/software/autosre-the-autonomous-on-call-engineer"
title: "AutoSRE: The Autonomous On-Call Engineer"
hackathon: "Google Cloud Rapid Agent Hackathon"
organization: "Google"
winner: true
words: 1066
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
---

# AutoSRE: The Autonomous On-Call Engineer

> AutoSRE is an autonomous on-call agent that diagnoses Dynatrace incidents in seconds and queues up the fix, but cannot touch production without your one-tap approval.

[Devpost](https://devpost.com/software/autosre-the-autonomous-on-call-engineer) · hackathon [[Google Cloud Rapid Agent Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[on_device_local]] [[provenance_signing]] [[sensor_fusion]] [[structural_withholding]]
**domain** [[accessibility]] [[developer_tools]] [[health_clinical]] [[housing_homeless]] [[labor_employment]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[sensor_telemetry]] [[transcript_audio]]

**stack** agent-development-kit, cloud-run, docker, dynatrace, fastapi, gemini, google-cloud, mcp, next.js, opentelemetry, playwright, pytest, python, react

## How they structured the write-up

- status:
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for autosre: the autonomous on-call engineer

## Body

Logo Logo Security Card Status: The hosted demo was retired after the hackathon. The Cloud Run deployment was shut down once judging finished, so the live demo link no longer resolves. The project still runs locally with no accounts needed: see the Quickstart in the GitHub repo, or set AUTOSRE_DEMO_MODE=1 for the deterministic, model-free replay. The demo video below shows the system running live against the real Dynatrace tenant. Inspiration Production incidents are expensive and miserable in a very specific way: the fix usually takes a minute, but finding it takes the 3am engineer 30+ minutes of dashboards, queries, and correlation. Industry context for the stakes, not my measurement: Gartner's widely cited 2014 figure puts IT downtime at $5,600 per minute , and EMA Research's 2024 analysis at roughly $14,056 per minute . What I measure on screen is the part AutoSRE actually changes: the investigation. The other inspiration was healthy skepticism. Most agent submissions focus entirely on blind execution. We built for the moment the agent is told no. What it does AutoSRE detects a production incident from Dynatrace, diagnoses the root cause from live telemetry with Gemini 3, proposes exactly one fix , and stops until a human approves it. The agent runs a 6-step loop (demonstrable entirely locally via a bundled deterministic mock, or live against a real Dynatrace tenant): DETECT : pull open problems from Dynatrace. DIAGNOSE : run DQL queries to correlate the problem with recent changes. PROPOSE : name exactly one remediation (disable flag, rollback, scale). PAUSE : block until a human approves (ADK-native require_confirmation=True , not a prompt). ACT : execute the approved remediation. VERIFY : re-check service health and confirm recovery. The value: triage that takes an on-call engineer 30+ minutes by hand happens in the seconds shown on the demo's live timer, with a human still owning every change that reaches production. What makes it different: The refusal is the product. Remediation tools are wrapped in ADK require_confirmation=True : the model cannot touch production without a human decision, and a rejection stands the agent down with nothing changed. Both outcomes are audited on Dynatrace's own timeline. An append-only ledger records who decided, what, and the outcome, then writes it back to the tenant : approved / resolved or rejected / declined . Dynatrace MCP is load-bearing. It is the agent's only sensory system; detection runs on a live DQL query against real OpenTelemetry. Graded, not vibes. A 25-run eval grades the live agent against an answer key it has no tool to reach : 25/25 correct, 0/25 false actions (0%), 5/5 no-action traps refused, median 13.3s detect-to-proposal. Results export to the same Dynatrace tenant the agent monitors and render live at /reliability . How we built it Reasoning engine: Gemini 3 via Vertex AI ( gemini-3-flash-preview ). Agent framework: Google Cloud's Agent Development Kit (ADK) , the code-first surface of the Agent Platform. Self-hosted on Cloud Run ; the same agent is deployable to Vertex AI Agent Engine . Observability partner: the Dynatrace MCP server . Read-only tools ( query_problems , execute_dql , get_kubernetes_events ) drive detect, diagnose, and recovery confirmation. Remediation tools: Python FunctionTool with require_confirmation=True , each machine-bounded by server-side allow-lists (replica band, known-good versions, managed flags) so out-of-bounds actions fail closed even when approved. Web UI: Next.js 16 + Tailwind v4 "Mission Control" that streams the loop live over typed SSE frames and renders the approval gate as a blocking modal. Backend: FastAPI with per-run sessions and a pause/resume bridge: the loop parks on a future until the approval POST resolves it. Defense in depth: an untrusted-telemetry guardrail (all Dynatrace data is evidence, never instructions), per-IP rate limits, a single-active-run guard, and a demo target that never leaks the answer key , so the diagnosis is genuine reasoning rather than a lookup. Challenges we ran into Holding an SSE stream open across a human pause. I built a per-run state machine that parks the agent loop on a future and resumes the same ADK session when the decision arrives. Auditing the refusal correctly. ADK emits a confirmation stub for the gated tool before the human decides, which a naive classifier miscounts as "acted". I derive the decision from the operator's actual choice and pinned it with deny-path regression tests. Gemini rate limits. The free tier allows ~5 requests/minute and a full loop makes 4 to 5 model calls. The shared loop backs off and resumes on 429/503, honoring the API's suggested retry delay, and surfaces the wait in the UI instead of hanging. Grading a nondeterministic agent honestly. I built an eval harness with a pre-registered pass criterion, decoy incidents where the reflex fix is wrong, and a no-action trap, scored against an answer key the agent has no tool to reach. Accomplishments that we're proud of The full 6-step loop deployed and verified live : detect, diagnose, propose, pause, act, verify, with the approval gate enforced by the framework. 25/25 graded runs correct, 0/25 false actions, 5/5 no-action traps refused , median 13.3s detect-to-proposal, with timestamped transcripts committed and the results queryable in the Dynatrace tenant via DQL. Both the approval and the refusal land in an append-only audit trail and write back to Dynatrace, with an honest sent vs verified badge. A 71-test suite (70 deterministic offline, 1 live-gated) pinning the deny path, the allow-list bounds, rate limiting, and the eval aggregation. A 50-check security audit with the scorecard published in SECURITY.md What we learned The approval pause is the product. A framework-enforced gate is stronger than any prompt instruction, and stronger still when backed by machine bounds that fail closed. I also learned to treat telemetry as attacker-influenceable input: the agent reads it as evidence to summarize, never as instructions to follow. And I learned that grading an agent against an answer key it cannot see changes how you build everything upstream of it. What's next for AutoSRE: The Autonomous On-Call Engineer Multi-incident concurrency beyond the one-run-per-session model. Deeper Dynatrace integration : Davis AI problem context, change events, SLO violations. Slack / PagerDuty approvals in the tools on-call teams already live in. Default-on second-opinion verifier : an independent Gemini pass that critiques the fix before the human sees it (shipped today as opt-in). Richer graduated autonomy : risk tiers are shipped; per-action policy configuration is next. CI as a regression gate on the eval harness, with a broader scenario pool. <div