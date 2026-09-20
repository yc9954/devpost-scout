---
slug: "denarii"
url: "https://devpost.com/software/denarii"
title: "Denarii"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 551
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/researcher"
  - "substrate/document_pdf"
---

# Denarii

> Denarii is your AI financial advisor, helping you make smart purchase decisions and guiding you toward your first million. Weighted Decision Matrix combined with Multi-Criteria Decision Analysis.

[Devpost](https://devpost.com/software/denarii) · hackathon [[Code with Kiro Hackathon]]

## Facets

  <sub>weak: cross_origin_web</sub>
**user** [[researcher]]
**substrate** [[document_pdf]]

**stack** firebase, github, javascript, json, kiro, next.js, react, tailwind-css, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for denarii

## Body

Denarii Logo Decision output Decision output Pro-mode analysis Main page, purchase analyzer tool Inspiration As a recent Computer Science graduate with a passion for personal finance, I wanted to merge my technical skills with my mission to help people make smarter financial choices. Many believe financial independence is unattainable, but decades of research show that consistent, disciplined decisions can make it possible. When I first tried Kiro, I was impressed by its spec-driven development workflow—it felt like having a professional engineering team ready to turn my vision into production code. That experience inspired me to build Denarii, a personal finance assistant that empowers users to answer one deceptively simple question: “Should I buy this?” What it does Denarii analyzes potential purchases using a Weighted Decision Matrix (WDM) combined with Multi-Criteria Decision Analysis (MCDA). It considers factors like affordability, utility, risk, and opportunity cost, then outputs a recommendation and a breakdown of strengths and concerns. It also has a fully functional AI voice advisor and AI chat advisor that will guide users in how to use the app and will provide financial advice where appropriate. It aims to: Classify purchases as essentials, discretionary items, or high-value buys Provide a transparent score based on research-backed thresholds Help users prevent lifestyle inflation and build a path toward financial independence How I built it Spec-driven planning with Kiro Started each major feature in spec mode, generating EARS-style user stories, design documents, and implementation tasks. Accepted criteria ensured clarity and traceability from idea to code. Decision model implementation Built structuredDecisionModel.js to calculate WMD & MCDA Kiro generated scoring functions and weighting logic based on my requirements. Iterative improvements with vibe mode Used vibe mode for small updates and quick bug fixes without rewriting specs. Automation with Kiro hooks Created a hook that triggers on edits to decision-model files, updating tests and README documentation automatically to stay in sync with the latest logic. Challenges I ran into Scope control – It was tempting to add too many features; spec mode helped me stay focused. Trusting AI-generated code – I learned to review, refine prompts, and iterate until the output matched my vision. Math to code translation – Implementing MCDA meant studying academic sources and converting theoretical models into working algorithms. Accomplishments that I'm proud of Implemented a complete WDM + MCDA system with adjustable weights based on user risk tolerance. Designed a maintainable architecture from the ground up using Kiro’s spec-driven workflow. Built a Kiro agent hook that automatically updates tests and documentation when key decision-model logic changes. Balanced quick creativity (vibe mode) with disciplined planning (spec mode) to deliver a polished, functional product. What I learned How to structure complex projects by breaking them into clear specs, designs, and granular tasks. How to leverage AI as a true development partner, not just a code generator. The importance of keeping tests and documentation in sync with evolving logic—and how to automate that process. How a transparent, research-driven decision model can be communicated in simple, user-friendly terms. What's next for Denarii Integration with user's financial data sources so recommendations reflect a user’s actual budget and spending trends. Expanded decision models to include sustainability, ethical considerations, and resale value. Mobile app version for quick, on-the-go purchase decisions. Community-driven presets where users can share and adopt decision-criteria weight profiles. <div