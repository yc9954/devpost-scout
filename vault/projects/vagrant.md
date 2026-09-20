---
slug: "vagrant"
url: "https://devpost.com/software/vagrant"
title: "Vagrant"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 561
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Vagrant

> 🐜 Harold wanders hill to hill searching for a place to rest his weary legs. Unfortunately strangers don't take too kindly to a vagrant in their midst, help Harold escape before the locals get wise.

[Devpost](https://devpost.com/software/vagrant) · hackathon [[Flutter Puzzle Hack]]

## Facets


**stack** bloc, firebase, flutter

## How they structured the write-up

- play now
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vagrant

## Body

Collect Power Ups! Compare your score to the Rest of the world Can you provide a clear path for Harlod? Where can he go? Play Now You can play right now at vagrant.ThatcherFamily.org Inspiration The Flutter Puzzle Hack prompt inspired the brothers behind Vagrant to relive the struggles and joys of solving slide puzzles as children. Naturally we also asked ourselves “How can we make the classic slide puzzle more interactive?” and better yet “How can we make it more competitive?” As children we could rarely play games without making them extra competitive. Many games were easily dominated by the elder brother, but one game type provided a slightly more even playing field. Maze building games provided countless hours of friendly challenges through the years. We realized that the slide puzzle interface can serve well for the foundation of a new maze building game that we as brothers could collaborate on before returning to our competitive ways. What it does In Vagrant Harold wanders colony to colony searching for a place to rest his weary legs. Unfortunately strangers don't take too kindly to a vagrant in their midst, help Harold escape before the locals get wise. Your task is to help Harold escape the unfriendly ant hill by sliding the tunnel tiles into a configuration that will lead him to safety. How we built it Vagrant was built using the Flutter framework to initially target a web deployment. Fortunately, since we used Flutter, deploying the app to multiple platforms was almost trivial. We learned how to effectively resize and reposition widgets based on windows size or screen form factor, which allows Vagrant to be responsive and intuitive no matter the device you are using. We were also able to quickly integrate Firebase login and storage. With this you are able to switch devices while maintaining your level progress as well as the consumable power ups that you can collect. Challenges we ran into State management proved to be more difficult than we had originally expected. Thankfully the Flutter Community online offers great insight and tools to solve this complex problem. After some research and a few quick proof of concepts we decided to use the “flutter_bloc” package to maintain and inject our state where it needs to be to build our interactive UI. Accomplishments that we're proud of We are proud of the replayability of this slide puzzle game. The fact that there are multiple ways to win and additional bonuses for taking a little longer. We are also proud of how we were able to complete this project with minimal brotherly feuds. What we learned We learned that adding animations, which generally strikes fear in our hearts, is in fact an enjoyable experience with Flutter. Many of the needed animations were achieved with implicit animations, almost like magic. While some of the more complicated animations, like marching the ant along a moving tile, took a little more work, they were still quite easy to understand and accomplish in code. We also gained an even greater respect for the Development community around Flutter. There are so many helpful people and resources out there. What's next for Vagrant We will continue to develop Vagrant and get it deployed to the App Store and Google Play. We will add additional game modes and consumables that will add new dimensions to the game. <div