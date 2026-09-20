---
slug: "release-kit"
url: "https://devpost.com/software/release-kit"
title: "Release Kit"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 787
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# Release Kit

> Bringing releases to service and business teams is only the start of our journey. By grouping releases, teams can ship together, no matter how they are organised.

[Devpost](https://devpost.com/software/release-kit) · hackathon [[Codegeist 2021]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[geospatial]]

**stack** atlaskit, forge, react, storybook, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for release kit

## Body

Bringing releases to every type of Jira project View and manage your releases from the same screen View progress in a blink See the progress and follow-up in detail When linking releases, see the overall progress in 1 view Create new releases immediately in multiple projects at the same time Inspiration As Atlassian coaches for all kinds of teams, we've encountered many cases where releases could be the answer to improve the collaboration. Classically, at the beginning of an implementation you'll need to decide on how to map projects onto an organisation: will you create a project per team? One per product? One per code repository? On top of that, people from different backgrounds work together. This might be a service team, creating small configuration changes that need to be checked in with an upcoming release over several engineering teams that work on different parts to a marketing team aligning efforts fo a new release event. What it does First and foremost, Release Kit brings an overview of all releases to teams that lost this functionality when the Jira product family emerged. With Release Kit, Jira Service Management and Jira Work Management teams have a project page where they can see all the releases for that project. When people have the correct permissions, they can manage the releases and create new ones in this view. In order to bring teams together, we've added the functionality of grouping multiple releases across projects. This way, you can easily get the complete picture and see what work needs to be done in order to ship. These releases can be linked upon creation. Alternatively you can link and unlink existing releases to and from releases in other projects. How we built it We've embraced the possibility of using Custom UI completely: this way we could build a React app, hosted on the Forge platform, brining the benefits of speed and security. The main component is a project page, containing all the logic for working with the releases. This page is making use of AtlasKit components, combined with own implementations of components that are not publicly available. The storage for linking releases is build on top of Forge storage, combined with project properties. The whole project is developed using TypeScript, drastically limiting the amount of walls we've ran into while coding. Challenges we ran into We wanted to start with a clear monorepo approach using yarn workspaces but unfortunately this broke forge tunnel. Since forge tunnel is such a great tool that improves our productivity, we used a different approach with nested projects and using npm so every part still has its own node_modules folder. When we started working on the storage part we were held back by the lack of tooling. With all the code and storage being handled remote, debugging what and how turned to be.. interesting. Therefore, we've implemented our own admin page to get a peek inside of the storage. After implementing the storage part, we ran regularly into random 402 errors that went away upon restarting forge tunnel. The performance of the storage module is something that should be improved, this is definitely lacking in comparison with the entity properties. And last but not least: time, or the lack thereof. We had a list of great ideas but ran out of time before we could implement them all! Accomplishments that we're proud of Building the React components and composing the views got a massive speed boost by making use of Storybook, so we could implement and test components in isolation. With the CustomUI path, it is possible to create great user interfaces with subtle animations (waiting! Adding! Removing!), delivering a shrink wrapped version of an idea. Even though it is a hackathon after all, we were able to build a product that is ready to be used and collect feedback from end users. What we learned The Forge framework is still progressing every day. This is a necessity, since it still doesn't have all the power that currently exists in the Connect framework. These changes might make it harder to build a stable product. Multiple times there where some changes that had an impact and needed code changes, but where not yet communicated. Following up the dev channel and CLI messages is more than just a recommendation. Although there are a bunch of restrictions, this product shows Forge is already a great platform that is getting ready to be used for the next generation of apps. What's next for Release Kit After the first round of feedback, we'd love to bring the possibility of release notes to the party as well. This might be a great foundation since Forge makes the integration of Jira/Confluence a breeze. <div