---
slug: "scrbot-ai"
url: "https://devpost.com/software/scrbot-ai"
title: "SourceBot"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 830
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# SourceBot

> Hello world! I'm SourceBot and I have one job - to boost developer's effectiveness. I will provide your team with daily updates on the project’s progress but also motivate you when needed!

[Devpost](https://devpost.com/software/scrbot-ai) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[structured_db]]

**stack** github, java, openapi, postgresql, postman, slack, springboot

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for source bot

## Body

How it works? Step-by-step Elevate effectiveness of your team with SourceBot Inspiration Our idea originated from Agile Information Radiators which are displays of key team information openly shared with all team members. We are convinced that representing project key information can be beneficial in an agile organization - teams are more collaborative, transparent and accountable and ultimately, efficient . But not all radiators are created equal… For us it was not about throwing sticky notes on a wall in the office and calling ourselves “agile”. We wanted to create something truly effective , especially when taking into account the current obstacles like the whole world shifting to remote work all at once. Facing the everyday challenges which pandemic brings and the fact that most people won’t return to the offices full-time, we had to think outside the box.. I mean the office! Hence, we decided to use Slack which is commonly used for daily communication among the remote teams. The aim was to be effective but also engaging and fun. We brainstormed ideas and our SourceBot (srcbot.ai) was born. He is a smart cookie! Not only does he share the project’s progress daily but motivates the team when they are running behind and gives them tips. We wanted the SourceBot to be much more than stats so we didn’t forget to equip him with humor and wit. He cracks a joke here and there – all to make programmers’ work life not only easier but also more pleasant ! What it does It’s an integration of software repository and simple code metrics analysis displayed in a form of Information Radiator in Slack. Our Source Bot not only displays the daily summary, he motivates teams when they run behind and also praises them for completing tasks on time. Some of the metrics the tool tracks are number of new lines of code written per person and per team member, code coverage by tests, static code analysis, number of days until the end of the projects and many more. How we built it The API was developed in JAVA / Spring Boot and the Postgresql database. Code analysis is performed in the background by external algorithms. The analysis result is parsed, statistically converted and saved in the database. Then made available to the indicated channels of Slack messenger. Code analysis is performed using: BitBucket GIT JACOCO SpotBugs CLOC JUNIT Challenges we ran into We are a team of developers already creating API’s for organisations. In this instance, we wanted to showcase our experience, which is why we used the OpenAPI specification for the first time. We used API mocks (which we don’t practice on a daily basis) to properly distribute the work amongst the team and design the API in a conceptual layer. Due to the fact the API will be public we want to ensure its high accessibility monitored by Postman tools. Accomplishments that we're proud of We have managed to combine over five advanced code analysis tools and turn them into shortened and humorous notes that are automatically published on Slack every day. With this tool, you can integrate and motivate remote developer teams even more. As experienced programmers we created this API mainly with our own teams in mind. Even though it was made by us for us, we hope that if it proves such a huge value , it will be welcomed by others with much enthusiasm too. Of course, different developers will use other external tools and analyze the code in detail, but our tool’s aim is to provide information very quickly and without any entry barriers . It works like a pedometer on any mobile device, always at your fingertips and you don’t have to remember to turn it on because it always works in the background. We are proud that we managed to achieve this . What we learned We learnt a lot about how to successfully build API using Postman and how to use its web tools. It’s a big win for our innovation team which will hopefully allow us to expand our business. We also learned about OpenAPI Specification. Not to mention learning how to integrate with Slack :-) What's next for Source Bot We hope our idea gets acknowledged as we would love to find a way to commercialize it. In the immediate future we want to integrate this solution with other tools like: Trello, JIRA, Confluence etc. The actual tool will be capable of integrating with many tools, not limited to those that are currently integrated with Slack. We want to continuously improve code stats for instance dedicated to other languages like dart, python or javascript. Additionally, in our development plans we also consider implementing individual stats besides the current project stats. Lastly, we want to keep developing the “character” of our bot, enhance the graphic capabilities, for instance allow him to send daily memes or other graphics simply to keep up team morale and put smiles on everyone’s faces. <div