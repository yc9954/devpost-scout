---
slug: "pandora-s-box-jlp6vm"
url: "https://devpost.com/software/pandora-s-box-jlp6vm"
title: "Pandora's Box"
hackathon: "LaunchHacks IV"
organization: "LaunchHacks"
winner: true
words: 797
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "substrate/video_visual"
---

# Pandora's Box

> A fine-tuned LLM powered HTTP honey-pot.

[Devpost](https://devpost.com/software/pandora-s-box-jlp6vm) · hackathon [[LaunchHacks IV]]

## Facets

**mechanism** [[on_device_local]]
**substrate** [[video_visual]]

**stack** docker, go, nextjs, python, react, typescript

## How they structured the write-up

- inspiration
- what is pandora's box?
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pandora's box

## Body

Web interface Web interface continued Training the model Inspiration Honey-pots are an excellent way to stay ahead of attackers that have breached a network. However, the issue is they rely on static responses and are either too complex or too obvious. So we thought why can't an LLM be used to generate custom responses to every request. After some research we found there was one or two projects that utilised regular online LLMs to provide responses, but the slow repsonse times are a bit of a giveaway that they aren't a regular server. To fix this we set out to create our own locally hosted honey-pot, with a specialised and local LLM. What is Pandora's Box? Pandora's Box a LLM powered honey-pot. A security measure, who's goal is to study cyberattacks and deflect attackers away from real systems. This is achieved by training our model to provide context-aware responses to web requests. This makes it less likely for an attacker to realise they're going after a honeypot and provides more insight into their methods and how to react. How we built it To build Pandora's Box we had to first ensure the viability of a locally run model in both its speed and accuracy. After both collecting our own data and synthesising some extra we finished our first training run through with distilgpt2. By utilising an external LLM we were able to polish and improve our python program to synthesise data, making it far more realistic and reliable for further training. This resulted in a model that was viable running on a CPU as well as greatly benefiting from a GPU. While further training of the model commenced we designed a backend in Go. This backend hosts the HTTP server to capture requests and connects to a front end web interface whcih uses a combination of React, TypeScript and Nextjs. This allowed us to record statistics and provide a convenient interface for monitoring the honeypot. Additionally we did not have time to train another model but wanted to be able to provide a classification for the requests as to whether they were malicious or not. To do this a user can hook up their Gemini API key which can be used for free for testing. This gives further insight into the nature of the requests. This is all brought together with custom Docker images for each component, and a Docker Compose stack to bring it all together and make it as easy as running a single command to fire up. Throughout the development process we also used AI to help create boilerplate code in the data synthesiser, design a format conversion for JSON and to better understand errors that arised. Challenges we ran into Our biggest challenge during this project was trying to find data suitable for training. Without being able to find suitable data we had to turn to learning how to collect our own as well as synthesising events that we didn't run into naturally. Additionally our team member who would train and fine-tune the model did not have a powerful enough computer to be able to optimise it within the timeframe. This meant we had to spend quite a bit of time trying to setup a way for them to ssh into another team members computer in order to run more training sessions during the short timeframe for the hackathon. Accomplishments that we're proud of We are proud of how well all the different parts of the project has come together for the final product. Between the front-end, back-end, and LLM each of it performs its job well and meshes with very little friction. Our honey-pot is capable of times as low as 1.4 seconds in our testing which while not ideal is a large improvement from where we started. What we learned We've learned a lot during this project and have come out with many new skillsets. We can now confidently work across machines utilising ssh and tail scale, gained valuable experience in Go, and got hands on practice with fine-tuning a LLM. Additionally we're better equipped for working in a team environment and learnt how to most efficiently divide up the work and play to each persons strengths. What's next for Pandora's Box Going forward with Pandora's Box we would love to further expand the capabilities of our honey-pot from just an HTTP server to being able to respond on almost any port. For this we would need to find ways to gather a large amount of training data due to the low availability of it online. If we can polish the project to a professional level, launching it as a service is a long term goal of ours. Potentially providing the computing power for super low response times to customers. <div