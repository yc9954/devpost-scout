---
slug: "zero-hour-df5jie"
url: "https://devpost.com/software/zero-hour-df5jie"
title: "Zero Hour"
hackathon: "ML Empowerment Build Challenge 2.0"
organization: "ML Empowerment Foundation"
winner: true
words: 714
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# Zero Hour

> A AI Engineer assessment platform to test how efficient a software is being made .

[Devpost](https://devpost.com/software/zero-hour-df5jie) · hackathon [[ML Empowerment Build Challenge 2.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[transportation]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]]

**stack** amazon-dynamodb, amazon-ec2, amazon-web-services, express.js, javascript, llama, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zero hour

## Body

Features The entire architechture UI UI UI UI Zero Hour Inspiration The software engineering interview process is fundamentally broken. Companies continue to test candidates on binary tree inversions or dynamic programming puzzles, which rarely reflect the day-to-day realities of software development. We were inspired to build a platform that measures what truly matters: navigating a sprawling codebase, debugging existing systems, understanding complex architecture, and writing clean, maintainable code. What it does Zero Hour is an advanced, AI-driven technical assessment platform that drops candidates directly into real-world codebases with actual business requirements, bugs, and architectural challenges. By providing a fully functional, cloud-hosted Visual Studio Code environment directly in the browser—complete with a terminal and file system—candidates can use the tools they are actually comfortable with. Upon submission, an integrated "AI Mentor" analyzes their work and provides instant, objective, and constructive feedback based on real software engineering principles. How we built it Zero Hour is built on a distributed, modern tech stack designed for security, scalability, and an exceptional user experience: Frontend (Vercel): A blazing-fast, React-based single-page application built with Vite. The UI features a premium "glassmorphism" design system, smooth micro-animations, and dynamic visual feedback, secured via Google OAuth. Backend Orchestrator (AWS EC2 + Express): A Node.js control plane that orchestrates user sessions and dynamically provisions isolated workspaces. Workspace Environments (Docker): When a candidate starts a challenge, the orchestrator spins up a unique Docker container running code-server (VS Code in the browser), pre-loaded with the specific challenge repository. Routing & Security (AWS CloudFront): Acts as a reverse proxy, handling SSL termination and strictly routing HTTPS API traffic alongside persistent Upgrade: websocket connections required by the IDE terminal. AI Evaluation (AWS Bedrock): The platform extracts the candidate's git diff and passes it to our LLM-powered AI Mentor to generate a structured evaluation scorecard. Challenges we ran into Building a platform that dynamically provisions servers and routes WebSockets across a CDN presented severe technical hurdles: WebSocket Proxying through CloudFront: The VS Code terminal relies heavily on persistent WebSockets. Initially, CloudFront aggressively cached or dropped these connections. We had to carefully configure custom cache behaviors, Origin Request Policies, and header forwarding ( Upgrade , Sec-WebSocket-Key ) to ensure the IDE remained responsive. React State Synchronization: We faced challenging race conditions where asynchronous localStorage token parsing caused authenticated users to get caught in redirect loops. We solved this by implementing strict synchronous initialization barriers in the React lifecycle and robust try-catch JSON parse error boundaries. Scale-to-Zero Cost Optimization: Running heavy EC2 instances continuously is prohibitively expensive. We had to engineer a robust background daemon that tracks active Docker session heartbeats to systematically shut down instances when load drops to zero. Accomplishments that we're proud of We are incredibly proud of the infrastructure cost optimizations and our custom evaluation algorithms . By building the Scale-to-Zero daemon, we successfully slashed infrastructure costs by over 90% during off-peak hours. Mathematically, instead of cost growing linearly ($C_{\text{static}} = c \cdot T$), our cost is a definite integral of the server's active state $A(t) \in {0,1}$ over time: $$C_{\text{dynamic}} = \int_{0}^{T} c \cdot A(t) \, dt$$ Because assessments are bursty and sparse, $\int A(t) \, dt \ll T$, resulting in massive savings. Furthermore, we are proud of our intelligent AI scoring algorithm. Rather than just checking if code "works," our model penalizes excessive code churn to encourage elegant solutions over brute-force rewrites: $$S = \max \left( 0, \sum_{i=1}^{N} w_i \cdot \text{Eval}_i - \lambda \cdot |\text{Diff}|_0 \right)$$ (Where $w_i$ represents weighted architectural criteria and $\lambda$ is a penalty factor for the $L_0$-norm of the git diff). What we learned We learned how to successfully orchestrate complex, stateful infrastructure (Docker + WebSockets) behind stateless CDNs (CloudFront). We deepened our understanding of React's rendering lifecycle to resolve insidious redirect loops, and ultimately mastered the art of balancing high-end, premium UI aesthetics with rock-solid, cost-efficient backend architecture. What's next for Zero Hour Expanded Codebases: Introducing more diverse, real-world repositories spanning different languages and frameworks (e.g., Python/Django, Go microservices). Conversational AI Mentor: Evolving the AI from a post-submission grader into an active pair-programming partner that can provide gentle hints if a candidate gets completely stuck during the assessment. ATS Integration: Seamlessly plugging Zero Hour into popular Applicant Tracking Systems (like Greenhouse and Lever) to fully automate the recruiter workflow. <div