---
slug: "synthesis-ag1djb"
url: "https://devpost.com/software/synthesis-ag1djb"
title: "Synthesis"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 828
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "substrate/structured_db"
---

# Synthesis

> News that promotes personalization and prevents polarization.

[Devpost](https://devpost.com/software/synthesis-ag1djb) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[retrieval_grounding]]
  <sub>weak: researcher</sub>
**substrate** [[structured_db]]

**stack** agents, algorithms, gpt-4, llms, natural-language-processing, next.js, pinecone, python, react, supabase, vectordbs, webscraping

## Body

Home Search Gists Syntheses Motivation Political polarization, now more than ever, is moving at an alarming rate. Our team has worked in the forefront of technology, policy, political science, and sociology. Christopher Arraya is a computational political polarization researcher at UNC-Chapel Hill, studying the Bolivian coup in 2019. He also works as an AI research advisor for multiple policy-tech nonprofits. Pranav Ramesh is an emerging entrepreneur interested in applying technology to social good who has led canvassing for several political campaigns. Ron Nachum has led several emerging technology research initiatives at Harvard analyzing effects of new technologies and how to mitigate/ensure positive outcomes–from AI, to investments, tech, and even space. The current media landscape, fueled by political polarization and algorithmic echo chambers, fuels division and hinders understanding. Synthesis was born from the desire to create a news platform that prioritizes unbiased information, facilitates diverse perspectives, and puts the news more in the hands of the readers through hyper-personalization. In the Synthesis, our users don’t just want to read about the world. They want to engage in it. What it does Think of Synthesis as a new-age of information digestion. Synthesis takes existing news articles around the internet, clusters them by topic similarity, and reshapes them into unbiased articles, equipped with enhanced readability and quality of life features that make it easier for readers to resolve any areas of confusion immediately. Search up any topic you want to learn about, and you will be presented with a list of “Gists,” which are quick blurbs. Through these readers, can decide whether or not to learn more, at which point they can dive into the “Synthesis” of the topic, or a deeper dive into the subject matter. How it works Synthesis is built on the following features: Scale : Synthesis aggregates news daily from 60K+ articles across 100+ sources. Clustering : We’ve developed the first AI News Agent that intelligently extracts and clusters using a combination of vector databases and set theory, and understands news to increase knowledge. Gists : Synthesis clusters are summarized into at-a -glance overviews of topics via our rich content extraction. Syntheses : Should the user choose to engage with a news topic past the Gist, these AI-generated analyses allow for the connection and interpretation of similar-topic articles. Recommender Algorithm : Recommendations regularize/balance against echo chambers. Info Traversal : Within-topic and global semantic search Hyper-personalization : Within syntheses, users can dynamically adjust the reading level of the content. Extensions : Users can engage with our Q&A and content explanation extensions. Rich Extraction : We adopt visuals and tooling for our high-fidelity data. How we built it A core part of building out this project that was particularly difficult and stimulating was our agent backbone. We reasoned about how to manage tens of thousands of articles in terms of their sources, relationships to one another, significance, and more. We came up with a truly innovative, multi-step agent framework that scraped over 60,000 news articles during this hackathon and continuously scrapes 20+ articles per minute to keep our dataset constantly active. We developed a system of clusters that related articles to one another using textual extractions, semantic similarity, and other parameters of articles. These then enabled us to extract rich data from articles and produce more complex outputs and workflows, paving the way for endless new ways to interact with news. And the most amazing thing? This agent costs almost nothing to run. Our total costs throughout this hackathon to scrape tens of thousands of data points, vectorize and store them in a vector database and a Postgresql database to query efficiently and extract powerful information lies in the single digit dollars. Due to optimizations and algorithmic ingenuity, we are able to create a truly one-of-a-kind agent system that can scrape the entire internet’s wealth of news knowledge at virtually zero cost. Challenges we ran into Creating Synthesis was a very challenging but intellectually stimulating endeavor. We sought to solve an increasingly prevalent social problem using rapidly innovating technology. In developing this project, we learned to leverage diverse web frameworks and pushed the boundaries of what was capable with generative AI. We found out very quickly, for example, that there is a tradeoff between context limit and requerying with regard to LLMs: In Lost in the Middle: How Language Models Use Long Contexts (arXiv:2307.03172), Liu et al demonstrate that when given longer contexts, LLM performance degrade when models must reference information in the middle of such contexts. Feeding multiple articles into a single context for an LLM to interpret could therefore allow them to fall prey to this trap. On the other hand, providing news articles to LLMs to read in multiple queries could prove to be costly as the state-of-the-art LLMs, such as GPT-4, can potentially be expensive. We were able to solve this issue using an ensemble of methods approach where we had our agent specialize in different contexts at different stages of our scraping pipeline. <div