---
slug: "time-estimations"
url: "https://devpost.com/software/time-estimations"
title: "Esti"
hackathon: "monday apps challenge"
organization: "Monday.com"
winner: true
words: 365
team_size: 7
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Esti

> Once again having trouble estimating time for a task you have no prior experience performing? Maybe someone else in your organization does have such an experience! That info is only one click away!

[Devpost](https://devpost.com/software/time-estimations) · hackathon [[monday apps challenge]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** fuse.js, lodash, react, styled-components

## How they structured the write-up

- inspiration
- what it does
- key features
- how we built it
- challenges we ran into
- what we learned
- what's next for esti

## Body

Inspiration Once again having trouble estimating time for a task you have no prior experience performing? Maybe someone else in your organization does have such an experience! With our Esti App, users can automatically compile a list of similar named tasks performed by all team members on their boards while providing them with all the statistical overview they need for doing a better job estimating their times. One of the most common challenges in project management is meeting deadlines and especially estimating times for various tasks. Team members are often required to estimate time for tasks under a great deal of uncertainty about the complexity of the task and the possible complications that will arise in the future. What it does Our new app helps users estimating the task's required time by displaying similar tasks that exist in the boards to which the user is subscribed. In addition, the same tasks will be concentrated in an accessible place and will allow faster access to consultation with people in the organization who have performed a similar task before. Key features Automatic targeted data. Filters the relevant results only. Prioritizing - better matches are weighted higher. Displaying calculated average and median of all results. How we built it Query up to 50,000 items across all subscribed boards. Search by selected Item name across all returned items. Sort by relevance. Return relevant items and their actual time. Calculating Average and Median of actual-time according to the numeric column containing the "Actual" keyword in its name. Challenges we ran into Monday API - querying data, complexity points Figuring out how to reliably filter and search for relevant items Performance tweaking Monday limitation on UI customization What we learned Querying data using GraphQL and the Monday.com API. We learned about features and integrations we did not know that exists on Monday.com Developing our own App on the Monady.com developers platform. What's next for Esti Optimization - Shortening loading time by search and sorting optimization as well as adding caching service. Filters - Allow users to choose which boards, columns, and team members they would like to include in their search. AI - Implementing NLP for even better results Statistics <div