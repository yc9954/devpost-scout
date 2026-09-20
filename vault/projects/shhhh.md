---
slug: "shhhh"
url: "https://devpost.com/software/shhhh"
title: "Datree Automated"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 355
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "substrate/code_repository"
---

# Datree Automated

> One CLI tool to rule them all 🔨

[Devpost](https://devpost.com/software/shhhh) · hackathon [[Cloud Native Hackathon]]

## Facets

**domain** [[civic_government]]
**substrate** [[code_repository]]

**stack** datree, node.js, typescript

## How they structured the write-up

- 💡 inspiration
- ⚙ what it does
- 🔧 how we built it
- 🤔 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🤠 what's next for datree automated

## Body

Datree Automated 🔨 💡 Inspiration While working towards Datree's sponsor track we realized that building new policies for each use case is redundant and why aren't we trying to just automate it. And we did just that by pivoting to build this tool on the last day of the hack! ⚙ What it does Our CLI tool takes in a Kubernetes config file, parses it using our custom Datree policy generative algorithm to produce a policy.yml file that can be published to test configurations using Datree. Features Parsing YAML config properties Support for Resource Limits. Ex: maximum: 25 Supports enums, string and limit values 🔧 How we built it The tool is written in Typescript and we've used Node to run the script. 🤔 Challenges we ran into We ran into a bunch of challenges while building this, mostly while trying to figure out where we can find the Kubernetes schemas to use ( the swagger file on the K8s repository is very difficult to parse). We tried using Kubeconform but ultimately decided to use Kubernetes JSON Schema for our use case. Because of the decision we made to pivot on the last day of the hackathon, our biggest constraint became time. However, we believe our hack is original and innovative enough for us to take this risk and showcase all the possibilities of our idea! 🏆 Accomplishments that we're proud of Getting it to work Making it stable enough to be used for generating policies 📚 What we learned Increased our understanding and interest in Kubernetes The problem that Datree is solving and a bit about how it works under the hood 🤠 What's next for Datree Automated We want to integrate our tool into the existing Datree CLI package and provide an automated solution for every user who wants to build a custom policy. Our tool can also be built into a web app that can generate a Datree policy from a user's Kubernetes configuration file. Thanks for checking out our hack! 🚀 We would love to talk all about it or if you run into any issues trying to run it <div