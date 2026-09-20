---
slug: "gemini-rqv74l"
url: "https://devpost.com/software/gemini-rqv74l"
title: "Gemini"
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 362
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Gemini

> An eclectic news search engine that helps with deduplication of news articles and enriches your reading experience.

[Devpost](https://devpost.com/software/gemini-rqv74l) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets

**mechanism** [[retrieval_grounding]]
**substrate** [[financial_record]] [[web_dom]]
  <sub>weak: sensor_telemetry</sub>

**stack** keyword-generation, natural-language-processing, pandas, python, pytigergraph, semantic-search, sentiment-analysis, streamlit, tigergraph

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gemini

## Body

Schema System Metrics View of the graph after data loading Path finding Topic View Shortest path for new insights/relations Country View Anchor and relevant news TigerGraph Dashboard Website Anchor News Search Related News on Website Inspiration The problem statement selected is 'Reduce The Noise Of News Search' (No.7). Time is of essence and hence spending it by only consuming necessary information is very important. That is the problem this project tries to solve in the domain of news search. What it does An eclectic news search engine that helps with deduplication of news articles and enriches your reading experience. Enables readers to dig deep into a certain opinion or explore multiple facets of the news at hand. How we built it 1) Fetched news articles from newsapicatcher.com. 2) Used the PyTigerGraph Python library to interact with the TigerGraph instance. 3) Used 3 different NLP models for Semantic Search, Keyword Generation and Sentiment Analysis respectively. Helps with enriching the news articles with additional metadata. 4) Later, loaded all data to the TigerGraph instance and processed/explored data in several ways using custom GSQL queries as well as special algorithms like centrality and similarity. 5) Finally, results are shown to the end-user in a Streamlit web application. Challenges we ran into There is a slight learning curve to graph technology and GSQL if you are learning it for the very first time. The resources and explanations provided in the TigerGraph docs were very helpful. My personal notes and useful references for this project have been linked in the Github repo. Accomplishments that we're proud of Being able to build a competent real-world solution for a pressing problem. What we learned Explored and used Graph technology for the first time and it was a very fulfilling experience. Learned about how existing news search engines work, their strengths and weaknesses and how cutting edge advances in NLP (keyword generation, semantic search) can be used to make news search better for the readers. What's next for Gemini The solution and the way it has been built can be extended into a regular search engine capable of generalizing on regular websites (non-news) as well; for different search terms. <div