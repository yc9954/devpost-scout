---
slug: "apicasso"
url: "https://devpost.com/software/apicasso"
title: "APIcasso"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 303
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/web_dom"
---

# APIcasso

> No API? No problem! APIcasso uses Cohere to generate complete data from URL and empty schema, offering permanent access URLs and schema-based automation to streamline development and prototyping.

[Devpost](https://devpost.com/software/apicasso) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** cohere, eth, next.js, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for apicasso

## Body

Inspiration No API? No problem! LLMs and AI have solidified the importance of text-based interaction -- APIcasso aims to harden this concept by simplifying the process of turning websites into structured APIs. What it does APIcasso has two primary functionalities: ✌️ Schema generation : users provide a website URL and an empty JSON schema, which is automatically filled and returned by the Cohere AI backend as a well-structured API. It also generates a permanent URL for accessing the completed schema, allowing for easy reference and integration. Automation : users provide a website URL and automation prompt, APIcasso returns an endpoint for the automation. For each JSON schema or automation requested, the user is prompted to pay for their token via ETH and Meta Mask. How we built it The backend is Cohere-based and written in Python The frontend is Next.js-based and paired with Tailwind CSS Crypto integration (ETH) is done through Meta Mask Challenges we ran into We initially struggled with clearly defining our goal -- this idea has a lot of exciting potential projects/functionalities associated with it. It was difficult to pick just two -- (1) schema generation and (2) automation. Accomplishments that we're proud of Being able to properly integrate the frontend and backend despite working separately throughout the majority of the weekend. Integrating ETH verification. Working with Cohere (a platform that all of us were new to). Functioning on limited sleep. What we learned We learned a lot about the intricacies of working with real-time schema generation, creating dynamic and interactive UIs, and managing async operations for seamless frontend-backend communication. What's next for APIcasso If given extra time, we would plan to extend APIcasso’s capabilities by adding support for more complex API structures, expanding language support, and offering deeper integrations with developer tools and cloud platforms to enhance usability. <div