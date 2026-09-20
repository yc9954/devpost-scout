---
slug: "drink-enough-water"
url: "https://devpost.com/software/drink-enough-water"
title: "Drink enough water"
hackathon: "Alexa Skills Challenge: Alexa Conversations"
organization: "Amazon"
winner: true
words: 746
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "substrate/document_pdf"
---

# Drink enough water

> Water is Life! Do you drink enough water? Many people don't! This skill enhances quality of life through healthy hydration. The Skill ensures that its users drink enough water and are protected.

[Devpost](https://devpost.com/software/drink-enough-water) · hackathon [[Alexa Skills Challenge- Alexa Conversations]]

## Facets

**domain** [[climate_energy]]
**substrate** [[document_pdf]]

**stack** amazon-dynamodb, amazon-web-services, cloudwatch, lamdba, ml, node.js, quicksight, react, s3, sns

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- what we learned
- what's next for drink enough water

## Body

Water is Life Drink enough water Skill demonstration Calculate the ideal water consumption Alexa Conversations 6 parameters Inspiration Drinking enough water every day is essential for life. This is true for all of us and especially for older people. We have experienced this ourselves with our own parents! While searching for a simple and affordable solution, we noticed that the current skills in the German and US amazon skill store for a healthy supply of water are missing important functions or that they do not work properly. This has motivated us to develop the “best skill in class" for daily drinking of sufficient water. What it does The skill ensures healthy hydration for its user by calculating the ideal drinking quantity, its individual memories of drinking water and hints on the amount of water drunk and still to be drunk. With its combination of functions that are essential for users, the skill clearly stands out from existing “drink water” skills: calculator : It determines the user´s ideal and very individually high drinking quantity per day. reminder : It reminds the user to drink water whenever he wants to. tracker : It records and tracks the amount of water the user has drunk and informs him about the amount of water still to be drunk per day. Calculation of the individual drinking quantity with Alexa Conversations The skill is able to determine the individual drinking quantity with 6 parameters. These are: The gender, the age, the size, the weight, the degree of activity and the prevailing climate. Due to the many parameters, the variance of input formulations and correction possibilities increases. The ideal application for implementing the possibilities of Alexa Conversations! With Alexa Conversations we have elegantly succeeded in handling these many possible cases in a flexible way. The Alexa Conversations dialog actively asks for missing input sizes or manages corrections that are made by the user. With Alexa Conversations the skill is easier to use for the user and therefore more suitable for everyday use. As a second basic function, it is easy and convenient for the user to be reminded by the skill to drink water at self-selected times. After setting a reminder time, the skill reads out all defined reminder times, so that the user gets an overview and can make changes. Afterwards the user will be reminded to "drink water" at the specified times. As a further basic feature, the skill can record and update the daily amount of water drunk. In addition, the user calls the Skill its drunk water quantity. The skill then tells him the amount of water he has drunk up to that point and gives him an indication of the remaining amount for that day. So the user knows how much he has already drunk and how much he has to drink to reach his ideal daily amount. These 3 basic functions of the "Drink enough water" skill enable the user to achieve healthy hydration. For this he needs his ideal drinking amount, his personal drinking reminders and the continuous recording of his drunk water quantity, and hints about the amount of water still to be drunk. ## How we built it We built it with the Standard Alexa / AWS technology stack using Lambda, S3, DynamoDB, Cloudwatch, SNS. For the backend (which is implemented but, because of the sake of simplicity, not activated) we use React and Quicksight with Machine Learnings-Features. Challenges we ran into The biggest challenge was the integration of the Alexa conversations part into the other skill part. Accomplishments that we're proud of In the skill store are already quite good drinking water skills. We are proud that we were able to create a new and better level of usability, and functionality. What we learned Alexa Conversations is a great technology with huge potential. But it is necessary to test this technology through multiple trials. What's next for Drink enough water Additional Premium Features are not only planned but already created in a backend (see AWS Account). Without giving too much away, soon it will be possible to offer a warning function that will indicate when there is a danger that a person has not drunk enough at a certain time. In addition to this, it will be possible to track and document the drinking behavior of people over long periods of time. And also to ensure that different people can use "Drink enough water" in parallel, such as families. So stay tuned! <div