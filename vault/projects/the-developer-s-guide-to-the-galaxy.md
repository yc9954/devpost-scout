---
slug: "the-developer-s-guide-to-the-galaxy"
url: "https://devpost.com/software/the-developer-s-guide-to-the-galaxy"
title: "The Developer's Guide to the Galaxy"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 268
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# The Developer's Guide to the Galaxy

> A Postman Collection that creates an automated "Choose Your Adventure" experience enabling the developer to learn about Postman and the Universe around us.

[Devpost](https://devpost.com/software/the-developer-s-guide-to-the-galaxy) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]] [[web_dom]]

**stack** cosmos-db, docker, docker-compose, express.js, image-classification, machine-learning, natural-language-processing, node.js, postman

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what i learned
- what's next for the developer's guide to the galaxy

## Body

Inspiration I was inspired to build this collection by my obsession with space, automation, and machine learning. What it does This collection creates an automated, choose-your-adventure experience for the user. It contains two workflows. The first workflow generates a random question about the Hubble telescope and poses that question to a QnA bot which returns an answer. The second workflow generates a random galaxy image URL and sends the URL to an image classifier which identifies the galaxy in the image. How I built it I built this project using Node.js, Azure Cognitive Services, Cosmos DB, Docker, Docker-Compose, Azure Pipelines, and Postman, of course! Challenges I ran into The biggest challenge for me was keeping everything inside of a Postman Collection. I wanted to create an automated workflow for the user that displayed interesting information. Accomplishments that we're proud of Learning to utilize Postman's tooling for automation was a great feat for me on this project. I wanted to create a seamless user experience, which took learning how to use Postman workflows, variables, and pre-request scripts. What I learned I learned how to use Azure Cognitive Services, Docker in Azure Pipelines, and Postman conditional workflows, tests, and pre-request scripts while building this project. What's next for The Developer's Guide to the Galaxy I would like to build this out to be a larger suite of workflows that result in more knowledge about the Universe, while keeping it completely contained in Postman. The next tangible step is likely to capture weather data from the NASA Mars Weather API and run predictive analysis to generate a Mars Weather Forecast. <div