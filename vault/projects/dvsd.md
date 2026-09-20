---
slug: "dvsd"
url: "https://devpost.com/software/dvsd"
title: "NovaSupport — When AI Agents Take Over Customer Support"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 1052
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "domain/legal_justice"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# NovaSupport — When AI Agents Take Over Customer Support

> Customer support is broken. Companies spend billions on support teams, yet customers still wait hours for responses. Agents are overwhelmed with repetitive tickets & critical issues get lost in noise.

[Devpost](https://devpost.com/software/dvsd) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]] [[housing_homeless]] [[legal_justice]]
  <sub>weak: media_journalism</sub>
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]
  <sub>weak: sensor_telemetry</sub>

**stack** amazon, amazon-api-gateway, amazon-bedrock, amazon-cloudwatch, amazon-cognito, amazon-comprehend, amazon-dynamodb, amazon-nova, amazon-polly, amazon-ses, amazon-sqs, amazon-transcribe, amazon-translate, amazon-web-services

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for novasupport

## Body

Dashboard with Tickets and Analytics – Combined overview of tickets, metrics, and support activity in one dashboard Analytics Dashboard – Visual analytics dashboard showing ticket trends, counts, and support insights Support Tickets Dashboard – Unified ticket dashboard for monitoring support requests and recent updates Teams Page – Team collaboration workspace with member details, workloads, and coordination tools Resolved Tickets Page – Archived resolved tickets view for tracking completed support cases NovaSupport — When AI Agents Take Over Customer Support Inspiration Customer support is broken. Companies spend billions on support teams, yet customers still wait hours (or days) for responses. Support agents are overwhelmed with repetitive tickets, and critical issues get lost in the noise. I asked myself: What if AI could handle the entire support workflow — not just answer questions, but actually think, route, prioritize, and escalate like a human team lead? That's when I discovered Amazon Nova on AWS Bedrock. Nova's multimodal capabilities (text, images, documents) combined with its reasoning abilities made it the perfect foundation for building an agentic AI system — one where multiple AI agents collaborate autonomously to resolve support tickets with minimal human intervention. What it does NovaSupport is a fully serverless, agentic AI-powered support ticket system with three portals: User Portal — Customers submit tickets, chat with an AI assistant, track status, and rate resolutions Team Portal — Support agents view assigned tickets, reply, translate messages, and resolve issues Admin Portal — Full dashboard with analytics, SLA tracking, team management, and AI insights The magic happens behind the scenes with 4 AI agents working together: Agent Role Routing Agent Reads ticket content and determines which team should handle it (billing, auth, technical, etc.) Assignment Agent Distributes tickets fairly across team members using round-robin Escalation Agent Flags sensitive tickets (security, legal, compliance) or low-confidence cases for human review Response Agent Generates AI-suggested responses using knowledge base and past resolutions How we built it Architecture User/Agent → API Gateway → Lambda (30+ functions) → DynamoDB ↓ Amazon Nova (Bedrock) ↓ ┌─────────────────┼─────────────────┐ ↓ ↓ ↓ Routing Agent Escalation Agent Response Agent ↓ ↓ ↓ Assignment Agent → SQS Queue → Workflow Orchestrator Tech Stack Infrastructure : AWS CDK (TypeScript) — 100% Infrastructure as Code Compute : 30+ AWS Lambda functions (Node.js 20.x) Database : DynamoDB with single-table design AI/ML : Amazon Bedrock (Nova Lite + Nova Embeddings) Auth : Amazon Cognito (2 user pools — admin/agent and end-user) Storage : S3 for attachments with presigned URLs Messaging : SQS for async ticket processing Real-time : WebSocket API for live notifications Translation : Amazon Translate + Comprehend for auto language detection Voice : Amazon Polly (TTS) + Transcribe (STT) Email : Amazon SES for resolution notifications Key Technical Decisions 1. Single-Table DynamoDB Design Instead of multiple tables, I used a single DynamoDB table with composite keys: PK: TICKET#<ticketId> SK: METADATA PK: TICKET#<ticketId> SK: MESSAGE#<timestamp> PK: TEAM#<teamId> SK: MEMBER#<memberId> This enables efficient queries and atomic transactions across related entities. 2. Agentic Workflow with Confidence Scoring Each AI agent returns a confidence score between 0 and 1. The Escalation Agent uses this to decide when to involve humans: $$ \text{Escalate} = \begin{cases} \text{true} & \text{if } C < 0.7 \text{ or keywords match} \ \text{false} & \text{otherwise} \end{cases} $$ Where $C$ is the confidence score from the Routing Agent. 3. Semantic Search with Nova Embeddings For finding similar tickets and knowledge base articles, I use vector embeddings: $$ \text{similarity}(A, B) = \frac{A \cdot B}{|A| |B|} $$ This cosine similarity calculation helps surface relevant past resolutions. 4. Round-Robin Assignment To ensure fair workload distribution: $$ \text{nextAgent} = \text{members}[\text{index} \mod |\text{members}|] $$ The index is persisted in DynamoDB and incremented atomically. Challenges we ran into 1. Cold Start Latency Lambda cold starts were adding 2-3 seconds to API responses. I solved this by: Using Node.js 20.x (faster startup than Python) Lazy-loading AWS SDK clients Keeping Lambda packages small (~5MB) 2. Multimodal Analysis Pipeline Processing images and documents attached to tickets required careful orchestration. I built a separate SQS queue for multimodal processing to avoid blocking the main ticket flow. 3. Real-Time Notifications WebSocket connections in serverless are tricky. I used API Gateway WebSocket API with DynamoDB to store connection IDs, then broadcast updates when ticket status changes. 4. Translation Auto-Detection Amazon Translate requires a source language, but users don't always know what language they're writing in. I added Amazon Comprehend to auto-detect the language first, then pass it to Translate. 5. Round-Robin State Persistence The assignment agent needed to remember which team member was assigned last. I used DynamoDB atomic counters to ensure consistent round-robin even under concurrent load. Accomplishments that we're proud of Built a true agentic AI system — 4 specialized AI agents that collaborate autonomously, not just a single chatbot 100% serverless architecture — Zero servers to manage, auto-scales from 0 to millions of requests 30+ Lambda functions working together seamlessly with proper error handling and retries Multimodal AI analysis — Nova can analyze text, images, and documents attached to tickets Real-time WebSocket notifications — Instant updates when ticket status changes Multi-language support — Auto-detect and translate tickets in any language Voice support — Speech-to-text and text-to-speech for accessibility Self-learning knowledge base — System gets smarter as more tickets are resolved Fair workload distribution — Round-robin assignment ensures no agent gets overloaded Production-ready — Deployed and running on AWS with proper auth, monitoring, and error handling What we learned Agentic AI is powerful — Breaking down complex workflows into specialized agents makes the system more maintainable and debuggable than one monolithic AI. Nova's multimodal capabilities are impressive — Being able to analyze images, documents, and text in a single model simplifies the architecture significantly. Serverless scales beautifully — With 30+ Lambda functions, the system handles spikes automatically without any capacity planning. Single-table DynamoDB is worth the learning curve — Once you understand access patterns, it's incredibly efficient. CDK > CloudFormation — Writing infrastructure in TypeScript with full IDE support is a game-changer. What's next for NovaSupport Agent memory — Let agents remember context across conversations Proactive outreach — AI detects patterns and reaches out before customers complain Voice-first support — Full voice conversations with AI agents Multi-tenant SaaS — Package NovaSupport as a product for other companies Advanced analytics — Predictive insights on ticket volume and customer satisfaction trends <div