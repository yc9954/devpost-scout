---
slug: "pokeguide"
url: "https://devpost.com/software/pokeguide"
title: "Pokeguide"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 535
team_size: 3
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Pokeguide

> FIRST EVER public transportation navigation app that guides people not to get on / off the bus stations or transit at stations where have Covid-19 cases nearby, so reduces the chances of infection

[Devpost](https://devpost.com/software/pokeguide) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[civic_government]] [[health_clinical]] [[transportation]]
**user** [[general_public]] [[patient_family]]
**substrate** [[geospatial]] [[web_dom]]

**stack** java, johns-hopkins-university-hub, machine-learning, natural-language-processing, objective-c, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for pokeguide

## Body

Inspiration In Hong Kong, many people get infected by Covid-19 just because they are waiting for buses together at the bus stop. As Pokeguide app does all public transportation routing ourselves using our APIs, and there are lots of open data source in Hong Kong (Government Open Data website) and worldwide (John Hopkins CSSE) telling exactly which location got Covid-19, why don't we just simply exclude these places in our search engine and walking path engine, then we can generate results that exclude all these things, and therefore reduce the chances people get infected just because they are waiting for public transportation, transiting or on the way home. What it does We are a public transportation navigation app that like others, but we are the FIRST EVER one providing transportation routes to our users that will skip all Covid-19 reported cases (e.g. patients' home, previously stayed places, hospitals and clinics), so that the users won't get on or off bus stops or transit at stops that are nearby the high risk places. Our walking path showing how to go from the bus stop to the destination also skips these places, so that it can highly minimize the risk of getting infected. This is extremely for crowded metropolitan like New York, London, Hong Kong and others where they are the serious outbreak places. How I built it Pokeguide already do the public transportation routing ourselves, so we need to get the open data sources such as Hong Kong government and Johns Hopkins CSSE to get the location of cases and then we can put these points in our routing calculation (public transportation and walking path) to generate results that escape from these places. Challenges I ran into Not many countries have open data of these Covid-19 locations. So far some data sources only have details down to city level, not even street / block levels. As a result, we are now crawling different sources of news to try to read, comprehend, extract location details and guess the locations from the articles if relevant. We are waiting for the approval from iOS App Store and Google Play Store, but they are very slow and reluctant on approving such app because they only allow official government apps to disclose Covid-19 information, which is awful. We are looking for other ways for users to search. So far public transportation data we only cover Hong Kong, Macau and Taiwan, while walking path routing is applicable to the whole world. We are going to add more public transportation data if we have volunteers helping us to plug in public transportation of their locations. Accomplishments that I'm proud of We are the first ever app to this and out-beat Google Maps again, after our AR navigation in 2018! What I learned Performance bottleneck takes long time to solve because on-the-fly omitting transportation nodes and walking nodes are tough and time-consuming before doing correct optimization. What's next for Pokeguide We are going to include more places that have exact latitude and longitude of Covid-19 cases like the US (Johns Hopkins CSSE) and Hong Kong, also include more public transportation for places that have serious Covid-19 issues, such as New York and London. <div