---
slug: "aegis-0qmide"
url: "https://devpost.com/software/aegis-0qmide"
title: "AEGIS"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 460
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# AEGIS

> Automated security scanning and instant remediation for your AWS infrastructure.

[Devpost](https://devpost.com/software/aegis-0qmide) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[structured_db]] [[video_visual]]

**stack** amazon-dynamodb, amazon-nova, express.js, framer-motion, jwt-(json-web-tokens), node.js, radix-ui, react, react-(v18), tailwind-css, vite

## How they structured the write-up

- about the project

## Body

About the project Cloud security posture management is often overwhelming, bombarding teams with an endless list of complex security errors. AEGIS (Advanced Cloud Security) was inspired by the need for an automated, intelligent guardian that doesn't just flag misconfigurations but actually fixes them. We wanted to build a platform that acts as a continuous compliance expert—capable of deep reasoning over cloud environments and providing instant, actionable, one-click remediation plans. How it was built AEGIS is built on a modern, scalable, AI-first monorepo architecture consisting of three core interconnected layers: The AI Reasoning Engine: At the heart of AEGIS is Amazon Bedrock , utilizing the Amazon Nova model. We built custom intelligent compliance agents ( compliance-reasoner , ec2-compliance-reasoner ) that ingest configuration metadata from the AWS SDK. Instead of static rule-checking, the LLM synthesizes this data against SOC2 standards and best practices to generate human-readable alerts and precise shell/API commands for remediation. The Backend Orchestration: Built with Node.js and Express , the backend engine manages continuous scanning pipelines, communicates seamlessly with the AWS environment, and handles dynamic region discovery. Structural scan results, AI analysis, and remediation plans are durably stored in Amazon DynamoDB . The Premium Frontend: The dashboard is a highly responsive single-page application built using React v18 and Vite . We focused heavily on the UX/UI, implementing a premium, accessible glassmorphism aesthetic using Tailwind CSS , Radix UI , and Framer Motion for micro-animations and full-page scroll-snapping designs. ### What I learned Building AEGIS was a massive learning experience in applied AI and cloud architecture. Key takeaways included: Applied LLM Reasoning: Learning how to effectively prompt and constrain Large Language Models (Amazon Nova) to perform complex logic over structural cloud configurations rather than just conversational text. Advanced AWS Integrations: Deepening my understanding of IAM structures, cross-region resource discovery, and the programmatic manipulation of S3 and EC2 configurations using the AWS SDK. Performance Optimization: Learning how to optimize data flow in a full-stack application, including migrating image storage solutions for speed and ensuring fast frontend rendering with complex data visualizations. ### Challenges faced Integrating an LLM with live cloud infrastructure presented several unique challenges: Safe Automated Remediation: Ensuring that the AI-generated remediation commands were strictly safe to execute via a "one-click" mechanism without inadvertently breaking existing infrastructure. Complex State Synchronization: Debugging the remediation flow to ensure the frontend accurately reflected backend and database state changes, specifically resolving persistent asynchronous synchronization issues during S3 bucket remediations. **Dynamic Region Management: * Overcoming the complexity of automating resource discovery across all active AWS regions seamlessly, removing the need for manual region configuration by the user while maintaining high scanning performance. Knowledge Base Ingestion: Fine-tuning the data pipeline to reliably parse and ingest various complex file formats into the AI agent's knowledge constraints. <div