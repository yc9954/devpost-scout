---
slug: "dependency-management-depman"
url: "https://devpost.com/software/dependency-management-depman"
title: "Developer Automation"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 298
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# Developer Automation

> Collection to automate developer's workflow and make their lives easier.

[Devpost](https://devpost.com/software/dependency-management-depman) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** apis, github, javascript, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for developer automation

## Body

Inspiration While working and collaborating on JavaScript projects, it could be difficult to keep track of various dependencies and their versions. Additionally, there wasn't an automated easy-to-use solution that could alert and automatically update all dependencies while also ensuring that the project doesn't break by updating these dependencies. Hence, we came up with a Developer Automation solution using Postman. What it does The "Auto Update Node module Bot" automatically manages all of the project dependencies by checking of each dependency updates, figuring out whether the update is a simple patch fix, a minor update, or a major update and if it's not a major update (that might break the existing code), it automatically makes updates and pushes it onto a branch. How we built it We built this project using javascript, NPMS API and GitHub APIs. Challenges we ran into Finding an optimal way to call API inside loop using collections. Testing it on numerous existing repositories and optimizing flow. Accomplishments that we're proud of Creating a tool that not only save's time but also is a super simple way for developers to keep their project's node modules up to date. We will certainly end up using it for our own projects. What we learned We learned a lot about the Postman platform. We started off with a limited understanding of different productivity tools and features available on Postman. Over time we understood the platform and its potential in building APIs while ensuring streamline collaboration. What's next for Developer Automation Next, we plan to increase the utility by adding new features such as Airtable to keep a log of scan history/updates, messaging or email services to keep developers posted about different changes etc. Add support for other languages. Auto merge pull request if all test cases pass. <div