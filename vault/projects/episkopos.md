---
slug: "episkopos"
url: "https://devpost.com/software/episkopos"
title: "Episkopos"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 318
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Episkopos

> Your smart DevOps virtual assistant to help you accelerate your software delivery in a fast, reliable, repeatable and safe manner.

[Devpost](https://devpost.com/software/episkopos) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** none

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for episkopos

## Body

Inspiration I've been working in the DevOps space for a number of years but it has always been a struggle to get development teams to understand what they need to do to improve their software delivery by adopting DevOps techniques, particularly in relation to the Cultural aspect. Episkopos is greek for "overseerer". A person charged with the duty of seeing that things to be done by others are done rightly. What it does The user enters some values for the 4 key DevOps metrics as defined by the [DevOps Research and Assessment DORA . How we built it The project was built incrementally with one widget type at a time for each metric - crafting the prompt and experimenting with each LLM, until the desired type of response was returned. The widgets were then replicated to represent the other DevOps metrics. Challenges we ran into One of the widgets was required to just provide a single digit score between 0 and 10. It took a while to get the prompt right to return the expected value in the format that was needed. I'd really like to be able to control the size of the images returned. Accomplishments that we're proud of It's been great learning what GenAI can do and how it can be customised to deliver a certain outcome that really provides some value. What we learned I've learnt the importance of prompt engineering but more importantly it's triggered the curiosity to explore the field of generative AI more deeply to see what I can develop to bring value to the clients that I interact with. What's next for Episkopos I'd like to develop this using an AI avatar from Soul Machines integrated with Amazon Lex and Bedrock to provide a User Interface that someone can interact with in a more natural way. Also to augment the foundational model with some data from DORA using embeddings. <div