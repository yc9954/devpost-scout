---
slug: "xyz-m0g1pw"
url: "https://devpost.com/software/xyz-m0g1pw"
title: "Deep Linked Issues for Jira"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 711
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/web_dom"
---

# Deep Linked Issues for Jira

> Browse not only directly related issues with the current issue. Reach the links out of sight. Let the user delve into the connections and better understand the context of the issue.

[Devpost](https://devpost.com/software/xyz-m0g1pw) · hackathon [[Codegeist 2020]]

## Facets

**substrate** [[web_dom]]

**stack** forge

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for deep linked issues for jira

## Body

Reach the links out of sight Inspiration We wanted to show on an Epic all issues that are related to the particular issue in any way (support requests, releases, development tasks). Many of them do not have a direct relation to Epic. Unfortunately, there is no view available in Jira that would gather all related issues, not just the direct ones. Of course, the solution is available not only for Epic but for all issue types. For example, being on the feature request in the service desk project I can see not only the linked requirement which fulfills this issue but also the release issue in which this feature was released. What it does This app shows all linked issues to the third depth which appears in the Issue Glance . It provides a quick way for a user to get an overview of information about these issues. They are three available criteria: Project Issue Type Status Thanks to presenting this data under a particular issue, a user can understand better the context and estimate the impact of related tasks on the current issue. This app works also in Next-Gen Jira projects. How we built it We used Forge UI components which helped us create the front end of our app: IssueGlance Table Text Link We also used Forge Fetch API which is a partial implementation of node-fetch. We manage the entire project using Jira Cloud and Confluence. We have prepared the interface graphic designs in Figma. Challenges we ran into To enjoy our full success, we lacked a few elements that are currently not supported in Forge: the ability to define the icon size in the component, such as Issue Type or Priority (now they are really huge, what looks weird) option to format the location of components on the form (cannot be justified, right / left aligned) Limitations on interface styling can negatively impact user experience, especially if we add new elements in the glance. All suggestions we reported to the Atlassian team. Accomplishments that we're proud of Our beginnings with Forge were very difficult. That is why we consider it successful that the application works. What's more: it works correctly. The strength of our solution is the lack of configuration. The application is installed and is immediately ready for use. On the other hand, we are aware that this can be a problem for large instances. Therefore, in the future, we would like to add a module with a configuration for the administrator. We think that the design of the panel (glance) and the mechanics of the application's operation do not differ from the Jira standards. We believe that it is important that the end-user does not feel that he is using an external application. Our application fits perfectly into the product offered by Atlassian. What we learned This was our first contact with forge, so everything was new to us. We learned how Forge works, what is currently possible to achieve, what not yet. In case of this app, the biggest limitation was using only their components to build the interface. We cannot use HTML tags and design UI with CSS. Worth noticing that having React background was really helpful to create the app quickly. None of us has ever participated in any hackathon! We work with each other every day, but it is a completely different style of work than during such a competition. We were still thinking about how little time we have left, and how much is still to be done. But we can say it was worth it and it certainly is not our last time. We still want to work together :) What's next for Deep Linked Issues for Jira The most important functionalities we would like to add to the application are: New criteria, such as Priority or Link Type Possibility to filter linked issues Graph view A lot depends on how much Forge will offer us and in what direction its possibilities will develop. Currently, Forge is not supported on the Atlassian Marketplace. (We are looking forward to adding such support!) For this reason, we decided to convert the application into a Connect app to be able to share it with other users and publish it on the Marketplace. <div