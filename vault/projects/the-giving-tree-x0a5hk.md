---
slug: "the-giving-tree-x0a5hk"
url: "https://devpost.com/software/the-giving-tree-x0a5hk"
title: "The Giving Tree"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 922
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# The Giving Tree

> Intelligent, Efficient, Crypto Donation Platform powered by AI agents

[Devpost](https://devpost.com/software/the-giving-tree-x0a5hk) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[disaster_emergency]] [[finance_payments]] [[immigration_refugee]]
**substrate** [[financial_record]] [[structured_db]]

**stack** beautiful-soup, chroma, chromadb, flutter, openai, perplexity, postgresql, python, rss, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the giving tree

## Body

The Giving Tree Inspiration As natural disasters and social crises fill our news feeds today, the need for humanitarian aid is at an all time high. With charitable donations sometimes being the only thing many charities rely on to combat their respective issues, for causes such as natural disasters or international conflicts, timely donations make a real time impact. However, not all types of donations are helpful. Without knowing what a disaster-stricken community might need, donations of material goods can quickly cause problems, classified as the “Second Disaster”. Our team discussed what allows rapid monetary transactions between a donor and a charity, through borders and roadblocks that material or cash donations could face, cryptocurrency. Cryptocurrency, once sent from one wallet to another is immediately a liquid asset one can use. Cryptocurrency is essential in areas where it is currently impossible to physically access banks and their services. With its speed, for charitable causes that require immediate reaction, crypto donations could contribute in helping hundreds to thousands and even millions of people. For example, just within seven days after the horrid Earthquakes in Turkey and Syria, AHBAP, a local non-profit, managed to raise 4.9 million dollars through crypto donations. It is also reported that around 20% of non-state aid to Ukraine was done in crypto currency. But nobody has time to constantly check the news, find a charity related to a topic, and donate. We wanted to come up with the most efficient way to assist users with crypto charity donations while being responsive to urgent news that relates to causes that they wish to donate to. What it does The Giving Tree is the most efficient and intelligent charitable donation portfolio manager. It takes the user’s mission statement (topics that they are passionate about) and creates their category portfolio. With live RSS feeds from news websites, our app tracks every article that it deems relevant to charity. It then sorts these articles into categories of impact. With these articles, we find charities that we could donate to and update our user’s charitable donation portfolio in real time to ensure that the user is making the most efficient and intelligent donations. How we built it The Giving Tree is built with a Flutter front end, Python FastAPI backend scripts, a database layer including both Postgres and ChromaDB cloud databases, as well as a series of AI agents to help us cater a collection of charities to most effectively handle user’s crypto. Our chroma databases use similarity search with the embeddings to provide the framework in sorting and filtering out news articles and charities. We scraped charity data from a series of websites, gathering wallet addresses, names, and descriptions to help determine donation portfolios. Additionally, we are constantly scraping RSS feeds for new articles, which are filtered by relevance and further processed through a similarity search to find the most relevant charities. This information, along with user data, is passed to smart contract functions to execute and record transactions on the block chain. Challenges we ran into Coming into the project, none of us had any experience developing with Flutter before nor have tried Web3 on Flutter. Because of this, there was a relatively steep learning curve when it came to our frontend, especially when integrating with AppKit, a package that was relatively unused in this context. We struggled with authentication of crypto wallets due to the limited documentation and community suggestions as well as generating and tuning prompts for the AI agents that would lead for us to get the responses that we thought were “correct”. Because our project had so many different parts to it, it was also a struggle trying to piece them all together. While we had mapped out our system layout, it was still a struggle bringing the full integration to life and we worked close to the deadline to connect everything. Accomplishments that we're proud of Having never really done Web3 development in the past, creating an application involving blockchain and integrating it with a frontend that none of us have worked with before was a difficult yet fulfilling challenge. We also had a relatively complex workflow involving our data processing and filtering, and being able to not only scrape everything but smoothly integrate our results with AI agents and vector databases was something we were proud to accomplish. Trying to wrap our heads around how everything ultimately tied together as well as highlighting the necessary relationships and interactions required collaborative system design effort from everyone, and we had very productive conversations trying to optimize our structures. What we learned As a team, we learned about developments in Flutter and creating our own API endpoints to support integration of backend development with Flutter. We learned how to utilize software IDE’s that integrated AI flawlessly to power our development process. We experimented and challenged ourselves to learn more about agentic workflow, letting AI make its own decision with tool calling, and classifications evaluations in order to fine tune our prompt generation. We also had the opportunity to dive deeper into Web3 and blockchain development, taking time to experiment with smart contracts and crypto wallets. What's next for The Giving Tree We want to continue integrating other cryptos into our app so that crypto donations become accessible to anyone who has ever owned a crypto wallet. We also want to expand the number of charities that will accept crypto donations, maybe once they find out how effective and powerful crypto donations could be, they’ll join us for our mission! <div