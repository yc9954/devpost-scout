---
slug: "course-connection"
url: "https://devpost.com/software/course-connection"
title: "Course Connection"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 1163
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Course Connection

> Ever meet another student, seemingly a stranger, only to realize you were in 12 classes together? See who you have taken classes with and form meaningful connections!

[Devpost](https://devpost.com/software/course-connection) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[education]] [[finance_payments]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** estuary, firebase, networkx, next.js, nginx, node.js, python, react, vercel

## How they structured the write-up

- inspiration
- what it does
- high-level tech stack
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for course connections

## Body

Welcome screen displaying connections between user, courses and other similar students. Hovering over class. Notice that students are represented with purple Hovering over similar user. Note how the edges form the user are at a greater visibility Here is the selection from the signed in user. This is the selection to show the entire graphical network. By hovering over a course or student, you can see all their connections. Course Connection Inspiration College is often heralded as a defining time period to explore interests, define beliefs, and establish lifelong friendships. However the vibrant campus life has recently become endangered as it is becoming easier than ever for students to become disconnected. The previously guaranteed notion of discovering friends while exploring interests in courses is also becoming a rarity as classes adopt hybrid and online formats. The loss became abundantly clear when two of our members, who became roommates this year, discovered that they had taken the majority of the same courses despite never meeting before this year. We built our project to combat this problem and preserve the zeitgeist of campus life. What it does Our project provides a seamless tool for a student to enter their courses by uploading their transcript. We then automatically convert their transcript into structured data stored in Firebase. With all uploaded transcript data, we create a graph of people they took classes with, the classes they have taken, and when they took each class. Using a Graph Attention Network and domain-specific heuristics, we calculate the student’s similarity to other students. The user is instantly presented with a stunning graph visualization of their previous courses and the course connections to their most similar students. From a commercial perspective, our app provides businesses the ability to utilize CheckBook in order to purchase access to course enrollment data. High-Level Tech Stack Our project is built on top of a couple key technologies, including React (front end), Express.js/Next.js (backend), Firestore (real time graph cache), Estuary.tech (transcript and graph storage), and Checkbook.io (payment processing). How we built it Initial Setup Our first task was to provide a method for students to upload their courses. We elected to utilize the ubiquitous nature of transcripts. Utilizing python we parse a transcript, sending the data to a node.js server which serves as a REST api point for our front end. We chose Vercel to deploy our website. It was necessary to generate a large number of sample users in order to test our project. To generate the users, we needed to scrape the Stanford course library to build a wide variety of classes to assign to our generated users. In order to provide more robust tests, we built our generator to pick a certain major or category of classes, while randomly assigning different category classes for a probabilistic percentage of classes. Using this python library, we are able to generate robust and dense networks to test our graph connection score and visualization. Backend Infrastructure We needed a robust database infrastructure in order to handle the thousands of nodes. We elected to explore two options for storing our graphs and files: Firebase and Estuary. We utilized the Estuary API to store transcripts and the graph “fingerprints” that represented a students course identity. We wanted to take advantage of the web3 storage as this would allow students to permanently store their course identity to be easily accessed. We also made use of Firebase to store the dynamic nodes and connections between courses and classes. We distributed our workload across several servers. We utilized Nginx to deploy a production level python server that would perform the graph operations described below and a development level python server. We also had a Node.js server to serve as a proxy serving as a REST api endpoint, and Vercel hosted our front-end. Graph Construction Treating the firebase database as the source of truth, we query it to get all user data, namely their usernames and which classes they took in which quarters. Taking this data, we constructed a graph in Python using networkX, in which each person and course is a node with a type label “user” or “course” respectively. In this graph, we then added edges between every person and every course they took, with the edge weight corresponding to the recency of their having taken it. Since we have thousands of nodes, building this graph is an expensive operation. Hence, we leverage Firebase’s key-value storage format to cache this base graph in a JSON representation, for quick and easy I/O. When we add a user, we read in the cached graph, add the user, and update the graph. For all graph operations, the cache reduces latency from ~15 seconds to less than 1. We compute similarity scores between all users based on their course history. We do so as the sum of two components: node embeddings and domain-specific heuristics. To get robust, informative, and inductive node embeddings, we periodically train a Graph Attention Network (GAT) using PyG (PyTorch Geometric). This training is unsupervised as the GAT aims to classify positive and negative edges. While we experimented with more classical approaches such as Node2Vec, we ultimately use a GAT as it is inductive, i.e. it can generalize to and embed new nodes without retraining. Additionally, with their attention mechanism, we better account for structural differences in nodes by learning more dynamic importance weighting in neighborhood aggregation. We augment the cosine similarity between two users’ node embeddings with some more interpretable heuristics, namely a recency-weighted sum of classes in common over a recency-weighted sum over the union of classes taken. With this rich graph representation, when a user queries, we return the induced subgraph of the user, their neighbors, and the top k most people most similar to them, who they likely have a lot in common with, and whom they may want to meet! Challenges we ran into We chose a somewhat complicated stack with multiple servers. We therefore had some challenges with iterating quickly for development as we had to manage all the necessary servers. In terms of graph management, the biggest challenges were in integrating the GAT and in maintaining synchronization between the Firebase and cached graph. Accomplishments that we're proud of We’re very proud of the graph component both in its data structure and in its visual representation. What we learned It was very exciting to work with new tools and libraries. It was impressive to work with Estuary and see the surprisingly low latency. None of us had worked with next.js. We were able to quickly ramp up to using it as we had react experience and were very happy with how easily it integrated with Vercel. What's next for Course Connections There are several different storyboards we would be interested in implementing for Course Connections. One would be a course recommendation. We discovered that chatGPT gave excellent course recommendations given previous courses. We developed some functionality but ran out of time for a full implementation. <div