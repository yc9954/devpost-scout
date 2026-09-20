---
slug: "ground-truth-97nqws"
url: "https://devpost.com/software/ground-truth-97nqws"
title: "Ground Truth"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 402
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# Ground Truth

> Remove the need to manually update your docs. When you make a PR, Doc's are auto updated based on the changes you committed.

[Devpost](https://devpost.com/software/ground-truth-97nqws) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** chromadb, groq, python, rag, reflex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ground truth

## Body

slide intro Inspiration When I was interviewing at a ~20 person startup and reading through their introduction doc, I read that the co-founders would often spend lots of nights just catching up on docs from the prior week. To me, the last thing any employee, much less a founder, should be spending their time on is writing docs. Ground Truth lets you simply review and accept changes to your docs based on what you have been coding. What it does Each time you make a commit to a specific repo, a new entry is made How we built it Chroma Docs can be pretty large. Far too large to pass multiple pages into a context window. To account for this, we embedded each page of the docs into a chromaDB using their built in functions, and we query the Vector DB we created to find the most similar doc so we can pass that as context. Groq We used Groq for basically all of our small context text completion. This was especially helpful when passing a code diff into the llama model and getting a description of what was being updated. This allowed us to consistently retrieve the right documentation that we would then update Reflex.dev Since most of our initialization and ChromaDB stuff was already being done in Python, it made sense to continue using it and go ahead with Reflex for the full frontend and backend. Challenges we ran into The biggest issue for us was finding good contenders for projects. Firstly, they had to be open source, non negotiable for us to test with. Secondly, they had to have a developer program or some need for docs that we could reasonably update. Accomplishments that we're proud of This was all of our first times working with any of these technologies (RAG anything, really) and we're proud to have put it all together in a somewhat attractive way over the 36 hours. The approach we took probably was a good 10 hours of ideation so it's nice to have it built and working What we learned Pretty much everything about RAG and Reflex. We all knew very little about the domain coming into this. What's next for Ground Truth This project has real potential as a company but is an incredibly hard engineering problem. If we stay excited about building it, we could make it widespread and very modular. <div