---
slug: "lettuce-ke6nsa"
url: "https://devpost.com/software/lettuce-ke6nsa"
title: "lettuce"
hackathon: "HackMIT 2023"
organization: "HackMIT"
winner: true
words: 462
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/supply_logistics"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# lettuce

> lettuce is an app that helps reduces food waste by allowing you to scan grocery receipts, track expiration dates, and build a sustainable community by offering surplus food to friends and neighbors

[Devpost](https://devpost.com/software/lettuce-ke6nsa) · hackathon [[HackMIT 2023]]

## Facets

**domain** [[agriculture_food]] [[supply_logistics]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** bootstrap, firebase, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lettuce

## Body

Landing page, where you create an account Home screen, where you scan receipts and track your own food Home screen, where you can see people in your network who have food available for you that is expiring soon. Recipes screen, where you can explore new recipes and find ingredients in your own and your network's pantries. Inspiration We love cooking and watching food videos. From the Great British Baking Show to Instagram reels, we are foodies in every way. However, with the 119 billion pounds of food that is wasted annually in the United States, we wanted to create a simple way to reduce waste and try out new recipes. What it does lettuce enables users to create a food inventory using a mobile receipt scanner. It then alerts users when a product approaches its expiration date and prompts them to notify their network if they possess excess food they won't consume in time. In such cases, lettuce notifies fellow users in their network that they can collect the surplus item. Moreover, lettuce offers recipe exploration and automatically checks your pantry and any other food shared by your network's users before suggesting new purchases. How we built it lettuce uses React and Bootstrap for its frontend and uses Firebase for the database, which stores information on all the different foods users have stored in their pantry. We also use a pre-trained image-to-text neural network that enables users to inventory their food by scanning their grocery receipts. We also developed an algorithm to parse receipt text to extract just the food from the receipt. Challenges we ran into One big challenge was finding a way to map the receipt food text to the actual food item. Receipts often use annoying abbreviations for food, and we had to find databases that allow us to map the receipt item to the food item. Accomplishments that we're proud of lettuce has a lot of work ahead of it, but we are proud of our idea and teamwork to create an initial prototype of an app that may contribute to something meaningful to us and the world at large. What we learned We learned that there are many things to account for when it comes to sustainability, as we must balance accessibility and convenience with efficiency and efficacy. Not having food waste would be great, but it's not easy to finish everything in your pantry, and we hope that our app can help find a balance between the two. What's next for lettuce We hope to improve our recipe suggestion algorithm as well as the estimates for when food expires. For example, a green banana will have a different expiration date compared to a ripe banana, and our scanner has a universal deadline for all bananas. <div