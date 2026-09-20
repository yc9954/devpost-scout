---
slug: "bugtrap-error-tracking"
url: "https://devpost.com/software/bugtrap-error-tracking"
title: "BugTrap: Error Monitoring"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 372
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# BugTrap: Error Monitoring

> Capture errors, monitor them in Confluence and track them as issues with Jira.

[Devpost](https://devpost.com/software/bugtrap-error-tracking) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** forge, javascript, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what i learned
- what's next for bugtrap: error tracking

## Body

Inspiration There are many tools that can be used to monitor errors in production web applications, but what if there was a way to monitor those errors on a Confluence page and also easily create Jira issues for those errors at a click of a button? That's where Bug Trap comes in!! What it does Bug Trap is a Forge application for Confluence that helps teams capture and monitor errors in production web applications, teams can also easily create Jira issues from those errors. Bug Trap also allows teams to filter the error information, see which errors occur the most, and see the number of affected users, this can help teams decide on which issues should be prioritized. When a user experiences an error, Bug Trap also provides the ability to collect additional feedback in addition to the error information that is already collected. How we built it The solution is made up of 2 components: The first is a NodeJS package that developers can add to their React web applications. This package is able to catch any error that might happen in the React component tree, log those errors and send them over to the Forge Application. The second part of this solution is a Forge app, this app receives the error information via a web trigger and displays that information neatly on a Confluence page. I used Forge UI to build the user interface and used the Jira API to allow users to be able to create issues from those errors at a click of a button. Challenges we ran into Trying to figure out how to protect forge Webhooks from unauthorized access was a challenge that I'm still trying to solve but one idea I had is to generate an API key and store it in the Forge storage API. Accomplishments that we're proud of Building a product that actually works and can be useful to me. What I learned I learned a lot about creating Forge applications, such as using the storage API, and Webhook triggers I also learned how to create a Node package for NPM and Yarn. What's next for BugTrap: Error Tracking Support for more web frameworks Angular, Vue, etc, and some minor upgrades. <div