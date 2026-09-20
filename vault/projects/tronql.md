---
slug: "tronql"
url: "https://devpost.com/software/tronql"
title: "Tronql"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 302
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Tronql

> We need api for different Tron projects. We try to provide faster and better api calling

[Devpost](https://devpost.com/software/tronql) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**mechanism** [[realtime_stream]]

**stack** apollo, fastapi, graphql, kubernetes, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tronql

## Body

Documentation for the api Run graphql query Run graphql query Inspiration Graphql is one the newest standart of the api. It is faster, use less bandwidth, better for clients. We decide to provide that for Tron as well. What it does Project allow to use graphql technology to query tron api. Graphql was developed by Facebook, is heavily used by many api providers(gitlab, netflix, etc) Advantages of the graphql vs rest You can select only that data that you need You can make several queries in one response, so it will be faster if you need a lot of queries You can use subscriptions(this is websockets) for data In many js libraries you can have more strict types, and compiler will show error if types does not match So in general graphql allows you to reduce latency, bandwidth, speed of the requests and have more strict types. It is microservice ready, I can add a lot of microservices and they will have only one endpoint. All data could be queried using that endpoint. How we built it We build it with apollo router, fastapi, tron full node and kafka. Challenges we ran into Run custom node for tron. Accomplishments that we're proud of Finally we did it, What we learned A little bit of java, learnt tron node api, a lot of things that are related to cryptocurrency and tron in particular. What's next for Tronql A lot of different plans. run ecosystem from tron mainnet(currently for nile testnet) Support more queries and mutation from tron node api support webhooks/subscriptions in graphql adding ability to subscribe to particular address and get webhook notifications. That can be usefull for online shops added stats for using api. Allow to add api key for users, make some plans (free and paid) for api users. <div