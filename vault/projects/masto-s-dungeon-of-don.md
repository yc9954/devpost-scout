---
slug: "masto-s-dungeon-of-don"
url: "https://devpost.com/software/masto-s-dungeon-of-don"
title: "Masto's Dungeon of Don"
hackathon: "Pygames"
organization: "Microsoft"
winner: true
words: 439
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Masto's Dungeon of Don

> Our Python text-based RPG game brings all the excitement of Dungeons and Dragons! With a rich fantasy world to explore, a variety of enemies to defeat using Mastodon.

[Devpost](https://devpost.com/software/masto-s-dungeon-of-don) · hackathon [[Pygames]]

## Facets


**stack** expressions, mastodon, mastodon.py, os, python, regular, time

## How they structured the write-up

- inspiration
- what i learned
- how i built it
- challenges faced

## Body

Masto's Dungeon of Don Mastos Dungeon of Don: A Python-based Text RPG on Mastodon Inspiration Mastos Dungeon of Don was inspired by the desire to create an engaging, community-driven text RPG experience on the Mastodon platform. As a federated social network, Mastodon encourages interaction and creativity. Building a text-based game that utilizes Mastodon's features allows users to participate in an exciting adventure while interacting with other players on the platform. What I learned Developing this project provided valuable experience in working with the Mastodon API and the Python programming language. The project required a solid understanding of the API's capabilities and how to communicate with it effectively. This led to learning about API rate limits, authentication, and efficient request handling. Additionally, creating this game involved designing and implementing the game's mechanics, such as character creation, combat, and game state management. This required a deep understanding of object-oriented programming and data structures in Python, as well as the ability to manage complex game state changes and user interactions. How I built it The game is built using Python and the Mastodon.py library, which offers a convenient wrapper around the Mastodon API. The game logic is centered around the Character and Monster classes, which represent the player characters and enemies, respectively. The main game loop is implemented in the handle_mentions function, which constantly polls for new mentions on the Mastodon platform. When a user issues a command, the game processes the command and updates the game state accordingly. The game utilizes regular expressions to parse user input and perform the appropriate actions. To store the game state, the application maintains a dictionary of active players, keyed by their Mastodon account name. The game state is also persisted using a simple text file, allowing the game to continue across sessions. Challenges faced One of the primary challenges in developing this game was handling user input and ensuring that the game processes each command only once. This required careful management of the game state and the creation of a system that tracks which commands have been processed in each batch of mentions. Another challenge was designing a game that is engaging and fun for players, while also being simple enough to be played through Mastodon's text-based interface. This required striking a balance between depth and simplicity in the game's mechanics, and ensuring that the game remains accessible to a wide range of users. Overall, creating Mastos Dungeon of Don provided valuable experience in working with APIs, designing text-based games, and managing user interactions. It serves as a unique example of how the Mastodon platform can be used to create innovative, community-driven experiences. <div