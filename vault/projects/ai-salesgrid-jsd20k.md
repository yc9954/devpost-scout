---
slug: "ai-salesgrid-jsd20k"
url: "https://devpost.com/software/ai-salesgrid-jsd20k"
title: "AI SalesGrid"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 617
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/labor_employment"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# AI SalesGrid

> Real-Time AI Sales & Account Managers Organization Powered by Amazon Nova & AWS Bedrock multi-agent that eliminates pricing mistakes, compliance risk and accelerate sales cycle for Enterprises.

[Devpost](https://devpost.com/software/ai-salesgrid-jsd20k) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[labor_employment]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** agent, ai, amazon-dynamodb, amazon-rds-relational-database-service, amazon-redshift, amazon-web-services, aws-api-gateway, aws-bedrock, aws-ecs, docker, lambda, nova, opensearch, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai salesgrid

## Body

AI SalesGrid Architect Demo 1 Demo 2 Demo 3 Demo 4 Demo 5 Demo 6 Inspiration The "dark matter" of enterprise sales—the hours spent digging through policy PDFs, calculating margins in spreadsheets, and manually drafting proposals—often stalls momentum just when a deal is heating up. We were inspired to build AI-SalesGrid to eliminate these bottlenecks. Our goal was to move beyond simple chatbots and create a coordinated digital workforce. We wanted to give sales teams a "superpower" that handles the administrative and analytical heavy lifting in real-time, allowing humans to focus on what they do best: building authentic relationships. What it does AI-SalesGrid is a multi-agent orchestration platform that manages the end-to-end sales lifecycle. Instead of a single AI trying to do everything, the system employs a hierarchy of specialized agents: Head Account Manager (Root Agent): The "brain" that delegates tasks and uses AWS Bedrock with Nova LLM Model. Solution Agent: Analyzes client needs against the internal knowledge base to ensure technical feasibility. Pricing Agent: Validates discounts and margins against strict company guardrails. Risk & Proposal Agents: Conduct automated due diligence and generate professional, template-ready documentation. Reporting Agent: Synthesizes complex deal data into concise executive summaries for leadership dashboards. How we built it We leaned heavily into the AWS Ecosystem to ensure the platform was enterprise-ready from day one: Brainpower: We utilized AWS Nova Pro and Lite for its high speed and massive context window, enabling fluid multi-agent dialogues. Orchestration: Built with AWS Bedrock (Agents - KB - Flow), allowing us to define clear tool-use boundaries and agent handoffs. RAG (Retrieval-Augmented Generation): We integrated AWS Bedrock Knowledge Base with OpenSearch and S3 to ground our agents in a company-rules-kb, ensuring they never hallucinate pricing or policy. Infrastructure: The entire stack is containerized with Docker and deployed on ECS and Lambda for serverless scalability, with Redshift and Dynamodb and RDS handling the data layer. Challenges we ran into The biggest hurdle was Agent Hand-off Logic. Ensuring the Head Account Manager knew exactly when to transition from the "Solutioning" phase to the "Pricing" phase without losing context was a complex prompt-engineering challenge. We also had to implement strict grounding checks; we couldn't afford to have a Pricing Agent suggest a discount that violated company margin thresholds. Balancing the creative freedom of Generative AI with the rigid logic of corporate financial rules required multiple iterations of our tool-calling schemas. Accomplishments that we're proud of Seamless Collaboration: Seeing five different agents pass a single client inquiry back and forth to produce a finalized, risk-assessed proposal in seconds was a "eureka" moment. Enterprise Rigidity: We successfully integrated a "Human-in-the-loop" feel where the AI respects complex business constraints (like margin limits) while maintaining a conversational interface. Full-Stack Integration: Creating a cohesive workflow that bridges the gap between raw data in Cloud Storage and an executive-ready dashboard. What we learned We discovered that specialization beats generalization. A single, massive prompt trying to handle sales, pricing, and risk is prone to error. However, by breaking these into "Micro-Agents," the system becomes significantly more reliable and easier to debug. We also learned that the quality of an AI’s output is directly tethered to the quality of its Grounding Data—using AWS Bedrock was a game-changer for maintaining a "single source of truth." What's next for AI SalesGrid The roadmap for AI-SalesGrid is focused on even deeper immersion: Native CRM Hooks: Building direct, bidirectional connectors for Salesforce and HubSpot to automate data entry. Predictive Analytics: Moving from "What is this deal worth?" to "What is the probability of this deal closing?" using AWS Redshift and AWS SageMaker ML. Multilingual Support: Expanding the agentic workflow to support global sales teams with real-time translation and localized regional pricing logic. <div