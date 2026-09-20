---
slug: "mongoql"
url: "https://devpost.com/software/mongoql"
title: "MongoQL"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 313
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# MongoQL

> Manage your CRUD database operations from the client-side, using one endpoint express middleware with the compatibility for other middlewares and logic of the express app.

[Devpost](https://devpost.com/software/mongoql) · hackathon [[The Postman API Hack]]

## Facets

**user** [[general_public]]
**substrate** [[geospatial]] [[structured_db]]

**stack** express.js, heroku, mongodb, mongoose

## How they structured the write-up

- introduction
- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what's next for mongoql

## Body

example of options Introduction Hello me dear reader. I would like to mention that the current project is the concept of the great idea to manage CRUD REST API from one endpoint . Inspiration Nowadays, maybe 95% of all platforms use API as their main business logic solution. But we have to create a lot of endpoints and maintain them. It's quite repetitive, moreover, the greater part of them is a CRUD operation for the database. We have a good solution GraphQL for making requests more flexible. But, is a totally different approach and could be difficult for the configuration. We need something as good and powerful as GraphQL for our REST APIs models. What it does The solutions consist of express middleware, so it could be used very flexibly with the whole express project. The idea is to handle the CRUD operation for the database only with one simple endpoint. And manage these operations from the client-side part of a project. Providing the option to another middleware to be passed, like authorization and role-based permissions. I used the No-SQL database MongoDB, so I called the project MongoQL. How we built it I have used an express project to create an example, that could show the basic use cases. However, this project can be better and cover much more situations. The example project is deployed on Heroku and the example routes could be found in the public workspace . Accomplishments that we're proud of As I mentioned before, this concept could evolve into something really powerful for the development teams, maybe even replace the existing GraphQL way. What's next for MongoQL I'm going to use this approach in one of my projects, so I will continually improve it. For now, I'm going to use it for express + MongoDB combination, but in the future, it could be replicated for other tech stacks. <div