---
slug: "equilex"
url: "https://devpost.com/software/equilex"
title: "EquiLex"
hackathon: "Tableau DataDev 2024-2025 Hackathon "
organization: "Tableau"
winner: true
words: 479
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
---

# EquiLex

> Empowering communities with data-driven contract clarity.

[Devpost](https://devpost.com/software/equilex) · hackathon [[Tableau DataDev 2024-2025 Hackathon]]

## Facets

  <sub>weak: retrieval_grounding</sub>
**domain** [[finance_payments]] [[legal_justice]]
**substrate** [[document_pdf]] [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** html, javascript, llm, python, rag

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for equilex

## Body

Inspiration The project grew out of witnessing how communities—especially those impacted by events like the LA bushfires—struggle to interpret legal and insurance documents. We saw first-hand the financial and emotional toll that unclear or misunderstood contracts could create. This inspired us to build an accessible solution that demystifies complex legal language, ensuring people are better protected and informed. What it does Importing & Synchronizing Contracts: Securely fetches and updates documents from Docusign or direct uploads. Intelligent Summaries & Q&A: Uses an LLM to provide layman-friendly summaries, highlight critical clauses, and answer questions. Analytics & Visualization: Transfers key data (like coverage details, expiry dates, and risk scores) to Tableau for user-friendly dashboards, enabling trend analysis and clearer decision-making. How we built it Streamlit Frontend : We used Streamlit to create a friendly web interface, allowing users to securely log in, upload contracts, or connect to Docusign accounts. LLM Processing Layer : We leveraged a Large Language Model (GPT-based) to summarize, extract key clauses, and answer questions about uploaded documents. Docusign Integration : The system securely fetches contract drafts and signed versions from Docusign, ensuring our LLM works off the most up-to-date data. Data Analytics in Tableau : After processing, structured contract info (e.g., coverage levels, expiration dates, risk metrics) is passed to Tableau for dynamic dashboards. We focused on visualizations that highlight coverage trends, important clause comparisons, and potential risk areas. Challenges we ran into Handling Legal Text Complexity : Legal documents often contain nuances, references, and specialized terms. We had to carefully manage LLM prompts to maintain accuracy. APIs & Permissions : Coordinating multiple APIs (Streamlit, Docusign, Tableau) introduced complexity in authentication, data flow, and version control of documents. Accomplishments that we're proud of Empowering Non-Legal Users We’ve made it easier for individuals with little to no legal background to parse and understand complex contract clauses. End-to-End Integration Combining Docusign, an LLM, and Tableau within a single Streamlit platform was a major milestone—allowing seamless contract updates, processing, and data visualization. What we learned Community Needs : We discovered that many individuals are not just interested in summaries; they want practical insights (e.g., risk exposure, important timelines, or critical clauses). Tech Integration : Integrating Tableau dashboards with a Large Language Model (LLM) and Docusign significantly enhances the user experience, but it also requires careful consideration of API structures and data flow. Value of Simplicity : Streamlit provided a simple yet powerful frontend that makes it easier for non-technical users to navigate and explore contract data. What's next for EquiLex Fine-tuning : We plan to fine-tune the LLM with more legal domain-specific data to improve clause extraction accuracy. Advanced Analytics : Our goal is to incorporate deeper risk scoring models, giving users a numerical sense of potential coverage gaps. Community Rollout : We’re exploring partnerships with local nonprofits and legal aid organizations to conduct pilot programs and gather user feedback. <div