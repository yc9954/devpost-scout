---
slug: "babel-jodvx5"
url: "https://devpost.com/software/babel-jodvx5"
title: "PlanMyNite"
hackathon: "Databricks Generative AI World Cup"
organization: "Databricks"
winner: true
words: 315
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
---

# PlanMyNite

> Planning a trip? Ask our LLM what's going on at your destination and have it give you a number of activities and points of interest.

[Devpost](https://devpost.com/software/babel-jodvx5) · hackathon [[Databricks Generative AI World Cup]]

## Facets

**mechanism** [[retrieval_grounding]]
  <sub>weak: geospatial</sub>

**stack** databricks, django, google-maps, meta-llama-3-70b, python, serpapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Example response from our bots. Working links! Another example response from a different prompt with differently formatted links. Inspiration I like to travel, but I don't like to plan. It would be nice if I could just ask a robot to tell me what options there are for things to do and places to see, so we built just that. What it does Using just a text prompt, our web app will show two responses from two bots, one of whom will provide details on events happening in your destination, including ticket links and recommendations, and the other will look for places of interest that align with your stated interests. How we built it This tool is built in python using the django framework for the web app. The LLM is the meta-llama-3-70b foundation model offered by databricks, and we've implemented RAG using serpapi . The user's prompt is parsed into a list of searches by the LLM, fed into serpapi, and then the results are parsed into a table, formatted into text and fed to the LLM as context for a response to the user. Challenges we ran into Connecting to and implementing various APIs Prompt engineering for good responses from foundation models Writing and hosting the django frontend Formatting queries correctly for the LLM API (still struggling with this one but given the time we were allotted I think we did pretty well, we get the occasional JSONDecodeError, but I'm mystified on where it's coming from at this point) Some LLM hallucination Accomplishments that we're proud of Implementing live RAG using serpapi Having our LLMs respond to the user with links and context Putting all of this into a django frontend What we learned How to implement live RAG using search results How to use the requests library in python to prompt LLMs Building a django frontend using bootstrap4 Hosting django apps <div