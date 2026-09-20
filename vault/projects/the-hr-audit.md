---
slug: "the-hr-audit"
url: "https://devpost.com/software/the-hr-audit"
title: "HR Audit"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 737
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# HR Audit

> Complete AI agent ecosystem for fraud detection & banking. Multiple specialized agents handle alerts, voice calls, account protection, and transactions. Dreaming to serve 1.7B without smartphones.

[Devpost](https://devpost.com/software/the-hr-audit) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[finance_payments]]
**user** [[general_public]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** capital-one-nessie-api, cedaros, flask, javascript, llm, mastra-agent-framework, ngrok, node.js, openai-api, python, react, sendgrid, twilio, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the hr audit

## Body

Application logo Inspiration In today's world, when artificial intelligence is constantly evolving, fraud detection in the banking sector has stayed virtually unchanged. According to Okta, the leader in identity and access management, 70% of customers still prefer to interacting with a human rather than an AI bot when it comes to customer service. At the same time, scammers are continually developing new ways to take people's hard-earned money. That's why we set out to build a learn-on-the-job AI ecosystem, a platform that can respond in real time to even the most sophisticated fraud attempts. What it does We have the video of how our fully automated system works. link Our application re-imagines financial operations by creating a single, interconnected ecosystem where AI agents serve as co-pilots for both consumers and businesses. Users gain unprecedented control and simplicity by proactively detecting security threats, accessing full banking services through simple phone calls, and automating time-consuming operational tasks. Key features include: The AI Security Co-Pilot : The platform's security co-pilot uses a Mastra agent on a Cedar-OS dashboard to analyze fraud with Open AI's Chatgpt , instantly freeze cards, and alert customers via Twilio. AI-Powered Voice Banking : Our voice banking system, powered by Twilio and the Capital One Nessie API, allows users to perform complex financial transactions using natural language over a simple phone call. The Intelligent Productivity Suite : The productivity suite leverages the Mastra framework to act as the system's backbone, automating complex workflows like enterprise emails with SendGrid, scheduling, and document generation. How we built it We integrated a diverse stack of modern technologies to create a robust and intelligent platform. AI & Agent Framework : We used Mastra for AI agent orchestration and OPEN AI's Chatgpt for advanced reasoning and fraud analysis. Frontend & Dashboard : The command center was built with React.js and Cedar-OS to create a modern, interactive dashboard. Backend & Voice API : A Python and Flask backend handles real-time API requests and the core voice banking logic. Communication & Financial APIs : We integrated Twilio for voice, SendGrid for email, and the Capital One Nessie API for banking operations. Challenges we ran into Developing a fully automated application came with several difficult challenges, such as: Complex System Integration : Our main challenge was integrating the React frontend, Mastra AI agent, and Python backend to operate as a single, cohesive system in real-time. Real-Time Latency : Minimizing latency for the voice banking feature was critical, requiring optimization of the entire voice-to-API-to-voice processing loop. State Management in Voice UI : We had to overcome the stateless nature of phone calls by building a custom context management system to enable natural, multi-step conversations. Accomplishments that we're proud of Advanced Email Infrastructure : Implemented SendGrid API integration instead of basic SMTP for professional-grade email delivery and tracking capabilities. AI-First Architecture : Built every feature with intelligent automation at its core, leveraging AI to enhance productivity across all tools. Complete Productivity Ecosystem : Delivered a comprehensive suite including email management, calendar integration, task automation, document handling, analytics, and workflow optimization. Practical Business Solutions : Focused on solving real-world productivity challenges that businesses face daily rather than building theoretical features. What we learned AI Agent Orchestration : Learned how to configure Mastra-powered agents with specialized tools for intelligent workflow automation beyond simple chatbots. Production-Grade Integrations : Discovered the importance of using enterprise APIs like Twilio and SendGrid instead of basic libraries for scalable, professional applications. Real-World Problem Solving : Learned that successful AI applications focus on solving actual business pain points rather than showcasing theoretical capabilities. What's next for The HR Audit Looking ahead, we aim to expand and enhance our AI-powered productivity and financial security platform to serve even more users: Multi-Platform Integration : Extend Cedar-OS capabilities to mobile apps and web dashboards for seamless cross-device productivity management. Advanced AI Models : Integrate cutting-edge language models and computer vision to handle more complex document processing and workflow automation. Enterprise Security : Implement advanced fraud detection algorithms and enhanced encryption protocols to meet enterprise-grade security requirements. Global Accessibility : Add multi-language support and voice recognition for diverse user bases, making productivity tools accessible worldwide. Smart Learning System : Develop machine learning capabilities that adapt to individual user patterns and preferences for personalized productivity optimization. API Ecosystem Expansion : Build integrations with popular business tools like Slack, Microsoft 365, and Salesforce to create a comprehensive productivity hub. <div