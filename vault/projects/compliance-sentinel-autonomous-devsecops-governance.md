---
slug: "compliance-sentinel-autonomous-devsecops-governance"
url: "https://devpost.com/software/compliance-sentinel-autonomous-devsecops-governance"
title: "Compliance Sentinel — Autonomous DevSecOps Governance Agent"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 1115
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/web_dom"
---

# Compliance Sentinel — Autonomous DevSecOps Governance Agent

> AI agents that enforce SOC2, HIPAA, PCI-DSS & GDPR as code on every merge request — with automated merge gating, auto-remediation, and conversational compliance analytics via MCP.

[Devpost](https://devpost.com/software/compliance-sentinel-autonomous-devsecops-governance) · hackathon [[GitLab AI Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]] [[structural_withholding]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]] [[patient_family]]
**substrate** [[code_repository]] [[geospatial]] [[regulation_legal_text]] [[web_dom]]

**stack** agent, bigquery, claude, duo, fastmcp, functions, gitlab, google, looker, mcp, mermaid, node.js, platform, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for compliance sentinel — autonomous devsecops governance agent

## Body

Google Looker Studio Dashboard from BigQuery GitLab Native Dashboard MCP Server Integration - Claude Desktop MCP Server Integration - Claude Desktop Inspiration Enterprise compliance is a \$30B+ annual problem . Manual security reviews add days to every release — typically \(d \in [3, 14]\) depending on organization size. Audit preparation consumes ~2–4 weeks of evidence gathering per cycle. Developers context-switch between writing code and understanding SOC2, HIPAA, PCI-DSS, and GDPR — often making mistakes that aren't caught until production. The compliance gap can be expressed simply: $$\text{Risk} = \frac{\text{Violations} \times \text{Time to Detect}}{\text{Remediation Capacity}}$$ Manual processes maximize the numerator and minimize the denominator. We asked: what if compliance was autonomous, continuous, and built into the GitLab workflow itself? What it does Compliance Sentinel is an autonomous DevSecOps governance platform on the GitLab Duo Agent Platform that enforces 4 regulatory frameworks as executable policy-as-code. Compliance Scoring Model: $$S_f = 100 - \sum_{i=1}^{n} w(s_i) \quad \text{where } w(s) = \begin{cases} 15 & s = \text{Critical} \ 8 & s = \text{High} \ 3 & s = \text{Medium} \ 1 & s = \text{Low} \end{cases}$$ Each framework \(f\) starts at 100 and receives deductions per finding based on severity. The overall compliance posture is the weighted aggregate across all \(k\) frameworks: $$S_{\text{overall}} = \frac{1}{k}\sum_{f=1}^{k} S_f, \quad S_f \geq 0$$ Core Capabilities: MR Compliance Review — Every merge request is automatically scanned against 25 regulatory controls and 100+ detection rules. Findings are posted as MR comments with per-framework scores, evidence (secrets always masked), and remediation guidance. Non-compliant MRs are blocked from merging with compliance::failed labels. Auto-Remediation — Critical findings generate tracking issues. The auto-remediator agent reads the violation, generates a fix, commits to a new branch, and opens a merge request — autonomously. No developer context-switching needed. Compliance Auditing — Full-repository audits triggered on demand via issue mentions. Comprehensive reports with severity breakdowns and tracking issues for every finding. Google Cloud Analytics Pipeline — Every scan feeds BigQuery via a Cloud Function webhook. An executive dashboard renders natively inside GitLab using Mermaid charts. The same data powers a Looker Studio dashboard for enterprise stakeholders. MCP Server for Conversational Compliance — Developers query compliance data through Claude Desktop using natural language: "What's our HIPAA posture?" or "List all critical findings." Four BigQuery-backed tools make compliance conversational. How we built it Policy-as-Code Engine All compliance requirements are declarative YAML — .compliance/policies/ maps regulatory controls to detection rules, .compliance/rules/ defines 100+ regex patterns and structural checks across 5 categories. Adding a new framework means adding a YAML file. The detection surface covers: Category Patterns Examples Secrets Detection 14 AWS keys ( AKIA* ), GCP keys, private keys, tokens Coding Standards 10 SQL injection, XSS, command injection, weak crypto Data Handling 5 PII/PHI in logs, sensitive data in URLs IaC Security 22 Public S3 buckets, root containers, wildcard RBAC License Compliance 3 tiers Permissive, copyleft, non-commercial $$N_{\text{total}} = \sum_{c=1}^{5} n_c = 14 + 10 + 5 + 22 + 3 = 54 \text{ base patterns} \rightarrow 100+ \text{ rules with framework mappings}$$ GitLab Duo Agent Platform Three autonomous flows registered in the AI Catalog, each with specialized system prompts that embed the full policy engine. The agent leverages GitLab-native tools: get_merge_request / list_merge_request_diffs — read MR context get_repository_file / list_repository_tree — access source code create_issue / create_merge_request — enforcement actions create_note / update_merge_request — reporting and labeling Google Cloud Integration A Cloud Function receives webhook events from GitLab, parses compliance reports, and loads structured data into BigQuery: Table Purpose scan_history Scan metadata, overall scores, timestamps findings Individual violations with severity, framework, file location framework_scores Per-framework scores and finding counts per scan A Python dashboard generator queries BigQuery and renders Mermaid charts as a GitLab issue. One-command deployment via gcp/deploy.sh . MCP Server Built with FastMCP (Python), exposing 4 BigQuery-backed tools over stdio transport: get_compliance_summary — current scores across all frameworks get_compliance_findings — detailed findings with filters get_compliance_trends — score trends over time get_framework_details — deep-dive into a specific framework Claude Desktop connects directly — no HTTP server, no authentication overhead. Sample Application \(55+\) intentional violations across a Node.js patient portal API serve as test cases — hardcoded AWS keys, SQL injection, PHI in logs, weak cryptography, missing GDPR endpoints, and more. Challenges we ran into Multi-agent flow reliability : Our original 13-agent DAG architecture experienced WebSocket premature closures on the Duo Agent Platform. We solved this by consolidating into single-agent flows with exhaustive prompts that embed the full policy engine — maintaining architectural correctness while achieving production reliability. IDE-only tool limitations : Several GitLab tools ( find_files , read_file , grep ) only work in IDE environments, not in ambient flows. We discovered this through debugging and switched to web-compatible alternatives ( get_repository_file , list_repository_tree , gitlab_blob_search ). AI Catalog caching : Flow definition updates were silently cached server-side. We learned to create new flow files with fresh names to bypass stale cache — a non-obvious operational pattern. Non-deterministic scoring : The AI reviewer produces variance across runs with identical input. We designed the scoring formula to be fully transparent — \(S = 100 - \sum w(s_i)\) — so the methodology is deterministic even when individual assessments vary. Accomplishments that we're proud of [x] Full autonomous loop : MR push \(\rightarrow\) compliance report \(\rightarrow\) merge gate \(\rightarrow\) tracking issue \(\rightarrow\) auto-remediation MR — zero human intervention [x] 100+ detection rules across 4 frameworks — all declarative YAML, extensible by adding a file [x] Native GitLab experience — reports on MRs, dashboards as issues, tracking issues linked to findings. Nothing leaves GitLab [x] Three integration layers — GitLab Duo for enforcement, Google Cloud for analytics, MCP for conversational access [x] Measurable improvement — compliance score \(25 \rightarrow 72\), a \(\Delta S = +47\) point improvement tracked in BigQuery What we learned The GitLab Duo Agent Platform transforms what would be months of integration work into days of focused development. Having native access to merge requests, issues, labels, and repository files through the agent's tool ecosystem means you spend time on your domain problem rather than on plumbing. The key insight: treat compliance requirements as structured data \(\mathcal{P} = \{(\text{framework}, \text{controls}, \text{rules})\}\) that AI agents can reason about — rather than hardcoding detection logic. This makes the system extensible by \(O(1)\) effort per new framework. What's next for Compliance Sentinel — Autonomous DevSecOps Governance Agent Additional frameworks — FedRAMP, ISO 27001, and NIST 800-53 as new YAML policy files Pipeline-native scanning — CI/CD stage alongside existing SAST/DAST for shift-left compliance Compliance drift detection — Scheduled audits alerting on \(\Delta S < -\theta\) regression Multi-project governance — One instance governing an entire GitLab group AI-powered policy authoring — Duo translates plain-English regulations into Policy-as-Code YAML <div