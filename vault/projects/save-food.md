---
slug: "save-food"
url: "https://devpost.com/software/save-food"
title: "Don't waste food"
hackathon: "Alexa Skills Challenge: In-Skill Purchasing"
organization: "Amazon"
winner: true
words: 589
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Don't waste food

> Say here the food you buy, when you opened it and when it expires. You will waste less food and avoid possible food poisoning.

[Devpost](https://devpost.com/software/save-food) · hackathon [[Alexa Skills Challenge- In-Skill Purchasing]]

## Facets


**stack** alexa-presentation-language, amazon-alexa, apl, dynamodb, dynamola, isp, lambda, multilanguage, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for save food

## Body

New list with Alexa Presentation Language (1) New list with Alexa Presentation Language (2) New product info sample Confirm subscription Notifications when a products expires today I recommend a subscription for you Home, with info about products that expire today, tomorrow, 1 day after tomorrow and products expired Order history Info about 1 product: saved date, opened date and expiration date info product Show list Inspiration In almost every house food is wasted. Sometimes the food expires without us noticing. Other times we buy food without really knowing the food we already have at home. In addition, we can eat expired food if we are clueless. The expiration date that appears on the product packaging is not enough if the product has already been opened. What it does Therefore, I have developed a skill that the whole family can use to manage foods when they are bought, opened or consumed. At the time of food purchase, you must indicate the name and expiration date of the food. At the time the food is opened, the new expiration date of the opened food must be indicated. The skill checks that this new date has to be closer than the initial date. At the moment a food is consumed or thrown away, we will tell the skill to dispose of the food. Every time you open the skill, she reminds you only what products will expire today, tomorrow or the day after tomorrow. It also tells you what products have already expired. So you can focus on using the foods that will expire soon and: avoid wasting food and reduce the purchase of food. The skill can be used for free up to 4 foods. From that moment, the skill suggests the subscription you need to add an unlimited number of foods. How I built it I have developed this skill using Alexa in-skill purchase, Alexa Presentation Language, node and dynamodb. The skill is multilanguage. It supports Spanish and English. Finally, I use Alexa UpsServiceClient to get Timezone of each user and converts expiration dates of their foods. I use dynamola as library to access dynamodb table. Challenges I ran into It is a skill used from different parts of the world, so I had to know the time zone of each user to convert the purchase dates, opening date and expiration date of the food. For this I used the Alexa API UpsServiceClient. I have also worked with the momentjs library and with to convert dates into more human words like "today", "tomorrow", "the day after tomorrow". Another important challenge has been to use the correct tense for past, present or future (depending on whether the product has already expired, expires today or will expire in the future). Accomplishments that I'm proud of I have learned to use alexa in-skill purchases and all its workflow. I also learned with this skill to correctly consult the timezone of each user and to convert dates correctly. Technically I am also proud of the result, because it is an easy-to-use skill that answers you briefly and with short useful information at all times. What I learned I have learned to use alexa in-skill purchases and all its workflow. I also learned with this skill to correctly consult the timezone of each user and to convert dates correctly. What's next for Save food I want to implement shared information between the members of the family. For example, the father can add milk, the mother can open it and finally the son remove it. <div