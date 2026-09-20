---
slug: "dailies-dailies-read-all-about-it"
url: "https://devpost.com/software/dailies-dailies-read-all-about-it"
title: "Dailies, dailies, read all about it"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 496
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Dailies, dailies, read all about it

> Your AI financial digest: Transforming overwhelming market news into accessible insights. Stay informed on global financial developments without spending hours reading—perfect for busy professionals.

[Devpost](https://devpost.com/software/dailies-dailies-read-all-about-it) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** openai, pdf2image, python, telethon, vectorembeddings

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dailies, dailies, read all about it

## Body

Inspiration I worked in the financial services industry, and there's not enough time in the day to digest all the information that comes out pertaining to markets. I built this news agent to synthesize the largest financial media outlets in quickly consumable market updates. What it does This agent processes newspapers published by the financial news sources, breaks the papers up into articles, sort the articles based on market category, and then provides summaries based on the users request. The agent can provide a summary of a specific topic, a list of articles published on a specific topic, as well as summarize specific articles. How we built it I created a pdf processor function to break down the pdfs of the newspapers. Articles are turned into individual files, which are then sorted based on the category they pertain to. Articles are then stored in a vector store, so that the LLM can easily parse the articles and find context relevant to the user's query. I then built functionality around this vector database for the agent to provide the synthesize information described above. Challenges we ran into The biggest challenge with news is staying up to date with the latest developments. The first step I made to help improved access to the latest info is creating a system (telegram.py in pdfs folder) that downloads the newspaper pdfs automatically from telegram. This is currently an individual file I have to run, but it will be be implemented with the agent in my next version. My goal is to make this agent fully autonomous, so it constantly grabs and processes the latest information. Accomplishments that we're proud of This is the first hackathon I've participated in, so I'm just generally pumped to be here. What we learned A ton about Near AI, vector stores, and the capabilities of python. What's next for Dailies, dailies, read all about it A lot. This is just the beginning. My goal is for this agent to be fully autonomous. I want the agent to find, download, process, and store the latest news on its own. My plan is to create an Telegram event smart contract on Near that listens for new newspapers to be posted. Once the agent finds a new news source, it will automatically do its thing. Then people will be able to access the latest information at at all times. Once this is complete, I want to create a customized user experience. I want the agent to learn about its users request, so it can provide more relevant answers. To do this, I plan to build an web UI around this agent. I will need to enhance the agent's memory, so it can learn about the user as well as the more relevant pieces of data it processes. Overall, I'm very excited for the future of this agent. Dailies news agent is something that I plan to use everyday, and I hope other people find it useful as well. <div