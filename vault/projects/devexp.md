---
slug: "devexp"
url: "https://devpost.com/software/devexp"
title: "DevExp"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 451
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# DevExp

> The Developer Experience is always reflected in the final product

[Devpost](https://devpost.com/software/devexp) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** dgraph, gcp, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for devexp

## Body

Inspiration Having spent quite a significant amount of time working with Cloud Native technologies and the GraphQL ecosystem as a full stack developer for my startup, I do realize how important the developer experience is for all along with the importance of automation in every workflow. This collection aims to bring the same to the table by demonstrating few ways in which devex can be made even better What it does The collection is a set of multiple folders each catering to a specific use case some of which includes working with GCE VMs, administrating Dgraph which is a GraphQL native Graph database by doing various operations around it, searching through code, issues and articles, getting the latest developer news and more. How we built it These are some of the things we did Created Team/Workspaces Created collections Created Environments to store variables Added collection scoped environment variables Added Google, Github OAuth2 authorization in addition to APIKey based authorization for some Used a socks5 proxy for making all requests. Since postman does not support socks5 directly, we used the npm package hpts to help us in forwarding requests through a proxy Used File (binary) request for Updating Dgraph schema Sent GraphQL requests to do Database admin operations Documented all the collections Added a monitor to help us monitor the health of the Dgraph database periodically NOTE: You will need to update the environment variables with your appropriate credentials before you can start using any of the APIs Challenges we ran into I had difficulty with making postman work with Socks5 proxy since there is no direct support. So, I used hpts npm package to help me out with this. I had trouble in understanding the difference between the Web User Interface and the Postman Desktop interface since I was more used to the desktop version but got used to it now. I wanted to setup variables scoped at the request level (and not collection or environment level). But I don't think that is supported currently in Postman Accomplishments that we're proud of Finally got to know how to setup monitors and write docs in Postman Able to use the collections in lot of my workflows to speed up stuff What we learned Setting up monitors Writing docs Using the Web UI Proxying postman requests via Socks5 proxy Doing OAuth2 via postman (I used to manually hardcode the token everytime before this) Scoping collection level environment variables What's next for DevExp Incrementally add more APIs to all the collections including more APIs which I personally use to automate a lot of my workflows. I hope it can help others as well. Use all of these learnings for my startup as well <div