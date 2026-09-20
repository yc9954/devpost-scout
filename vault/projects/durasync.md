---
slug: "durasync"
url: "https://devpost.com/software/durasync"
title: "DuraSync"
hackathon: "monday apps challenge"
organization: "Monday.com"
winner: true
words: 202
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# DuraSync

> Synchronize data from a remote API, SQL Server, MySQL, PostgreSQL, or MariaDB data source into your monday.com board.

[Devpost](https://devpost.com/software/durasync) · hackathon [[monday apps challenge]]

## Facets


**stack** python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for durasync

## Body

Inspiration We had a monday.com customer who needed to keep their board in sync with a legacy CRM that could only be accessed via SQL. What it does DuraSync allows you to pull data from a remote data source and make it available within a monday.com board. For example, pull in a list of products and their prices from your production environment, then include this in other boards using a Mirror column. Data can be pulled from a REST API with a JSON response, or any of the following SQL servers: Microsoft SQL Server, MySQL, PostgreSQL, or MariaDB. You can configure how often the data is kept in sync. How we built it We first built an MVP for the customer to self host in Docker. Then we rebuilt and productized the application to run for any monday.com customer who wants to pull it in from the Marketplace. Challenges we ran into We had to tweak design and UX to comply with monday.com requirements. We had to build out more features to support common use cases. What's next for DuraSync Support for more data source types More advanced API connection capabilities Ability to push data from monday.com into a remote destination <div