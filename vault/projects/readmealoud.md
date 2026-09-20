---
slug: "readmealoud"
url: "https://devpost.com/software/readmealoud"
title: "ReadmeAloud"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 366
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
---

# ReadmeAloud

> A simple tool to provide an easy and efficient way to understand open-source projects for everyone especially visually impaired or sight-impaired friends

[Devpost](https://devpost.com/software/readmealoud) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]]
**user** [[developer]] [[general_public]]

**stack** azure, azure-cognitive, blazor, dotnet, github, readme

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for readmealoud

## Body

ReadmeAloud-Logo Architecture Inspiration As a developer, we often came across many open source projects in GitHub, in which Readme.md is one of the first files which we will see 🤩. It is the simplest way to understand, what the project is about, how to use it, and other related information (kind of documentation). Moreover having a good readme file which will help and attract many contributors. However, it's always been challenging for any low vision or visually impaired developers and contributors. As most of the readme content is in the form of text, which is quite difficult for them to read and understand. What it does "ReadmeAloud" is a simple tool that can convert the raw-text from any public GitHub readme file to Speech 🎤 and also provides a way to download it in form of an mp3 file 🎵 How we built it Using Azure Cognitive Text to Speech API Challenges we ran into Understanding Server-side Blazor application. Accomplishments that we're proud of Focused more on the real-life use-case for solving the low vision or visually impaired developers and contributors. What we learned Learning Blazor What's next for ReadmeAloud The architecture itself is currently highly coupled with the server(blazor), we can make it more scalable by introducing a separate layer for the cognitive calls i.e, the azure function Current limitation to convert only the public GitHub repo, we can improve that to private repo also by including some additional authentication. Engish language is the by default for both text and speech conversation, we can improve that easily, since azure cognitive service has a very wide variety of supported languages I'm not a front-end guy 🙈. So feel free to contribute to readmealoud with your creative ideas or UI/ If the Readme file is too long then the speech conversation would take more time some time it eventually timed out too. Currently, it is suited for small readme files. We can improve that by changing the architecture which we discussed above. We can also improve the design with more accessibility for people with low vision like providing voice search capability input for GitHub repo details. You can find the full detailed article about readmealoud here <div