---
slug: "onewaysms-api"
url: "https://devpost.com/software/onewaysms-api"
title: "OneWaySMS API Collection"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 251
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# OneWaySMS API Collection

> Postman collection for Malaysia OneWaySMS API.

[Devpost](https://devpost.com/software/onewaysms-api) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]]

**stack** collection, node.js, npm, postman, workspace

## How they structured the write-up

- 💡 inspiration
- 🔩 what it does
- 🔧 how i built it
- 🤔 challenges i ran into
- 📙 what i learned

## Body

💡 Inspiration Since I've used OneWaySMS provider before, maybe I can create a Postman Workspace ( Collection ) that could be useful to other developers which use this service. 🔩 What it does A simple Postman Workspace and Collection which features the basic 3 core functions of OneWaySMS. By default, requests will route to my OneWaySMS mock server with tests included. 🔧 How I built it Based on the official API documentation by OneWaySMS, I've created a public workspace which includes a small collection of OneWaySMS API requests. The requests inside the collection are backed up with tests, in which should pass if baseURL is set to the mock server endpoint. 🤔 Challenges I ran into As this is my first ever Hackathon, I am a bit anxious on whether if I will build something useful for the community or not. Personally I've used Postman before, but only with limited knowledge on it (I didn't even know that Postman has variables to be frank). 📙 What I learned Throughout the event, I've learned the concepts of workspace, collections as well as mock server. I've also learned that runner can be automated with cli using newman . The GitHub repository in which the scripts and the iteration data is stored can be found here . This is a rather simple project. I am surprised that Postman can do so much more than just sending requests to a specific endpoint. I didn't even know that you can write tests in your requests! <div