---
slug: "pilot-talk-pth4iv"
url: "https://devpost.com/software/pilot-talk-pth4iv"
title: "Pilot Talk"
hackathon: "Alexa Skills for Students – Powered by AWS Educate"
organization: "Amazon"
winner: true
words: 448
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/education"
  - "user/educator_student"
  - "substrate/financial_record"
---

# Pilot Talk

> Learn to navigate the skies with Alexa

[Devpost](https://devpost.com/software/pilot-talk-pth4iv) · hackathon [[Alexa Skills for Students - Powered by AWS Educate]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[financial_record]]

**stack** alexa, fsm

## How they structured the write-up

- inspiration
- what it does
- how i had built it
- accomplishments that i'm proud of
- what i learned
- what's next for pilot talk

## Body

Inspiration As an aspiring pilot we are usually trying to juggle between many different learning materials. However, the one aspect that no book can teach us to overcome is the act of navigating and speaking on the radios effectively. It's incredibly hard to practice - especially when the things that we have to learn to say are constantly changing. It got us thinking, what if Alexa could help tune our experience on the radios to help us become more effective. What it does Pilot talk is designed to help you get better at speaking on the radios as a student pilot. The virtual instructor will let you know what to say and then ask for follow up items if you missed anything. You can ask for an example at any time. As we add more and more scenarios, you will be able to navigate yourself through the busy skies just like a professional pilot on the radios. Be sure to say your commands fast because Alexa stops listening after eight seconds. How I had built it To core of the system is built as a finite state machine. This is something that was very unique. There are so many different things that can happen in the air, and keeping track of all the states to make a proper voice flow without using if statements everywhere was incredibly powerful. Accomplishments that I'm proud of Building a way such that you can say something and having Alexa wait for a confirmation was super cool! I think you'll realize that when you are playing. You have to repeat back what the controller just said, and that was an interesting implementation. I am also super hapoy with the way the conversational flow works. It's just a matter of adding a few more states to the FSM, and that's handled very elegantly in the code to make sure that response ids line up. What I learned I had never worked with Finite State Machines before. That was super cool. I think they are very powerful ways to build skills that can create a great a conversational experience and maintain state. Building Alexa skills with the new console. The console was friendly and I was able to get up and running very quickly. This was different from my past experiences. What's next for Pilot Talk I need to build in more states and clean up some interaction pieces. I also need to go to the Alexa Dev Team and request if I can extend teh 8 second listening time - since it creates a poor experience. I need to also add a few more randomizers to make this more of a story game. <div