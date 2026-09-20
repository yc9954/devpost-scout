---
slug: "flowdingo-issue-workflow-visualisation-for-jira-cloud"
url: "https://devpost.com/software/flowdingo-issue-workflow-visualisation-for-jira-cloud"
title: "FlowDingo – Issue workflow visualisation for Jira Cloud"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 1110
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# FlowDingo – Issue workflow visualisation for Jira Cloud

> Rethink the Jira issue view by visualising your teams workflows. Forget about plain todo list items. FlowDingo comes with a workflow builder and is really fun to use!

[Devpost](https://devpost.com/software/flowdingo-issue-workflow-visualisation-for-jira-cloud) · hackathon [[Codegeist 2022]]

## Facets

**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** forge, node.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of & what we learned
- what's next for flowdingo

## Body

extends the Jira Issue view fully fledged workflow editor comes with a rich set of templates fullscreen mode for large workflows JQL support and available in Jira Automations Detailed view and worklog for every task Inspiration Hey there, I'm Julian 👋 – I'm a heavy Jira user since about 10 years. With this project I filled a gap in the platform that I've had in my head for a long time now. Like we all, I see the Jira issue view every day. What I've always felt was missing in Jira, is an overview of the actual status of an issue and its depending tasks. Of course there is the status selection. But the simple one-dimensional metric that's expressed with words like "in progress", "waiting" and "resolved" ignores the hard facts about our daily work: We are working in teams. Issues are getting resolved together. We aren't working following a strict waterfall model: People can work in parallel. Still sometimes there are bottlenecks (like mandatory approvals) or tasks that build on each other: Some tasks need to be resolved before others. There are groups und sub-groups of tasks that an issue is contained of Jira itself and vendors on the marketplace offer partial solutions for this: There are Jira subtasks, to-do list and checklist apps: Yup, and they are working quite well for certain scenarios. Regarding subtasks: in most cases you won't need the power of a full issue. Especially for small tasks. Another issue leads to another source of information that might get lost in transmission. But the main problem here is that also checklist apps suffer from: Tasks expressed in a list don't show how subtask correlate to each other: What has to be done first? Which tasks can get worked on in parallel? That's why I built FlowDingo. What it does FlowDingo is a workflow visualisation solution for Jira issues. It shows the actual work progress of an issue right within the issue view. You can see which of your team members are working on what and which tasks need to get resolved to move forward. When tasks aren't ready yet (because other tasks are placed before them in the flow) FlowDingo marks them accordingly with a lock item. 🔒 Each Jira project can have its own workflows. Those workflows are created with a workflow builder which allows you to build even complex structures. The editor uses well known AtlasKit components like the editor and the emoji picker. This makes it easy to recognise single tasks and integrates seamlessly into the Atlassian UI. This is the list of features that I've been able to implement during the hackathon: Workflow Editor in project settings ✅ Workflow Viewer in issue panel ✅ Workflow Connector that shows up when an issue has been assigned a workflow yet ✅ Progressbar that shows within the issue ✅ Confetti in that Progressbar ☄️ ✅ Option to reset the workflow ✅ Worklog for each task transition ✅ JQL integration that also enables FlowDingo for Jira Automations ✅ Mandatory assignee for tasks only specific users are allowed to resolve ✅ Fullscreen mode for large workflows ✅ Template gallery with some example workflows ✅ Get started page (that module luckily has been released during the hackathon 🤓) ✅ Don't miss the list with the things that I haven't been able to develop during the hackathon in the roadmap below 😅⬇️. How we built it Libraries and set-up FlowDingo is an app solely built on Forge. I was lucky to find a great template for new Forge Apps on CDAC . This set-up has been made public on Github and leverages Turborepo, vite, esbuild and other tools and really speeds up the development process compared to the default templates provided by the Forge CLI. Another important libraries that I've used: reactflow for the workflow visualisation and @atlaskit/emoji & @atlaskit/editor for the Atlassian-like editor experience. Forge modules jira:issuePanel This is where the magic happens. The issuePanel extends the issue view with the FlowDingo workflow viewer. jira:projectSettingsPage Workflows are configured per project. The workflow builder and the template gallery are located here. jira:entityProperty This was a tricky part. Information about the workflow are persisted per issue in an entityProperty. To make this data accessible in JQL and Jira Automations, an indexed entityProperty is used. jira:adminPage Due to a coincidence Atlassian released the "getStarted" flag for Forge during the hackathon. That's why I created an adminPage that is used as a starting point for the app. Challenges we ran into The code examples and project templates for Forge are very simple. They might be sufficient for small proof of concepts. But when it comes to medium-sized apps, the lack of a up-to-date build pipeline and the usage of the rather slow approach with react-scripts & webpack doesn't seem to be sufficient. The documentation of some atlaskit components like @atlaskit/emoji and @atlaskit/editor is bad. It took me some time to make that both libraries running within the Forge context Accomplishments that we're proud of & What we learned I found an approach where you don't have to bootstrap a whole new React sub-package for each view in the UI: the Forge context objects provides all information of what module and which modal is currently being loaded. This made it possible for us to route to different parts of the application from one single React app. This tremendously speeded up the build and development process. Some Atlassian libraries (like the editor) don't compile with vite & esbuild. That's why I have implemented a webpack-based precompile step for those libraries that can be cached via turborepo. This also helped a a lot when it was about decreasing build time. What's next for FlowDingo There are still a lot of things to do. At the beginning of the project I made a list of what features I want to have ready for Codegeist. To be honest I underestimated the work a little bit. 😅 That's why I definitely want to implement this features before FlowDingo will be available publicly: ROADMAP Things that haven't made it to the Codegeist release: Bugfixes 🐛 Zooming doesn't work well with Atlaskit tooltip components 🐛 The Builder sometimes crashes when complex root nodes are removed 🐛 Features ⭐️ Possibility to convert a FlowDingo task to an issue 🚀 Auto assign certain issue types with a pre-defined workflow 🚀 Build flow from issues: Skip the workflow builder by generating the workflow from existing issue links like "blocked by" and "has to be done before". 🚀 Skipping tasks as an alternative to resolving them when they're actually not needed 🚀 Thank you for reading this project story! 🦊 Cheers, Julian <div