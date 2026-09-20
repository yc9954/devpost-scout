---
slug: "asktra-the-cognitive-librarian-for-software-systems-mbx6zo"
url: "https://devpost.com/software/asktra-the-cognitive-librarian-for-software-systems-mbx6zo"
title: "Asktra: The Cognitive Librarian for Software Systems"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 696
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "user/developer"
  - "substrate/code_repository"
---

# Asktra: The Cognitive Librarian for Software Systems

> Asktra uses Gemini 3 to reconcile fragmented truths across Slack, Jira, and Git. It identifies "Why" code was written, detects policy violations, and automates post-mortem reconciliation.

[Devpost](https://devpost.com/software/asktra-the-cognitive-librarian-for-software-systems-mbx6zo) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[human_in_the_loop]] [[multi_agent]] [[provenance_signing]] [[realtime_stream]]
**user** [[developer]]
**substrate** [[code_repository]]
  <sub>weak: document_pdf</sub>

**stack** causal-reasoning, custom-css, deterministic-business-logic, eslint, fastapi, gemini-3, google-gemini-api, google-genai, google/genai, javascript, multi-agent-systems, net-business-value, next.js-14, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for asktra
- built with

## Body

Thinking stage steps Thinking steps and answers page Answer page Answer page Source aware New document creation for future use Sample data used Reconciliation Bundle Asktra — The Cognitive Librarian for Software Systems Inspiration Software systems don’t just break because of bad code — they break because of vanishing context . In modern enterprises, the “Truth” is fragmented across Slack messages, Jira tickets, Git commits, and release notes. When a senior engineer leaves, their why leaves with them. What remains is code without memory. We were inspired to build Asktra after repeatedly watching teams spend 70% of their time playing forensic detective — digging through chaotic chat logs and stale documentation just to understand why a critical security setting was changed months ago. We wanted to build a Cognitive Librarian that remembers why every line of code exists . What It Does Asktra is an investigative agent that reconstructs the Truth by weaving together fragmented signals from a company’s entire software stack. It doesn’t just search — it reconciles . Core Capabilities Causal Reasoning Traces a production bug back to a “temporary hack” mentioned in Slack six months ago. Contradiction Detection Flags when: Code (Git) violates a security policy (Docs), or A production release contradicts explicit human intent (Slack). Sync Reality Generates PR-ready documentation and Reconciliation Bundles — including: Post-mortem incident reports Remediation code patches (diffs) Stakeholder-ready Slack summaries These bundles bridge the gap between intent and reality . How We Built It Asktra is powered by Gemini 3’s high-reasoning engine , using a multi-agent architecture : The Agents Context Weaver Leverages Gemini’s long-context window to ingest 50+ pages of policy and months of Slack history , performing temporal grounding to track how a crisis evolved over time. Policy Enforcer Audits Git commits against SOC2 and internal compliance mandates, flagging violations even when Jira says an issue is “Resolved.” Resource Allocator Reconciles Jira backlogs and human constraints to suggest “Third Path” solutions during organizational conflicts. Deterministic Business Logic We implemented a deterministic financial layer to compute Net Business Value : We implemented a deterministic financial layer to compute Net Business Value : Net Business Value = (Revenue Saved + Liability Mitigated) − Direct Cost This ensures Asktra’s recommendations are not just correct — they are economically justified . Frontend Design The UI is built around Investigative Flow , allowing users to: See the 22-step reasoning trace Inspect every source Verify exactly how Asktra reached its conclusions Challenges We Ran Into Causal Disconnect One of the hardest problems was Causal Disconnect — when Slack, Jira, Git, and Docs all disagree. We had to teach Gemini not to choose a source, but to: Identify the Truth Gap Flag it as an active risk Preserve contradictions instead of smoothing them over High-Stakes Security Because Asktra operates in security-critical environments, we implemented a cryptographic Audit Signature (SHA-256) for every reasoning trail. This ensures Asktra’s outputs are tamper-evident and audit-admissible in real-world compliance reviews. Accomplishments We’re Proud Of The Reconciliation Bundle is our biggest win. Watching Asktra: Detect a 90-second timeout violation, Identify the human intent behind it, Generate the exact code diff to fix it, Write the post-mortem, And draft the Slack message to align the team… …was a true wow moment. We also proved that AI can handle Triple Conflict scenarios — balancing Engineering, Security, and Business constraints simultaneously. What We Learned We learned that context is the ultimate currency . Modern reasoning models like Gemini 3 aren’t just conversational — they are capable of organizational logic across time, policy, and human intent. We also learned the importance of Human-in-the-Loop design . Asktra doesn’t replace engineers; it acts as an Investigative Co-pilot , presenting evidence and reasoning for human authorization. What’s Next for Asktra Our next milestone is Proactive Drift Detection . Instead of waiting for someone to ask a question, Asktra will: Monitor conversations and commits in real time Detect when decisions begin to drift away from policy Alert teams before a security or compliance failure happens Our goal is for Asktra to become the immune system for the world’s most critical software. Built With Gemini 3 Multi-Agent Systems Vertex AI Node.js / React SHA-256 Cryptographic Auditing <div