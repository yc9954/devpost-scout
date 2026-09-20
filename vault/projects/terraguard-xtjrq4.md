---
slug: "terraguard-xtjrq4"
url: "https://devpost.com/software/terraguard-xtjrq4"
title: "TerraGuard"
hackathon: "MEGA Hackathon 2025"
organization: "MegaHackathonLeague"
winner: true
words: 454
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/structured_db"
---

# TerraGuard

> TerraGuard: Because Your Cloud Shouldn’t Be an Open Bar for Hackers. 🍻

[Devpost](https://devpost.com/software/terraguard-xtjrq4) · hackathon [[MEGA Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** amazon-web-services, langchain, mistral, nextjs, ollama, prisma, tanstack, terraform, terraformer, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for terraguard

## Body

TerraGuard Inspiration I keep coming across stories of people whose cloud bills skyrocketed due to simple misconfigurations. Curious about this issue, I started digging deeper and learned that misconfigurations don’t just lead to unexpected costs—they are also a major security risk. Many high-profile data breaches and cyberattacks happen because of small, overlooked mistakes in cloud infrastructure. This realization inspired me to create TerraGuard , a tool designed to automate security testing and catch misconfigurations before they cause damage . What It Does TerraGuard is a cloud security automation tool that: Imports cloud configurations and scans for security misconfigurations. Runs static security tests using tfsec to detect issues in Infrastructure as Code (IaC). Uses AI for debugging , providing intelligent suggestions and fixes instead of just reporting errors. How We Built It TerraGuard was built using the following technologies: Frontend: Next.js and Tailwind CSS for a clean and responsive UI. Database: Prisma for efficient and scalable data handling. Backend & AI: TypeScript , Ollama , and LangChain for integrating AI-powered debugging. Security Analysis: tfsec for static testing of Terraform configurations. Infrastructure Management: Terraform and Terraformer for importing cloud configurations. Challenges We Ran Into One of the biggest challenges was choosing the right tool for static security testing . Initially, I planned to use Checkov , but I quickly realized that its advanced features required a paid subscription . Since I wanted TerraGuard to be accessible and effective without additional costs , I had to pivot to tfsec at the last minute . This required some quick adaptation, but in the end, tfsec provided a solid open-source alternative. Accomplishments That We're Proud Of Successfully integrating tfsec for static security testing. Implementing AI-driven debugging , making security testing more interactive and developer-friendly . Creating a fully automated security workflow that reduces manual effort in cloud security audits. Overcoming last-minute challenges and delivering a working security tool despite setbacks. What We Learned Cloud misconfigurations are more common than expected and can have severe consequences. AI can enhance static analysis tools by not just detecting misconfigurations but also helping developers fix them. Choosing the right security tools is crucial, especially when considering cost, effectiveness, and integration . Building with Terraform and tfsec provides a solid foundation for cloud security automation. What's Next for TerraGuard While static code analysis is powerful, it has limitations. To extend security testing beyond traditional methods , the next step is to expand AI-powered testing capabilities by: Enhancing AI debugging to provide more detailed insights and automated fixes . Introducing dynamic security testing to analyze cloud environments in real-time. Expanding rule sets to cover more cloud providers and compliance frameworks . Improving the UI/UX to make security testing even more accessible and intuitive . <div