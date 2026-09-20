---
slug: "fridgemate"
url: "https://devpost.com/software/fridgemate"
title: "FridgeMate"
hackathon: "hack:now"
winner: true
words: 416
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/elder_child_care"
  - "domain/housing_homeless"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/patient_family"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# FridgeMate

> Shelter-in-place has got us storing a lot more food at home. FridgeMate helps manage it! Push notification reminders, so you can eat food while it's still fresh. Recipe suggestions for tastier cooking

[Devpost](https://devpost.com/software/fridgemate) · hackathon [[hack-now]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[agriculture_food]] [[elder_child_care]] [[housing_homeless]] [[retail_commerce]] [[supply_logistics]]
**user** [[patient_family]]
**substrate** [[financial_record]] [[video_visual]]

**stack** amazon-remote-shopping-api, bigoven-recipe-api, figma, google-cloud-vision-ai, postmate, voiceflow

## How they structured the write-up

- inspiration
- what it does
- how i built it
- what's next for fridgemate

## Body

Title Page Kitchenventory Recipe Search Expiration Reminder Grocery Shopping Cart Inspiration COVID-19 has significantly changed how we live our life. Having to eat every single meal at home, we spend a lot of time thinking about what we want to eat, what food we already have, whether we have enough food, what to cook, and when we should make another grocery trip. We have made many mistakes including forgetting about the groceries we have and cooking ingredients in the wrong order both of which resulted in a lot of food wasted and hungry stomachs. We also constantly worry about whether our parents and grandparents are able to manage online grocery shopping well and have enough food at home. Most online grocery delivery services now require people to make the orders a week in advance. What it does It is a mobile app that replaces the above thought process and automates planning. It tracks food inventory and their freshness and reminds people when things are expiring. It also suggests recipes based on the ingredients that people already have, so that the recipes are all actionable. The app also allows users to add or restock groceries to a shopping cart while they are browsing recipes. It allows all family members to collaborate. Kids can add the ingredients in the recipes they want into the cart. Users can also help their beloved elderly with food inventory and meal planning. How I built it We have prototyped the app using figma, planning out interactions powered by several technologies. Google Cloud AI will be used for OCR in grocery receipt images. Voiceflow will power the Alexa interactions that allow users to quickly check up on their Kitchenventory. Postmate will help us access the BigOven API for searching recipes, and the Amazon Remote Shopping API for managing users' grocery carts. What's next for FridgeMate So far, FridgeMate is just our vision, but there are probably great ways to help our users that we haven't even thought of yet. Engaging with our user base will be key, through focus groups and pilot testing. We'd love to build out the MVP and interview our pilot users to determine which features to prioritize based on what users really need. We will streamline our critical user journeys, and remove unnecessary complexity. Down the road, it would also be exciting to monetize FridgeMate, possibly by charging a subscription for premium features, or potentially taking a share from Amazon / Whole Foods orders made within the app. <div