---
slug: "overcrowded-trolleybus-game"
url: "https://devpost.com/software/overcrowded-trolleybus-game"
title: "Overcrowded Trolleybus game"
hackathon: "Pygames"
organization: "Microsoft"
winner: true
words: 491
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Overcrowded Trolleybus game

> Remake of my old Overcrowded Trolleybus PC game, originally written in Delphi (corners-like game on chessboard) released specially for Pygames Hackathon 2023

[Devpost](https://devpost.com/software/overcrowded-trolleybus-game) · hackathon [[Pygames]]

## Facets


**stack** pygame, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for overcrowded trolleybus game

## Body

Inspiration Remake of Overcrowded Trolleybus game, originally written in Delphi (corners-like game on chessboard) released specially for Pygames Hackathon 2023 What it does Remake of Overcrowded Trolleybus game, originally written in Delphi (corners-like game on chessboard) released specially for Pygames Hackathon 2023 How we built it I have found some example of checkers implementation on pygame library and repurposed and refactored to implement Overcrowded Trolleybus game Challenges we ran into I didn't have a team and enough time to include some interesting features like: Networking option feature so that two players could play this game over internet or local network. Hard level of AI opponent. I was able to implement some basic AI, however, it is still not smart enough and can be easily beaten. Save game option feature. It would be nice if player could save the game and return to it later. Since in my Delphi implementation I had at least ability to undo/redo a turn. Accomplishments that we're proud of I felt very happy and joyful that I was able to port my old PC Delphi game into pygame platform. I like this being a greenfield project. I was recalling my childhood when I played this game with my grandfather. https://github.com/Patlatus/Pygame-Overcrowded-Trolleybus/issues/1 Actually I was able to port my old AI implementation from Delphi implementation to Python. Also I was able to improve it so that it could now leave the base for 50 turns in 90% of cases When it is given 90+ moves, it can actually finish and win the game. Also I am proud to manage to implement a new AI to be smarter and more sophisticated. In 99% of cases the new AI should be able to leave the base in 50 moves unless you specially play against it and intentially block their pieces. When new AI has 70+ moves, it can actually finish and win the game. https://github.com/Patlatus/Pygame-Overcrowded-Trolleybus/issues/5 Also I was able to use gettext library to implement Ukrainian localization for the game What we learned It was hard to find a hosting platform to host this solution. I was searching and trying to find some simple host platform. I have seen something is suggesting trinklet to be a good platform to host a pygame based game, but when I tried to post it there, it was cropped: https://trinket.io/pygame/8f2fb93796 Next platform I tried was itch.io but it was required a file to upload as downloadable option. Finally I have found a platform replit, which wasn't cropping the game https://replit.com/@JulfyPatlatus/Overcrowded-Trolleybus?v=1 What's next for Overcrowded Trolleybus game Networking option feature so that two players could play this game over internet or local network. https://github.com/Patlatus/Pygame-Overcrowded-Trolleybus/issues/3 Save game option feature. It would be nice if player could save the game and return to it later. https://github.com/Patlatus/Pygame-Overcrowded-Trolleybus/issues/2 Implement hard level of AI. https://github.com/Patlatus/Pygame-Overcrowded-Trolleybus/issues/6 Actually, it would be nice to have some Overcrowded Trolleybus tournament so that many people could join and play to find the ultimate passengers master <div