---
slug: "monch-e5k0hv"
url: "https://devpost.com/software/monch-e5k0hv"
title: "Monch"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 442
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/scientific_research"
  - "user/social_worker"
  - "substrate/genomic_bio"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Monch

> Meet Monch – the AI-powered app that uses photos of your food to instantly recognizes ingredients, portion sizes, and calculates complete macro breakdowns.

[Devpost](https://devpost.com/software/monch-e5k0hv) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**domain** [[scientific_research]]
**user** [[social_worker]]
  <sub>weak: government_staff</sub>
**substrate** [[genomic_bio]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** clerk, next, pinata, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for monch

## Body

landing page home page Inspiration As people who track our health, we know how tedious it is to track your macros of everything you eat, especially when there aren't written out values for carbs, fats, calories, or even proteins. Additionally, if you do get a macro tracker on your own, there is usually a pay wall for a lot of your features and functionalities. That is why Monch is a website that allows you to just take a photo if you wanted to track your macros. What it does Our application lets you track your calories, carbohydrates, fats, and proteins for your meals given a picture. You can pull your goals into the website when you sign up so that you can keep track your day to day intake and see if you are meeting your macros! Additionally, we display a graph with your macro totals across different days. How we built it We had to incorporate a bunch of different parts together to get the actual model to display data we need. First, we built a model to classify food from an image using a neural network (not chatgpt requests). Then after we trained the model to classify the food, we had to connect it this to a public data set that stores the amount of calories, carbohydrates, fats, and proteins in the food displayed. After getting all the data we need, we just had to connect that to Pinatas file storage database, which was convenient since we were storing images anyways, and display those images and data on our website. Challenges we ran into We realized how hard it is to actually train a model and how long it took. Additionally, it was our first time using pinata as well as our first time using machine learning and AI to build a model. Accomplishments that we're proud of We are proud to have a photo recognition software to correctly classify a hotdog! This is something we were proud of immensely since we had a lot of data to sift through and get everything working. What we learned We learned how fun it is to build such a fun project! We have gained invaluable experience and knowledge about how to streamline an entire model to a web application! It was a lot of fun getting our project deployed and see our results! What's next for Monch Due to our web experience, it made more sense for us to build a web app and just use it on the browser. However, we do know that most people use phones to take photos so we could take it to a mobile application. <div