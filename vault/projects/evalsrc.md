---
slug: "evalsrc"
url: "https://devpost.com/software/evalsrc"
title: "EvalSrc"
hackathon: "Wix Make-A-SaaS Hackathon"
organization: "Wix"
winner: true
words: 323
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# EvalSrc

> Run arbitrary code from your users without worrying about the infra.

[Devpost](https://devpost.com/software/evalsrc) · hackathon [[Wix Make-A-SaaS Hackathon]]

## Facets


**stack** javascript, node.js, typescript, velo, wix

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for evalsrc

## Body

Inspiration The idea for this platform came about when I was making a chat application. And an eventual feature that I wanted to have was that users could send code to other users and the recipient wouldn't have to download a whole runtime or install any tools or plugins just to be able to see what the code does. But soon I worried that for a chat platform this was a very, very tedious task. No one wants to have to worry about how the code is going to be ran. The infrastructure that it will be run on, the safety, security, all of it. Thus, Evalsrc was born. What it does What we aim to do is provide a simple interface for our users so that all they have to do is make a simple post request with the code they want to run to our API and we give them the result. How we built it Our frontend is built using Wix and a provided template from them. Our backend is built using Velo Backend Functions which allows us to have a serverless way of ingetsing code. Our code runners are built using TypeScript & Node.JS. Velo APIS being used: wix-http-functions , wix-pricing-plans-backend , wix-data , wix-fetch Challenges we ran into There were various permission gates that we had to figure out how to navigate when it came to using some of the Velo APIs. We were eventually able to navigate these with ease. Accomplishments that we're proud of We're proud of how we have the code caching set up so that even stylistic changes in the code like adding an extra space in the function body will result in the same code cache being returned. What we learned We learned a lot about how serverless environments work, the limitations and usecases for Velo, and the various APIs that velo provides us for interacting with data. What's next for evalsrc <div