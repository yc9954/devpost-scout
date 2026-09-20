---
slug: "wordpress-static-site-guardian"
url: "https://devpost.com/software/wordpress-static-site-guardian"
title: "WordPress Static Site Guardian"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 762
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/runtime_tool_creation"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# WordPress Static Site Guardian

> Secure your static WordPress sites with enterprise-grade CloudFront signed cookies, seamless Cognito authentication, and zero-downtime protection - all deployed with a single command.

[Devpost](https://devpost.com/software/wordpress-static-site-guardian) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[runtime_tool_creation]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[web_dom]]

**stack** api-gateway, cloudformation, cloudfront, gatey, javascript, kms, lambda, python, s3, ssm, yaml

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i’m proud of
- what i learned
- what’s next

## Body

Public homepage of the demo site - freely available content, with protected routes clearly indicated. Sign-in page rendered by Gatey, offering multiple identity providers (Google, Facebook, Auth0) alongside Cognito username/password login. Protected blog page - only accessible after signing in with Cognito through Gatey and receiving a valid CloudFront signed cookie. Project workspace with Kiro-generated specifications, design documents, and production-readiness tasks. Successful one-click deployment of WordPress Static Site Guardian stack via AWS CloudFormation from the Serverless Application Repository. Diagram of the WordPress Static Site Guardian architecture, showing S3, CloudFront, API Gateway, Lambda, and supporting AWS services. Inspiration Many WordPress site owners want the speed and security benefits of serving their sites statically from S3/CloudFront. The challenge comes when some parts of the site — such as member areas or premium downloads — need to be restricted to signed-in users. Traditional WordPress authentication no longer applies once the site is exported as static files. I wanted to provide an AWS-native solution that gives developers both: the performance of a static site, and the ability to protect selected paths with proper authentication. What it does The application deploys an AWS stack that: Hosts a static WordPress-generated site in S3 behind CloudFront Protects configurable URL paths with CloudFront signed cookies Exposes an API endpoint that issues or clears those cookies with proper CORS support Stores and encrypts signing keys with KMS and SSM Creates self-referencing CloudFront behaviors for protected content routing Integrates smoothly with the Gatey plugin, which handles the Cognito login UI inside WordPress and calls the cookie-issuance API after sign-in and sign-out The result is that a visitor logs in through Cognito (via Gatey), receives the correct CloudFront cookie, and can then access the protected content transparently through dynamically created cache behaviors. How I built it The project began with a simple initial prompt for Kiro : generate a CloudFormation stack that can protect static WordPress exports with CloudFront signed cookies and an API Gateway + Lambda for cookie issuance. Based on this idea, the first working version of the stack was created. Later, I used Kiro 's specification capabilities to generate structured documents — requirements, design, and tasks. These gave the project a more formal architecture and a clear implementation plan. From there, the remaining development (response cache policies, comprehensive end-to-end tests) followed this structure. Architecture : S3 + CloudFront for hosting, signed cookies for protection, API Gateway + Lambda for cookie issuance, Cognito/Gatey for login. Infrastructure as Code : CloudFormation templates extended with custom Lambda resources to handle CloudFront components not natively supported in SAR (PublicKeys, KeyGroups, OAC). Serverless functions : Lambda for cookie signing (with KMS and SSM), CloudFront Functions for authentication and path rewriting. Testing : End-to-end flows, validation of stack creation and deletion, and security tests for cookie tampering and expiration. Challenges I ran into SAR limitations : Several CloudFront resources (KeyGroup, PublicKey, OAC) aren’t supported, so I had to implement custom Lambda-backed resources with proper lifecycle handling. Cookie expiration : Aligning cookie lifetime with Cognito refresh token validity to ensure consistent session behavior. Domain scoping : Cookies must cover both the main site and the API subdomain to work correctly. Accomplishments that I’m proud of A working end-to-end stack that any AWS account owner can deploy with one click from the Serverless Application Repository. A clear path for WordPress site owners: export their static site, deploy this stack, and use Gatey to connect Cognito sign-in to the cookie API. Making something simple to explain but powerful enough for real production use cases like course platforms or member-only areas. What I learned How to handle unsupported CloudFormation resources in SAR by building custom Lambda-backed resources with robust error handling and retry logic. Practical aspects of CloudFront signed cookies: key management, domain scoping, expiration alignment. The value of starting from a rough prompt, then switching to a structured design (with Kiro’s help) for finishing production-grade features. What’s next Add a form plugin for static sites : submissions would go directly to protected APIs using Gatey’s Amplify Auth helpers, instead of relying on WordPress backends. Enhanced monitoring : CloudWatch dashboards and alarms for API performance, CloudFront cache hit rates, and authentication success metrics. Multi-environment support : staging/production deployments with environment-specific parameters. Provide analytics and monitoring so site owners can better understand how protected content is accessed. Explore multi-region deployment for higher availability. Develop automated integration tests for the complete authentication and access flow. The latest version is production-ready and resilient to the real-world challenges of CloudFront-based authentication at scale, while still being approachable enough for WordPress developers to use. <div