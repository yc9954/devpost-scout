---
slug: "forged-in-code"
url: "https://devpost.com/software/forged-in-code"
title: "Forged In Code"
hackathon: "Devs Unleashed"
organization: "Atlassian"
winner: true
words: 1144
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Forged In Code

> There's a mystical sword which makes you a 10x developer, Only thing which stands in between are the Jira issues.

[Devpost](https://devpost.com/software/forged-in-code) · hackathon [[Devs Unleashed]]

## Facets

**domain** [[developer_tools]] [[labor_employment]] [[mental_health]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** agile, atlassian, cloud, emoji, forge, game, javascript, jira, maze, rotjs

## How they structured the write-up

- demo
- game play
- features
- installation
- requirements
- accessing the game
- controls
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for forged in code

## Body

Do you have what it takes to get the 10x developer sword? Items are based on actual Jira issues Congratulations, You're about to be a 10x developer! You're about to have a burnout! You're not going to meet the project deadline! Leaderboard Forged In Code There's a mystical sword which makes you a 10x developer, Only thing which stands in between are the Jira issues. Demo Clicking the above image would load the demo video on YouTube. Game Play You're a ninja(🥷) sneaking in to obtain the mystical sword(🗡️) which would make you a 10x developer, But Jira issues(🐞) stand between you and your sword. Navigate the maze to reach the sword without depleting the health to zero(burnout) or running out of time(project deadline: 15 seconds). Keep yourself hydrated(💧) to gain health points. Congratulations, You're about to be a 10x developer! You're not going to meet the project deadline! You're about to have a burnout! Features A perfect maze generated using Eller's algorithm . Game items are based on real Jira issues, 13 Jira issue types supported. Game difficulty is based on the number of issues in the projects, For productivity and fun. Leaderboard to compete with the team mates. Cool synthwave music. Monday? Thank the hydro homies! Nail-biter! Installation If you're already a member of Jira Software Cloud, Use the installation URL to install Forged In Code. If you don't already have a Jira site, Then create it for free at Jira Software Cloud before installing Forged In Code. Requirements Projects with open issues. If you created a new Jira Software Cloud account to play Forged In Code, You probably have a project created for you during setup; Create couple of issues before accessing the game. Accessing the Game Find Forged In Code in the Apps menu after installation. Allow access to read-only data from your project(Issues) and profile(Name, Profile Picture). Note: Leaderboard shows your profile picture only if you had set a custom profile picture for your Jira account. Controls Click the game screen. Use arrow keys to move your character. Use (M)/(S) keys to toggle music and sound respectively. Inspiration One can get carried away with their agile practice at work, So I wanted to make work fun again. What it does Forged In Code is a game which makes use of Jira issues in the game mechanics to increase fun and productivity at work. How I built it Choosing the engine After trying out few different engines, I chose Rot.js due to its minimalist nature while providing the necessary feature set for building a rogue-like game. Learning ROT.js I learnt the basics of ROT.js using the tutorial from logrocket and ROT.js interactive manual . Building the Game Play I decided that the game needs to have single stage as the difficulty of the game is directly linked to the actual Jira projects of the team. The game can be very easy or very difficult to complete based on the actual project status of the team. The game might be easy to finish in the beginning, But as new issues open up in the Jira software it gets progressively difficult. If the game turns out to be difficult to finish, Then just doing the regular agile work as a team to resolve issues can lessen the difficulty in the game by removing the hurdles. Choosing the Map I used the tutorial from logrocket as the starting point for building the game but the cellular automata generation used in the tutorial wasn't the correct choice of map for the placement of the Jira issue items and the bug within cellular generation lead to the creation of unplayable maps with closed walls. So after experimenting with other map generators of ROT.js I found Eller's maze as the perfect map generator for Forged In code as its perfect maze was suitable for placing the Jira issue items, health potions at random positions and placing the player, sword in the fixed positions; Yet generating new mazes each time to keep us engaged with the game. Choosing the enemies Actual Jira issues are the enemies in Forged In Code as it can reflect real-life project development atmosphere. I added support for 13 different issue types which are commonly used in Jira projects. Choosing the duration After experimenting with different duration, I arrived at 15 seconds timeout(project deadline) for the game as I found it to be optimal limit for solving the maze while under pressure. Choosing the health potions I decided water(hydration) as the health potion for the game as its grounded(no pun intended) in reality, Two random health potion placements and +25HP was decided after experimentation. Choosing the UI I decided to use unicode emojis as assets for Forged In code as original Rogue-like games were ASCII based and Choosing emojis as game assets bought me time to focus on Forge and Atlassian REST API integration within the game. Devs Unleashed This game was built as part of Atlassian Devs Unleashed Hackathon using Atlassian Forge platform and Atlassian REST APIs . How Forge and REST APIs were used in Forged In Code Platform Description Forge Serverless FaaS platform to deploy and host the game. GET /rest/api/3/project/search To fetch the projects in the Jira account. GET /rest/api/3/search To fetch the issues associated with the projects in the Jira account for showing them as in-game items. GET /rest/api/3/myself To fetch the profile name and picture of the current player for showing it in the leaderboard. Storage API To set, get and to delete data used for leaderboard. Challenges I ran into Choosing emojis as game assets led to issues with browser compatibility as each browser/OS render emoji differently. To fix this I used Mozilla Twemoji font for the emojis and created similar UI/UX for the game across all browsers. I faced some hurdles in trying to access the issues from the Jira projects, A quick question in the Atlassian's developer community got me the required help immediately. Accomplishments that I'm proud of I was able to build a fun and engaging game which makes work fun again while increasing developer productivity within the stipulated time for the hackathon. What I learned I learnt about Forge serverless FaaS platform and how it helps us build solutions to address problems in agile using Atlassian products. I learnt about REST APIs of Atlassian to access data from different Atlassian products. I learnt ROT.js to build Rogue-like games. What's next for Forged In Code Integrating more Atlassian products into Forged In Code when support for site-less products lands in Forge . Upgrading the timer in Forged In Code to perhaps one using workers for better accuracy. A separate time based leaderboard to rank those who finish Forged In Code in least time. Adding more game play elements based on user feedback. Submitting Forged In Code to the Atlassian Marketplace . <div