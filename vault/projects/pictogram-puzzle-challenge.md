---
slug: "pictogram-puzzle-challenge"
url: "https://devpost.com/software/pictogram-puzzle-challenge"
title: "Rebus Puzzles"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 1370
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Rebus Puzzles

> Have fun while solving brain teasers using Alexa. This Alexa skill provide 3 new rebus word puzzles every day.

[Devpost](https://devpost.com/software/pictogram-puzzle-challenge) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets

**domain** [[education]] [[labor_employment]] [[supply_logistics]]
**user** [[general_public]]
**substrate** [[structured_db]] [[video_visual]]

**stack** node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for rebus puzzles

## Body

Splash Page "Akan" in "sky walker" = "Anakin Skywalker" "Genes" in blue font = "Blue Jeans" The final "Jed. I" in the list = "The Last Jedi" Content Management System build in Excel with VBA Example badge Inspiration I've built quite a few Alexa skills over the last two years, but nothing that generated heavy and consistent user engagement (which make sense, as most of my Alexa skills require DIY hardware). I knew I wanted my next Alexa skill to be more user/consumer friendly. I ultimately decided to build a game. I originally planned to build a Geography challenge, where users would race around the globe to find "bad guys" by using hints/clues (facts about a city or country). I completed 80% of the framework before realizing that no child under the age of 13 would want to play my game. It was too complicated and the questions/clues were not things the average elementary school child would know. So, I stopped development for a few weeks and just observed my kids as they played games on our Alexa devices. Here's what I learned: My kids love simple games. A question with a clear answer makes it easy for them to get the question right They like competing, but also like working together. They want to know how they compare to others playing the game. In addition, they like badges or clear indicators of progress They like laughing at silly guesses They like new and fresh content I took that feedback, with a few non-Alexa things that they like (puzzles, challenge games, etc) and came up with the Rebus Puzzles skill. What it does Rebus Puzzles is a game where players are given three rebus* puzzles to solve each day. Players can ask for a hint or for more time as they work to solve the puzzle. Points are awarded for each correct answer. Badges are earned as players hit certain milestones. The skill is best played on a device with a display (Amazon Echo, Amazon Spot, Fire TV, etc). Players will need to see the puzzles in order to solve them. Puzzles will be sent to the Amazon App if a user is not using a device with a display. *Rebus puzzles are word picture puzzles that are solved by looking at the organization and arrangement of words, letters, and numbers. The puzzles typically represent a saying, word place, person, or thing. How I built it Building the skill required five major pieces of work Developing the logic/framework for the skill Developing the puzzles and rewards system Creating a content management system Building a self healing system Making use of the Echo Show Developing the Logic/Framework: I used the Alexa Skills Kits for NodeJS to start building my skills. In addition, I used AWS Lambda and DynamoDB to save session state. I also used S3 to save and serve up image content. Alexa, by default, only gives 8 seconds between asking a question and waiting for a user response. I knew that my users would need more time to solve the puzzles, so I added a 10 sec timer (via an mp3 file) to give the users more time to analyze the puzzle. [Note: This is a bit of a rant, but want to share my thoughts on the ASK CLI: In the past, I've manually uploaded the code to Lambda and added skill logic (intents, etc) via the Alexa dashboard. This time, I used the Alexa Skill Kit Command Line Interface. It saved me hours of non-development time (zipping up code, uploading code, logging into the Alexa Dashboard, navigating to the correct screen to make changes, etc). I highly recommend that anyone looking to advance to more complex skill development start using the CLI.] Developing the puzzles and rewards system Skills with fresh content (e.g. Jeopardy!, Flash Briefings, etc) keep users engaged and coming back, so I knew that continually adding new puzzles would be key to my skill's success. I wanted the puzzles to be new and different, so I did my best to create original puzzles. I also wanted to ensure that a player didn't receive puzzles that were too difficult, so each user gets one easy, one medium, and one "hard" puzzle each day. And easy puzzle might look like this (mouse over to see the answer): While medium or hard puzzles are as so (mouse over to see the answer): I also needed to create categories and hints that would guide the users. Finally, I had to design a points system and award badges based on certain criteria (100 points, 3 puzzles solved in a day, 5 days of concurrent use, etc). Content Management System Typically, I enter data directly into the Lambda code or a DynamoDB table for my skills. I needed to create 180-200 puzzles for my initial entry. I also knew that it was possible that a user could play the skill every day, which means that I need 90 new puzzles each month. Given that, manual updates into DynamoDB wasn't going to be an option. I decided to dust of my VBA books and create a GUI that sits on top of an Excel spreadsheet. The GUI allows me to easy add information needed for the puzzle (the answer, the selected image, synonyms, etc). I have "add on" node.js scripts that: upload the images to S3 update the skill JSON file (specifically, I update the "PuzzleGuess" Intent with possible responses/answers and synonyms) upload the puzzle details into the DynamoDB "Puzzle" table use Amazon Polly to test voice output Building a Self-Healing System I've spent most of my Christmas vacation working on the skill. When I resume work, I know that I'll have limited time to update the skill. Given that, I wanted to automate as much "healing" as possible, so I am in the process of writing a lambda function (to run daily) that looks to see if any puzzles are not being answered correctly. If less than 5% of users answer a puzzle, then it probably means that there is a problem with the puzzle. The function will remove the puzzle from the "available queue" until I can make changes. Likewise, if 90% of users answer a skill correctly, then the puzzle should be moved down a complexity level (e.g. from medium to easy). Making Use of the Echo Show The skill is built for playing on an Echo Show (though it will work with any device through the use of display cards). I wanted to get the most out of the Echo show, so I tried to use the best Display Templates for each interaction. In addition, I allow the users to click on their badge inventory to see what they've earned and what other badges are available. I also wanted to give players the chance to learn about a particular answer (if it was relevant), so I added Alexa hint logic as well ("Ask Alexa to tell me about "The Last Jedi"). Challenges I ran into Outside of what I listed above, here are a few additional challenges: Sometimes I had to do special formatting the words/phrases so that Alexa said them correctly. I originally called this skill "Word Play Puzzles"; unfortunately I couldn't use the word "Play" in the invocation name. I ultimately went with "Rebus Puzzles". It's not a pretty as "Word Play Puzzles", but I'm hoping that does't work against me. Accomplishments that I'm proud of I believe that 80% of my code can be reused for my next quiz/challenge skill... which is great because I already have ideas. Mastering the ASK CLI (as I called out in my rant above). This was HUGE! Designing the skill with my kids. A lot of the functionality was developed based on their direct feedback. Plus I've offered them $1 for each puzzle they create on their own (otherwise, I'll never get around to creating 90 new puzzles a month). What's next for Rebus Puzzles I want to update my quick and dirty CMS to a more sustainable model... I'll probably create a node application; this will cut down on the multiple steps to get the updates into Alexa. I need to finish my "health check" scripts. <div