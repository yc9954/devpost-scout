---
slug: "scopeai-okczsu"
url: "https://devpost.com/software/scopeai-okczsu"
title: "ScopeAI"
hackathon: "Build with MeDo Hackathon "
organization: "Baidu"
winner: true
words: 674
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
---

# ScopeAI

> Turn client chaos into a clean Scope of Work in 5 minutes powered by guided AI conversation, built entirely with MeDo.

[Devpost](https://devpost.com/software/scopeai-okczsu) · hackathon [[Build with MeDo Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]]
**user** [[small_business]]
**substrate** [[document_pdf]] [[sensor_telemetry]]

**stack** html2canvas, html2pdf.js, localstorage, medo-ai-native, node.js, react, supabase, vite

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for scopeai

## Body

Landing Page ScopeAI generates a complete, professional Scope of Work after 6 guided questions with Refine, Copy, and Download PDF options. The AI guides users through 6 steps one at a time with a live demo mode that shows the full flow automatically. Progress tracked Inspiration I run BlindspotLab, a productized build studio in Lagos. I've shipped 20+ products across AI, SaaS, and Web3. Every single time I onboard a new client, the same problem shows up: they describe a "simple" project, scope creep hits by week two, and someone loses money. Usually me. The best habit I ever built was writing a tight Scope of Work before touching any code. But most freelancers don't know how to do that. They shouldn't need a consultant to figure it out. ScopeAI exists to fix that. What it does ScopeAI is a conversational AI tool that takes a messy project description and through 6 guided questions asked one at a time generates a complete, professional Scope of Work document in under 5 minutes. The output includes: Project Overview Goals & Success Metrics Full Scope of Work (deliverables) What's Out of Scope Milestones & Timeline (3 phases) Pricing Recommendation with milestone payments Post-Launch Maintenance Retainer Next Steps The AI doesn't just accept vague answers. If you say "landing page, hero, navbar" when asked for deliverables, ScopeAI pushes back: "Those are components, not deliverables. What are the three core functional modules this project must do?" That intelligent pushback is what makes this a real tool, not a fancy form. After generation, users can refine the SOW through continued conversation ("make it more formal", "add a retainer tier", "break milestone 2 into two parts") and download the final document as a formatted PDF. How I built it 100% MeDo. One master prompt. Zero external APIs. Zero manual configuration. Zero npm installs done by hand. MeDo built: The entire multi-turn conversation engine The 6-step progress tracking sidebar SOW generation with proper markdown rendering PDF export via html2pdf.js (including diagnosing and fixing a missing html2canvas peer dependency crash) Session persistence via localStorage Dark/light mode toggle Example project prefill cards on the landing page All meta tags, favicon, and OG data The LLM powering the SOW conversation inside the app is MeDo-native. No OpenRouter. No Claude API. No OpenAI key. MeDo handled the entire AI layer as part of the build itself. I gave prompts MeDo gave me a product. Challenges I ran into The most critical bug was a blank screen crash caused by html2pdf.js having an undeclared peer dependency on html2canvas. When Vite resolved the static import at startup, the missing require("html2canvas") crashed the entire module graph before React could mount. MeDo's AI Quality Analysis diagnosed the root cause precisely recommended installing html2canvas and switching to a dynamic import() inside the function body, so the PDF library only loads on demand. That level of autonomous debugging is something I hadn't seen on any build platform before. Accomplishments that I'm proud of Went from idea to deployed product in under 3 hours The AI pushback logic works correctly, but it doesn't just accept bad answers; it guides users to better ones The generated SOW is professional enough to send to a real client immediately 100% MeDo-native no external LLM APIs required PDF export produces a clean, properly formatted document What I learned MeDo isn't just a builder tool it's a build partner. The difference matters. A tool executes your instructions. A partner understands what you're trying to achieve and fills in what you didn't think to ask for. I also learned that the best AI-native products aren't the ones with the most features they're the ones where the conversation IS the product. Every feature in ScopeAI exists to serve one conversation. That constraint made it better. What's next for ScopeAI SOW templates by industry (SaaS, Web3, mobile, brand) Client-facing share link send the SOW directly for approval without downloading Team collaboration multiple stakeholders can refine the same SOW Integration with invoicing tools (Wave, QuickBooks) A BlindspotLab-branded version for studio clients <div