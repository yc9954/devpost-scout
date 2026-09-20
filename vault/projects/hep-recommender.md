---
slug: "hep-recommender"
url: "https://devpost.com/software/hep-recommender"
title: "hep-recommender"
hackathon: "Facebook Hackathon: AI"
organization: "Facebook"
winner: true
words: 680
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
---

# hep-recommender

> A recommender system for scientific papers in the field of High Energy Physics

[Devpost](https://devpost.com/software/hep-recommender) · hackathon [[Facebook Hackathon- AI]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]

**stack** amazon-web-services, bootstrap, flask, gensim, gunicorn, heroku, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hep-recommender

## Body

Inspiration With the vast amount of items available in digital scientific libraries, recommender systems for academic literature have become an active field of research. These systems can have a direct impact on the research community by making it easier to navigate, filter, and discover relevant scientific articles. Digital libraries typically provide standard bibliographic information for a given article, such as the reference list and the list of works citing the article. Though these are very useful for exploring the literature, it is clear that a more direct access to relevant related works to a given article would be useful. Indeed, sites like Google Scholar, Semantics Scholar, and Microsoft Academic, already offer recommendations of related articles. There are different approaches to determine the degree of similarity between articles in order to identify related work. Some works have used text-mining and natural language processing methods. Another popular approach is based on citation analysis, where the similarity between two articles is estimated based on bibliographic information. Finally, other works have used a combination of the previous approaches. In this project, we develop a recommender system based on citation analysis. More specifically, we will develop a recommender system that elaborates on the ideas of co-citation analysis and co-citation proximity analysis (CPA). Co-citation analysis is based on the premise that articles which are frequently cited together (by the same papers) should be related to each other. CPA extends this idea by incorporating the notion that the closer the citations are to each other within the article text, the more likely it is that they are related. While these methods are relatively simple they provide a high quality of related article recommendations. Our recommender system relies on a distributed representation of articles obtained by training a Skip-Gram model on reference lists. This model also captures the notion that articles cited close to each other on the text are similar. What it does hep-recommender aims to help researchers and students in their quest for knowledge. It is a recommender system for scientific articles in the field of High Energy Physics. Researchers exploring the literature can search for similar articles to the ones they are currently interested via a web application. This allows researchers to find relevant literature in the topic they are interested in. How we built it The recommender system is based on data collected from the INSPIRE-HEP API. We collect reference lists for each article. We estimate the similarity among articles based on how frequent they are cited close to each other within the reference lists. We use an approach that has proven to be very fruitful in Natural Language Processing. We take the lists of references and train a Skip-Gram model, such that articles which tend to be cited close to each other will have similar embeddings. We can then retrieve recommendations by searching for embeddings that are close in the vector space. The Skip-Gram model used to determine the similarity between articles was implemented using Pytorch. Storage of data and model artifacts is done in AWS S3 and deployment of the Flask web application is currently done using Heroku. More details can be found here . Challenges we ran into One challenge we faced was keeping a low memory footprint on the server side of the web application while hosting the machine learning model artifacts. Accomplishments that we're proud of We are proud to serve high quality recommendations of similar articles to the community via a web application. We are also proud to use novel technologies like Pytorch and AWS in conjunction within our project. What we learned We have learned several things, from machine learning to web development (both backend and front-end). We improved our knowledge about the different libraries and services we used for this project. We also learned new things about the field of information retrieval and recommender systems. What's next for hep-recommender There are many open possibilities for personalization in the area of Digital Libraries. We would like to add more features and services with the objective of personalizing the exploration of literature, academic job search and conferences. <div