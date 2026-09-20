---
slug: "e-agent-user-violation-detector"
url: "https://devpost.com/software/e-agent-user-violation-detector"
title: "E-Agent user violation detector"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 1123
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "substrate/video_visual"
---

# E-Agent user violation detector

> AI moderation for a Ghana housing platform that detects fake listings, duplicates, and misleading images ensuring renters only see authentic homes.

[Devpost](https://devpost.com/software/e-agent-user-violation-detector) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]] [[labor_employment]]
**substrate** [[video_visual]]

**stack** agentcore, amazon-nova, amazon-web-services, api-gateway, aws-amplify, bedrock, lambda, python, ruby, s3bucket, serverless, strands-agent

## How they structured the write-up

- inspiration
- the system is powered by amazon nova (nova pro) and built using the strands agent framework , deployed on amazon bedrock agentcore . it receives listing and image payloads, evaluates whether they meet platform requirements, and only allows compliant content to proceed to the next stage of processing.
- what it does
- how i built it
- challenges
- accomplishments that i'm proud of
- what i learned
- what's next for e-agent user violation detector

## Body

E-AGENT USER VIOLATION DETECTOR ARCHITECTURE OVERVIEW Inspiration Renting a home in Ghana can be a frustrating and often unfair experience for many people. In the current housing market, informal intermediaries commonly known as agents intercept vacant properties from landlords and then inflate rental prices before presenting them to renters. These intermediaries frequently demand nuisance payments, high commissions and sometimes encourage landlords to demand up to two or three years of rent in advance . This practice significantly increases the cost of renting and places unnecessary financial pressure on tenants. In many cases, homes remain vacant simply because access to them is controlled by intermediaries. To address this problem, I created E-Agent , a platform designed to allow property owners and renters in Ghana connect directly , without the need for exploitative middlemen. During early testing with a small group of users, another challenge quickly became clear. Because the platform allows users to create listings and upload images, there needed to be a reliable way to prevent: Spam listings Duplicate property postings Fake or misleading property details Inappropriate or unrelated images As an early-stage project, hiring human moderators across every region in Ghana was not financially feasible. To solve this, I built the E-Agent User Violation Detector , an intelligent AI moderation layer that automatically reviews all listings and uploaded images before they are allowed to appear on the platform. The system is powered by Amazon Nova (Nova Pro) and built using the Strands agent framework , deployed on Amazon Bedrock AgentCore . It receives listing and image payloads, evaluates whether they meet platform requirements, and only allows compliant content to proceed to the next stage of processing. What it does The E-Agent User Violation Detector acts as an automated moderation layer that protects the platform from spam, misleading content, and inappropriate media. It performs several key moderation tasks: Listing authenticity verification The system reviews new listings and listing updates to determine whether they appear to be genuine property listings. It evaluates important fields such as the location, description, price, and contact information to detect entries that appear fabricated, meaningless, or intentionally misleading. Duplicate listing detection Listings from the same owner are compared to identify potential duplicates. This helps prevent repeated postings of the same property designed to manipulate visibility or mislead users. Image moderation The system analyzes uploaded images to determine whether they actually represent property-related content. Images that appear unrelated to real estate such as selfies, advertisements, offensive or unrelated objects are automatically flagged and removed before they reach platform users. Automated moderation actions When suspicious content is detected, the system can automatically: Suppress listings from appearing in public search results Remove inappropriate images Record the reason why content was flagged Administrative visibility Platform administrators can review flagged listings or images and see clear explanations of why the AI system took action, allowing them to intervene if necessary. How I built it The platform uses a serverless, event-driven architecture built on AWS services. Key components include: AI Moderation Layer: Built with the Strands agent framework and powered by Amazon Nova running through Amazon Bedrock Agent Runtime Frontend Application: React-based interface hosted using AWS Amplify Backend Services: Application logic implemented using AWS Lambda and exposed through Amazon API Gateway Data Storage: Listing data stored in Amazon DynamoDB Event Processing: Asynchronous workflows managed using Amazon SQS and Amazon EventBridge Image Analysis: Image detection is performed using Amazon Rekognition Moderation workflow When a new listing is created or an existing listing is updated , the backend sends the listing data to the AI moderation system for inspection before it can proceed further in the platform workflow. Similarly, when users upload listing images , the upload triggers an automated processing event that sends the image information to the moderation system for evaluation. The AI agent evaluates the data and determines whether the content meets platform standards. If it passes moderation checks, the listing continues through the normal platform pipeline. If violations are detected, the system automatically applies the appropriate moderation action. Challenges One of the biggest challenges in building this system was designing and refining the agent's system prompt . The prompt needed to clearly guide the agent’s reasoning process so it could make reliable moderation decisions and call the correct tools at the appropriate time. Achieving consistent and deterministic behavior required multiple iterations and careful prompt engineering. Another challenge involved working with Bedrock Agent Runtime permissions and configuration . During early development, broader permissions were required to allow the system to function correctly. These permissions are now being refined to meet production-grade security best practices. Additionally, integrating the agent runtime deployment process into a clean CI/CD workflow required extra effort to ensure that configuration and infrastructure changes could be managed reliably. Accomplishments that I'm proud of I am proud that the system now functions as a fully operational automated moderation layer for the platform. Key accomplishments include: New listings are automatically intercepted and inspected before they become visible on the platform. Duplicate or suspicious listings are successfully detected and flagged. Updates to existing listings are re-evaluated to ensure they remain compliant with platform rules. Non–real-estate-related images are automatically identified and prevented from appearing on the platform. The system records clear moderation reasons, allowing administrators to review and manage flagged content effectively. The result is a system that significantly reduces the need for manual moderation while maintaining trust and quality within the platform. What I learned Building this project taught me several valuable lessons: Prompt engineering for agentic systems requires careful iteration. Designing a prompt that produces consistent reasoning and tool usage is a process of continuous refinement. Event-driven architectures are extremely powerful for AI workflows. Using asynchronous services makes it possible to build scalable moderation pipelines that react automatically to user activity. AI moderation must balance strictness with practicality. The system must be strict enough to prevent abuse while still allowing genuine user content to pass through without unnecessary friction. What's next for E-Agent User Violation Detector The next phase of development will expand the moderation system’s capabilities. Planned improvements include: Advanced image validation The system will be extended to detect reused or duplicated images across multiple listings and identify potential image plagiarism. Expanded platform moderation The moderation layer will also be applied to other areas of the platform, such as user comments and messaging , ensuring that harmful or inappropriate content is filtered before being stored or displayed. Appeals and dispute handling Future versions will include AI-assisted review of user appeals for flagged listings , helping administrators handle moderation disputes more efficiently. These improvements will continue moving the platform toward a fully automated trust and safety layer , enabling it to scale while maintaining fairness and integrity for both renters and property owners. <div