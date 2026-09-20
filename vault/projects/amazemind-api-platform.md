---
slug: "amazemind-api-platform"
url: "https://devpost.com/software/amazemind-api-platform"
title: "Amazemind API Platform"
hackathon: "Go Hack"
organization: "Google"
winner: true
words: 478
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Amazemind API Platform

> API platform for managing and solving Katas — programming tasks of any complexity.

[Devpost](https://devpost.com/software/amazemind-api-platform) · hackathon [[Go Hack]]

## Facets

**domain** [[transportation]]
**user** [[frontline_worker]]
**substrate** [[code_repository]] [[video_visual]]

**stack** cloud-build, gcp, gin, github, go, postgresql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for amazemind api platform

## Body

Inspiration There are a lot of platforms for automated programming challenges solving right now (Codewars, Leetcode, etc). But the implementation of their checking process is hidden and is usually limited to a single file. The goal of this project is to create an open highly-customizable Kata management platform that could be used for creating easy or complex programming challenges (for example, a Spring project with intentional errors to be fixed or a Python Django project where a new template should be created) and also validating the users' attempt to solving those challenges. Another driver was to explore how the simple and effective API of the Cloud Build service could be used for running some tasks like Kata validation or submission check. What it does The Amazemind API platform provides a REST API for managing Katas and users' submissions (attempts to solve Katas). It defines the open standard of Kata, which includes: Dockerfile, where you are free to set up the testing environment as you need; tests, for validating the user's attempts; source, the boilerplate code that can be as complex as needed - it can include the whole Django project or several Go modules; Documentation on how to get started. The API platform of this project is responsible for validating such Katas and building images that later will be used for validating users' submissions. Through the API platform, the users will be able to select the Kata they want to solve and the platform will create a boilerplate repository in their Github account. To solve the Kata user must make some changes to the created repository, push the changes to it and start the checking process. How we built it The API was built with Go and Gin framework. For git management, it uses Github API and for the heavy-lifting tasks like building images for Katas and running tests, it uses the Cloud Build. The API is deployed on the Cloud Run which is used for Kata management and also serves a Pub/Sub endpoint for events from Cloud Build. Challenges we ran into The major challenge was to create an E2E testing suite for the pub/sub integration. This part still requires some setup for local development but works well in the Cloud Build environment. Another issue is the code architecture. I've already completed several rounds of refactoring but it's still far from perfect. Accomplishments that we're proud of The fact that Cloud Build could be efficiently and robustly used for these types of tasks. I'm also happy that I was able to complete the goal - validating and later sending submissions for Katas. What we learned Learned a lot about Go and Github API. What's next for Amazemind API Platform After catching up with code coverage the next step would be the creation of a web client for more convenient access to the project. Logo attribution: https://www.flaticon.com/free-icons/brain <div