---
slug: "sting-bfqvia"
url: "https://devpost.com/software/sting-bfqvia"
title: "STING"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 748
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/retail_commerce"
  - "domain/security_privacy"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# STING

> STING is AI anti-scam protection that protects elderly and naive users from phishing, fake stores, and risky sites in real time — stopping scams before money is lost and making scammers unprofitable.

[Devpost](https://devpost.com/software/sting-bfqvia) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
  <sub>weak: voice_speech</sub>
**domain** [[elder_child_care]] [[finance_payments]] [[immigration_refugee]] [[retail_commerce]] [[security_privacy]]
**substrate** [[code_repository]] [[financial_record]] [[web_dom]]
  <sub>weak: transcript_audio</sub>

**stack** anthropic, anthropic-claude, anthropic-claude-for-plain-english-scam-explanations, arize, arize-/-phoenix-for-ai-evaluation-and-tracing, asi:one, browserbase, browserbase-for-isolated-suspicious-link-inspection, chrome-extension-apis, chrome-mv3-extension-apis, claude, codex, cognition, css

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sting
- links

## Body

hero value proposition problem STING is a non-technical solution target market use cases for STING impact - call to action Inspiration Scams are profitable because victims are usually alone at the exact moment they need help. Elderly users, kids, immigrants, lonely people, overwhelmed shoppers, and non-technical internet users are constantly targeted by phishing pages, fake stores, impersonation scams, suspicious checkout flows, and too-good-to-be-true offers. By the time someone asks for help, the money or private information is often already gone. STING was built around a simple idea: scam protection should happen before the victim clicks, pays, or types in sensitive information. What it does STING — Scam Tracking & Intelligence Network Guard — is an AI anti-scam browser guard that detects risky websites in real time. It analyzes pages for signs of scams, phishing, fake storefronts, impersonation, suspicious payment flows, urgency tactics, and unsafe claims. Then it gives the user a plain-English warning and a clear risk receipt before they lose money or personal information. The goal is bigger than flagging bad pages. The goal is to make scams less profitable by reducing victim conversion at the moment scammers depend on most. How we built it We built STING as a browser-first scam defense system with a real-time extension interface, deterministic scam signals, AI-generated explanations, and evidence receipts that show why a page was flagged. Instead of making AI the only detector, STING combines structured risk signals with AI reasoning so users get both fast warnings and understandable explanations. We also built sponsor-backed proof layers for tracing, evaluation, sandbox inspection, voice scam analysis, reliability, and scam memory — while keeping the core product focused on one clear loop: detect risk, explain it, and stop the user before harm happens. Challenges we ran into The hardest part was making scam protection clear for normal people, not just security nerds. A warning has to be calm, specific, and actionable. Too much technical detail gets ignored. Too little detail feels untrustworthy. We had to think carefully about how to explain danger without overwhelming the user or making every website feel scary. We also had to balance many sponsor integrations without turning the project into logo soup. Every integration had to support the actual anti-scam mission: detect scams earlier, explain them better, preserve evidence, or make the system more reliable. Accomplishments that we're proud of We are proud that STING is built around a real human problem, not just a technical demo. The project focuses on protecting people who are often targeted precisely because they are trusting, overwhelmed, isolated, or not deeply technical. We are also proud that STING gives users a plain-English explanation instead of just a vague red warning screen. Most of all, we are proud of the mission: if STING works, scammers lose victims, lose conversion, and lose money. What we learned We learned that anti-scam protection is not just a detection problem. It is a timing problem, a trust problem, and a human vulnerability problem. The best intervention is not a report after someone gets scammed. It is a protective voice that appears before the mistake happens. We also learned that AI is most useful here when it explains and contextualizes structured evidence, instead of hallucinating from scratch. The safest system combines deterministic signals, evidence receipts, and human-readable AI explanations. What's next for STING The next step for STING is making anti-scam protection ambient, seamless, and native to everyday life. Scams do not only happen on suspicious websites. They arrive through text messages, phone calls, voicemails, emails, social DMs, fake support chats, marketplace listings, and payment links. The long-term vision is for STING to sit quietly across the places people already communicate and make decisions — especially on mobile. That means native protection for text messages, phone calls, voicemail, email, social DMs, checkout flows, marketplace conversations, and family safety workflows for elderly relatives. STING should not require vulnerable users to become security experts or remember to open a separate app. It should feel like a protective layer in the background of normal life: warning before a risky payment, explaining why a message looks suspicious, catching voice scams before someone calls back, and helping families protect loved ones without taking away their independence. The goal is huge: make scam protection as normal and automatic as spam filtering, but smarter, more personal, and present at the exact moment scammers try to exploit trust. Links Live Demo Source Code Pitch Deck Chrome Webstore Listing Hype Launch Video Extension Demo Video <div