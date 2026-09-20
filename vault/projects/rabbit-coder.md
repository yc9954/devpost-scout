---
slug: "rabbit-coder"
url: "https://devpost.com/software/rabbit-coder"
title: "Rabbit Coder"
hackathon: "Facebook Hackathon: AR"
organization: "Facebook"
winner: true
words: 457
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Rabbit Coder

> Rabbit Coder is an augmented reality puzzle game based on programming.

[Devpost](https://devpost.com/software/rabbit-coder) · hackathon [[Facebook Hackathon- AR]]

## Facets

**substrate** [[video_visual]]

**stack** augmented-reality, blender, javascript, spark-ar

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for rabbit coder

## Body

Inspiration I started Rabbit Coder with the intention of creating an AR game that teaches programming concepts in the form of a puzzle game. The idea is to let the user code the movement and rotation of a game character to complete an objective. What it does Rabbit Coder is an AR puzzle game based on coding, it teaches you programming concepts as you play! it was designed with first-time coders in mind, to help them improve their problem-solving skills with logic and puzzles. The game has 10 levels, for now, and it introduces new programming concepts as you progress through the levels, currently, the game helps users learn about the following topics: Sequences. Loops. Boolean logic. How I built it The game was built in Spark AR Studio, I used javascript to write all the game logic and I used the Patch editor to control the camera movements. The script executes a set of commands based on what the user has selected within the game, Spark AR studio does not have the ability to create new game objects, so I had to create a pool of objects game objects that can be reused. Next, I had to design 10 puzzles for the game the first three levels introduce the user to basic sequences, using "FORWARD", "LEFT" and "RIGHT" commands the next three levels introduce the user to boolean logic in these levels we introduce switches that have to be activated in order to get rid of the obstacle, e.g if switch 1 and switch 2 are activated remove the spikes. The last four levels introduce the user to loops with the "Loop" and "End Loop" commands. Below are all the 10 levels currently in the game. To create the 3D models I used MagicaVoxel and Blender. I also downloaded a few free to use 3D assets from Kenney: link . I made the main rabbit character with MagicaVoxel and exported it in .obj format to be used in Spark AR Studio. For the sound effects, I downloaded some free to use audio from FreeSounds: link and converted them to M4A mono format to be used in Spark AR studio Challenges I ran into One of the challenges was creating game objects, Spark AR does not support that at the moment but that was solved by the use of object pooling. Accomplishments that I'm proud of Bringing this idea from concept to a working application is one thing that I'm proud of. What I learned I learned a lot about creating AR effects In Spark AR Studio. What's next for Rabbit Coder Next, I plan to add more complicated puzzles to the game, and also find a way to introduce more programming concepts to the user. <div