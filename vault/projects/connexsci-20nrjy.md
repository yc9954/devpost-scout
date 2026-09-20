---
slug: "connexsci-20nrjy"
url: "https://devpost.com/software/connexsci-20nrjy"
title: "ConnexSci"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 475
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/retrieval_grounding"
  - "domain/scientific_research"
  - "user/researcher"
  - "substrate/structured_db"
---

# ConnexSci

> Most investment in scientific investments fail to materialize. We provide analytics and a crowdsourcing platform to identify the highest-potential and impactful projects for public and private funds.

[Devpost](https://devpost.com/software/connexsci-20nrjy) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[graph_reasoning]] [[retrieval_grounding]]
  <sub>weak: vision_ocr</sub>
**domain** [[scientific_research]]
  <sub>weak: civic_government, finance_payments</sub>
**user** [[researcher]]
**substrate** [[structured_db]]
  <sub>weak: document_pdf</sub>

**stack** beautiful-soup, cohere, ds3, firebase, flask, javascript, json, jupyter-notebook, nextjs, postgresql, python, pytorch, react

## Body

Inspiration The way research is funded is harmful to science — researchers seeking science funding can be big losers in the equality and diversity game. We need a fresh ethos to change this. What it does Connexsci is a grant funding platform that generates exposure to undervalued and independent research through graph-based analytics. We've built a proprietary graph representation across 250k research papers that allows for indexing central nodes with highest value-driving research. Our grant marketplace allows users to leverage these graph analytics and make informed decisions on scientific public funding, a power which is currently concentrated in a select few government organizations. Additionally, we employ quadratic funding, a fundraising model that democratizes impact of contributions that has seen mainstream success through https://gitcoin.co/ . How we built it To gain unique insights on graph representations of research papers, we leveraged Cohere's NLP suite. More specifically, we used Cohere's generate functionality for entity extraction and fine-tuned their small language model with our custom research paper dataset for text embeddings. We created self-supervised training examples where we fine-tuned Cohere's model using extracted key topics given abstracts using entity extraction. These training examples were then used to fine-tune a small language model for our text embeddings. Node prediction was achieved via a mix of document-wise cosine similarity, and other adjacency matrices that held rich information regarding authors, journals, and domains. For our funding model, we created a modified version of the Quadratic Funding model. Unlike the typical quadratic funding systems, if the subsidy pool is not big enough to make the full required payment to every project, we can divide the subsidies proportionately by whatever constant makes the total add up to the subsidy pool's budget. For a given scenario, for example, a project dominated the leaderboard with an absolute advantage. The team then gives away up to 50% of their matching pool distribution so that every other project can have a share from the round, and after that we can see an increase of submissions. The model is then implemented to our Bounty platform where organizers/investors can set a "goal" or bounty for a certain group/topic to be encouraged to research in a specific area of academia. In turn, this allows more researchers of unpopular topics to be noticed by society, as well as allow for advancements in the unpopular fields. Challenges we ran into The entire dataset broke down in the middle of the night! Cohere also gave trouble with semantic search, making it hard to train our exploration model. Accomplishments that we're proud of Parsing 250K+ publications and breaking it down to the top 150 most influential models. Parsing all ML outputs on to a dynamic knowledge graph. Building an explorable knowledge graph that interacts with the bounty backend. What's next for Connex Integrating models directly on the page, instead of through smaller microservices. <div