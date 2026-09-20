---
slug: "happee-know-how-your-employees-feel-by-collecting-feedback"
url: "https://devpost.com/software/happee-know-how-your-employees-feel-by-collecting-feedback"
title: "Happee - Company Happiness for Confluence"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 566
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/runtime_tool_creation"
  - "substrate/sensor_telemetry"
---

# Happee - Company Happiness for Confluence

> Whether your employees work in a remote team or share the same location, being happy at work means you're more engaged and productive & less likely to change your job. So Happee asks "How are you?"

[Devpost](https://devpost.com/software/happee-know-how-your-employees-feel-by-collecting-feedback) · hackathon [[Codegeist 2020]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[runtime_tool_creation]]
**substrate** [[sensor_telemetry]]

**stack** atlassian-apis, atlassian-connect, firestore, javascript, love, scss, typescript, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for happee - know how your employees feel by collecting feedback

## Body

Welcome to Happee! Let's tell us how you feel Rate how you feel about your team How happy are you with the company? What made you feel good this week? Is there anything that concerned you? All of the questions can be answered anonymous, so your feedback can be really honest. At the Happiness Dashboard you can see different kind of metrics related to the given votes. This is your personal Happiness Index. You can compare your votes with the average votes of your colleagues. The overall company happiness shows the average results of the last weeks. Take a look at the feedback wall to see the latest feedback entries. Inspiration We are working completely remote for months now. We have experienced how difficult it is to get an insight of how our coworkers feel, especially how happy they are with the team and the company. There are no conversations in the tea kitchen any more, nor is there any lunch together, where people talk about the good and the bad things at work. Especially for roles such as Scrum Masters and Agile Coaches it is a special challenge to have so little personal contact in order to identify where challenges currently exist. With Happee we want to bring teammates closer together - no matter if they are working co-located or remotly. What it does Pulse survey On a regular basis, employees are asked to measure their personal happiness, happiness with the team and also with the company. Facts that influence their mood are asked as well. The survey only takes a couple of minutes and the employee can choose whether to share his or her name or to remain anonymous. Dashboard Happee offers a simple and effective analysis of the submitted results. A dashboard provides the possibility for employees to compare their own mood with the company's average or to review how the happiness has changed over time. How we built it We built the Front-end with Vue.js – the data persistence is handled via Google Firestore and the Authentication mechanisms are implemented with Atlassian Connect. The backend is running on Cloud Run. :) Challenges we ran into iFrame resizing of the macros and dynamically generated lists can get a bit tricky when developing Confluence Cloud apps. Accomplishments that we're proud of We built the MVP in a week after work ❤️ What we learned It is worth the time to build a good development set-up. We achieved this using ngrok and nodemon to emulate our microservices locally. This way we were able to build our backend without time intensive deployment delays. The atl.general webPanel location is quite handy when implementing an application wide reminder functionality. Combined with a cookie within the Connect iFrame we used it to show a notification if the user can share information regarding his or her happiness. What's next for Happee - Know how your employees feel by collecting feedback Next, we want to provide the possibility to start an interaction based on the feedback. It will be possible to vote on feedback items or start a discussion with other people. Recommendations will be shown depending on the personal entries: For example, if there are negative entries, Happee suggests you to address them in the next retrospective or discuss them with a Scrum Master or any other teammate who you trust. We also want to add more metrics . <div