---
slug: "llm-pro-max"
url: "https://devpost.com/software/llm-pro-max"
title: "LLM Pro Max"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 357
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# LLM Pro Max

> Tired of character limits on ChatGPT? Look no further than LLM Pro Max! By spoon-feeding little bits of info to the LLM, this amazing app is able to greatly improve the efficiency of token usage.

[Devpost](https://devpost.com/software/llm-pro-max) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[structured_db]]

**stack** auth0, chromadb, cohere, convex, fastapi, github-auth, javascript, langchain, networkx, python, pyvis, rag, react.js, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for llm pro max

## Body

Landing Page Interactive Visualization Graph Dependency Visualization General Repo interaction Code Specific Repo interaction Inspiration Large Language Models (LLMs) are limited by a token cap, making it difficult for them to process large contexts, such as entire codebases. We wanted to overcome this limitation and provide a solution that enables LLMs to handle extensive projects more efficiently. What it does LLM Pro Max intelligently breaks a codebase into manageable chunks and feeds only the relevant information to the LLM, ensuring token efficiency and improved response accuracy. It also provides an interactive dependency graph that visualizes the relationships between different parts of the codebase, making it easier to understand complex dependencies. How we built it Our landing page and chatbot interface were developed using React. We used Python and Pyvis to create an interactive visualization graph, while FastAPI powered the backend for dependency graph content. We've added third-party authentication using the GitHub Social Identity Provider on Auth0. We set up our project's backend using Convex and also added a Convex database to store the chats. We implemented Chroma for vector embeddings of GitHub codebases, leveraging advanced Retrieval-Augmented Generation (RAG) techniques, including query expansion and re-ranking. This enhanced the Cohere-powered chatbot’s ability to respond with high accuracy by focusing on relevant sections of the codebase. Challenges we ran into We faced a learning curve with vector embedding codebases and applying new RAG techniques. Integrating all the components—especially since different team members worked on separate parts—posed a challenge when connecting everything at the end. Accomplishments that we're proud of We successfully created a fully functional repo agent capable of retrieving and presenting highly relevant and accurate information from GitHub repositories. This feat was made possible through RAG techniques, surpassing the limits of current chatbots restricted by character context. What we learned We deepened our understanding of vector embedding, enhanced our skills with RAG techniques, and gained valuable experience in team collaboration and merging diverse components into a cohesive product. What's next for LLM Pro Max We aim to improve the user interface and refine the chatbot’s interactions, making the experience even smoother and more visually appealing. (Please Fund Us) <div