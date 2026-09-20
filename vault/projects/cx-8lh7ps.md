---
slug: "cx-8lh7ps"
url: "https://devpost.com/software/cx-8lh7ps"
title: "Heuristic AI"
hackathon: "TiDB Future App Hackathon 2023"
organization: "PingCAP"
winner: true
words: 552
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Heuristic AI

> Heuristic AI is a search management system that creates search pages for products. The tool allows companies to have fast and efficient direct insights into their consumer's issues thanks to TiFlash.

[Devpost](https://devpost.com/software/cx-8lh7ps) · hackathon [[TiDB Future App Hackathon 2023]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**user** [[general_public]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** cohere, flask, nextjs, openai, tailwindcss, tidb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- how it works
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for heuristic ai

## Body

Logo Architecture Inspiration People have problems with their machines. Sometimes, they get errors or failure codes in the equipment and have no clue how to interpret the issue. So user calls directly the customer service which is most of the time full, and there is no way to allow consumers to interpret the error code or ask any supplement questions regarding the product. What it does We have developed the platform to allow manufacturers to index the manuals for all their products and have a search bar for every product. And it gives direct insight correlated to their internal task list and readjusts automatically when a user asks a question. How we built it The tech stack is used from the online database TiDB. The tables are: Users: to store user information Analytics: to store analytics like user's questions, datetime Products: to store products information Document: to store documents related to a product Sessions: to store the authentications sessions Tasks: to store internal tasks of the company IP: to track the number of visitors on the product search page for the dashboard For the backend, we used Flask to handle the user queries. The Backend is hosted on AWS EC2 and the IP user query are forwarded via Ngrok for the security purpose. TiDB to handle the handle users, and company information in Real-time, and the monitoring of the task using HTAP operations for retrieving the task by desc order from a REPLICATED table. The documents are indexed into Qdrant to allow the semantic search. OpenAI to ensure the generative Context-based QA to the consumer. We control the output of the Generative model via a prompt, to not invent the answer if there is no answer in a given context. Cohere to vectorize the user queries and the documents(whatever the language of the text). And lastly, a cross-encoder to ensure the readjustment of the user query to the internal company task. For the frontend, we used Next.js and Tailwindcss for the styling. How it works Our use case <company> is samsung . Role : company & Action : Create a product (product name) via /<company>/products/ Role : company & Action : Index the document of the product (select the manual from the storage: the Samsung instruction manual ) via /<company>/indexing/ Role : company & Action : Stick the QR code to the equipment. Role : user & Action : Ask questions and get answers via /<company>/<product-id>/search/ Role : company & Action : Check user questions via /<company>/questions/ Role : company & Action : Monitor the internal company task via /<company>/analytics/ Challenges we ran into The challenge we ran into was about handling the Replicate into our SQUAD dataset (extracted only questions, which represent the internal company task) Accomplishments that we're proud of We are proud to successfully use Replicate our Tasks table with 13127 rows and apply analytical processing via TiFlash. What we learned We learned that it was possible to handle analytical processing while querying the DB via TiFlash. What's next for Heuristic AI The next step of Heuristic AI is to Improve UX by integrating feedback Integrate clients authentication Map multiple user manuals to improve their integration in the index Test use cases. And design integration to the most popular CRM in order to open tickets directly from Heuristics. <div