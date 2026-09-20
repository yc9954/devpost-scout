---
slug: "linkit-0yqkw7"
url: "https://devpost.com/software/linkit-0yqkw7"
title: "LINKIT"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 355
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/code_repository"
---

# LINKIT

> Chainlink Job Spec Editor (existing project upgrades)

[Devpost](https://devpost.com/software/linkit-0yqkw7) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[code_repository]]

**stack** cockroachdb, go, next.js, openai, react, thirdweb, vercel

## How they structured the write-up

- what it does
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for linkit

## Body

GIF Drag n' drop to add tasks to your job spec pipeline GIF Select from a preconfigured example GIF Import an existing job spec to visualize, test and tweak it GIF Use natural language to let the AI generate tasks for your pipeline! GIF Test execution of your pipeline in a simulated environment GIF When you're done, copy the generated TOML to your Chainlink node What it does LINKIT is a web-based, drag n' drop Chainlink job spec editor with an API that enables you to simulate job spec execution in the browser. Note: LINKIT is an existing project that was submitted to the previous Chainlink hackathon. The feature additions that have taken place as part of this hackathon are as follows: Integration with OpenAI to enable the generation of sections of your job spec pipeline with natural language The ability to import an existing job spec (great way to help visualize specs taken from the official docs) User login and saving/loading of job specs UI upgrades and dark/light theme toggle Challenges we ran into While I'm proud at the level of improvement I've been able to make, other commitments have meant I wasn't able to add as much functionality as I would have liked to. As as result, the user profile features are very far from where I would like them to be, and I haven't had the time to upgrade to v2 of the Chainlink node software, or support all of the available job-type-specific variables. Accomplishments that we're proud of The AI generation of tasks is surprisingly good given that I haven't yet trained a custom model but am instead providing as much information as can condense in the limits of a request to Open AI's APIs. What we learned This was my first time using the Open AI APIs, Cockroach DB, thirdweb's Auth module, shadcn's UI component library builder, so I learned a lot about those. What's next for LINKIT With more time and resources I would love to fully flesh out the features which are half-complete and bring a solid app to production so people can make use of it! <div