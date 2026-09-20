---
slug: "azure-issue-manager"
url: "https://devpost.com/software/azure-issue-manager"
title: "Azure Issues Manager"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 305
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Azure Issues Manager

> This project was designed to effectively make use of Azure Custom Vision to manage issues on GitHub. It warns users that post adult content in the issue or pull request section of GitHub to delete it.

[Devpost](https://devpost.com/software/azure-issue-manager) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]]
**user** [[general_public]]
**substrate** [[code_repository]] [[video_visual]]

**stack** azure-computer-vision, github-actions, github-workflow, javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for azure issue manager

## Body

AI bot Inspiration I've always wanted to implement AI in one of my builds. Having little experience with AI, I figured out that I could still create smart and intelligent apps turbo-powered by Azure AI in a seamless way. I really love the extra capabilities that GitHub action provides for a repository, so I decided to create a GitHub action that manages issues on GitHub using Azure Computer Vision What it does My build monitors comments in pull requests and GitHub issues for illicit images and warns the user(poster of the illicit image) to delete it. How we built it My build works with a GitHub workflow that listens for an issue_comment and issues event from a repository. Anytime an issue is created, edited or opened, the workflow fires immediately calling the Azure issue manager to analyse the content of what was posted. If the content is acceptable, the user(poster of the image or comment) isn't warned, but if the content is not accepted, the user is warned to delete the image. Challenges we ran into I initially had issues retrieving the event context, so I tried hacking my way through it, only to find out that there was actually a function that I could have called to obtain the event object. Accomplishments that we're proud of I learned more about GitHub actions and how to integrate a GitHub action with Azure Custom Vision . I also got to make my Azure Issue Manager action available to the public at GitHub Market Place What we learned I learned how robust Azure Cognitive Service is and how the service makes it easy for users to build smart and intelligent applications. What's next for Azure Issue Manager I would like to try out Azure text analytics to flag profane words in GitHub issues and pull requests <div