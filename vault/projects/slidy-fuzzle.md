---
slug: "slidy-fuzzle"
url: "https://devpost.com/software/slidy-fuzzle"
title: "Slide Puzzle (fethi)"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 775
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Slide Puzzle (fethi)

> A Mobile/Web/Desktop Slide Puzzle app made with flutter

[Devpost](https://devpost.com/software/slidy-fuzzle) · hackathon [[Flutter Puzzle Hack]]

## Facets

**substrate** [[video_visual]]

**stack** dart, firebase, flutter, rive

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for slide puzzle (fethi)

## Body

mobile casual size 3 puzzle solved pop up mobile advanced size 4 web casual size 3 web casual size 5 Inspiration i was mainly inspired by the provided slide puzzle for the challenge, obviously, I downloaded and tried all slide puzzles available and tried my best to make the best merge out of them with of course my own special touch, also the streams you guys made was awesome and helpful for brainstorming What it does first, it has 2 game modes, Casual and advanced, Casual the player is offered to play a beautifully animated slide puzzle of both numbers and alphabets (can be toggled) I also provide the option to change the board size to 3 (9 tiles), 4 (16 tiles), 5 (25 tiles), where the size 5 is only available on the web platform only beside game configuration, the user is prompted a warning dialog whenever he/she is about to discard the game, also when the game ends a dialog appears showing the leaderboard of the other players and their scores, also there is a help dialog to give an idea about some parts of the app, the user is given 5 switches at each game, the switch is basically swapping 2 different tiles noting that the puzzle will always be solvable but this would help the player, even more, taking that seriously I made an auto solve option which letterly solves the puzzle for the player, at the mean time it needs some enhancments but for most of the puzzles it does the job pretty well, for the second mode which is advanced, all the previous options available since this mode is just like the casual but with images instead of text which is quite difficult to be honest but so fun to solve How i built it I used flutter of course, also made the animations using the RIVE platform, I have started using rive long time ago (2 years) so I was goona include animation or 2 from it eventually, for state management I used provider I add very few portions of code from the provided repo I'm not gonna lie but most of the code is from scratch, I also letterly add firebase with all its integration 6 hours before the deadline. Challenges i ran into the first challenge was not knowing the exact subject of the competition I wasted 50% of the time developing a PegSolitaire puzzle I got up to 80% then after carefully reading through the discussions and the FAQ i noticed that I'm off-topic completely and i had to start again well i wouldn't count as a start from zero cause i learned a lot of it, the second one is having the tiles to slide it was so appealing playing with that animation over and over again another hard thing was importing an image and dividing it into tiles, it was a nightmare really the first tries were nice but the image splitting process was happening each time a tile moves and that was so laggy and resource-consuming i solved after a while, the last and most difficult part yet so fun, i really wish i had more time to work on, it is the auto solve puzzle, it is related to math which i know so well it was a real challenge, thought about a lot of solutions and ways then i settled for the A* algorithm to find the shortest path to the solution, the issue is that it after the first 10 iteration it takes a lot of time to figure out the path so i limited the iterations to only 20 moves. Accomplishments that I'm proud of I'm really proud of solving and overtaking the obstacles and challenges mentioned above it gives such a thrill that pushes me and my capabilities to the limits really. What I learned throughout the project and the competition as a whole, learned one of the most valuable lessons, which reading carefully and actually understanding what I'm reading through, a single wrong idea can really cost a lot, for the technical part I learned how to polish animations, make a cross-platform app, deploy to firebase, clone objects in dart and many more What's next for Slide Puzzle (fethi) well the submission was not as perfect as it is intended to be due to the exams period first and starting the wrong ways for about 50% of the time, anyways I'm definitely gonna keep this game going and actually make it into production I'm really interested in the auto solve option so because of that i will strive to make it as perfect as possible <div