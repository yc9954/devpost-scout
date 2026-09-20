---
slug: "support-time-contract-management-for-jsm"
url: "https://devpost.com/software/support-time-contract-management-for-jsm"
title: "Support Time Contract Management for JSM"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 554
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Support Time Contract Management for JSM

> Support time contract management right within Jira Service Management

[Devpost](https://devpost.com/software/support-time-contract-management-for-jsm) · hackathon [[Codegeist 2022]]

## Facets

**substrate** [[financial_record]] [[sensor_telemetry]]

**stack** forge, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Configure support time quota contract right in JSM Expose metrics directly in customer portal Realtime monitoring of support time contracts.. Inspiration Its interesting to see how Jira Service Management can be used across multiple industries. One use-case for JSM users is tracking time that has been spent on the support contract and exposing it to their customers via the portal. This was a use-case requested by many customers for our flagship App, and we decided to create a Forge App to expose support contract metrics directly in the customer portal. What it does To explain what the App does, lets take ACME - which services their customers using JSM and uses support contracts to track the hours spent for support . Example - Customer A has a support contract for X hours, say 240 hours per year. ACME wants to set up a shared dashboard where a Customer A can see how much time has been spent on their support contract, preferably via a Gauge chart. Thus the solution (Forge App) helps JSM users - Configure support time quota/contract for your organization right in JSM Expose support contract metrics directly in the customer portal bringing transparency to your customers How we built it We divided the project into multiple phases. Phase 0 - Phase 0 comprised the feasibility study of what could be technically achievable, the limitations of the Forge platform, solution of the problem statement, etc. Phase 1 - Phase 1 focused on piloting the core capabilities and building the screens and user flow. We tried out the new JSM Forge modules and exposing support metrics in the customer portal. The pilot POC gave us the base for refining the solution and revisiting our drawing board to evaluate what customers would appreciate as a value add to the core solution. Phase 2 - Based on the trials from Phase 1, we reprioritized the backlog. We also limited the level of configurability to ensure speed to market. We went from requirements to an alpha build that our team could test internally in a short amount of time. Challenges we ran into While testing out the App, we found that Forge app won’t be shown in customer portal for JSM customer users FRGE-189 . So we do have a limitation of the App working only for internal customers until we get FRGE-189 fixed by the Forge team. Accomplishments that we're proud of We are now very familiar with the Forge platform, its features, and its current limitations. Since the last Codegeist, we have view26 Labs initiative exclusive for Forge App ideation. What we learned Posting on the Forge Community is a good way to get issues resolved. Atlassian team & others are quick to share their experience & resolve the issues faced. We also intend to use a 'Forge first' development approach for our Cloud apps going forward as we build expertise on the Forge platform. What's next We have the App already listed on the marketplace and the results are quite encouraging. One requirement from our early users was the ability to exclude certain worklogs - Eg. Non billable hours. As a solution we have added support to exclude worklogs with prefix in the App settings page. We are now working on optimizing the worklog calculation by making use of Forge product triggers. <div