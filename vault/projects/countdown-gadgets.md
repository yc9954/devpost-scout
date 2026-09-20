---
slug: "countdown-gadgets"
url: "https://devpost.com/software/countdown-gadgets"
title: "Countdown Gadgets"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 294
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Countdown Gadgets

> Track release and sprint date on your Jira dashboard with countdown gadgets

[Devpost](https://devpost.com/software/countdown-gadgets) · hackathon [[Codegeist 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** javascript, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for countdown gadgets
- special thanks for

## Body

Dashboard with Sprint Countdown and Gadget Countdown Release Countdown gadget configuration Sprint Countdown gadget configuration Inspiration In our team, we use Days Remaining in Sprint Gadget which is pretty simple and useful. Unfortunately, our release date doesn't match the end of sprint. We use Jira versions feature in our projects to track release date and deploy our apps in time. After some consideration, we decided to build a tiny gadget for tracking the release end date. Then we didn't stop and extend Atlassian's Days Remaining in Sprint Gadget with some new features. What it does Jira Cloud plugin contains 2 gadgets: Release Countdown Gadget and Sprint Countdown gadget. Release Countdown gadget configuration contains 3 fields: Project, Version(Release), and countdown format. Users can select the countdown format - the gadget can display remaining time in days, hours, minutes and seconds. Sprint Countdown gadget has a similar configuration. There's other field pair: Board and Sprint. If the user selects "Next Sprint Due" checkbox, the gadget starts a new countdown when the new sprint starts. How we built it We use a new forge module: dashboardGadget with Custom UI (for build interface we use React) Challenges we ran into After deploying our app from mac os, gadgets crashed with error: Uncaught ReferenceError: process is not defined at index.js:7:30 at index.js:13:27 at index.js:13:27 Unfortunately, this problem hasn't been resolved yet. We build and deploy an app on the PC. What we learned How to create gadgets for Jira with Forge. Creating gadgets for Jira Server/DC was a nightmare 🙃 and we're really excited about how powerful Forge is. What's next for Countdown Gadgets We'll publish it to the Atlassian marketplace and add a new features (custom countdown) Special thanks for Atlassian Forge Team and Atlassian Developers Community <div