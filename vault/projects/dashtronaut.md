---
slug: "dashtronaut"
url: "https://devpost.com/software/dashtronaut"
title: "Dashtronaut"
hackathon: "Flutter Puzzle Hack "
organization: "Google"
winner: true
words: 1302
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
  - "user/educator_student"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Dashtronaut

> Solve a Slide Puzzle with Dashtronaut by your side, the Astronaut Dash!

[Devpost](https://devpost.com/software/dashtronaut) · hackathon [[Flutter Puzzle Hack]]

## Facets

**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]] [[educator_student]]
**substrate** [[video_visual]] [[web_dom]]

**stack** animations, custompainter, dart, flutter, getit, provider, rive

## How they structured the write-up

- slide puzzle game built for the flutter puzzle hack challenge
- inspiration
- about dashtronaut
- how dashtronaut was built
- challenges i faced
- educational content
- what's next for dashtronaut

## Body

Dashtronaut - Slide Puzzle Game Built With Flutter Dashtronaut Motivates & Supports you! 3x3 Size Puzzle Dashtronaut Motivates & Supports you! 4x4 Size Puzzle 5x5 Size Puzzle 6x6 Size Puzzle Share your score Dashtronaut Slide Puzzle Game Built For The Flutter Puzzle Hack Challenge Made by Roaa Khaddam (@roaakdm) Inspiration When the Flutter Puzzle Hack Hackathon was announced , I had just got Covid and was in house quarantine. So in the midst of all the physical as well as psychological symptoms, most importantly, feeling like my life has no meaning, this challenge came to the rescue. It gave me the opportunity to focus all the energy I can summon to work on something I’m extremely passionate about. So I dove in and did nothing but Flutter day and night for a couple of weeks to create my version of the slide puzzle. I cherished the distraction and brainstormed lots and lots of ideas. I wanted so badly to challenge myself. I had been working with Flutter for about 2.5 years and I felt confident that my skills and experience are up to the challenge. Also, being passionate about and having some experience in graphic & UI design, I knew that I had the ability and opportunity to create something cool visually and programmatically! (Ahm, unicorn developer speaking 🦄) About Dashtronaut Dashtronaut is a slide puzzle game set out in space with Dashtronaut, Dash the Astronaut, floating in space and interacting with the user. Most of the basic puzzle functionality found in the example app is present in addition to some user experience enhancements, interactivity, and design features including: The ability to swipe the tiles and have them move in the direction of the swipe. Giving the user the option to change the puzzle size to easier or more difficult sizes to solve than the default 4x4 puzzle. Tile animations created with Rive that run when a tile is moved to its correct place and when the puzzle is solved. Persisting user progress including elapsed time, moves count and puzzle size even when the app is closed and reopened. Showing the user a list of their last 10 scores in the app drawer. Stopwatch that starts automatically on the first tile move. Space-themed environment design around the puzzle with planets that animate into view along with the puzzle board on app launch as well as stars randomly laid out and animated using Flutter’s CustomPainter Dashtronaut floats into view on app launch then floats in place. With phrase bubbles, tapping on her let’s her express herself in a fun way. She also motivates the user to solve the puzzle and she is amazed when they pick a difficult puzzle size! Haptic feedback for multiple events like moving a tile to its correct place, solving the puzzle, and tapping on Dashtronaut To optimize performance, shader captured in the Skia Shader Language (SkSL) was warmed up and cached and added to the builds of each platform to avoid animation jank on the first app run. Responsiveness: The puzzle and its surrounding UI is responsive for all screen sizes. Most importantly, the puzzle board is laid out such that it is all in-view in landscape mode in small screens How Dashtronaut Was Built I started by reading through the example code made by the awesome people of Very Good Ventures . I learned a lot from it but ended up starting from scratch and only using the puzzle logic ( e.g. solvable puzzle algorithm), along with minor puzzle features here and there, from the example code. I wanted an empty canvas to spread my ideas on and I wanted to make tweaks on the way the puzzle tiles were laid out and how they interacted with user input. After doing some planning and typing up some Todo’s in a text note that is growing in length until this very moment, I dove into the development of my slide puzzle version by clearing out the code of the good old Flutter counter app that comes with any new Flutter project and started coding from there. In the couple of weeks I was quarantined and working only on my slide puzzle, I managed to finish only the basic puzzle logic and layout. I achieved what I had in mind by adding the ability to swipe the tile in the target position direction and have them animate to it. And I added keyboard and mouse support. At this point the puzzle was a skeleton! It looked like this: It even had the ability to do this: Wouldn’t such a puzzle be much easier to solve! Anyway, as soon as the puzzle was in a stable state and I got to the design part, I tested negative for Covid and had to get back to real life and I wasn’t able to focus on the puzzle full-time. So in the remaining weeks before the deadline, in between client projects and my full-time job responsibilities, I squeezed in some hours and was able to create the designs and animations, come up with the Dashtronaut name, buy a domain to host the web app and the app landing page and tutorials pages, which I also built as quickly as I could with pure Html, CSS & JavaScript, deploy the web app, submit the app to the App Store (iOS & MacOS) and to the Google Play Store for Android, and finally, work on the demo video. Design Inspiration - Why Dashtronaut? I liked the idea of presenting the image of the tiles floating in space, so I created the design accordingly. And because this is a game, I wanted to add something fun and interactive to it, I wanted to add a character! And since the puzzle is in space, it made sense to have an astronaut character. But what made even more sense, and what I’ve wanted to do since the moment I saw the hackathon announcement, is bring Dash, the beloved and unbelievably cute Flutter & Dart mascot, into the picture! By grabbing a pen & paper and doing a quick sketch, Dashtronaut, Dash the Astronaut, was born! Challenges I faced 2 words: App Review . It’s always a nightmare. And even when I anticipated that it would be a nightmare and made sure to finish the app and submit it to the App Store and Play Store as soon as possible, it still was an excruciating process of having the app rejected multiple times and uploading build after build after build. But thankfully, eventually I was able to release the app a few days before the deadline so that I had some time for user feedback as well as time to set up the tutorials website and write some tutorials. Educational Content It felt selfish to me to enjoy the process of creating Dashtronaut that much and not share it! So I dedicated pages in Dashtronaut’s website to articles explaining the app’s architecture as well as individual tutorials detailing each feature in the app. And those tutorials will be updated and added to regularly. The Published Tutorials: App Architecture, Folder Structure, and Widget Tree The Background Stars - Creating And Animating The Stars Using CustomPainter I will also be giving a session to showcase this slide puzzle and talk about its app architecture, folder structure, and other technical details in the Silicon Vally Flutter Festival event on March 23rd What's next for Dashtronaut With Flutter, there are absolutely no limits to what you can do. And Dashtronaut is nothing but a small portion of what I wanted to do. But I’m proud of what I accomplished and will do my best to keep updating the app with features in the future. Because it turned out to be an amazingly fun project rich with stuff to learn and teach. <div