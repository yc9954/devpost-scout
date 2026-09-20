---
slug: "runsheet"
url: "https://devpost.com/software/runsheet"
title: "AnalitiQ"
hackathon: "Azure AI Developer Hackathon"
organization: "Microsoft"
winner: true
words: 737
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/housing_homeless"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# AnalitiQ

> Turning feedback into data-driven decisions.

[Devpost](https://devpost.com/software/runsheet) · hackathon [[Azure AI Developer Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[housing_homeless]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** asp.net-core, azure-(functions, azure-ad, azure-blob-storage-**ai-&-analytics**:-azure-cognitive-services-(sentiment-analysis, bi, blob-storage, c#, cognitive-services, openai-gpt-4, power, power-bi, rest, sql, sql-**frontend**:-wpf-(windows-presentation-foundation)-**backend**:-asp.net-core-web-api-**cloud-services**:-azure-(functions

## How they structured the write-up

- 🚀 inspiration
- 🔍 what it does
- 🛠️ how we built it
- ⚡ challenges we ran into
- 🎯 accomplishments that we're proud of
- 📚 what we learned
- 🔮 what's next for analitiq saffron

## Body

data upload analytics page dashboard view admin settings AnalitiQ Saffron 🚀 Inspiration Companies launch products, users leave reviews, and somewhere in between, critical feedback gets buried under a mountain of text . Managers don't have time to sift through endless comments to figure out what's working and what's broken. AnalitiQ Saffron was built to cut through the noise —helping businesses instantly see how their products are being received and whether fixes are actually making a difference. 🔍 What It Does AnalitiQ collects and analyzes product reviews across multiple platforms. Using Azure AI services and Power BI Fabric , it sorts feedback by sentiment, urgency, and recurring themes—so managers can instantly see: ✅ What customers love ⚠️ What needs fixing ASAP 📉 If past issues have been resolved No more manual sorting. No more guesswork. Just clear, actionable insights powered by Azure AI . 🛠️ How We Built It To create a scalable, intelligent, and cloud-powered solution, we built AnalitiQ Saffron using: Frontend: WPF for a sleek and responsive desktop app Backend: ASP.NET Core Web API, hosted on Azure App Services AI Processing: Azure OpenAI with GPT-4 for deep contextual analysis Azure Cognitive Services for sentiment analysis and key phrase extraction Data Storage: Azure SQL Database for structured analytics with tenant isolation Azure Blob Storage for handling large volumes of raw feedback data Visualization: Power BI Fabric with embedded dashboards and row-level security 💡 Context-Enhanced Architecture Our system uses an innovative context-enhanced approach: Event-Driven Processing - Azure Functions triggered by blob storage events Multi-Format Document Processing - Support for PDF, DOCX, TXT, CSV, and XLSX Context Retrieval - Intelligent lookup of similar past feedback Enhanced AI Analysis - Context injection into OpenAI prompts Power BI Fabric Integration - Advanced analytics with row-level security 🤖 How GitHub Copilot Helped GitHub Copilot significantly accelerated our development process: 🔍 Efficient Data Processing Patterns – Suggested optimized approaches for handling large document volumes 🚀 Azure OpenAI Integration – Provided code templates for context-enhanced prompting 📊 Power BI Fabric Implementation – Helped implement row-level security and tenant data isolation 🔄 SQL Query Optimization – Generated efficient database queries for context retrieval Together, Azure and GitHub Copilot allowed us to focus on building a powerful, scalable solution instead of reinventing the wheel. ⚡ Challenges We Ran Into Processing large volumes of reviews in real-time - Solved with event-driven Azure Functions architecture Implementing true context-enhanced AI - Created a custom retrieval system that injects historical context Ensuring multi-tenant data isolation - Implemented row-level security in both Azure SQL and Power BI Creating seamless Power BI Fabric integration - Developed custom embedding with dynamic filtering 🎯 Accomplishments That We're Proud Of ✅ Context-enhanced AI analysis that improves over time as more feedback is processed ✅ Event-driven architecture processing documents immediately upon upload ✅ Multi-format document support handling diverse feedback sources ✅ Power BI Fabric integration with row-level security and dynamic filtering ✅ Advanced visualization dashboards providing immediate, actionable insights 📚 What We Learned 🧠 Context is critical for AI analysis - Traditional sentiment analysis falls short without historical context 🔄 Event-driven architectures enable real-time insights - Serverless functions provide immediate processing 🔐 Multi-tenant security requires layered approaches - Both database and visualization layers need security 📊 Power BI Fabric transforms raw data into stories - Interactive dashboards communicate insights effectively ⚙️ Azure's managed services eliminate operational overhead - Focus on business logic, not infrastructure Our implementation taught us that effective feedback analysis requires not just AI, but AI with proper context. By retrieving and injecting historical feedback patterns, our system delivers significantly more accurate and actionable insights than traditional sentiment analysis alone. 🔮 What's Next for AnalitiQ Saffron To move from our current implementation to an enterprise-ready solution, we plan to add: 🔗 Advanced Context Retrieval – Implementing semantic similarity search with vector embeddings 📩 Automated Insight Delivery – Using Azure Functions to generate and distribute reports based on critical feedback trends 🌎 Multi-Language Support – Expanding our Azure OpenAI implementation to analyze sentiment across multiple languages 🚀 Expanded Data Sources – Adding integrations with social media platforms, support tickets, and internal feedback channels 🤖 Custom AI Fine-Tuning – Creating domain-specific models for specialized industries and use cases 📊 Enhanced Power BI Fabric Dashboard Ecosystem – Building comprehensive analytics suites for different organizational roles AnalitiQ Saffron isn't just about collecting reviews—it's about making customer feedback truly actionable for businesses through context-enhanced AI and powerful visualization. <div