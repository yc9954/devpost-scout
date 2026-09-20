---
slug: "aws-dzera"
url: "https://devpost.com/software/aws-dzera"
title: "AWS Dzera"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 450
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/geospatial"
---

# AWS Dzera

> Automatically scan your AWS account and discover exactly why your bill is high—with actionable cost-saving recommendations in seconds.

[Devpost](https://devpost.com/software/aws-dzera) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

  <sub>weak: on_device_local</sub>
**domain** [[developer_tools]]
**substrate** [[geospatial]]
  <sub>weak: sensor_telemetry</sub>

**stack** ai, amazon, api, apis, assistance, aws., backend, cloudfront., delivered, frontend, full-stack, gateway, integrated, lambda.

## Body

aws dzera homepage AWS Dezra tab feature1 AWS Dezra tab feature2 Inspiration We built AWS Dzera because cloud cost and operations data is often hard to act on unless you already have deep AWS expertise. Teams can gather metrics and findings, but translating that into clear priorities is still difficult. We wanted to build something that closes that gap and helps people move from data to decisions quickly. -We wanted to make optimization easier for both technical and non-technical users. -We focused on clarity, speed, and practical next steps over raw dashboards. -We wanted AI to guide action, not just generate text. What the project does AWS Dzera helps users connect AWS credentials with read-only access, scan their environment, and get actionable findings with estimated impact. It combines infrastructure scanning, AI explanations, map visualization, and voice summaries so users can understand what to fix first. Scans key cloud services and surfaces cost/risk findings. -Uses AI chat to explain findings in plain language. -Provides visual context through map and relationship views. -Generates audio summaries for quick executive consumption. How we built it: We built Dzera as a full-stack platform with a static frontend and serverless backend on AWS. The frontend is built with Next.js and React and delivered through Amazon S3 and CloudFront. APIs run through API Gateway and Lambda. We integrated Amazon Nova for context-aware AI assistance and Amazon Polly for spoken reports Frontend: Next.js, React, TypeScript. Hosting/Delivery: Amazon S3 + Amazon CloudFront. Backend: AWS Lambda + Amazon API Gateway. AI and voice: Amazon Nova + Amazon Polly. Security: IAM read-only model, request validation, rate limiting, CORS controls. Challenges we faced: The hardest part was making everything reliable across real deployment conditions, not just locally. Caching behavior, CORS/origin alignment, and multi-environment deployment targets created failures that looked like app bugs at first. We also had to strengthen mobile interactions and keep AI behavior consistent under edge cases. -CloudFront cache invalidation and stale bundle debugging. -Origin/CORS configuration across environments. -Mobile event handling and state synchronization. -AI prompt consistency and graceful fallback behavior. -Map rendering reliability and CSS loading edge cases. What we learned: We learned that production AI quality depends on more than just model output. Infrastructure correctness, security, observability, and UX consistency are just as important. We also learned that users trust systems that clearly explain confidence and next actions. What’s next: We plan to expand Dzera with forecasting, anomaly prediction, and stronger governance workflows. We also want to broaden support for multi-cloud environments and continue publishing practical AI integration patterns to help other builders. -Add predictive cost/risk forecasting workflows. -Improve team governance and collaboration features. -Deepen map explainability and relationship intelligence. -Share educational resources for hands-on AI implementation. <div