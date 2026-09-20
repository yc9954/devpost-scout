---
slug: "so-many-apis"
url: "https://devpost.com/software/so-many-apis"
title: "So Many APIs"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 375
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/legal_professional"
---

# So Many APIs

> "Fun" game to Learn about So Many APIs while also testing your non-computer knowledge!

[Devpost](https://devpost.com/software/so-many-apis) · hackathon [[The Postman API Hack]]

## Facets

**user** [[legal_professional]]

**stack** crypto-js, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for so many apis

## Body

Inspiration I was talking with Brian about how to judge the contest the judges will likely have to sign up for So Many APIs so they can get API keys if they want to really test out a lot of the collections. We came up of the idea that we could create a game where you have to figure out how to get the API key, learn about various APIs, and then sort the collection (or disable certain request) so that you can win. Trying to make hunting the API information into a kind of sick scavenger hunt & using the Postman crypo libraries to make sure you can't cheat. What it does You run a collection and then if all the tests pass you win. RULES: The first request in your collection run must be "First Request" and the last request you run is the request titled "Last Request". You should set your environment variables correctly and save them (for example, setting your API keys). You cannot modify the Pre-request scripts or Tests for any of the requests. You may reorder the requests between First Request and Last Request. You may disable 0 or more Requests. Additional rules are in the documentation for the collection. How we built it We created various Postman Collections with various topics, like "US Presidents", "Favorite Tool for understanding APIs", etc. When you run the "First Request" the scripts will set some environment variables. The next requests (which you must order correctly before running) takes advantage of Using External Libraries and creates crypto hashes based on the responses. The "Last Request" request compares the hash to see if you got everything correct & displays the results in the Visualize tab. Challenges we ran into It took more time to figure out which APIs we wanted than we originally planned for. We are working on another hackathon project too (CoinStop)[ https://jamisonderek.github.io/coinstop.htm ] which took most of our hacking time. Accomplishments that we're proud of Making Postman into a fun game. Learning crypto-js. What we learned there really are... So Many APIs Postman collection runners Crypto-js library. What's next for So Many APIs More Collections (games)! Add Mocks once our quota resets. We used them all in our other hackathon. <div