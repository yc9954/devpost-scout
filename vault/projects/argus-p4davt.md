---
slug: "argus-p4davt"
url: "https://devpost.com/software/argus-p4davt"
title: "ARGUS"
hackathon: "Splunk Agentic Ops Hackathon"
organization: "Splunk"
winner: true
words: 1190
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# ARGUS

> ARGUS finds the gaps in your Splunk detection rules before attackers do. One AI invents new attacks, another fixes the rule, and every improvement is proven live.

[Devpost](https://devpost.com/software/argus-p4davt) · hackathon [[Splunk Agentic Ops Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: provenance_signing</sub>
**domain** [[developer_tools]] [[security_privacy]]
  <sub>weak: accessibility</sub>
**user** [[developer]] [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** amazon-web-services, anthropic, claude, cloudfront, css, docker, ec2, enterprise, fastapi, hec, nginx, python, react, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for argus

## Body

The landing page - Red attacks, Splunk scores, Blue evolves, live on real security data. The arena just started - Red AI has read the detection rule and is already running live Splunk queries to plan its first attack. Generation 1 converged - Blue rewrote the SPL and coverage jumped from 33% to 100%, with zero false positives. Human review is next. Two generations in- Red invented harder attacks against the rule Blue just improved, and Blue adapted again. 41 live Splunk searches so far. Generation 3, mid-run - 47 searches and counting. Every query is visible in the live feed - nothing is running behind the scenes. The evasion autopsy - each attack variant gets a full breakdown: what it did, why the original rule missed it, and what Blue learned. 9 attack variants, 3 generations, all caught - MITRE coverage at 100% across T1078, T1098, and T1136. MITRE ATT&CK map, self-improving - baseline coverage in grey, ARGUS-hardened coverage in blue. Every bar computed from a live Splunk search. The Resilience Certificate -- 11% to 100%, 9 variants tested, 0 blind spots - SHA-256 signed and exportable as a real Splunk app. The full audit log - every Red move, every Blue attempt, every rejection and convergence, in order. Nothing is a black box. Inspiration Security teams have a quiet problem: detection rules go stale. An attacker changes one field -- a different IP, a new region, a slight timing variation -- and suddenly a rule that caught them yesterday misses them completely. Nobody knows until there is a breach. We asked: what if Splunk could automatically discover those gaps and fix them, before an attacker finds them first? That is ARGUS. We also spent a lot of time in the Splunk developer Slack getting our heads around BOTS v3 and the SDK -- the community there was genuinely helpful in shaping this. What it does ARGUS puts an AI attacker and an AI defender inside your real Splunk data and lets them fight. Each round: Red agent invents new attack variations specifically designed to slip past your current detection rule -- using real field distributions from your Splunk data, not made-up numbers Evaluator runs live Splunk searches to measure exactly what the rule catches and what it misses Blue agent looks at the missed variants and rewrites the SPL detection to close the gap Repeat -- Red attacks the improved rule, Blue adapts again At the end, you get: A measurably better detection rule (we went from 0% to 100% recall in a single live run) A MITRE ATT&CK coverage map showing which techniques are now covered A Resilience Certificate -- a SHA-256 fingerprinted proof of what was tested and what improved An honest residual frontier -- the evasions ARGUS could not close, so your analysts know exactly what to prioritize next A human approval gate -- the evolved rule is shown to you for review before anything changes in Splunk. Nothing ships without a human saying yes. How we built it The AI layer Claude Sonnet 4.6 powers the Red and Blue agents -- generating attack variants, rewriting SPL, and explaining every change in plain English Claude Haiku handles the fast, repetitive reasoning steps to keep costs low The Splunk layer (fully native) Real BOTS v3 data (576 actual aws:cloudtrail events from a real cryptomining incident where user web_admin launched EC2 instances across 10 AWS regions in one hour) Splunk Python SDK for all live searches -- 24 per arena run, every one streamed to the UI in real time so you can see exactly what Splunk is doing HEC (HTTP Event Collector) for Red to inject synthetic attack variants into a dedicated argus_sandbox index | anomalydetection -- Splunk's built-in ML command -- as the anomaly scorer, training live on real BOTS v3 baseline data The app FastAPI backend with Server-Sent Events so every search result, score, and generation update streams live to the browser React + TypeScript + Tailwind frontend with a real-time duel display Deployed on AWS EC2 behind CloudFront -- live at https://d3dk3o9z0i46e2.cloudfront.net/ Challenges we ran into No fake data allowed We made a rule early: every number ARGUS shows must come from a live Splunk search. No hardcoded metrics, no mocked responses. If Splunk is not connected, ARGUS fails loudly. Enforcing this throughout the engine -- through LLM retries, HEC ingest lag, and parallel variant evaluation -- was the hardest part to get right. Getting Blue to write valid SPL The Blue agent does not just suggest changes -- it writes actual SPL that gets run live against Splunk data. Getting Claude to consistently produce syntactically correct, logically sound detections (especially with Splunk's dotted-field quoting rules) took a lot of iteration and a fenced-block parsing approach. Making the streaming work end-to-end SSE over POST through CloudFront with long-running LLM calls in the middle is not a combination that just works out of the box. Getting events to stream in real time without buffering or timeouts required careful nginx and CloudFront cache-behavior configuration. Accomplishments that we're proud of 0% to 100% detection coverage in one live generation -- and the real BOTS web_admin attacker is still caught by the evolved rule, with zero false positives Every metric is provable: 24 live Splunk searches per run, all visible in the UI's search-trace panel. Nothing hidden, nothing fabricated. The human approval gate -- we deliberately made ARGUS not auto-deploy anything. The improved rule is shown side-by-side with the original, Blue's plain-English rationale is right there, and you Approve / Edit / Reject before Splunk sees a change. Even after approval, the saved search is created disabled=1 . Turning it on is a separate, deliberate action. The evolved detection is exported as a real installable Splunk app, validated by Splunk's own AppInspect tool, so teams can install it directly without copy-pasting SPL. What we learned | anomalydetection is genuinely powerful as a first-class ML backend. Training it live on a per-hour BOTS v3 baseline and getting meaningful anomaly scores back in under a second was a pleasant surprise. Grounding LLMs in real data changes everything. Red does not invent random attacks -- it queries the actual field distributions in Splunk (regions, IPs, instance types) and builds variants from those real pools. That is what makes the evasions realistic and the coverage gains meaningful. Honest reporting builds more trust than perfect scores. Showing the residual frontier -- the gaps ARGUS could not close -- made the results feel more credible, not less. Security teams have seen enough tools that claim 100% detection. Showing the gaps is a feature. What's next for ARGUS More attack scenarios -- ransomware lateral movement, S3 exfiltration, credential stuffing -- anything with real Splunk data to anchor the baseline Splunk MCP Server (app 7931) as the primary search path for richer field introspection and agent-native tool use Slack notifications -- when ARGUS finishes a run and issues a Resilience Certificate, ping your team in Slack with the coverage gain and the approval link CI/CD integration -- run ARGUS in a pipeline on every detection-rule PR and automatically flag regressions before they hit production <div