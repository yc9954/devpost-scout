---
slug: "super-saiyajira"
url: "https://devpost.com/software/super-saiyajira"
title: "The Saga of the Super Dev"
hackathon: "Devs Unleashed"
organization: "Atlassian"
winner: true
words: 1126
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# The Saga of the Super Dev

> Live the life of an aspiring developer starting out as a trainee until you become a Super Dev! You will have tech questions, career advices and after you become Super dev you get access to rankings!

[Devpost](https://devpost.com/software/super-saiyajira) · hackathon [[Devs Unleashed]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]]

**stack** java, javascript, maven, phaser.js, postgresql, vps

## How they structured the write-up

- the team
- inspiration
- what it does
- throubleshooting
- how we built it
- challenges we ran into
- accomplishments that we're proud of && what we learned
- what's next for the saga of the super dev

## Body

The Saga of The Super Dev Valuable Career tips The hall of the Super Dev's Part of the map The Rankings when you get the Super Dev level The Credits Welcome to (♪♪ thrilling song ♪♪) The team Hi everybody, we are Guilherme, Pettrus, and Weslei. Inspiration We were thinking about what kind of game makes sense for developers to play as they work. What if we can make them learn new things by challenging them in the game, and at the same time make them work? The company would have engaged employees and the employees would evolve as a professional. Inside the Atlassian ecosystem, we have everything to feed up the game and control the players' progress. There are cards inside Jira, documentation inside the Confluence, and code inside Bitbucket repositories, and much more. This can be explored in many ways. The way the game is fed up and is quite well mapped, but how to make people feel like playing? Most developers are moved by challenge, that's why there are a lot of code-challenging tools and hackathons out there. So, as part of this first delivery, we thought about quizzing the players with IT questions, and as the player evolves parts of the map will get unblocked. Ok, but what's the history behind the game? Well, yourself. It's about your Career Path. As you explore the world, you will find out companies that might challenge you with questions, others are not open to you since you might not have experience enough to get in. You might get valuable career tips along the pathway in the Saga to become the legendary The Super Dev . What it does The Saga of the Super Dev is a game where your efforts in your real company will be given credit through your XP bar and levels, but at the same time, you can drive your character on the map looking for achieving knowledge either by getting into companies to be interviewed with IT questions or interacting with people in the streets. XP bar - level. See also the button below is to refresh your XP that was not computed yet. You can get XP either by finishing tasks in JIRA, opening/merging PR's on Bitbucket, and creating/updating pages on Confluence. As you get XP you might level up. bitbucket branch merged confluence page created Jira card moved to done Make sure you have answered all the questions inside the buildings, otherwise your level may not upgrade. Answer carefully or points might be taken from you. You can follow the progress of your question on the top-right bar, and your XP on the top-left bar. See below: Above, you are outside of the first level building, each level has a specific building to be unblocked. You can get in and go directly to the character in the middle to be questioned: Note that if don't have enough experience you will have a guard asking to come back when you have another level: You can receive valuable Career Tips from different characters during your pathway: ♪♪ Enjoy the different soundtracks on the map ♪♪ The main purpose of the game is to overcome all proposed challenges, evolve for the proposed levels, get tips to improve your career, and become the legendary Super Dev . At this level you will get access to the fanciest building, and get access to the top4 ranking: Rules: Move the Jira task to 'Done' on the project: 10XP Open Pull Request: 1XP Merge Pull Request: 10XP Pull Request Cancelled: -1XP Create Document on Confluence: 10XP Edit Document on Confluence: 1XP Question answered correctly: Question bar counter increases +1 Question answered incorrectly: -3XP Ps: If you don't answer the 2 questions proposed by the game, your XP might increase until the limit to the next level. To level up, the 2 questions are a requirement. Throubleshooting The language of Atlassian Products must be ENGLISH. You have to start Jira, and create a Project with a Kanban template that has a column 'Done'. This name is very important since ONLY when the cards are moved to this state that the points will be computed. You have to start Confluence also. You can set up your BitBucket repository also in the main menu of the game. The game page it self instructs how you set up (Basic Authentication) Known limitation: When you level up with the game opened, make sure you go inside any building and then come back to the guard. He will have left. Instructions are on the https://youtu.be/hDiR-YdMjms How we built it Frontend: Phaser v3 ( https://phaser.io/ ) : Boilerplate https://github.com/blopa/top-down-react-phaser-game-template with the MIT license Edited/created all the new assets using the tool Tiled provided by https://www.mapeditor.org/ React JS ( https://reactjs.org/ ) Backend: Javascript Forge modules: jira:globalPage, trigger, and Webtrigger. Jira API Confluence API Bitbucket API/Webhooks AI human voice to present the game intro This content was produced with Typecast, an AI virtual actor service. Characters casted: Angela https://typecast.ai Challenges we ran into The documentation that Atlassian provide is spread and we took some time to figure out everything. Search inside the Atlassian platform does not always give the best results, then we google it to direct us to the Atlassian page. Confluence documentation is very confusing, they don't provide a UI for webhooks and don't accept basic authentication like Bit Bucket. I understand that this might not be the safer approach, but when you are working in a POC for example, you don't want to waste time on side features. Forge API can't share the storage between apps, so Confluence has a different scope the Jira, for example. So we decided to move from storage to an external source for this delivery. Understand how the phaser works and create new assets. Accomplishments that we're proud of && What we learned We are proud of the integration that we created between all services from Atlassian and the game interactivity Learned the Atlassian ecosystem and how its apps and modules work. Created a functional game end-to-end using new technology. This was the first game that we have ever created. It was a huge challenge, also, and we had no idea how to deploy an app in the Atlassian cloud. Getting through the documentation and delivering a functional game on a time was very satisfying. What's next for The Saga of the Super Dev FEATURES Give the possibility to choose other characters Tips and Questions according to your level Possibility become the CTO of a company Add more challenges and rewards with badges Possibility to integrate with hackerrank-like tools Possibility to improve the dev's house Add multiplayer where players can interact with each other Tech debit: Implement Oauth2 Implement Confluence webhook Work on improving the responsivity <div