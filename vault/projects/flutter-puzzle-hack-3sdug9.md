---
slug: "flutter-puzzle-hack-3sdug9"
url: "https://devpost.com/software/flutter-puzzle-hack-3sdug9"
title: "Hash"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 531
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "user/educator_student"
---

# Hash

> Have fun learning to count to 15 in different languages!

[Devpost](https://devpost.com/software/flutter-puzzle-hack-3sdug9) · hackathon [[Flutter Puzzle Hack]]

## Facets

**domain** [[developer_tools]] [[transportation]]
**user** [[developer]] [[educator_student]]

**stack** dart, flutter, rive

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hash

## Body

Hash Logo Level Selection Starry Starry Night Multiplatform FTW Language Selection Inspiration Flutter brings to the table a new level of ease and convenience when it comes to cross-platform development with stunning animations. Smitten by the abundant tutorials and low barrier to entry, flutter presented itself as a very attractive framework to developers who are keen to elevate their app experience. As developers who want to bring better user experiences and interfaces to our users, getting our hands dirty with Flutter was a no-brainer and what better way to do it than through a hackathon. What it does Hash is an educational tile game that focuses on aesthetics and comes with a variety of features. Features include the following: Educational game, multi-language gameplay Grooved Tiles Dark/Light Mode Multi-platform (Web, Android, Windows, Linux) Indicator for tile in correct position Background music and sound effects Rive animation integration Random background events while playing (paratrooper & fish balloon) Carousel menu Difficulty level selector Responsive to screen size changes Supports different modes of play (touch, mouse clicks & keyboard arrows) How we built it Hash is built from scratch using Flutter and Rive. Flutter provides the foundation for the game and the coordination between animations while Rive gives us the flexibility to create and employ more complex animations. Challenges we ran into We ran into many challenges but more notable 3 of which allowed us to learn a lot. Coordination between Flutter and Rive can be tricky at times. Rive animation relies on setState to trigger or transit, however, the frequency of setState and the duration of animations are not in sync. This has caused issues like animation not being played sometimes. Gesture handling for Rive assets Gesture handling is done solely via flutter and with no bindings to Rive assets, we are forced to overlay a gesture grid on top of our assets due to the way our Rive assets are built. This is not ideal and is one of our key takeways. Flutter lifecycle In the initial days, we didn't really understand why certain issues were popping up and how to go about debugging them. Related to both 1. and 2., understanding Flutter's lifecycle becomes critical to the fruition of our game. Accomplishments that we're proud of For our first time touching the Flutter framework, we are proud of our work. We are proud of how beautiful it turned out to be. What we learned Aside from the hard skills like Flutter development and Rive animation, one key takeaway for us is that understanding fundamentals remain one of the most important aspects in development work. We made the mistake of diving in headfirst and wasted a lot of time on debugging. Even a crash course on the fundamentals would have gone a long way and would very likely affect design and implementation decisions as well. We also documented some of our tricks and techniques in the following links https://medium.com/@tanjiansin/rive-trick-frame-chaining-with-state-machines-6b184a9065bd https://medium.com/@hexcone/flutter-puzzle-hack-handling-interaction-between-elements-with-z-index-9cd8bb3dde39 What's next for Hash Hash will remain as a hobby project for us to work on during our free time but more importantly, Hash will serve as a reminder for the wonderful time we had working on it through this hackathon :). <div