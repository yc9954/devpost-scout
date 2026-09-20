---
slug: "judgy-ai-hackathon-judge"
url: "https://devpost.com/software/judgy-ai-hackathon-judge"
title: "Judgy | AI Hackathon Judge"
hackathon: "Atlas Madness"
organization: "Google"
winner: true
words: 283
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "user/legal_professional"
---

# Judgy | AI Hackathon Judge

> Judgy streamlines hackathon judging by leveraging AI to assist in code analysis, market research, and providing chat capabilities, along with an semantic search to navigate through submissions

[Devpost](https://devpost.com/software/judgy-ai-hackathon-judge) · hackathon [[Atlas Madness]]

## Facets

**mechanism** [[retrieval_grounding]]
**user** [[legal_professional]]

**stack** atlas, gcp, langchain, mongodb, node.js, python, svelte, vertexai

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for judgy | ai hackathon judge

## Body

MongoDB Atlas Project Architecture Inspiration I created Judgy to address the challenges of hackathon judging, such as time-consuming evaluation, missed high-potential ideas, limited market knowledge, and inadequate code assessment. What it does Judgy is an AI-powered platform that combines market research, code analysis, chat interaction, and semantic search to enhance hackathon judging. It provides quick insights into the potential of project ideas, assesses code quality, facilitates direct communication between judges and participants, and enables efficient project discovery. How I built it I used Langchain (VertexAI's PaLM is used as the LLM model) to implement the market and the code agent. The market agent fetches real world and latest data by first browsing and then feeding that to the LLM model. After that, I used some prompt engineering to design prompts and querying the LLM. Similar approach is used for the code analysis. All of the data was stored in MongoDB Atlas (Truly dear to heart ❤️) Challenges I ran into Integrating AI algorithms into a cohesive platform, processing natural language, optimizing search functionality, and ensuring a balance between technical accuracy and user experience were some of the challenges I faced. Accomplishments that I'm proud of I am proud of seamlessly integrating AI agents and the overall implementation of the project. What I learned Developing Judgy enhanced my understanding of AI technologies, including Langchain, and helped me understand MongoDB and it's capabilities, as well as the importance of balancing technical usecase with user experience. What's next for Judgy | AI Hackathon Judge I plan to expand the Market Research Agent, enhance code analysis, improve the conversational experience and integrate judge feedback to further enhance Judgy and empower judges in the hackathon judging process. <div