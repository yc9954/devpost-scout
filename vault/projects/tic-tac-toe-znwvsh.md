---
slug: "tic-tac-toe-znwvsh"
url: "https://devpost.com/software/tic-tac-toe-znwvsh"
title: "Tic-Tac-Toe"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 881
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Tic-Tac-Toe

> Tacos Before Vatos ......!

[Devpost](https://devpost.com/software/tic-tac-toe-znwvsh) · hackathon [[Funathon]]

## Facets


**stack** eclipse, java

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learnt
- what's next for tic-tac-toe

## Body

code-1 code-2 code-3 code-4 code-5 output-1 output-2 Inspiration Since we are spending most of our time outdoors now I thought of making one set of Tic Tac Toe for outside play. It came out lovely and Sofia has a new favorite toy she can carry around. What it does Tic Tac Toe Set is a great toy itself but it's all about presentation too. Especially if you want to give this as a gift. I made a tag (picture below) and I attached it to the "fabric board". I simply tied one corner of fabric with rope and I attached this tag to the other end. How we built it Using java language, we created a code.. package aoops; import java.util.*; public class project { static String[] board; static String turn; // CheckWinner method will // decide the combination // of three box given below. static String checkWinner() { for (int a = 0; a < 8; a++) { String line = null; switch (a) { case 0: line = board[0] + board[1] + board[2]; break; case 1: line = board[3] + board[4] + board[5]; break; case 2: line = board[6] + board[7] + board[8]; break; case 3: line = board[0] + board[3] + board[6]; break; case 4: line = board[1] + board[4] + board[7]; break; case 5: line = board[2] + board[5] + board[8]; break; case 6: line = board[0] + board[4] + board[8]; break; case 7: line = board[2] + board[4] + board[6]; break; } //For X winner if (line.equals("XXX")) { return "X"; } // For O winner else if (line.equals("OOO")) { return "O"; } } for (int a = 0; a < 9; a++) { if (Arrays.asList(board).contains( String.valueOf(a + 1))) { break; } else if (a == 8) { return "draw"; } } // To enter the X Or O at the exact place on board. System.out.println( turn + "'s turn; enter a slot number to place " + turn + " in:"); return null; } // To print out the board. /* |---|---|---| | 1 | 2 | 3 | |-----------| | 4 | 5 | 6 | |-----------| | 7 | 8 | 9 | |---|---|---|*/ static void printBoard() { System.out.println("|---|---|---|"); System.out.println("| " + board[0] + " | " + board[1] + " | " + board[2] + " |"); System.out.println("|-----------|"); System.out.println("| " + board[3] + " | " + board[4] + " | " + board[5] + " |"); System.out.println("|-----------|"); System.out.println("| " + board[6] + " | " + board[7] + " | " + board[8] + " |"); System.out.println("|---|---|---|"); } public static void main(String[] args) { Scanner in = new Scanner(System.in); board = new String[9]; turn = "X"; String winner = null; for (int a = 0; a < 9; a++) { board[a] = String.valueOf(a + 1); } System.out.println("Welcome to 3x3 Tic Tac Toe."); printBoard(); System.out.println( "X will play first. Enter a slot number to place X in:"); while (winner == null) { int numInput; // Exception handling. // numInput will take input from user like from 1 to 9. // If it is not in range from 1 to 9. // then it will show you an error "Invalid input." try { numInput = in.nextInt(); if (!(numInput > 0 && numInput <= 9)) { System.out.println( "Invalid input; re-enter slot number:"); continue; } } catch (InputMismatchException e) { System.out.println( "Invalid input; re-enter slot number:"); continue; } // This game has two player x and O. // Here is the logic to decide the turn. if (board[numInput - 1].equals( String.valueOf(numInput))) { board[numInput - 1] = turn; if (turn.equals("X")) { turn = "O"; } else { turn = "X"; } printBoard(); winner = checkWinner(); } else { System.out.println( "Slot already taken; re-enter slot number:"); } } // If no one win or lose from both player x and O. // then here is the logic to print "draw". if (winner.equalsIgnoreCase("draw")) { System.out.println( "It's a draw! Thanks for playing."); } // For winner -to display Congratulations! message. else { System.out.println( "Congratulations! " + winner + "'s have won! Thanks for playing."); } } } Challenges we ran into What is the challenge of Tic Tac Toe? The #tictactoe challenge has gained quite the popularity on the video-sharing app. The videos work this way. A checkerboard is drawn on a sheet of paper and the boxes are filled with treats. And then the participants are introduced - they are none other than pets. Accomplishments that we're proud of Certainly I am proud of designing a game, but I still wait for the first real professional achievement of my life. Applying for a job in your gaming, I hope to get a chance to work on some big campaigns, to have some impact in my work, and maybe to achieve a positive change in the world. What we learnt designing an gaming application using java What's next for Tic-Tac-Toe Tic Tac Toe—it's so simple, yet endlessly entertaining. But did you know that there's a mathematically proven strategy to follow that can help you win, or at least draw, every time you play? That's right; you never have to lose a game of Tic Tac Toe again, and we'll teach you exactly how. Keep reading to learn how to always win at Tic Tac Toe using a foolproof strategy. <div