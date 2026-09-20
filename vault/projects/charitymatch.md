---
slug: "charitymatch"
url: "https://devpost.com/software/charitymatch"
title: "CharityMatch"
hackathon: "Hack the North 2019"
winner: true
words: 319
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/geospatial"
---

# CharityMatch

> An ML-based web application to facilitate non-monetary donations to charities in urgent need.

[Devpost](https://devpost.com/software/charitymatch) · hackathon [[Hack the North 2019]]

## Facets

**substrate** [[geospatial]]

**stack** firebase, google-maps, javascript, machine-learning, python, react

## How they structured the write-up

- inspiration
- what it does
- what's next for charitymatch

## Body

Sign-up page User can choose to upload a picture or manually enter a product category if they don't have a picture The algorithm recognizes from the picture that the item to be donated is a t-shirt, and provides a list of charities in urgent need. Users receive points for each donation depending on their tier. Confusion matrix Inspiration We live in a world of consumerism, where most people care more about acquiring products than their disposal. By the end of 2019, Americans are expected to have produced 35.4B of waste -- textile only. Only 28% of people donated unwanted items to charities. To make an impact on our environment, we need to think about disposing and repurposing used products as much as possible. What it does CharityMatch uses Machine Learning to identify item categories of item to donate from pictures that users will have uploaded. Given an item category, it outputs a list of charities that are most in need of this product category at that moment so that users can make an impactful donation. The list also displays the need urgency of the category for each charity. A map feature displays the location of each charity to help users plan their trip. Points are awarded to the user after making a donation, the amount of which depends on the urgency of the charity's need, with Tier 1 being the highest priority and amount of points, and Tier 3 being the lowest for both. Built using Google's Auto-ML Vision API, Firebase, Google Maps API, Google OAuth 2.0. What's next for CharityMatch In the future, CharityMatch could integrate the QR code scanning feature in order to track donations for all users to multiple charities. There is also the possibility of partnerships with rewards programs to strengthen the points system it currently has, so that users can benefit from offers and have rewards programs benefit from user acquisition and retention. <div