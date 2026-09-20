---
slug: "shieldai-6x2z1q"
url: "https://devpost.com/software/shieldai-6x2z1q"
title: "ShieldAI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 651
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/graph_reasoning"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/security_privacy"
  - "user/developer"
  - "user/educator_student"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# ShieldAI

> Open-source correlation engine for cyber threat intelligence. 14 zero-auth APIs, 5 analysis layers, 19 cross-layer rules — not an API wrapper, a risk intelligence platform. Clone → run → scan.

[Devpost](https://devpost.com/software/shieldai-6x2z1q) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[graph_reasoning]] [[simulation_digital_twin]]
  <sub>weak: benchmark_measured, sensor_fusion</sub>
**domain** [[developer_tools]] [[education]] [[security_privacy]]
**user** [[developer]] [[educator_student]] [[small_business]]
**substrate** [[document_pdf]] [[structured_db]] [[web_dom]]
  <sub>weak: sensor_telemetry</sub>

**stack** abuse.ch-(threatfox, cisa-kev, cloudflare-doh, framer-motion, google-doh, hibp-pwned-passwords, ip-api.com, ipapi.is, jspdf, malwarebazaar), next.js-16, nvd/nist, phishdestroy, qualys-ssl-labs

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- what i learned
- what's next

## Body

Expose your Shadow Attack Surface Multi-dimensional threat extraction Beyond basic scanning Command Center Temporal Score Trend Security Score Telemetry Cross Comprasion Table Benchmark Log View Phishing Awareness Quiz Client Engine Audit Credential Audit Module Threat Intelligence Graph Inspiration Most cybersecurity tools fall into two categories: expensive enterprise platforms that require weeks of setup, or free "API wrappers" that call VirusTotal and display the JSON. Neither helps a small business owner, freelance developer, or student understand their actual risk. I wanted to build something different: a tool where you enter a domain and get a complete threat intelligence report — with real analysis, not just raw API output. No API keys to manage. No accounts to create. Just git clone , npm install , and you're scanning. What it does ShieldAI is an open-source correlation engine for cyber threat intelligence. It takes a single domain as input and: Acquires data from 14 free, zero-authentication APIs in parallel (DNS, SSL, threat databases, IP intelligence, vulnerability databases) Analyzes through 5 independent layers: DNS & Email Security, SSL/TLS Posture, Threat Intelligence, Hosting Trust, and Known Vulnerabilities — each with its own rule set (40+ rules total) Correlates across layers using 19 cross-layer rules that detect compound risks no single API can surface (e.g., "active threat IOC + expired SSL + no DMARC = compromised infrastructure being used for phishing") Scores risk 0–100 with dynamic weight redistribution when APIs fail Narrates findings in a multi-section plain English report — entirely template-driven, zero AI/LLM dependency Generates a one-click PDF report, an interactive threat graph, a live 3D threat radar, and a voice briefing Additional tools: honeypot URL tracker, password breach checker, browser security audit, and phishing awareness quiz. How I built it Solo project. 8 days. Claude Code as the development tool. The architecture is a pipeline of pure TypeScript functions. Every analysis layer is a pure function: pass in data, get findings out. No side effects, no shared state. The correlation engine evaluates pre-computed boolean conditions across all layers to avoid redundant scans. Key technical decisions: Dual-lookup for threat intel : ThreatFox, URLhaus, and MalwareBazaar are each queried by both domain AND resolved IP, then merged and deduplicated Worst-grade SSL : Multi-IP domains use the worst endpoint grade, not the best Graceful degradation : Failed APIs redistribute their weight proportionally — even if 3/5 layers fail, the score remains meaningful Radial graph layout : Pure math positioning (no physics simulation) for instant render of the threat intelligence graph Tech stack: Next.js 16, TypeScript, Tailwind CSS v4, React Flow, react-globe.gl, jsPDF, Framer Motion, Web Speech API. Deployed on Vercel. Challenges Rate limits without API keys. NVD allows 5 requests per 30 seconds without a key. SSL Labs allows one concurrent scan. The engine handles this with aggressive caching, timeout management, and graceful degradation — a failed layer never crashes the scan. Correlation rule design. The hardest part wasn't calling APIs — it was deciding what combinations of findings actually indicate compound risk. A domain on a residential IP is unusual. A domain on a residential IP with ThreatFox IOCs is a compromised home device. Writing rules that distinguish signal from noise across 5 independent data sources required careful calibration. Zero-config philosophy. Every design decision was filtered through: "Does this require the user to create an account, get a key, or configure anything?" If yes, it was either made optional or replaced with a zero-auth alternative. What I learned Building a correlation engine taught me that the value in cybersecurity tooling isn't in the data — it's in the connections between data points. Any individual API call is a commodity. Cross-referencing ThreatFox IOCs with URLhaus distribution patterns with DNS fast-flux signals with hosting reputation — that's where real intelligence emerges. What's next Plugin architecture for community-contributed analysis layers CLI tool and browser extension Docker self-hosted version Historical trend tracking with graph database (Neo4j) 50+ threat feed sources <div