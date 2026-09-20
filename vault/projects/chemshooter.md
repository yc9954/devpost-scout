---
slug: "chemshooter"
url: "https://devpost.com/software/chemshooter"
title: "ChemShooter"
hackathon: "Hack the Northeast"
winner: true
words: 1369
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ChemShooter

> Engaging youth with chemistry through a 2D RPG.

[Devpost](https://devpost.com/software/chemshooter) · hackathon [[Hack the Northeast]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** arcore, blender, css, echoar, html, javascript, phaser.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chemshooter

## Body

The main menu screen Floor one: Where the enemies are easily defeated and the map is small. The enemies drop elements which the user collects. Floor two: The room is a bit harder: the map is bigger and the enemies receive more health. Enemies dropping Hydrogen. The periodic table as well as the sidebar with details about the selected element. The game over screen when you run out of health. Viewing the atom using Augmented Reality. Inspiration In this day and age, video games have a lot of influence over youth. However, they're not all necessarily built for positive influence, and many people associate video games with being detrimental to a successful future. However, we see many video games that are trying to change this perception, with games such as Prodigy and CodeCombat incorporating video games into a motivating experience that teaches and gets younger kids interested in their respective topics. For example, we've seen CodeCombat introduce many kids to programming; a topic they likely wouldn't have touched if it weren't for CodeCombat presenting itself as a fun, enjoyable video game that also helps teach coding. Inspired by these educational video games, we decided that we would like to create a game associated with introducing and teaching youth about chemistry. As high school students, we know that chemistry has the potential to become an interesting topic, especially with all the cool science videos and other chemistry-related topics that seem like magic to younger kids. That's where the idea for ChemShooter comes in. What it does ChemShooter is a 2D RPG that incorporates many aspects of chemistry into its gameplay. You control a cute lizard scientist, who roams around a dungeon with the ability to spit fireballs at enemies. When the enemies die, they drop elements that the lizard collects. Currently, these elements only act as collectables, but in the future we hope to integrate some form of crafting where you can use these elements to unlock upgrades, better weapons, et cetera. Currently, the game only has an endless mode, where you try to go as deep into the dungeon as you can without losing, with the enemies becoming more powerful as well as the map expanding with each level you go down. If you press the pause button, you're brought to a screen where you can view a mini periodic table. The more tinted an element is, the more of that element you've collected. When you click on one of these elements, you can see information about the element pop up to the right of the game. There, you can get an overview of the element, and learn more about chemistry while you play. You'll also notice a ChemCode to the right. This is a picture that, when scanned using your mobile phone on a certain website , will bring up a model of an atom in Augmented Reality, where you can explore it in 3D with the camera on your phone. When you run out of health, the game is over and you are presented with a screen that shows your final score, and your poor lizard with a broken flask. Not to worry, though! You still have the chance to redeem yourself by playing again and attempting to beat your high score. You can also take a break and read more about each element in the pause screen, or explore chemistry with our AR model. ChemShooter is more than just a normal RPG, and we hope that many youth will benefit and gain a newfound interest in chemistry from playing our game! How we built it The game was built with Phaser , which is a Game Development Framework built using JavaScript. This allowed us to easily integrate the game into a webpage, and since it was regular JavaScript, we were able to even manipulate parts of the webpage outside of the game, such as the sidebar you see to the right. For the AR component of the app, we used echoAR to host the 3D models and to make them easily accessible, and we used Blender to create them. Challenges we ran into At the beginning, none of us were familiar with game development. We had never built big games before, especially not using JavaScript. One of our teammates once heard about Phaser, and was somewhat interested about learning it in the past, but never got around to it. After hearing about the Gaming track for Hack the Northeast, we decided to challenge ourselves and use something that none of us had ever used before. We challenged ourselves to build a game in under 2 days, from scratch, both in the code and knowledge. Our teammate also struggled while building the AR side of the app, such as running out of API calls and many issues with exporting Blender 3D models. In the end though, he was able to get it working and had sifted through much of the documentation and online forums to find the solution to his problem. We started out by reading up on Phaser tutorials. Luckily, Phaser was decently popular and so there were a lot of helpful tutorials that helped us understand the basics and the fundamentals. We read tutorials for the whole first day, and we followed along and built the games that the tutorial guided us through. We were worried that we wouldn't have enough time to finish our game in the remaining 2 days. However, on the start of the second day, when we started building our game, we realized that Phaser was really powerful and could do a lot with few lines of code. Unfortunately, the docs were somewhat lacking and it was hard to find documentation for many problems we encountered. Luckily, the developers of Phaser put a lot of importance on building tutorials and providing code snippets, which we heavily depended on for finding out how to perform certain actions with Phaser. Accomplishments that we're proud of Considering that we went into this hackathon with low expectations (as we couldn't imagine ourselves building a working game in only 36 hours), we were really proud of our final result. We stepped up to the challenge and pushed our limits, and we were pleasantly surprised at our end result. Although there were a lot of features that we didn't get to adding, we ended up creating a game that incorporated a lot of the original ideas. Creating a working game in so short of a time frame was truly a great accomplishment for us. What we learned Coming into the hackathon with no prior game development experience, we've learned so much over the past 36 hours. Thanks to many tutorials and code snippets, we were able to grasp a good understanding of what Phaser can do for our game. We learned new concepts related to game development, such as tilesets, tilemaps, and spritesheets. As well, our teammate also learned a lot about building 3D models with Blender. He learned about uploading 3D models, integrating echoAR into our app, as well as using ARCore to create cool things like the custom ChemCode you see to the right of our game. What's next for ChemShooter ChemShooter originated as an idea for memorizing the elements of the periodic table by playing a video game. Once being a fan of playing first-person shooters, I noticed that there were a myriad of weapons in these games, each with their own unique stats. I thought about how the periodic table seemed to mirror the vast amount of weapons with their own unique characteristics, and imagined a game where you could have weapons that represented these elements and mirror some of the element's real traits (e.g. damage would be equal to atomic weight, recoil equal to melting point, etc.). Now that we've become somewhat familiar with 2D game development, this idea of a first-person shooter now becomes more than just a distant possibility. We hope to take the ideas and concepts that we learned from building 2D ChemShooter and extend it into a 3D game sometime in the future. Links Online web app (game): https://chemshooter.herokuapp.com/ EchoAR web app (for scanning the ChemCode): https://chemshooter.github.io Github Repo (game): https://github.com/ChemShooter/ChemShooter Github Repo (EchoAR web app): https://github.com/ChemShooter/AR.js <div