---
slug: "resistbot-contact-your-elected-representatives"
url: "https://devpost.com/software/resistbot-contact-your-elected-representatives"
title: "Resistbot - Contact your officials"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 506
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/general_public"
  - "substrate/structured_db"
---

# Resistbot - Contact your officials

> Use Resistbot to send feedback directly to your elected officials

[Devpost](https://devpost.com/software/resistbot-contact-your-elected-representatives) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**user** [[general_public]]
**substrate** [[structured_db]]

**stack** alexa, amazon-alexa, amazon-dynamodb, amazon-web-services, javascript, lambda, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for resistbot - contact your elected representatives

## Body

Inspiration In the 2016 presidential election, only ~50% of eligible voters participated. Our goal is to build a platform that enables every US citizen to make their voice heard, and increase participation in the political process. We love our Alexa devices, and figured that this would be the easiest way for citizens to send feedback to their elected officials. So far, our team of volunteers has enabled 100s of thousands of citizens to send over a million faxes to congress via an SMS chatbot, and we are looking forward to scaling our Alexa skill as well. What it does With Resistbot, US citizens can send their feedback directly to their elected senators and house representatives via their Alexa enabled devices. This feedback is delivered via real fax messages. Many of our users also receive responses from their representatives. Also, users can call their congress members via Alexa(after user expresses intent to call congress, they will receive a call on their mobile phone, which then connects them to their congress member - call congress is pending Alexa skill review as of 5/9/17 ). How I built it I was responsible for building the Alexa skill. It uses Amazon account linking and the new Alexa address API to get user name and address information, which is required to lookup congress members and also set a "from" address for fax messages(the "from" address enables officials to respond to feedback). The skill business logic is built with node.js on AWS Lambda, and user data is persisted using Amazon DynamoDB. There is a separate Resistbot backend service, built by our talented team of volunteers, which the skill service calls to look up senators, house representatives as well as initiate communications flow (SMS/voice calls enabled by Twilio). Challenges I ran into We found that there is no easy way to capture free-form user input. We are using Amazon literals to get around this, but sometimes user speech is still not accurately recognized. To improve this, we grabbed ~1500 of the top messages from our existing database of SMS messages, and fed them into the Amazon sample utterances, which did improve accuracy significantly. While the recognition is accurate most of the time, we wanted to make sure we are not spamming our congress members. As a result, we introduced an intent that allows users to edit their message / confirm via text message, if they desire. Accomplishments that I'm proud of Every morning, I use the Resistbot Alexa skill to send feedback to my elected officials. Given the low participation overall in the political process, we are proud that our project directly enables more people to take part and make their voices heard in a very easy, simple, and quick way. What's next for Resistbot - Contact your elected representatives Our goal is to progressively encourage users to participate in their political process over time. Today, Resistbot for Alexa lets you send messages to elected officials. We have a long list of future features and enhancements and we look forward to iterating. <div