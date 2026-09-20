---
slug: "wit-ai"
url: "https://devpost.com/software/wit-ai"
title: "Wit.ai CI and CLI"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 267
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/code_repository"
---

# Wit.ai CI and CLI

> Create a production-ready solution using Wit.ai and Implement Continuous Integration/DevOps best practices using GitHub Actions workflow/Azure DevOps pipeline and Wit.ai CLI created for this tutorial.

[Devpost](https://devpost.com/software/wit-ai) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[code_repository]]

**stack** githubactions, node.js, oclif, typescript, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wit.ai ci and cli

## Body

wit ci Inspiration We wanted to implement DevOps best practices for AI projects to make sure that software engineers and data scientists could work together seamlessly building Wit.ai solutions. What it does A tutorial on how to build CI using GitHub Actions workflows or/and Azure DevOps pipelines for models built with Wit.ai. We built testing framework to run batch tests for Wit.ai and developed Wit.ai CLI (wittycli) for this tutorial. This tutorial helps software engineers and AI developers to follow engineering best practices like continuous integration and deployment and test driven development, pull requests reviews and apply these practices to Wit.ai models. How we built it We used GitHub Actions and Azure DevOps and our own Wit.ai CLI to build workflows for testing and developing models on Wit.ai and we've written a tutorial about how to do it. Challenges we ran into There is no official CLI for Wit.ai, so we've built it ourselves https://github.com/ShyykoSerhiy/wittycli . There is no official "unit testing"/batch testing system for Wit.ai to validate trained Wit.ai model version, so we developed the approach of how as a developer you can test Wit.ai model programmatically by comparing Wit.ai outputs with expected intents and entities and confidence levels. Accomplishments that we're proud of First CI pipeline for Wit.ai models. Our own Wit.ai CLI that's easily extendable and a pleasure to use. Wit.ai model testing framework. What we learned A bit about how Wit.ai APIs work and what to avoid when using it. What's next for Wit.ai CI and CLI Add support for more API calls from the REST API in wittycli Add more examples <div