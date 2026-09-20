---
slug: "morning-zen-with-coco"
url: "https://devpost.com/software/morning-zen-with-coco"
title: "Morning Zen with Coco"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 772
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/geospatial"
---

# Morning Zen with Coco

> 💚 *inhale* hold *exhale* Pause for a moment in the morning and take care of yourself.

[Devpost](https://devpost.com/software/morning-zen-with-coco) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** javascript, openaq, openweathermap, positionstack, slack, webhooks

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for morning zen with coco

## Body

Thoroughly documented collection Morning Zen message from Coco Inspiration 2020 was a challenging year. 2021 is also pretty strange. The physical distancing, waiting for vaccines, not knowing when we will see our friends again and so much more. But we are fighting through it. I am sure you are following your local COVID-19 health guidelines, showing up to work (or school) on Zoom and doing your best. Yay you! The pandemic has certainly taken a toll on our minds, but did you know that while we are sitting at our desks (ok fine, couch) at home, we are also destroying our bodies - quite literally . Problems like insomnia, back pain, hunched over and stiff shoulders, aching eyes and so much more are plaguing many of us because we're stuck at home and not doing much. :( This is a BIG deal. 💚 Taking care of yourself is the best "developer productivity" life hack in the world. We all know that we should drink more water, stretch, take breaks, ... but it's tough to remember to do them all the time, right? What it does Well, Coco is here for you. 🐶 Every morning, Coco will send you a gentle message in a private slack channel to remind you to take care of yourself and to help kick start your day on the right foot with: Local weather report Air quality alerts 5 minute stretching exercise 5 minute meditation/reflection time Random Zen Tip of the Day How I built it Coco relies on 3 freely available APIs to gather data about factors that may affect a developer's productivity. The Position Stack API converts the developer's address to coordinates. The OpenWeatherMap API provides a detailed weather report from around the world, while the OpenAQ API returns real-time air quality report from 110 countries. Challenges I ran into The OpenAQ API, an open-source project run by a D.C. based non-profit, is struggling these days with technical issues. I have been using this API for 5+ years and never had this issue with it. Hopefully it is temporary. For the past few weeks, the API is returning quite a few 504 Gateway Time-out, 503 Service Unavailable Error, and the catch all 500 Internal Server Error response status codes. I mitigated this by handling the 5XX status code use case with some Javascript. Accomplishments that I'm proud of I'm proud of building something that I'd use myself and feel comfortable recommending to my friends and coworkers. I didn't only spend my time on the technical aspect of building this Postman collection. I also took care of thinking through how a developer can easily get up and running with it with clear instructions (e.g. how to get API keys) and educating them about why things like air pollution matter to developers and other knowledge workers. What I learned I learned that it is possible to use Postman Collection Runners to build and launch bots for any platform that has an API, like slack or twitter. The finish line for several side projects that I am still working on feels so much closer now that I know this option is available. A few API calls with some javascript scripting pre and post requests is all I need in most cases. Secondly, I had no idea it was so easy to publish API docs with Postman. All it took was two clicks and I was done. 🤯 What's next for Morning Zen with Coco I have only scratched the surface with what Morning Zen with Coco could do. First of all, I would move from using Slack webhooks to the Slack API to get more flexibility in formatting and delivering Coco's message. Instead of delivering all 5 tips in one go. I'd like to send one tip at a time with a button to move on to the next one. Also, with the Slack API Coco can send reminders like "drink water" or "look away from the screen" a few more times in the day. Use Slack buttons to let developers select how much time they have today to stretch, e.g. 5 mins, 10 mins, etc. Each button will link to a different YouTube video with morning stretches. Integrate with Spotify API and link to a different productivity/coding playlist daily. Integrate with Outlook or Google Calendar API to schedule time on the calendar to stretch or take a break depending on that day's schedule. Slack seems like the optimal platform for Coco's message, but I'll need to do some customer developer interviews to learn whether email (SendGrid), SMS (Twilio), WhatsApp (Twilio) or another platform may be more effective. <div