---
slug: "manaclean"
url: "https://devpost.com/software/manaclean"
title: "manaClean"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 626
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "substrate/geospatial"
---

# manaClean

> Email cleaning at your fingertip without exhausting your SMTP, ability to pay for the service through Chainlink External Adapters and Any API

[Devpost](https://devpost.com/software/manaclean) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[finance_payments]] [[security_privacy]]
**substrate** [[geospatial]]
  <sub>weak: structured_db</sub>

**stack** amazon-web-services, axios, chainlink, csv-parser, node.js, pangea

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for manaclean

## Body

Inspiration My inspiration was sparked by a glaring challenge I faced – a high number of email bounces in my marketing campaigns. I scoured the internet for an open-source tool to solve the problem, but nothing seemed to fit the bill. Even commercial offerings fell short in delivering satisfactory results. I realized the need for a more effective, reliable email cleaning system, so I decided to build one myself. What it does My project, manaClean, is an innovative email cleaning system designed to improve the quality and deliverability of email campaigns. It operates on a unique algorithm that invokes SMTP verification only when necessary, thus reducing the chances of being blacklisted by spamhaus. Moreover, it provides a special feature that supports proxy routing, given that port 25 is open. Notably, manaClean also integrates with Pangea , leveraging cybersecurity technology for a more secure, efficient process and returns whether the checked email is part of the breach. How we built it I developed manaClean using my knowledge of email systems, network protocols, and innovative programming techniques. The system's core is built on Node.js and integrates with SMTP for verification when required. In particular, when emails come from non-public domains, we employ a Pangea process: First, we check the domain's A record and its reputation. If the domain reputation is unfavorable, we return the email as invalid. Secondly, we examine the IP reputation and embargo status derived from the A record. If the IP reputation is malicious or linked to an embargoed country, the system deems the email invalid. Thirdly, we search for breached users - if the email has been compromised, we include this as part of the information return. To prevent frequent hitting of SMTP servers, which could trigger Spamhaus, we utilize different login systems. Furthermore, I engineered a solution to allow proxy support, enhancing the service's capabilities. Despite the challenges, we managed to achieve eight operational APIs without resorting to SMTP. Using Chainlink , we can offer automatic payment system through smart contract and pay via Fantom and other coins for each validation. A Smart Contract is connected directly to API Gateway to make payment easy and secure. It offers additional ways of automating entire payment system with the service itself. Routed through AWS API Gateway and AWS Load Balancer through AWS EC2 service Challenges we ran into One of the most significant challenges I faced was finding a proxy provider that allows port 25 to remain open. This restriction made it impossible to test the proxy feature during the hackathon. Another challenge was the industry itself; email cleaning is a tough field as most service providers block port 25, inhibiting the use of SMTP verification. Also the recaptcha slide was giving me some problems Accomplishments that we're proud of Despite the challenges, I am particularly proud of building a versatile email verification system that surpasses existing open-source and some commercial options. I managed to create specialized verifications for many major domains, which is a feature not found in most similar tools. I'm also proud that I could build such a system during a hackathon, and plan to open-source it after some security fine-tuning. I got 8 api running for this without using smtp What we learned Through this project, I discovered that email cleaning is a complex, challenging industry. It reinforced the fact that innovation often necessitates overcoming technical hurdles, like the prevalent restriction on port 25 usage. What's next for manaClean I envision several potential future developments for manaClean. I plan to continue refining the system, particularly the untested proxy feature. I also intend to delve deeper into the security aspects of the software, ensuring it's robust and secure before I open-source it, allowing the wider community to benefit from this solution. <div