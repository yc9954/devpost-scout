---
slug: "as-yet-unnamed"
url: "https://devpost.com/software/as-yet-unnamed"
title: "Covid-19 Alerts"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 298
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/civic_government"
  - "domain/labor_employment"
  - "substrate/video_visual"
---

# Covid-19 Alerts

> Get up-to-date Covid-19 information straight to Slack, with government policies and a graph of recent cases, all from a convenient postman collection.

[Devpost](https://devpost.com/software/as-yet-unnamed) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[civic_government]] [[labor_employment]]
**substrate** [[video_visual]]

**stack** postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for covid-19 alerts

## Body

Example Slack Post Example Slack Post with notes turned on Inspiration Covid-19 has affected us all in countless ways. Among other things it has had a deep impact on how we work with restrictions on when we can leave our homes, how we can travel, and when and where to wear a mask. With differing policies and levels of concern from day to day, it can hard to keep track of. What it does This Postman collection provides up-to-date Covid-19 information straight to Slack, including government policies and a graph of recent cases so you can be aware of any spikes in Covid-19 cases to help keep you and your co-workers safe. How we built it The collection uses Postman's setNextRequest function to make several API calls to the "Oxford University COVID-19 Government Response Tracker" to collate data from across the specified time period then uses a Slack webhook to post the data to a specified Slack channel along including a graph generated with image-charts.com free graph API. Challenges we ran into Working with the limitations of the Graph imaging APIs was challenging, but I was still able to show the desired information in a simple and meaningful way. Accomplishments that we're proud of Creating something that is not only useful to me but can be used to get Covid-19 updates by anyone with a slack channel or as an example of how to use Postman's setNextRequest function for anyone just starting out with Postman. What we learned Through this project, I have learnt how to effectively use Postman's setNextRequest function. What's next for Covid-19 Alerts The logic and functionality created in this Postman collection can now easily be replicated in a nodeJS application using crons to automatically send the alerts at the start of each day. <div