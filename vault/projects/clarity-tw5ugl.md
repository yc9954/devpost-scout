---
slug: "clarity-tw5ugl"
url: "https://devpost.com/software/clarity-tw5ugl"
title: "Clarity"
hackathon: "RAG 'n' ROLL Amp up Search with Snowflake & Mistral"
organization: "Snowflake"
winner: true
words: 496
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/supply_logistics"
  - "user/researcher"
---

# Clarity

> AI Powered Clarity turns customer tickets into clear insights. With smart tagging, sentiment analysis, and quick solutions, it helps SaaS teams solve faster, understand better, and build smarter.

[Devpost](https://devpost.com/software/clarity-tw5ugl) · hackathon [[RAG -n- ROLL Amp up Search with Snowflake - Mistral]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[supply_logistics]]
**user** [[researcher]]

**stack** mistral, python, snowflake, streamlit

## How they structured the write-up

- inspiration
- 💡 what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for clarity

## Body

Inspiration The idea for Clarity was born from the need to simplify how SaaS product teams analyze customer feedback and support tickets. We noticed that product builders often struggle with sifting through large volumes of feedback to uncover actionable insights. The customer facing team also struggles to reduce the resolution time and be proactive to improve customer satisfaction. This inspired us to create a tool that could streamline this process, saving time and enhancing decision-making. 💡 What It Does Clarity is an AI-powered tool designed to help SaaS teams: Summarize Customer Tickets : Generate concise summaries of support tickets for quicker understanding. Tag Issues Automatically : Classify tickets by issue type, module, and category to improve organization and prioritization. Analyze Sentiments : Detect customer emotions from ticket description to gauge overall satisfaction or frustration. Show Related Tickets : Provide suggestions for similar tickets and fetch answers from their solutions to reduce response time. Customer Insights Dashboard : Offer a comprehensive summary of a customer’s recent feedback, sentiment trends, and actionable recommendations. Feature & Issues Based Analysis : Easily get an overall perspective of customer issues based on individual features, Modules and categories. By providing these features, Clarity empowers teams to understand customer needs faster and make data-driven decisions. How we built it We combined several technologies and methodologies to bring Clarity to life: Snowflake : Used as our data warehouse to store and process large volumes of customer feedback and support ticket data. Snowflake Cortex Search : Powered our RAG (Retrieval-Augmented Generation) capabilities for efficient search and summarization. Snowflake Cortex Analyst : Enabled advanced query-based search functionality to dig deeper into data insights. Mistral Large 2 LLM : Leveraged this cutting-edge Gen AI model for generating summaries and extracting actionable insights. Streamlit : Built an intuitive and interactive frontend for visualizing customer feedback and sentiment trends in real time. Challenges we ran into Data Complexity : Normalizing ticket data and extracting meaningful insights while handling varied formats. AI Summarization : Adjusting the prompts to AI models to generate accurate and contextually relevant summaries. Time Constraints : Balancing scope and quality within the limited timeframe of the hackathon. User-Centric Design : Ensuring the tool remained intuitive and useful for diverse SaaS product teams. Accomplishments that we're proud of We’re especially proud of the following accomplishments in Clarity : The ability to group tickets under different tags , making it easier to organize and prioritize feedback. Optimizing the search using advanced methods to ensure users find the most relevant tickets and information quickly. Using insights from similar tickets to provide potential answers, reducing solution time and enhancing efficiency. These features make Clarity a powerful and practical tool. What's next for Clarity We're excited about the potential of Clarity ! Future plans include: Enhancing AI models for deeper insights. Integrating with other feedback channels and tools like Jira, Zendesk, Hotjar, GA to maximize insights quality. Expanding features, such as automated roadmap suggestions based on customer feedback trends. etc. <div