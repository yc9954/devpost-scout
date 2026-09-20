---
slug: "shower-buddy"
url: "https://devpost.com/software/shower-buddy"
title: "Shower Buddy"
hackathon: "Alexa Skills Challenge: Tech for Good"
organization: "Amazon"
winner: true
words: 583
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Shower Buddy

> See how much water you showering and what that equates to in relatable quantities like cans of soda or watermelons.

[Devpost](https://devpost.com/software/shower-buddy) · hackathon [[Alexa Skills Challenge- Tech for Good]]

## Facets


**stack** amazon-dynamodb, ask, javascript, s3

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for shower buddy

## Body

Inspiration The inspiration for this project had to do with my personal shortcomings and passions. I do my best to reduce my negative impact on our planet. It's something that means a great deal to me. Everyday I do the little things I can to help, like picking up any trash I see, using a refillable water bottle and always turning off the lights as I leave the room. One day I happened to think about my shower habits and realized I take much longer than I need to. I researched the output of most shower heads and realized I was wasting a lot of water. That gave me the idea to create this skill and maybe help others come to the same realization that I did about how much water we waste by spending those extra couple of minutes in the shower. What it does Shower Buddy times how long you are in the shower and uses that duration as well the average output of a shower (2.1 gal/min) to determine how much water you use. In addition to the boring quantity in gallons it will give you the equivalent as a more interesting and relatable quantity, such as cans of soda, to put into better perspective how much water you used. How I built it I built Shower Buddy using the Alexa Skills Kit platform and hosted my javascript code on AWS Lambda. For the timing functionality I used a DynamoDB table to record the timestamp of the start request so that when the stop timing request was made the skill can use both timestamps to determine the duration of the shower. The javascript code has a list of quantities, such as cups of coffee or cans of soda, that is uses to format the water used into a more relatable representation. Challenges I ran into The biggest challenge I ran into was how to build a stopwatch-like timer into my skill. There was no inherent way to do this through the Alexa Skills Kit or javascript so I had to find my own way to do it. I saw that each request through Alexa has a timestamp and those could be used if I could save the starting timestamp. So with that in mind I had to learn to use DynamoDB, something I'd never used before, so I could make this functionality a part of my skill. Accomplishments that I'm proud of I am proud of the fact that I was able to create a timer within my skill to track the shower duration. I have tried to make this skill in the past, as I had the idea a while ago. This part always tripped me up and I never finished. But for this challenge I knew my idea really fit the theme so I was determined to make it work. After a lot of research and thinking I finally did it and was overjoyed when I got it to work. What I learned I learned how to use a DynamoDB table with Alexa and AWS Lambda. This will prove useful in my future skills because I can now include memory persistence to create a better, more involved user experience. What's next for Shower Buddy Next up for Shower Buddy will be a family leaderboard to compete against members of your family for who can use the least water while in the shower. I believe people's competitive nature can be a big promotor to further conserve our resources. <div