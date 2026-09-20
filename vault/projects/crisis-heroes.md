---
slug: "crisis-heroes"
url: "https://devpost.com/software/crisis-heroes"
title: "Crisis Heroes"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 267
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/elder_child_care"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Crisis Heroes

> A free community platform enabling the sharing of services and resources to ensure no one is left stranded.

[Devpost](https://devpost.com/software/crisis-heroes) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[elder_child_care]]
**substrate** [[geospatial]] [[structured_db]]

**stack** algolia, elixir, phoenix

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for crisis heroes

## Body

Inspiration I came home from a holiday and was forced to self isolate for 14 days. Luckily I had a friend in my apartment building to buy me groceries - but I started wondering how people would do it if they had no friends nearby. This would be made worse if you're elderly and don't want to risk contracting the virus. What it does Crisis Heroes allows you to signal for help or offer help in your community. You specify your location, pick a radius (eg. 2km) and then can view all help requests or offers to help in your area. If you want to help someone the platform allows you to send a message. Only your first name and suburb is shared with people to protect your privacy. How I built it I built it in elixir using the Phoenix library. The maps stuff is utilising Googles API. And search is handled by Algolia. It's hosted on Google Cloud Platform - App Engine flex and uses Postgres as the database. Challenges I ran into Getting the UI right - people were a bit confused by the dashboard. This is mainly due to there not being many people on the platform yet so it appears empty. I've since improved the UI. Accomplishments that I'm proud of I built in a week and after releasing now have over 140 users in 2 days - 70+ of which have offered to help others. What I learned Keep things simple. What's next for Crisis Heroes Just get it out there. Learn from feedback and implement a better onboarding process. <div