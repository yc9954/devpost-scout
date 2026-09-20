---
slug: "syncup-dmi15k"
url: "https://devpost.com/software/syncup-dmi15k"
title: "SyncUp"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 455
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# SyncUp

> Enabling DevOps teams to stay in sync with internal API changes.

[Devpost](https://devpost.com/software/syncup-dmi15k) · hackathon [[Codegeist 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** forge

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for syncup

## Body

Adding API Subscribing to API Updating API Jira Updates Received by Subscirbed Project Updating, Removal and Deprecation of API Inspiration We talked to several developers about how they keep in touch with changes in the internal API changes of their company and most of them agreed that this was a hassle. This is when we thought of leveraging the Jira platform to give such updates because it falls in naturally with the development workflow. What it does SyncUp allows developers to subscribe to APIs on Jira. Whenever an API is updated, all the projects that have subscribed to the API will receive Jira Issues to notify them of the update. How we built it We used Forge's UI Kit for the UI, Atlassian APIs and Triggers for Creating issues whenever an API is updated, Forge Storage APIs to track subscriptions and store APIs. Challenges we ran into It was the first time we worked with Atlassian and Forge, hence it took a while to get familiar with the platform. Deciding where to place our app on the UI, so as to cause the least friction in the development workflow required some time. Accomplishments that we're proud of We helped Puffy's team prevent abrupt game crashes :P (Refer to the demo video). We feel that this product accomplishes the goal of helping developers stay updated with internal API changes. The idea and design is very simple yet we feel that this solves a prominent problem, the elegance of the solution is an accomplishment that we are proud of. What we learned To use Forge platform and develop Atlassian applications The Jira workflow and about Agile and Scrum While coding we came across some bad coding patterns that we did and realized how we could solve/prevent this in the future. What's next for SyncUp Some features can be added to SyncUp to make it amazing, such as: Reading the codebase and extracting the API dependencies (Either from files such as package.json or from the code itself using some script) to update the API dependencies automatically rather than all of them being entered by the user. Linking confluence blogs with the Jira tickets. To elaborate, while a developer is writing about an API change in confluence, there should be a feature to allow him to send Jira updates to all projects subscribed to the API. This will make the workflow even better because it is natural (and perhaps, required) for developers to write API updates on confluence. Give developers insights as to which all programs/projects will break if they update their API before they update the API. This can give the teams some time to discuss with each other about the update before going for the update. <div