---
slug: "bed-jumpers"
url: "https://devpost.com/software/bed-jumpers"
title: "Bed Jumpers"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 249
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Bed Jumpers

> Interactive version of Five Little Monkeys Jumping On The Bed

[Devpost](https://devpost.com/software/bed-jumpers) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets


**stack** alexa-skills-kit, aws-lambda, node.js, rollup, serverless

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for bed jumpers

## Body

Inspiration My nearly 2 year old daughter often asks me to recite Five Little Monkeys Jumping On The Bed, but with random things she's thinking of. For example, she'll say things like, "Five little whales? Five little apples? Five little pants?" Of course, I oblige, but I've been told it's not uncommon for kids to do that, so I figured this would be something fun to implement. What it does The Alexa skill recites Five Little Monkeys Jumping On The Bed, except the child will be prompted to select what's jumping on the bed, and will be asked how many remain in between verses. How I built it I made liberal use of speechcons, SSML, and audio sources to make it fun and engaging. Challenges I ran into Originally I was going to do do this in song form, but considering Alexa only allows 5 audio sources per response, I had to settle for just letting Alexa recite the verses and let the child answer how many remain in between verses. Accomplishments that I'm proud of My nearly 4 year old son is actually pretty good at interacting with it by himself, whereas my daughter loves the random speechcons. I think the sweet spot would be between 5 and 8, but I'm glad my kids enjoy it! What I learned It was pretty fun playing with <prosody /> and <audio /> . What's next for Bed Jumpers I hope to get feedback from parents and will act accordingly. <div