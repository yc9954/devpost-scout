---
slug: "compliant-workflows-for-jira"
url: "https://devpost.com/software/compliant-workflows-for-jira"
title: "Compliant Workflows for Jira"
hackathon: "Codegeist 2025: Atlassian Williams Racing Edition"
organization: "Atlassian"
winner: true
words: 966
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/regulation_legal_text"
---

# Compliant Workflows for Jira

> Configure Jira for regulatory compliance in pharma, medtech, fintech, and more—no guesswork required.

[Devpost](https://devpost.com/software/compliant-workflows-for-jira) · hackathon [[Codegeist 2025- Atlassian Williams Racing Edition]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]] [[regulation_legal_text]]

**stack** atlaskit, forge, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for compliant workflows for jira

## Body

View compliance warnings Audit configured statuses Audit configured transitions Configure user restrictions Configure required fields Apply fixes Generate a report Download a configuration report Inspiration This project was inspired by a problem I’ve seen again and again while working with regulated life sciences teams: they want to use Jira Cloud, but they don’t fully trust it. Pharma, medical device, and other highly regulated organizations are under pressure to modernize and adopt agile tools, yet Jira provides no compliance-specific guidance out of the box. The result is uncertainty, delayed adoption, and teams relying on parallel compliance systems to feel confident using Jira. In practice, the challenge isn’t that Jira can’t be compliant. It’s that configuring it correctly requires uncommon overlapping expertise: Jira admins usually understand workflows, but not FDA or ISO expectations while QA and validation professionals understand regulations, but not Jira’s configuration model That gap leads to the same anti-patterns everywhere: closed records that aren’t properly protected, overly permissive transitions, and missing or inconsistent configuration documentation. I’ve helped fix these issues repeatedly, and I realized most organizations were solving the same problems from scratch, often with significant time, cost, and stress. What it does This app helps regulated teams audit, fix, and document their Jira Cloud workflows with confidence. It connects directly to Jira and analyzes existing workflows exactly as they are configured today. It evaluates statuses and transitions against compliance-focused rules based on real-world regulatory expectations and the most common failure patterns seen in audits and validations. When risks are identified, the app explains what’s wrong and why it matters. For most issues, it also provides guided, automated fixes that allow administrators to remediate problems safely and without manually editing complex workflow configurations. This reduces reliance on trial and error and makes it easier for IT and QA teams to work from a shared, compliant foundation. Finally, the app generates audit-ready workflow reports directly from the live configuration in Jira. These reports capture how workflows are designed and which controls are in place, giving teams clear, usable documentation for validation, internal reviews, and regulatory audits. The result is a practical tool that helps regulated organizations use Jira Cloud with greater speed, confidence, and peace of mind. How I built it I built this app entirely on the Atlassian Forge platform to ensure security, reliability, and tight integration with Jira Cloud. Front-end: The app runs inside Jira’s admin portal and uses a Custom UI built with React and Atlaskit components. The UI uses Forge resolvers to interface with the compliance rules in the Forge-based backend. Back-end: The app reads live workflow configurations through Jira’s REST APIs. The compliance rules engine analyzes workflow statuses and transitions in real time, identifying risks and generating structured findings based on how Jira is actually configured. Storage: Currently, the app uses no data storage. Everything is processed in real time via the REST APIs. Runs on Atlassian: The entire application runs exclusively on Atlassian infrastructure using Forge’s hosted runtime, permissions model, and secure UI bridge. No customer data leaves Atlassian’s environment. This architecture aligns with the Runs on Atlassian program and reflects the same principles that regulated teams expect from their own validated systems: clear boundaries, traceability, and trust by design. Challenges I ran into AI Assistance I decided to use this project as an opportunity to learn how to work with AI coding agents during development. Although I have decades of experience as a software developer, this was my first time building a production-grade system with AI support. Finding a productive workflow took longer than expected. Early on, the AI often produced partially working code that was difficult to maintain. There was no time savings at first, and I spent a lot of effort refactoring and stabilizing the app. As the prototype matured, however, the AI became a real accelerator. REST API Navigation Managing workflows through Jira’s REST APIs was another challenge. Some critical endpoints are in transition, with older versions deprecated and newer ones still in beta. Navigating these changes required careful research and testing, but all required functionality was available, allowing the core features to work as expected. Accomplishments that I'm proud of Seeing the app work in real environments has been especially rewarding. Even as an experienced Jira administrator, configuring a compliant workflow manually often takes an hour or more. Watching the app analyze, fix, and document a workflow in under a minute exceeded my expectations. More importantly, early results show that the app can meaningfully reduce uncertainty and rework for regulated teams. Turning complex compliance tasks into a guided, repeatable process is exactly what I set out to achieve. What I learned Forge is improving Forge has matured significantly over the years. Having used it in 2021, 2023, and now again for this project, I’ve seen major improvements in stability, tooling, and developer experience. Today, I feel confident building and supporting customer-facing applications on Forge in regulated environments. AI is just like working with a junior teammate This project reinforced that AI works best when treated like an entry-level developer. With clear instructions and small, focused tasks, it can produce high-quality output quickly. Without guidance, it can introduce subtle problems. Learning how to supervise and structure AI-assisted development has been one of the most valuable outcomes of this project. What's next for Compliant Workflows for Jira There is a significant opportunity to expand the functionality based on early feedback and real-world use. Planned next steps include: More advanced configuration and remediation support Integration with electronic signatures and other common third-party tools A library of predesigned, compliance-ready workflow templates AI-assisted workflow analysis to suggest more optimized statuses, transitions, and pathways The long-term goal is to give regulated teams a clear, trusted path to using Jira Cloud confidently, without constant second-guessing, heavy consulting support, or unnecessary complexity. <div