---
slug: "protetsus"
url: "https://devpost.com/software/protetsus"
title: "ProtectSUS"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 842
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "domain/security_privacy"
  - "user/developer"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# ProtectSUS

> It protects us from sus

[Devpost](https://devpost.com/software/protetsus) · hackathon [[NexHacks]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[legal_justice]] [[security_privacy]]
**user** [[developer]] [[patient_family]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** amazon-ec2, amazon-web-services, docker, figma, github, llm, mongodb, nextjs, python, pytoch, react, tailwind, typescript

## How they structured the write-up

- overview
- what inspires us
- how we built it
- how the github integration works
- challenges we ran into
- accomplishments we're proud of
- what's next

## Body

Github app available for installation Landing page of PROTECTSUS Admin dashboard Finetuned gpt4o model loss/accuracy graph New Pull Request with Security/Bug fixes Automated Merged Pull Request Rejected Pull Request used for Reinforcement Learning and make new PR with user preference fixes Token compression and multi agent orchestration Accept Pull Request agent conversation Pull Request Data for Reinforcement Learning ProtectSUS Project Description Overview In 2024, 90% of tech organizations suffered at least one successful cyberattack, many of which stemmed from preventable human error and misconfiguration. Traditional security scanners flag syntax patterns but miss the logic flaws and edge cases that cause expensive breaches. ProtectSUS (it protects us from sus) is a multi-agent AI copilot that goes beyond detection to understand vulnerabilities in context and automatically generate fixes. Two specialized agents debate each finding challenging severity, context, and exploitability, while a third synthesizes their analysis into effective summaries. This approach surfaces only genuine threats with context-aware remediation, turning the vulnerability that would've cost $4.5M into a pull request merged before lunch. What inspires us As people looking into our own futures in startups and tech and as people who all rely on healthcare systems where record high breaches have patient data at risk, we felt the stakes of poor security tooling personally. We were tired of watching developers drown in false positives from tools that don't understand code context. Alert fatigue isn't just annoying, it's also ridiculously expensive. When such a high percentage of breaches trace back to human error and the average incident costs adds into the millions, we realized the problem isn't that developers don't care about security, it's that existing tools cry wolf so often that real threats get ignored. We built ProtectSUS because we believe security tooling should work like a trusted senior engineer: challenging assumptions, explaining the "why," and offering solutions, not just dumping a list of maybes and then moving on. How we built it Frontend We used Next.js 14 and TypeScript to build a fast, reliable website. Login: Users sign in with their GitHub account via NextAuth.js . Design: Built with Tailwind CSS for a clean "Dark Mode" look that works on phones and desktops. Features: A dashboard to pick your code, a real-time scanner, and a viewer that highlights exactly where your code is vulnerable. Backend The heavy lifting happens in a Python -based system. AI Agents: Instead of one AI, we use a team of agents ( OpenAI, Claude, and Gemini ) that work in parallel. One looks for general bugs, another checks your third-party libraries, and a third that summarizes their debate. Smart Fixing: If a bug is found, our system writes a fix. We use a Machine Learning model that looks at 20 different factors to predict if a human would actually like the fix before we suggest it. Fine Tuning: We fine-tuned our model using OpenAI API on specific security patterns to ensure consistent and accurate vulnerability detection across different codebases. Databases: We use MongoDB to store results and also used it as a RAG system, enabling our AI agents to query historical vulnerability patterns and successful fixes to improve their analysis accuracy and recommendations over time. How the GitHub Integration Works The app is built to turn "finding a bug" into "fixing a bug" automatically: Access: You give us permission; we fetch your list of projects. Clone & Scan: When you commit or create a pull request, our backend clones your code, runs the AI team, and writes code patches. The Auto-PR: If the AI is confident, it automatically creates a new branch and opens a Pull Request on your GitHub. Feedback Loop: You can type /approve or /deny on the GitHub PR. If you deny it, the AI reads your feedback, learns what it did wrong, and tries to write a better fix (up to 3 times). Challenges we ran into Learning from People: Getting our AI to understand "human feedback" (like a comment on a PR) and turn it into better code was tough. The "Auth" Headache: Keeping users logged in securely while they moved between the landing page and the dashboard took a lot of fine-tuning. Agent Arguments: Sometimes our different AI agents disagreed. We had to build logic to make sure they reached a useful conclusion instead of arguing forever. Accomplishments we're proud of The "Full Loop": We successfully built a system that finds a bug, writes a fix, and handles your feedback on GitHub without you ever leaving your workflow. Agent Courtroom: Seeing our "Red Team" and "Blue Team" AI agents argue about code and actually find real bugs was a huge win. Self-Improving Fixes: Our system doesn't just guess; it uses a "confidence score" to make sure the fixes it suggests are high-quality. What's next Instant Audits: Checking your code in a more speedy manner every single time you push to GitHub. More Language Support: Expanding from specialising in Python and JS to things like Rust and Go. Better Learning: Upgrading our "approval predictor" so the AI gets smarter the more people use it. <div