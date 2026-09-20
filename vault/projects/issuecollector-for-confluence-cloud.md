---
slug: "issuecollector-for-confluence-cloud"
url: "https://devpost.com/software/issuecollector-for-confluence-cloud"
title: "IssueCollector for Confluence Cloud"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 376
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/web_dom"
---

# IssueCollector for Confluence Cloud

> Easily create preconfigured Jira issues in Confluence without using unsafe HTML macros

[Devpost](https://devpost.com/software/issuecollector-for-confluence-cloud) · hackathon [[Codegeist 2021]]

## Facets

**substrate** [[web_dom]]

**stack** forge, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for issuecollector for confluence cloud

## Body

Issue Collector Form Issue Collector Config Inspiration I think the key inspiration was the simple Feedback Collector in the example forge apps. The sample app opened up the idea of collecting customised issues easily within Confluence and just the possibilities of Forge in general What it does In short, it lets you create highly configurable issue collector forms within Confluence Cloud, The longer description is that it dynamically fetches the fields of the selected project and issue type to create an adaptive config menu where the user can customise the following: Which optional fields to include in the form (any field available for that project + issuetype combo) Ability to preset values for fields (and have the field show up for the user to edit, or hide and always set as preset) Ability to choose a custom label for each field to effectively rename it in the form These configurations allow the presentation of the customised form for the Confluence users to fill out and create Jira issues How we built it Looking to the feedback collector as an initial example, I looked into ways to use the Jira API to find out which fields are available for a specific project and issuetype. From there it was a process of using the available Forge Confluence Macro form inputs to adapt to the fields depending on their type. Challenges we ran into The biggest challenge was figuring out how to code something flexible enough to adapt to all sorts of issuetype fields including customfields Accomplishments that we're proud of The end result :) It has quite a lot of functionality for a forge macro What we learned This definitely highlighted the capacities of Forge, so I learned what its capable of and am a lot more ready to use and implement it going forwards. Already have a few more ideas for projects but there's only so much time in the hackathon. What's next for IssueCollector for Confluence Cloud I'm hoping to refine it and develop it into a Marketplace app, at the moment you have to provide it with env variables for baseUrl as well as username and token, I think this may need to be adjusted before it turns into a viable market place app. <div