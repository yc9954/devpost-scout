---
slug: "code-flow"
url: "https://devpost.com/software/code-flow"
title: "Code Flow"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 522
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "user/researcher"
---

# Code Flow

> Remove the need for tedious onboarding by demystifying new repositories.

[Devpost](https://devpost.com/software/code-flow) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[retrieval_grounding]]
**user** [[researcher]]

**stack** cohere, flask, mongodb, python, pyvis, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for code flow

## Body

Logo Inspiration All of us have gone through the painstaking and difficult process of onboarding as interns and making sense of huge repositories with many layers of folders and files. We hoped to shorten this or remove it completely through the use of Code Flow. What it does Code Flow exists to speed up onboarding and make code easy to understand for non-technical people such as Project Managers and Business Analysts. Once the user has uploaded the repo, it has 2 main features. First, it can visualize the entire repo by showing how different folders and files are connected and providing a brief summary of each file and folder. It can also visualize a file by showing how the different functions are connected for a more technical user. The second feature is a specialized chatbot that allows you to ask questions about the entire project as a whole or even specific files. For example, "Which file do I need to change to implement this new feature?" How we built it We used React to build the front end. Any folders uploaded by the user through the UI are stored using MongoDB. The backend is built using Python-Flask. If the user chooses a visualization, we first summarize what every file and folder does and display that in a graph data structure using the library pyvis. We analyze whether files are connected in the graph based on an algorithm that checks features such as the functions imported, etc. For the file-level visualization, we analyze the file's code using an AST and figure out which functions are interacting with each other. Finally for the chatbot, when the user asks a question we first use Cohere's embeddings to check the similarity of the question with the description we generated for the files. After narrowing down the correct file, we use its code to answer the question using Cohere generate. Challenges we ran into We struggled a lot with narrowing down which file to use to answer the user's questions. We initially thought to simply use Cohere generate to reply with the correct file but knew that it isn't specialized for that purpose. We decided to use embeddings and then had to figure out how to use those numbers to actually get a valid result. We also struggled with getting all of our tech stacks to work as we used React, MongoDB and Flask. Making the API calls seamless proved to be very difficult. Accomplishments that we're proud of This was our first time using Cohere's embeddings feature and accurately analyzing the result to match the best file. We are also proud of being able to combine various different stacks and have a working application. What we learned We learned a lot about NLP, how embeddings work, and what they can be used for. In addition, we learned how to problem solve and step out of our comfort zones to test new technologies. What's next for Code Flow We plan on adding annotations for key sections of the code, possibly using a new UI so that the user can quickly understand important parts without wasting time. <div