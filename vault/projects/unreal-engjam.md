---
slug: "unreal-engjam"
url: "https://devpost.com/software/unreal-engjam"
title: "Unreal EngJam"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 346
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/document_pdf"
---

# Unreal EngJam

> A cursed programming language and game engine inside of Figma.

[Devpost](https://devpost.com/software/unreal-engjam) · hackathon [[Cal Hacks 11.0]]

## Facets

**domain** [[finance_payments]]
**user** [[developer]]
**substrate** [[document_pdf]]

**stack** figma, typescript

## How they structured the write-up

- think of all the benefits
- clippy
- how we built it
- challenges we ran into

## Body

Is that... the start of a 3D engine? Unreal EngJam Design engineers are the latest trend in the tech space, but nobody is talking about engineer designers. We're here to change that. Unreal EngJam (working title) is a concerningly robust, from-scratch programming language and game engine, designed from the ground up to be programmed in a Figma FigJam whiteboard. With our incredibly high quality and extremely spaghetti programming language, you can program such things as classic single-player pong... ... and even render 3D models inside Figma: Think of All the Benefits Why be limited to syntax highlighting when you can color-code your software? Whiteboard out math and algorithms in the same space as your business logic The visual programming appeal of Scratch, with the power and robustness of a real programming language Comments are first-class, graphical, and move around as you refactor (and refactoring is as easy as drag-and-drop) Clippy Make a mistake? Your favorite office assistant will hover above the relevant code and help you out: How We Built It We wrote the programming language entirely from scratch (no dependencies) in TypeScript. We use Figma's plugin API to traverse the document and generate an AST which we can then interpret. We provide the programmer with access to render to and manipulate a "game window" inside Figma. It is important to sufficiently emphasize that this is a full, statically-typed, dynamically-bound novel programming language designed explicitly for the medium of Figma flowcharts. For example, to define a variable you draw a box. To store values, you can draw an arrow to the box, and to read values you draw an arrow from the box. With arrows, nothing needs to be referenced by name and refactoring is easy. The assignment of function and infix operator arguments are inferred first by applied name and then internal type. Challenges We Ran Into Figma runs plugins in WASM which means it is extremely difficult to debug code, and simple bugs like stack overflows often result in cryptic low-level memory leak errors. Also, 3D models are hard to get right :) <div