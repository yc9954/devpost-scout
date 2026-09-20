---
slug: "mocktape"
url: "https://devpost.com/software/mocktape"
title: "Mocktape"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 310
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Mocktape

> Mocktape is a service that lets you mock a back end with no setup. Just send the response you want in the request itself.

[Devpost](https://devpost.com/software/mocktape) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for mocktape

## Body

Inspiration Image placeholder services where you don't need to setup anything and get an implementation with images in no time and the recurrent issue of having to hardcode data in the front end when an endpoint is still in development, which usually requires non-trivial refactors. What it does Mocktape is a service that lets you mock a back end with no setup. Just send the response you want in the request itself. Don't get block when endpoints are not ready yet. Test client side code end to end with the production request params and responses. All possible http requests and responses with a single endpoint and a simple convention. Everything is handled by code on your side, not accounts or services needed to setup. You can focus on testing your client business logic. Easily promote implementations to production by changing base urls. Backwards compatible requests (your API calls mocks are just ignored in the production back end). Deliver fully fledged features in less time. How we built it It's a simple node app with a single route that ignores all the content of the request and focuses on finding the response mock and returning it. Challenges we ran into Designing the API and finding the most straightforward way to send the mock, that worked across http methods and variations, that was backwards compatible and didn't require a lot of work to undo (go from requesting to mocked api to production). Accomplishments that we're proud of Having a working demo in a short time and thinking in a user centric way. What's next for Mocktape Find edge cases not supported by the tool. Find ways to create mocks so easily and that could be so convenient that could even replace actual back end implementations (i.e. being able to manage the responses in a more flexible way, not just by code). <div