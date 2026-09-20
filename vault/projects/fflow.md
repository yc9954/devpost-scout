---
slug: "fflow"
url: "https://devpost.com/software/fflow"
title: "FFLOW"
hackathon: "Formula 0001: Rapyd Fintech Grand Prix"
organization: "Rapyd"
winner: true
words: 724
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
---

# FFLOW

> With FFLOW you can make complex financial applications, without using code. Instead, you represent your application in the same way you think about it, all this by using visual scripting.

[Devpost](https://devpost.com/software/fflow) · hackathon [[Formula 0001- Rapyd Fintech Grand Prix]]

## Facets

**user** [[developer]] [[general_public]]
**substrate** [[code_repository]]
  <sub>weak: web_dom</sub>

**stack** express.js, mongodb, node.js, pm2, rapyd, sendinblue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- technical demo
- what's next for fflow

## Body

Website Flow Editor Usage example inside Rapyd's Client portal Inspiration I co-founded a fintech startup called Growishpay in Milan about 8 years ago, and since that, I have been designing many complicated financial solutions for many companies, small and big here in Italy. But no matter how wildly different the financial applications were, it always goes like this: business or management conceptualize the flow, and then it goes to the engineering team that writes the code that makes the idea a reality (IDEA-->CODE-->REALITY). And this is true not only for my company but for any type of IT entrepreneurial endeavor. I had this vision of going from IDEA to REALITY right away about 2 years ago, heavily inspired by other industries [1] that are using Visual Scripting [2] to create complex flows without using code, allowing non-technical people to develop complex applications . What it does FFlow Ninja is a service for creating financial flows that works by dragging and dropping blocks that describe the application in terms that make sense for humans. If you can draw your application on paper, chances are you can build it and deploy it with FFlow without writing a single line of code. When you are done designing your application, the FFlow engine takes care of running it in the cloud, supported by Rapyd's API ( Collect, Wallets, and Disburse ). The user does not have to worry about all the nooks and crannies associated with creating a financial application, like concurrency, queues, security, idempotency, and many others, everything is handled by the FFlow engine. All of that works as a standalone product (SAAS), or it can also be easily embedded inside another product that wants to give its users the ability to consume their services using visual scripting. Imagine this inside the Rapyd Client portal! How we built it Using state-of-the-art tech, and techniques that I mature in the past decade of working in fintech. Essentially the whole application runs in 2 NodeJS processes (that can scale horizontally). If you want to get more into the technical details, please take a look at the Github repository Readme Challenges we ran into When you create something that allows people to build anything, it means that it can break in infinite scenarios 😅, since the user can connect the blocks in many possible ways, there are for sure combinations that I did not anticipate that break the application, not necessarily because of user's mistake. So the challenge was especially in the last week of developing since the more features I added to FFlow, the more ways the service could fail. Accomplishments that we're proud of Having a stable MVC to show. Even tho it is an alpha, I'm very proud of what I was capable of doing in just a month, in part due to how relatively easy it was to implement a client for the Rapyd's API. Just look how beautiful it is 🥰: https://fflow.ninja (PS: You'll need an invitation code or a demo account to access it, please take a look in the repository Readme) What we learned Rapyd was a service that my company was looking into early this year, to understand how it technically works and it's potential in our products. Because of it, this contest was the perfect opportunity for me to take a deep dive into the documentation and trying to build something that works because I'm a firm believer that you learn fast by doing. Now that I learned exactly how it works and its potential, I can see a future in which both companies can work together. Technical demo Check the Github repository for more information on how to access the public demo What's next for FFLOW Making the engine more stable Adding third party blocks (Salesforce and other CRMs integration, Analytics services, etc) Adding support for more Rapyd functionalities, countries, and currencies exchanges (FX). Notes [1] Companies allowing non-technical people to create complex applications: Marketing automation: GetResponse automation builder CRM automation: Salesforce Flow builder Interactive Voice responders: Twilio Studio Videogame development: Unreal Engine Blueprints [2] Visual scripting is a type of programming language that lets humans describe processes using illustrations. Whereas a typical text-based programming language makes the programmer think like a computer, a visual script lets the programmer describe the process in terms that make sense to humans. <div