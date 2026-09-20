---
slug: "crazy-conversation"
url: "https://devpost.com/software/crazy-conversation"
title: "Crazy Conversation"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 950
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "substrate/document_pdf"
---

# Crazy Conversation

> Alexa will blabber on with a clue that sounds like nonsense and you need to figure out what she's trying to say!

[Devpost](https://devpost.com/software/crazy-conversation) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**domain** [[education]]
**substrate** [[document_pdf]]

**stack** alexa-presentation-language, alexa-skills-kit, dynamodb

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for crazy conversation

## Body

1. Large Hub Homepage 2. Large Hub Clue 3. Large Hub Correct Answer 4. Large Hub Incorrect Answer 5. Large Hub Final Score 6. Small Hub Homepage 7. Small Hub Clue 8. Small Hub Correct Answer 9. Small Hub Incorrect Answer 10. Small Hub Final Score Inspiration This was a game I wanted to make for a previous game competition but I was still in school for the semester. When I saw this competition I thought of all the ways I could incorporate APL to my idea to make a great skill and being on winter break I had a lot more time to get it done. As I started to make my APL documents I learned more and more things I could do with APL and thought of more features I could add to my displays. What it does Crazy Conversation is a game where Alexa will say random words that sound like absolute nonsense but as you repeat the clue you may soon discover that there is a common word or phrase hidden within it. Each game consists of 10 questions. After each of your answers Alexa will tell you (and show you if applicable) if your answer was correct or incorrect. There are hundreds of clues so each game will always be different. At the end of the game Alexa will give you your final score. How I built it I have created Alexa Skills in the past but they have always been rather simple and written in v1 of the Alexa Skills Kit. For an idea as complex as this I knew I would need to learn v2 to make the skill. I have a data file that holds all the clues as well as a lot of the speech responses. When giving your answer, the skill will trigger the intent that compares your answer to the correct answer. Alexa will respond appropriately and then give you the next question. This cycle repeats until the game is over and Alexa gives you your final score. If you run out of time for a question Alexa will ask if you are ready for the next one and if you say yes then she will proceed. The skill is also linked with a DynamoDB table which will save the clue the user is on so they can progress through the entire clue set without any questions repeating. Challenges I ran into My biggest challenges were APL related. It was something I had never used before so I had to learn it from scratch. Part of my skill consists of one APL page that shows if the answer was right or wrong and then the next page shows the next question. I wanted to show this all in one intent when the user provides an answer. My vision was for Alexa to congratulate you on a correct answer, page over to the next question, and then read the next question. For this I needed to use the APL commands so that the speech for each part was synchronized with how the display paged to the next question. I set this up by using a SpeakItem - AutoPage - SpeakItem combination of commands. On top of that I wanted to add a visual timer to the skill so you could keep track of how long you have left to answer the question. I was originally going to use a video but for that I needed to add play and pause directives which would defeat the purpose of a timer. Instead I added a pager that would look like a timer and autopage every second to count down from one minute. This was probably my biggest challenge and I almost scrapped the timer completely because I didn't know if I would be able to do it. Accomplishments that I'm proud of My proudest accomplishment while making this skill is the set up of my APL document that includes a response based on your given answer, the next question (both with the accompanying display), and the timer that counts down the minute you have to answer. I had to setup and elaborate combination of APL commands using Sequential, SpeakItem, AutoPage and Parallel commands. It was difficult to set up and took me a few weeks of trial and error but with the help of some examples I found and Amazon's office hours I was able to make it happen. I am also very proud of making my first really complex skill that combines DynamoDB data persistence, displays that have touch elements and moving parts like pagers and building a game skill that I think is a lot of fun to play. What I learned The amount that I learned when making this skill is more than I can even list here. I started making my displays with APL and realized that I had only scratched the surface of what you can do with them when I discovered how to use a lot of the APL commands you can add in. I had to really think about the dialogue model I was putting together so that I could have a user seamlessly progress through a game with Alexa. In addition I had to learn how to use DynamoDB with Alexa so that I could save the question a user leaves off at, that way they can go through all the clues and have unique ones in each game. What's next for Crazy Conversation Next up for Crazy Conversation will be Echo Buttons support so that a group of friends can play against each other or in teams and use the buttons to buzz in to answer what they think the clue means. <div