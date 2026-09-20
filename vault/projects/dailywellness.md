---
slug: "dailywellness"
url: "https://devpost.com/software/dailywellness"
title: "DailyWellness"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 371
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# DailyWellness

> Wellness is much more than absence of sickness, but learning to prevent them and cultivating healthy living. This API delivers wellness and health tips every single day of the year

[Devpost](https://devpost.com/software/dailywellness) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[mental_health]]
**user** [[developer]]
**substrate** [[structured_db]] [[web_dom]]

**stack** firestore, go, heroku, mux, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dailywellness

## Body

Daily Wellness, treat yourself all through the year. How DailyWellness tips appears in a Slack channel Inspiration According to Stack Overflow Developer Survey 2020, 1 in 5 Developers are said to have a mental health and differences - memory disorder, concentration or emotional disorder. Much more than ever, developers must take responsibility for their mental health and wellness. We were thinking of way to help developer learn productive health tips consistently that could help them develop a productive and healthy lifestyle. This will include eating a healthy diet; making exercise enjoyable and a part of your life, and making decisions that will actively improve the quality of their life. What it does This API delivers a very concrete, relatable and action triggering tips , one per day to your channel or your chat room( Slack, Skype, Teams) How we built it We gathered wellness tip from Wealth 365 , From the University of California, Berkeley Wellness Letter called Wellness 365 and converted them into a Json Format, we used the API to load them into a Cloud FireStore using Postman Runner We then we use Postman Monitor to Send one request per daily. Challenges we ran into Getting the data into Json format was very challenging , but once this was completed. We used Iteration Data in Postman Runner to load the 365 tips for the year into the database via the API. Accomplishments that we're proud of We used mock server in Postman, Pre-Request Script , Test Runner and Monitor. We also built the API with Golang- production ready , deployed to Heroku with CI/CD pipeline , created and published the postman collection and a Monitor that runs everyday . This monitor alone is enough to deploy your daily tip to slack for any developer team. We achieved this by using a Pre-RequestScript to get the Tip and the Send in a Post Request to the Slack webhook Url. What we learned Use of PostMan Monitor, Mock Server, ,Pre-Request Script, Google Firestore with Golang . What's next for DailyWellness We will open source this API and accept more contributors . Integration will be done with discord and Microsoft Teams so dailywellness can be made available on those platforms too. <div