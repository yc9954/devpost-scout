---
slug: "agentops-black-box"
url: "https://devpost.com/software/agentops-black-box"
title: "AgentSight"
hackathon: "Splunk Agentic Ops Hackathon"
organization: "Splunk"
winner: true
words: 947
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/human_in_the_loop"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "mechanism/revocation_withdrawal"
  - "mechanism/sensor_fusion"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
---

# AgentSight

> Who watches the MCP agents querying your Splunk data? AgentSight does - native Splunk observability for AI agents: real MCP audit logs, agent-specific detections, and splunklib.ai investigation.

[Devpost](https://devpost.com/software/agentops-black-box) · hackathon [[Splunk Agentic Ops Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[human_in_the_loop]] [[on_device_local]] [[provenance_signing]] [[retrieval_grounding]] [[revocation_withdrawal]] [[sensor_fusion]]
**domain** [[accessibility]] [[developer_tools]] [[security_privacy]] [[transportation]]
**user** [[legal_professional]] [[researcher]]
**substrate** [[code_repository]] [[sensor_telemetry]]

**stack** bash, foundation-sec, mcp-(model-context-protocol), mit, ollama, powershell, python, rest-api, simple-xml, spl, splunk-ai-assistant, splunk-ai-toolkit, splunk-enterprise, splunk-mcp-server

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for agentsight

## Body

Inspiration Everyone is building agents that query Splunk. Almost nobody is building Splunk to watch the agents. As MCP clients and autonomous assistants get direct access to enterprise data through the Splunk MCP Server, security teams inherit a new blind spot: traditional detections were written for humans typing SPL, not for agents firing hundreds of splunk_run_query calls in minutes. I wanted to invert the usual hackathon story - instead of “an AI assistant that searches Splunk,” AgentSight asks: who governs the agents already inside Splunk? The Security track framing clicked immediately. Agent-native threats - runaway tool loops, scope violations, data-exfiltration SPL, prompt injection in tool arguments - need agent-native detections, AI-assisted investigation, and containment that still respects human approval. AgentSight is that layer: Splunk watches the agents that use Splunk. What it does AgentSight is a native Splunk app that provides observability and security for MCP clients and autonomous agents hitting your Splunk data. End-to-end flow: Observe - Ingests real Splunk MCP Server audit telemetry (index=_internal sourcetype=mcp_server, plus _audit/audittrail for scope and exfil signals). Detect - Five agent-native saved searches: MCP Tool Loop, Scope Violation, Off-Hours Burst, Data Exfiltration, and Prompt Injection. Investigate - Custom alert action agentsight_investigate runs a splunklib.ai agent with local tools; classify_agent_behavior calls | ai (Foundation-Sec via Ollama on Enterprise). Govern - Analysts review queued actions on the Approve Actions dashboard and run | agentsightapprove to approve or deny. Contain - On approval, quarantine revokes the rogue agent’s Splunk tokens via REST - never without human sign-off. Explain - | agentsightexplain turns a case into a plain-English summary in the search bar. The dashboard shows live MCP KPIs, an activity timeline, open cases, and pending approvals - so analysts see rogue agent behavior the moment it happens. How I built it AgentSight is a Splunk app (apps/agentsight/) installed into $SPLUNK_HOME/etc/apps/, built on verified MCP audit fields from Splunk MCP Server 1.2+. Splunk AI capabilities (runtime, not mock): splunklib.ai — Investigation and explain agents with seven local tools in bin/tools.py | ai (AI Toolkit) — Security classification via Foundation-Sec open weights in Ollama Splunk MCP Server — Primary telemetry source Custom alert action — agentsight_investigate Custom generating commands — agentsightapprove, agentsightexplain Architecture: MCP audit → normalization → five detection rules → AI investigation → index=agentsight cases → dashboard + async approval → optional token quarantine. Full diagram: architecture_diagram.md Stack: Python (Splunk’s embedded interpreter), splunk-sdk[ai], Splunk dashboards (Simple XML), bash + PowerShell demo scripts for Linux and Windows. Foundation-Sec runs locally through Ollama on Enterprise (Path A); hosted models on Splunk Cloud are supported as Path B. Built during the hackathon (first commit June 9, 2026). MIT licensed, open source. Challenges I ran into MCP audit discovery was the hardest gate. Telemetry lives in _internal/mcp_server, not a tidy CIM datamodel - I had to verify real field names (username, tool_name, request_id, etc.) before any detection could be trusted. Splunk AI on a single Enterprise box. Hosted Foundation-Sec only runs on Splunk Cloud, so I split responsibilities: llama3.2 for splunklib.ai tool orchestration, Foundation-Sec GGUF via | ai for security classification - same model family, two integration paths. Custom commands in Splunk are picky. Generating commands need a leading pipe (| agentsightapprove), not search agentsightapprove. PowerShell 5.1 and Splunk REST export quirks required a CLI fallback path for reliable demos. Human-in-the-loop UX. The approval queue initially showed stale cases until I deduped by latest case_id status - small SPL change, big analyst trust impact. Governance vs. speed. Full splunklib.ai investigation can take minutes; I added optional demo mode for rehearsals while keeping | ai classify on the real path. Accomplishments that I'm proud of A complete detect → investigate → approve → explain loop on real MCP audit traffic, not synthetic mock data. Five agent-native detection rules grounded in verified MCP and _audit fields — including exfiltration SPL and prompt-injection signatures. Multiple Splunk AI capabilities wired together in one app: MCP Server + splunklib.ai + | ai + custom alert action + custom commands. Governance by design - containment (token revoke) never runs without analyst approval; the investigation agent blocks dangerous SPL patterns itself. Cross-platform operability - bash scripts for Linux/macOS, PowerShell for Windows, judge quickstart in README, working dashboards with live KPIs (420 tool calls, open cases, pending approvals in the demo). Turning an underused telemetry source (MCP Server audit) into a first-class security surface inside Splunk. What I learned Agent security is a data problem first. Until MCP audit fields are mapped and trusted, no AI layer helps. Splunk’s AI stack is composable - splunklib.ai for orchestration, | ai for model calls, dashboards for humans - each piece has a distinct job. The best agentic security pattern is async approval, not autonomous remediation. Analysts need a queue, not a black box. Hackathon judges care about runtime integration. Calling Splunk AI from real alert actions matters more than architecture slides. Building for both Splunk Enterprise (Ollama Path A) and Splunk Cloud (hosted models) forces clearer abstractions - environment variables and ai.conf over hardcoded assumptions. What's next for AgentSight Scheduled detections + SOAR playbooks - ship with sensible defaults for production, with tuning guides per environment. Splunk AI Assistant integration - analyst copilot for ad-hoc SPL after AgentSight opens a case (complement, not replace, the investigation agent). Richer MCP coverage - more tools beyond splunk_run_query, per-agent risk scoring, and session correlation across request_id / session_id. Splunk Cloud Path B as default - hosted Foundation-Sec where available, Ollama fallback on Enterprise. AppInspect + Splunkbase packaging - hardened install, RBAC roles, and documented capacity planning for high-volume MCP fleets. Peer benchmarking - baseline “normal” agent behavior per team so detections tune from observed patterns, not static thresholds alone. <div