---
slug: "zerorisk-sentinel-d3zc90"
url: "https://devpost.com/software/zerorisk-sentinel-d3zc90"
title: "ZeroRisk Sentinel"
hackathon: "NextGenHacks"
organization: "NextGenHacks"
winner: true
words: 510
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/government_staff"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ZeroRisk Sentinel

> Hybrid cybersecurity platform scanning files, URLs & Android APKs using YARA, VirusTotal & Groq AI. Detects malware, phishing & rogue apps — with plain-English AI explanations anyone can understand.

[Devpost](https://devpost.com/software/zerorisk-sentinel-d3zc90) · hackathon [[NextGenHacks]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[security_privacy]] [[transportation]]
**user** [[government_staff]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** abuseipdb, androguard, css, dnspython, flask, google-safe-browsing-api, groq, html, hybrid-analysis-api, javascript, llama-3.3-70b, python, python-magic, python-whois

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next

## Body

Inspiration Every time I analyzed a suspicious file, I was juggling five different tools — VirusTotal for hashes, URLScan for links, a separate APK analyzer, and still had no idea what the results actually meant in plain English. I wanted one unified platform that did all of it, explained it clearly, and worked even without internet. That frustration became ZeroRisk Sentinel. What It Does ZeroRisk Sentinel is a hybrid, multi-layered cybersecurity analysis platform detecting threats across three attack vectors: File Analysis Engine — YARA rule pattern matching, Shannon entropy detection (identifies packed/encrypted binaries), PE structure inspection, magic number vs extension validation (catches invoice.pdf.exe spoofing), and VirusTotal hash lookup across 70+ antivirus engines. URL Security Scanner — 9-source intelligence pipeline covering Google Safe Browsing, URLHaus, VirusTotal (70+ vendors), AbuseIPDB IP reputation, SecurityTrails domain intelligence, SSL/TLS certificate validation, DNS record analysis (A, MX, SPF), WHOIS domain age, and redirect chain unwinding up to 5 hops. Deep Scan mode adds live urlscan.io browser sandboxing with screenshot capture and network activity monitoring. APK Inspector — AndroGuard-powered Android package decompilation with permission risk scoring. Flags critical permissions (BIND_ACCESSIBILITY_SERVICE for keylogging, READ_SMS for OTP interception, BIND_VPN_SERVICE for traffic hijacking) with severity classification and combination heuristics. AI Threat Explanations — Groq Llama 3.3 70B converts raw technical IOCs into plain-English analysis: what the threat does, why it's dangerous, and concrete next steps. Sandbox Analysis — Submits suspicious files to Hybrid Analysis for live execution in an isolated Windows 7 VM, tracking process injection, network callbacks, file drops, and MITRE ATT&CK technique mapping. The system uses a hybrid architecture — client-side JavaScript performs instant triage (entropy, magic bytes, extension spoofing) with zero latency, while the Python Flask backend provides deep multi-source intelligence. Core detection always works, even fully offline. How I Built It Six modular Python backend components, each independently testable: file_scanner.py — YARA + VirusTotal + entropy + PE analysis url_scanner.py — 9-source URL intelligence pipeline with unified response normalization apk_analyzer.py — AndroGuard integration + custom permission risk heuristics ai_explainer.py — Groq Llama 3.3 70B with graceful fallback to heuristic mode sandbox_scanner.py — Hybrid Analysis live VM execution integration server.py — Flask routing, CORS, and API key management Challenges I Ran Into Normalizing 9 different threat intelligence APIs (each with different schemas, rate limits, error formats) into one unified, consistent response format was the hardest engineering challenge. Making core detection work offline required reimplementing entropy analysis, magic byte detection, and extension spoofing checks entirely in JavaScript — not just wrapping API calls. Getting Groq LLM to produce consistently structured, actionable explanations (not generic safety advice) required significant prompt engineering iteration. What I Learned How real malware detection works under the hood — PE headers, YARA signatures, Shannon entropy as a packed-file indicator. Also that the biggest gap in security tools isn't detection, it's explanation — most tools tell you a file is malicious but not why or what it does. What's Next Docker containerization for one-command deployment Community YARA rule repository Browser extension for real-time URL scanning Team SaaS dashboard for SMBs CI/CD pipeline scanner plugin <div