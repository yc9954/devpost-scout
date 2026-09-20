---
slug: "stackoverflow-dev"
url: "https://devpost.com/software/stackoverflow-dev"
title: "StackOverflow (Dev)"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 346
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
---

# StackOverflow (Dev)

> Improving developers collaboration and effectiveness via providing them a collection which they can leverage to seek help and support the community in way easier manner

[Devpost](https://devpost.com/software/stackoverflow-dev) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]

**stack** google-cloud, javascript, postman, stackoverflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what's next for stackoverflow (dev)

## Body

Inspiration As developers we love summarized solutions and thoughts, we are lazy and we don't have enough time, also we are dealing with exceptions and unknowns every day. This inspired me to write a public collection which can be leveraged to chat bot / personal assistant to help developers quickly resolve their issues and help the largest Dev community - StackOverflow to grow. What it does It allows you to ask questions and seek for answers in StackOverflow by leveraging the google cloud search capabilities to find the most relevant questions similar to your query, show you only the best answers with high probability to help. How we built it Using Postman public workspace and the new visualize feature to create an embedded clickable web app inside Postman. Almost every request displays the data with Visualize Challenges we ran into The copy button from the visualize table was not straightforward to be built as navigator.clipboard is disabled and it's a bit hacky. Also window can't be opened from Postman. Other than that there were no major challenges. The google cloud key rotation was interesting and the error handling. And pretty much for the scope of my idea I was able to find a workaround in everything with the existing Postman functionality. Accomplishments that we are proud of I am proud of completing my initial idea - to provide summarized solution to any tech related question with higher accuracy. Also I would be proud if I am able to encourage the developers to help each other as I observed a trend where less questions were asked / resolved in the public community for the past two years. What we learned A couple of more hacks with Postman to overcome different limitations What's next for StackOverflow (Dev) For me as a full-stack developer this is pretty much enough. I can use postman and query my exceptions and issues/questions very quickly and get the summarized solutions. This can be built as MS Teams chat bot/ Slack chat bot and be the fist point of contact for every developer. <div