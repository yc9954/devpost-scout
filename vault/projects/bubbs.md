---
slug: "bubbs"
url: "https://devpost.com/software/bubbs"
title: "Bubbs"
hackathon: "XR Design Challenge"
organization: "immersive insiders"
winner: true
words: 547
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "user/educator_student"
---

# Bubbs

> Bubbs is a bubble-inspired, dynamic MR to-do list app that makes productivity fun and interactive, bringing our childhood highs of popping bubbles to your daily tasks.

[Devpost](https://devpost.com/software/bubbs) · hackathon [[XR Design Challenge]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[developer_tools]]
**user** [[educator_student]]

**stack** c#, fcpx, figma, metacoresdk, mxinksdk, openxr, shadergraphs, unity, unityphysics, xritk

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what we learned
- what's next for bubbs

## Body

Bubbs: A Bubble-Inspired MR To-Do List App Inspiration Most of us can recall a childhood high of popping all the bubbles at the park, hundreds of them, the big tube-like ones—it was a good time. I wanted to channel that kind of fun and vibrance into our grown-up day-to-day tasks and productivity by making this interactive and dynamic MR to-do list app. Plus, it motivates you to get work done so that you can pop the bubbles! What it does In Bubbs tasks and to-do items are represented as bubbles. Using the Logitech MX Ink, users can: Start a tutorial to learn the how-to's of the app. Create, organize, and visually interact with their tasks bubbles. Save, load, and carry around bubbles. Pop the bubbles once the task is completed. How I built it I designed and developed Bubbs using: Unity : For building the core interactions, tutorials, and the high fidelity prototypes. Unity Shader Graphs : For technical art on the bubble materials. Meta Core SDK : To integrate passthrough and MR functionalities. MX Ink SDK : To establish stylus controls and bubble interactions. Physics and Animation : To make bubble interactions, such as capturing and popping, feel realistic and immersive. Figma : For brainstorming and ideating, as well as quick/dirty prototypes to test concepts. UI Design : For creating task management features and tutorial panels that adapt to the user’s environment. Challenges I ran into Making the bubbles look natural and interactive. Originally I used Unity's cloth simulation which gave it a more realistic feel and look but caused some buggy behaviors and performance tradeoffs. It was hard to let go of what looked so good and find other close alternatives! Positional and rotational discrepancies, viewing angles, parenting and spaces (world vs local)—there were puzzles all around. Prioritizing and balancing: functionality? playfulness? Intuitiveness? Accomplishments that I'm proud of Tutorial System: walks through the user with visuals such as the stylus model with highlighted buttons, etc Robustness: I discovered this hackathon opportunity late, so I had a much shorter window to work with. Despite that, I'm proud that I was able to achieve the fidelity and robustness of this MVP. Overall, overcoming the technical barriers of bugs and logic errors, etc—I didn't want to make a design tradeoff for the sake of shortcuts in development. I'm proud to have kept my initial idea and fleshed it out fully! What we learned Prioritization: between technical precision and user experience. Especially in a short duration project like this, it was a huge practice to balance all the difference aspects and goals of the project. Some of the more advanced Unity physics concepts and Vector math. Many victorious headaches(?), and learned to use these concepts along with utilizing different render spaces effectively. What's next for Bubbs Refinement: I want to add animations and hand poses to the tutorial system to make it even more intuitive to learn. The code also needs a lot of cleaning and would like to stylize the visual elements. Platforms: I want to bring this experience to many different platforms, especially the Apple Vision OS. Maybe an opportunity for WebXR to make it completely platform agnostic. Publishing: After refining and planning for future features, I want to publish this app on the Quest store. <div