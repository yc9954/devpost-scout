---
slug: "universalapi-z0chxa"
url: "https://devpost.com/software/universalapi-z0chxa"
title: "universalAPI"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 335
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/developer"
---

# universalAPI

> universal API is API converter with goal a seamless ESB ( Enterprise Service Bus ) for developer to connect to any biller / API gateway.

[Devpost](https://devpost.com/software/universalapi-z0chxa) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]]
**user** [[developer]]

**stack** java

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for universalapi

## Body

List of biller already integrated Application UI protocol response sample integration to Jatelindo protocol request sample integration to kisel Inspiration I created universalAPI from 2012, back to my previous role as a junior backend developer. In my previous company, I must create any H2H integration for payment gateway system, and this thing sometimes made me struggle since I must face various protocol ( from HTTP/S GET to ISO 8583 ) from various company. What it does So I created a API converter for made me easier for integration. From all the tech spec I already have, I created unified response request and response and translate it into any tech spec needed. Since until now, most of integration regarding to payment gateway, so I created the template like this : REQ listener using HTTP/S -> biz logic to convert message -> biller RESP biller -> convert message based on response needed -> sent back to requester How we built it I already built it and until now there is more than 5 tech spec already deployed with more than hundred service running from electrical bill, water bill, phone bill, balance top up, e money top up, bank traansfer, etc. Challenges we ran into Most of challenges is to understand what client need for the responses. The other parts is doing some translator for any tech spec given by biller Accomplishments that we're proud of This app bring me to 5th champion for mini BCA finhack and become a part of grand final BCA finhack 2017 What we learned I learned there is lot of potential client who didn't want to burn they cost for hiring specific programmer for H2H integration, so this apps help them much for anay integration without needed high skill of programming What's next for universalAPI I want to expand this application into cloud service based ( currently it's only for desktop app ) and can using it as global converteer ( currently most of interconnection only for Indonesian based company ) <div