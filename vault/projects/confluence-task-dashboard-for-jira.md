---
slug: "confluence-task-dashboard-for-jira"
url: "https://devpost.com/software/confluence-task-dashboard-for-jira"
title: "Confluence Task Dashboard for Jira"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 1292
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Confluence Task Dashboard for Jira

> Create consolidated Confluence Task Reports on Jira Dashboards to keep your team accountable, improve communication, and analyze data faster! New Dashboard Gadgets to integrate Confluence with Jira.

[Devpost](https://devpost.com/software/confluence-task-dashboard-for-jira) · hackathon [[Codegeist 2022]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[web_dom]]

**stack** atlassian, forge, react, rest, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for confluence task dashboard for jira

## Body

Inspiration Confluence Tasks and Action items are very powerful features. They fill in the gaps between personal to-do lists, and all tasks which profit from a more complex workflow and usually end up in tools like Jira. No other project management solution offers this genius combination of simple tasks (Confluence) and more complex work items (Jira). Since Meetical is all about Meetings, Confluence Meeting Notes , and Action Items, we’ve been thinking for quite some time about how to improve certain things around Confluence Tasks. When the Hackathon started, we implemented our Beta Version of a new Task Management Feature for the Confluence Chrome Extension first. We then wanted to implement a next-gen Confluence Tasks Manager but realized that actually there is no Dashboard Gadget for Confluence at all which brings in together Data from Tasks with Jira issues. What an opportunity! So we got started with crafting a concept and implementing an App. Our vision is to create a seamless experience for Task Reports, a simple solution to quickly document task outcomes, and enable users to use Confluence tasks also as a personal to-do app. We want furthermore to introduce Analytics around tasks that help Project Teams to have a sense of progress and motivate them to keep things up-to-date while moving fast. In 2020 we focused on a Confluence App to automate Meeting Notes . For this year's Hackathon, we focused on Dashboards, to help teams using both Confluence, Jira Work Management, and Jira Software Teams manage tasks effectively and succeed through better insights and analytics. What it does Confluence Task Reports for Jira come with an impressive feature set, which is a tribute to Confuence as first class citizien in the Atlassian world. The native task reports might become jealous but more on that in ‘What’s next' section: The Task Report Gadget shows a Task Report from Confluence for your team on your Jira Dashboard. Tag the @mentioned users accordingly, and show a due date including the Day of the Week for easy orientation. The task report can show complete/incomplete or all tasks. Which tasks shown can be filtered by Space or for more complex scenarios with a CQL query. Jira tickets mentioned in the task are also shown and linked for easy access, including the issue summary Users can check/uncheck tasks directly from the Dashboard. Additionally they can complete a task with an “outcome”. This outcome is added to the task, allowing users to document the result in an easy way, without having to edit the page. (Note that this is not a comment, but the outcome is added as blue text next to the item itself!) Users can order the Tasks by due date and also show tasks without due date. Tasks have a Simple List view and a Calendar view! The Calendar view can also be set in the config of the Gadget as default. This allows to have both views: list and calendar side by side on the same dashboard. The Calendar view allows to the creation of Calendar Subscriptions, compatible with ics/ical, which means almost every calendar can sync them. Tasks show up on people's calendars and are updated if anything changes. They also have a nice emoji status to show overdue tasks immediately. The second Gadget is an Activity Stream! Really helpful to show the latest created and completed tasks by all people on your team. Tasks created and tasks completed are helpful to get a sense of progress related to the Confluence Tasks. Avatars of users are shown to reward them for their actions taken. The third Gadget is a cool Analytics Dashboard. It shows a statistic of all created, completed, and total tasks in a time frame. It also shows the workload for each person on the team. It also shows the cycle time/lead time, so teams get a sense of how fast they are in completing their tasks. Additionally, a leaderboard brings in gamification features, so people are rewarded to create tasks and more importantly complete their tasks on time. Finally, the resolution rate is calculated and shown as an indicator to teams of how much work is left for their Tasks. To keep things fast, Analytics are cached and recalculated every hour or can be refreshed on demand These three gadgets, the Tasks Report, Tasks Activity Stream, and the Tasks Analytics can be combined in endless ways with any other Gadgets and in whatever layout the user wants them to display! How we built it The solid foundation of our app is Atlassian Forge and Atlaskit, but we also have a lot of custom code, for both visual components and server parts. We use TypeScript for both server part and front-end and custom Vite configuration to build multiple front-ends from the same codebase, enabling us to share a lot of code between our gadgets. But it doesn’t stop there, since Vite is configured in a way, which allows us to easily import code from the server-side part of the application into our front-end code. We actively use this feature in our custom wrapper for @forge/bridge and @forge/resolver, which ensures type safety on both sides of front-end—server communication (and provides great autocomplete too :slight_smile:). On the front end, we use React for building reusable components and Sass for styling. We extensively use Atlaskit components and also have components tailor-made for this project. For example, we had to write our custom parser which will transform the task’s HTML we get from Confluence into a list of tokens, which later can be easily analyzed in code to extract a list of assignees or other data and can be rendered by our component across our gadgets. Challenges we ran into From a technical standpoint, one of a challenges we faced was: how do we render tasks from Confluence (which are in XHTML storage format) on our front-end. We wanted to provide rich experience to our users, like preloading of mentioned Jira issues, other users, dates, etc. So just rendering tasks as plaintext wasn’t an option at all! What we end up with is a custom parser that converts storage format into a list of tokens, which can be later processed to extract all mentioned users or Jira issues, which should be preloaded and the same tokens used by our front-end to render interactive tasks components. Another challenge is that our App is cross-platform and so we need to install it on both Confluence in Jira. Especially for the Marketplace, this will be quite a hassle. Hopefully, cross-platform Apps are soon supported by the Marketplace. Also when working as a team with multiple developers, not being able to associate an App ID with a team is very cumbersome. We wanted to use embedded Confluence (a new API feature from Atlassian!) to show and preview pages. However, we run into issues and the Forge/Ecosystem team could help us identify the issue but not solve it on time for the hackathon. Accomplishments that we're proud of Unbelievable that we now are handing in 3 awesome gadgets. We’re really proud of this. And we feel that every feature fulfills a specific goal and demand. We are very curious to get real user feedback and publish the App right away to the Atlassian Marketplace! What we learned A lot of Forge! And a lot about the awesome possibilities of the Jira and Confluence REST Apis. What's next for Confluence Task Dashboard for Jira Next up, we want to re-shift our focus to the Chrome extension to provide a personal Task manager for users. And also implement the “complete with outcome” feature there. We have a great list of features coming up, and we want to make everything available also for Confluence as Macros and New Menu Items! <div