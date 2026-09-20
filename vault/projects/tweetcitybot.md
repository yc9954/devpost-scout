---
slug: "tweetcitybot"
url: "https://devpost.com/software/tweetcitybot"
title: "TweetCityBot"
hackathon: "Junction 2016"
winner: true
words: 298
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# TweetCityBot

> The smartest Twitter bot that handpicks the best tweets around you

[Devpost](https://devpost.com/software/tweetcitybot) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]]

**stack** bootstrap, geolib, jelastic, node.js, pubnub, radix, react, redux, sass, twitter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tweetcitybot

## Body

The best category All categories Some categories Some details ;) It works on your mobile phone too! Inspiration We wanted to transform Twitter into something more personal that would give you information about what's happening around you and your city. What it does TweetCityBot is the Twitter bot you always wanted. It streams tweets about the most interesting topics around your location. How we built it We took the Twitter API and parsed only the relevant tweets for the user based on different categories and location, improving what Twitter provides through its API. We applied category filters, hashtags and location-based filters. TweetCityBot streams live tweets to your dashboard, using the Twitter Streaming API. Challenges we ran into Twitter doesn't provide a streaming API that filters by category and location so we needed to build our own, parsing the coordinates and streaming live tweets in real time if they are within the Helsinki area. Another challenge has been using the new Jelastic PaaS. It was our first time using it, so we ran into some problems but we eventually managed to solve them and run a Node.js server. We managed to build a continuous delivery pipeline of our Node.js app that automatically gets deployed when there's new changes. Accomplishments that we're proud of Expanding the Twitter API to be compatible with our concept was challenging, so we're proud we've achieved it. What we learned We learned a lot about Jelastic and the Twitter API, how they work and what are the limitations. We've also learned how to overcome this limitations and build a great product for the hackathon. What's next for TweetCityBot We want to take this further. TweetCityBot is a very interesting project and it can become the perfect dashboard for events, companies or even bus stops! <div