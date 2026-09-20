---
slug: "the-great-gatsby-review-session"
url: "https://devpost.com/software/the-great-gatsby-review-session"
title: "A Review Session On The Great Gatsby"
hackathon: "Alexa Skills Challenge: Alexa Conversations"
organization: "Amazon"
winner: true
words: 302
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
---

# A Review Session On The Great Gatsby

> An Alexa Skill that allows students to review F. Scott Fitzgerald's novel, The Great Gatsby, through multiple-choice and free response questions - powered by Alexa Conversations.

[Devpost](https://devpost.com/software/the-great-gatsby-review-session) · hackathon [[Alexa Skills Challenge- Alexa Conversations]]

## Facets

**domain** [[education]]
**user** [[educator_student]]

**stack** alexa, amazon-alexa, node.js

## How they structured the write-up

- inspiration
- what it does
- how it's built
- challenges i ran into
- what's next
- what i learned

## Body

Inspiration One of my favorite school memories was of my literature class where we had intimate discussions on books and short stories together. Not only was it a fun way to learn, it was a smart way to learn. "[T]he dual action of speaking and hearing oneself... has the most beneficial impact on memory," a study by the University of Waterloo found. This project hopes to nurture discussion between Alexa and students. What it does Provides review sessions on the first three chapters for free Goes over multiple-choice questions on the story and literary devices (symbolism, polysyndeton, etc.) Converses with the user in forming an answer to a free response question Lets customers review the rest of the book (chapters 4-9) through in-skill purchase How it's built Uses an intent-based dialog manager to handle chapter selections and multiple-choice question answers Uses Alexa Conversations to handle answers to free response questions; this allows: collection of multiple parts of a free response answer - who, what, where, when, why, and how conversational memory without complicating the back-end less time spent on dialog creation Uses a Node.js back-end to delegate between the two dialog managers Challenges I ran into Learning how to use Alexa Conversations was a big challenge that I could not have overcome without the help of Justin Jeffress , Sam Ingbar, Nathan Grice, and the other wonderful people of the Alexa team . What's next A time when we can ask Alexa, "start a review session on Romeo and Juliet" A time when we can ask Alexa, "start a review session on Night by Elie Wiesel" A time when we can ask Alexa, "start a review session on Midnight's Children" What I learned When dealing with an input set as infinite as the English language, Alexa Conversations is a must-have tool. <div