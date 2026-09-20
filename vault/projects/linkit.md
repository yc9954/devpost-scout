---
slug: "linkit"
url: "https://devpost.com/software/linkit"
title: "LINKIT"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 518
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# LINKIT

> Chainlink Job Spec creation, testing, and learning tool

[Devpost](https://devpost.com/software/linkit) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

  <sub>weak: simulation_digital_twin</sub>
**domain** [[developer_tools]]
**user** [[developer]]

**stack** chainlink, cypress, go, next.js, react, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for linkit

## Body

GIF Select and configure your job type. GIF Drag from the task handles to add new tasks to your pipeline. GIF As you enter configuration details the 'Codegen' panel will change in realtime. GIF Open the 'Test' panel and enable test mode to parse your job spec and enable you to simulate execution of the pipeline. GIF Once you're happy with your job spec, copy the generated TOML to your clipboard! Inspiration It's my ultimate goal to create a tool that accelerates the creation of decentralised oracle networks. I hope to achieve this by creating an app which 1) helps educate people on how Chainlink works, 2) makes development of job specs easier and 3) helps developers, node operators and users communicate about how a custom DON will work. What it does LINKIT is a web app which enables users to generate job specs by visually dragging, connecting and configuring nodes on a canvas. Enabling 'Test Mode' parses the generated job spec and allows the user to step through execution of their pipeline. Snapshots of the current pipeline variables available for each task and the current result help with understanding and debugging. How we built it LINKIT is an extension of a project I submitted to the previous Chainlink Hackathon named 'Chainlink Job Spec Viz'. In-between hackathons I worked on an API which facilitates running individual Chainlink task code from a custom fork of the Chainlink node software (where internal functions are exposed). Note: Since the API behind this web app was worked on before this hackathon I do not intend for it to be part of this submission Over the past 5 weeks I have worked on integrating the web app with this API and putting logic in place to allow the execution of full pipelines by holding encoded data about the in-progress pipeline run client-side, on top of a bunch of changes to UI/UX. Challenges we ran into The main challenge behind creating this app is the encoding and decoding of data between the Chainlink code written in Go and the web app's Javascript. Designing a user experience which attempts to make the underlying complexity as simple to the user but displays all the essential data has also been challenging. Accomplishments that we're proud of I'm very new to working with Go and it was quite daunting for my first experience of using Go to be working with the Chainlink node software so I'm proud of myself for pushing myself to learn it. What we learned I've learned a lot about the internals of how Chainlink jobs are executed. What's next for LINKIT I'd love to keep working on this app and to take it to production. I have a long list of features I'd like to work on including: Ability to parse an existing job spec and generate the visualization of connected tasks (reversed process) Collaboration and sharing features Full test coverage for the UI and API Full task/job/job-variable coverage Extensive list of examples Support for multiple Chainlink node versions The ability to model interactions between several Chainlink nodes making up a DON (eventually...) <div