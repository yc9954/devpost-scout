---
slug: "sentinel-qwen-ensemble"
url: "https://devpost.com/software/sentinel-qwen-ensemble"
title: "Sentinel Qwen Ensemble"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 1082
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Sentinel Qwen Ensemble

> Autonomous DFIR/SOC triage agent on Qwen Cloud (Alibaba DashScope) - Track 4 Autopilot Agent. Deterministic trust layer: code, not the LLM model, decides what is confirmed.

[Devpost](https://devpost.com/software/sentinel-qwen-ensemble) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[deterministic_policy]]
  <sub>weak: benchmark_measured, human_in_the_loop, measured_ablation, provenance_signing, runtime_tool_creation</sub>
**domain** [[finance_payments]] [[health_clinical]] [[scientific_research]] [[security_privacy]]
**user** [[legal_professional]] [[researcher]]
  <sub>weak: general_public, social_worker</sub>
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** alibaba-cloud, dashscope, mcp, plaso, python, qwen, sleuth-kit, volatility, yara

## Body

Architecture Investigation Report Workbench Proof Onboarding Evidence On Alibaba-Cloud Box Inspiration AI is being adopted fastest exactly where a wrong answer is most expensive: security investigations. A SOC analyst under pressure at 3 a.m. is extremely tempted to let a model write the verdict, and a hallucinated finding in an incident report is worse than no answer: it burns analyst hours and can put a false attribution in front of leadership. Incident-response agents fix outages; nobody had built an autopilot that investigates compromises with forensic rigor. We wanted an agent that is fully autonomous AND structurally incapable of reporting what it cannot prove. What it does Sentinel Qwen Ensemble is an autonomous DFIR (digital forensics and incident response) agent. Point it at the raw Windows evidence behind an alert (memory image, disk image, event logs) and it investigates end-to-end with zero human steering: read-only mounting with SHA-256 chain of custody, automatic evidence profiling, tool selection, a 4-model Qwen ensemble with consensus merge, ReAct cross-checks, and a final adjudication pass, then hands the analyst a risk-ranked, proof-linked incident report. The differentiator is executed depth, not just the concept: 195 typed forensic tools (Volatility 3, Sleuth Kit, Plaso, EZ Tools, RegRipper, YARA) on a custom MCP server with zero shell access , behind a deterministic trust layer where code, not the model, decides what is "confirmed". Every finding traces to the exact tool output that proves it. An opt-in human-in-the-loop checkpoint ( SIFT_HITL_CHECKPOINT=1 ) pauses at the disposition decision, before the report, for the analyst to approve or override; remediation stays gated behind the human by design. The agent automates the judgement; the human authorises the action. The proof: a public case any judge can rerun (DC01) We feature the public, reproducible DFIR Madness "Stolen Szechuan Sauce" domain controller (DC01) - paired memory (2 GB) + disk (~4.9 GB, two-segment E01), both SHA-256 verified - run fully autonomously on Qwen Cloud at two model tiers through the identical trust layer: DC01 (public, reproducible) Light ( qwen-plus x4) Heavy ( qwen3.7-max , 4-member ensemble) Findings surfaced 1 44 Confirmed malicious 0 0 Needs-review / benign 1 / 0 21 / 23 Tools (0 failed, both tiers) 33 swept 33 swept Runtime 3m 46s 14m 39s Cost (cache-aware, est.) ~$0.22 ~$1.67 Integrity mem+disk SHA-256 MATCH mem+disk SHA-256 MATCH The heavy tier reconstructed the full intrusion : coreupdater.exe C2, inbound/outbound RDP, \FileShare\Secret exfil, memory injection (explorer / svchost / spoolsv), and scheduled-task + WMI persistence, attributed to administrator / public across 5 MITRE tactics (Execution, Persistence, Defense Evasion, Lateral Movement, Command and Control), overall risk CRITICAL - and it held every lead: 0 confirmed . DC01's intrusion is real but stealthy (a custom-named C2, living-off-the-land), so no single artifact atomically proves malice, and the engine says exactly that. 0 confirmed on a real compromise is the trust layer working, not a gap. DashScope implicit prompt caching reused 371,072 tokens on the heavy run (cache-read billed below fresh-input rate), holding the paired investigation to ~$1.67. And when atomic proof IS present, the same engine confirms. On a held-back reference case (rd01, non-public), the heavy tier confirmed 4 - PsExec lateral movement, PWDumpX credential dumping, an IFEO sethc.exe sticky-keys backdoor, and p.exe executed from a temp directory, each traced to its proof tools - while the light tier confirmed 0 . A flags-off ablation isolates the trust-layer finalization: inconclusive findings jump 0 -> 11 without it, and confirmations drop 3 -> 1 (same case, same model, same deterministic gates). The bar does not move; the model's ability to clear it does. Sanitized metrics for every run ship in docs/qwen-runs/ . How we built it ~79,500 lines of modular Python: a 5,035-line typed validator, fail-closed disposition gates, and a 16-step deterministic conductor that invokes the model only inside bounded steps. Custom MCP server (FastMCP): 186 dynamically registered + 9 core tools = 195 typed tools, JSON in and out, never a shell. Qwen Cloud on Alibaba DashScope: a stdlib OpenAI-compatible provider ( src/sift_sentinel/llm_provider.py ) with DashScope-specific engineering: implicit prompt-cache accounting via prompt_tokens_details.cached_tokens , a reasoning_content fallback for Qwen thinking models, per-model output-cap clamps, and bounded read-timeout retries that fixed a live-run failure in the heavy ensemble. Model tiering to fit the $40 credit: qwen3.7-max for keystone analysis and final adjudication, qwen-plus for the high-call-volume stages. Challenges we ran into Porting a working pipeline to a new provider with zero regression: we built a duck-typed provider seam and proved an identical test-failure set against the pre-port tree before flipping anything. Live-run reliability on DashScope: the heavy ensemble initially died on read timeouts; we added bounded retries honoring Retry-After and explicit timeout handling. Budgeting $40 of credit across a 4-model ensemble: tiering plus prompt-cache reuse held a full paired public investigation to ~$0.22 (light) - ~$1.67 (heavy). Honesty under deadline pressure: part of the historical test suite went stale mid-refactor; instead of hiding it we quarantined it with the state documented ( tests/QUARANTINE.md ), so pytest tests/ is green (4,700+ passing) and the debt stays visible. Accomplishments that we're proud of Two end-to-end autonomous investigations of a real compromise, on Qwen Cloud, with every headline count/runtime/token number in the shipped metrics JSONs (cost figures derive from those token counts at the documented pricing rates). The DC01 result on a PUBLIC case: 44 findings mapped, 0 confirmed - the engine reconstructed a real intrusion end to end yet refused to over-claim, because no artifact atomically proved malice. On the held-back rd01 reference the same gates promoted 4 when atomic proof existed. Same bar, both directions; confirming nothing on DC01 is the design working, not a gap. A judge can verify with zero cost and zero keys: ./setup.sh docker builds (~30 s, once) and runs a full synthetic case end to end on any OS, and audit/nocheat.py proves the demo is not rigged. What we learned Model tier changes what clears the bar, not the bar itself: qwen-plus surfaced similar leads but could not marshal atomic proof; qwen3.7-max could. DashScope implicit prompt caching is an architecture input, not a billing footnote: 371k reused tokens on the heavy DC01 run reshaped our cost model. For agents in high-stakes domains, what the agent refuses to say is the product. What's next A hosted triage service on Alibaba Cloud ECS with OSS evidence intake. Remediation actions behind the existing human approval gate. More evidence types (Linux, macOS, cloud logs) and a public cross-case benchmark. Demo video: https://youtu.be/A53FpVgdnnU (2:50, PUBLIC) Repo: https://github.com/3sk1nt4n/Sentinel-Ensemble-Qwen (public, MIT) Architecture diagram: https://github.com/3sk1nt4n/Sentinel-Ensemble-Qwen/blob/master/ARCH_VERTICAL.png <div