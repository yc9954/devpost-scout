---
slug: "docker-genius"
url: "https://devpost.com/software/docker-genius"
title: "Docker Genius"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 271
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Docker Genius

> Docker Genius helps you identify and automatically resolve Dockerfile issues.

[Devpost](https://devpost.com/software/docker-genius) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[structured_db]] [[video_visual]]

**stack** docker, go, gpt, hadolint, nextjs, openai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for docker genius

## Body

Left side: your annotated dockerfile, right side: you fixed dockerfile Before uploading dockerfile Inspiration As the Co-Founder of a Docker Hosting Platform I am debugging Issues with Dockerfiles daily. While this is a lot of fun, many issues could be automatically found and fixed. For this, I built Docker Genius. Docker Genius uses ~100 best-practices that are validated using hadolint and fixed automatically using the latest gpt-4 model by OpenAI. What it does Simply upload your Dockerfile and Docker Genius checks its database of ~100 best practices against your Dockerfile. It then annotates everything that it found and fixes it automatically (as far as possible!). How we built it The frontend is a next.js page hosted as Docker container at Sliplane . It talks to an API written in Go that is also hosted as a Docker Container which validates the Dockerfile and uses OpenAI gpt-4 to fix the issues that were found. Since the Dockerfile linting is written in Haskell and the API that uses the linter in Go, using Docker made it super easy to run both in the same environment! Challenges we ran into Making sure that the results were consistently good was challenging. Mostly because gpt-4 is missing context (such as code or configuration files) to be confident in really fixing some issues. Accomplishments that we're proud of I already tested it with 20+ older projects and found a lot of issues that I could easily improve :) What we learned There is an official page with best-practices provided by Docker: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/ What's next for Docker Genius Finetuning of the model/prompt, open-sourcing, and integration into Sliplane <div