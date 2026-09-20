---
slug: "staticlink-immutable-static-sites-deployments-in-postman"
url: "https://devpost.com/software/staticlink-immutable-static-sites-deployments-in-postman"
title: "StaticLink - static sites deployments in Postman"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 222
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/transportation"
  - "substrate/geospatial"
---

# StaticLink - static sites deployments in Postman

> StaticLink is a set of simple API to deploy static websites and it can be easily used within the Postman workspace. It also supports multiple version previews for a single site.

[Devpost](https://devpost.com/software/staticlink-immutable-static-sites-deployments-in-postman) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[transportation]]
**substrate** [[geospatial]]

**stack** firebase, next.js, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for staticlink - static sites deployments in postman

## Body

Inspiration Static site generation tools have been trendy. Multiple version deployments have been made popular by platform such as netlify. I want to explore this model and build an easy open source alternative completely running on serverless platforms. What it does StaticLink is a set of API where you can create a static site and publish multiple versions of the site easily. How we built it The Next.js server handles all traffic, which can be easily deployed on Vercel serverless platform. All files and related data are stored in firebase powered by google cloud storage and firestore. Challenges we ran into I need to hack Next.js a bit to make the routes work. Accomplishments that we're proud of The service is quite easy to deploy with only several commands. Running completely on serverless platforms also means it is easier to scale and costs much less. What we learned Building serverless service is quite different. There is much less abstraction compared to using a web framework. It's my first time to use a postman workspace, which help debug the serverless request body. What's next for StaticLink - static sites deployments in Postman Support deploying with aws lambda and google cloud functions DNS & CDN integration support Easier ci/cd integration, such as Github action and circle ci Token management and multiple users support <div