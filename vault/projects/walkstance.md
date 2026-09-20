---
slug: "walkstance"
url: "https://devpost.com/software/walkstance"
title: "Walkstance"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 203
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# Walkstance

> Make Social Distancing fun with AR.

[Devpost](https://devpost.com/software/walkstance) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets


**stack** arkit, scenekit, swift, xcode

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned

## Body

Problem Solution How it works Home Screen Step 1 Step 2 Wow it spins Social Distancing from a tree Inspiration 33.7K confirmed COVID-19 cases in NYC (as of Mar 29) social distancing is still not ubiquitous determining 2 meter distance can be stressful fidget spinners relieve stress need for positivity / rainbows What it does Walkstance places a rainbow circle under you on the ground in AR. The rainbow represents the "safe zone" when you are walking and social distancing. The radius of the circle is 2 meters, so you just need to make sure that other people are outside the rainbow. Walkstance is interactive. You can swipe left or right to spin the rainbow. If you keep swiping in the same direction it spins faster, just like a fidget spinner. How I built it First I made sure the rainbow's center always follows the device's real-world position. After that worked I added swipe detection and the spinning feature. Challenges I ran into XCode 11 glitches. e.g. "Message from debugger: Terminated due to memory issue" Accomplishments that I'm proud of The app works! What I learned Figured out what hitTest does and how matrix transformations work. Got solid knowledge on gesture recognizers. <div