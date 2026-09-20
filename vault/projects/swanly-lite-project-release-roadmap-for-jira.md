---
slug: "swanly-lite-project-release-roadmap-for-jira"
url: "https://devpost.com/software/swanly-lite-project-release-roadmap-for-jira"
title: "Swanly Lite - Project Release Roadmap for Jira"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 1027
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Swanly Lite - Project Release Roadmap for Jira

> Get visibility over your project releases; track release progress and plan releases in a simple Jira roadmap every stakeholder understands!

[Devpost](https://devpost.com/software/swanly-lite-project-release-roadmap-for-jira) · hackathon [[Codegeist 2021]]

## Facets

**mechanism** [[realtime_stream]]

**stack** atlaskit, atlassian-api, forge, konvajs, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for swanly lite - project release roadmap for jira

## Body

Swanly Lite - Simple Project Release Management Roadmap for Jira Cloud Open release detail by clicking on the release on the roadmap to see it's scope and key information like name, description, and so on. Roadmap offers daily view with highlighted weekends. Weekly view with up to 6 weeks in the view. Monthly view with up to 6 months in the view. Quarterly view on the roadmap. And Yearly view where you can plan long running releases. Inspiration Many teams out there use Jira releases to plan and track their work. By default, Jira allows you to create fix versions (releases) in your project, with links to issues; this is great for tracking but it doesn't give you a full story of your release progress. It’s hard to visualize progress over time with just a list or table of releases, as it is currently in Jira. The Swanly Lite app solves this problem by showcasing releases on a timeline that release managers and teams can quickly access to view release progress and scope, as well as overlapping schedules! Swanly Lite is a lighter version of Jexo’s flagship product Swanly , which is built with the Atlassian Connect framework. We wanted to test how hard it would be to transition Swanly, a fairly complex Jira app, to Forge. If you want to know how it went and what we learned along the way, continue reading! :) What it does Swanly Lite is a simple release roadmap you can find in your project menu. It offers clear visibility with respect to overlaps between releases and helps you understand the distribution of your planned deliveries. Timeline features Clear roadmap based on information from Jira fix versions, and with releases drawn on the timeline Zoom levels (daily, weekly, monthly, quarterly and yearly) ‘Back to today’ button Simply click on the release name in the timeline to access the release report, which is where you’ll find all the key information about your release, what was planned, issue progress and so on. Release report features Key release information such as release name, description, start and release date Release scope shows issues linked via the Fix version field in Jira Affects version tab showcases issues linked via the Affected version field in Jira All issues show details like issue key, summary, priority, assignee, status Quick access to issue details by simply clicking on the issue How we built it To build Swanly Lite, we used the latest Atlassian framework Forge, KonvaJS and React. Swanly Lite uses data that is already available in Jira, like Fix version name, description, start and end dates and so on, and visualizes releases in a roadmap timeline. To generate release reports, we use JQL by Fix version and Affected version. We used the following frameworks: Forge by Atlassian React KonvaJS Atlaskit From the Atlassian APIs we used: Project (/rest/api/3/project/{key}) Issue (/rest/api/3/search) Versions (/rest/api/3/project/{key}/versions) Version (/rest/api/3/version/{version_id}) Challenges we ran into Here are the top 3 challenges we had while working on the Swanly Lite project. 1# Can’t add the app on the global level navigation Initially, we wanted to build Swanly Lite as a cross-project release timeline where you’d be able to see releases from across different projects in a single view. The perfect place to put such an app is the global Jira navigation, to show that the app pulls data from across projects. Given we couldn’t place the app there, we decided to limit its scope to one project at a time only, and we added it to the project menu. 2# Paginated API for Jira releases isn’t available There is no paginated API for Jira releases, so we needed to pull all releases from the project. Because releases have a start and end date, and they’re continuously being scheduled in the bigger projects, their numbers can go to thousands. This may bring about performance problems over time. 3# No real-time updates We wanted to make sure that when the user updates release information in Jira, they’re able to see it in Swanly, in real-time. But because there are no webhooks or GraphQL yet available on Forge, we weren’t able to achieve this part. What we learned #1 You can literally build anything on the frontend using Custom UI Swanly Lite is a great example of that because the app UI is complex. The timeline itself is built with KonvaJS and there is a lot of styling and customization involved. The good news is that there are no limits to how your app can look like in Forge. #2 More time for fun while Forge handles deployments and infrastructure Having deployments and infrastructure covered by Forge is a great win. We don’t need to spend time and resources looking into this side of things and we can spend more time delivering value to our customers. 3# Think twice when porting complex apps from Atlassian Connect to Forge There were a few challenges we ran into that would make moving Swanly to Forge harder. For example, we have questions regarding the performance of the app for customers with many releases in their Jira projects, not to mention losing real-time updates in the app. So we’re in no rush to port our flagship Swanly app to Forge completely. We’ll keep an eye on progress with the Forge framework and evaluate again in a few months. What's next for Swanly Lite - Project Release Roadmap for Jira Swanly Lite proved to be a successful experiment for us; as I mentioned earlier, we wanted to know if we’d be able to transition our existing Connect apps to Forge. There are a few limitations we bumped into; some we were able to fix with a workaround, others await improvements in Forge itself, and so we were able to start thinking of moving our Connect apps to Forge without losing any current functionality (for more on that, check out the challenges section below). In terms of the app itself, we’re evaluating whether it would be useful to publish it as a free app on Jexo's Atlassian Marketplace apps listing. Let us know if you’d like to use Swanly Lite in the comments section! <div