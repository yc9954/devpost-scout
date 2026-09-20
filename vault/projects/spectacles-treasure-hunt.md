---
slug: "spectacles-treasure-hunt"
url: "https://devpost.com/software/spectacles-treasure-hunt"
title: "SnapChest"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 698
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
---

# SnapChest

> Find treasure using the Spectacles + haptic smartphone feedback!

[Devpost](https://devpost.com/software/spectacles-treasure-hunt) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]]

**stack** figma, github, javascript, lens-studio, spectacles, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for snapchest

## Body

Preview of our UX architecture Early-stage diagram of our algorithms for treasure chest detection Treasure chest that appears once user enters inner radius Lens Studio Development Environment Inspiration Open-world AR applications like Pokemon Go that bring AR into everyday life and the outdoors were major inspirations for this project. Additionally, in thinking about how to integrate smartphones with Spectacles, we found inspiration in video games like Phasmophobia's EMP sensors that react more strongly in the presence of ghosts or The Legend of Zelda: Skyward Sword that contained an in-game tracking functionality that pulsates more strongly when facing the direction of and walking closer to a target. What it does This game integrates the Spectacles gear and smartphones together by allowing users to leverage the gyroscopic, haptic, and tactile functionalities of phones to control or receive input about their AR environment. In the game, users have to track down randomly placed treasure chests in their surrounding environment by using their phone as a sensor that begins vibrating when the user is facing a treasure and enters stronger modes of haptic feedback as users get closer to the treasure spots. These chests come in three types: monetary, puzzle, and challenge. Monetary chests immediately give users in-game rewards. Puzzle chests engage users in a single-player mini-game that may require cognitive or physical activity. Finally, challenge chests similarly engage users in activities not necessarily games, and a stretch goal for multiplayers was that if multiple users were near a spot that another user found a treasure in, the other n users could challenge the treasure finder in a n vs. 1 duel, with the winner(s) taking the rewards. How we built it Once we figured out our direction for the project, we built a user flow architecture in Figma to brainstorm the game design for our application ( link ), and we also visualized how to implement the system for integrating phone haptic feedback with the spectacles depending on distance and directional conditions. From there, we each took on specific aspects of the user flow architecture to primarily work on: (1) the treasure detection mechanism, (2) spawning the treasure once the user entered within a short distance from the target, and (3) the content of the treasure chests (i.e. rewards or activities). Nearly everything was done using in-house libraries, assets, and the GenAI suite within Snap's Lens Studio. Challenges we ran into As we were working with Spectacles for the first time (compounded with internet problems), we initially encountered technical issues with setting up our development environment and linking the Spectacles for debugging. Due to limited documentation and forums since it is limited-access technology, we had to do a lot of trial-and-error and guessing to figure out how to get our code to work, but luckily, Snap's documentation provided templates to work off of and the Snap staff was able to provide technical assistance to guide us in the right direction. Additionally, given one Spectacle to work with, parallelizing our development work was quite challenging as we had to integrate everything onto one computer while dealing with merge conflicts between our code. Accomplishments that we're proud of In a short span of time, we were able to successfully build a game that provides a unique immersive experience! We've come across and solved errors that didn't have solutions on the internet. For a couple of members of our team, this sparks a newfound interest in the AR space. What we learned This was our first time working with Lens Studio and it's unanimously been a smooth and great software to work with. For the experienced members on our team, it's been a rewarding experience to make an AR application using JS/TS instead of C# which is the standard language used in Unity. What's next for SnapChest We're excited to push this app forward by adding more locations for treasures, implementing a point system, and also a voice agent integration that provides feedback based on where you're going so you won't get bored on your journey! If Spectacles would be made available to the general public, a multiplayer functionality would definitely gain a lot of traction and we're looking forward to the future! <div