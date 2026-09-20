---
slug: "reflexx"
url: "https://devpost.com/software/reflexx"
title: "Reflexx"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 469
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

# Reflexx

> Reflexx lets your team respond to bugs in your code faster than ever before.

[Devpost](https://devpost.com/software/reflexx) · hackathon [[Codegeist 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** browserify, codex, github, javascript, openai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for reflexx

## Body

Inspiration One of the teams I am on have automated bug ticket creation from services like Sentry.io and Datadog. They are able to make these tickets with the stack trace of the raised error as a part of the description. The nature of these auto generated tickets is that no human is informing the rest of the team about them. This is even the case with bugs that are caught by teammates. As a developer I found it very frustrating that I learn about a bug related to code i was working on after I've already moved on to a different task. There are also some super small errors that can happen in a development environment such as checking for a null value. As an engineer I realized it would be great to do these from the Jira front end and not have to go through the formal process back on my code editor. What it does Reflexx analyzes stack traces and injects their Jira ticket into the relevant lines and functions in the codebase as a comment. It also provides a UI code editor on the Jira Issue with a Codex Powered Auto Bug Fixer. How we built it Reflexx was built using the Atlassian Forge Platform, Javascript, OpenAI Codex, and Github API. Challenges we ran into One of the biggest challenges with building Reflexx was Github api and using it for the specific purpose of automated code changes. A lot of research and testing was needed for this to work perfectly leading to digging up many years old articles which probably haven't been read or updated in over 5 years. Another huge challenge was analyzing stack traces and program function structure, this led to the use of libraries which I had to compile into pure JS using tools like Browserify. With this I able to bring in a lot of powerful functionality from existing libraries into Atlassian's forge. Accomplishments that we're proud of One of the trickiest features was the AI auto fix feature. Using just a stack trace and a function block to fix a bug is extremely challenging. However thanks to a high temperature on the Codex model users are able to achieve the desired result if they try the same input a couple of times. In addition to this we are feeding as much context as possible as input. What we learned What's next for Reflexx Reflexx is something I would love to use in my own workplace. With automated bug ticket creation integrations its really hard as a developer to know what code needs a quick fix. In addition I intend on improving the functionality of Reflexx and partnering with some of the up and coming AI code completion companies to someday approach a solution that responds automatically with minimal human intervention. <div