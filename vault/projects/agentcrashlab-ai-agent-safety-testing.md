---
slug: "agentcrashlab-ai-agent-safety-testing"
url: "https://devpost.com/software/agentcrashlab-ai-agent-safety-testing"
title: "AgentCrashLab — AI Agent Safety Testing"
hackathon: "Pixel Forge AI Hackathon ($18,000+ in Prizes)"
organization: "Pixel Forge"
winner: true
words: 520
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/genomic_bio"
---

# AgentCrashLab — AI Agent Safety Testing

> AgentCrashLab tests AI agents with real-world failure scenarios, finds unsafe behavior, explains what went wrong, and verifies safer versions.

[Devpost](https://devpost.com/software/agentcrashlab-ai-agent-safety-testing) · hackathon [[Pixel Forge AI Hackathon -18-000- in Prizes-]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[developer_tools]] [[health_clinical]] [[labor_employment]] [[security_privacy]]
**user** [[developer]]
**substrate** [[genomic_bio]]

**stack** bullmq, express.js, google-gemini, neon, node.js, postgresql, prisma, react, redis, render, tailwind-css, typescript, vite, zod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agentcrashlab

## Body

Inspiration As AI agents become more capable of using tools and taking actions, testing only their final responses is not enough. An agent can sound correct while silently making an unsafe tool call. We wanted to build a practical way to answer a simple question: “What happens when we deliberately try to break an AI agent?” That idea led to AgentCrashLab. What it does AgentCrashLab is a crash-testing and regression platform for AI agents. Developers can register an agent and run adversarial scenarios against it, including prompt injection, authorization failures, unsafe refunds, contradictory instructions, ambiguous requests, tool failures, timeouts, and goal drift. The platform captures execution traces and explains failures through Failure DNA , showing the expected behavior, observed behavior, tool involved, evidence, and remediation hint. It also supports failure mutation and v1 vs v2 comparison , allowing developers to test whether a hardened agent actually improved. How we built it We built the frontend with React, Vite, TypeScript, and Tailwind CSS . The backend uses Node.js, Express, and Zod , with PostgreSQL and Prisma for persistent data. Crash tests are processed asynchronously using Redis and BullMQ , with a dedicated evaluator worker running the sandboxed agent scenarios. We use Google Gemini for scenario generation, mutations, and nuanced evaluation when available. Safety-critical checks remain deterministic and rule-based, such as detecting refunds without confirmation. The complete application is deployed on Render, with Neon PostgreSQL and Upstash Redis. Challenges we ran into One of our biggest challenges was making the evaluation reliable. Using an LLM alone to decide whether an action is safe can introduce inconsistency. We solved this by separating objective safety checks from more subjective evaluation. Critical behaviors are checked deterministically, while Gemini is used only where flexible reasoning is useful. Another challenge was making failures understandable instead of simply returning a pass/fail result. This led us to build execution traces and Failure DNA so developers can understand exactly what went wrong. Accomplishments that we're proud of We are proud that AgentCrashLab doesn't just detect failures — it creates a complete test → diagnose → fix → retest workflow. Our demo includes a Customer Support Agent with tools such as order search, cancellation, refunds, and email. We intentionally created a vulnerable v1 and a stricter v2 so that the platform can demonstrate measurable improvement rather than just theoretical safety. We also built adversarial test generation, failure mutation, execution traces, Failure DNA, analytics, and version comparison into one workflow. What we learned We learned that AI agent reliability is about behavior, not just responses . A successful-looking response does not necessarily mean the agent behaved safely. Tool calls, permissions, recovery behavior, and adherence to constraints all need to be tested. We also learned the value of combining deterministic rules with LLM-based evaluation rather than relying completely on either approach. What's next for AgentCrashLab We want to take AgentCrashLab beyond a hackathon prototype by supporting more agent frameworks, richer attack libraries, CI/CD integration, automated regression gates, stronger isolation, and deeper observability. Our long-term goal is simple: Make testing AI agents as natural as testing traditional software — before they reach production. <div