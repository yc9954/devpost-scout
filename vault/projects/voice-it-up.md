---
slug: "voice-it-up"
url: "https://devpost.com/software/voice-it-up"
title: "Voice It Up"
hackathon: "Codegeist Unleashed"
organization: "Atlassian"
winner: true
words: 767
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# Voice It Up

> Resurrect dark data to life with AI - Let developers focus more on productive things - Treat AI as an ally, not as an enemy

[Devpost](https://devpost.com/software/voice-it-up) · hackathon [[Codegeist Unleashed]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** ai, azure, forge, javascript, openai, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for voice it up

## Body

Architecture Diagram Output - What's the update? Output - Can it be reassigned? Output - Assess Commit Quality? Output - Whom to assign? Output - Get story points? Team Details Usage Confluence Page Forge Storage API BitBucket Repo Commits Forge App - Folder Structure Azure OpenAI Service Usage The Squad Inspiration Every time I attend a scrum call, it's taking away my productive time, it might not be the case for all, but when you work on a critical deliverable, distractions like these can easily be boring for a developer. This is just me but when I write code, I just need to eat something at my desk, visit the restroom, and sleep and repeat the same thing over again. Most or all of the hackathons I've participated in are of that sort, I just want to write code all day and complete it as soon as possible. Even when I work at my office, I prefer to have as less distractions as possible. This way you'll save developers time and thereby save 10 to 25% of developer's time every week. What it does It can help in two different scenarios - The following are the features you can use, Daily Scrum Call update, What's the update? 🗣️ - You're on a scrum call with your team and the AI can give you the ticket update instead of the developer Can it be reassigned? 🤔 - You can use this to see if there is anyone else who can take up this ticket except the current assignee Assess commits quality? 🧪 - Score the commit messages of the developer in the range of 1 to 5 Assess code quality? 👾 - Analyze the BitBucket repo and provide a rating in the range of 1 to 5 Backlog Grooming, Whom to assign? 💬 - This can give you a fair suggestion on whom to pick for the ticket Get story points? ✏️ - This can help in proving story points based on the Jira ticket description Get ticket labels? 🏷️ - This can assign labels to the current Jira ticket How we built it Azure OpenAI Service - Make Chat Completion API calls Jira Rest API - Access Jira ticket descriptions and assignee BitBucket Rest API - Access repo commit messages Confluence Rest API - Access page details (team details and logging pages) Forge App Storage - Store the usage logs of each user node.js - Building the code for Forge backend Challenges we ran into Getting the confluence page details and formatting has become a bottleneck during the final phase of the development I was not able to use BitBucket context and Confluence context in the Jira instance so I've to use the Rest APIs to get things done A lot of node and React stuffs are not available in Forge (window.speechSynthesis) - was struggling to make it work We've to use Form if I've to use toggle button with @forge/ui node package- can't find a workaround for it Was not able to access confluence page data with the older access token, I've to create a new token after the confluence page was created to access the data Accomplishments that we're proud of With all the above things, was able to make things work in a week Successfully integrated Jira, BitBucket, and Confluence Rest APIs in one place and have respective handlers Was able to use the Form submit button to toggle between feature sets Added Response time and Tokens used in the UI to make the developer aware of how much he is costing each time Added a Logging toggle button to log the requests made to each feature both on a Confluence page and via storage API What we learned It was my first Forge application and I'm pretty satisfied with the results How to write async JS code which interacts with Azure OpenAI Service How to dynamically update states based on user action Calculate response time with async functions How to connect multiple Rest API and interoperate between them to execute a single action How to write optimized prompts to get the desired results from GPT-4 What's next for Voice It Up Let it out on Atlassian Marketplace to get more feedback Definitely integrating the Jira sprint management and how and when to start a sprint Adding a feature to assess the priority of each ticket based on the project goals and other parameters Add temp storage for previous results to show up , this might come in handy when you want to see how the ticket summary has evolved along the sprint <div