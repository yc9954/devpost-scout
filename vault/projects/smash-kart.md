---
slug: "smash-kart"
url: "https://devpost.com/software/smash-kart"
title: "Smash-Kart!"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 754
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/video_visual"
---

# Smash-Kart!

> Rev up for high-speed thrills in this action-packed kart racer — race across wild tracks, unleash powerful power-ups, and unlock awesome new karts!

[Devpost](https://devpost.com/software/smash-kart) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

**user** [[educator_student]] [[legal_professional]]
**substrate** [[video_visual]]

**stack** blender, horizon, photoshop, vscode

## How they structured the write-up

- welcome to smash-kart!
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for smash kart!

## Body

Soaring to temple island at 'Ancient Airways' Skidding over the ice lake at 'Chilly Village' Hitting the beach at 'Speedy Shores' Welcome to Smash-Kart! To start a game, join a lobby and wait for the track to load. Then, when the 'Enter Race' button turns red, click it to teleport to the track. Once your kart loads in, look for the seat icon on your screen and tap it to enter the kart. You'll see instructions on how to steer on screen. During the race, collect items from the '?' boxes and tap the icon on screen to use them. To test multiplayer, gather up to 6 players in the lobby first and then hit 'Enter Race' Inspiration I was inspired to create something unique, that I hadn't seen before on the Horizon Worlds platform. I wanted to push myself to create something that I hadn't tried before in order to improve my understanding of different game genres. And of course, classic kart racers like Crash Team Racing for PS1 and Mario Kart 64 were a big influence on the design. What it does It's a full arcade kart racing game within Horizon Worlds. Your Avatar can take a seat in one of 6 different karts, "travel" to one of the 3 themed tracks and race against other players in multiplayer, or solo against AI bots. Player's can also hang out in the lobby room between races, take photos and check their spot on the leaderboard. How I built it I took advantage of many of the Horizon Desktop Editor's tools and features, and tried to optimise the gameplay for mobile players. I used focus mode to allow for a custom camera that follows the kart and adjusts its FOV depending on the players speed. The tracks are loaded in dynamically using sublevels, and code/events are shared between them and the main lobby level using assets. The player can unlock karts by placing first in the various tracks, and that information is kept in persistent variable groups so their progress is maintained between sessions. While I created the main geometry of the tracks in Blender, I used the asset library as well as the Gen AI mesh generation to add additional decorations to achieve the look I was going for. Both the lobby screen and the player's in-game HUD are created using the custom UI tools and images created in Photoshop. Challenges I ran into One issue I ran into early on is that there is no way to force a player to take a seat, nor to detect if a player has taken a seat. This lead to me having to start the player in an invisible "cage" and ask them to seat in the kart at the start of each race. It's not ideal, but it works. It was important to me that the player's actual avatar was able to sit in and drive the kart. I could have simplified the game by instead putting a generic "racer" model in the kart seat and left the player's avatar off screen somewhere, but I felt that wasn't inline with the social aspect of Horizon Worlds. Accomplishments that I'm proud of I'm very proud of what I managed to achieve with this game, and there are many aspects of it which took considerable work to accomplish. Overall, some highlights for me include creating the AI bot karts, the physics of the karts themselves and my favourite level, 'Ancient Airways'. What I learned I'd never used Horizons as a creator before starting this project a couple of months ago. However the resources, tutorials and Live talks helped me get up and running far quicker than I was expecting. I'd definitely handle the project differently if I started working on it today, but I'm happy with how it's put together on the whole for now. What's next for Smash Kart! I have some exciting plans for the future, which include new tracks to race on, new karts to unlock and potentially a "battle" mode similar to Mario Kart 64! I'd also like to improve the multiplayer UX so that it works a bit more traditionally. I'd like to take this opportunity to thank the Meta SMEs who tested my game and provided insightful feedback during the Feedback Festival. I would also like to thank the judges for taking the time to consider my submission, I had a lot of fun making this game and I hope that you find it just as fun to play. <div