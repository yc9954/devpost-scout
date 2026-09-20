---
slug: "personal-learning-journey"
url: "https://devpost.com/software/personal-learning-journey"
title: "Knowledge Keeper"
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 731
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/graph_reasoning"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Knowledge Keeper

> Tag, share, query and learn from your own and others' learning journey

[Devpost](https://devpost.com/software/personal-learning-journey) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets

**mechanism** [[cross_origin_web]] [[graph_reasoning]]
**domain** [[developer_tools]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** extension, fastapi, javascript, python, tigergraph

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for knowledge keeper

## Body

Graph Schema Knowledge Domain Graphs User Graph User Knowledge Domain Graph Inspiration Learning is a lifelong process in the age of the internet. Today the problem is the abundance of resources in various forms (video, text, images) on a topic. Often you don't know how useful a resource would be in terms of your prior knowledge and what you aim to learn from it. A normal search engine would provide generic resources (introductory and advanced) without considering your level of skillset. Another aspect is the pain in knowledge-keeping, storing, and sharing various resources. How can we make this time-consuming process more efficient/better? The problems can be described in the following points - The abundance of resources on any topic Where to read/watch from next to fulfill your criteria of learning? Current search engines do not take your prior knowledge/ skill level into consideration while 4. recommending resources to learn from How can we efficiently manage the things we learn? How can bookmarking be made more efficient? How can linked and domain knowledge data help us? What it does Our solution builds a learning journey over a lifetime. Any user can add to their own journey, share the journey and see other people’s journeys. Using our browser extension the user can easily add resources to track their learning journey. User can discover resources with similar tags and concepts. User can query over their own learning graph to revisit similar URLs saved. An automated graph generation is generated through which the user doesn’t have to manually attach the nodes. How we built it Our solution is divided into the following parts - Browser extension by which users can add any URL to their own learning journey. They can save notes, highlights, tag the links Through NLP we discover similarities which help us to discover new relations and insights. We discover resources that share the same tag and which concepts. In the backend, there is a User-specific learning graph being formed in an automated manner. Nodes are URL’s, Date, tags, highlights, notes, type of resource Graph Backend/Database(Tigergraph) that help us to find relations and build a graph structure Get insights about your collected resources. Which resources are related to each other and in which way they are connected to each other? Our automated graph generation process takes the previously formed graph into consideration and finds out the correct node to attach to by similarity algorithms (We have this module ready, and need to query to GSQL to embed it into the pipeline) Challenges we ran into Defining the solution - We believed in the problem statement and brainstormed a lot about what a feasible solution should be. Our process involved talking to our friends about the problems they face while learning something new to come to a solution that could be deployed in the real world. Once we had the problem statement and solution defined we went through many iterations of how the graph scheme of data and graph should look like. Technical challenges Debugging a browser extension Concept Mining Building Domain Knowledge Graph Find data Accomplishments that we're proud of We are proud of learning an interesting graph framework that provides a beautiful UI and easy querying. Moreover, we built an end-to-end application with backend and browser extension. We also expanded our knowledge about NLP, graph structure and knowledge graphs. We are proud of building something which could be useful to many people interested in changing careers or learning something new. Learning from the journeys of others would save time and provide the best-trusted methods. We have something not just for a submission but a base-case of something which could be useful for a greater audience. What we learned We learned the following things - Tigergraph Gsql Explore your Data(sometimes very interesting) How to build a browser extension Finding and building a domain knowledge graph Building a graph scheme What's next for Knowledge Keeper We would like to build this into a platform where any user can share their learning journeys and learn from other people's journeys. Our product will have two faces to our platform - Where a user can search for other people with a similar background and look at their journeys The user can search within their own learning journey/ notes for revision Get recommendations for new resources Different queries to get more insights into the collected resources Logo <div