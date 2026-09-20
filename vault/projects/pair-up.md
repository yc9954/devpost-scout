---
slug: "pair-up"
url: "https://devpost.com/software/pair-up"
title: "Pair Up"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 472
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "substrate/geospatial"
---

# Pair Up

> Pair Up helps remote teams address their Jira issues efficiently by leveraging tribal knowledge held within their organization.

[Devpost](https://devpost.com/software/pair-up) · hackathon [[Codegeist 2020]]

## Facets

**mechanism** [[graph_reasoning]]
**substrate** [[geospatial]]

**stack** amazon-web-services, connect, ibm-watson, network-x, node.js, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for

## Body

Pair Up App Relevant people with expertise Relevant issues Dynamic keywords and list of people Inspiration In most vertical engineering orgs, each agile team owns a piece of the product from end-to-end. A frequent problem faced by individuals on these teams is to identify the best person in the org who can help unblock important bugs and enable them to make progress. This has become more challenging with the current pandemic related lockdowns, where teams have become remote and quick communication across orgs is becoming difficult given fluid schedules and time-zones. What it does When you launch the Pair Up issue glance, the app ranks people in your org who would be best suited to resolve the current issue based on similar issues they have resolved in the past. It also maps these individuals to the Jira issues they've fixed, that the app found relevant to the one currently being worked on. Pair Up helps users quickly connect with the right people and solve the issue more efficiently. How I built it We built the app as an issue glance using the Atlassian Connect framework. The app has a webhook module to process new issues and updates to existing issues. In the backend, the app uses AWS Lambda and IBM Watson NLU AI Framework to find relevant keywords from the summary and description of issues. Based on the analysis of keywords, we build multiple knowledge graphs using NetworkX, which in turn identifies and ranks people who have the experience to resolve the issue. Challenges I ran into Finding the right UI elements to use in the issue glance was a bit challenging. There was a bit of confusion on whether we should use Atlassian UI (AUI) or Atlaskit for the UI elements. Accomplishments that I'm proud of The app does a good job at identifying related keywords in issues, some of which might not have been explicitly mentioned by the reporter. Finding and ranking these people cannot be done purely based on keywords as most issues have multiple keywords. To overcome these issues, we built custom knowledge graphs for each issue which ranks importance of all people in the org to resolve this issue based on all issues they had resolved previously. We also had to fine tune our usage of the Watson API and our graph algorithm in order to accomplish this. Since we designed it with a cloud-based approach, the app is extremely scalable, reliable and capable of handling production load. What I learned We learned how to develop an Atlassian app and use the Atlassian UI elements in a way that maintains the look and feel of Atlassian products. What's next for Integrate with Confluence in order to make the knowledge graph more accurate and targeted Integrate with tools like Slack to make the collaboration easier and seamless. <div