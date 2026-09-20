---
slug: "jirio"
url: "https://devpost.com/software/jirio"
title: "Jirio"
hackathon: "Devs Unleashed"
organization: "Atlassian"
winner: true
words: 431
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/education"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Jirio

> Mario game for Jira - get a break for an old-school game revival!

[Devpost](https://devpost.com/software/jirio) · hackathon [[Devs Unleashed]]

## Facets

**domain** [[education]] [[supply_logistics]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]]

**stack** forge, javascript, jira, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for jirio

## Body

Inspiration Unlike many established or well-planned in advance projects, Jirio was invented after learning about this hackathon. I wanted to practice my frontend skills, and this looks like a great opportunity to do so. What it does I hope all of you have at least heard of classic Mario brothers game. Jirio is a revival of Mario game targeting Jira platform. The main idea is simple: resolve the issues and get an opportunity to play old-school game with new design as a reward. How we built it Jirio was built using React for frontend part and @forge packages for "backend". It relies heavily on Jira API-provided data and regulates levels complexity and profitability depending on issue importance and quality metrics. Challenges we ran into The first challenge was developing a somewhat reliable level generator that creates maps which are not way too simple, but still playable. An article from 2011 presented great comparison of several algorithms so that we could pick the best of them for us. The second challenge was related to VCS integration. Apparently Jira does not expose any APIs that can help fetch PR and commit information in an adequate way. There are a few solutions on forum and StackOverflow, but none of them seem to be actual: they mostly use internal/private API which doesn't work with OAuth2 scopes. The issue page uses GraphQL endpoint for that, and I even believed that this is solution for some time. However, my GraphQL query works well in explorer, but is impossible to integrate into application. The reason is that required scope jira:atlassian-external is still beta and is not accepted in manifest.yml as part of production application. Accomplishments that we're proud of First of all, I'm happy that it works at all: my React experience is far from 5 stars. The application even doesn't freeze, so I think things are not as worse as I expected. The main real part of project I'm really proud of is the overall design. The monsters are cute, and this is surely the way for people's hearts. What we learned This project served as a good step towards React proficiency and overall hands-on frontend development. I never used atlassian UI packages, and they were a nice surprise: well-thought components which fit the common atlassian products design. What's next for Jirio Catching all bugs - I'm sure there are some. I also have plans on adding flying monsters to make them more distinct. Also playing with level generator to improve it further looks promising: for example, monsters are currently falling from the platforms too often. <div