---
slug: "advision-2b04ns"
url: "https://devpost.com/software/advision-2b04ns"
title: "AdVision"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 828
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/retail_commerce"
  - "domain/security_privacy"
  - "user/small_business"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# AdVision

> From AI-generated ads to performance insights and side-by-side comparisons—see what works, scale what wins.

[Devpost](https://devpost.com/software/advision-2b04ns) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[measured_ablation]] [[realtime_stream]] [[vision_ocr]]
**domain** [[retail_commerce]] [[security_privacy]]
**user** [[small_business]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** axios, cloudinary, deepseek, django, git, github, javascript, npm, numpy, pandas, pip, pollinationai, postgresql, reactt

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for advision

## Body

AdVision Inspiration We noticed that small businesses and marketers spend countless hours creating advertisements, testing different versions, and analyzing performance metrics. The advertising landscape has become increasingly complex with multiple platforms, audience segments, and creative variations to manage. We were inspired to build AdVision after realizing that AI could not only automate these tedious tasks but actually make better data-driven decisions than manual processes. Our goal was to democratize enterprise-level advertising capabilities for everyone. What it does AdVision is an AI-powered advertisement management platform that revolutionizes how businesses create and optimize their ad campaigns. The platform combines three core capabilities: Intelligent Ad Generation : Using DeepSeek V3.1 and Stability AI, AdVision generates compelling ad copy and stunning visuals tailored to your brand and target audience Automated A/B Testing : The system automatically creates multiple ad variations, tests them across your audience, and identifies the best-performing combinations Real-time Analytics & Optimization : Advanced ML models continuously analyze campaign performance, predict trends, and automatically adjust bidding strategies and targeting parameters Users simply input their campaign objectives, target audience, and budget—AdVision handles everything from creative generation to performance optimization. How we built it We architected AdVision as a full-stack application with a React frontend and Django backend. The technology stack includes: Frontend : React.js for the user interface, providing an intuitive dashboard for campaign management and real-time analytics visualization Backend : Django REST Framework for building robust APIs, handling business logic, authentication, and AI model orchestration AI Models : DeepSeek V3.1 for natural language generation and ad copy creation Stability AI for generating high-quality advertising visuals Custom ML models for predictive analytics and performance optimization Data Pipeline : Real-time data processing for campaign metrics, audience insights, and performance tracking Database : Django ORM with PostgreSQL/SQLite for structured storage of campaign data, user profiles, and analytics We leveraged Django's powerful features including its ORM for database management, built-in authentication system, and middleware for request processing. The frontend communicates with the backend through RESTful APIs, and we implemented robust error handling and data validation throughout the system. Challenges we ran into The biggest challenge was balancing AI creativity with brand consistency. Early versions generated ads that were creative but didn't always align with brand guidelines. We solved this by implementing a sophisticated prompt engineering system that incorporates brand voice, tone, and visual style guidelines into the AI generation process. Another significant hurdle was optimizing the real-time analytics pipeline. Processing thousands of data points per second while maintaining low latency required us to implement efficient caching strategies using Django's cache framework and batch processing mechanisms. We also faced challenges with API rate limiting when integrating multiple AI services. We built a smart queuing system using Django's asynchronous task capabilities that prioritizes high-impact requests and implements exponential backoff for retries. Accomplishments that we're proud of Successfully integrated three different AI models (DeepSeek V3.1, Stability AI, and custom ML) into a cohesive Django-powered platform Built an intuitive interface that makes enterprise-grade advertising tools accessible to non-technical users Achieved sub-second response times for ad generation despite complex AI processing Leveraged Django's security features to build a secure, production-ready application Created a fully functional MVP with real-time analytics and automated optimization capabilities Designed a scalable architecture using Django's MVT pattern that can handle multiple concurrent campaigns What we learned This project taught us invaluable lessons about AI orchestration and production-ready ML systems. We learned that effective AI applications require more than just calling APIs—they need thoughtful prompt engineering, robust error handling, and intelligent fallback mechanisms. We gained deep appreciation for Django's "batteries-included" philosophy, which accelerated our development by providing built-in solutions for authentication, database management, and API creation. The framework's emphasis on security by default helped us avoid common vulnerabilities. We gained deep insights into the advertising industry's challenges and how AI can genuinely solve real business problems rather than just being a flashy feature. The importance of user experience became crystal clear; no matter how powerful the AI, if users can't easily access and understand the insights, the tool fails. We also discovered the critical importance of data quality and validation when building AI-powered analytics. Django's form validation and serializer classes were instrumental in ensuring clean data throughout our pipeline. What's next for AdVision Our roadmap includes several exciting enhancements: Multi-platform Support : Expanding beyond web to support Facebook Ads, Google Ads, Instagram, and TikTok advertising platforms Advanced Personalization : Implementing hyper-personalized ad generation based on individual user behavior and preferences Collaborative Features : Adding team collaboration tools for agencies managing multiple client campaigns Performance Prediction : Developing predictive models that forecast campaign performance before launch Budget Optimization : AI-powered budget allocation across campaigns and platforms to maximize ROI Integration Marketplace : Building an ecosystem of third-party integrations for CRM, e-commerce, and analytics platforms Celery Integration : Implementing Celery for handling long-running AI generation tasks asynchronously We're also exploring the possibility of implementing voice-activated campaign management and a mobile app for on-the-go campaign monitoring and adjustments. <div