---
slug: "payguard-qj08ie"
url: "https://devpost.com/software/payguard-qj08ie"
title: "PayGuard"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 718
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "user/general_public"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# PayGuard

> PayGuard is a free, privacy-first platform for smarter international payments. Compare fees, detect scams, track exchange rates, and manage invoices instantly—no signup required.

[Devpost](https://devpost.com/software/payguard-qj08ie) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[finance_payments]] [[immigration_refugee]] [[labor_employment]] [[security_privacy]]
**user** [[general_public]] [[small_business]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[web_dom]]

**stack** css3, html5, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for payguard

## Body

Inspiration Every year, billions of dollars are lost to hidden international transfer fees and payment scams. A friend of ours once sent money abroad through their bank, not realizing they were paying 3x more in fees than necessary, and another person we know nearly fell for a fake “account locked” scam message. That got us thinking: why is there no simple, free tool that helps everyday people make smarter, safer international payments? Most tools are cluttered, require sign-ups, or are behind paywalls. We wanted to build something instant, private, and genuinely useful . PayGuard was born from that frustration. What it does PayGuard is now a multi-tool web application designed to help users make safer and more cost-effective financial decisions: 💱 Cross-Border Fee Calculator Enter transfer amount, sending country, and receiving country Instantly compare fees, exchange rates, and delivery times across 6 providers : Wise, PayPal, Bank Transfer, Western Union, Crypto (USDT), and Revolut Automatically highlights the best option and shows savings vs. the most expensive route Supports 15 countries/currencies 🛡️ Payment Scam Checker Paste suspicious payment messages (email, SMS, WhatsApp, etc.) Scans against 44 scam signal patterns across 6 categories: Urgency Tactics, Financial Red Flags, Impersonation, Phishing, Prize/Reward, Social Engineering Returns animated 0–100 risk score , verdict level (Safe / Low / Medium / High), highlighted phrases, and signal breakdown Includes sensitivity levels and one-click report copy 📈 Exchange Rate Tracker (Live) Tracks live exchange snapshots from a public API Shows 7-point trend chart with automatic 2-minute refresh Includes transfer timing guidance and target-rate alert support Gives quick visibility into when to send for better value 🧾 Tax and Invoice Helper Generate simple invoices with live subtotal, GST/VAT, and total Categorize expenses into useful business buckets Includes practical document checklist for freelancers/small businesses 🤖 AI Assistant Available on all pages as a floating chatbot icon Opens a quick dialog for guidance on fees, scams, exchange targets, and tax basics Improves usability for first-time users Everything runs in the browser. No account needed. How we built it PayGuard is a frontend web application built with: HTML5 for semantic multi-page structure CSS3 for custom design system, responsive layouts, and animations Vanilla JavaScript for fee logic, scam scoring, live exchange tracking, chatbot interactions, and UI state Font Awesome 6 for icons Google Fonts (Inter) for typography Architecture includes shared styles/scripts and feature-specific modules across landing and tool pages. The fee calculator uses a realistic provider model (percentage fee + fixed fee + exchange-rate markup). The scam checker uses weighted scoring by severity ( high , medium , low ) with sensitivity multipliers. The exchange tracker uses live API data with graceful fallback behavior. Challenges we ran into Browser CORS with exchange APIs : some endpoints failed in frontend-only mode. We switched to a browser-compatible live source and added fallback handling. Keyword highlighting without breaking markup : overlapping scam phrases could cause replacement issues; solved with careful ordering and escaped processing. Making comparisons feel realistic : model tuning was needed so provider outcomes felt believable and practical. Responsive multi-panel UI : maintaining clarity across desktop and mobile required careful grid, spacing, and component hierarchy decisions. Balancing detail vs simplicity : exposing enough data (rate trends, alerts, risk categories) without overwhelming users. Accomplishments that we’re proud of ✅ Built a polished multi-page fintech app using only HTML, CSS, and JavaScript ✅ Implemented 44 scam signals with severity scoring and visual breakdowns ✅ Delivered fee comparison across 15 countries and 6 providers ✅ Added live exchange tracking with auto-refresh and target logic ✅ Added tax/invoice productivity tools for freelancers and small businesses ✅ Added site-wide AI assistant for better onboarding and support ✅ Maintained strong privacy-first, no-signup product experience What we learned Transfer cost transparency depends on both explicit fees and hidden FX markup Scam messages can be effectively categorized by linguistic risk patterns Vanilla JS can handle complex, production-style interactive flows UX microdetails significantly improve trust in financial tools API/CORS constraints are a major consideration in frontend-only fintech products What’s next for PayGuard 🌐 More robust multi-source live exchange feed support 📄 PDF export for fee/scam/invoice outputs 🌙 Dark and Light mode toggle 🤖 Smarter AI-assisted scam analysis with lightweight NLP 🌍 Expand to 50+ countries and 10+ providers 🔔 Browser extension to detect risky payment messages directly in email/chat clients <div