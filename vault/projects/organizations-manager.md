---
slug: "organizations-manager"
url: "https://devpost.com/software/organizations-manager"
title: "Organizations Manager"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 523
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
---

# Organizations Manager

> Enhance Jira Service Management by adding additional information to organizations. Use the app to create fields, control permissions and edit organizations straight from the Jira issue view.

[Devpost](https://devpost.com/software/organizations-manager) · hackathon [[Codegeist 2021]]

## Facets


**stack** amazon-web-services, dynamodb, forge, lambda, s3, trello

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for organizations manager

## Body

Organizations Manager View organizations Edit organization details Manage fields Field types Edit fields Manage permissions Edit organization fields from the issue Inspiration The team at New Verve Consulting uses Jira Service Management (JSM) on a daily basis to manage external and internal requests, and JSM organizations are heavily utilised. We realised that we needed to capture some metadata for each of our customers such as the main contact, their address, or the type of agreement and share the information with our agents. This led to the development of Organizations Manager which would provide a central location for all our organization needs. What it does Organizations Manager , extends the native JSM organizations, provides a central place to manage, edit, and administer JSM organizations, and enables agents to quickly address service requests. It provides a high level view of the organizations and the current level of engagement in the landing page, while in the organization view, new custom fields are added to capture client specific data. In addition, an issue panel is available on the requests, where the agent can quickly view and edit the organization's details. Project permissions allow admins to control who has access to the app. How we built it The design process started with defining the app requirements and the use cases. While we are heavily motivated to solve our specific use case, the market was analysed to provide a well rounded application that would add value to IT teams using Atlassian Cloud. The app itself was developed using the Forge framework, Atlassian Connect, in conjunction with AWS. The development process involved a solution prototype where the challenges were identified and the final features were agreed upon. Challenges we ran into The main challenge was the synchronization with JSM, as during implementation there wasn't direct support for JSM APIs. We attempted to solve this in UI kit and custom UI, but eventually settled on using 'Forge on Connect' to implement a synchronization logic. We wanted to use Project roles in our permissions configuration. Due to the high complexity and potentially high execution time, we used the Project Permissions scheme to enable Project role access to the application, by building the permission on top of Jira's permissions. Accomplishments that we're proud of Most of the technology was built with Forge, including the use of UI kit and also APIs like storage and authorization provided by Forge out of the box. This was our first time using 'Forge on Connect' and we proud to produce a solution that is compact and secure. What we learned As Forge takes care of security, compute, and storage, it was interesting to learn about this new architecture or new way of working, and about the difference between server side rendering versus our previous experience with client side rendering. What's next for Organizations Manager We have a backlog of features we would like to implement in the future which would enhance the user experience and provide additional functionality for project administrators including: improved management of fields; management of customers/people and asset management. If you liked Organizations Manager, why not check out Crumbs on the marketplace ! <div