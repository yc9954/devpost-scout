---
slug: "the-crooked-tankard"
url: "https://devpost.com/software/the-crooked-tankard"
title: "The Crooked Tankard"
hackathon: "Google Chrome Built-in AI Challenge"
organization: "Google"
winner: true
words: 621
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/code_repository"
---

# The Crooked Tankard

> A text-based adventure game on the web, powered by built-in AI

[Devpost](https://devpost.com/software/the-crooked-tankard) · hackathon [[Google Chrome Built-in AI Challenge]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[code_repository]]
  <sub>weak: video_visual</sub>

**stack** iconify, node.js, npm, react, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the crooked tankard

## Body

A screenshot of the game (supports dark / light mode) Hovering on things gives you detailed information The AI narrates each turn of the game based on the events of that turn NPCs offer random quests, which are phrased by the AI You can also trade with the NPCs, and the AI will generate their response message Items before AI content generation Items after AI content generation AI-generated location names on a village street Inspiration I like playing, and I like creating games. The AI provides an opportunity to scale up the diversity of the game world without investing too much energy to do so. It also opens up the possibility of a fully open-ended game, with infinite replayability potential. What it does It is a text-based adventure game. In each turn you decide to do something (your action), and the game simulates the outcome. This simulation, and the capabilities of the game logic are fixed. There are many situations controlled by RNG, and many others where AI is involved in the decision making process. The AI is also used to populate the pre-generated game world with concrete names and descriptions, and to narrate the events that occur in each round. How we built it We used React, Tailwind and @iconify/react to create the application. We have created an NPM mono-repository, which holds the skeleton for our apps. This makes it easier to experiment with creating different apps. In the react app, we have the useLanguageModel hook, which provides access to the currently selected language model settings. This abstracts the window.ai.languageModel , but it is also used to give access to GCP models (Gemini Flash, Gemini Flash 8B, Gemini Pro). This allows quick and easy comparison of the models, but it was also handy to allow collecting prompts for the smaller model. Challenges we ran into There are a couple of challenges, that we needed to work around in some way or another: Prompt API does not allow returning any text other than English. But, its way of detecting whether it is speaking english or not is a bit bugged. Sometimes short english answers are flagged as non-english, and out retry loops could easily be trapped in an infinite loop. This can be worked around by forcing the model in the prompts to use a longer english prefix, like "I propose the following name: ". Parallel requests can crash the entire AI API layer. If I continously try to send many requests to the AI in parallel (with different AILanguageModel instances), the AI layer crashes, and can no longer accept any requests, until the page is reloaded. Reloading the page fixes the problem, but this is what caused the birth of GlobalScheduledBuiltinLanguageModel , which schedules messages globally to run in series. Accomplishments that we're proud of We have created something, that is very entertaining to play around with :D What we learned The most important thing we learned was how to work around "intelligence issues" of an underlying AI model in a game. We know for sure, that higher capacity models can easily solve some of the tasks we tried, but breaking these down into concrete algorithm parts , and integrating the AI into these smaller parts is a methodical approach, that needs practicing. This gave us a very good opportunity to practice this. What's next for The Crooked Tankard We would like to make the game world richer. Also open it up for modding. Once Electron is shipped with the AI model, we want to create an installable Desktop version of the game. The same applies for Android / iOS web views: once the window.ai API becomes available there, we would consider creating App Store versions of the game. <div