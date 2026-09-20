---
slug: "caterpillar-zombie"
url: "https://devpost.com/software/caterpillar-zombie"
title: "Caterpillar Zombie"
hackathon: "Devs Unleashed"
organization: "Atlassian"
winner: true
words: 425
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
---

# Caterpillar Zombie

> Caterpillar Zombie is a game where players defend their fruits from invading zombie caterpillars. The game turns in progress bitbucket project issues into an invading army of caterpillar zombies.

[Devpost](https://devpost.com/software/caterpillar-zombie) · hackathon [[Devs Unleashed]]

## Facets

**domain** [[developer_tools]]
**substrate** [[code_repository]] [[sensor_telemetry]]

**stack** bitbucket, css3, forge, html5, javascript, jira, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for caterpillar zombie

## Body

Game User Interface 1 Game User Interface 2 Game User Interface 3 Game User Interface 4 Game User Interface 5 Game User Interface 6 Inspiration Fixing bugs and reviewing open pull requests can be hectic. The purpose of this game is to make the process of managing bitbucket project issues more fun by turning pending pull requests into an invading army of caterpillar zombies. What it does Caterpillar Zombie is a invasion game where players defend fruits from invading zombie caterpillars. The game turns in progress bitbucket project issues, open pull requests, and active alerts into an invading army of caterpillar zombies to defeat. The larger the number of unresolved bitbucket project issues get, the longer the Caterpillar Zombies get and the fewer the number of unresolved Jira issues get, the shorter the Caterpillar Zombies get. How we built it We use the bitbucket API Call to fetch fetches open issues from the bitbucket RESTful API. The data is stored into a log file inside the game. The game reads the log file and identifies the number of in progress bitbucket project issues, open pull requests, and active alerts, and uses these numbers to construct an invading army of caterpillar zombies. The larger the number of unresolved bitbucket project issues get, the longer the Caterpillar Zombies get. Likewise the fewer the number of unresolved bitbucket project issues get, the shorter the Caterpillar Zombies get. To see the caterpillar zombies increase in length, go to the game's bitbucket source code ( https://bitbucket.org/vakindu/caterpillarzombie/src/master/ ) and create new pull requests for the project. (For simplicity, try to update the README documentation and create a pull request). Then visit the game's site again ( https://caterpillarzombie.5starsafari.co.uk/ ). You should see the caterpillar zombies increase in length as the number of pull requests increase. LIVE DEMO: https://caterpillarzombie.5starsafari.co.uk/ API USED (BITBUCKET CLOUD REST API): https://api.bitbucket.org/2.0/repositories/vakindu/caterpillarzombie/pullrequests BITBUCKET REPOSITORY USED: https://bitbucket.org/vakindu/caterpillarzombie/src/master/ LICENSE: https://github.com/VakinduPhilliam/CaterpillarZombie/blob/main/LICENSE Challenges we ran into The bitbucket project API is quite difficult to learn for beginners. So is bitbucket and Forge Authentication. Accomplishments that we're proud of The game loads really fast using bitbucket's API Call. We are also proud of the game's beautiful user interface. The game's User Interface is easy to learn (Anyone can play the game after 5 seconds of reading the instructions). What we learned We gained a lot of experience working with Jira, bitbucket, and Forge. Jira is a great platform for building large world-class software projects. What's next for Caterpillar Zombie Working on new versions for iOS and Android. Also working on in app purchases. <div