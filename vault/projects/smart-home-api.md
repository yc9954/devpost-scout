---
slug: "smart-home-api"
url: "https://devpost.com/software/smart-home-api"
title: "Smart Home API"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 219
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Smart Home API

> Aggregates smart home devices from different vendors so they can be controlled using a single API. Aim to use Postman Monitoring to schedule smart devices e.g. turn lights on at 9am.

[Devpost](https://devpost.com/software/smart-home-api) · hackathon [[The Postman API Hack]]

## Facets


**stack** node.js, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smart home api

## Body

Inspiration Smart home devices from different vendors have their own proprietary applications for controlling the devices. This makes home automation a challenge when you have devices from different vendors. I wanted to create a single web api to manage these devices. What it does Single REST API for controlling smart home devices from: tp-link samsung-tv How we built it We built the REST API using node.js & express. This API interacts with the smart devices over the local network. We then created a Postman collection so the different requests could easily be accessed. Challenges we ran into Finding documentation on how to control the smart devices over the network. It's normally suggested to control the devices using their proprietary mobile applications but it is also possible to communicate with them over TCP. Accomplishments that we're proud of We managed to get something practical to work. This is going to be very useful for us. What we learned We learned about smart devices and how to control them over TCP. What's next for Smart Home API We would like to add security to our API & host it somewhere public so we can use Postman monitors to schedule our devices to turn on at specific times etc. We would like to interact with more smart devices from different vendors. <div