---
slug: "zerorisk-sentinel"
url: "https://devpost.com/software/zerorisk-sentinel"
title: "ZeroRisk Sentinel"
hackathon: "Dev Season of Code "
organization: "DSOC Official"
winner: true
words: 658
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# ZeroRisk Sentinel

> ZeroRisk Sentinel – Spot malware, phishing & spyware before you click or run, with zero trust required.

[Devpost](https://devpost.com/software/zerorisk-sentinel) · hackathon [[Dev Season of Code]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[provenance_signing]] [[realtime_stream]]
**domain** [[accessibility]] [[agriculture_food]] [[finance_payments]] [[health_clinical]] [[security_privacy]] [[supply_logistics]]
**user** [[government_staff]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]] [[web_dom]]

**stack** androguard, anime.js, echarts, flask, github, groq, html5, javascript, python, tailwind, typed.js

## How they structured the write-up

- the problem
- the solution
- architecture
- tech stack
- key features
- development journey
- results
- future roadmap

## Body

ZeroRisk Sentinel The Problem Every day, over 450,000 new malware variants are detected. Keyloggers steal passwords. Phishing sites harvest credentials. Android apps request permissions they have no business needing. Most people are flying blind when it comes to understanding what they're actually downloading or clicking. The question is simple: How do you know if a file, URL, or app is actually safe? The Solution ZeroRisk Sentinel is a hybrid cybersecurity platform that combines client-side analysis with enterprise-grade threat intelligence. It functions as a digital immune system for files, URLs, and Android applications. Core Capabilities Capability Description Deep File Analysis YARA rule scanning, entropy analysis, VirusTotal integration, and sandbox execution for comprehensive malware detection URL Security Scanner Multi-source threat intelligence including Google Safe Browsing, URLHaus, SSL/DNS analysis, and browser sandboxing APK Inspector Android permission risk scoring and manifest analysis to identify invasive applications Architecture ZeroRisk Sentinel uses a privacy-first hybrid architecture : Client-Side (Browser) File header analysis JavaScript pattern matching Extension spoofing detection Local heuristic analysis Backend (Python Flask) YARA rule compilation File hashing (MD5, SHA1, SHA256) VirusTotal API integration URL threat intelligence Hybrid Analysis sandbox Groq AI explanations The system features graceful degradation — if backend services are unavailable, client-side analysis continues functioning with local pattern matching. Tech Stack Frontend Vanilla JavaScript Tailwind CSS Anime.js for animations ECharts for data visualization jsPDF for report generation Backend Python Flask YARA pattern matching engine python-magic for file type detection AndroGuard for APK analysis dnspython for DNS analysis External APIs Google Safe Browsing VirusTotal (70+ antivirus engines) URLHaus malware database Hybrid Analysis sandbox urlscan.io browser sandbox Groq AI (Llama 3.3 70B) Key Features Quick Scan vs Deep Scan : Rapid triage or comprehensive sandbox analysis Extension Spoofing Detection : Identifies files disguised as other formats (e.g., invoice.pdf.exe) Keylogger Identification : Pattern-based detection of keystroke logging code Real-time Console : Live terminal output showing every analysis step AI-Powered Explanations : Groq-powered threat analysis in plain English Professional Reports : Export to JSON or PDF with threat distribution charts Development Journey What I Learned YARA Rules and Malware Signatures : Writing signature-based detection patterns revealed how malware behaves in coordinated, purposeful ways rather than random malicious code. Entropy Analysis : Implementing Shannon entropy calculations (0-8 scale) to detect packed or encrypted files provided insight into evasion techniques. Hybrid State Management : Managing async operations between client and server, handling fallbacks, and polling for sandbox results required careful architecture design. APK Permission Analysis : Understanding how permission combinations tell stories — when an app requests BIND_ACCESSIBILITY_SERVICE + READ_SMS + BIND_VPN_SERVICE, that's surveillanceware. Challenges Overcome Challenge: Sandbox Integration Real malware analysis requires isolated execution environments. Sandbox APIs are complex and expensive to maintain. Solution : Integrated Hybrid Analysis API with intelligent polling. Frontend displays real-time progress ("Analyzing... 12/30") while backend monitors sandbox execution. Challenge: YARA Deployment YARA requires compiled rules and specific dependencies. Deploying to cloud platforms with all components was non-trivial. Solution : Built a robust fallback system. If YARA fails, the system uses built-in JavaScript pattern matching for key signatures. Analysis continues with alternative tools. Challenge: APK Size Limits APKs can be 50MB+. Uploading large files to free-tier backends causes timeouts. Solution : Implemented size limits with clear user messaging and local permission extraction for lightweight analysis. Challenge: Security Data Visualization Threat scores, hashes, and entropy values are inherently dry. Solution : Designed a cyberpunk-inspired interface with animated threat meters, orbital particle systems, real-time terminal consoles, and color-coded severity indicators. Results ZeroRisk Sentinel successfully detects: Keyloggers from code patterns Extension spoofing attacks Phishing URLs before clicking Invasive Android permissions Packed/encrypted files via entropy analysis All analysis includes professional PDF report generation with executive summaries and actionable recommendations. Future Roadmap Browser extension for instant link analysis Batch processing for multiple files Community-driven YARA rule contributions Mobile application for on-device APK scanning Security is not a product — it is a process. ZeroRisk Sentinel makes threat analysis accessible to everyone, not just security professionals. <div