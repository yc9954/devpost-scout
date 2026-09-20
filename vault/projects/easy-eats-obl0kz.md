---
slug: "easy-eats-obl0kz"
url: "https://devpost.com/software/easy-eats-obl0kz"
title: "Easy Eats"
hackathon: "AWS Graviton Hackathon"
organization: "Amazon"
winner: true
words: 452
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "user/small_business"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Easy Eats

> Launch your own self hosted ultra low maintenance food ordering platform in few seconds.

[Devpost](https://devpost.com/software/easy-eats-obl0kz) · hackathon [[AWS Graviton Hackathon]]

## Facets

**domain** [[labor_employment]]
**user** [[small_business]]
**substrate** [[geospatial]] [[structured_db]]

**stack** amazon-web-services, docker, node.js, notion-api, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for easy eats

## Body

Home Page Cart page Order Management through Notion Web App Menu Management through Notion Mobile App Inspiration Covid-19 brought tremendous change to the world. One of the biggest changes was in the way we work. While a lot of workers and businesses were displaced it also brought a trend of new businesses being created. One such business is food delivery. Food delivery is a great business to start from home with a low barrier to entry. The SaaS based enablers however charge fees as high as 30% of the order thus making it less lucrative for the business owners. We made Easy Eats to help these small business owners. What it does Easy eats is a self hosted solution that allows businesses to easily start their own online order taking platform where they can manage their menu and accept orders online. It's free to use, completely open source, can take hundreds of orders in a month and costs less than $3 a month to maintain using AWS Graviton compute instances. How we built it Built on top of Notion API serving as the backend and database for handling menu and orders, we used Vue and Nuxt JS to build middleware and frontend on Nuxt JS. Challenges we ran into Most of the challenges were around Notion API. We used this API due to lack of time in building a full fledge backend admistration area for the owner. The Notion API is currently incomplete which has prevented us from creating a 1-click bootstrapper for installing the server. The user now has to perform a few manual steps to start their store. The Notion API can always be replaced by any database or a proper CRUD app like Django or Laravel. Accomplishments that we're proud of We wanted to establish a few things which we were successful and proud of Notion API can be used as a database eliminating the need of spending tens of hours in building a custom backend for MVP End to End flow of users being able to see the menu and picking the items and their quantities to create a cart and order it The product can run on minimal specs like T4G compute instances What we learned We learned how to build a backend for a self hosted product on top of Notion API and deploy it using docker. We also learned how to build a product from scratch without spending a great deal of time on it. What's next for Easy Eats Fix any UI bugs Add some features like taking user's location on the map Replace Notion API with a hosted database like SQLite therefore packing the whole application into a small monolith docker container. <div