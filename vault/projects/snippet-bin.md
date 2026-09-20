---
slug: "snippet-bin"
url: "https://devpost.com/software/snippet-bin"
title: "clpbcpy"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 163
team_size: 0
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# clpbcpy

> Do you find yourself emailing links and media to yourself? Would you prefer to use a self-hosted, local solution? clpbcpy is a simple local sharing solution with a RESTful API for just this purpose.

[Devpost](https://devpost.com/software/snippet-bin) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[geospatial]] [[structured_db]]

**stack** h2, hibernate, http, java, jpa, json, lombok, spring

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clpbcpy

## Body

Inspiration I realized there was no popular, self-managed, open-source clipboard synchronization app. What it does Stores clippings posted to the root endpoint /, retrieves them on demand and lets you delete clippings as needed. How we built it I created a simple spring boot service with a file-based database using open-source technologies, tested it using Postman requests. Challenges we ran into Data security. Currently the service can be used only in a local network, as the service does no hashing or user verification at the moment. Accomplishments that we're proud of Quick startup-time, clear mapping of endpoints, brevity of code. What we learned Clear structure of even the simplest app enhances the process of development by a great deal. What's next for clpbcpy Hashing and authentication! The most straightforward modification the author is planning to make is to integrate Spring security (authentication and authorization of different users) and the hashing of stored clippings to make it suitable for use across different networks. <div