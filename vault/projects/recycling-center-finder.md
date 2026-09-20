---
slug: "recycling-center-finder"
url: "https://devpost.com/software/recycling-center-finder"
title: "Alexa Skill to Find Recycling Center"
hackathon: "Alexa Skills Challenge: Tech for Good"
organization: "Amazon"
winner: true
words: 197
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Alexa Skill to Find Recycling Center

> Alexa Skill for Find recycling center for Drop-Off in nearby location based on user's Item and Zip Code

[Devpost](https://devpost.com/software/recycling-center-finder) · hackathon [[Alexa Skills Challenge- Tech for Good]]

## Facets

  <sub>weak: developer_tools</sub>
**substrate** [[geospatial]] [[structured_db]]

**stack** alexa-skill-kit, ask-sdk-for-python, beautiful-soup, https://search.earth911.com, python-3.6

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for recycling center finder

## Body

Search Nearest Center Recycling Center Inspiration With over 350 materials and 100,000+ listings, earth911.com maintain one of North America's most extensive recycling databases. Sometime it is difficult to find the place where we can send the item to recycle and save the environment. earth911.com provides extensive search engine to find recycling drop-off center for numerous type of materials. What it does Alexa skill " Recycling Center Finds recycling center for Drop-Off in nearby location based on user's Item and Zip Code and items to be recycled. How I built it I have utilized python libraries "urllib" and "BeautifulSoup" to send the request to https://search.earth911.com/ and scrape the response to find the result list of the recycling centers near the Zip Code provided by the user. Alexa skill Challenges I ran into Scrapping the http response got from the search engine Accomplishments that I'm proud of I can help people in finding suitable recycling center to support the cause of save-environment What I learned python package BeautifulSoup and Web Scrapping What's next for Recycling Center Finder To automatically find nearest location, based on user's address Call Recycling Center Send the Location Data on SMS and on Email <div