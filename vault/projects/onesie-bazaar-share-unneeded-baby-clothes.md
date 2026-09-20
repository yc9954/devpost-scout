---
slug: "onesie-bazaar-share-unneeded-baby-clothes"
url: "https://devpost.com/software/onesie-bazaar-share-unneeded-baby-clothes"
title: "Onesie Bazaar"
hackathon: "Alexa Skills Challenge: Tech for Good"
organization: "Amazon"
winner: true
words: 428
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
---

# Onesie Bazaar

> Onesie Bazaar is a green marketplace for sharing unneeded baby clothing, for free

[Devpost](https://devpost.com/software/onesie-bazaar-share-unneeded-baby-clothes) · hackathon [[Alexa Skills Challenge- Tech for Good]]

## Facets

**mechanism** [[graph_reasoning]]

**stack** alexa-skills-kit, amazon-alexa, amazon-dynamodb, amazon-web-services, aws-lambda, dynamodb-atomic-counters, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next

## Body

Inspiration The idea for Onesie Bazaar started as a general marketplace for sharing second hand items. I've noticed there are hardly any skills that connect people in such a way, so why not build the first? As the idea matured, I decided to pivot into a niche marketplace which will be customized for exchanging baby clothes, hopefully making a positive impact on the environment and local communities. What it does Onesie Bazaar allows you to reduce waste and clutter by listing unneeded baby clothes, or save money by browsing clothes in your area. Users can list items in their city by gender and age range in months, and each listing contains contact information which can be later used to set a pickup. How I built it Onesie Bazaar was coded from scratch in NodeJS using the latest Alexa Skills Kit, and includes AWS Lambda, DynamoDB and S3. The skill was built using many advanced Alexa features such as persistence (for both the user details and the actual listings marketplace), dialog management and entity resolution. I also designed the logo :) Challenges I ran into My challenges were both product and technical. Product wise - although I needed quite a lot of information from the user about their listing, I wanted to make the experience as frictionless as possible. For example, I ended up using the contact information API for the user's first name and phone number, so the user is not bothered to supply them during the dialog. I also designed some one-shot sentences so a user can create a listing or browse by using a single sentence. Technical wise - In order to list all of the items for a specific filter, I had to find a way to query the DB efficiently and I ended up using DynamoDB's secondary indexes feature. I also had to figure out how to generate a unique ID for every new listing, which will also scale well with DynamoDB - I ended up using the atomic counters capability of DynamoDB. Accomplishments that I'm proud of Designing & coding this skill has been a hell of a ride, and I enjoyed (almost) every moment of it :) seeing all of the tech bits play together nicely was extremely fulfilling. What I learned That it's better to leave some features out in favor of a cleaner voice experience. What's next This skill has great potential to expand to many other unneeded household items, and there are more features to come such as: marking favorites, earning badges, searching by mile radius and more. <div