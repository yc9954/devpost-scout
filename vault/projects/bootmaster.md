---
slug: "bootmaster"
url: "https://devpost.com/software/bootmaster"
title: "Bootmaster"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 225
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# Bootmaster

> A public workspace to search API's compatibility for different frameworks .

[Devpost](https://devpost.com/software/bootmaster) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** h2, java, jsoup, springboot

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bootmaster

## Body

Inspiration I was learning an android application from web and then I tried to create an application for play-store , but The api-version on which i learn and the API-version which I was Targeting were different. I need to search the alternate packages available available for the Target version , update code and then deploy again to check if it works correctly. What it does This Workspace remove the repetitive "update code" part of the development . If the developer has an idea about the similar package name or classes/interface they can search a for all matching candidates . Developer can narrow the search by adding api-versions operations like "lt", "gt", "eq". How we built it I used spring-boot application as backend with H2 database. For Indexing the API database I have written different web-scrapping implementations with JSoup. Enterprises can use it on-premise by implementing their own framework indexes . Challenges we ran into Scraping pages is a big challenge. Accomplishments that we're proud of Completing the project in the timeline . Learning frameworks like JSoup. First live running project on Heroku. Subbmitting first hackathon successfully on DevPost. What we learned Usage of Postman pre-request scripts , test , monitor, Jsoup , web-scrapping What's next for Bootmaster Containerise the backend. Adding more frameworks to index . Checking compatibility for methods of classes and interfaces <div