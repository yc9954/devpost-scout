---
slug: "analog-argus"
url: "https://devpost.com/software/analog-argus"
title: "Analog Argus"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 232
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Analog Argus

> You're looking for analog camera but you don't know the good price (to buy or sell). This API provide list of analog camera with short desc. A feature will search and compute the average price.

[Devpost](https://devpost.com/software/analog-argus) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[video_visual]] [[web_dom]]

**stack** angular.js, beautiful-soup, django-rest-framework, postgresql, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for analog argus

## Body

request example - get all models Analog Argus has been created to display the average prices retrieved by the API. Postman helps to develop this part. Inspiration I'm looking for a camera model (analog) but I don't know if it's expansive. Also, I don't know if I can sell to the best price. I wished create a simple website to display the good price (like a blue book, or argus as we say in France) but there's no resources to provide my application with these data. So, I develop a tiny api to get brand, model and search a specific model. This last feature is based on beautiful soup (web scraping) to fetch the searched model and compute an average price. Of course, this api is used for personal usage but you can fork this project to do the same thing. What it does Provide a list of brand, models and search and compute average price for a given model How we built it Api build with Django Rest Framework Challenges we ran into First time with Django. Rest Framework Accomplishments that we're proud of To finish this project and learn Django Rest Framework in limited time What we learned A simple way to find a good price if you love analog camera (film camera) What's next for Analog Argus Actually, provide price for France but it could be from anywhere <div