---
slug: "flowfi-sw3jeg"
url: "https://devpost.com/software/flowfi-sw3jeg"
title: "FlowFi"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 416
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/financial_record"
---

# FlowFi

> FlowFi ,is an effortless web application that allows users to keep track of their monthly expenditure. Allowing them to budget properly and maintains active financial freedom

[Devpost](https://devpost.com/software/flowfi-sw3jeg) · hackathon [[Build Beyond Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[financial_record]]

**stack** css3, html5, javascript, next.js, node.js, tailwind, vercel

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what's next for flowfi

## Body

This is the demo of flowfi with a demo budget given to spend to see how the app works and tracks finances Inspiration Traditional budgeting apps act like static bank statements—they show you where your money went, but offer very little foresight into where your financial health is heading. We were inspired to build FlowFi to transform budgeting from a reactive chore into a predictive science. We wanted to build an intelligent platform that doesn't just record expenses, but proactively calculates daily spending allowances, forecasts month-end liquidity, and lets users simulate "what-if" financial scenarios using interactive AI. What it does FlowFi is an AI-powered predictive budget intelligence dashboard built to help users make smarter financial decisions in real time. Key features include: Interactive FlowFi AI Assistant: A floating AI chatbot that parses natural language inputs (e.g., "Spent $24 on lunch at Chipotle") and dynamically renders custom interactive SVG pie charts directly inside the chat window. Daily Burn-Rate Velocity: Calculates a safe, dynamic daily spending allowance based on remaining billing cycle days and projected liquid cash:$$\text{Daily Allowance} = \frac{\text{Total Income} - \text{Total Spent}}{\text{Days Remaining}}$$ "What-If" Scenario Simulator: Allows users to adjust interactive sliders (e.g., reducing dining or discretionary spend by $x\%$) to see real-time impact on month-end balance forecasts.Natural Text & Receipt Parser: Instant expense logging that auto-detects categories, merchant names, and purchase values.Recurring Charge & Category Allocation Tracking: Real-time progress bars monitor active budget thresholds and upcoming subscriptions. How I built it Frontend Framework: Next.js 14 / React (App Router) with client-side state management. Styling & UI Components: Tailwind CSS for a dark-mode glassmorphism theme, combined with lucide-react icons. Interactive Data Visualization: Custom-built SVG rendering algorithms inside React components to produce responsive pie charts dynamically within the chat interface. Deployment & CI/CD: Deployed on Vercel with production builds optimized for instant cold starts. Challenges I ran into Creating a lightweight SVG pie chart component that dynamically calculates arc paths ($M, L, A, Z$ commands) and renders cleanly inside a chat bubble without external charting library bloat. Navigating Next.js App Router component boundaries (Server vs. Client components) and resolving strict path alias configurations during production builds on Vercel. What's next for FlowFi The next step for FlowFi is to make an Ai chatbot to help organize finances in the easiest manners possible with pie charts to show spending in different categories, i also want to make the ai a financial advisor, any financial concerns can be prompted to the Ai and valid information will be given <div