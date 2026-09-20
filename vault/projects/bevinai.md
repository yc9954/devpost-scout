---
slug: "bevinai"
url: "https://devpost.com/software/bevinai"
title: "bevinAI"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 1271
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# bevinAI

> Better than devin😉

[Devpost](https://devpost.com/software/bevinai) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]]

**stack** api, confluence, css, django, express.js, html5, javascript, jira, mcp, mysql, node.js, npm, nvidia, pnc

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bevinai

## Body

Inspiration Project Management lifecycle is broken. In a high-stakes, regulated environment like PNC , the friction between development, project management, and business goals isn't just inefficient. We were inspired to solve this by building a true AI Project Manager. We didn't want another dashboard. We wanted a central "brain" powerful enough to manage the entire lifecycle, from the initial idea for a new service to the final, secure, and optimized code. That's why we built bevinAI from the ground up on NVIDIA's NIM and Nevatron platforms to create an autonomous PM that could meet the speed, security, and scale requirements of an industry leader like PNC . What it does bevinAI is an AI powered orchestration engine that acts as the central nervous system for your development lifecycle. It automates the high level cognitive work of project management, allowing PNC to launch new services faster and more securely. PNC can go from a simple idea (like "a new rewards feature") to a fully-planned project in minutes. bevinAI autonomously: Performs market and tool research. Generates a detailed Cost Analysis and Functionality Report. Recommends the optimal Tech Stack after analyzing pros, cons, and costs. Uses NVIDIA NIM to instantly generate a complete JIRA board with Epics, User Stories, set deadlines, Tasks. Once a project is active, bevinAI's most powerful features kick in: 📈 Cost Optimization Reporting : After deployment, bevinAI generates an "Evidence Based Report" that analyzes the new service's infrastructure. It identifies redundant processes or over provisioned resources, providing a clear path to reduce overhead costs which is a massive value add for managing PNC's large scale cloud infrastructure. How we built it We built bevinAI as a three-part system, with the NVIDIA AI "Brain" at the absolute center. The AI Brain (MCP Server): This is the heart of bevinAI , built on NVIDIA's stack. It's a Python based FastAPI server that runs our NVIDIA Nevatron Bots . All high level reasoning market research, cost benefit analysis, JIRA ticket generation, and our critical code validation all is handled by API calls to a NVIDIA NIM (Nemotron-70B) endpoint . The Backend (The "Nervous System"): A robust Python and Django application. It manages the project state and connects the AI brain to all of PNC's enterprise tools . We use MCP (Model Context Protocol to manage the AI's long-running tasks asynchronously, so the user never has to wait. The Frontend (The "Face"): A clean React and JavaScript dashboard hosted on AWS Amplify. It provides a "single pane of glass" for a PNC project manager to interact with the AI and see data from JIRA and GitHub in one place. Our tech stack is a pipeline: The React frontend captures the user's intent. The Django backend schedules the job. And the NVIDIA NIM powered MCP server executes the cognitive work. Challenges we ran into Reasoning, Not Just Text: We couldn't just generate "pretty text." We needed the AI to produce structured, hierarchical JSON that the JIRA API would accept. This required sophisticated, multi stage prompt engineering on the NVIDIA NIM platform to teach the AI how to think like a senior project manager and break a concept like "new payment service" into a 50 item JIRA board . Validating Code to Requirements: The hardest part was the PR validator . Teaching an AI to read raw code (a diff) and semantically compare it to a human language requirement (an "Acceptance Criteria") is a massive reasoning leap. Only a powerful model like Nemotron 70B was capable of this abstract analysis. Enterprise-Scale Orchestration: Connecting five different APIs (NVIDIA, JIRA, GitHub, Slack, Confluence) while managing state (like "is this PR for this JIRA ticket?") was a huge challenge. The NVIDIA Nevatron bot framework was essential for managing this complex orchestration Accomplishments that we're proud of The "Idea-to-JIRA" Pipeline: We are incredibly proud of the "Create New Service" flow. Watching a one-sentence idea for a new banking product get transformed by NVIDIA NIM into a fully-planned JIRA project in under 10 minutes is game-changing. It proves we can cut PNC's speed-to-market for new products by weeks, if not months. The "Update Service" Template: This is more than a feature; it's a core solution for any large enterprise. Building a workflow that can safely analyze and manage PNC's existing legacy systems is a massive accomplishment and a key differentiator. What we learned NVIDIA NIM is an Enterprise Orchestrator, Not a Chatbot: Our biggest lesson was that the true power of NVIDIA's platform is not chat. Its power is in structured data generation and complex reasoning. We learned to use NIM as the "cognitive engine" to power our entire workflow, from JSON generation to code analysis. AI is the Ultimate "Glue": We learned that in an enterprise like PNC, the biggest problems live between the tools. AI is the perfect "glue" to connect JIRA, GitHub, and Slack. bevinAI's MCP, powered by NVIDIA, acts as the central hub that finally gets all the tools to talk to each other. Prompt Chaining is Key for Complex Products: You can't plan a financial service in one prompt. We learned to "chain" NVIDIA NIM calls: Prompt 1: Analyze this new product idea. Prompt 2: Take that analysis and research 3 tech stacks. Prompt 3: Take the chosen stack and generate the epics. This mimics a human thought process and delivers far more accurate results. 🚀 Key Features & Flows Idea → JIRA in Minutes From a natural-language idea, bevinAI: Runs market & feasibility analysis Suggests architecture and stack Generates a fully linked JIRA board (Epics, Stories, Tasks) with rationale Meeting-Aware Tickets Meeting summaries are not just text; they are binding references. Every critical rule or decision is mapped into one or more tickets. Tickets remain in sync as new clarifications or changes are discussed. AI-Powered PR Validation For each PR, bevinAI: Reads the diff Pulls the linked ticket’s requirements Checks semantic alignment: implementation vs acceptance criteria Flags: Missing requirements Unauthorized scope creep Conflicts with prior decisions This acts as an automated compliance and quality gate. 🔗 Solana Integration for Verification & Efficiency To further harden trust and performance, we integrate Solana as a verification and audit ledger for ticket and workflow integrity: Each generated JIRA ticket set or critical workflow (e.g., “Idea-to-Board” snapshot, major spec update, PR block/approval event) can be: Hashed Anchored onto Solana This gives: Immutable traceability of who agreed to what and when A verifiable chain linking: Meeting decisions JIRA structures PR validations Because Solana is optimized for high throughput and low latency, this verification layer adds: Minimal overhead Fast confirmation of events A scalable foundation for “git-vision”-style views of: How specs evolve How fast aligned tickets are generated Whether processes are being followed in real time This combination—NVIDIA-powered reasoning + Solana-backed verification—makes bevinAI a powerful, efficient, and trustworthy way to ensure that no time is wasted and that teams are always building exactly what was intended. What's next for bevinAI AI-Powered Legacy Code Analysis: We will supercharge our "Update Service" template by having NVIDIA NIM ingest an entire existing PNC codebase. The AI will then automatically identify risks, suggest modernization paths, and flag potential security vulnerabilities before a single line of new code is written. Autonomous Code Generation: Go beyond tickets. We want bevinAI to read its own JIRA tasks and automatically generate the boilerplate Django models, DRF serializers, and React components, pushing them to a new GitHub branch for a developer to review. Automated Compliance & Security Scanning: We will expand the AI-Powered PR Validator to not just check acceptance criteria, but to also perform automated security and compliance scanning specific to PNC's regulatory requirements, making every PR "pre-audited". <div