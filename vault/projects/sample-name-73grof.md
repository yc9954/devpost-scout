---
slug: "sample-name-73grof"
url: "https://devpost.com/software/sample-name-73grof"
title: "Light It Up"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 754
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/geospatial"
---

# Light It Up

> Carry electricity from the generator to bulbs to light up bulbs by sliding different kinds of wires.

[Devpost](https://devpost.com/software/sample-name-73grof) · hackathon [[Flutter Puzzle Hack]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[geospatial]]

**stack** animated-text-kit, dart-extensions, firebase, flame, flutter, google-fonts

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for light it up

## Body

Start game screen Game play 1 Game play 2 Pause game screen End of game screen Inspiration Thousands of miles of cable cover our oceans, powering countries and bringing the internet to the far reaches of the globe. Without a complete connection, countries can go completely dark. Once, a fishing boat accidentally broke one of the cables and 10 countries lost access to the internet! We are amazed at how electricity works. As such, we set out to make a game with one goal: complete the connection to bring electricity from source to destination. What it does By sliding different types of wires, our game simulates carrying electricity from a generator to a light bulb, to “Light It Up”! Completing the circuit can be challenging at times! How we built it We were impressed that Flutter has game engine libraries. So, we wanted to use a game engine to develop the game. We found Flame, a popular and new game engine. Since Flame is so new, there are very few resources apart from Flame's official documentation and some sample projects. We just read the documentation and examined a few projects that are developed with Flame. From there, we just started experimenting! We developed Light It Up in Android Studio. Android Studio enabled us to run the game on the web or a mobile device. So, we were able to test it through a browser, on iOS, and on Android. We deployed the project with Firebase Hosting. Challenges we ran into There are a few challenges we ran into: Since Flame is so new, we struggled, at times, to get it to work the way we wanted. Many times we were able to explore a sample project to understand how the engine worked. However, there were not very many resources available, so, at other times, we just had to try something ourselves. In a game engine, you need to provide exact coordinates and exact dimensions to place objects on the screen. There are no components like CoordinatorLayout or ListView to organize the UI. We had to write algorithms for calculating the exact coordinates of every game object, after each user action. Since we did not have much experience around this, it complicated the development process. When writing these UI-layout algorithms, we wanted to ensure we supported any screen size. This further complicated the layout algorithms. Accomplishments that we're proud of We can tell a few accomplishments we are proud of: Rather than copying the sample projects for the competition, our team opted to challenge ourselves with the newer Flame game engine. This was a risky decision, but we believe it payed off for us! We made this an open source project. We believe that the project will be a helpful resource for anyone looking to develop a game using Flutter + Flame. We did our best to write clean and understandable code for anyone exploring our project. You can resize your browser window to change the scale of the game! The project also supports mobile devices. This was a challenge we faced with Flame, as this functionality is not automatically provided by the library. We are proud that we were able to make this work and think that it resulted in a much higher quality project. What we learned Our team has been using Flutter for a long time, but we didn't know it was possible to make games with the framework. This project taught us that we can make great games in Flutter! We also ran across other game engines that even provide the ability to create 3D games. As you can see in the sample project for this competition though, you can develop games without a game engine! We continue to be amazed with the tools that Flutter provides and its power as a development framework. We also learned features, facilities of Flame in this project! It is not difficult to make 2D games with Flame. What's next for Light It Up We have a few things to add that we couldn't add because of time limitations. Our game consists of just 5 levels, all of which are created manually. In the future, we would like to write an algorithm to generate levels dynamically and automatically. We want to create a level selection screen, instead of forcing the player to start from level 1 each time they return to the game. We want to give users a star rating or score, based on how long it takes them to complete a level. <div