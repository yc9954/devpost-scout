---
slug: "alien-showdown"
url: "https://devpost.com/software/alien-showdown"
title: "Stuffed Suspects"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 600
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Stuffed Suspects

> Can you blend in with the NPCs? Search for toys without being caught by another player.

[Devpost](https://devpost.com/software/alien-showdown) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

**substrate** [[geospatial]] [[video_visual]]

**stack** blender, gimp, substance-designer, typescript, unreal-engine, visual-studio-code

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stuffed suspects

## Body

Start screen Waling around Finding a toy Wrongly accused an NPC of being a player Inspiration My goal with the mobile competition was to solve the controller difficulty problem by developing a new movement system that involved tapping where you want to move instead of controlling your character with the virtual joysticks. By experimenting, I found that you can't create your own player movement system using your player avatar because their legs don't move if you move the player over time. So instead I tried using the agent NPCs which do animate when you move them. I messed around with the different agent NPC options and created two movement systems, one where you move the NPC to a position by tapping your screen and one where it moves to a random position. My idea came from the realization that it would be hard to tell the difference between a randomly moving NPC and an NPC that is player controlled, and decided to build a game around the mechanic of trying to complete objectives without other players noticing that you are a player. What it does There are 15 stuffed bears in a carnival. When you join a game, you take control of one of the bears. Any bear may be controlled by another. If you suspect a bear is controlled by a player, hit them. If it was a player, they get knocked out. If you are wrong, you get knocked out. Be the first player to collect all 5 toys. If you get knocked out, you lose your toys and you have to collect them again. How we built it I used a combination of local camera API, navmesh API, focused interaction, and custom UIs to create the movement system for the bears. The map was an asset I purchased through CG Trader and imported. Challenges we ran into It is difficult to find the balance between making the bears easy to control and making it too easy to find the toys without being spotted. When it is difficult to control the bear, it is easier to spot a player because they make more movement adjustments than the NPCs do. I initially added two levels of zoom, one close up and one of the full map. The full map view allows you to see where the possible toy locations are. You could move by clicking on the map in full map view. This made it too easy because you could simply click where you wanted to go and get there without any way of other people knowing you're real. I added another zoom level that is twice as far as the first zoom level and made it so you can't move by tapping on the map with the full map view. This made it so you can move around easier by zooming out once and still see where the toys are by zooming out twice, and it's easiest to attack while zoomed in all the way. This also allows players to zoom out if there is something in front of the camera when it zooms in really close to your bear. This solution worked out best! Accomplishments that we're proud of I am proud of the look of the map and creating a new movement system that I don't believe anyone has done before. What we learned I learned a lot about NPC movement using focused interaction. What's next for Stuffed Suspects The leaderboards won't be ready for the submission deadline, the buttons weren't working when I used player.focusUI() for some reason. I will investigate this more later. <div