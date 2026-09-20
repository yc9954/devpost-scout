---
slug: "contestgame"
url: "https://devpost.com/software/contestgame"
title: "IssuesHunter"
hackathon: "Devs Unleashed"
organization: "Atlassian"
winner: true
words: 574
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# IssuesHunter

> game, arcade, shooter, 2d, waves

[Devpost](https://devpost.com/software/contestgame) · hackathon [[Devs Unleashed]]

## Facets

**substrate** [[geospatial]]

**stack** javascript, jira, phaser.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for issueshunter
- google slides presentation: link
- assets resources

## Body

Setting wall Bonus Box Grenade explosion Waves Game over Playing Menu Inspiration My inspiration comes from retro arcade games like for example Contra link or Chicken Invaders link . I wanted to make simple game that would let your mind rest and allow you to compete with collegues at the same time. It was also important that the game should motivate us to work. Then i got an idea to create perks system that depends on our work. I thought that the best genre will be waves arcade game. What it does My game are getting account data and issues for playing user. account data is getting with /rest/api/2/myself From account data my game is using only displayName to display it on game over screen. issues are getting with /rest/api/2/search?jql=assignee=currentuser()&fields=status,statuscategorychangedate Fields search params are added to avoid from getting unnecessary data. From issues are counted those that was assigned to playing user and was finished in last 30 days. For each done issue player gets extra points that could be spent on perks that will strengthen our hero. The goal of the game is simple, we need to survive as many waves as posible with the help of grenades, covers, weapon and perks of course. How we built it I built the game based on starter app with Phaser.js and Atlassian Gorge library. At the beginning i considered using Three.js but i came to the conclusion that using Phaser.js will be easier. I created two scenes and several objects on which the entire game is based. Challenges we ran into The biggest challenge was to make object works in Phaser.js environment. I had some troubles with timeouts, then i got an idea to set variable when some event should start and in update function compare with time.now if it is a good moment. Working with geometry is also very challenging for example when you need to think how to set objects in proper place or how to calculate vector of bullet direction. But i must admit that i love solving math problems, so creating this game was a great time. Accomplishments that we're proud of I am most proud of perks system that makes every play different, of course if we choose different perks. I am also proud of increasing difficulty level during successive waves, around 15 level the game is getting very hard in my opinion. However good combination of perks allows you to survive even in later waves. But apart from the perks, you also need skill. What we learned I learned to work with Atlassian Forge API and Phaser.js . I have to admit that i have never heard about Phaser.js before and i regret it. It is very interesting tool and i think i will use it many more times . What's next for IssuesHunter I have some ideas to improve IssuesHunter: 1) Connect with other Atlassian products (Bitbucket, Confluence). 2) Add more weapons for player, from bonusBox or for surviving waves. 3) Add more types of grenades for example: grenade which decreases speed for a moment, grenades with stuns for a moment. 4) Add in-game ranking that will allow users to check and compare their scores. 5) Add bosses for example after each 10 waves. 6) Allow user to move horizontally. 7) Extension of map, enemies coming from all directions. 8) Add more perks. Google Slides Presentation: link Assets resources https://didigameboy.itch.io/jambo-jungle-free-sprites-asset-pack https://opengameart.org/content/elven-land-2d-backgrounds https://opengameart.org/content/building-block-assets-stone-logs-bricks https://opengameart.org/content/ammo https://opengameart.org/content/modified-32x32-treasure-chest https://www.flaticon.com/free-icon/grenade_3836647 https://opengameart.org/content/simple-crosshairs https://opengameart.org/content/explosion-3 <div