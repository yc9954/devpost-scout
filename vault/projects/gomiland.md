---
slug: "gomiland"
url: "https://devpost.com/software/gomiland"
title: "Gomiland"
hackathon: "Global Gamers Challenge"
organization: "Google"
winner: true
words: 765
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Gomiland

> Gomiland is a pixel art RPG. Explore the town to learn about sustainable cities and recycling. Pick up rubbish off the streets, then head home to sort them to receive coins!

[Devpost](https://devpost.com/software/gomiland) · hackathon [[Global Gamers Challenge]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
  <sub>weak: general_public</sub>
**substrate** [[geospatial]] [[video_visual]]

**stack** dart, firebase, flame, flutter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gomiland

## Body

Main menu GIF Pick up rubbish from the streets Visit the bamboo forest shrine! Sort your rubbish! Speak to characters in the game Grow your zen garden GIF Learn about sustainability from citizens GIF Add friends and find them in the game Inspiration Having lived in Japan for 2 and a half years, sorting rubbish has become a habit in daily life. However it was quite a challenge for foreigners when we first arrived. We referred to a handbook of recycling materials written in Japanese to know the days and types of rubbish collected and how to dispose of it. Gomiland is a Japanese-themed RPG where players pick up and sort trash. It is directly influenced by the waste disposal endeavours we had to do while living there. Personally, I grew up playing 2d pixel art games like Pokemon , Stardew Valley and The Binding of Issac . Thus, I wanted to create one myself. NPCs in this game take after people that I know and locations on the map take after places that I have visited. What it does Gomiland is a 2D top down RPG where players explore the town of Gomiland and clean up the streets! Learn about sustainable cities by exploring the town, talking to characters and reading the signs. Many will give fun facts on sustainability and how we can contribute to it! Pick up thrash you see on the ground while exploring Gomiland. Sort rubbish at home into plastics, paper, metals, electronics, glass and food. Earn coins for sorting them correctly and loose coins for getting them wrong. Complete quests and see some changes to the city. Complete them all for a special statue award! Some other features include saving the game and loading it on a different device, adding friends and receiving bonuses from them in-game and redeeming a code to upgrade your zen garden! How we built it The game uses the Flutter framework with the Flame package as the main game engine. It is playable on web, Android and iOS . The main IDE used was Android Studio. Sprite assets were primarily designed in GIMP and the tile map with Tiled. A series of Medium articles were written about the development. Challenges we ran into This was the first time using the Flame engine and there were plenty of minor setbacks due to the limits of the system. Besides that, there were 2 challenges. FPS Because the 2 world areas (neighbourhood and park) have a large tilemap and animated tiles, The frames per second, FPS, took a big hit. This was remedied by using a package to merge all tile layers and animated tiles into a single image. Additionally, there are also over 300 objects in each area, some being animated sprites. There was a need to reduce the number of objects to improve the FPS Creating sprites I had some old unused sprites from an earlier project. However, many sprites still had to be made and many had to be scaled and changed to fit the theme of the game. This took up much time during the 8 weeks. Accomplishments that we're proud of Gomiland is a fully functioning bona fide RPG with over 2hrs of gameplay, animated sprites, quests, a mini sorting game and tons of unique features. I am very satisfied that I was able to create a working game in the short time given. My articles about the Jenny API were also featured in Flame's discord by one of their team. I hope the tutorials I have made will benefit other game developers. What we learned In the Medium articles written about the development, there are links to several tutorials about how to code features for an RPG. These include raycasting, dialogues with Jenny API and tilemap rendering. All these stem from lessons learnt during development of the Gomiland with the Flame engine. Other things I learnt were also about how to build and show a sustainable city. First I, myself, had to read about sustainability and incoprorate it into the game. After that, I had to imagine a city where sustainability had been partially achieved and try to present it to the players. I found that the most effective way for players to get engaged in sustainability took both visual and written aspects of the game. What's next for Gomiland There are plans to include more rubbish types, more quests, more areas of the map depending on user feedback. There is also a possibility of creating more real world interactions like adding in game purchases and expanding the 'friends' feature. <div