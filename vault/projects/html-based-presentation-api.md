---
slug: "html-based-presentation-api"
url: "https://devpost.com/software/html-based-presentation-api"
title: "HTML-based Presentation API"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 283
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# HTML-based Presentation API

> An API for building presentations with web technologies over the 'net. Plus, some additional options in other collections.

[Devpost](https://devpost.com/software/html-based-presentation-api) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[code_repository]] [[web_dom]]

**stack** css3, express.js, heroku, html5, javascript, jsdom, postman, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for html-based presentation api

## Body

Inspiration I was inspired by libraries like Reveal.js and my wish to explore the creation of presentations using open web technologies. What it does In the HTML Presentation API collection, there are endpoints for an API that allows one to create, manipulate, download, and delete presentations made with HTML, CSS, and JavaScript. The MS Office Web Viewer collections show to display previews of Microsoft PowerPoint presentations (and other types of files) in the browser. The WOPI collection contains some endpoints used in WOPI to create and edit PowerPoints. How I built it The implementation of the HTML Presentation API uses JavaScript, Express.js, and jsdom. The corresponding demo uses React and is deployed on Heroku. I used Postman to form the API collections submitted here. Challenges we ran into I haven't used Postman in a project before, so I had to learn about some of Postman's features. I also don't do back-end of server-side development often. Also, it was a bit difficult to find 'prior art' that I could relate to this project. Accomplishments that we're proud of To support using 'cursors' or 'locators' into the tree structure of a presentation to edit the presentation, the implementation internally creates a flat array representation of the presentation and computes indices into that array. This idea was somewhat inspired by quick-lint-js , which uses 'locators' to keep track of locations in source code (although I'm not sure how exactly quick-lint-js' locators work). This is also my first project where I've deployed a React website something like an Express server. What's next for HTML-based Presentation API I want to make the API and its implementation more robust, and create a better demo application for the API. <div