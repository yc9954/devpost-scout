---
slug: "lootcode-10"
url: "https://devpost.com/software/lootcode-10"
title: "Lootcode 10"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 362
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Lootcode 10

> If you've ever used Leetcode, you may know that the grind can get a bit boring. Lootcode 10 turns it into an adventure through 8 regions, with AI assistance available if you get stuck on a problem!

[Devpost](https://devpost.com/software/lootcode-10) · hackathon [[ShellHacks 2024]]

## Facets

**user** [[legal_professional]]
**substrate** [[geospatial]] [[web_dom]]

**stack** chainguard, svelte, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lootcode 10

## Body

Inspiration We were inspired to create Lootcode 10 after hearing about Lootcode (the original), which gameifies the Leetcode experience in order to make it more fun. We wanted to take a shot at our own implementation, and we wanted to use this opportunity to integrate an AI assistant, since we think an AI assistant can provide a good opportunity for people to learn how to solve difficult problems that they otherwise might not get on their own. What it does Lootcode 10 offers 8 unique regions to explore (Geometry, Range Queries, Sorting/Searching, Math, DP, Trees, Graph Algorithms, and Strings), each of which offer a set of problems to be solved. The problems are arranged in a directed acyclic graph, and a problem can only be solved if all its prerequisites have been solved first, in order to ensure a specific progression through the game. We also offer an AI assistant that will show up if the user gets an incorrect verdict, in order to help them fix their code and learn how to solve the problem correctly. How we built it We built it using Svelte for the frontend, Typescript for the backend, and we used Chainguard to sandbox solutions that are judged, since users could potentially submit malicious code and we need to handle that case gracefully. Challenges we ran into We ran into issues with styling the large amount of text the AI produces to fit into a box for the judge. Other than that, most of our issues came from coming up with a design for the product that resembled the original Leetcode but had our unique twist. Accomplishments that we're proud of We're proud of having a fully functional website containing a login, map, leaderboard, and an AI coding assistant for problems within a day. What we learned We learned how to use new technologies like Chainguard and Svelte alongside essential communication skills that occurred when we ran into technical issues. What's next for Lootcode 10 We want to patch up Lootcode 10 to look cleaner and fix any possible bugs. We also want to add more language support as we only support C++, Java, and Python <div