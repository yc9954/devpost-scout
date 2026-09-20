---
slug: "tigergraph-unbiased-news"
url: "https://devpost.com/software/tigergraph-unbiased-news"
title: "BiasCheck - Chrome extension to reduce bias in online news"
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 721
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/security_privacy"
  - "user/general_public"
  - "substrate/structured_db"
---

# BiasCheck - Chrome extension to reduce bias in online news

> This project helps foster critical thinking by showing bias/accuracy of all news sources and also helps users explore news with differing view points from their usual idealogies..

[Devpost](https://devpost.com/software/tigergraph-unbiased-news) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets

**mechanism** [[cross_origin_web]] [[graph_reasoning]] [[realtime_stream]] [[vision_ocr]]
**domain** [[security_privacy]]
**user** [[general_public]]
**substrate** [[structured_db]]
  <sub>weak: video_visual</sub>

**stack** chromeextension, flask, javascript, newscatcherapi, python, rest, tigergraph

## How they structured the write-up

- inspiration
- what it does
- how we built it
- problem
- challenges we ran into
- what's next for tigergraph - unbiased news
- tech stack
- data sources
- screenshots
- references

## Body

Architecture Generated graph from newscatcher api data Load the chrome extension code in the "extensions" section in chrome Chrome extension option visible on news websites and other social media sites Shows bias and accuracy rating of the current news being viewed. Also shows similar and different view news Alerts user of news articles with differing view points bias ratings visible on social media sites News sources imported with ratings Inspiration I wanted to work on making people aware of their inherent bias due to the social media bubble they live in. So built a chrome extension which works on a Graph database backend and tells them similar and differing news views. What it does Chrome extension shows bias/accuracy ratings of all news sites visited by user News articles with similar and differing view points are shown to make user aware of the bias How we built it Data is fetched from Newscatcher API periodically using cron jobs. This data is then loaded on to tiger graph database to populate the graph and run cosine based similarity algos Basic Entity detection is done using NLP libraries News Data is then exposed through simple REST API application built on python flask Architecture Problem The Problem Human thought is prone to errors. In recent times, we have gotten better at understanding why those errors occur and how to utilize and exploit them. Modern advances in technology like Artificial Intelligence, big data, cloud computing, and blockchain can all be used to manipulate our cognitive biases in order to sell us products and services or make us value certain information more than others. One of the most notable of these cases is the utilization of confirmation bias by social media companies to create “filter bubbles” of opinions that a person agrees with. This not only prevents us from being well-informed, but ultimately leads to a lack of critical thinking and adds to polarization. If we only listen to and validate one way of thinking, and do not expand and question it, sooner or later we will become intolerant citizens. And when there is no more tolerance, the very foundations of our democratic coexistence begin to crack. The Challenge In a context in which humanity is facing major challenges and democracies are being questioned throughout the world, emerging technologies can represent either a threat or an opportunity. In this case, the key is to identify a way to use these technologies to break through the confirmation bias and the filter bubbles enhanced by social media platforms. The aim is to foster critical thinking in digitally literate citizens who access and critically relate to different types of information, and who increasingly engage in dialogue with other points of view and with those who think differently. The goal is not to come up with an alternative business model for digital platforms or to eliminate the confirmation bias of the human mind, which would be almost impossible. Rather, it is to empower citizen-users with the necessary tools to be able to identify the presence of these biases and to consciously seek diverse perspectives and opinions on the same topic. Challenges we ran into Rate limitation in fetching news articles so I resorted to running the news api scripts at periodic intervals What's next for TigerGraph - Unbiased News We wish to include the following features in further releases Entity detection using algorithms Real time graph database updation Tech Stack TigerGraph, pytigergraph, Flask, Chrome Extension API - Simple flask hosted REST API application for accessing similar/differing news articles from TigerGraph Chrome Extension - That gets activated on over 1000 different news sources and also all news in twitter, facebook, reddit, google etc Data sources Bias Ratings, Accuracy rating - Various rating agencies News data - Newscatcher News API Screenshots https://docs.google.com/presentation/d/1Ko59z8EhumNrrtNfCdut1h9J8nmWXHyY7E1TokSNtFY/edit?usp=sharing References Garton Ash, T. (2017). Free Speech: Ten Principles for a Connected World. Pariser, E. (2017). The Filter Bubble: How the New Personalized Web Is Changing What We Read and How We Think. Pariser: https://medium.com/@10797952/the-causes-and-effects-of-filter-bubbles-and-how-to-break-free-df6c5cbf919f Zuboff, S. (2018). The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power. Friedman-Wheeler, D. (2020). Democracy requires us to work on our biases – all of them. The Fulcrum. Available in: https://thefulcrum.us/amp/democracy-requires-us-to-work-on-our-biases-all-of-them-2645473111 Lu, M. (2020). 11 Cognitive Biases That Influence Political Outcomes. Visual Capitalist. Available in: https://www.visualcapitalist.com/11-cognitive-biases-influence-politics/ <div