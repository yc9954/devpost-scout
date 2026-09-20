---
slug: "epicstory"
url: "https://devpost.com/software/epicstory"
title: "EpicStory"
hackathon: "Codegeist 2025: Atlassian Williams Racing Edition"
organization: "Atlassian"
winner: true
words: 916
team_size: 0
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# EpicStory

> Turn epic descriptions into production-ready Jira backlogs in seconds. EpicStory app converts epic descriptions into fully structured, reviewable user stories with acceptance criteria and subtasks.

[Devpost](https://devpost.com/software/epicstory) · hackathon [[Codegeist 2025- Atlassian Williams Racing Edition]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]]
**substrate** [[code_repository]] [[structured_db]]

**stack** amazon-web-services, azure, gcp, rovo, typescript

## How they structured the write-up

- what inspired this project
- what we learned
- challenges faced
- key innovations
- impact and results

## Body

EpicStory: Building an Enterprise-Grade AI-Powered Jira Forge App What Inspired This Project EpicStory was born from a fundamental frustration in software development: the tedious, time-consuming process of breaking down epic requirements into actionable user stories and subtasks. Product managers and engineering leads were spending hours manually decomposing high-level features into detailed backlogs, often resulting in inconsistent story formats, missing acceptance criteria, and incomplete task breakdowns. The inspiration came from recognizing that this decomposition process follows predictable patterns that could be automated using Large Language Models (LLMs). However, existing AI tools were either too generic, lacked enterprise security controls, or couldn't integrate seamlessly into existing Jira workflows. The vision was clear: create an AI-native automation tool that turns epic descriptions into production-ready Jira backlogs in seconds, not sprints, while maintaining enterprise-grade security and compliance. What We Learned Technical Learnings Multi-Cloud AI Orchestration is Complex but Essential We discovered that enterprise customers demand choice and redundancy in their AI providers. Building a unified abstraction layer across AWS Bedrock, Azure OpenAI, GCP Vertex AI, and OpenAI taught us that each provider has unique authentication patterns, rate limits, and response formats. Forge Platform Constraints Drive Architecture Working within Atlassian's Forge platform taught us valuable lessons about serverless constraints: 900-second timeout limits required async queue processing for complex generations Storage limitations necessitated efficient data structures and cleanup strategies Security model required careful handling of encrypted credentials in KVS storage Enterprise Security is a First-Class Concern Building for regulated environments taught us that security isn't an afterthought. AES-256-GCM encryption, audit trails, token rotation, and SOC 2 compliance patterns had to be designed into the architecture from day one, not bolted on later. Product Learnings Fallback Strategies are Critical Enterprise customers can't afford AI downtime. The multi-layer fallback system (tenant config → global defaults → circuit breakers) became essential for maintaining service availability during provider outages. Collaboration Between Humans and AI Agents The admin panel's design for both human administrators and coding agents revealed the importance of API-first design. Functions like getProviderHealth and bulkUpdateProviders serve both human UIs and automated monitoring systems. Development Methodology Test-Driven Architecture The codebase includes extensive testing at multiple levels: Unit tests for pure functions and services Integration tests for multi-component workflows E2E tests with Playwright for user journeys Performance tests for large dataset handling Incremental Migration Strategy The UI Kit 2 migration was executed in phases to minimize risk: Challenges Faced Technical Challenges Multi-Provider Authentication Complexity Each AI provider has different authentication mechanisms Creating a unified configuration system while preserving provider-specific requirements was complex. Forge Platform Limitations Atlassian's Forge platform imposed several constraints: Storage Limitations : KVS storage required careful data structure design and cleanup strategies Timeout Constraints : 900-second limits necessitated async processing for complex operations Security Model : Encrypted storage and secure credential handling within Forge's sandbox UI Constraints : Migration from Forge UI to UI Kit 2 required complete frontend rewrite LLM Output Consistency Ensuring consistent, structured output from probabilistic models required: Retry logic for malformed responses Fallback strategies for provider failures Token estimation and cost prediction Concurrent User Management Supporting multiple users generating stories simultaneously required: Credit reservation system to prevent over-commitment Rate limiting to prevent abuse Circuit breakers for provider health management Audit trails for compliance and debugging Product Challenges Enterprise Security Requirements Building for regulated environments meant implementing: AES-256-GCM encryption for all stored credentials Comprehensive audit logging with user attribution Token rotation and expiration management SOC 2 and ISO 27001 compliance patterns Cost Transparency and Control Enterprise customers demanded predictable costs: Real-time usage tracking and analytics Credit-based billing with reservation system Burning rate multipliers for different model tiers Cost estimation before generation User Experience Complexity Balancing power with simplicity was challenging: Supporting both novice and expert users Providing granular control without overwhelming the interface Maintaining performance with complex tree views and selection logic Graceful error handling and recovery Operational Challenges Multi-Cloud Reliability Managing reliability across multiple AI providers required: Health check systems with automatic failover Circuit breaker patterns for degraded providers Monitoring and alerting for provider outages Graceful degradation when providers fail Development Velocity vs Quality Maintaining rapid development while ensuring enterprise quality: Comprehensive testing strategy across unit, integration, and E2E levels Pre-commit hooks with linting, type checking, and testing Specification-driven development to reduce rework Modular architecture enabling parallel development Compliance and Audit Requirements Meeting enterprise compliance standards: Detailed audit trails for all configuration changes Secure credential storage and rotation Data residency and privacy controls Regular security assessments and updates Key Innovations Provider-Agnostic AI Client System The unified ChatClient interface enables seamless switching between providers while preserving provider-specific optimizations. Credit Reservation Pattern Prevents race conditions in multi-user environments while providing transparent cost control and billing. Modular Admin Architecture Complete separation between issue panel and admin functionality enables independent development and testing. Enterprise-First Security Design Built-in encryption, audit trails, and compliance patterns rather than retrofitted security measures. Impact and Results EpicStory transforms epic decomposition from a hours-long manual process into a seconds-long automated workflow while maintaining enterprise-grade security and compliance. The system processes natural language epic descriptions and generates structured Jira backlogs with: 10x Speed Improvement : Epic-to-backlog generation in seconds vs hours Enterprise Security : SOC 2/ISO 27001-ready controls with encrypted credential storage Multi-Cloud Flexibility : Support for AWS, Azure, GCP, and OpenAI with automatic failover Cost Transparency : Real-time usage tracking with predictable credit-based billing The project demonstrates that AI-native automation can be both powerful and enterprise-ready when built with proper architecture, security, and operational patterns from the ground up. <div