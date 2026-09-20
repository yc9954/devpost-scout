---
slug: "streets-ahead-learner"
url: "https://devpost.com/software/streets-ahead-learner"
title: "Streets Ahead"
hackathon: "2019 Developer Circles from Facebook Community Challenge"
organization: "Facebook"
winner: true
words: 835
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/transcript_audio"
---

# Streets Ahead

> Language learning games for people who are not streets behind.

[Devpost](https://devpost.com/software/streets-ahead-learner) · hackathon [[2019 Developer Circles from Facebook Community Challenge]]

## Facets

**mechanism** [[provenance_signing]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[transcript_audio]]

**stack** facebook-analytics, facebook-messenger, facebook-messenger-sdk, hacklang, hhvm, proxygen, react, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for language learning api

## Body

Facebook Messenger ties everything together. A variety of designs to spice things up while you match pinyin to their simplified Chinese counterparts Play the quiz game when you cannot give your full attention to learning. Flash cards fit into everything in between. Users should be in control whenever they want, so it's pretty easy for users to delete their own data. Inspiration Have you ever had a New Year's resolution? Perhaps exercise more, get more sleep, or even learn a new skill. Well I had a resolution this year to learn Mandarin Chinese. So I did what everyone does: read Chinese lesson books, play some games, and plenty of trips to Chinese restaurants to get a little bit of practice with the employees. After about 6 months of working at it, I learned a few lessons: small consistent steps throughout the day towards my larger goal is the best way for me to learn and games can make the time fly. I built Streets Ahead with these lessons in mind to help other people as well as myself learn Chinese. The goal is to make it feel less of a chore and still make progress to the larger goal. What it does Streets Ahead consists of three games: flash cards, multiple choice quiz, and a concentration card game. The reason for the three games is to conform with how much time and effort a student can give at any point to learning throughout the day. For example you might use flash cards while watching TV in the morning when you can't really think just yet, do a quiz in the afternoon while having tea, or for when you can give it your all, play the concentration card game to both work your short and long term memory. The concentration game is a bit unique because it solves a problem I am still having while learning Chinese. Rather than trying to matching the same word to each other or even matching the English to simplified Chinese translation to each other, it asks students to match pinyin characters to simplified characters. I think if a student works multiple parts of their brain for a task, they will be able to learn these relationships faster, which in my opinion, is the hardest part of learning the language. Finally, I wanted to help user's feel safe about any user data they might share with the Streets Ahead. The user can request to have all the data we have collected about them at any point. How I built it Facebook Messenger acts as the entry point to all the different games with the Facebook Messenger SDK signature used to authenticate the user. Wit.AI helps users navigate the bot and find different games to play. React is used to create all the web games. Facebook Analytics helps collect the minimal amount of data within the games so I know which features are popular and parts of the games some people might find difficult to navigate. Finally HHVM with Proxygen was used to build part of the back end for both the Facebook Messenger and Game Sync using HackLang . Google Cloud handles the core game experience. The language learning API is built on top of AWS with Azure Text to Speech used to create the audio recordings. Azure was chosen since they are the only provider with a neural option for Chinese out of the big three. Challenges I ran into This was my first time deploying HHVM and Proxygen on Google App Engine. Took a little longer than I was hoping but glad I did it. Plus, for anyone else who wants to try HHVM and Proxygen on GAE, I deployed an open repo with simple instructions on how to get started. https://github.com/jjdharmaraj/hhvm-app-engine-sample has a couple of samples including a little hack I built to get composer to work with HHVM. Accomplishments that I'm proud of Still trying to make a go at accomplishing my New Year's resolution!! Also building a variety of games to help me throughout the day that fit my lifestyle so I can keep learning during downtime. The main technical achievement I am proud of is deploying HHVM on app engine and getting composer to work. What I learned The best games are both snackable for the amount time it takes to complete and the amount of brain power it takes to complete the game. So, I built a range of games to fulfill a variety of appetites. Not to mention the amount of Chinese I learned while testing my games and building my Language Learning API. What's next for Language Learning API Visit the Great Wall of China!! I mean I did choose to learn the language for a reason. I would also like to package up my games as an Instant Game. That way I could add in-app purchasing to help build a revenue stream so the platform can be sustainable. I also would like to add more language support in the future. <div