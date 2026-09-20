---
slug: "travel-info"
url: "https://devpost.com/software/travel-info"
title: "Travel Info"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 719
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Travel Info

> Get information on interstate public transport in Nigeria

[Devpost](https://devpost.com/software/travel-info) · hackathon [[Azure AI Hackathon]]

## Facets

**substrate** [[structured_db]] [[web_dom]]

**stack** azure, azure-luis, django, heroku, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for travel info

## Body

Inspiration Recently, a member of our team has had the need to travel quite a bit. Usually familiar with where he's traveling to and how to get there, with new places, he had the problem of not knowing how to go about it. And by go about it, we mean where to find public parks/terminals/garages to get buses that travel to his desired destination. Also, it would seem other people have the same problem too, cause on two occasions around the same time, friends asked similar questions: What it does The usual conversation goes like this: Traveller : I'm going to X state. I am currently in Y state. Where do I get a bus going to X state? Response : Check Z terminal in Y state. I know they have buses that go there. (plus any other relevant information). And so was an app/product conceived: let's crowdsource information on public transport in Nigeria, organize and make it available. Availability here is going to primarily be through a chatbot. With a search engine-indexable website to come. How we built it There are three parts to the product: data entry, query resolver, and data retrieval. Data entry This component of the problem will make it possible to enter information you know. It is highly doubtful that one person has travelled to all states through all terminals. So, it is important to be able to collect information from various people. For example, a person travels by train to a specific state. They can enter information about that journey through this component, making it available to the resolver. Query resolver This part of the app pieces together information to make it useful. For example, (when we sufficiently improve the product), a user can ask "what is the fastest way to get to this state from this state?". The fastest means of transportation is by air. But what if a particular state does not have a functioning airport or there are no direct flights connecting those states, it would be the job of the resolver to respond "you can take a flight to X state, and then board a bus from Y terminal to your destination". This query and response, though, is done via API and JSON. This leaves the job of parsing structured info into a formatted response, to the data retrieval component of the product. Data retrieval There are various ways to make collected information available to a user, two of them are in focus for this project: a chatbot and a browsable/searchable page. One of these methods, the chatbot, was worked on for this hackathon and is what is being showcased. Challenges we ran into Regrettably though, for the sake of time + complexity constraints, the chatbot is only able to answer a particular type of query: "tell me about terminals in X state that travel to Y state". That was one challenge. The other major challenge was collecting information from knowledgeable travelers. And as with any crowdsourced dataset, attention still has to be paid to accuracy and detail. Accomplishments that we're proud of Even though the product had been conceived before the hackathon, designing and implementing only started a few days into the announcement of the hackathons. So, we really do feel proud that we were able to pull it off. Getting familiar with Azure services, frequently deploying and testing to get the hang of it, collecting information, and altogether making things work as a team. We're really proud of that. What we learned It is apt to say that the process, alone, of building a project, whatever it is, holds new knowledge and skills to achieve. We did a lot of that: unlocking new knowledge and skills. This includes: making available and connecting databases across different applications deploying as well as managing config across apps (almost like in a microservice environment) building bots with Azure's cognitive services collecting and cleaning crowd-sourced data What's next for Travel Info The product is only in like v0.0.1. There is so much left to do. We would improve the chatbot, adding several more intents and abilities. More varied data will be collected and organized, like travel time, prices, etc. The query resolver, in its simplistic state, will be drastically improved. All these things and more will go into improving the app. <div