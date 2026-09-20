---
slug: "sentinel-poyh3v"
url: "https://devpost.com/software/sentinel-poyh3v"
title: "Sentinel"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 742
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
---

# Sentinel

> Sentinel is an AI security engineer that scans your app, proves vulnerabilities with real attack simulations, and ships production-ready fixes before hackers find them.

[Devpost](https://devpost.com/software/sentinel-poyh3v) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]] [[labor_employment]] [[security_privacy]] [[supply_logistics]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]]

**stack** browserbase, fetchai, redis, sentry

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

🛡️ Sentinel Inspiration AI coding tools have made it possible for anyone to build and deploy software in hours. Platforms like Cursor, Claude Code, Replit, and Lovable dramatically lower the barrier to shipping products, but they don't answer a critical question: "Is this application actually secure?" We noticed that many founders, indie hackers, and student developers were deploying production applications without understanding common security risks such as exposed API keys, broken authentication, injection vulnerabilities, and insecure dependencies. Traditional security tools are designed for security professionals and often generate overwhelming reports filled with jargon and false positives. We wanted to build a security platform that works for the new generation of AI-powered builders—a system that doesn't just detect vulnerabilities, but actually proves, explains, and fixes them. What it does Sentinel is an AI-powered security platform that uses multiple specialized agents to scan applications, validate vulnerabilities, generate fixes, and continuously monitor security posture. Instead of producing long vulnerability reports, Sentinel follows a complete workflow: Detect vulnerabilities using specialized AI security agents. Simulate real-world attacks inside isolated sandboxes. Explain findings in plain English with visual evidence. Fix vulnerabilities by generating production-ready patches. Monitor applications continuously with a Trust Score. Sentinel can identify issues such as: Exposed secrets and API keys Authentication and authorization flaws SQL injection and XSS vulnerabilities Missing rate limits Vulnerable dependencies and supply-chain risks The result is a security experience that is understandable even for non-security experts. How we built it Sentinel combines three major components into a unified security pipeline: AI Security Engine We built a multi-agent architecture consisting of: Coordinator Agent Secrets Detection Agent Authentication Agent Injection Testing Agent Rate Limiting Agent Supply Chain Agent Validation Agent These agents work in parallel to investigate applications and verify findings. Exploit Simulation Layer Using Browserbase and isolated cloud sandboxes, Sentinel safely reproduces vulnerabilities against sandboxed copies of applications. Findings are only escalated when an exploit can actually be reproduced, dramatically reducing false positives. Platform Infrastructure Our stack includes: Next.js for the frontend Cloudflare Workers and Durable Objects for orchestration Browserbase for browser automation Upstash Redis for queues and rate limiting PostgreSQL and Prisma for persistence Anthropic and OpenAI models for reasoning and patch generation Sentry and Arize AI for observability Once a vulnerability is verified, Sentinel generates a fix and can automatically create a GitHub pull request containing the patch. Challenges we ran into Reducing false positives One of the biggest challenges in application security is alert fatigue. Most scanners report issues that are not actually exploitable. To address this, we built a validation layer that requires every finding to be reproduced in an isolated sandbox before it is considered verified. Safe exploit execution Running attack simulations is inherently risky. We needed a way to test exploits without touching production systems. We solved this by spinning up isolated environments for every scan, ensuring all attack activity remains contained. Multi-agent orchestration Coordinating multiple autonomous security agents introduced challenges around consistency, duplicate findings, and patch conflicts. We introduced dedicated Coordinator and Validator roles to manage communication and maintain deterministic results. Explaining security to non-experts Security reports are often difficult to understand. We spent significant effort translating technical findings into plain-language explanations supported by visual evidence and guided remediation. Accomplishments that we're proud of Built a fully functional multi-agent security workflow. Created a validation system that proves exploitability before reporting issues. Generated real patches instead of generic remediation suggestions. Integrated live browser-based attack simulation. Produced an experience that makes security accessible to non-security builders. Unified detection, validation, explanation, and remediation into a single platform. What we learned Building Sentinel taught us several important lessons: Proof beats detection. A verified exploit is far more valuable than hundreds of theoretical warnings. Specialized agents outperform giant prompts. Giving each agent a focused responsibility improved reliability and reasoning quality. Security is also a UX problem. Users care less about vulnerability names and more about understanding risk and fixing it quickly. Isolation is critical. Safe testing environments are essential for trustworthy automated security validation. What's next Our roadmap includes: Launching a production-ready VS Code extension. Expanding continuous monitoring capabilities. Supporting additional vulnerability classes such as SSRF, CSRF, and IDOR. Releasing mobile notifications and voice-based security summaries. Building organization-wide security dashboards and Trust Passports. Our vision is simple: Make application security as accessible as modern AI coding tools. Sentinel helps builders understand what is vulnerable, see how it can be exploited, and fix it before attackers ever get the chance. <div