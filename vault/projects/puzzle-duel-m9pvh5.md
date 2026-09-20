---
slug: "puzzle-duel-m9pvh5"
url: "https://devpost.com/software/puzzle-duel-m9pvh5"
title: "Puzzle Duel"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 1053
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Puzzle Duel

> Online Multi-Platform Classic Puzzle Match. Now with Strategy 😈

[Devpost](https://devpost.com/software/puzzle-duel-m9pvh5) · hackathon [[Flutter Puzzle Hack]]

## Facets

**domain** [[transportation]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** android, dart, firebase, firestore, flutter, ios, kiwi, rxdart, sharedpreferences, vscode, web

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for puzzle duel

## Body

Inspiration I always love to play online games and competing with other players. Wether it's an MMO games, or Board Games. So, I think that its interesting to play this classic puzzle game with other player, 1-1 match game. Not only to solve the puzzle with selected level (which may take the players time a lot in insane mode, obviously), but I added some features to make this multi-player games more fun. What it does Puzzle Duel is basically one-versus-one online puzzle game. The objective of each game is solving the puzzle as fast as you can before your opponent solve the puzzle. But, in the middle of the game, you may use certain actions that may affect to your own puzzle board, or attacking your opponent's board. The actions you may use in-game: Shuffle. It's basically re-shuffle your puzzle board, if you lucky you may get a piece of tile that already in-place. This action will be resetted for each game, where you'll always get 3 chance to shuffle your board. Fix Board When you got a tiles where the position is reversed, you may want to use this action. Basically, this action will positioned your tile (one tile for each action) to the right position. Use it wisely, because you may run out this action. Swap Opponent's Board It's basically the opposite of the Fix Board . This action will swap the correct position of one tile in your opponent's board to the incorrect one. This action will also be reduced everytime you use. Shuffle Opponent's Board Almost get lost? You may want to use this action where you basically "Restart" the opponent's board. Yes, all the tiles in your opponent's board will get shuffled. 😈 The Fix Board , Swap Opponent's Board , and Shuffle Opponent's Board quantity will be reduced eveytime you use them. But, if you win the game, you may get a chance to win one of these action. For the Swap Opponent's Board and the Shuffle Opponent's Board , once you use those actions, the opponent's will unable to undo their move. So, basically it's also refresh their movement history. How we built it I love flexibility, so I decided to use MVVM architecture, and RxDart to manage the state in the ViewModel. I added some extensions to manage the Subject's disposal, so it won't get leak. I also use the Firestore. We already know that it simplify the "realtime" applications. For the dependency injection, I use Kiwi. When user start to find match with the selected level, the application will check if there's any other player is waiting for the match? If no, the application will create new record in the collections to tell that someone is looking for match. If yes, the application will mark that this user is the opponent and also mark the state of the game to waiting for the presentation for each player. When user enter the match game, the application will mark that each player enter the match, and match will begin. When the game started, the application will stream the data from the document to check certain things like: the opponent's move, the game status (if the other players abandoned, won, lose, etc), and also the Action taken by each players. Everytime user move the tiles, i debounce it in n milliseconds before write it into the document. This way, we can reduce the cost of writing and reduce the possibility of race condition. When user use an action, it will immediately recorded into the document, so the other application (in other player) can react to the action in realtime. When the player complete the game (either using action or normally completing the game), the winner will get a chance to win a random action. All the actions have their own probability, and the Shuffle Opponent's Board have the least probability. Challenges we ran into Detect when the user exit/close the website Because I got no solution (up until now) to check if user is leaving the app in their browser, I decided to not letting all the players in the website to create the game. They can only join the match which created by other players who's playing in either iOS or Android. Connection Problem Since it is a realtime game, we expect there will be a bunch of network traffic in the game. So, when user have some issues with their connection, the other player won't get the updated data from the player. The first idea to solve this problem is by checking the internet connection simultaneously and when the connection is in trouble, we can show an indicator that the connection is unstable. UI and UX Because i have a limited skill set in the designing the application (especially for games, which i have never done before) i think there's a room for improvement for the UX/UI. Especially in the UX for the in-game Actions. Inconsistency of Data At first I ran a problem where the movement data from each players is not sync. And there's some errors in the log saying that the async function is timeout. Turns out that always writing to the documents without awaiting every time players move the tiles cause this problem. So, I solve the problem by debouncing the players movement before writing it to the document. Accomplishments that we're proud of Completing the application for multi-platform in less than a month. It's prove that Flutter increase the development speed, a lot. I also proud enough when solving the Inconsistency of Data which already explained above. I also happy that i can finish this application while there's another job is waiting to be release at the same time of this competition end. What we learned Do not simultaneously write the data to the document without awaiting it The font size for Web and App slightly different. Need help from auto_size_text to keep it beauty. The performance of Flutter Web is good enough, but will be great if there's a code splitting to reduce the bundle size. What's next for Puzzle Duel Showing the ranking of the players Showing the win-rate of the players in their profile Tweak or add the actions, so the game will become more fun Revamp the UI and UX with the help of pros <div