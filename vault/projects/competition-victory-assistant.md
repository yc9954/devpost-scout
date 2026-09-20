---
slug: "competition-victory-assistant"
url: "https://devpost.com/software/competition-victory-assistant"
title: "Competition Victory Assistant"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 379
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "user/legal_professional"
---

# Competition Victory Assistant

> Have you ever wanted to win a competition but didn't even know where to start? Competition Victory Assistant will give you strategies, ideas, and even a chatbot to help you win a competition.

[Devpost](https://devpost.com/software/competition-victory-assistant) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**mechanism** [[voice_speech]]
**user** [[legal_professional]]

**stack** bedrock, partyrock

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for competition victory assistant

## Body

Your Future Self after using this app! Inspiration In order to come up with something unique and exciting, I wanted some help in figuring out what would be a winning entry in this competition. What better than to have PartyRock help me figure out a way to win? With this in mind, I went one step further and came up with Competition Victory Assistant 3.0. What it does Competition Victory Assistant 3.0 is designed to help the user strategize and win competitions. By submitting the terms of the competition and the judgement criteria, Competition Victory Assistant 3.0 outputs a general strategy guide, 5 winning ideas, and an interactive chatbot to talk through potential winning entry ideas. How we built it Once the idea was solidified, figuring out what kind of information would be helpful for the end user was pretty straightforward (Strategy, 5 Winning Ideas, and a Chatbot). Most of the work was focused on prompt engineering and testing a lot of different competitions. Challenges we ran into When testing Competition Victory Assistant 3.0, the initial "5 Winning Ideas" widget prompt was very simple: “Give me 5 winning entries for the competition in @competition and use the Judging Criteria in @Judging Criteria to help shape the answer". When I entered in the rules and judging criteria for this hackathon in, the "5 Winning Ideas" widget would instead make up imaginary hackers instead of ideas to help win the competition! This prompted me to take a deeper dive into Prompt Engineering and understanding the Temperature and Top P variables. Accomplishments that we're proud of I particularly enjoyed finding several different competitions to use as test cases. I found rules to a chili cook-off, karaoke competitions, this very hackathon, and even an obscure customizable card game's organized play rules. Tweaking the prompts through prompt engineering techniques as well as testing various temperatures and Top P values helped us dial in the desired values for each widget. What we learned LLMs are unlocking interesting ideas for what people are empowered to do with computers. I personally am very excited to see what voice assistants are capable of when powered by an LLM. What's next for Competition Victory Assistant With user feedback, prompts can be tweaked and other widgets can be added. <div