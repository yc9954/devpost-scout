---
slug: "cov-tell"
url: "https://devpost.com/software/cov-tell"
title: "Cov-Tell"
hackathon: "hack:now"
winner: true
words: 361
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
---

# Cov-Tell

> Instantly access real-time updates on COVID-19 at multiple scales through your Alexa or Google voice device.

[Devpost](https://devpost.com/software/cov-tell) · hackathon [[hack-now]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]

**stack** voiceflow, wolfram-technologies

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cov-tell

## Body

Cov-Tell logo How It Works Voiceflow Application API in JSON format Cov-Tell Logo Inspiration Everyone is constantly looking up the latest statistics on the coronavirus, and specifically, they often want to know the most recent information about their county and state, which becomes a challenge due to information noise. We want to make this information easily and quickly accessible to laypeople - like through an Alexa device! What it does The user can open our app from their Alexa or another voice-compatible device. Then, the device asks whether they want information at the county, state, or national level. The user can respond and input their location to receive a report on the change in confirmed cases and deaths in the user’s county or the change in state or national infection rate. This report is based on data from Wolfram. How we built it We used the Wolfram Language to build API functions that retrieve location-specific data from Wolfram on COVID-19 and format it in a speakable string format. Then, we used Voiceflow to make a voice app that provides the user with information from the API functions. Challenges we ran into It was challenging to locate the necessary data and format it and the API functions to be compatible with Voiceflow. Accomplishments that we're proud of We’re proud that we made a functional voice app that provides users at home with reliable updates on the spread of the coronavirus - in particular, hyperlocal information. What we learned No member of the team had previous experience with APIs or Voiceflow, so this project was an excellent opportunity to learn about how to design and implement APIs and how to create a user-friendly voice app. What's next for Cov-Tell We hope to be able to retrieve more data from sources other than Wolfram, specifically the Johns Hopkins curated data since it is usually the most reliable and has the most recent updates. We also would like to provide data for regions and nations around the world instead of just the United States. With further work (and publicly available data), Cov-Tell will be able to provide crucial information, such as nearby hospital capacities. <div