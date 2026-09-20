---
slug: "chatmail"
url: "https://devpost.com/software/chatmail"
title: "Chatmail"
hackathon: "Boost Hacks II"
organization: "Boost Hacks"
winner: true
words: 153
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
---

# Chatmail

> Email as an interface to Large Language Models.

[Devpost](https://devpost.com/software/chatmail) · hackathon [[Boost Hacks II]]

## Facets

**mechanism** [[retrieval_grounding]]

**stack** langchain, python

## How they structured the write-up

- motivation
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for chatmail

## Body

Motivation Access to large language models on the go through the simple email interface. What it does Supports standard LLM queries through email as well as queries for Retrieval Augmented Generation (RAG) using email attachments for context. Detaches the user from the process (send an email and the response comes back as email). How I built it Developed with Python3 and the Langchain libraries (as well as the pop3 and smtp libraries). Challenges I ran into Langchain is useful, but difficult to use and poorly documented. What I learned Python is great for prototyping and getting a project up and running quickly to validate. LLMs can run inference on resource-constrained devices (such as Raspberry Pi's). Smaller LLMs (7 billion parameters) are useful for simple tasks and queries. What's next for Chatmail Support email threads for context (LLM conversation) and agentic workflows (to allow multiple LLMs to work together on the user problem). <div