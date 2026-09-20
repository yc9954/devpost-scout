---
slug: "reflexion-b2gjhk"
url: "https://devpost.com/software/reflexion-b2gjhk"
title: "Reflexion"
hackathon: "Junction 2016"
winner: true
words: 371
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Reflexion

> Reflexion is a social media analytic product providing analytic dashboards based on big data and machine learning

[Devpost](https://devpost.com/software/reflexion-b2gjhk) · hackathon [[Junction 2016]]

## Facets

**substrate** [[sensor_telemetry]] [[web_dom]]

**stack** apache-nifi, azure, centos, css, elasticsearch, facebook, facebook-graph, graphapi, hadoop, heroku, html, java, kibana, kibana5

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for reflexion

## Body

Facebook dashboard 2 Facebook dashboard 1 Twitter dashboard 1 Competitor dashboard Twitter dashboard 2 Inspiration The social media landscape continues to evolve at a rapid pace, but then, you already know that. Like us, you live and breathe it daily. The big brands need to track and measure all user interactions efficiently. We provide a social media analytic solution based on big data aiming to improve their digital presence. What it does Our solution “Reflexion” aims to help those brands to establish a smart social media strategy based on Bigdata providing 4 Packages: 1- Social Media Performance: to monitor metrics and get a real overview of digital impact. 2- Competitive Intelligence: to get competitors insights and understand their strategy. 3- Customer care: to monitor user interactions and auto react with a machine learning system. 4- Strategy Inspiration: to identify trends, influencers and most engaged users. How we built it Gathering data from social media (Facebook & twitter basically) using APIs ( graph api and twitter stream API) and submitting it through a Heroku server to Azure. On Azure, we use big data architecture to process the huge amount of received data (Using apache Nifi and Hadoop), then we efficiently transfer the aggregated data to elasticsearch. The last step is to display the most interesting collected information to the final user that can be used as a part of decision making process (Using Kibana). Challenges we ran into Facebook confidentiality strategy protecting any external data pumping. Having a scalable/efficient big data architecture. Building the big data architecture. Choosing the best strategy of data aggregation and displaying the most meaningful insights. Accomplishments that we're proud of Build a full stack and configurable solution. The use of plenty (more than 10) tools that we didn't know before. What we learned Time management. Team work. Work under pressure. The use of many tools. What's next for Reflexion Correlating data in our dashboard between the main company and its competitors. Making more predicting analytics. Collecting more insights. PS : To try the website please pass the two steps authentication with those informations : Step 1 : User : kibanaadmin Password : admin Step 2 : User : admin_younes Password : kibana First Demo : https://www.youtube.com/watch?v=WZOAW1Y9v1Q <div