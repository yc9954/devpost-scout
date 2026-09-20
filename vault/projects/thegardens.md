---
slug: "thegardens"
url: "https://devpost.com/software/thegardens"
title: "TheGardens"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 454
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/accessibility"
  - "domain/finance_payments"
---

# TheGardens

> The adaptive banking app powered by a mobile app, web server, game and a microcontroller to free up your hand

[Devpost](https://devpost.com/software/thegardens) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[accessibility]] [[finance_payments]]

**stack** c++, css3, dart, esp32, flutter, html5, imu, javascript, python, sqlite, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for thegardens

## Body

Inspiration We wanted to make a Jarvis-like like in Iron Man, but the Desjardins sponsor challenge(and also some hardware quirks) decided to pivot to this. What it does Our project consists of four parts: A desktop video game in which the character collects treasures and travels through various environments in which they experience a multitude of weather conditions, a mobile application that reacts to the different weather conditions that the video game character is experiencing, a shared backend server where the desktop game and banking app can communicate, and a haptic glove capable of controlling the in-game character via hand gestures as well as navigate the mobile application using voice activation and commands. How we built it We started with the hardware, we built the glove relatively quickly, but we weren't able to DIY flex sensors(initial idea was to detect which fingers were bent for 2^5=32 possible actions) so we cut our losses & focused on aura. Linear algebra was done(Math 223 pinot the goat) with the IMU units to project ax ay az -> dx dy. Then we split our team into 2. Team A wrote the flutter mobile application, Team B built the game, and we touched base to build the server together after agreeing on the APIcontract. Challenges we ran into Throughout the realization of this product, we encountered many ordeals that significantly impeded on the progress our team made, most of which were related to the hardware part of the project. For instance, our decision to make our very own flex sensors from scratch ended in failure and forced us to innovate and find an alternative solution. Other issues involved faulty circuitry and difficulties combining the different sections of the project. Accomplishments that we're proud of We are very proud of the fact that we were able to create a fun-to-use piece of hardware that is able to communicate between multiple devices through bluetooth and WIFI. Furthermore, we are very proud of our development of a server that is able to relay information between two completely different devices. What we learned All in all, despite the many issues we encountered in these 24 hours, we ultimately learned many lessons through our collective efforts and teamwork. We all got to pool our different skills & experiences so that by the end of the hackathon, our team had a shared understanding on electronics, fullstack dev, & the idea of "production grade code." What's next for TheGardens We plan on continuing to develop the haptic gloves used in this project in hopes of one day helping many people such as those unable to conveniently use standard I/O devices like keyboards and mice whether it be due to working conditions or physical disabilities. <div