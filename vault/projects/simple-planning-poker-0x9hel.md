---
slug: "simple-planning-poker-0x9hel"
url: "https://devpost.com/software/simple-planning-poker-0x9hel"
title: "Easy Planning Poker"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 988
team_size: 14
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
---

# Easy Planning Poker

> Easy Planning Poker provides a new interface for the Jira Issues on the backlog view where users can initialize a voting session in an Issue glance and vote and accept the final estimation.

[Devpost](https://devpost.com/software/simple-planning-poker-0x9hel) · hackathon [[Codegeist 2021]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]]

**stack** atlassian, cloud, forge, javascript, jira, mobx, node.js, npm, python, react, typescript, uikit, yarn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for easy planning poker

## Body

Inspiration Our DEV team lives in the Jira scrum board and in its backlog. On the Jira server we were able to create our custom solution for planning poker with automations, without the need of third party app or solution. After our company migrated to Jira cloud, we faced a problem to recreate this solution due to lack of tools. We wanted a planning poker app that integrates with and lives in the Jira backlog, so the team can stay there without the need to open or navigate to another page. The codegeist was a perfect opportunity to implement our solution for the planning poker with Forge. We organized an internal 6 day hackathon to develop an app for our needs, and to learn about the properties, boundaries of the forge and learn to use it. What it does Easy Planning Poker provides a new interface for estimating Jira Issues without leaving the backlog view. This solution saves time for the users, they do not need to open a third party app or navigate to another app's page and configure the scope of the issues again. Also, all the options that the backlog provides are retained, such as all the information about the User Story is available instantly, the team can re-prioritize the issues any time, modify them, etc. With the app the users can: initialize a voting session for the issue estimation in an Issue glance while staying in the backlog vote for the estimation discuss and accept the final estimation copy it to the selected Issue estimation field How we built it We organized an internal 6 day hackathon to develop this app and to learn about the properties, boundaries of the Forge and learn to use it. We created the specification and user stories one week before our internal hackathon event. On the first day we did a backlog grooming, went through the user stories and created the necessary technical tickets for them. We managed the stories and tasks on a kanban board and worked with Extreme programming methodology: programming in pairs and doing extensive code review. We decided to place the app interface in an Issue Glance to make it available to users whenever they need it. The new Jira interface provides an opportunity to see the app interface with the Issue data as well. We wanted the app not to be distracting to users with its constant presence, but to be available at any time if needed, and the Issue glance was a perfect option to do this. We also started with custom UI, however, due to some limitations, we changed back to Forge UI kit for the prototype. Challenges we ran into One of the most UX breaking problem is that due to the call limitations when we use the custom UI we cannot refresh the pages frequently for the users (polling). We also did not find any information about how we can connect to external servers with Forge. Due to this, we were not able to provide real-time informations and interaction for the app users that we planned to do, and how we imagined the app. As a workaround, we changed it to Forge UI kit and stored the data in the issue property. Our plan was that we will listen to the set_issue_property event and change the UI based on it as we did it once with the connect, however, this does not worked as well, since this event is not available for Forge yet. Due to these issues, in addition to updating the interface for all user interactions, we had to place a “Refresh” button on each screen for the users, which is far from the user experience we imagined and wanted to achieve. Accomplishments that we're proud of We were able to create a prototype after multiple challenges we faced due to the limitations of the forge in only 6 days. After multiple iteration between the Forge UI and Custom UI we were able to find a way to almost reach the desired behaviour using Issue properties and other smart solutions. Great atmosphere and working together onsite after a long year of remote work. We were able to figure out a desirable way of handling the UI components' states without using React context hooks or observables. The end product is a maintainable code base even though we had a relatively short period of time to achieve it. We were able to regroup and re-plan every time we faced a major issue. What we learned Forge and its limitations. What it can, and can't do, and in what case we can use it to implement an app. While developing the app, we were forced to make up different (low-level) solutions for state management problems due to Forge related limitations. We think that Forge needs some polling mechanism enabled or more Jira events to handle, so we can develop real-time applications. We learned that we are more than able to overcome bigger issues and solve them quickly as a team. The team is able to adapt to many different solutions and styles, we are versatile. We learned to use completely new technologies like Forge (UI, Custom UI, Storage etc.). We tried out extreme programming while developing the app and it actually worked great, we were able to share a lot of knowledge between each other. What's next for Easy Planning Poker We will use it internally for some time to evaluate and further refine based on our experience. It’s possible that we will publish it on the Marketplace as a free app for some time. Based on the interest, we will improve it further in Forge or migrate it to Connect. In the future, we want to extend it with configuration options to: define the scope where the app will be present define roles for the app configure custom deck types and cards configure timer values improve the UI/UX <div