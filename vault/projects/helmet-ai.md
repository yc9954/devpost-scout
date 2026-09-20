---
slug: "helmet-ai"
url: "https://devpost.com/software/helmet-ai"
title: "Helmet.ai"
hackathon: "UC Berkeley AI Hackathon"
organization: "Cal Hacks"
winner: true
words: 411
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/retrieval_grounding"
  - "domain/scientific_research"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Helmet.ai

> Keep a-head of the news and protect your competitive edge

[Devpost](https://devpost.com/software/helmet-ai) · hackathon [[UC Berkeley AI Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[retrieval_grounding]]
**domain** [[scientific_research]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** azure, github, gpt3.5, gpt4, graphql, langchain, llamaindex, mindsdb, openai, python, rss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for helmet.ai

## Body

Inspiration In today’s world, things change fast - too fast. High-ranking business executives are expected to make hugely impactful decisions based on the best information available - but what if that information never stops changing? With the pace of tech innovation enabling new competitors to launch every single day, CEOs of companies big and small alike are forced to waste precious time looking over their shoulders instead of focusing on the road ahead. These leaders’ divided attention makes it even more difficult for them to uncover the truly insightful ideas that can radically improve corporate strategy and deliver outsize returns. What it does Helmet is the always-on market intelligence tool that’s truly smart, enabling leadership teams to stay a- head of the news and their competitors. Helmet’s context-aware Ingestion Engine continuously monitors the wide world of breaking news to build a complete understanding of global events. Helmet's Insight Extractor leverages the power of OpenAI’s GPT models to discover and concisely explain the hidden relationships between seemingly disparate topics. Together, these tools equip the world’s best leaders to confidently tackle the challenges of today and seize the opportunities of tomorrow. How we built it Azure to the max (App Services, PostgreSQL Databases, Static Web Apps, Virtual Machines, Storage accounts, Virtual Networks, Bastion, …) MindsDB LlamaIndex + LangChain for document processing AutoGPT-like chain of thought and introspection GraphQL RSS feeds GitHub Action pipelines for one-click deploy OpenAI (have you heard of them before?) Challenges we ran into MindsDB Gmail authentication being limited to AWS S3 (we are #azure4life) The perils of mono-repo, mono- branch development Replacing JavaScript with TypeScript. New look, same terrible taste iPhone GitHub Actions Storage Full Accomplishments that we're proud of It works! Went from cutting-edge LLM prompting research papers to self-evaluating explanatory AI implementation in 24 hours. We set up a proper deployment using GitHub Actions to automate lots of annoying manual service orchestration. Great experience for the first-time hackers on the team! What we learned Getting your deployment flows set up early saves a lot of stress in crunch time. They call them ‘best practices’ for a reason. Software engineering jobs probably aren’t going to be replaced by AI anytime soon. LLMs can be surprisingly good when used as implicit knowledge graphs instead of just sources for embeddings. What's next for Helmet.ai Productionize and scale up the Ingestion Engine to handle the full web (AnyScale? 👀) Round up some enterprise bizdev teams for a pilot ??? Profit <div