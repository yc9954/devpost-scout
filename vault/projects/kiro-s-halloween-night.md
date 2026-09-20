---
slug: "kiro-s-halloween-night"
url: "https://devpost.com/software/kiro-s-halloween-night"
title: "Kiro's Halloween Night"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 474
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# Kiro's Halloween Night

> A gentle roguelike game set on Halloween night starring Kiro

[Devpost](https://devpost.com/software/kiro-s-halloween-night) · hackathon [[Code with Kiro Hackathon]]

## Facets


**stack** dart, flutter, fluttergpu, macos, metal

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kiro's halloween night

## Body

Story Give them sweets to make them your allies Peaceful combat Inspiration First of all, since this was a Kiro hackathon, We wanted to create a game with Kiro as the main character. Ghosts are synonymous with Halloween, but we came up with the idea for a gentle game where you give children candy instead of scaring them, and made the genre roguelike! What it does As mentioned earlier, this game is a roguelike. Controls are via the arrow keys and "i" (inverted arrow key). As with a typical roguelike, you move with the arrow keys, and pressing the arrow keys towards enemies will deal damage (but only peaceful damage). You can use candy you've picked up with the "i" key, or you can give it to enemies if they're nearby. Giving candy will turn enemies into your allies. Finally, you must scare the Vampire Lord to complete the game. It can be played on macOS by building it with Flutter. Once you have set up Flutter, you can build it by running flutter run -d macOS --release How we built it First, before starting development, I prepared a minimal system for rendering with Flutter GPU. We created a spec in Kiro, then created a task list and implemented them in order. Since the spec is the most important thing in Kiro, we used Claude Opus 4.1 via Cloude Code for the difficult implementation. Challenges we ran into It was difficult to make the gameplay entertaining and engaging. In fact, this is the third game I've made for this hackathon. I've quit the project twice. Accomplishments that we're proud of Taking the time to carefully develop and refine our game specifications made the game significantly more fun. For instance, the candy-giving mechanic was originally just a hidden easter egg that didn't add to the gameplay experience. However, when we revisited this during the design documentation phase, we transformed it into a core mechanic where giving candy to enemies converts them into allies. This change became the heart of what makes our game engaging. What we learned We learned the importance of specification-driven development in game development, especially when working with AI coding assistants. Previously, we had only created games that ran on a single logic system, which made AI coding straightforward. However, the roguelike game we built this time involves various objects and AI behaviors interacting with each other, which seemed to be a very challenging task for AI assistants. For the AI to verify that its implementations were correct, we needed to create detailed specifications and update them as needed during the implementation process. What's next for Kiro's Halloween Night We kept the game systems minimal to meet the hackathon deadline, but we'd love to expand the features and release a fuller version. Of course, we'll continue using specification-driven development with Kiro. <div