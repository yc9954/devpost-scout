---
slug: "mba-to-commas"
url: "https://devpost.com/software/mba-to-commas"
title: "MBA to Commas"
hackathon: "Build with MeDo Hackathon "
organization: "Baidu"
winner: true
words: 584
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "user/educator_student"
  - "substrate/structured_db"
---

# MBA to Commas

> Free, AI-powered MBA admissions coaching for first-gen and underrepresented applicants — the same playbook elite consultants charge $10K+ for, built end-to-end on MeDo.

[Devpost](https://devpost.com/software/mba-to-commas) · hackathon [[Build with MeDo Hackathon]]

## Facets

**domain** [[education]] [[finance_payments]] [[housing_homeless]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** ai, chatbot, education, javascript, mba, medo, no-code, react

## How they structured the write-up

- inspiration
- what it does
- how i built it with medo
- the most impressive feature medo built
- challenges i ran into
- what i learned
- what's next for mba to commas

## Body

MBA to Commas Inspiration First-generation college students and underrepresented professionals are systematically locked out of top MBA programs — not because they're less qualified, but because they don't have the $10,000+ admissions consultants, family connections, and insider playbooks that wealthy applicants take for granted. I lived this gap myself. MBA to Commas exists to close it. What it does MBA to Commas is a free, AI-powered admissions platform for first-gen and historically underrepresented MBA applicants (Black, Latino/a, Indigenous, low-income, women in finance/consulting). It packages the same coaching, resources, and community that elite consultants sell behind paywalls into one always-on app. Users get: An AI MBA Coach trained on the elite-consulting playbook, the Consortium / Forté / Toigo / Reaching Out / MLT fellowship landscape, and the application strategies of the M7/T15 Eight self-paced workshops covering everything from "Is the MBA right for you?" to "Mastering the Stanford Essays" A searchable resource library with the top 25 US MBA program profiles, scholarship database, application checklists, and an MBA glossary written for people whose families don't speak the language A community forum organized by school, application round, and topic A financial literacy module — including an MBA Cost Calculator, scholarship-vs-loan visualizer, and post-MBA salary infographic — because first-gen applicants rarely have family financial advice on six-figure decisions How I built it with MeDo I structured the build as a single, dense prompt followed by targeted iterations. The first prompt was the architecture: brand identity, six core modules (Home, AI Coach, Workshops, Resource Library, Community, Financial Literacy), an onboarding wizard, content scope (8 workshops fully written, 25 school profiles, 12+ scholarships, 30+ glossary terms, 15+ seed community posts), and the design system. MeDo generated the full multi-page dashboard from that single prompt — sidebar navigation, all six modules wired up, sample content populated. From there I iterated through MeDo's multi-turn chat: refining the AI Coach's system prompt to specialize on URM/first-gen applicants, expanding the financial calculators with realistic default data, and tuning the community forum's seeded posts so the launch experience didn't feel empty. The most impressive feature MeDo built The Financial Literacy module . From a single paragraph in my prompt, MeDo generated an interactive MBA Cost Calculator (school + housing + opportunity cost), a scholarship-vs-loan tradeoff visualizer with a working slider, a post-MBA salary infographic by industry, and a plain-English breakdown of Federal vs. private vs. refinance loan products. That's the differentiator first-gen applicants need most — and MeDo built the whole thing with working logic, not a static mock. Challenges I ran into The hardest part was making the AI Coach feel like a peer instead of a corporate chatbot. It took several prompt iterations to land on a voice that's specific, honest, and never patronizing — a voice that talks to first-gen applicants like the ambitious professionals they already are. What I learned A single, well-structured prompt beats fifty vague ones. The difference between a generic AI app and a useful one is whether you bring real domain knowledge to the prompt. I poured my own MBA application research, fellowship pipeline expertise, and financial-literacy gaps into one detailed brief — and MeDo turned it into a working platform. What's next for MBA to Commas Verified-admit badge program (manual review of acceptance letters) Live group AMAs with Black/Latino MBA grads from each M7 program Mobile app Partnerships with the Consortium, MLT, and Forté to embed the tool in their existing pipelines Built for the Build with MeDo Hackathon — Learning & Education track. <div