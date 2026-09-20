---
slug: "request-cachet-and-analyzer"
url: "https://devpost.com/software/request-cachet-and-analyzer"
title: "Postman Process Automater"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 235
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
---

# Postman Process Automater

> Service which automates sequences of various Postman requests with Python.

[Devpost](https://devpost.com/software/request-cachet-and-analyzer) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]]

**stack** javascript, linux, mongodb, postman, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for postman process automater

## Body

View of the Postman Process Automator tool as seen by a user without a Postman account who is exploring useful collections. Inspiration Many long hours spent writing hard-coded programs to execute sets of ordered API calls for inter-system endpoint coordination or system diagnostics. What it does Postman Process Automator generates API request sequence automation scripts by passively observing the user's activity in the Postman suite as they use their APIs built with the Postman tool set. How we built it First, a back-end service built with ExpressJS and MongoDB was built to record the request sequences and generate the Python automation script. Next, the Postman scripting and environment tool sets were used to build functionality which observes and replicates user-specified requests as the requests exit the Postman suite. Finally, a Postman collection was constructed to enable simple tool usage and interactions with the back-end service so that the user does not have to leave the Postman Suite to use the tool. Challenges we ran into Integrating the back-end service with the Postman functionalities required lots of testing as Postman's simplified tool sets are less complex and easier to use than typical back-end programming. Accomplishments that we're proud of What we learned The powerful yet simple-to-use tool set offered by the Postman suite. What's next for Postman Process Automater An open source project where various developers can contribute to the growth of the system's functionality. <div