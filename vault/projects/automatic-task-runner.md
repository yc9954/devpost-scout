---
slug: "automatic-task-runner"
url: "https://devpost.com/software/automatic-task-runner"
title: "Automatic task runner"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 411
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
---

# Automatic task runner

> This is a collection to run task easily and automatically, using mock servers for testing not applicable for real project, it use monitor to run the collection and slack to give real time feedback

[Devpost](https://devpost.com/software/automatic-task-runner) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[structured_db]]

**stack** javascript, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for automatic task runner

## Body

Request to the mocked server with and errors Monitor info with the info of the collection Slack notification at the end of the collection Inspiration This solution was inspired in real situation that happens when database are really bigs and the queries are not the best option because it is necessary to dispach events or emails users, in this case it is necesary to run tasks for these. What it does It lets us run tasks in order to update the information or whatever we want, using some resource especified in the server (in this case we are using mock server) time by time and automatically and at the end of the process a slack message is dispached with the information of the failed resources or with and okay message. To show the fails resource information it was organized to received no matter how many parameters at first level, it will show them in slack notification. How we built it All the project was build using postman, the server was mockery using mock server and collections and a monitor was setted to run the collection once by week (these could be changed). Challenges we ran into One of this was to use the mock server because it was my first time using and then using with test and pre-request Script, but at the end it was really easy to mock request. Accomplishments that we're proud of I was very happy to discover how the use mocked collection and server, it is very useful to create task without the needs of a real server or a full project. The monitor is also very interesting and useful because we can automate the task and because we are using slack to notify we can be aware of this What we learned I learned how to used tests, Pre-request Script alongs with mockery and monitors, and how to notify through slack. I also learned how to protect my mocked server through and x-api-key. I've also learned how to use the documentation, this is really easy and cool to see, because it use the request setted to show how to make a request and we can easily specify if show the info with variables or real info. What's next for Automatic task runner It will be cool that the community start to used has I said it was built using just postman but the idea will be to integrate with real application and real task. <div