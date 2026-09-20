---
slug: "serverless-bootstrapper"
url: "https://devpost.com/software/serverless-bootstrapper"
title: "Serverless Bootstrapper"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 647
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Serverless Bootstrapper

> Getting a taste of serverless was never easier. This project enables you to take your Postman APIs into a serverless world seamlessly with automated code stub generation and auto-deployment.

[Devpost](https://devpost.com/software/serverless-bootstrapper) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[web_dom]]

**stack** javascript, nimbella, postman, serverless, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for serverless bootstrapper
- how to use

## Body

Upload to Github API Upload to Nimbella API Inspiration We are a group of developers passionately focused on simplifying and enriching the developer experience with a mission for making cloud-native development for developers of all skill levels and not just experts. What we saw was that the developers spend a lot of time in infrastructure management therefore we created this seamless experience for a Postman developer where they not only mock, test, document their APIs but can also develop and run those APIs. No management of servers, no server application to run, just automatically generate shareable secure URLs of your Postman Collection with a single click. Development is a social activity, you have to involve all stakeholders. You can't code in silos and do it all alone. We have found API first development approach suits us best. We believe API comes first, then the implementation. But frequent iteration and sharing that perfect JSON on which all parties agree is again a difficult job. Owing to these two frequent and omnipresent challenges we undertook this project. What it does It deploys APIs in Postman Collection with a single click, you instantly get shareable HTTPS URLs returning example JSON data from the collection. They say the first step is always the hardest and for you, we make it as easy as a click. On another click, it creates a GitHub repository containing code stubs, unit tests, the dependency configuration file in the language of your choice (Currently we support Golang, Javascript, Typescript, Python, Java, Swift, PHP). Not only that, but the repository also contains the updated collection document and a readme with the collection description. How we built it We used Postman APIs to fetch and update the collections, Postman's open-source libraries to read, parse and extract the information from it. Generate code stub, unit tests, and other artifacts for the language of choice based on the handlebar templates. Nimbella platform to deploy the generated code stubs and Github repository to host them. Challenges we ran into Achieving cross-language functionality, generating unit tests, augmenting the Postman collection document with new tests and endpoints were difficult tasks. Accomplishments that we're proud of We can tell our fellow developers, "You focus on your APIs, your API is the first user interface and interaction for your application, and without you having to leave your Postman client, we make your APIs live, generate code stubs and host them on GitHub!" What we learned No servers, no worries. It's an entirely new set of emerging practices that eventually will change the way we build businesses. We are solely concerned about writing code. Not concerned about machines, operating systems, or the worries of distribution or scaling. In this event-driven approach. The code is not running and listening for some input but instead is initiated and executed by the event. We pay only when our code is running, and the cost paid depends upon the resources the code consumes. There is no payment for idle time or hosting. The environment in which the code runs is constructed in response to an event, code is then executed, and the environment deconstructed. No information can be passed between each function call by the environment it is running in. What's next for Serverless Bootstrapper Updating either collection or the project has to be synchronized, i.e. if one is updated manually the other one has to be updated dynamically. We'll work on and add another API for two way synchronization. How to Use Fork this Collection . Get your Postman API Key from the Postman Integration Dashboard . Get a Nimbella Auth Token from the Portal . If you're already using the Nimbella CLI Tool , you can do nim auth export to get a token Specify a Collection Name or GUID Click Send. Your APIs are live! You can also select Postman Action Environment and set values there. <div