---
slug: "the-turing-werewolf"
url: "https://devpost.com/software/the-turing-werewolf"
title: "The Turing Werewolf"
hackathon: "Google Chrome Built-in AI Challenge 2025 "
organization: "Google"
winner: true
words: 468
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/civic_government"
  - "user/clinician"
---

# The Turing Werewolf

> The Turing Werewolf turns the classic social deduction game Werewolf into a solo experience powered. Each player you meet is a Chrome Prompt API that debates, and deceives, all running locally.

[Devpost](https://devpost.com/software/the-turing-werewolf) · hackathon [[Google Chrome Built-in AI Challenge 2025]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[civic_government]]
**user** [[clinician]]

**stack** chrome, javascript, react, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the turing werewolf

## Body

The village Inspiration I wanted to see if the built-in AI could make social deduction games playable as a solo player. Werewolf (also known as Mafia) is a perfect example for that, since it is all about deception, deduction, and language. I wanted a human-feeling Werewolf game where the user plays against a room of Chrome AI villagers and werewolves, all running locally in their browser. I also wanted to test if it is possible to create a set of AI that can interact and think humanly under certain constraints. What it does The Turing Werewolf is a client-side web application game where you play as a villager, werewolf or fool. Every other player are AI agents using Chrome's built-in AI that converse, accuse, and vote like humans. Core features: Turn-based conversation : Chrome AI NPCs take turns to speak and reason about suspects. Style Normaliser : your messages can be rewritten into neutral English before being sent, so the AI cannot “meta-read” your grammar or style. Structured reasoning : each agent outputs both public speech and hidden logic (in JSON). Voting system : after discussion, everyone secretly votes to lynch a suspect. Each NPC runs as its cloned Prompt API session with their own prompt: Agent includes the game state and asks for an action (speak/vote/kill). NPC responds with structured JSON. How we built it Tech stack Frontend : JavaScript / React / TailwindCSS AI layer : Chrome’s Prompt API for per-agent reasoning sessions and Rewriter API to provide player with the option neutralise or refine their messages before sending so as to prevent AI agents from detecting personal writing patterns. Local state : XState with persistence Schema Validator : JSON schemas enforced in-browser to keep AI responses consistent API used Prompt API: To build the core gameplay aka the NPCs talking Rewriter API: To allow the player to use neutral English speech Challenges we ran into The LLMs often spoke unnaturally and failed to maintain conversational flow, even with extensive context. Implementing structured turn-taking was necessary to improve realism. Some prompts were ignored, even when explicitly told not to perform certain actions, the models still did. Accomplishments that we're proud of A fully client-side multiplayer : Each game feels different and you can influence the AI based on the messages you send While it is turn based speaking for the AI, it still feels natural as if the conversation is going by. What we learned LLM is fragile unless you give them structure + constraints . Designing multiplayer interactions between multiple Prompt API: I learnt about cloned sessions to provide different memory and persona. What's next for The Turing Werewolf Add new roles: Doctor, Seer. Voice chat mode (STT + TTS) for full immersion. Dynamic turn taking for the AI to decide when to speak <div