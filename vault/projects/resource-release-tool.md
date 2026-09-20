---
slug: "resource-release-tool"
url: "https://devpost.com/software/resource-release-tool"
title: "Resource & release tool"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 143
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
---

# Resource & release tool

> A tool to provide resource usage estimations and to provide a central resource for scattered teams that call nested services in large companies with thousands of services .

[Devpost](https://devpost.com/software/resource-release-tool) · hackathon [[The Postman API Hack]]

## Facets


**stack** golang, svelte

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i am proud of
- what i learned
- what's next for resource & release tool

## Body

Inspiration Work in a medium sized company with new apis being built every day . It's hard to keep track of what services depend on what What it does A library that tracks the services that an API is subscribed to and is connected to postman. also autogenerates the necessary payload it needs. Wraps a mini router to prevent double definitions of Handler functions. How I built it Super rough around the edges . planned and implemented in 2 days. Challenges we ran into Time. Time. Time. Accomplishments that I am proud of The library has the basic functionality working. What I learned Learned that postman has an enterprise offering. Didn't know that . Just thought everything was out there and free What's next for Resource & release tool Polishing it . Using an in-memory cache to keep track of the resources. <div