---
slug: "one-to-one-analytics"
url: "https://devpost.com/software/one-to-one-analytics"
title: "One-to-One Analytics"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 924
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
---

# One-to-One Analytics

> One-to-One Analytics provides metrics for continuous improvement to be used in software engineer One-to-One meetings. It brings your One-to-One meetings to a new level with data-driven insights.

[Devpost](https://devpost.com/software/one-to-one-analytics) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[sensor_telemetry]]

**stack** atlaskit, atlassian, bitbucket, confluence, forge-custom-ui, github, recharts, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for one-to-one analytics

## Body

Add metrics to your One-to-One meeting pages Choose the time window, KPIs to review and repositories Spot the details by using the interactive charts Inspiration Our inspiration came from our observations during One-to-One software engineer meetings and realizing that we lack statistics and data to make these meetings effective for both sides. We wanted to make use of data driven insights to help develop individual engineers and ultimately continually improve the team as a whole. What it does One-to-One Analytics provides metrics for continuous improvement to be used in software engineer One-to-One meetings. It is a Confluence integrated macro that a user can configure during a One-to-One using GitHub or Bitbucket DC repository data for a single user. It provides metrics and helps to visualize key performance indicators by using interactive charts. Why we believe these KPIs matter and level up your One-to-One meetings? As an Author of a Pull Request Time to Open (TTO) - Time from first commit to pull request creation. Working too long in isolation hinders you to get early feedback from your peers. Lead Time (LT) - Time from opening to merging a pull request. As a pull request author, you are responsible for reaching out for feedback and incorporate suggested improvements. Minimizing the time for this process reduces the risk of merge conflicts, and also allows you to get feedback from your customers earlier. Pull Request Size - is the sum of added and deleted lines of code (LOC) from a pull request. Small pull requests are more motivating to review, and can have a positive impact on the quality of the feedback. This KPI ties into the Agile/DevOps tenet of working in small batches . Merges without Reviewers - Includes those pull requests not reviewed before merging. Reviewing as a team provides knowledge- and skill-sharing opportunities, collective code ownership, and more eyes on the code to spot bugs and specification errors. As a Reviewer of a Pull Request Comments per Review: includes the total number of pull request comments made during a pull request review. The team benefits from quality feedback so staying involved as a PR reviewer is important for the development of team members. Time until Review: is the time from when the pull request is open until the pull request review is submitted. Slow response times as a PR reviewer can slow the team down so keeping an eye on review times is important to avoid bottlenecks. The data can be used to support the One-to-One meeting discussions and then documented in Confluence so that goals and feedback can be added and used as a point of reference in future meetings. How we built it We started by experimenting with the Forge CLI to narrow down the best Forge module to use for our purposes. We chose the Macro module as it provided the MacroConfig component that we needed in order to insert dynamic content based on the user's configuration. Then we explored using the UI Kit and quickly determined that we needed to use the Custom UI template as well in order to build out the features that we had in mind. We also made use of the Forge APIs, hooks and functions to be able to fetch and handle that data in our app. And, we used an external charting library to help visualize that data. Given we are familiar with React, it was great to be able to dive in and start developing using the languages and libraries that we are already familiar with. Forge makes it very easy to get started and develop a prototype so it was fun to see the progress in a short period of time. Challenges we ran into We encountered UX issues based on Forge Custom UI limitations like not being able to interact with the page during the editing of a Confluence macro. However, we were able to introduce some workarounds to improve the user experience despite these limitations. We are confident that Atlassian will continue to improve the Forge UX. We also noticed debugging limitations with Forge so it was hard to debug at times and logs seem to be very limited or not appear at times. Accomplishments that we're proud of We are pleased that we could create a new app in a short amount of time using Forge. We are also happy that we could experiment with Forge during the development of this app by trying out different UI templates and modules which helped us understand the platform much better. What we learned We learned more about charting libraries and options to use with Forge in order to visualize data. We also got well acquainted with using Forge and discovering its limitations. We gained experience and knowledge in order to build future products using the platform when it makes sense. At this stage, we intend to consider "Forge first" for our future apps but we are well aware of the limitations that Forge still has to overcome so we will consider all options including Connect where appropriate. Time will tell how Atlassian Forge evolves over time and more importantly how it improves and overcomes its limitations. What's next for One-to-One Analytics We have made the app available on the Atlassian Marketplace so we can start gathering interest and feedback which will determine how we continue to evolve the app and its features. We are contemplating adding more key performance indicators, including other data sources and we are considering adding more features like the ability to add and configure individual goals. <div