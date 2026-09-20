---
slug: "smoove-tqwl18"
url: "https://devpost.com/software/smoove-tqwl18"
title: "Smoove!"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 749
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/runtime_tool_creation"
  - "substrate/video_visual"
---

# Smoove!

> Smoove puts a new spin on slide puzzle games.

[Devpost](https://devpost.com/software/smoove-tqwl18) · hackathon [[Flutter Puzzle Hack]]

## Facets

**mechanism** [[runtime_tool_creation]]
**substrate** [[video_visual]]

**stack** flutter

## How they structured the write-up

- inspired by flutter!
- about the game/puzzle
- challenges we ran into
- how it was built it
- accomplishments that i'm proud of
- what i learned
- what's next for smoove!

## Body

Choose from a number of available images Instead of a square puzzle ... it's round! Start on an easy level with just 4 puzzle pices Work your way up to as many as 72 puzzle pieces which will keep you busy for quite a while! Inspired by Flutter! Flutter has been the most amazing dev tool I've ever used. I love that you're able to do pretty much anything you want, and for any platform you want ... even a Raspberry Pi! I had never built a game before, so I thought this would be a fun challenge. At first I literally just wanted to be able to see if I could make a simple slide puzzle using Flutter. I've only known about Flutter since May 2021 and I have only ever used it for more business-like applications so this seemed like fun. Little did I know how carried away I'd get! About the game/puzzle It's a simple slide puzzle ... but with a slight difference. Slide puzzles are traditionally square, with square puzzle pieces allowing it to slide left/right/up down. I wanted to try something a little unusual ... a round/circular puzzle! Challenges we ran into Early on I had a LOT of challenges ... and nothing to do with Flutter, but everything to do with the logic of how you make a circular slide puzzle! With a square puzzle you simple divide the image by a number of equally sized columns and rows, keep one space blank and away you go! With a circular puzzle it's not quite that easy! Logically you think ok, we just create a number of concentric bands of equal width and then we split each into a number of segments ... seems easy right? Now try and do it dynamically! In order to be able to use any background/puzzle image, all the segments pieces need to be calculated ... not just its position and which part of the image should display, but also its shape and orientation. As a piece moves from one position to the next in the same band, the size stays the same, but the orientation angle changes. When you move from band to band ... the piece's size changes. Of course thanks to Flutter and its clip path capability for widgets, this ends up being very doable. ... but then there's the center piece! Traditional puzzles have an empty square on the bottom right, this puzzle has an empty circle in the middle! Easy you say! Maybe, but in order for a puzzle piece to move from the right hand side of the center circle e.g., through the center and then to the left hand side (or above), the piece has to go through many transformations. The section of the background image can't just remain at the same angle or size ... or even shape! So to make the animation/transition look smooth, the background has to rotate smoothly with the transition, and the shape has to morph. This created a very interesting and almost hypnotic effect as you watch it transition between those states! How it was built it It's all Flutter baby! I started with just the ability to take an image asset and divide it into segments. It dynamically creates a number of widgets, each assigned on initial "position". Based on its initial position and its current position the widget then figures out where to draw itself. Once I figured out the mechanics of drawing the slide pieces and different positions, I then worked on animation the movement from one to the next. Calculating background positions for this and the shapes as well required a lot of trigonometry, but the results were very pleasing. With the game mechanics sorted out, it then came time to use Flutter's awesomeness to just make it look good ... applying gradients and shadows (I say in a subtle way, others may disagree!) to make it all pop. Accomplishments that I'm proud of This was the first ever game I built. I work full time (long hours!) yet I was able to pull this off in what I think was a very short time ... thanks to Flutter (and the thousands of Flutter videos I've watched on Youtube over the last 8 months!!!) What I learned There is absolutely nothing like Flutter and almost nothing I can't do with Flutter! What's next for Smoove! Implement game center for leaderboards etc. I feel this is only just the start for Smoove! <div