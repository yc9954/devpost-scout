---
slug: "pipeline-doctor"
url: "https://devpost.com/software/pipeline-doctor"
title: "Pipeline Doctor"
hackathon: "AI in Action"
organization: "Google"
winner: true
words: 498
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
---

# Pipeline Doctor

> Pipeline Doctor auto-diagnoses GitLab CI failures with AI, suggests .gitlab-ci.yml fixes, auto-creates merge requests, finds similar past issues via vector search, and notifies devs instantly.

[Devpost](https://devpost.com/software/pipeline-doctor) · hackathon [[AI in Action]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[clinician]] [[developer]]

**stack** gemini, gitlab, google-cloud, java, mongodb, sendgrid, springboot, vectorsearch

## How they structured the write-up

- 🚀 inspiration
- 🩺 what it does
- 🛠 how i built it
- ⚠️ challenges i faced
- 🏆 accomplishments i'm proud of
- 📚 what i learned
- 🌱 what's next for pipeline doctor

## Body

AI Analysis for Job Failure Similarity Analysis for Past Job Failures Merge request raised for AI-generated suggestions to fix failing job AI-generated changes to .gitlab-ci.yml file MongoDB job_failures collection for similar job failure analysis Project deployment on Google Cloud Platform Pipeline Doctor – Your AI-Powered CI/CD Assistant 🩺🚀 🚀 Inspiration As a software engineer, I frequently run into failed GitLab pipelines , often accompanied by cryptic and overwhelming logs . Pinpointing the root cause feels like searching for a needle in a haystack. Debugging becomes even more time-consuming when I have to rely on SREs for support. I wanted to remove this friction and empower developers like myself to self-diagnose and fix CI/CD issues faster and more confidently . That’s how Pipeline Doctor was born—your friendly AI-powered companion that understands, analyses, and heals your pipelines. 🩺 What It Does Pipeline Doctor is an AI-powered CI/CD assistant that: 🔍 Analyses failing pipeline jobs using Gemini 2.0 Flash 🧠 Performs similarity analysis on past failures using MongoDB Atlas Vector Search 🛠️ Suggests AI-generated fixes to .gitlab-ci.yml (when config-related) 🤖 Auto-creates a merge request with: Root cause summary Past similar job context A fix diff patch for .gitlab-ci.yml 📬 Sends this as a GitLab MR comment , or email (if not MR-linked) 🏷️ Labels AI-created MRs with ai-generated and job ID reference It not only saves developer time but also improves long-term pipeline health and debugging capabilities. 🛠 How I Built It Tech Stack : Java 17 + Spring Boot AI Analysis : Used Gemini 2.0 Flash to summarize pipeline failures Generated embeddings for log data Vector Search : Embedded historical job logs in MongoDB Queried for top 3 similar failures using MongoDB Atlas Vector Search Automation : Used GitLab REST APIs to post comments and auto-raise MRs Deployment : Hosted on Google Cloud Run Managed secrets via Google Secret Manager ⚠️ Challenges I Faced First time working with MongoDB Atlas Vector Search —took time to learn the query structure Choosing the best secret management tool took careful evaluation Debugged a major MongoDB authentication error before the demo deadline 🏆 Accomplishments I'm Proud Of 🎯 First solo project combining AI + Vector DB + CI/CD + Cloud 🔧 Created an end-to-end tool that is immediately usable in real developer workflows 🧠 Took a personal pain point and solved it using modern AI tooling 🚀 Got hands-on experience with full-stack DevOps & ML engineering 📚 What I Learned 🧾 Prompt engineering for Gemini 2.0 🔍 Vector similarity search with MongoDB Atlas 🛠️ GitLab APIs for CI/CD automation ☁️ Google Cloud Run and Secret Manager for production deployment 🌱 What's Next for Pipeline Doctor ☁️ Build a cloud-hosted version to increase adoption, as the current version is self-hosted, and the developers need to use their infrastructure to use the application as a CI/CD component 🔘 Add user toggle controls for auto-analysis and auto-fix generation 🔄 Extend support to other CI/CD platforms 🧠 Use RAG (Retrieval-Augmented Generation) to make AI fixes even smarter <div