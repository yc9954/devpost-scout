---
slug: "talentos"
url: "https://devpost.com/software/talentos"
title: "TalentOS"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 600
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# TalentOS

> From resume to interview — get placement-ready faster.

[Devpost](https://devpost.com/software/talentos) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[education]] [[finance_payments]] [[labor_employment]] [[retail_commerce]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]]
  <sub>weak: document_pdf</sub>

**stack** api, cayu.ai, cloud, email/password-authentication-+-sessions, linkedin-optimization, llm-powered-ai-analysis-(ats-scoring, mock-interview-evaluation), postgresql, project-rewriting, rails-activestorage-(pdf-upload/download), react.js, ruby-on-rails, sandbox, stripe

## How they structured the write-up

- about the project — talentos (placement buddy)
- what we built
- business aspect — stripe monetization
- what we learned
- how we built it
- challenges we faced
- why talentos matters

## Body

About the Project — TalentOS (Placement Buddy) TalentOS (Placement Buddy) is an AI-powered placement readiness platform built specifically for college students to bridge the gap between “having skills” and actually getting shortlisted. The inspiration came from noticing how many students struggle during placements—not because they lack potential, but because they don’t know how to present themselves across the full hiring pipeline. Resumes get rejected by ATS, LinkedIn profiles look incomplete, project descriptions feel generic, and interviews become stressful. TalentOS solves this end-to-end by bringing Resume + LinkedIn + Projects + Interviews into a single placement pipeline. What We Built TalentOS includes four core AI-powered features : 1) Resume Scoring & ATS Fixing Users upload their resume and receive: ATS score + keyword gap analysis strengths and improvement areas role-based missing keyword suggestions an option to generate an ATS-optimized Resume v2 for a strong before → after improvement 2) LinkedIn Optimization Users get a LinkedIn profile score with: section-wise evaluation (headline, summary, experience, skills, etc.) improvement priorities role-fit keyword recommendations and profile boost guidance 3) Project Rewriter (STAR/XYZ Engine) Users enter a Project Title and description, and TalentOS rewrites it into recruiter-ready bullets using: STAR framework XYZ framework metric placeholder suggestions and keyword enrichment 4) Mock Interview Coach A JD-based mock interview module where users answer questions and receive: structured scoring on clarity, relevance, confidence, and depth improved sample answers actionable feedback and readiness insights Business Aspect — Stripe Monetization To make TalentOS startup-ready (not just a hackathon demo), we integrated Stripe to support a sustainable business model using a Freemium + Credits → Pro Subscription system. Free Plan (Credits System) Every new user receives: 3 ATS resume scans 3 LinkedIn analyses 3 project rewrites 3 mock interviews (5 questions each) This ensures users experience real value before upgrading. Student Pro (Paid Subscription) After free credits are used, users can upgrade via Stripe Checkout to unlock: unlimited usage across all features ATS Resume v2 generation + downloads LinkedIn headline/about optimization pack full mock interview reports and improvement plans export-ready placement outputs Stripe webhooks are used to activate premium access instantly after payment and keep subscription status persistent across sessions. What We Learned Building TalentOS taught us that AI for placements isn’t only rewriting text — it’s about creating measurable progress and a workflow that feels like a real product. We learned how to: design a complete placement pipeline instead of isolated tools create scoring systems and structured evaluation rubrics ensure consistent AI outputs using structured formats for reliable UI implement authentication and session persistence build monetization logic using Stripe while keeping the UX smooth How We Built It TalentOS was designed as a modern SaaS dashboard with: clean UI/UX focused on outcomes structured modules with scorecards, keyword chips, and improvement lists role/JD-based personalization for realistic and relevant results freemium gating + paid unlocks using Stripe subscriptions Challenges We Faced A key challenge was balancing speed, reliability, and output quality while processing resume uploads and generating analyses. We also faced: async processing delays and ensuring results update correctly avoiding generic AI responses by aligning outputs to role/JD context maintaining a smooth journey from dashboard → feature → output implementing credits and subscription access without session issues Why TalentOS Matters TalentOS is built for the exact moment students need support the most: placements . Instead of switching between multiple tools (resume checker, LinkedIn builder, interview prep apps), students get one integrated pipeline that takes them from “not ready” to placement-ready with clarity, confidence, and a clear path forward. ✅ One dashboard. Full placement pipeline. Real results — and a real business model. <div