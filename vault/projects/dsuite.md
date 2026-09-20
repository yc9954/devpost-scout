---
slug: "dsuite"
url: "https://devpost.com/software/dsuite"
title: "dSuite"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 558
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# dSuite

> dSuite is multi-platform include dForm, dEvent, dMessage, dCalendar and more

[Devpost](https://devpost.com/software/dsuite) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets


**stack** assemblyscript, nextjs, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dsuite

## Body

Inspiration With the continuous development of web3 storage, opening up an infinite possibility in the data mining process, Information security, as well as distributed information management, is an absolute necessity. We are inspired by google form's gSuite product, Design dSuite with the mission of decentralization as well as maximum security of users' information, When using dSuite, you will not need to worry about your data will be illegally collected, as well as geographically unlimited interoperability is the strength of dSuite. What it does dSuite is a set of web3 applications that include dForm: allows users to create forms that collect questions, evaluations, or anything from the participants dEvent: allows users to post their events, raise funds or promote any content they want dCalendar: allows users to manage their events in the most efficient way All of the above applications take full advantage of the power of web3, ensuring transparency as well as high security How we built it We completely separate the construction of dSuite into 2 main parts Contracts, And UI. As for the contract, for some reason, we chose assembly script to build the dSuite contract. dSuite contracts are organized according to a pure MVC pattern project structure. Consists of a set of Controllers that handle user requests, abstract models that support interactions with entities in the system, and system on-chain storage to store them. In the other hand, UI development is also a challenge when we apply NextJs to dSuite development, Nextjs gives us strong customization ability with relatively simple configurations, However with the separation of Server -Side Rendering and Client-Side Rendering, which we had to fiddle with to be able to interact with Near API JS. Challenges we ran into During the development of dSuite, we encountered quite a few problems with the storage mechanisms of the NEAR Protocol. Optimizing between the amount of data to store and the ability to satisfy the user experience is an extremely difficult thing. Unlike web2, they have an extremely powerful backend system to be able to process data before sending it to users, when working with NEAR Protocol, we have to separate this process into 2 stages including normalizing the data before it is sent to the client from the contract and process the data displayed to the user. Accomplishments that we're proud of In a short period, we're proud to be able to bring three web3 apps to everyone. Although they are still in the process of being completed, however, through dSuite, we want to demonstrate our self-mastery in technology as well as our desire to contribute useful products to the community in the future. What we learned Through this MetaBUILD as well as our development of dSuite, the most we have learned is how to run an organization. Our team members all have their own lives, We can only work together every evening, discuss and come up with solutions to work together, A good combination will bring the perfect application. What's next for dSuite The fact that we chose the name dSuite also contributes to its future development of it. Shortly, we hope to have more members from the community participate in the development of dSuite with a huge number of dApps, bringing maximum utility to users. In addition, we are also planning to develop some interesting products this summer such as dNote dMessage <div