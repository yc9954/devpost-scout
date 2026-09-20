---
slug: "timesheet-check-for-jira"
url: "https://devpost.com/software/timesheet-check-for-jira"
title: "Timesheet Check for Jira"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 1000
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/legal_justice"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Timesheet Check for Jira

> Using Jira and taking time management seriously, Tempo Timesheets will be your go-to solution.But what about legal requirements, and working laws? Timesheet Check for Jira gets you covered.

[Devpost](https://devpost.com/software/timesheet-check-for-jira) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[legal_justice]]
**substrate** [[regulation_legal_text]] [[sensor_telemetry]] [[structured_db]]

**stack** bitbucket, confluence, custom-ui, figma, forge, jira, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for timesheet check

## Body

Inspiration Since we had planned a familiarization and further training in the direction of Atlassian Cloud Ecosystem for this year anyway, the opportunity to take a closer look at the new technology Forge presented itself. Since Forge is supposed to be the future in Atlassian's cloud development, we naturally made it our immediate task to develop a meaningful and usable app so that what we had just learned could be put into practice. Of course, there were also other app suggestions, but after validating the apps, it turned out that Timesheet Check was an app that could be implemented well with the current state of Forge. Our company is using a similar feature of our server app xPort. Since xPort was not conceived and implemented for timesheet review, but for exporting Jira data, we thought it would be great to build an app that does just that. We thought about how to make it even better for the user to view and even more accessible for the admin to configure some Reports that validate timesheets. What it does If you use Jira and take time management seriously, Tempo Timesheets will be your go-to solution for tracking and reporting. But what about guidelines, legal requirements, and working laws? Timesheet Check for Jira is a versatile tool for defining rules that reflect these regulations and running them against Tempo Timesheets to ensure your timesheets comply with them. Timesheet Check comes with basic metrics like length of working days or daily rest periods to get started right away. Based on these metrics, rules are set up and ready to go in minutes to meet any regulations or internal company policies. Reports are the connection between rules and timesheets. All rules defined in a report will be checked against the selected timesheets to instantly show you whether a timesheet has passed or failed the checks. If checks fail, you will get details on the when and why. How we built it We started with a knowledge building in Forge. We checked some crucial topics like the difference between Custom UI and Forge UI, how to get started with Forge, possible entry points in Forge, and much more. Because of many different topics to study, we divided the topics among the team. We then shared the knowledge with everyone that everybody in the team was at the same level of knowledge. We wanted to build an app that was just an idea at this moment. That's why we had to specify everything in much more detail. We created mocks, specifications for the backend and for the Tempo Timesheets connection as well. A lot of meetings were needed to sync with the team and discuss the specifications for the whole app. All needed pages, dialogs, and functionalities were written down in Confluence, the tickets were created in Jira, and the code was stored in Bitbucket. Most of us were not that familiar with the Atlassian-Cloud products. That's why we decided to use Jira, Confluence, and Bitbucket as Cloud products for this project. The implementation was split into three different parts: Frontend (UI), Backend, and integration of Tempo Timesheets. Due to the detailed planning and specification, in the beginning, we could work on these three parts in parallel and just combined them when all three parts were finished. Of course, some problems we could not see in the planning phase came up when we implemented everything and integrated the parts. Extensive testing has always accompanied the implementation. Finally, the wording in the whole app was reviewed and changed if needed. Challenges we ran into We had to spend a few weeks with Forge and share all the new knowledge with the entire team so that everyone was on the same level of knowledge. We started with Forge Beta and had to watch out for many changes during development. Everyone always had to keep up to date with changes in Forge and update versions with caution. In addition to that, not everything related to Forge was documented that clear, so that we often had to reach out to Atlassian/CDAC to get all information right. We worked with Figma for the first time and often had to change the entire structure because we were not familiar with the tool. A requirement and a big challenge for our new app was to integrate data from a 3rd Party app. Accomplishments that we're proud of We are proud to have created such a great product in a very short time, with new technologies and a new team. We are proud to have built a working app with Forge even though we've started with Forge being in Beta status. We are proud to have launched a new product for Jira Cloud. We are proud to publish this project in the Marketplace as well. What we learned We learned the differences between a Forge UI app and a Forge custom UI app. We learned how to build a Forge app from the ground up and what the possibilities and limitations are. We got to know the Atlassian cloud environment better. We have learned to query data from 3rd party apps using initial authentication. We worked with Figma mocks for the first time and learned how detailed mocks could help build an entirely new app. Furthermore, we can now use Figma mocks in our daily work to create other apps or improve our existing apps. What's next for Timesheet Check We want to provide a function to export the results of a report as CSV as well as further rules to add more meaningful checks. Furthermore, Rule sets are to be introduced. A rule set is a collection of rules that you can define yourself to use later in your report as a group. This offers the advantage that you can pack, e.g., five rules, which are to be used in all reports, into a rule set and then only must select the rule set instead of the five rules for the report. <div