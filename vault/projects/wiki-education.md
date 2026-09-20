---
slug: "wiki-education"
url: "https://devpost.com/software/wiki-education"
title: "Wiki Education"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 494
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Wiki Education

> This solution helps people from around the world have access to general information from Wikipedia without the use of data via the Facebook Free Basic Initiative.

[Devpost](https://devpost.com/software/wiki-education) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**user** [[educator_student]]
**substrate** [[document_pdf]] [[financial_record]] [[web_dom]]

**stack** docusaurus, facebook-free-basic, facebook-messenger, facebook-messenger-api, node.js, wikipedia-api, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that i'm proud of
- what we learned
- what's next for wiki education

## Body

DevC Wiki (wiki education) Nice logos Nice logos Our documentation homepage Inspiration We were inspired by what the wit.ai platform could do and how awesome it would be to integrate it with the Messenger platform. What it does This project helps Facebook users to have access to information from Wikipedia with or without having data on their mobile phone using the help of Facebook free basic initiative, the Messenger platform and wit.ai. How we built it Our solution requires five major things:- wit.ai platform/ API nodejs server Facebook messenger API Wikipedia API A facebook page Docusaurus (for documentation) The wit.ai platform would be used to train a model that selects the word to search for from an interrogative statement. A Facebook page would be created to allow users to interact with the created messenger bot (DevC Wiki) The nodejs server would be used to listen to chat event from the messenger bot that would be made. Once a question is asked by a user interacting with the bot on the DevC Wiki page, a message event is triggered on our server with details of the message. The Wit platform also provides us with an API that allows users to interact with the wit.ai platform via an HTTP request. We would be training the wit.ai platform to select words from the messenger chat which would be consumed by the Wikipedia API, we would also have to make a call to the wit.ai platform providing the message from the chat using the API and the returned response provides the selected keywords from the message. Once the response is returned we would make an extra call to Wikipedia using the Wikipedia API, the returned information would be sent to the user on Messenger using the Messenger API. If no information is found on Wikipedia the user is also sent a "not found" response. Challenges we ran into We had issues making our build public. Facebook pages policy requires that we submit some business document before a messenger bot can be made public. So to test it, please send me your Facebook username at sammychinedu2ky@gmail.com . This would help me to add you under the available test account for access. Accomplishments that I'm proud of We are proud of the Fact that we were able to create a chatbot that gives users answers to questions. And our solution is also accessible to people without data with the help of the Facebook free basic initiative. What we learned We learnt a lot about Natural Language Processing(NLP) using the wit.ai platform and also how to make a chatbot with the Messenger platform. We also learnt how to make use of another Facebook open-source tool (Docusaurus) to create a cool documentation website for our tutorial which you can find here docusaurus site What's next for Wiki Education We hope to be able to add more educational features to our solution, For instance being able to convert measurements in various units <div