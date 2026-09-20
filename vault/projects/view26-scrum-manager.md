---
slug: "view26-scrum-manager"
url: "https://devpost.com/software/view26-scrum-manager"
title: "view26 Scrum Manager"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 807
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/media_journalism"
  - "domain/supply_logistics"
  - "substrate/financial_record"
---

# view26 Scrum Manager

> A connect on Forge App to intuitively capture team updates and blockers to significantly improve the daily stand-up experience for the Scrum Master.

[Devpost](https://devpost.com/software/view26-scrum-manager) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[media_journalism]] [[supply_logistics]]
**substrate** [[financial_record]]

**stack** connect-on-forge, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for view26 scrum manager

## Body

Capture daily updates from each team member Daily stand-up card deck for the scrum master Inspiration I am the Scrum Master at VIEW26 . One challenge I usually face is that my daily scrum calls end up extending longer than usual, with some critical issues being missed and a few non-key matters being discussed for much longer than required. I am sure you would have faced these issues in your daily scrums too. My team at VIEW26 realized that a tool that intuitively captures the daily updates and blockers would significantly improve the stand-up experience. This is how the Scrum Manager was born. What it does Scrum Manager App helps the Scrum Master :- a) focus on the key issues/bottlenecks b) have a precise and time-bound discussion c) have a fun experience through gamification The App captures daily updates from each team member by capturing the response for the below questions What did I do yesterday? What am I planning to do today? Do I have any blockers/ impediments? In addition, teams can flag Jira Issues as blockers and add generic comments for non-Jira tasks they worked on since the previous stand-up. Now, once the team updates the stand-up details, the details are available for the Scrum Master. On clicking the 'Daily stand-up,' the Stand-up deck opens up. The updates from the team are stacked up like a deck of cards and are sorted based on their criticality, i.e., the most blocked items will be picked first for the stand-up meeting. The stand-up duration can be adjusted on the Settings page. You can also configure the default option of stacked card display order - either by alphabetical order or by the number of items at risk. The Scrum Master starts the daily ritual by clicking on the Start button. The card timer kicks in and starts the countdown. The Scrum Master can decide the pacing of the daily scrum by controlling the navigation to the next card. The summary card helps you to record action items and summarizing the stand-up meeting. You can handpick the Jira issue that needs to be tracked for the next stand call by pinning the issue. There is also an option to retrieve the Summary Card archives, even during the stand-up for follow-ups. The daily scrum meeting is completed by clicking on the timer stop button. The team is awarded fun badges at the end of the stand-up based on the previous streaks, a bit of gamification. How we built it We divided the project into multiple phases. Phase 0 - Phase 0 comprised the feasibility study of what could be technically achievable, the limitations of the Forge platform, solution of the problem statement, etc. Phase 1 - Phase 1 focused on piloting the core capabilities and building the screens and user flow. We tried to populate the cards based on the data, which was readily available from the Jira board. The pilot POC gave us the base for refining the solution and revisiting our drawing board to evaluate what customers will appreciate as a value add to the core solution. Phase 2 - Based on the trials from Phase 1, we reprioritized the backlog. We also limited the level of configurability to ensure speed to market. We went from requirements to an alpha build that our team could test internally in a short amount of time. Challenges we ran into Being a new platform, Forge was indeed a challenge for us to work on during a short period. We ran into an initial problem: Forge did not support all the available locations(jira.software.board.tools) supported by Connect for Web Items. The Atlassian team was quick to point out using Connect on Forge as a possible work-around. Apart from that, we had to resolve manifest file validation issues and a work-around to get to the final submission just in time. Accomplishments that we're proud of With a new team to the Forge platform, we are proud of our very first Connect on Forge App. What we learned We became very familiar with the Forge platform, its features, and its current limitations. Posting on the Forge Community is a good way to get issues resolved. Atlassian team & others are quick to share their experience & resolve the issues faced We also intend to use a 'Forge first' development approach for our Cloud apps going forward as we build expertise on the Forge platform. What's next for view26 Scrum Manager Since this is an initial start, we hope to develop more features after receiving user feedback post-Codegeist submission & marketplace beta listing. We want to work on a couple of features, such as full-fledged gamification, value-added Reports, Alerts via Slack/Email, etc. Looking into the architectural aspects between the Forge and Connect parts is also something that we have in our Forge App development roadmap. <div