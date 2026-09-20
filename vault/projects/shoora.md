---
slug: "shoora"
url: "https://devpost.com/software/shoora"
title: "Shoora"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 277
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/education"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "user/educator_student"
---

# Shoora

> WhatsApp Bot to help people stranded due of COVID-19 lockdown

[Devpost](https://devpost.com/software/shoora) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[civic_government]] [[education]] [[housing_homeless]] [[labor_employment]]
**user** [[educator_student]]

**stack** amazon-dynamodb, amazon-lex, aws-lambda, python, twilio

## How they structured the write-up

- inspiration
- what it does
- how i built it
- what's next for shoora

## Body

Inspiration Thousands of people across the globe are stranded away from their home due to sudden lockdown decision by local governments. They have either gone to a different country or a different city in their home country for vacation, studying or job. Most of them are either student or daily wage labors who have lost their source of income and do not have enough money to pay for basic needs like food, shelter, etc. They cannot return to their home due to the lockdown and need immediate help. What it does Shoora is a WhatsApp bot which helps such people. It asks for some basic information like their name, contact number, current location and their home location and stores it. If the local government has setup any shelter home near person current location, it is displayed to user. It also provides notification regarding important steps taken by government like how they can apply for relief money provided by government or timelines when travel restrictions would be lifted. How I built it I used Twilio API for WhatsApp to receive and send WhatsApp messages. Amazon Lex is used for building conversational interfaces. AWS Lambda is used to perform validation and other business logic. The data is stored in Amazon Dynamodb. What's next for Shoora Currently Shoora does not has data for shelter homes setup by governments around the globe and is not aware of latest development and steps taken by government. It needs to get these information so that it can notify the people with correct information. This proof of Concept is done using WhatsApp bot, however it can be extended to other channels including messenger, SMS. <div