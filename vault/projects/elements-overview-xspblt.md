---
slug: "elements-overview-xspblt"
url: "https://devpost.com/software/elements-overview-xspblt"
title: "Elements Overview"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 358
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
---

# Elements Overview

> Display snippets of related issues exactly where you need them

[Devpost](https://devpost.com/software/elements-overview-xspblt) · hackathon [[Codegeist 2022]]

## Facets

**mechanism** [[cross_origin_web]]

**stack** atlaskit, forge, love, react, styled-component, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for elements overview

## Body

Elements Overview Overview - Table view Overview - Glance view Overview - Portal view Inspiration Wasting time between the constant back and forth when working with linked issues is frustrating. What it does Elements Overview is an issue visualization app for Jira that allows to organize how, where and when information about related issues is displayed on the issue view to provide actionable context to Jira users. The app is for ITSM professionals, software project managers or business project managers who are looking to provide detailed status information to JSM customers about the work that’s carried behind the curtain to resolve their request give a customized overview of related work to Jira users - agents, software and business teams alike - right inside the issue spare Jira users the need to navigate from tickets to tickets to get relevant information, or update linked issues details How we built it Elements Overview uses: Forge modules Custom UI Jira REST API Challenges we ran into One of our biggest challenge was to make an application that looked like a native feature of Jira itself, in a month. On the technical aspect, we faced some issues around the iframe size limitation and how to handle transitions with screens of displayed issues, so it made it quite difficult Accomplishments that we're proud of We are very proud of having a working application created on Forge, that behaves like we've imagined. We are even prouder of the time we spent to get here, on the user experience we provide, on how it's integrated in Jira and on how we used the whole Cloud pipeline with Bitbucket Cloud to deploy our Forge app. What we learned A few things actually, by digging in the documentation and finding what's the best for Overview: Editmeta API of Jira, which helped us a lot Atlassian JQL Forge component How to correctly use React Popper That's it's not easy, and not recommended to re-code Jira in Jira, just use existing components :) What's next for Elements Overview We plan on adding a few features to our app, but stay tuned, a Marketplace version will soon be available <div