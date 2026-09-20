---
slug: "upguard"
url: "https://devpost.com/software/upguard"
title: "UpGuardian"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 523
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# UpGuardian

> Struggling with accidentally making subtle breaking changes to your APIs? Are those sensitive unit tests failing all of the time even though unimportant things have changed? Well you are in luck!

[Devpost](https://devpost.com/software/upguard) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]]

**stack** fastapi, flutter, nemotron, python, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for upguardian

## Body

MVP defined for what this app should do detailing how the pages should look as well as example UI Inspiration Migrating a service to a new API version is often the most tedious troubleshooting an application developer can go through. Verifying that different endpoints work and combing through different responses to find minimal but important differences takes valuable time that could have been spent developing features. We wanted to make API upgrades easy for developers so they can focus on their applications' business logic. What it does UpGuardian helps developers with the process of updating their codebases to handle upgraded versions of the APIs they rely on. Using reliable difference detection paired with structured agentic AI intuition, this service works together with the developer to guide them through discovering breaking changes to the APIs. The dashboard provides a way for developers to give UpGuardian insight into the APIs they use by uploading known request logs, and to see the results of the tests they run. The service is designed to mediate the dashboard's access to APIs, keeping them secure and preventing access token leaks. We planned from the beginning for it to be possible for multiple developers and organizations to share an instance of the UpGuardian service, and although we have yet to implement the necessary security layer for this, we already have the groundwork for authentication and isolation in our codebase. How we built it The UpGuardian dashboard is made in Flutter, and communicates a service made with Python and FastAPI in order to allow a developer to configure their applications' endpoints and see results. We used the agentic Nemotron AI model from Nvidia to intuitively distinguish the ways in which API response formats have changed. The UpGuardian service reliably and deterministically detects differences between old and new response formats, and the AI-powered agent guides the detection to make sense of the discovered differences and helps the developer build a set of known changes. Our database code is meant to be modular and extensible so that future implementations of the database can easily be added, ensuring scalability. Challenges we ran into Some challenges we ran into were convincing the AI agent to give as specific outputs as possible, as well as preparing all the necessary parts of this project in the given time. We were also not able to find a room until 3pm. We were waiting outside of a hackerspace since 8am. However, the staff told us the room was not a hackerspace and we lost a lot of time there. Accomplishments that we're proud of The UI was inspired by Github and IntelliJ Idea to hopefully give this fledgling developer tool a familiar feeling for developers and admins. Bridging the gap between structured, deterministic logic and the black box that is an LLM was an interesting problem to solve, and we hope we have prioritized reliability in a way that can be used in production. What we learned This project helps us learn to prompt engineer agentic models, validate schemas, and work with server-to-server communication to bring multiple APIs together. What's next for UpGuardian The world is our oyster. <div