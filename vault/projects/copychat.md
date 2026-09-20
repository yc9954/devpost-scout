---
slug: "copychat"
url: "https://devpost.com/software/copychat"
title: "CopyChat"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 464
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
---

# CopyChat

> CopyChat is a language learning tool designed to allow a person to listen and recite a word in a language they want to learn. It's a great learning tool using Cognitive Services Speech as its backbone

[Devpost](https://devpost.com/software/copychat) · hackathon [[Azure AI Hackathon]]

## Facets

**domain** [[education]]
**user** [[educator_student]]

**stack** azure, c#, cognitiveservices, speech, xamarin

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for copychat

## Body

Read the word and say it in the desired language you want to learn Inspiration Learning a new language can be hard! You can read a book, or join a class. But how do you know if the words you say are correct? That’s where CopyChat can help. CopyChat is a new app that shows you a word in your language and prompts you to say the same word in the language you want to learn. If you are correct you get to move onto the next word. If you are wrong, you go back to the previous word. The market is huge for language learning and only getting bigger. Indeed language learning is estimated to be a $20 billion dollar industry by 2026. But with so many apps and books in this market what was the gap? I did some research and it turns out that countries like Japan we're desperate to have english speaking people come over and teach because it turns out that the hardest part about teaching english was just having someone "chat" to these students. I then devised the idea of CopyChat. CopyChat is a gamified language learning system designed for a person to recite a word in a language and have the system verify that what they said was correct or not. I started looking into this idea back in the days of Project Oxford but I was not adept with cross-platform development at that stage. Now I have a grasp on cloud and mobile technologies I decided to look at this again. What it does CopyChat allows you to pick from 8 langauges to recite. Each time you get the word right you progress to another word in a series, such as "Greetings", "Places", "People" etc.,. If you get it wrong you move back one step. This helps to re-enforce the learning while making it fun. How we built it I first used Xamarin Forms to create a cross-platform app for iOS and Android. I then used Azure's Cognitive Services Speech service to compare a pre-populated language matrix with what was uttered by the user. I could have used the synthesized speech as well but this will incur further costs. Challenges we ran into Didn't realize Speech Services needed to have a PAYG subscription. Accomplishments that we're proud of Got it working!! What we learned Languages are hard! What's next for CopyChat I think to keep costs low and development going I think a subscription model to this service would be good to subsedize the costs for the Speech service long-term. I may even look to have a pay as you go model that groups questions up into "stages". I also want to work on phrase analysis and include pictures and more of a "game" feel. <div