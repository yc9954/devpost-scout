---
slug: "claimi"
url: "https://devpost.com/software/claimi"
title: "Claimi"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 550
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Claimi

> Millions of people are eligible for class action settlements, but most people don’t know they’re eligible. Claimi is an AI-powered settlement claim discovery and application management platform.

[Devpost](https://devpost.com/software/claimi) · hackathon [[NexHacks]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[vision_ocr]]
**domain** [[finance_payments]] [[legal_justice]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** gemini, javascript, mcp, openai, opus, python, react, sql, sqlite, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for claimi

## Body

Inspiration Claimi is Simplify for settlement claims. Every year, billions of dollars in settlement money goes unclaimed simply because people don’t know they’re eligible or don’t want to deal with confusing, tedious claim forms. We realized that the process feels exactly like doing taxes before TurboTax or managing bills before Simplify — painful, fragmented, and easy to procrastinate. We wanted to build something that turns a messy, legal, multi-step process into a one-click, guided experience powered by AI agents. What it does Claimi is an AI-powered claim assistant that: Discovers active settlement or insurance claims Parses eligibility rules into structured, verifiable logic Interviews the user with only the minimum necessary questions Matches the user to claims they’re likely eligible for Builds a personalized evidence checklist Guides the user to submit the claim and tracks status + deadlines Instead of hunting through legal pages and filling out repetitive forms, users answer a few questions and Claimi does the rest. How we built it We built Claimi using a full-stack JavaScript and TypeScript architecture with Next.js powering the web application and a custom Chrome extension handling local form autofill. The backend uses API routes to orchestrate AI workflows that ingest claim pages, extract eligibility rules, generate evidence checklists, and draft pre-filled claim packets. We store case data and user state in a lightweight database and use a deterministic rules engine to make eligibility decisions. LLMs are only used where they add real value: parsing messy legal text into structured rules, explaining matches in plain language, and generating user-friendly instructions. The Chrome extension runs entirely on the user’s machine to safely and transparently fill official claim forms, keeping the user in control of the final submission. Challenges we ran into Legal text is extremely messy and inconsistent across different claim sites, and many pages mix marketing, FAQs, and legal notices in one giant blob of HTML. Designing something that feels “one-click” while still keeping the user in control and legally safe was also surprisingly difficult. We had to carefully decide what the AI should propose versus what must be deterministic and auditable, and the tight time constraints forced us to be very disciplined about scope and automation. Accomplishments that we're proud of In 24 hours, we built a full end-to-end agent pipeline that turns real legal eligibility text into structured, auditable rules. We created an adaptive interview agent that asks only the minimum necessary questions, generates real claim packets and evidence checklists, and produces a system that feels magical while still keeping the user informed and in control. What we learned We learned that the hardest part of claims isn’t submitting the form, it’s understanding the requirements and preparing the right information. We also learned that AI works best when it proposes and explains rather than silently making decisions, and that combining deterministic logic with LLM agents produces far more reliable systems than using LLMs alone. What's next for Claimi Next, we want to expand Claimi to insurance reimbursement claims such as medical, travel, and renters claims, add a browser extension that safely autofills forms in place, and build partnerships with claim administrators and insurers. We also want to add email and portal monitoring agents to track claim status automatically and move toward a true personal claims inbox for everything you’re owed. <div