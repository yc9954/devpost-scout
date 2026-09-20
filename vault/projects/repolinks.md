---
slug: "repolinks"
url: "https://devpost.com/software/repolinks"
title: "RepoLinks"
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 383
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# RepoLinks

> RepoLinks is a graph for better collaboration. It connects developers and provides a window into an organization's technology stack.

[Devpost](https://devpost.com/software/repolinks) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]]

**stack** fast-csv, node.js, tigergraph

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what we learned
- what's next for repolinks

## Body

RepoLinks TigerGraph View Inspiration I work in an organization with several hundred repos. It can be difficult to get a big picture view of the technologies we use and the people that use them. Leveraging Git repo data in a graph database is a natural fit to grasp the bigger picture. What it does Repolinks starts with a Node.js script that takes in a GitHub organization name that it uses to export all the connected repos, contributors, and languages to a CSV file. A TG graph is then created for each new organization based on the global schema so multiple organizations can be supported. The CSV files are then mapped and loaded into the graph. Using the TigerGraph Explore and Query tools you can answer several questions: What programming languages and technologies are in use by the organization? What code repositories use those technologies? Who is contributing to those repos and how much? How are developers within the organization connected? Who is the best person to answer my question about a particular technology or project? What skills should I look for in new developers and where are my training dollars best spent? What do I have in common with other developers in my organization? How I built it I built the GitHub data export script in Node.js using the GitHub API and the "fast-csv" library. The graph was built in TigerGraph (of course 😉). Challenges I ran into I have never touched a graph database before so there was a bit of a learning curve for me. Daniel Barkus's TigerGraph 101 course on YouTube was super helpful. I quickly hit the rate limit on GitHub's API but was able to fix this by using authenticated requests which increases the limit from 60 requests per hour to thousands. Accomplishments that I'm proud of I super happy I got my first graph up and running and it is already providing interesting insights. What we learned I am completely new to graph databases so... a lot. I.e., vertices, edges, data mapping, etc. What's next for RepoLinks Unfortunately GitHub does not provide dependency information. I am interested to learn what libraries are being used by which repos so I would like to parse the project dependency info (I.e., package.json for Node.js projects) to reveal further insights. <div