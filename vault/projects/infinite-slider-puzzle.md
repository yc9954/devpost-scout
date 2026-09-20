---
slug: "infinite-slider-puzzle"
url: "https://devpost.com/software/infinite-slider-puzzle"
title: "!Puzzle"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 741
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# !Puzzle

> Not your typical sliding puzzle. While using the same mechanics, a lot of interesting games can be achieved with enough inspiration and creativity

[Devpost](https://devpost.com/software/infinite-slider-puzzle) · hackathon [[Flutter Puzzle Hack]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[education]]
**substrate** [[geospatial]] [[video_visual]]

**stack** api, flutter, rive

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for !puzzle

## Body

!Puzzle promotional Inspiration I have always liked puzzles and brain teasers. And as a kid, I remember buying many sliding puzzles at school events and having lots of fun. When I saw the challenge I got excited to try imagining all the different games that could be built using the same mechanics. What it does It generates different games using the same mechanics, such as: Basic: The classic numbered puzzle. Images: The image gets broken down into small tiles. Sort them to form the image. Words: Sort the tiles to spell a random word correctly. Tic tac toe: Move the tiles to win a tic tac toe match. Candy: Move the tiles so that the monster can eat the candy and avoid the red traps. Gyro: Use the mouse's coordinates to move the rotation. Sort them correctly until it forms a single image. And many more to come... Additionally, it handles levels and scoring. How we built it First a puzzle model was created using classes such as PuzzleTile and PuzzleTilePosition . A wrapper class was created for generating the puzzle and handling moves and callbacks. For the visual part, a PuzzleTileWidget class was created to render the tiles and handle interactions and animations. For more customization, the Level class serves as a wrapper handling pause and restart controls, as well as specific customizations. Basic: Tiles are generated with a correctPosition and a value attribute (the numbers themselves). After a move, if the correctPosition matches the current position in all tiles, the player wins. Images: Random images are fetched from https://picsum.photos and each tile wraps a clone in a FittedBox with custom positioning. Once again, after a move, if the correctPosition matches the current position in all tiles, the player wins. Words: Random words and definitions are fetched from https://random-words-api.vercel.app/word . Each of the tiles in the game is assigned one of the letters of the word. After a move, if all the tiles spell out the word correctly, the player wins. Tic Tac Toe: A helper function receives a two-dimensional array of O's and X's to determine if there is a win. The function is executed after each move. Candy: A random number of candy and red traps are generated. The empty tile is rendered as a monster. Both the monster and the candy are Rive animated components. Gyro: A component is generated that displays the bottom part yellow and the top part grey. Using a MouseRegion widget for desktop to get the mouse coordinates, and the accelerometer listener from Sensors Plus for mobile devices, the angle of the yellow/grey changes. Like the image level, each tile wraps a clone of the component in a FittedBox with custom positioning. After a move, if the correctPosition matches the current position in all tiles, the player wins. Challenges we ran into Shuffling: At first I thought that the tiles could be generated in random order, but had a lot of trouble solving the puzzle. However, it turns out there is mathematical proof that shows only some of the configurations are possible. Instead, for shuffling I used the existing moving mechanisms to move left, right, up and down randomly for n times. Shuffling for tic tac toe: Because of the size and possible combinations, sometimes the shuffling of a tic tac toe level would already be solved. To prevent this, the shuffling method of the puzzle was modified to continue shuffling while a condition was met (in this case, continue shuffling if tic tac toe has winner). Gyro: On desktop it became difficult to provide an enjoyable user experience when the cursor was moving over the tiles. It caused lots of strange behaviors. To overcome this, I set a minimum distance from origin to update the angle. Accomplishments that we're proud of Each level had its own challenges, however I am most proud of the gyro level because of the alternative user experience it provides, and because it uses each device's ways of interacting (mouse, accelerometer). What we learned I learned a lot about the inner workings and theory behind sliding puzzles. Likewise I also had the chance to dive deeper into Flutter and Dart. What's next for !Puzzle I plan to release this as a mobile phone game in the not so distant future. I also plan on adding a bit more functionality between levels (eg, share score on Twitter). New levels will be added from time to time as well. <div