---
slug: "0-day-radar"
url: "https://devpost.com/software/0-day-radar"
title: "0-Day Radar"
hackathon: "Hex-a-thon"
organization: "Hex"
winner: true
words: 568
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/security_privacy"
  - "user/researcher"
  - "substrate/sensor_telemetry"
---

# 0-Day Radar

> Predicting the next hack, not just reporting the last one

[Devpost](https://devpost.com/software/0-day-radar) · hackathon [[Hex-a-thon]]

## Facets

**domain** [[civic_government]] [[security_privacy]]
**user** [[researcher]]
**substrate** [[sensor_telemetry]]

**stack** cisa, epss, gemini-api, hex, nvd, pandas, python, sql

## How they structured the write-up

- 0-day radar: predicting the next hack

## Body

0-Day Radar: Predicting the Next Hack Inspiration: The Noise Problem In cybersecurity, everything is "Critical." Security teams are drowning in vulnerability alerts, often relying solely on CVSS (Common Vulnerability Scoring System) severity scores to prioritize patching. I realized that most scanners are reactive they tell you what is broken after the fact. I wanted to build something predictive . The inspiration came from the realization that a "Medium" severity vulnerability with a 95% chance of exploitation is far more dangerous than a "Critical" vulnerability that no hacker is using. The goal was to shift the focus from "what is bad?" to "what will hit us next?" by triangulating government intelligence with machine learning. How I Built It: The "Risk Triangle" Architecture The core of the project is a data architecture I call the "Risk Triangle," which ingests and merges three distinct authoritative sources: NVD (NIST): Provides the metadata and "Base Severity" (CVSS). CISA KEV: The "Known Exploited Vulnerabilities" catalog, offering evidence of active attacks in the wild. EPSS (First.org): The Exploit Prediction Scoring System, which uses ML to generate a daily probability score (0-100%) of a vulnerability being exploited. The Algorithm I used Python and pandas to merge these datasets and implemented a custom Composite Risk Score to rank threats. Instead of relying on a single metric, I used a weighted formula to calculate actual urgency: This formula heavily weights EPSS (probability) and KEV (confirmed activity) over the theoretical CVSS severity, ensuring that "active fires" rise to the top of the Kill List . The AI Analyst For the "CISO Translator" feature, I integrated the Google Gemini API via REST. This component takes raw technical data (e.g., "Heap-based buffer overflow in libwebp") and converts it into a business impact summary (e.g., "Full system compromise risk; patch within 24 hours"). Challenges Faced Data Asymmetry: Merging the datasets was difficult because they update at different rates. The NVD data is a static snapshot, while EPSS and CISA KEV are fetched live. I had to create a logic flow that handles missing vendors or scores by marking them as "Other" or filling NaN values to ensure the pipeline didn't break. Structured AI Output: Getting a Generative AI model to return reliable data for a dashboard was tricky. I had to implement a Rule-Based Fallback Engine because the LLM would occasionally fail to return valid JSON. The code now attempts to parse the AI response, but if it fails, it instantly falls back to keyword matching (e.g., detecting "RCE" or "SQLi" in descriptions) to generate the impact assessment safely. The "Vendor Shame" Visualization: Identifying which vendors introduced the most risk required filtering out general noise. I had to build a specific intersection of the datasets to only penalize vendors with verified critical vulnerabilities, creating a "Trusted Source" list to prevent the chart from being dominated by "Unknown" or generic software names. What I Learned Building 0-Day Radar taught me that context is king . By visualizing the data in a Risk Matrix (Age vs. EPSS), I learned that many "Critical" vulnerabilities sit unexploited for years, while newer, lower-severity bugs are weaponized immediately. I also learned the power of LLMs as translators . The technical gap between a security analyst and a CISO is often where decisions get stalled. Automating the "Executive Briefing" proved that we can use AI not just to write code, but to translate technical risk into business language. <div