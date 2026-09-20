---
slug: "debttracker"
url: "https://devpost.com/software/debttracker"
title: "debttracker"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 513
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# debttracker

> Technical debt is part of software development, but we should make it transparent and trackable. Debttracker helps developers easily create Jira issues while reviewing code to track of technical debt.

[Devpost](https://devpost.com/software/debttracker) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[web_dom]]

**stack** forge, github, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for debttracker

## Body

Technical debt is part of software development, but we should make it transparent and trackable. Debttracker helps developers to easily create Jira issues while reviewing code to track technical debt. Inspiration As a software developer I always struggle to find the balance between shipping working software and shipping working maintainable software. When I do code reviews via pull requests I often think "this should be done better, but if we do it like we should do it, we're going down a rabbit whole because this requires a lot of changes...". Keeping track of such things is hard, so why not make it a little bit easier. What it does The idea behind debttracker is to make it easier to track technical debt by combining the tools used by developers to identifier technical debt with the tools to track work. Debttracker allows developers to create JIRA issues from within GitHub. After connecting debttracker with a GitHub repository the developer can use a special PR review comment format to create JIRA issues from her comment. Just type: #debttracker: <title> <description> as a PR comment and debttracker will create a JIRA issue with the title, description and label "technicaldebt". This allows the team to keep track of technical debt and plan the work to get rid of it like normal work. It also makes it transparent to other stakeholders. How we built it My personal goal was to test if I could develop such a tool without any additional infrastructure, so I just used the Atlassian forge platform: custom UI, web trigger and an OAuth app in GitHub. Challenges we ran into Learning new technologies, I was not familiar with Atlassian stack at all. Also, on some edges the forge platform feels very beta, like error message which do not really help or missing capabilities (get the url of a project page). Accomplishments that we're proud of I'm proud of having a working MVP. It is also great to see that even more complex scenarios - like integrating other services with OAuth - are possible with the Forge Platform and I'm proud because I got it working even there are no example apps or guides for such a scenario. What we learned I've learned a lot. Last time I used JIRA as a developer is over 10 years ago. So, the Forge platform - even with it quirks it has in this early stage - seems like a great direction Atlassian is going for allowing extensibility of their products. I was not familiar with NodeJS and modern JS development - I also had to learn react. As someone who struggles with frontend development and is more a C# backend person this is quite a lot to learn. What's next for debttracker My plan is to create a Visual Studio Code extension, which shows the JIRA issues for the files the developer has open. Like "Oh hey, there 2 items in this file for technical debt, maybe I can improve something along the way". This would allow to not only track but also solve technical debt. <div