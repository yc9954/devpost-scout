---
slug: "ai-insights-for-jira-service-desk"
url: "https://devpost.com/software/ai-insights-for-jira-service-desk"
title: "AI Insights for Jira Service Desk"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 337
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# AI Insights for Jira Service Desk

> Measure and report your on your customer’s experience from within Service Desk in real time via AI linguistic analysis. Build dialog strategies to adjust conversion patterns accordingly.

[Devpost](https://devpost.com/software/ai-insights-for-jira-service-desk) · hackathon [[Codegeist 2020]]

## Facets

**mechanism** [[realtime_stream]]

**stack** forge, ibm-watson, quick-chart

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what i learned
- what's next for ai insights for jira service desk

## Body

Issue satisfaction timeline Agent conversation scores Customer satisfaction chart Problem tickets reported on the dashboard Inspiration There is a huge potential for the use of AI within the cloud space to support and enhance business processes. Taking advantage of an opportunity to leverage the Forge framework to get a taste for what might be possible was a 'no-brainer' What it does The app uses the IBM Watson Tone Analysis to detect tones and emotions found in Jira Service Desk ticket conversations. Tones detected with this endpoint include frustrated, sad, satisfied, excited, polite, impolite and sympathetic. Conversations between user agents and customers are broken down and given a score according to their tone. Real time updates and a timeline of conversation tones are displayed via the quick chart API right within the issue panel. Tones and their scores are then stored within Jira for filtering, reporting and tracking. How we built it Forge of course... and with some help from the Jira Kanban board and Bitbucket. The Forge Slack channel was helpful. Challenges we ran into We only decided to have a go at building this proof of concept within Forge for codegeist early in June. Just 10 days before Codegeist entries were due to close! We wanted to get a feel for forge and see if we could actually stand something up in such a short amount of time. We definitely would have liked a little more time to refine and polish things a little more.... Accomplishments that we are proud of We think our app is pretty cool. Like playing with Siri or Alexa right within Service Desk. Working out how to incorporate the quick chart API into the Forge UI was rewarding too. What I learned We learnt that Forge has great potential and will keenly watch and support further development. What's next for AI Insights for Jira Service Desk We plan to utilise the winnings from Codegeist to plan and build a fully featured version of this app for the Atlassian Cloud marketplace. <div