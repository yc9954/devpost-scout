---
slug: "easytime-cnzqu2"
url: "https://devpost.com/software/easytime-cnzqu2"
title: "EasyTime"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 487
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/general_public"
  - "substrate/code_repository"
---

# EasyTime

> Start tracking instantly, recording time automatically and review timesheets visually. For Relaxing Times – Make it EasyTime

[Devpost](https://devpost.com/software/easytime-cnzqu2) · hackathon [[Codegeist 2020]]

## Facets

**domain** [[developer_tools]] [[labor_employment]]
**user** [[general_public]]
**substrate** [[code_repository]]

**stack** atlaskit, atlassian, connect, java, jira

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of:
- what we learned
- what's next for easytime

## Body

Worklog created just by viewing the issue Asking for user input on an extended worklog EasyTime glance after creating a worklog Part of the Configuration Screen Be Lazy, The Machine Does It Better Instant, Automatic, Visual Inspiration EasyTime is all about taking a painful, manual process and letting the machine do the hard work. Our team had been struggling, manually inputting time data so that we could accurately bill our customers, when we finally got fed up and decided to let the machine handle it. We have been using EasyTime internally at TechTime and have seen accurate completion of timesheets skyrocket, while even less time is spent by team members worrying about it. What it does automatically records time based on viewing an issue, commenting on an issue or resolving an issue records time in predefined chunks aligns worklogs to a time grid produces distinct messages configurable for different events optionally limit tracking to select projects only track time for select user groups only automatically suspends tracking when browser window is not active, resumes when activated records in Jira Issue View, Jira Software Boards and Jira Service Desk Queues recognises priority of events identifies clashes, shrinks or replaces low priority events merges sequential worklogs silently prompts to merge worklogs that are too far apart How we built it We already had a Server / DC version of the app, but had little experience writing apps with Connect for Jira Cloud, so we decided to use the same codebase for the business logic behind the decisions EasyTime makes like when to merge, when to overwrite and when it's best to not do anything. We literally use the same business logic in the server and cloud versions of our app, so a lot of the work went into the translation between the data that Jira Cloud provides and the data our business logic was built to work with. Challenges we ran into async and lossy nature of Jira Cloud webhooks mean EasyTime needs to be more forgiving of the raw data provided by Jira. limited nature of some Jira Cloud API's and extension points mean we needed to squeeze EasyTime into the UI in slightly unnatural way, particularly the "flags" UI which we use extensively in the server version of our app, works in a completely different way for cloud. Accomplishments that we're proud of: Accepted to the Atlassian Marketplace and live today in production :) The first working automated worklog on Jira Cloud was a magical little moment. What we learned Sometimes adapting your solution to the platform is the hardest part of the problem Leaned a huge amount about the Connect platform and Jira Cloud in general What's next for EasyTime Integrating with other tools you use every day, to log time in Jira, like Bitbucket, Confluence, Slack, IDE's etc. etc. Polishing of the interface, to reach the standards expected of a high quality, consumer-facing application <div