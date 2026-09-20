---
slug: "docker-registry-image-reader"
url: "https://devpost.com/software/docker-registry-image-reader"
title: "Docker Registry Image Reader"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 151
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/video_visual"
---

# Docker Registry Image Reader

> This collection interacts with the Docker Registry HTTP API (v2), allowing a Postman Monitor to forward on your webhook the image tags on a scheduled basis

[Devpost](https://devpost.com/software/docker-registry-image-reader) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[video_visual]]

**stack** javascript, postman

## How they structured the write-up

- inspiration
- what it does

## Body

Inspiration I felt the necessity to automate some checks that can be done on a private Docker registry given the growth of the number or docker images/version in each company in the latest years. I've created just a couple of automated request but I think the results could already be effective What it does This project interacts with the Docker Registry HTTP API (v2), allowing the management of docker images on your registry via Rest API instead of docker command. This may be useful if you can't use the docker command directly in some environments, or if you want some automation to check/pull images when a new version is released on your registry. By using a Postman Monitor, the first scheduled request will fetch all images from your registry and then the second request will run in a loop, sending the images current tag to a webhook of your choice. <div