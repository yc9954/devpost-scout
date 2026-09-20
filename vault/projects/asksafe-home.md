---
slug: "asksafe-home"
url: "https://devpost.com/software/asksafe-home"
title: "AskSafe Home"
hackathon: "H0: Hack the Zero Stack with Vercel v0 and AWS Databases"
organization: "Amazon"
winner: true
words: 528
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# AskSafe Home

> AskSafe Home helps seniors pause, understand risk signals, and choose a safer next step when a message, call, video chat, or payment request feels uncertain.

[Devpost](https://devpost.com/software/asksafe-home) · hackathon [[H0- Hack the Zero Stack with Vercel v0 and AWS Databases]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[elder_child_care]] [[finance_payments]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** amazon-bedrock, aws-dynamodb, cloudformation, github, guardrails, iam, next.js, react, shadcn/ui, tailwind-css, terraform, typescript, v0, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges
- accomplishments
- what we learned
- what’s next

## Body

Situation selection screen that keeps the safety check simple, focused, and senior-friendly. Guided input flow where AskSafe helps the user describe what happened before showing a result. Pause-first result with safer next step, risk signals, and verification guidance. Inspiration AskSafe Home was inspired by a simple problem: when an older adult receives an uncertain message, call, video chat, or payment request, the hardest part is often not technology itself. It is the pressure of deciding what to do next. Many safety tools focus on detecting scams. We wanted to build something narrower and more human: a calm safety decision workflow that helps seniors pause, understand risk signals, and choose one safer next step before acting. What it does AskSafe Home guides a user through one uncertain situation at a time. The user can describe what happened by typing or voice, select what the other person is asking them to do, and receive a clear result with: a safer next step what to hold off on risk signals that stood out why the situation is worth a pause safer verification steps official Australian help links optional trusted support The product does not claim to prove whether something is real or fake. It helps the user slow down, check through safer channels, and stay in control. How we built it We built AskSafe Home as a full-stack web product using Next.js App Router, TypeScript, React, Tailwind, shadcn/ui-style components, and Vercel. We used v0.app for rapid UI exploration and iteration, then hardened the product with server-side routes, DynamoDB persistence, Bedrock-assisted explanation, validation and fallback logic, Terraform-managed AWS infrastructure, GitHub Actions, and FinOps guardrails. Amazon DynamoDB is the primary backend database for privacy-safe safety events, feedback outcomes, trusted support actions, user setup, household setup, and Bedrock quota counters. Amazon Bedrock is used only as bounded explanation assistance. Deterministic rules still own the safety structure, and Bedrock output is validated before use. We also prepared a visual architecture diagram showing the Vercel, Next.js, DynamoDB, Bedrock, Terraform, GitHub Actions, and FinOps guardrail flow. Challenges The biggest challenge was avoiding a generic chatbot or an overconfident “scam detector.” In high-pressure safety moments, vague AI answers can reduce trust. We had to design a workflow that is calm, structured, and honest about uncertainty. We also had to balance AI usefulness with privacy and cost control. AskSafe uses input limits, rate limits, quota checks, deterministic fallback, and FinOps hard stops so the product can remain shippable and safer to operate. Accomplishments We built a live product with: production Vercel deployment DynamoDB-backed event persistence Bedrock-assisted explanation with validation and fallback trusted support flow official Australian help links voice input and read-aloud support Terraform and GitHub Actions infrastructure workflow production smoke checks architecture documentation and evidence pack What we learned We learned that the strongest product direction is not “AI detects scams.” It is “AI-supported safety workflow.” For seniors, the most valuable outcome is often clarity: what to pause, what not to do yet, and how to verify safely. What’s next Next steps include deeper guided clarification, stronger trusted support workflows, screenshot or image review, more official verification pathways, and accessibility testing with older adults and community partners. <div