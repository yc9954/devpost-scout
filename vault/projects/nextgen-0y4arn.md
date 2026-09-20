---
slug: "nextgen-0y4arn"
url: "https://devpost.com/software/nextgen-0y4arn"
title: "Chiral AI - Chat with PRDs and Create Tickets in Record Time"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 810
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Chiral AI - Chat with PRDs and Create Tickets in Record Time

> We help product managers write better tickets and multiply their developers' productivity by providing chat-with-PRD and AI-based ticket generation features. Go from idea to tickets in under 5 mins!

[Devpost](https://devpost.com/software/nextgen-0y4arn) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** amazon-web-services, astradb, axios, cassandra, datastax, docker, drizzle-orm, embeddings, langchain, linear-sdk, lucia-auth, neon-db, nextjs, openai

## Body

Dashboard Chat with Linear Document Generate Issues from Document List of AI-generated issues based on Document content The Product Manager's Dilemma Product Managers have too much on their plate already. From user meetings, stakeholder management, to ticket drafting, all of these activities stretch out the PM's time and focus. This is due to the nature of the work, where PM resides in the middle of the action, acting as glue between teams and teammates, between junior engineers up to the senior management. As a PM, you are expected to be the go-to guy who can do it all. On the other hand, you are also expected to perform at your best, in terms of analytical skills, communication, strategic thinking, and much more. This is the Product Manager's dilemma , where you have to balance the two conflicting sides of your work. Ok Fair. But how does this phenomenon impact developers? In a typical large-size tech company, usually a PM collaborates with a team of engineers and helps them define business objectives, project scope and timelines, crisis management, etc. PMs are also the actor who is responsible for creating feature tickets to break down the project into smaller parts. Usually, the tickets are written in tools such as Jira (yikes!) or Linear (if you're cool. Here, tickets are also called issues ). It is no wonder, then, that some engineers complain of badly written tickets by their PM. Whether it's because they were writing it in a hurry, a lack of business understanding, or even plain old grammatical mistakes. These errors can significantly impact developer experience , because engineers have to go back and forth with the PM to clarify missing/unclear parts of the requirements. We've seen this firsthand, as some of us and our peers have working experience as professional software developers. There are also cases where the document itself has some parts that are vague or incomplete. This can cause more friction not just as a developer trying to understand the requirements, but also for the PMs who are trying to communicate their intentions through this document. With Chiral AI, we enable developer productivity by eradicating badly written tickets from PMs. We also improve overall team productivity and product understanding by helping PMs complete and improve the quality of their documents Chiral AI: Our solution to the Dilemma Drawing from our own experiences as developers and the seemingly frequent cases of "my PM's tickets are so confusing", we decided to build our own solution. Chiral is an AI-powered product management workflow accelerator, where we help product managers to get from problem statement to Linear.app Issues (tickets) in record time. It has two main features: first, you can chat directly with your PRDs from Linear.app, second, you can ask Chiral to generate ticket suggestions by understanding context from your document. You can chat with your PRDs to improve your understanding of the business context, and then creating a list of recommended issues from the document. You can even use the chat feature to not only get an understanding of the document, but also to ask suggestions, corrections, and other questions where the answers can be used as feedback to improve the quality of the documents. This way, you can go from a problem statement to Linear.app Issues in under a minute while also having the benefit of improving and expanding your documents with minimal time. You are free to iterate further by chatting with the Linear Document on our app, until all Issues are clear as crystal. With Chiral AI, bad tickets are as good as history. How we built Chiral Chiral was built using a full-stack development process to enable fast iteration. We used Next.JS 13 for the frontend with tRPC for the backend. For the database we used NeonDB (PostgreSQL) for application data and DATASTAX AstraDB (Cassandra) to store embeddings of the product documents as well as its vector search capability for question-answering the documents and ticket generation. To interact with the Postgres database, we used DrizzleORM, an ORM with near-SQL like semantics and high performance. The application is containerized using Docker technology and deployed on an AWS EC2 Virtual Machine. We also used various AI tools in our stack. For the model and embeddings we used OpenAI's GPT-3.5-16k and transformer embeddings, specifically the bge-large-en-v1.5 model. We also used Vercel’s AI SDK to help us build the chat feature. To make our AI model able to understand documents and create ticket recommendations, we implemented RAG (Retrieval Augmented Generation) to fetch relevant context from a document with the help from LangChain. Future development As of right now, we only support Linear workspaces. However, we plan to add support for other knowledge management systems and PM tools such as Jira, Asana, Clickup, etc. to provide our services for more teams out there looking to accelerate their workflow and productivity. <div