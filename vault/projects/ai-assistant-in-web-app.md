---
slug: "ai-assistant-in-web-app"
url: "https://devpost.com/software/ai-assistant-in-web-app"
title: "Book Recommendations AI Assistant"
hackathon: "Microsoft Fabric and AI Learning Hackathon"
organization: "Microsoft"
winner: true
words: 630
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# Book Recommendations AI Assistant

> This project is about building a new Recommendations AI Engine leveraging the power of Azure SQL Database, AI Search Vector Index, Microsoft Fabric and Azure Web Apps.

[Devpost](https://devpost.com/software/ai-assistant-in-web-app) · hackathon [[Microsoft Fabric and AI Learning Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** azure, docker, express.js, node.js, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for book recommendations ai assistant

## Body

Architecture Skills Challenge Completion User Resommendation Login\Register Screen Near Real Time Update Logged In - Waiting Update Keyword for personalized recommendations Specific request Very specific request and enhanced answer Inspiration The Microsoft Fabric Platform made a huge impact as a unified SaaS offering with a well established set of integration capabilities. The inspiration came from the idea to create an AI powered recommendations engine Web App, where developers can work from a single platform for all the aspects of the build lifecycle. What it does This a recommendations AI Assistant hosted in Azure Web Apps. The Data is one hand user SignUp details with Book Genre preferences stored in Azure SQL, and a Books Dataset stored in Fabric OneLake. Two Separate pipelines create and update on schedule Vector Indexes within Azure AI Search, where embeddings are generated from Azure OpenAI, using Jupyter Notebooks. The Notebooks perform also data cleaning and transformation, as well as incorporate API rate Limiting backoff procedures for successful embeddings generation. Users are able to login to the Web APP with username \ password where a React Frontend allows them to interact with the Assistant, a NodeJS backend, that recognizes keywords like recommendation or rating and provides answers to the users. When new users sign up a Reflex is activated by CDC on Azure SQL and it fires up a new indexing process for only the new users. The User is updated in near real time with a polling mechanism and a new field created in Azure SQL upon embeddings and index update. How we built it We utilized Terraform for the Azure Infrastructure like KeyVaut , Azure SQL, Azure Container Registry and Microsoft Fabric Environment, Fabric Pipelines, Fabric Onelake and Notebooks. The Frontend is a React WebApp containerized and the backend an expressJS , containerized as well. We utilize an Azure Function to update the SQL Users Table field "RecommendationsReady' and a message updates the user in the UI that their personalized recommendations are ready. Challenges we ran into The challenge was to create a backoff strategy for API Rate Limits, and to manage correctly the Environment and the Cleaning Code for the Books Dataset. Also the decision to use CDC proved to save a lot of coding since we just re index the AI Search Index with a trigger from new user registration on Azure SQL Accomplishments that we're proud of Integrating a Custom Identity Solution on Azure SQL with AI Search and the final result where users Data upon registration are stored in AI Search and a separate Index is created from the books dataset. The Index is updated in Real Time with a CDC Event, with specific rule only to watch the Id Column so we can still update the Table without falling in a loop. All users can chat with the engine about their favorite books, ask about specific Genres or Ratings and even words in the description. We are also very happy with the last minute functionality to update the UI when the embeddings are completed and the index is updated. What we learned We learned a lot about AI Search Indexes, moreover we understood the reach and the power of Fabric and how Jupyter Notebooks can be really automated within an environment. Also connecting Azure DevOps repositories provided the ability to have another option for DevOps developers to deploy their code. Fabric Pipelines added value to the overall solution making it a self updating engine when it comes to new data. What's next for Book Recommendations AI Assistant The plan is to make the UI more appealing, provide more flexibility into the recommendations engine and most important create a Fabric Dashboard that can get logging and monitoring data from all sources, and provide Insights of the Application with precision. <div