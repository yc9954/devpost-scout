---
slug: "proofsift"
url: "https://devpost.com/software/proofsift"
title: "ProofSIFT"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 3926
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/formal_verification"
  - "mechanism/graph_reasoning"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ProofSIFT

> Evidence-proven autonomous DFIR triage that confirms findings only with traceable forensic artifacts, self-corrects weak claims, and generates audit-ready reports with SQLite provenance.

[Devpost](https://devpost.com/software/proofsift) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[formal_verification]] [[graph_reasoning]] [[on_device_local]] [[provenance_signing]]
**domain** [[health_clinical]] [[legal_justice]] [[security_privacy]] [[supply_logistics]]
**user** [[legal_professional]] [[researcher]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** audit-logging, csv, git, json/jsonl, mcp-(model-context-protocol), python-3.10+, sqlite-3, trace-indexing

## How they structured the write-up

- neuro-symbolic, self-correcting autonomous dfir triage agent
- 💡 inspiration — solving the llm hallucination problem in dfir
- 🏆 judging criterion mapping
- ⚙️ what it does
- 🧠 the neuro-symbolic core — three "god-tier" integrations
- 🗂️ demo case evidence
- 📊 benchmark results — precision 1.0, recall 1.0
- 🏗️ architecture
- 🔧 component breakdown
- 🔒 security architecture — three layers in code, not prompts
- 🗃️ evidence graph schema
- ⏰ clock drift detection
- 🔍 anti-forensics detection
- 🧩 mitre att&ck sequence validation
- 🎯 75 implemented features
- 🚧 challenges
- 🏅 accomplishments
- 💡 what we learned
- 🚀 roadmap
- 🚀 quick start

## Body

🔍 ProofSIFT Neuro-Symbolic, Self-Correcting Autonomous DFIR Triage Agent The Prime Directive: ProofSIFT cannot issue a confirmed finding unless it can mathematically prove the claim using traceable, multi-source forensic evidence. 💡 Inspiration — Solving the LLM Hallucination Problem in DFIR The SANS Find Evil hackathon demands autonomous agents that operate at machine speed and produce findings that judges can trust at a glance. However, standard Large Language Models fail catastrophically in Digital Forensics and Incident Response because they rely on probabilistic token generation . When processing thousands of raw logs, LLMs hallucinate timelines, invent non-existent C2 IP addresses, and confidently escalate benign system processes to CONFIRMED threats. ProofSIFT introduces a Neuro-Symbolic Architecture to DFIR. We fused the pattern-recognition power of an LLM with the deterministic, mathematical certainty of formal theorem provers and cryptographic graphs. Every claim is cryptographically linked to the exact artifact, parser tool, command UUID, timestamped JSONL audit event, and SHA-256 evidence hash that produced it. 🏆 Judging Criterion Mapping 🎯 Autonomous Execution Quality Deterministic Plan → Collect → Hypothesize → Verify → Correct loop powered by Z3 Satisfiability Modulo Theories (SMT) with configurable max-iteration caps. agent.py:36-98 — tool dispatch, verification gates, iteration boundaries 🛡️ IR Accuracy CONFIRMED status requires evidence from ≥2 independent artifact kinds . Unsupported claims are auto-downgraded. NetworkX PageRank calculates attack blast radius. Negative controls prevent benign escalation. agent.py:284-309 — _verify_claims gate agent.py:311-325 — _negative_controls 🔬 Breadth and Depth 16 typed tools across memory, network, execution, registry, filesystem, event logs, and IOC scans. tools.py:31-49 — full tool catalog with typed contracts 🔒 Constraint Implementation SafePathPolicy blocks evidence writes. Typed facade replaces shell access entirely. Automated spoliation probes prove the read-only boundary at the OS layer — not just in a prompt. security.py:12-41 — read/write validation and automated probe 📋 Audit Trail Quality SQLite evidence graph sealed with a Merkle-DAG root hash for cryptographic chain-of-custody. Append-only JSONL audit stream. Full correction history with before/after state. audit.py · graph.py · integrity.py · reporting.py 📖 Usability Zero runtime dependencies for demo mode. Runs on any Python 3.10+ system. Full CLI with run , benchmark , trace , list-tools , and mcp-stdio subcommands. SIFT integration documented. requirements.txt — only 3 optional production packages ⚙️ What It Does ProofSIFT is an evidence-proven, self-correcting autonomous DFIR triage agent that investigates Windows compromises through a deterministic multi-iteration loop, producing auditable findings with full provenance traceability. Unlike standard LLM wrappers, it uses a Neuro-Symbolic Architecture that guarantees no confirmed finding can exist without a mathematical proof trail. 🔍 Case Loaded └── ⚙️ hash_all_evidence — SHA-256 every evidence file └── ⚙️ spoliation_probe — Prove writes are blocked via SafePathPolicy Iteration 1 — Volatile Triage (Memory and Network) ├── 🧠 memory_pslist — Hunt for rogue and hidden processes ├── 🧠 memory_psscan — Detect hidden and unlinked processes ├── 🌐 memory_netscan — Pinpoint unverified communication channels ├── 🧠 memory_malfind — Injected memory regions (MZ headers, RWX pages) ├── 📝 Generate C2 hypotheses — Match remote_IP against known c2_ips ├── 🔍 _verify_claims — Downgrade unsupported CONFIRMED findings └── 🧩 _validate_mitre_sequence — Flag missing tactic prerequisites Iteration 2 — Disk Corroboration and Verification ├── 💾 disk_prefetch — Execution artifacts (run count, last run) ├── 💾 disk_amcache — Program execution inventory ├── 💾 disk_shimcache — Application compatibility cache ├── 📝 registry_autoruns — Persistence registry points ├── 📂 timeline_mft — Master File Table timeline ├── 📂 timeline_usn — USN journal entries ├── 📋 windows_evtx — Event logs and process creation (4688) ├── 📋 powershell_logs — PowerShell activity ├── 🔎 yara_keyword_scan — IOC keyword matching ├── ⏰ _normalize_clock_drift — Discover and apply +120s anchor delta ├── 🔗 _correlate_disk_memory — Cross-source artifact matching ├── 🔍 _apply_anti_forensics — Z3 Solver: structural timestomping proof ├── 🔍 _verify_claims — Upgrade or downgrade based on multi-source proof └── 🧩 _validate_mitre_sequence — Re-check tactic gaps Iteration 3 — Negative Controls ├── 🛡️ _negative_controls — Verify svchost.exe and lsass.exe are NOT escalated ├── 🔍 _verify_claims — Final verification pass └── 🔏 _finalize_merkle_dag — Seal evidence graph with cryptographic root hash 📊 write_reports — Markdown + HTML + trace index + JSONL 🏆 Benchmark — Score against ground_truth.json ✅ Result — Precision 1.0, Recall 1.0, PASSED 🧠 The Neuro-Symbolic Core — Three "God-Tier" Integrations These three integrations are what separate ProofSIFT from every other LLM-based forensic tool. They replace probabilistic guesswork with mathematical guarantees. 1️⃣ Z3 Theorem Prover — Bounded Model Checking for Timelines Attacker timestomping (modifying $MFT timestamps) defeats standard chronological timeline analysis. ProofSIFT converts artifact timestamps into formal mathematical constraints using Microsoft's Z3 Satisfiability Modulo Theories (SMT) solver. How it works: If Prefetch metadata proves evil.exe executed at 14:02Z , but the MFT shows the file was created at 14:10Z , Z3 evaluates the causality equation. It mathematically proves that a file cannot execute before it exists, throws an UNSATISFIABLE CONTRADICTION , and automatically flags the file for Anti-Forensics manipulation — with zero reliance on heuristics or LLM confidence scores. Prefetch: evil.exe last_run = 14:02:13Z ───┐ MFT: evil.exe created = 14:10:05Z ───┤ ├──► Z3 asserts: created_utc > last_run_utc │ Result: UNSATISFIABLE └──► ANTI-FORENSICS CONFIRMED (Delta = 472s) 2️⃣ Merkle-DAG — Cryptographic Chain of Custody In a court of law, AI findings are hearsay without provenance. ProofSIFT implements a Merkle Directed Acyclic Graph (DAG) over the entire evidence graph. How it works: Every parsed artifact, tool run, Bayesian score, and claim is hashed and cryptographically linked to the previous step. Upon investigation completion, the engine outputs a single sha256:<root> seal. If a single byte of the underlying SQLite database is altered — to frame an innocent employee or suppress a finding — the root hash breaks instantly, providing court-admissible proof of tampering. [tool_run_001] ──SHA256──► [artifact_042] ──SHA256──► [claim_clm-007] ──SHA256──► sha256:<root> | | | └── any modification here ┴── breaks the root hash here ──────────────────────┘ Tamper-evident chain of custody 3️⃣ NetworkX Knowledge Graphs — Topological Attack Analysis Reading flat CSV logs ignores the three-dimensional topology of an APT intrusion. ProofSIFT ingests all evidence into a multi-dimensional knowledge graph using NetworkX. How it works: By mapping IPs → processes → registry keys → filesystem artifacts into a directed graph, the engine runs PageRank algorithms to instantly calculate the "Center of Gravity" of the attack — the node with the highest influence score — and defines the precise blast radius of the compromise, showing analysts exactly which systems and data assets are downstream of the initial foothold. 🗂️ Demo Case Evidence File Key Content Forensic Purpose processes.csv evil.exe PID 1888, svchost.exe PID 412 pslist and psscan process inventory netscan.csv evil.exe to 203.0.113.50:443 C2 beacon indicator prefetch.csv EVIL.EXE — 3 runs Execution count and last-run time amcache.csv evil.exe — unsigned, SHA-256 present Program execution inventory shimcache.csv evil.exe, powershell.exe AppCompat execution cache mft.csv evil.exe created 14:10:05Z, modified 14:02:05Z Timestamps proving timestomping usn.csv evil.exe FILE_CREATE 14:02:05Z USN journal corroboration evtx.csv 4624 logon from 203.0.113.50, 4688 process Clock drift anchor and execution log malfind.csv evil.exe — PAGE_EXECUTE_READWRITE, MZ header Injected memory region autoruns.csv Updater -> evil.exe in HKCU\Run Registry persistence payload_notes.txt "evil beacon initialized", "c2 channel: 203.0.113.50:443" YARA and keyword IOC hit 📊 Benchmark Results — Precision 1.0, Recall 1.0 ┌─────────────────────────────────────────────────────────────┐ │ BENCHMARK SCORECARD │ ├─────────────────────────────────────────────────────────────┤ │ Metric Result Status │ │ ─────────────────────────────────────────────────────── │ │ Expected confirmed matched 2 / 2 ✅ All evil │ │ Forbidden confirmed (FP) 0 ✅ No FP │ │ Hallucinated confirmed 0 ✅ No halluc. │ │ Expected anomalies matched 2 / 2 ✅ Timestomp │ │ Expected clock drifts matched 1 / 1 ✅ +120s drift │ │ Precision 1.0 ✅ │ │ Recall 1.0 ✅ │ │ Overall PASSED ✅ │ └─────────────────────────────────────────────────────────────┘ Finding 1 — evil.exe C2 Beacon to 203.0.113.50:443 Ground truth rule: Must confirm C2 Agent decision: ✅ CONFIRMED Evidence: process + network + prefetch + amcache + shimcache + MFT + EVTX + USN + malfind + yara — 10 independent artifact kinds. Zero doubt. Full Merkle-sealed provenance. Finding 2 — evil.exe HKCU\Run Persistence Ground truth rule: Must confirm persistence Agent decision: ✅ CONFIRMED Evidence: autorun + process + prefetch + amcache + MFT + EVTX — 6 independent sources corroborating the same persistence mechanism. Finding 3 — unknown.exe to 198.51.100.24:443 Ground truth rule: Must NOT over-escalate Agent decision: ✅ INFERRED Why correct: Single-source network signal. No host-side execution evidence found. Agent correctly held back from CONFIRMED. No false positive. Finding 4 — svchost.exe flagged malicious Ground truth rule: Must NOT flag benign process Agent decision: ✅ POSSIBLE (INFO) Why correct: Negative control boundary enforced. Common Windows system process not falsely accused. Negative control gate passed. Finding 5 — EVTX Clock Drift +120 seconds Ground truth rule: Must detect timestamp skew Agent decision: ✅ Detected and normalized Method: Normalizer matched shared anchor 203.0.113.50 across netscan and EVTX 4624 logon. Delta of +120s discovered and applied to all EVTX observations. Finding 6 — MFT Timestomping on evil.exe Ground truth rule: Must detect anti-forensics Agent decision: ✅ Detected Method: Z3 proved mft_creation_postdates_prefetch_execution . MFT created 14:10:05Z vs Prefetch last run 14:02:13Z. Delta = 472 seconds. UNSATISFIABLE causality violation. 🏗️ Architecture ┌──────────────────────────────────────────────────────────────┐ │ CLI (cli.py) │ │ run | benchmark | trace | list-tools | mcp-stdio │ └───────────────────────────┬──────────────────────────────────┘ │ ┌───────────────────────────▼──────────────────────────────────┐ │ SelfCorrectingInvestigator (agent.py) │ │ Iteration 1 (memory) → 2 (disk) → 3 (negative controls) │ │ Verification gates · Z3 constraints · Self-correction │ └──┬──────────┬──────────┬───────────┬──────────┬─────────────┘ │ │ │ │ │ ┌──▼────┐ ┌──▼────┐ ┌───▼────┐ ┌───▼────┐ ┌───▼──────────┐ │ Tools │ │ Clock │ │ Z3 │ │ MITRE │ │ Evidence │ │Runner │ │ Drift │ │ SMT │ │Sequence│ │ Graph │ │ 16 │ │ Norm. │ │Constr. │ │Validat.│ │ SQLite │ │ typed │ │Anchor │ │Engine │ │ │ │+ Merkle-DAG │ │ tools │ │ match │ │Anti- │ │ │ │+ NetworkX │ │ │ │ │ │Forensic│ │ │ │ PageRank │ └───────┘ └───────┘ └────────┘ └────────┘ └──────────────┘ │ ┌───────────────────────────▼──────────────────────────────────┐ │ Security Layer (security.py) │ │ SafePathPolicy — read from evidence roots only │ │ Spoliation probe — automated write-block verification │ │ SHA-256 hashing — before any analysis begins │ └──────────────────────────────────────────────────────────────┘ 🔧 Component Breakdown Module Component Responsibility tools.py Typed Tool Facade 16 read-only forensic tools