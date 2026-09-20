---
slug: "near-smart-events"
url: "https://devpost.com/software/near-smart-events"
title: "NEAR SMART EVENTS"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 450
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/educator_student"
---

# NEAR SMART EVENTS

> No-code solution to listen and process on-chain events. It's an Integration Platform As A Service that can be embedded into Pagoda Console or run stand-alone

[Devpost](https://devpost.com/software/near-smart-events) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**domain** [[finance_payments]]
**user** [[educator_student]]

**stack** coinmarketcap, express.js, mongodb, near-api, node.js, pm2, sendinblue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- open source and embeddable
- what's next for near smart events

## Body

Check if deposit is over 1000USD and notify the compliance team NSE concept inside Pagoda console Notification over Telegram Notification over Email ❗️ Technical demo video https://youtu.be/IQ76AY2issw Open alpha site : https://nearsmart.events For accessing the alpha you need to use the demo account ( email: near@test.com password: Pagoda1. ) or create a new one using the invitation code nse0001 Inspiration Making technology easier to use has been my obsession for many years now, and this is why Pagoda resonates so much with me. One of the most important "eaves" of Pagoda console is the alerts section, which allows non-technical users to set up simple alerts with a if-this-then-that approach. Altho the simplicity is great, the very moment the user needs a bit of business logic to decide if a notification is due or not, the system falls short. Don't give me wrong, Pagoda console is amazing as it is, but I think I found a way to make it even better while keeping intact the Pagoda vision of being the easiest Web3 Startup Platform . What it does It allows users to create flows, which are small applications created using visual scripting, that work by dragging and dropping blocks that describe the application in terms that make sense for humans, so even non-technical people can develop complex logic. Flows are connected to NEAR accounts/contracts, and when an interaction with a contract happens, the flow is executed and the user's logic determines if a notification is due or not. Notification then can be funnel into emails, webhooks or Telegram: With NEAR Smart Events you can do all of this and much more without writing a single line of code: Notify by email your compliance team when contract X receives a deposit over 1000$? Send a telegram message every Friday at 9:00 AM with contract X balance to Bob from accounting? Create a ticket on Salesforce using a webhook when the Gas fees from contract X method Y are getting too high? How we built it The whole service runs in 2 NodeJS processes (that can scale horizontally). If you want to get more into the technical details, please take a look at the https://github.com/domingosl/nse Open source and embeddable NSE is and uses only MIT license open source libraries, and from the gecko is designed to be easily embeddable. It does not depend on any frontend framework, and the backend engine is very light. What's next for NEAR Smart Events On chain writers blocks : By storing the private key, user can actually not only read and react to on-chain events but also write to it. Documentation and Tutorials Research into other use cases that might need new types of blocks <div