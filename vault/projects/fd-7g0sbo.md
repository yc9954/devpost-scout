---
slug: "fd-7g0sbo"
url: "https://devpost.com/software/fd-7g0sbo"
title: "Zen"
hackathon: "USAII® Global AI Hackathon 2026"
organization: "USAII"
winner: true
words: 1459
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/security_privacy"
  - "user/social_worker"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Zen

> Google gives you a list. Zen guides you through, tells you where you qualify, explains why in your language, and follows through until help actually arrives. That's the difference.

[Devpost](https://devpost.com/software/fd-7g0sbo) · hackathon [[USAII- Global AI Hackathon 2026]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[accessibility]] [[health_clinical]] [[housing_homeless]] [[labor_employment]] [[legal_justice]] [[security_privacy]]
**user** [[social_worker]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** python, render, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zen

## Body

Home Asking for Help Follow-up for a case Caseworker View Organization View Why you qualify Natural Language Processing (NLP) Questions Organization View Try it out!! Inspiration Every year, billions in benefits go unclaimed, not because people don't need them, but because the system wasn't built for them. María qualifies for food assistance. But the rules are written in legal language she can't parse. She doesn't speak English well. She's stressed, has two kids, and doesn't know where to start. And even if she finds a program, she has no way to know if help will actually come through. We asked ourselves: what if we could build something that doesn't just point people to a list, but actually guides them through, in their language, and follows up until help arrives? That's why we built Zen. What it does Zen is a web-based benefits navigator, no app to download, works on any device, in English, Spanish, and French. It works in three layers: Layer 1: Eligibility in plain language A user describes their situation in their own words (typing or speaking). Zen's NLP extracts their needs with confidence scores, asks follow-up questions when it's not sure, and returns a plain-language explanation of why they may qualify, grounded in the official rule (e.g., §SNAP 273.9), verified with a reading-level badge. Not a guess, a cited translation. Layer 2: We don't just inform, we help organizations actually deliver the help Most tools stop at "here's a list, good luck." Zen's core does what the challenge asked: scrape real resources, interpret eligibility, and guide people to their next step. But we went one step further. Because people come to us looking for help, we also see the demand side. So when organizations choose to partner with Zen, we can close that loop from the other end too, using operations research optimization (mathematics) to match cases to available capacity fairly. When slots are limited, the math ensures who gets served is decided by need and equity, not by who happened to be closest or scored highest on a flawed metric. Underserved communities, who normally lose out, get a fair share. This is an add-on, not every resource works this way, only the ones that partner with us. But it's something uniquely ours: we don't just connect people to the system, we help the system work better for them. Every decision is transparent and downloadable. No black box. Layer 3: Verified loop closure Zen tracks whether help actually arrived. Each user gets an anonymous case number (ZEN-2026-XXXX). If no one confirms within 24 hours, the case escalates to a human caseworker, triaged by vulnerability, not first-come-first-served. And when a case is too complex, sensitive, or urgent for the AI to handle alone, it goes to a human. Always. Zen connects three actors in one system: the person asking for help, the caseworker reviewing cases, and the organizations that hold the resources. Because help only works when everyone is aligned. How we built it What the challenge asked for, and what we built on top The brief asked us to build a benefits navigator that translates confusing eligibility rules into plain language and guides people to clear next steps. That is our core, and we built it first. On top of that, we added what we believe transforms a navigator into a system that actually works end to end: fair resource allocation when capacity is limited, verified follow-up, and human escalation when AI isn't enough. Stack: FastAPI backend, PuLP/CBC for the optimization solver, rule-based NLP for intake (no LLM in the eligibility pipeline, intentional), Gemini API for the contextual chat only, OpenStreetMap/Overpass API for live resource scraping (works US-wide), Supabase for production data, Leaflet.js for mapping, vanilla HTML/CSS/JS frontend, deployed on Render. Architecture flow: Input: User describes their situation in natural language (text or voice, 3 languages) + browser geolocation (consent-first, never stored). NLP layer: Extracts needs, urgency, household size, income, transport, each with a confidence score. Low confidence triggers a follow-up question instead of guessing. Matching: Cross-references against a live resource database pulled in real time from OpenStreetMap, applies eligibility rules per program, generates a plain-language explanation with official citation and a readability score. Fair allocation layer: When partner organizations have limited capacity, Zen runs an optimization model with a demographic fairness constraint. It computes both a naive (greedy) run and a fair run, outputs per-person assignments, and makes every decision downloadable as an auditable CSV. Loop closure: Creates an anonymous case, tracks status (pending, confirmed, escalated), and surfaces unresolved or sensitive cases to the caseworker dashboard for human review. Key design decision: We deliberately kept Gemini out of the eligibility pipeline. Eligibility interpretation uses rule-based NLP with cited official rules, because in social services, a hallucinated eligibility answer can cause real harm. Gemini powers only the conversational chat, where it already has context of the user's specific plan. Challenges we ran into The leveling-down problem: Our first fair allocation implementation achieved equality by serving fewer people overall, making everyone worse off equally. We caught it when we saw empty resource slots that should have been filled. The fix required redesigning the entire scenario, not just the code. Fairness constraints need careful problem design, not just solver parameters. Resisting feature creep under pressure: With a 7-day build window, the temptation to keep adding was constant. We cut a live email notification system, a full organization portal, and SMS alerts to focus on making intake, plan, tracking, and escalation work completely end to end. The features we shipped are real. The ones we cut are honest roadmap items. Testing from Mexico: Our team is in Monterrey, Mexico, but the app serves the US. Browser geolocation from Mexico breaks the live resource scraper because there are no US-formatted social service tags in Mexican data. We built a USA bounding-box guardrail that gracefully falls back to Houston for demos outside the US, honest, transparent, and clearly labeled. Accomplishments that we're proud of What we're most proud of is that we saw the problem as a whole, not just as a search engine for programs, but as a complete support system. We didn't build a tool that hands you a list and walks away, Google already does that. We built something that understands your situation, guides you to what you qualify for, makes sure the distribution is fair when resources are limited, and stays with you until help actually arrives. 19/19 tests passing on the final build. The engine, the solver, and the integration all verified. The fair allocation works: underserved neighborhoods go from 30% served to 60%, same resources, zero additional cost, 86% gap reduction. Every result is downloadable as proof. No fake features. Everything in the demo runs for real. No placeholder phone numbers, no email stubs claimed as live. What you see is what works. Loop closure as a real mechanism, not a checkbox. Pending, confirmed, escalated, with caseworker triage by vulnerability score. Plain-language eligibility with receipts. Every "you may qualify" comes with the official rule citation and a reading-level badge. The user can verify. We don't ask for blind trust in the AI. We don't trust the AI blindly either. When a case involves crisis signals, sensitive situations, or anything the system isn't confident about, it escalates to a human caseworker. Automatically. Because some decisions should never be made by an algorithm alone. Web-based, no install, 3 languages, accessible from any device, in English, Spanish, or French. What we learned The hardest problem wasn't building the AI. It was resisting the temptation to add many features, and instead building fewer things that actually work end to end, from intake to confirmed help. We learned that demographic parity is not just an ethical choice but a technically defensible one when ground-truth labels are historically biased. Equalized odds sounds better in a textbook, but requires unbiased labels that don't exist in social services data. We learned that the loop, verifying help arrived, is what separates a navigator from a directory. And we learned that showing a working demo in the first 60 seconds matters more than explaining architecture for 3 minutes. What's next for Zen Immediate roadmap: Automated follow-up reminders via email (opt-in), so users don't have to remember to check back. Organization portal, partner organizations list their resources directly, receive matched cases, and track outcomes. The architecture already supports this; the portal is the next layer. Demand forecasting, feed organizations predictions of where need will peak before it peaks, so they can deploy resources proactively instead of reactively. Longer term: Expand beyond food assistance to housing, healthcare, childcare, and employment. Real-time capacity updates from partner organizations. Multi-city deployment leveraging the existing OpenStreetMap architecture, which already works US-wide. Deeper integration with 211 systems and official benefits APIs. <div