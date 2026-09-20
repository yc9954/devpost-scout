---
slug: "intelligent-helper-ai-suggest-for-jsm-support-agents"
url: "https://devpost.com/software/intelligent-helper-ai-suggest-for-jsm-support-agents"
title: "Intelligent Helper - AI Suggest for JSM Support Agents"
hackathon: "Codegeist Unleashed"
organization: "Atlassian"
winner: true
words: 906
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/structured_db"
---

# Intelligent Helper - AI Suggest for JSM Support Agents

> Give your support team a power boost with automated ticket insights and AI-generated responses - built directly into your JSM portal.

[Devpost](https://devpost.com/software/intelligent-helper-ai-suggest-for-jsm-support-agents) · hackathon [[Codegeist Unleashed]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**substrate** [[structured_db]]

**stack** chromadb, forge, javascript, langchain, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for intelligent helper - ai suggest for jsm support agents

## Body

Intelligent Helper app automatically displays related issues and allows user to generate a response Inspiration The best product ideas often come from what customers are saying. You can learn so much about the customers & the product through support tickets, especially if you’re new to the organization. Here's the hitch. Support agents are often swamped with new tickets, and there’s no quick way to find information relevant to the customer problems. In an ideal world, whenever a request ticket is resolved, a support agent collects common questions and puts together a knowledge base article. So the next time similar tickets are raised, anyone on the team can quickly verify the resolution, ensuring the customer gets quick and satisfying answers. But, it's a classic "which came first, the chicken or the egg” scenario: your team spends countless hours trying to solve issues because of limited help articles, yet creating and keeping up such a knowledge base demands time and resources. As a small team that develops multiple products, we experience this problem first-hand. Our support team has to wade through extensive documentation and past tickets to piece together the best solutions for our customers. Training new team members? That's another uphill marathon. Collecting and analyzing customer tickets can take hours. As you’d imagine, simple issues search by keywords often fall short due to terminology or vocabulary variations. Advanced JQL search might be helpful if the tickets are properly labeled or organized. But the real challenge? Reviewing individual responses to extract meaningful insights. We were evaluating different ways to tackle this problem, and the idea of whipping up an AI-powered solution has been floating around for a while. When Atlassian announced the Codegeist AI theme, we knew, “It’s go time!” So, my team decided to work on an app idea that would revolutionize the customer support job and unlock hidden treasures within support portals for product teams! With that, Intelligent Helper for Jira Service Management came to life. What it does The AI-powered search and recommendation engine helps support agents quickly find relevant information from previous support tickets. This reduces the time spent on information retrieval and enables faster response times. The app provides real-time assistance for JSM agents by gathering related issues based on contextual information and presenting them on the issue details view. From there, users can generate a resolution suggestion in a single click. These suggestions include relevant responses or solutions, helping agents provide faster and more accurate support. How we built it We built this app using Forge Custom UI for the frontend, hosting the backend on AWS with Python programs utilizing LangChain. To maintain an index of relevant issues, we employ ChromaDB as our database. The Forge modules we are using include projectSettingsPage for the issue index creation page and issuePanel for the user interface assisting support agents. On the backend, we leverage the LangChain library to create issue indexes using OpenAI's Embeddings API and generate reply suggestions using the Chat Completions API. Challenges we ran into For us, developing an AI-powered app was a new endeavor. As a result, we had to quickly learn various aspects such as the RAG framework, the LangChain library, VectorDatabase, and how to construct prompts in a relatively short period. We needed to ensure that the app would be genuinely beneficial for real support agents. To accomplish this, we installed the app on our actual support site and validated its functionality. As a result, we made prompt adjustments and fixed any bugs. Accomplishments that we're proud of We achieved a proof of concept and expanded our knowledge in AI app development with Forge - all within 2 weeks! From internal testing, we confirmed that the app significantly benefits our agents, adding more value to ticket analysis beyond the native "Similar requests" feature in Jira Service Management. Cross-functional collaboration from identifying the problem space to coming up with the solution, and the design of this app. What we learned In integrating Forge and OpenAI, we've identified that Forge's processing time limit of 25 seconds can pose challenges when using the OpenAI Chat Completions API, given its response times. Currently, we are employing temporary workarounds to address this issue. However, we recognize the need to transition to a design that allows the Forge to call the API as an asynchronous job by setting up an intermediary server. The current state of AI Chat services and how to use them. In particular, RAG Framework and its implementation method by LangChain. We were very impressed with how well LangChain hides its implementation regarding LLM. What's next for Intelligent Helper - AI Suggest for JSM Support Agents The ultimate goal for our app is to act as a second brain for product teams : Helps support agents work more efficiently with instant access to information they need on top of the JSM database, including knowledge base articles and documentation (through Confluence integration) Free up the support team’s time to allow them to focus on delivering innovative solutions to customer problems, contribute to the knowledge base, and consequently, help the AI model to learn from new responses & suggest better resolutions over time With Confluence integration, we also aim to provide some automated ways for support agents to quickly craft a knowledge base article and directly publish it in Confluence The insights generated from customer’s inquiries can be used to validate new feature ideas and improvements and create the constant feedback loops <div