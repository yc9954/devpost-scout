---
slug: "retrospective-tools-for-jira"
url: "https://devpost.com/software/retrospective-tools-for-jira"
title: "Retrospective Tools for JIRA"
hackathon: "Atlassian Codegeist: Add-on Hackathon"
organization: "Atlassian"
winner: true
words: 455
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "substrate/structured_db"
---

# Retrospective Tools for JIRA

> Improve team's effectiveness and efficiency by analyzing project history

[Devpost](https://devpost.com/software/retrospective-tools-for-jira) · hackathon [[Atlassian Codegeist- Add-on Hackathon]]

## Facets

**mechanism** [[cross_origin_web]]
**substrate** [[structured_db]]

**stack** appengine, atlassian, flask, javascript, jira, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for retrospective tools for jira

## Body

Inspiration Retrospective meetings. JIRA lacks advanced tools for analysis of history of projects, in particular for the agile and lean teams using Kanban or Scrum. The teams I worked with wanted to see replay of the project progress and JIRA stores all the information required to make it possible. What it does Allows the teams to analyze history of iteration, sprint, or any other part of the project in order to improve efficiency and effectiveness. Animations visualise the flow of work - you can actually see what happened during the project in fast forward replay of project's history! Seeing 2 weeks of the project in 1 minute animation can really open your eyes to the team dynamics. Identification of problems with the workflow is aided by selection of charts and analysis : statistics about times issues spend in statuses (can be used for forecasting), visualisation of progress of each issue on a timeline, Cumulative Flow Diagram and others. Filter issues to analyse with JQL , filters , or use configuration of any board Configure columns yourself or use any board's column configuration All easy to use, works out of the box or requires small edits to column configuration. How I built it Appengine with lightweight Flask for server APIs. JavaScript (jQuery, Highcharts) and lots of patience for the UI work. Challenges I ran into Optimisation of performance for animation of large number of issues. Accomplishments that I'm proud of Smooth animation of status changes of issues is something I haven't seen anywhere else. It required some patience and a lot of tweaking to get nice visual effect. Playback of history makes it really easy to get the feel of the team and get to the bottom of problems. What I learned Unfortunately the biggest learning was the limitations of Connect APIs at the moment. There were 2 fairly big problems that made me rethink the concept of the add-on: JIRA Server version of the plugin has playback controls that are affixed to the bottom of the screen. That makes it easier to operate with large number of issues as you see the controls at all times. This is not possible to achieve in Cloud add-on as it's rendered in iframe. You cannot impersonate any JIRA user when calling JIRA REST API from the server. Because of that searching for issues has to take place in the client. This is not how I originally imagined it working. What's next for Retrospective Tools for JIRA [RELEASED in 1.0.9-AC] Integration with JIRA Agile/JIRA Software - replay history of all the issues from Agile board (Scrum or Kanban). There won't be the need to configure columns manually. Coming soon: Data export for further analysis outside JIRA (e.g. spreadsheets) <div