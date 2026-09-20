---
slug: "green-basket-2wutmx"
url: "https://devpost.com/software/green-basket-2wutmx"
title: "CogniOps"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 531
team_size: 0
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# CogniOps

> AI-powered cloud learning & developer productivity platform built on AWS helping students understand cloud concepts & developers generate architectures, Terraform and debug code using Amazon Bedrock.

[Devpost](https://devpost.com/software/green-basket-2wutmx) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[health_clinical]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[structured_db]]

**stack** amazonapigateway, amazonbedrock, amazondynamodb, amazoniam, amazonlambda, amazons3, awscognito, dart, flutter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cogniops

## Body

Inspiration Cloud computing is one of the highest-demand skills in tech, yet most learners — especially from Tier-2 and Tier-3 cities in India — are stuck watching passive tutorials with no real guidance. Developers also waste hours switching between documentation, architecture tools, cost calculators, and debuggers. CogniOps was built to fix that — an AI mentor powered by Amazon Bedrock that takes a learner from "what is AWS Lambda?" all the way to generating production-ready Terraform infrastructure. What it does CogniOps is a dual-mode AI cloud platform — persona locked at registration. Student Mode (CogniBot Student — Powered by Claude on Bedrock) AI Chat mentor that gives real-time answers, generates 8-week personalized roadmaps, and creates visual AWS architecture diagrams on request Quiz Generator with difficulty levels — scores tracked and shown on dashboard Progress Dashboard with XP points, day streak, modules done, and avg score Voice input support (mic button) for hands-free learning Multilingual support — EN/TA/HI language toggle Developer Mode (CogniBot Dev — Powered by Claude on Bedrock) AI Chat that recommends full AWS architecture stacks for any app idea Architecture Generator — describe your app, get Overview + visual Diagram + Terraform + Cost breakdown in 4 tabs Backend Designer — paste your code, get recommended AWS services, API endpoints, database suggestions, and implementation notes Terraform Generator — describe infrastructure, get production-ready HCL code with copy button Socratic Debug Assistant — guides you to the fix with diagnostic questions, likely causes, and step-by-step fix instructions How we built it Frontend: Flutter Web — hosted on Amazon S3 Backend: AWS Lambda (Python) + Amazon API Gateway AI Engine: Amazon Bedrock — Claude Sonnet 4.6 Auth: Amazon Cognito Database: Amazon DynamoDB Monitoring: Amazon CloudWatch + AWS IAM All requests from Flutter hit API Gateway → Lambda → Bedrock. User progress and chat history are stored in DynamoDB. Cognito handles role-locked authentication. Challenges we ran into Dual persona in one codebase: Two completely different toolsets in one Flutter app required careful Provider-based state management and role-aware Lambda functions. Prompt engineering per feature: Every screen needed its own AI personality — the debugger guides without giving answers, the Terraform generator outputs real production code, not pseudocode. Serverless cold starts: Initial Lambda latency was high. Mitigated through provisioned concurrency, keeping average AI response time at 2–4 seconds. Flutter Web + Cognito: Managing auth tokens across Flutter Web required careful CORS handling at API Gateway. Accomplishments that we're proud of Fully deployed live app on AWS with real Amazon Bedrock responses — not a mockup End-to-end serverless architecture that scales automatically 2–4 second average AI response time for architecture generation and concept explanations Scalable to 1000+ concurrent users at ~$120/month What we learned Prompt design is product design — the same Bedrock model gives drastically different quality based on system prompt structure Flutter Web on S3 is a serious, fast, cheap deployment path Serverless-first architecture forces good stateless design decisions Role-locking at registration eliminates an entire class of conditional UI logic What's next for CogniOps Multilingual voice interaction using Amazon Transcribe (Hindi + regional languages) Visual AWS architecture diagram generation as SVGs One-click Terraform + CloudFormation export from Developer Mode Dedicated Android/iOS mobile app <div