---
slug: "chess-master"
url: "https://devpost.com/software/chess-master"
title: "Chess Master"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 1032
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/video_visual"
---

# Chess Master

> Play a game of chess against Alexa or another person (either in the same location or a different location).

[Devpost](https://devpost.com/software/chess-master) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**domain** [[developer_tools]]
**substrate** [[video_visual]]

**stack** alexa-skills-kit, node.js, stockfish, twilio

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for chess master

## Body

High Level Architecture Recommend a move Screen shot of Alexa App Inspiration My wife and I purchased the Stratego board game for the kids last Christmas. After playing a few times, I noticed similarities to chess. Soon after, I started playing chess online. After a few weeks, I decided to look into Alexa-based chess games. I found a few, but felt like that they could be improved on, so I built my own. What it does Chess Master allows a user to play a game of chess in three modes: Mode 1: Play against the computer: In this mode, the user chooses to play against Alexa in easy, medium, or expert skill level. The user will indicate his preferred move, then Alexa will respond. Am image of the board will be sent to the Alexa App. If asked, Alexa will recommend plays and will undo a move. Mode 2: Play against someone in the house: This mode is meant for two players in the same location. This mode works best with a Fire TV (though this can be played with a Alexa device and tablet/phone combo as well). All functions (except undo) are available in this mode. The board "flips" from a black or white perspective based on who's turn it is. Mode 3: Play against a remote user: The remote option is for playing against someone in another location. Game play is similar to Mode 2, except that users require a mobile device for game play. This allows the user to be notified when his opponent plays. How I built it The chess master is built leveraging Amazon Web Services and a number of 3rd party APIs and programs. The following diagram highlights the high level architecture. Alexa Skill (AWS Lambda function written in nodeJS) Game play, move validation, etc is governed by Chess.js . Alexa moves and best move recommendations come from Stockfish . Session variables (including game status) saved in DynamoDB tables. Image Creation I have a small AWS LightSail webserver running to support image creation (in this case, the chess board). The image is created when the "Main" Lambda function calls the web server (via the AWS API Gateway). The image is retrieved, saved to AWS S3, and presented to the user in the Alexa app. The code based on the following WebImage project . Communication to support remote user game play A second AWS Lambda function (exposed through Amazon API Gateway) is used to support received text messages (via Twilio ). Note - The main Alexa skill also sends messages via Twilio in order to notify an opponent that it is his turn to move. Challenges I ran into I've written a number of skills; this has been been, by far, the most complicated one I have built, for a number of reasons. Understanding a user's move - part 1 Users make moves by saying "move piece to target location" (such as, move pawn to E4). Originally, I planned for the user to indicate the source and target moves (move from C1 to D2). The challenge was that Alexa interpreted "to" as 2... so the source coordinate became C "one two". I moved to the "piece and target coordinate" designation for moves; this required a more complex function to determine the move (the chess.JS library required moves to be indicated by source and target). I ultimately had to loop through the entire chessboard square by square to (a) see if the piece matches the requested move piece and (b) see if the move was a valid move. If a and b were, true, then the move was executed. Understanding a user's move - part 2 The second problem with moves is that Alexa does not always hear letters correctly. B is sometimes "B", "Bee", "Bea", "Be". I did a lot of testing and wrote an array that translated the "heard" word to the correct user intention. To help, also recommend to users that they use the NATO phonetic alphabet (move pawn to Echo 4). Running an executable in Lambda (Stockfish) I originally exposed the Stockfish recommendations as an API (on the same server that I use for Image creation), but I found that I would get timeouts based on the complexity of the move. Stockfish is also a CPU intense program and would impact the image creation functions. I decided to remove it from the image creation web server and run it as part of the main Lambda function. Running an executable in Lambda isn't as straightforward as I thought it would be. Ultimately, I got it to work, but it took days instead of hours to get working. Special Moves There are 3 special moves that are supported during a game of chess. Two of these (en passant and castling) were straightforward to handle. Pawn promotion was more difficult, as I had to determine the location of a pawn to determine if it was eligible for promotion. During traditional game play, a user has the ability to promote a pawn to Queen, Knight, Rook, or Bishop. Based on my research, a pawn is promoted to Queen 99% of the time, so I decided to automatically promote eligible pawns to queen (versus prompting the user for a choice). Accomplishments that I'm proud of I'm happy that I could build a skill that supports game play between two users with two different Alexa profiles (with the help of Twilio). I'm also proud that I was able to use the skill with my family as part of our game night. What I learned So much. First off, I starting playing chess again. I learned how to better use the functions in the Alexa SDK. I also learned how to add executables to Lambda functions. What's next for Chess Master There are a few ideas that I'd like to incorporate in the next release: 1) I'd like to build a smart chessboard that can be used to enhance game play. 2) I'd like to give users the option to choose the pawn promotion. 3) I'd like to add a game play timer. 4) I'd like to give users the ability to play more than one game at a time. <div