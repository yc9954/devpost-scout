---
slug: "connie-ai"
url: "https://devpost.com/software/connie-ai"
title: "Connie AI"
hackathon: "Codegeist Unleashed"
organization: "Atlassian"
winner: true
words: 473
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/labor_employment"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Connie AI

> Connie AI is an AI assistant for Confluence. We launched Connie AI in the marketplace in June. For Codegeist, we implemented two game-changing new features: - Natural language table querying - X-ray

[Devpost](https://devpost.com/software/connie-ai) · hackathon [[Codegeist Unleashed]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[labor_employment]]
**substrate** [[structured_db]] [[web_dom]]

**stack** amazon-web-services, dynamodb, elasticsearch, javascript, lambda, node.js, openai, redis, s3, typescript

## How they structured the write-up

- building natural language table querying
- adding x-ray explainability
- overcoming challenges with forge
- what's next for connie ai
- read more

## Body

Connie AI logo Table question answering X-ray The Story Behind Connie AI - An AI Assistant for Confluence As former Atlassian employees, we experienced firsthand how challenging it can be to navigate all the information in Confluence. My co-founder and I envisioned an AI assistant that could understand natural language questions about Confluence content and provide direct answers by querying tables and databases. This inspiration led us to create Connie AI, an AI assistant designed specifically for Confluence. We first launched Connie on the Atlassian Marketplace in June 2023. For Atlassian's 2023 CodeGeist hackathon, our team at Applied Language Understanding (ALU) implemented two major new features: natural language table querying and X-ray explainability . Building Natural Language Table Querying Enabling Connie to understand and query tables required a complex AI pipeline. Connie automatically indexes new and updated Confluence pages, decomposing them into semantic chunks. Chunks containing structured data like tables are flagged. When a user asks a natural language question, Connie retrieves the most relevant chunks. If any chunks have structured data, Connie uses GPT-3.5 to convert the question into a custom pseudo-SQL query language. This allows Connie to perform powerful operations like unit conversions and date reformatting on the fly. We built a custom engine to execute these AI-generated queries while generating explanations of the operations performed. The output is passed to GPT-3.5 to generate a final human-readable answer. Streaming responses directly to the client reduces perceived latency. Adding X-ray Explainability We realized trust would be a challenge - users needed more than just a magical answer from an AI assistant. Our solution was X-ray, a feature that shows the user every retrieved fact, reasoning step, and operation behind each answer. This helps build user trust and aids in detecting any potential errors. X-ray is an innovative capability - Connie is the only system we know of that provides this level of transparency into an AI's process. Overcoming Challenges with Forge Building Connie's complex pipeline required moving beyond Forge's robust default security. We implemented cryptographic signing for all communications and enforced user access rights at runtime. We added easy opt-outs for any potentially shared data. Forge's spacePage, macro, and customUI modules allowed Connie to integrate naturally into Confluence. We were even able to add support for dark-mode in just a day. What's Next for Connie AI Looking ahead, our priorities are bringing Connie's table analysis to Confluence databases, expanding the capabilities of the query language, and improving latency and reliability by bringing inference in-house. The Connie AI project shows how AI can thoughtfully augment human intelligence. We overcame key challenges to build an assistant that provides powerful capabilities and unprecedented transparency. Connie AI represents the exciting future potential of AI to aid knowledge workers. Read more You can see the slide deck for our submission in our blog. Connie AI website <div