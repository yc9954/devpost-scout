---
slug: "re-space"
url: "https://devpost.com/software/re-space"
title: "Re:space"
hackathon: "Garuda Hacks 2020"
winner: true
words: 563
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/on_device_local"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/retail_commerce"
  - "substrate/geospatial"
---

# Re:space

> Finding the best location to grow your business has never been easier! Re:space offers a beautiful app that lets you find commercial spaces for rent and manage them in one platform

[Devpost](https://devpost.com/software/re-space) · hackathon [[Garuda Hacks 2020]]

## Facets

**mechanism** [[benchmark_measured]] [[on_device_local]]
**domain** [[finance_payments]] [[housing_homeless]] [[retail_commerce]]
**substrate** [[geospatial]]

**stack** docker, dockest, express.js, figma, jest, nextjs, openapi, postgresql, styled-components, typeorm, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- how to install & run
- challenges we faced along the way
- what we're most proud of
- what we learned
- what's next for re:space

## Body

Our Beautiful Landing Screen Actually forcing ourselves to write unit tests Oversimplified Architecture Story Behind Re:Space Inspiration One of the biggest disruptions the global Covid-19 pandemic has caused is towards offline retail. Many businesses have started closing shops due to piling rent thus opening up potential spaces for newer businesses to fill them once the situation gets better. We believe that times of crisis like this is the optimal time for disruptive marketplace solutions to come in and change how people find and promote spaces for rent in Indonesia. Commercial space marketplaces is important because often, business owners have limited access to information (One of our teamates has first hand experience when trying to expand his family business). We see that in the current landscape, the reason these marketplaces aren't working is because the platforms are not well maintained and not built to scale. With that said, we believe with the right code and user-focused design, we can provide significant value to SME's looking to start up or expand to new areas. Sure marketplace solutions aren't as sexy in 2020 as super smart AI bots or virtual reality games, but if it does solve a problem why not give it a shot? What it does Main Features Search for top available commercial spaces (Limited to malls in current MVP) Interactive maps to get a birds eye view of the mall / shopping centre Detail information regarding Mall and space Save spaces to Watchlist so you can view them easily (and scout for price drops!) Dashboard to trackand manage spaces you've rent How we built it Frontend Stack NextJS Typescript Styled Components Backend stack Express + Typescript Jest + Supertest PostgreSQL + TypeORM Deployment Docker Architecture How To Install & Run Re:space-service Running apps locally (development mode) Start DB service in docker with docker-compose -f docker-compose.test.yml up -d Run DB migration with npm run migration:run Start application with npm run start:dev Apps will be running on http://localhost:3000 Running test on local machine Start DB service in docker with docker-compose -f docker-compose.test.yml up -d Run DB migration with npm run migration:run Run test with npm run test Running test inside docker with dockest Run npm run test:dockest Re:space-UI Running apps locally (development mode) set environment variable $ export API_URL=http://149.129.63.34 run in dev mode npm run dev Build app set environment variable $ export API_URL=http://149.129.63.34 build app npm run build start app npm run start Challenges we faced along the way Coordinating effectively while remote (We manage to do it though 24 hour Google Meet Session) Designing the right backend architecture (We want to make sure our app is modular, testible, and scalable) Making interactive maps from scratch (Turns out you can do it with SVG tricks!) Making sure the backend and frontend team are in sync and aware of what each other is doing or needs What we're most proud of 70% TEST COVERAGE WE DID NOT HARDCODE IN A HACKATHON Tried our very best to always stick with the best practices What we learned Sometimes it is better not to reinvent the wheel When time is limited you need to learn to sacrifice features You CAN code for 36 hours as long as you have your friends with you Using Swagger.io and OpenAPI saves a lot of time and communication cost What's next for Re:space Chat feature Commercial space owner dashboard Payment System <div