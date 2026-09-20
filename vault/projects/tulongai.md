---
slug: "tulongai"
url: "https://devpost.com/software/tulongai"
title: "TulongAI"
hackathon: "USAII® Global AI Hackathon 2026"
organization: "USAII"
winner: true
words: 728
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "user/legal_professional"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# TulongAI

> AI-powered benefits navigator helping Filipino families discover which of 4 government programs they may qualify for — in plain language, with real next steps.

[Devpost](https://devpost.com/software/tulongai) · hackathon [[USAII- Global AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[developer_tools]] [[education]] [[housing_homeless]] [[labor_employment]] [[retail_commerce]]
**user** [[legal_professional]] [[social_worker]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** fastapi, framer-motion, github, github-actions, groq-api-(llama-3.3-70b), jwt, python, react, tailwind-css, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tulongai

## Body

Inspiration The DSWD website was built for caseworkers who already understand the system. TulongAI was built for Maria in Caloocan — four kids, just lost household income, one hour before school pickup. In the Philippines, an estimated 2 million eligible families have never applied for benefits they qualify for, mainly because eligibility is split across 4 separate agencies (DSWD, PhilHealth, DOLE, SSS), each with technical, English-heavy rules and zero explanation when a check fails. With roughly 1 DSWD social worker per 500+ urban poor households, most families have no one to ask. What it does TulongAI checks eligibility across 4 government programs simultaneously — 4Ps, PhilHealth, TUPAD, and SSS — and shows the user: A may-qualify / may-not-qualify result per program, with a confidence score A full plain-language reasoning trace (not a black-box yes/no) Conflicts between programs (e.g. 4Ps vs. TUPAD) A document checklist and real office addresses NGO alternatives when no government program fits — "no" is never the final answer A bilingual (English/Filipino) AI chat assistant for follow-up questions How we built it Backend: Python + FastAPI. A deterministic rules engine ( backend/engines/ ) evaluates each program against officially documented thresholds (sourced and cited per program) — this part never touches an LLM, so it can't hallucinate an income threshold. A separate AI layer (Groq / Llama 3.3 70B) turns the rules engine's raw JSON into a warm, plain-language explanation and powers a general chat assistant. Frontend: Vite + React + Tailwind CSS, with an intake form, a full eligibility results view, and a floating chat widget. Deployment: Frontend on GitHub Pages, backend on Render, connected via a GitHub Actions build pipeline. Challenges we ran into Deciding where AI belongs: we deliberately kept the actual eligibility decision rules-based and deterministic, using AI only for explanation and conversation — judges specifically wanted this justified, not assumed. Wording: shifting every "you are eligible" to "you may qualify" throughout the UI, AI prompts, and reasoning trace, so the tool never overstates certainty about a government decision it doesn't actually make. Connecting a static frontend (GitHub Pages) to a live backend (Render) across CORS and environment-variable boundaries in CI/CD — our first deploy silently failed because the build never received the backend URL, and CORS blocked the real one until we fixed both. A bad git checkout midway through the hackathon left a large number of backend files at 0 bytes with no error message, costing real build time before we traced it back to the actual missing code. Accomplishments that we're proud of A genuinely deterministic eligibility core: the parts of the system that decide whether someone may qualify never touch an LLM, so the rules engine can't invent an income threshold — only the explanation layer is generative. Built and shipped a fully working, fully deployed two-service app (static frontend + live API) end to end within the build window, including CI/CD. Took the "never say you qualify" requirement seriously enough to rewrite wording across the UI, the rules engine's reasoning trace, and both AI system prompts (English and Filipino) — not just the marketing copy. A bilingual experience that isn't an afterthought — Filipino translations exist at the prompt level, not just the UI strings. What we learned The most "AI" part of a responsible AI product is often deciding what not to hand to the model. Judges reward an explicit answer to "why is an LLM better here than a rules engine" more than a flashier demo. Responsible AI guardrails are cheap to add once you know what to look for (wording, source citations, confidence display) — the hard part is noticing they're needed in the first place. Free-tier infrastructure (Groq, Render, GitHub Pages) is genuinely enough to ship a real product during a hackathon — the constraint was our own setup mistakes, not the tools. What's next for TulongAI A "what-if" scenario simulator: let a user model how a decision (taking an informal job, a change in household size) shifts their eligibility across all 4 programs before they act, not just check their status today. Expand beyond 4 programs to housing assistance and education/training benefits. Replace the illustrative NGO directory with a verified, regularly updated one, ideally sourced directly from partner organizations. A lightweight case-manager mode for frontline barangay health workers who currently rely on outdated pamphlets to serve dozens of families a month. <div