---
slug: "animal-workout"
url: "https://devpost.com/software/animal-workout"
title: "Animal Workout"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 452
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
---

# Animal Workout

> Become different animals while getting exercise. Great for rainy days and sunny days too!

[Devpost](https://devpost.com/software/animal-workout) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets

**domain** [[developer_tools]]

**stack** amazon-alexa, amazon-web-services, javascript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for animal workout

## Body

Inspiration My kids usually (okay, not as much as I’d like) are able to entertain themselves, but every once in a while they run out of ideas. It usually coincides with a lot of unreleased energy. One day I just started having them bounce on one foot, then the other, then raise their arms over their head. They had so much fun with my impromptu workout that I decided to build it in to an Alexa skill. What it does After launching Animal Workout, Alexa goes through a series of three different animals that a child ‘becomes’. With each animal, Alexa gives a quick fact, and then has the kiddo do some sort of movement such as leaping or walking very slowly. On each set of three animals there is a medium, low, and high intensity movement. After going through a set of three, Alexa will ask the kiddo if the'd like to keep going or stop. If they keep going, Alexa will throw in an encouraging word before starting the next three animals. The animals are randomly picked, so the workout is different each time. How I built it I used AWS pretty intensively. AWS Lambda hosts my javascript code to run the Alexa Skill, while I store my audio files in S3. I initially used the basic fact skill template in AWS Lambda that uses the ASK NodeJS SDK and then did a bunch of alterations. Using the SSML markup to add pauses and audio really simplified things. Challenges I ran into When testing my alexa skill, I would intermittently get an error message and no data returned. I realized that in some cases, I was trying to retrieve more than 5 audio files at times, but needed to keep it to 5 or less. I ended up removing most of my animal sounds and just leaving the music part. I also had some issues with my audio files not being at the right rate or quality, so I had to adjust them to get them to run. Accomplishments that I'm proud of I’ve been driving my husband nuts (and I can’t help it), as every day I check my unique customers and let him know the numbers. It’s been really fun to track and watch engagement. I also really value the feedback I get from reviews. What I learned I hadn’t ever tried to incorporate audio in to an Alexa skill before, so that was pretty neat - especially with how seamless it was. What's next for Animal Workout I’m not sure yet. I’ve thought about adding in more animals, more facts (so you get different facts each time you bring up a specific animal), and even jokes. <div