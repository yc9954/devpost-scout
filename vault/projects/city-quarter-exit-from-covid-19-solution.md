---
slug: "city-quarter-exit-from-covid-19-solution"
url: "https://devpost.com/software/city-quarter-exit-from-covid-19-solution"
title: "UgoRound Community Alert Solution"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 802
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "domain/labor_employment"
  - "domain/media_journalism"
  - "user/general_public"
---

# UgoRound Community Alert Solution

> Divide the City into Quarters and set up a "First to Know" Group for each Quarter. The City can send hyper relevant alerts and information to workers and residents based on their anonymised location.

[Devpost](https://devpost.com/software/city-quarter-exit-from-covid-19-solution) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**domain** [[civic_government]] [[disaster_emergency]] [[labor_employment]] [[media_journalism]]
**user** [[general_public]]

**stack** couchbase, couchbase-lite, firebase, java, javascript, php, socket.io, swift, symfony, zeromq

## How they structured the write-up

- the challenge for our cities
- what it does
- what we demonstrate
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ugoround

## Body

Tap Group Pin to Join (anonymously) A Covid-19 Alert A Covid-19 Alert continued First to Know Groups in a City The Challenge for our Cities One of the most difficult and ongoing challenges that each City will face is how to get people back to work. According to Governor Mike DeWine of Ohio in a recent CNN interview “If people are scared to death, they not going to go out – how do we give people confidence?” Countries, Cities, and indeed Communities within the City have all been affected very differently. Our solution proposes a universal Location Based Alerting solution that works within Cities, around the Country and then between Countries (In the EU). What it does We deploy a Web Based platform that enables City Authorities to send localised Community alerts to their City Quarter First to Know Groups. People download the app and cannot register - they are totally anonymous . They can then join multiple First to Know Groups, be it representing where they live or work, and then can receive alerts and updates from authorities instantly. This will be an invaluable tool to manage people as they come out of lock down. It will allow authorities to inform about localised restrictions and then slowly relax these as they become more confident. It will also allow authorities to send targeted Community alerts where they need to update the situation, for example if movement or place restrictions need to be reinstated. It will enable Citizens to receive trustworthy instructions and advice. It will be a reliable Community safety alert system, without the confusion (and misinformation) now rife on social media. What we demonstrate In the video we demonstrate how easy it is to set up First to Know Groups for City Quarters. A City Quarter can be be situated by municipal boundaries, or any other natural and obvious area. People are associated by living in, working in and/or visiting a City Quarter. We then demo a scenario where a Citizen visiting a Supermarket has been discovered to be infected. Now City officials must advise all people that could have visited that Supermarket. The quicker the information is disseminated and to the affected area - the quicker Citizens can take the appropriate action. How we built it We developed a web based platform using PHP & JavaScript and integrated the Firebase API. We developed our own proprietary geofencing logic that requires no personally identifiable information (PII) from App users. Challenges we ran into We had to come up with a way to use Location services on the mobile phone that does not require the user to allow location to run in the background. Whenever you are using GPS in the background you are draining the battery. Our solution does not require users location to run continuously and indeed we state less than 1-2% of the battery will be used over the whole day. Accomplishments that we're proud of We wanted to ensure a single alert can be sent in multiple languages. We came up with a unique method that allows the Admin to send a single alert in as many languages as they choose. The app user can tap the alert language icon to select their preferred language. What we learned We have discovered that you can easily deliver vital information and updates to a user based on their location - anonymously. Traditional methods such as SMS, Social Media and email all require the user to register and give away personal data. This is the generally accepted methods as how critical communication is disseminated. We asked why? And can we do it where the Citizens are totally anonymous to us and the people sending alerts. The answer was YES! What's next for UgoRound Our solution is ready and can be deployed in Cities. All places must manage the re-opening of their locality in coordination with authorities. Both the City and the Municipalities within need to be able to send alerts to the Community. We developed our system so there is a hierarchy that gives authorities in the (City) access while still allowing the local (Village/Town) "alert originator" to send out community First to Know alerts. It needs to be managed at the village or municipal level because each place is different and local mayors/leadership and health authorities are ultimately on the ground. In addition there are many other use cases such as Security, Evacuations, Weather and other public safety concerns that can benefit the City/Country once the system is being used. At this time there is no universal alerting methodology across Europe - each Country implements their own system. We have built UgoRound to work anywhere in the World. UgoRound is a universal Safety App that will create a secure and trusted source of information for any public safety situation. <div