---
slug: "sentinel-eye"
url: "https://devpost.com/software/sentinel-eye"
title: "sentinel-eye"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 424
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/government_staff"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# sentinel-eye

> AI Visual Security Inspector - Gemini Live Agent Challenge submission

[Devpost](https://devpost.com/software/sentinel-eye) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[government_staff]]
**substrate** [[video_visual]] [[web_dom]]

**stack** dockerfile, html, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for sentineleye

## Body

Inspiration Traditional security scanners output walls of technical jargon — CVEs, CVSS scores, raw HTTP headers. Most website owners can't interpret these results or prioritize what to fix. Meanwhile, visual security issues (mixed content warnings, suspicious iframes, deceptive UI patterns, phishing indicators) are completely missed by automated scanners because they require seeing the page. SentinelEye combines browser automation with AI vision to inspect websites the way a human security expert would — by actually looking at them. What it does SentinelEye is an AI-powered visual security inspector that navigates websites like a real user and uses multimodal AI to identify security vulnerabilities. Visual Threat Detection: Screenshots pages and uses Google Gemini's vision API to identify phishing indicators, deceptive UI, suspicious forms, and visual security issues Automated Navigation: Playwright-based crawler navigates the site, clicks through pages, fills forms, and captures the full user experience Security Header Analysis: Checks HTTP security headers (CSP, HSTS, X-Frame-Options, etc.) and flags misconfigurations SSL/TLS Verification: Certificate validation, expiration checks, and protocol analysis AI-Powered Reports: Generates human-readable security reports with severity ratings, screenshots of issues, and actionable remediation steps Dark Security Theme: Professional cybersecurity-themed UI for presenting findings How we built it Backend: Python FastAPI with async architecture for concurrent scanning Browser Automation: Playwright for headless Chromium navigation and screenshot capture AI Vision: Google Gemini multimodal API for visual threat analysis Frontend: Dark-themed security dashboard with real-time scan progress Containerized: Docker support with Google Cloud Build for deployment Challenges we ran into Balancing scan thoroughness with speed — deep crawling takes time Reducing false positives in visual threat detection (not every red warning is malicious) Handling JavaScript-heavy SPAs that require full browser rendering Rate limiting against target sites to avoid being blocked Accomplishments we're proud of Nobody else combines visual AI + browser automation for security scanning — this is a novel approach The AI can identify phishing pages, fake login forms, and deceptive UI patterns that traditional scanners completely miss Human-readable reports that non-technical website owners can actually understand Full containerized deployment with one command What we learned Multimodal AI is surprisingly good at identifying visual security threats Many real-world security issues are visual (deceptive forms, misleading URLs, phishing layouts) and invisible to traditional scanners Playwright's screenshot capabilities combined with AI vision create a powerful inspection pipeline What's next for SentinelEye Browser extension for on-demand page inspection CI/CD integration for automated security checks on deployments Historical comparison — track how a site's security posture changes over time API marketplace integration for third-party security tool enrichment Mobile app scanning support <div