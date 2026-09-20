---
slug: "send-it-later-for-comments-mgacjz"
url: "https://devpost.com/software/send-it-later-for-comments-mgacjz"
title: "Comment scheduler"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 516
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
---

# Comment scheduler

> Schedule delivery of your comment in Jira ticket, just like in Slack scheduled messages or in Gmail scheduled emails.

[Devpost](https://devpost.com/software/send-it-later-for-comments-mgacjz) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[developer_tools]]

**stack** atlaskit, forge, javascript, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for comment scheduler

## Body

Inspiration I was inspired by a feature that is present in Gmail and in Slack. This feature can be considered as bread-and-butter tool for digital communication, because it gives you control of when the message will be delivered. This makes sense also for Jira tickets, or JSM requests. What it does As a user you can schedule comment delivery: afternoon, tomorrow, next week, or any custom date and time. Then you can also see what is scheduled for delivery in each issue, so that you or your colleagues don't duplicate messages. How I built it I started from example TODO app which turned out to be a good starting point and a playground for learning purposes. Eventually I had to rewrite everything. I'm using the scheduled-trigger functionality on the backend, and custom UI with React and Atlaskit on the frontend. The implementation is super simple. Challenges we ran into This is a mix of problems caused by lack of experience on my side, or alternatively by limitations of Atlassian Forge. This is my very first Forge app, so I was discovering everything on the go Forge tunnel functionality did not work well for me (Cmd+C seems to not kill it permanently - need to completely reinstall the app) I wish this functionality could be blended into Jira UI, but apparently it is not possible with Forge (I'm not sure if it makes sense to raise such feature request to Atlassian Forge team) There are several constraints in the API: minimum interval for scheduled trigger is 1 hour, I wish it could be more granular ( https://ecosystem.atlassian.net/browse/FRGE-390 ) I cannot impersonate users from scheduled trigger handler, so the comment author is the app ( https://ecosystem.atlassian.net/browse/FRGE-389 ) Forge does not work with JSM projects yet, while comment scheduling seems to be essential for service desk projects ( https://ecosystem.atlassian.net/browse/FRGE-391 ) I cannot reload Jira comments panel from my app code ( https://ecosystem.atlassian.net/browse/FRGE-393 ) It is not possible to dynamically resize the issue panel ( https://ecosystem.atlassian.net/browse/FRGE-392 ) Using Storage API for scheduled comments is not the best idea out there - security is an issue, and good old Jira Issue properties might be a better fit. Accomplishments that we're proud of I wanted to create something that is minimalistic in terms of implementation, and yet can bring a lot of value to the user. What we learned Advices to myself: start with unit tests for backend, story book for custom UI - this will boost the productivity tremendously in Forge app development. Otherwise you will waste a lot of time debugging sometimes very trivial bugs with the build/deploy cycle. Make sure you are using Typescript, it will solve many problems for you - automatically! What's next for Comment Scheduler I would like to expand this feature to Jira issue updates, which means for example the possibility to "resolve a ticket after 2 hours", or "assign a ticket to someone next week". Simple automations at your fingertips ! There are quite a few UX quirks, sometimes caused by Atlassian Forge limitations. Certainly I can make the app look much better. <div