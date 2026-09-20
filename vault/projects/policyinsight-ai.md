---
slug: "policyinsight-ai"
url: "https://devpost.com/software/policyinsight-ai"
title: "PolicyInsight AI"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 816
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/media_journalism"
  - "user/developer"
  - "substrate/document_pdf"
---

# PolicyInsight AI

> PolicyInsight uses AI to analyze insurance policies and instantly highlight exclusions, limits, and key clauses, helping users quickly understand coverage without reading pages of dense legal text.

[Devpost](https://devpost.com/software/policyinsight-ai) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[legal_justice]] [[media_journalism]]
**user** [[developer]]
**substrate** [[document_pdf]]
  <sub>weak: video_visual</sub>

**stack** django, figma, foxitapi, javascript, mysql, next-js, python, react, youapi

## How they structured the write-up

- inspiration
- what it does
- how i built it
- architecture overview
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for policyinsight ai

## Body

flowchart of app login screenshot TEST ACCOUNT CREDS: testuser, testpassword PolicyInsight AI Inspiration Insurance policies are long, dense, and written in complex legal language. Most policyholders do not fully understand exclusions, coverage limits, or conditions until they attempt to file a claim. This lack of transparency creates confusion, financial risk, and poor decision-making. I built PolicyInsight AI to transform static, hard-to-read insurance PDFs into structured, understandable insights. By combining document automation and AI reasoning, I aim to make complex insurance documents accessible and actionable. What it does PolicyInsight AI is a full-stack web application that analyzes insurance policy PDFs and converts them into structured, categorized insights. Users can: Upload an insurance policy PDF from health, life, renters/home to finally auto. Automatically extract document text Identify exclusions, limits, definitions, and conditions View categorized insights in a clean dashboard Generate a structured summary report Instead of manually reading dozens of pages, users receive an organized conclusion/AI analysis . How I built it Product Design (Figma Make) I began the project using Figma Make to prototype the idea before development. I created a clickable prototype with 3–5 connected screens: Landing page Login / onboarding Policy upload screen Analysis dashboard Detailed policy breakdown view Actionable detail page for how to prevent misinformation This helped define a clear user flow: Login → Upload Policy → Analyze → View Structured Insights Figma Make allowed me to validate usability, layout clarity, and information hierarchy before building the full-stack system. Frontend React with Next JS JavaScript Backend Django Django REST Framework Secure REST API endpoints Pythonanywhere to host Django API MySQL for user persistence Foxit API Integration I integrated both required Foxit APIs in a meaningful workflow. PDF Services API Notable user API endpoints: POST /pdf-extract POST /analyze-document not limited to these Purpose: Extract structured text from uploaded insurance policy PDFs Normalize and prepare document content for AI processing This converts unstructured PDF data into machine-readable text. Document Generation API After AI analysis, I generate a structured Policy Insight Report as a new PDF. The report includes: Categorized exclusions Coverage limits summary Definitions Risk-related clauses This creates a complete input → process → output pipeline. You.com API Integration I built a custom AI agent using You.com APIs. Custom agent name: insurance-policy-insight Workflow: Extracted policy text from Foxit is sent to the You.com custom agent The agent analyzes and structures the legal content Structured JSON is returned with categorized insights The agent is designed to reason over legal language and return structured, usable outputs rather than raw text generation. This demonstrates thoughtful and effective use of You.com APIs for intelligent document analysis. This also includes a defined agent used to explain confusing legal language where a user can interact with a chat box and translate a confusing line in the insight or raw policy. Architecture Overview System pipeline: User uploads insurance policy PDF Backend sends file to Foxit PDF Services API Extracted text is processed and normalized Text is sent to the You.com AI custom agent Structured JSON insights are returned Final insights and report are delivered to the user dashboard This architecture connects document automation, AI reasoning, and structured output into a cohesive workflow. Challenges I ran into Handling inconsistent formatting across real-world insurance PDFs Structuring unstructured legal language reliably Coordinating multiple external APIs in a single workflow Kilo Deploy service bug, when trying to deploy after extensive debugging I found that using my WiFi to access my Kilo site was causing a “security risk” and redirecting me to a safe endpoint resulting in my site not loading on my WiFi (workaround was to use phone hotspot) you.com services was blocking my API calls from my Kilo deployed site leading to local analysis hence video explanation Working with real legal documents introduced edge cases that required iterative refinement and structured validation. Accomplishments that I'm proud of Integrating Foxit PDF Services and Document Generation APIs in a complete workflow Building and deploying a You.com custom AI agent Creating an end-to-end document intelligence pipeline Designing a functional prototype in Figma Make and translating it into a working application Delivering a practical AI solution for a real-world problem as a solo developer Using a data server backend via python anywhere to communicate with my react frontend What I learned How to integrate third-party document automation APIs How to design AI agents that return structured, production-ready outputs Managing asynchronous API orchestration across multiple services The importance of UX when simplifying complex legal data Turning AI capabilities into meaningful user value making protection accessible What's next for PolicyInsight AI Add real-time web validation using You.com search capabilities Implement risk scoring for policy sections Support additional policy types (auto, health, home, life) Improve AI structuring accuracy through prompt refinement Deploy scalable cloud infrastructure for production use Refine “Explain this line” feature to allow users to discuss there uploaded policy in a chat session like format with You.com custom agent <div