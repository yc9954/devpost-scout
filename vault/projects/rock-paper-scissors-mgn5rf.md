---
slug: "rock-paper-scissors-mgn5rf"
url: "https://devpost.com/software/rock-paper-scissors-mgn5rf"
title: "Rock,Paper,Scissors...!"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 463
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Rock,Paper,Scissors...!

> Game theory in everyday life....

[Devpost](https://devpost.com/software/rock-paper-scissors-mgn5rf) · hackathon [[Funathon]]

## Facets


**stack** jupyternotebok, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learnt
- what's next for rock, paper, scissors....!

## Body

output with code Inspiration What it does If you’re unfamiliar, rock paper scissors is a hand game for two or more players. Participants say “rock, paper, scissors” and then simultaneously form their hands into the shape of a rock (a fist), a piece of paper (palm facing downward), or a pair of scissors (two fingers extended). The rules are straightforward: Rock smashes scissors. Paper covers rock. Scissors cut paper. How we built it using python programming language we built it by using Jupyter notebook Challenges we ran into Take User Input Taking input from a user is pretty straightforward in Python. The goal here is to ask the user what they would like to choose as an action and then assign that choice to a variable: user_action = input("Enter a choice (rock, paper, scissors): ") This will prompt the user to enter a selection and save it to a variable for later use. Now that the user has selected an action, the computer needs to decide what to do. Make the Computer Choose A competitive game of rock paper scissors involves strategy. Rather than trying to develop a model for that, though, you can save yourself some time by having the computer select a random action. Random selections are a great way to have the computer choose a pseudorandom value. You can use random.choice() to have the computer randomly select between the actions: possible_actions = ["rock", "paper", "scissors"] computer_action = random.choice(possible_actions) This allows a random element to be selected from the list. You can also print the choices that the user and the computer made: print(f"\nYou chose {user_action}, computer chose {computer_action}.\n") Printing the user and computer actions can be helpful to the user, and it can also help you debug later on in case something isn’t quite right with the outcome. Determine a Winner Now that both players have made their choice, you just need a way to decide who wins. Using an if … elif … else block, you can compare players’ choices and determine a winner: Accomplishments that we're proud of Certainly I am proud of designing a game, but I still wait for the first real professional achievement of my life. Applying for a job in your gaming, I hope to get a chance to work on some big campaigns, to have some impact in my work, and maybe to achieve a positive change in the world. What we learnt designing a gaming application using python What's next for Rock, Paper, Scissors....! Game programming is a great way to learn how to program. You use many tools that you’ll see in the real world, plus you get to play a game to test your results! An ideal game to start your Python game programming journey is rock paper scissors. <div