---
slug: "nic-sdk"
url: "https://devpost.com/software/nic-sdk"
title: "NIC - No Internet Connection"
hackathon: "Junction 2016"
winner: true
words: 342
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
---

# NIC - No Internet Connection

> NIC SDK helps you to keep your users connected when they have no internet connection.

[Devpost](https://devpost.com/software/nic-sdk) · hackathon [[Junction 2016]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]

**stack** 46-elks-api, 46elks, 46elks-api, amazon-web-services, android, android-studio, fintech, java, nic-sdk, node.js, npm, postman, radix, transferwise

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for nic sdk

## Body

Main page Getting live rates Adding reference Getting successful response Proof that there was no internet connection Inspiration Today's there're amazing technologies that are changing the way we're living. Unfortunately, there's one manner which is we need the Internet all the time. Not having access to the Internet means no knowledge and information. Unfortunately, most of the people in the world don't have access to the Internet. That's why I created NIC SDK (HTTP over SMS). What it does NIC SDK recognize if user has the Internet access or not. If user has the Internet access, NIC calls your API and you get the data. If the user doesn't have internet access, that's where the magic happens. NIC SDK will get request, parse it, and send SMS to NIC servers, and return the data you need as SMS. How I built it In this hackathon, I couldn't manage to build a team, and I did all the parts alone. I built backend part to handle SMS and parse them as request, and I build customized SMS Manager for Android, to deal with incoming data. Moreover, I built one demo app which let's you Transfer Money via TransferWise without Internet access. You can access video demo below. Challenges I ran into There was problems with integrating transferwise api and 46elks api. However, I could solve problems to show working demo. Accomplishments that I'm proud of I made base of platform that let's people to connect to the internet any time. As demo, I proud of that now, people can transfer money without Internet barrier. What I learned Untill we wait google, facebook, or internet.org projects to build good infrastructure, we can help most of the people in the world to access to the Internet through SMS. According to statistics, 85% of population of the world has access to SMS through 2G network. So, this SDK can help them to connect. What's next for NIC SDK To build great team and release NIC SDK for developers; To release apps for offline payment transfers. <div