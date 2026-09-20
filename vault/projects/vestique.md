---
slug: "vestique"
url: "https://devpost.com/software/vestique"
title: "Vestique"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 326
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "domain/retail_commerce"
---

# Vestique

> Vestique, your AI wardrobe assistant, tracks your style and ensures no clothes go unworn. Smart alerts help you wear 40% more of your closet and save $1,200 yearly.

[Devpost](https://devpost.com/software/vestique) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**domain** [[climate_energy]] [[retail_commerce]]

**stack** brevo, llama, opencv, sambdanova, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vestique

## Body

Inspiration The fact that we go through life and are willing to spend $2000/year on clothing while only ending up wearing 20% of it. This statistic is commonplace and results in "fashion landfills", which lead to the fashion industry's global emissions jumping by 50% by 2030. What it does It provides users with a platform to maintain their wardrobes. By giving daily "fit checks", our app can tell the user what kind of clothing items they tend to wear more, giving the user guidelines they can follow next time they go clothes shopping. This app also provides them with an outlet to sell unwanted items, rather than letting them rot in a landfill. This works by emailing a user when it has been some number of days since they last wore a piece of clothing, then giving them the option to automatically list that unwanted item. How we built it We built our UI using Streamlit and the main model that we use for identifying and classifying clothing items uses llama-3.2-11B-Vision-Instruct and Meta-llama-3.1-70B-Instruct via SambaNova and Brevo for automated email sending. Challenges we ran into We had some integration issues as well and managing the development of a large number of features over a short period of 24 hours proved to be difficult. Accomplishments that we're proud of We managed to implement all of our target features and they were of good quality. What we learned How to use SambaNova and how powerful of a platform it is. As well as learning how to make a full-stack application in Streamlit. What's next for Vestique We want to improve the model's accuracy, as well as make the predictions for user preferences more detailed to give a user a better idea of what kind of clothing they tend to wear vs clothing they tend to neglect. All of this is being done to make a model that can give more personalized details to help people reduce wastefulness. <div