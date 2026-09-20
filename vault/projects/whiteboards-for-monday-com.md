---
slug: "whiteboards-for-monday-com"
url: "https://devpost.com/software/whiteboards-for-monday-com"
title: "Virtual Whiteboards with video chat and GitHub integration"
hackathon: "monday.com Apps Marketplace Challenge: solutions for teams "
organization: "Monday.com"
winner: true
words: 427
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# Virtual Whiteboards with video chat and GitHub integration

> Do you miss your team collaborating on a whiteboard in your office? Whiteboards is the online collaboration tool that helps remote teams to collaborate and brainstorm in a remote work environment.

[Devpost](https://devpost.com/software/whiteboards-for-monday-com) · hackathon [[monday.com Apps Marketplace Challenge- solutions for teams]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[developer_tools]] [[security_privacy]]
**substrate** [[code_repository]] [[geospatial]]

**stack** gcp, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for whiteboards for monday.com

## Body

Add Monday.com items to your whiteboard. Seamless integration with Monday.com, editing items, and providing updates directly from the whiteboard. Add GitHub issues and pull requests to your whiteboards, and collaborate on them with your colleagues. Video conferencing built into the whiteboard, chat with your team directly on the whiteboard! Whiteboard is a view connected to your board Inspiration Monday.com is a an amazing tool with a well thought structure focused around timeline, topics, and the team. I wanted to add a bit of chaos into the mix. Physical whiteboard is a synonym of unlimited creativity, and I want to achieve the same with a virtual whiteboard, so that a team can collaborate in real time, or asynchronously. What it does The idea is to enable Monday.com users to organise their work items the way how they want, and collaborate on it in the most suitable way from their perspective. At the same time we want keep the data in Monday in sync, so they can come back to traditional views whenever they want. Software development teams are able to plan their work, and visually monitor the progress on a custom made board with drawings, animated gifs, GitHub issues, and Monday items. Whiteboards can help you with: Sprint planning, PI planning, running your daily standup meetings Brainstorming sessions, mind mapping, user story mapping, threat modelling Design sparring, collaboration on mockups, and diagrams ... and other types of collaboration you would normally do on a whiteboard Key features: Monday.com items: creating, editing, assigning, managing timelines, linking them visually GitHub integration: add GH issues, pull requests to your whiteboard Creative content: shapes, free hand draw, animated gifs, lines, curves, videos, content embedded via iframes Video conferencing Voting ... and everything else you would expect from a virtual whiteboard How I built it I'm using React, Firebase, and Twilio. The application is powered by whiteboards.io engine , and it had to be adjusted to Monday.com platform. Challenges I ran into I was anxious whether I will be able to embed existing code into a new platform. It turned out to be easy thanks to well thought APIs, and having a platform agnostic codebase. Discovering, and understanding Monday.com was the main challenge. Monday.com Community was the source of knowledge about users, and their needs. What I learned Monday.com concepts New app platform What's next for Whiteboards for Monday.com Deeper understanding of Monday.com specific user needs, add more depth to the app. Align design style of Whiteboards with Monday.com, so that it feels more native Add more integrations: Jira, GitLab, Azure Devops <div