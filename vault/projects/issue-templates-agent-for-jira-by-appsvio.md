---
slug: "issue-templates-agent-for-jira-by-appsvio"
url: "https://devpost.com/software/issue-templates-agent-for-jira-by-appsvio"
title: "Issue Templates Agent for Jira"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 802
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
---

# Issue Templates Agent for Jira

> Get the most out of issue templates and save your time. Create once, use whenever needed, and enjoy immediate field fulfillment on the issue screen.

[Devpost](https://devpost.com/software/issue-templates-agent-for-jira-by-appsvio) · hackathon [[Codegeist 2022]]

## Facets

**mechanism** [[cross_origin_web]]

**stack** atlaskit, figma, react, react-hook-form, storybook, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for issue templates agent for jira by appsvio

## Body

All templates stored in one handy place Template configuration easy as pie Apply template immediately on the Create issue screen Inspiration The biggest dose of inspiration is the people around us. So many times, we’ve heard that creating the same issues all over again is too time-consuming. You can’t buy time, so we decided to try to save it for others. How? By solution that allows you to make coherent issues with automated field fulfillment. Keep your backlog neat and tidy and give the needed information for creating issues immediately. Looking closely at our daily work and listening to our clients and the Atlassian community, we noticed that there is a lack of a solution that allows you to create a template right on the native issue screen. Without extra buttons, no new views and what comes next, without users’ confusion and wasting time. We wanted to create an app where the path of creating issue templates is simple, quick, and, what’s more, already familiar to users. What it does Issue Templates Agent for Jira allows users to apply templates on the native create issue screen immediately. It means you don’t have to start from scratch every single time. With our app, it’s possible to speed up creating issues with ready-to-use templates. What’s more, once created templates can be used many times. It is possible to save them in the template library – one storage place, thanks to which the admin has an easy global configuration. Standardized tickets are a key to skyrocketing Jira management. One template can be matched with many pairs: project and issue type. Admin specifies in which projects it can be available. Templates setup is hassle-free, no matter how many templates an admin needs to prepare. In practice: For example, whenever you are a UX designer and need a "hypothesis testing" task for every project, or when you report a bug as a tester, templates are to the rescue! 🚨 In a nutshell: Customize issue templates and manage the library Specify summary, description, priority, labels, and assignee Assign issue templates to different projects and different groups – create once, use them whenever you need How we built it 🛠 This app is built with Forge. The starting point was the UI modifications (UIM). We used Forge Custom UI, Forge Storage, and Admin page. The frontend is built with AtlasKit's components. We managed the entire project using Jira Cloud and Confluence. The Interface graphic designs are prepared in Figma. Fun fact: This app is our hackathon's baby! We created it during our Team integration near our beloved Baltic Sea and between running training sessions. Thanks to Forge, that was a quick but effective one. Challenges we ran into What would a new app be without a few hassles and new challenges 😎 We find opening a modal on the open Create issue screen when using UI modifications challenging. There was also an issue with the lack of possibility to display custom icons for f.e. priority or project. We’re still missing the onClose callback to create structures’ template, and currently, the app supports five fields (soon, there will be more). Forge doesn’t support service projects which also can generate limitations for JSM enthusiasts. UIM allows uploading a limited number of contexts (1,000), and a specific issue type and project pair must always be specified when doing so - it is impossible to make more generic contexts, as is the case with other types of schemas in Jira - so we had to take this into account in the template configuration. Accomplishments that we're proud of We managed to use UI modification slightly differently, as it’s said. Its creators didn’t foresee using it to open modals that allow you to perform some action. We were able to make it work during the four days hackathon. Forge allows a fast development process, and it’s a friendly environment for shaping new ideas and experimenting with them. What we learned Developing Issue Templates Agent taught us how to use UI modification differently. We also learned new Forge modules and how to use our prebuilt and reusable components (based on other AtlasKit components). Creating configuration screens has never gone so smoothly. What's next for Issue Templates Agent for Jira by Appsvio Hey Forge, we're waiting for service project support! 😂 And to be serious, when Forge will support a service project, we’ll make templates available on the portal for customers. We also look forward to API extension to support more fields: those systems ones and custom fields too. We are considering improving UX and changing the template choosing bar, but we also need an API extension here. We're going to expand the app. The new features will appear, you can be sure 😊 It depends on our users' needs because they're our ultimate inspiration. <div