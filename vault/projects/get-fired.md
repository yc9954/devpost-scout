---
slug: "get-fired"
url: "https://devpost.com/software/get-fired"
title: "Get FIREd"
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 494
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "user/educator_student"
  - "substrate/web_dom"
---

# Get FIREd

> With our FIRE (Financial Independence Retire Early) calculator you'll be saving time and money! Get FIREd shows its users directly how much their spending or saving changes their FIRE date.

[Devpost](https://devpost.com/software/get-fired) · hackathon [[HooHacks 2021]]

## Facets

**domain** [[education]] [[finance_payments]] [[housing_homeless]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** domain.com, fastapi, gcp, google-app-engine, google-cloud, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for get fired

## Body

Wireframe mockup of the front end Get FIREd Inspiration The American dream has long been intertwined with financial independence. There are many Financial Independence Retire Early (FIRE) calculators on the internet but this project set out to be able to demonstrate how individual categories of spending can have significant impacts on career length. It's easy to come to the mindset that an extra few hundred dollars on rent may not matter but Get FIREd helps users understand how their spending affects their future. Get FIREd hopes to support college students that are graduating and entering the work force as they take a big leap in financial literacy. What it does Get FIREd lets the user input their annual income and expenses and calculates how long they must work until they can retire. The website also lets users take more granular control over parameters such as withdraw rate and retirement spending. If a user wants to get even more detailed they can break their spending down into a monthly budget which allows the site to demonstrate how each category affects their FIRE date and allows the user to test how changing the categories would affect their career. How we built it The front end is built using React and is hosted on Google App Engine in GCP. The front end takes the users input and makes asynchronous calls to the API which does the heavy lifting. The API is also hosted on App Engine and is written in Python using FastAPI. Most of the financial functionality was implemented using the numpy-financial Python library. The website was designed to work with minimal user input for quick feedback but also allowed more detailed user input if desired. We opted to not implement user accounts as storing financial information brings many security risks. Challenges we ran into React was something David was somewhat familiar with but still took up the biggest section of our time. It is a great library with lots of functionality but it still took time to understand. The back end did not give any surprises thankfully as it was all stateless and relatively straight forward. Accomplishments that we're proud of David: How responsive the website is due to its asynchronous calls. Josh: The API worked quickly and smoothly and was deployed to a cloud platform. What we learned David: React and Flex boxes Josh: FastAPI and Google App Engine What's next for Get FIREd Get FIREd accomplished our main goal that was set out at the beginning of the hackathon. There are a couple more graphs that we would like to have implemented that would give more information to the user. The major path forward would be to setup user accounts and integrate with banks using Plad to pull a user's actual spending. This would require a significant effort towards securing the website and the user data but would greatly reduce the required effort from the user and would removes any guess work. <div