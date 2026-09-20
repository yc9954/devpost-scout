---
slug: "gitignore-cli"
url: "https://devpost.com/software/gitignore-cli"
title: "Gitignore CLI"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 189
team_size: 0
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# Gitignore CLI

> Download git ignore files through a convenient cli

[Devpost](https://devpost.com/software/gitignore-cli) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** api, golang, postman, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gitignore cli

## Body

Inspiration In order build this Gitignore CLI, from the difficulties that I encounter as a developer. It is a CLI application that allows developer to create gitignore file efficiently without the need for downloading manually or create manually. What it does Create gitignore files, allow to replace, append addition gitignore based on different code types. How we built it The backend API server is designed with Golang, there is scraper to get upto date gitignore files from githubs' official gitignore repository, and finally CLI part is also developed in Golang and compiled to execute on user-end. Challenges we ran into When building this I had following challenges: a. Creating new gitignore files on user-end without additional permission requirements b. Accessing the cli domain, .devcli file was introduced to overcome custom domain issues, and allow developers to host their own server. Accomplishments that we're proud of I am very happy to release this version. What we learned I used postman collections to test my API endpoint and to verify everything before I develop What's next for Gitignore CLI Allow support for multi platforms, right now only tested on linux <div