---
slug: "split-sketch"
url: "https://devpost.com/software/split-sketch"
title: "Split Sketch"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 1355
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/civic_government"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Split Sketch

> A fast, two-player drawing game where one player selects a word draws half of it, the other completes the drawing blind, and the community guesses the word.

[Devpost](https://devpost.com/software/split-sketch) · hackathon [[Fun and Games with Devvit Web]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[civic_government]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]]

**stack** devvit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for split sketch
- acknowledgments

## Body

Game Post Word Selection Canvas Random Split First Player's Half Drawing Area First Player's Half Complete Drawing Submission Post Second Player's finish The Drawing Post Second Player's Half Drawing Complete Drawing Ready For Community Complete Drawing Post Community Guess Post Community Guess Community Results Inspiration The idea for Split Sketch came from playing Split Fiction, a collaborative storytelling game that sparked something in me about the magic of creative collaboration between strangers. I was fascinated by how two people who had never met could create something together that neither could have imagined alone. I wanted to explore this concept through visual art. I kept thinking: what if you could only see half of what someone else drew, and had to complete it without knowing what they intended? The uncertainty, the creative interpretation, the surprise of seeing the final result - it felt like the perfect recipe for both hilarity and genuine artistic moments. Reddit's community-driven nature seemed like the ideal platform to bring this vision to life. What it does Split Sketch is a collaborative drawing game built for Reddit communities using the Devvit platform. The game works in three phases: Phase 1 - The Setup : A player chooses a secret word from three options and gets randomly assigned the canvas split (vertically or horizontally). They then have 60 seconds to draw their half, focusing on the most recognizable features of their chosen word. Phase 2 - The Collaboration : A second player sees only the first half of the drawing and has 60 seconds to complete the other side. They have no idea what the original word was - they can only interpret what they see and try to create something cohesive. Phase 3 - The Community : The completed artwork is revealed to the community, who then try to guess what the original word was. Both players earn points for every correct guess, encouraging them to work together effectively despite never communicating directly. How we built it The architecture consists of three main layers: Frontend Canvas System : The canvas handles real-time drawing with smooth brush strokes, color mixing, and responsive touch controls for mobile devices. The split-screen functionality required careful coordinate mapping to ensure drawings aligned properly when combined. State Management : The game flow required complex state management across multiple Reddit posts. I implemented a system where each phase creates a new post type - initial drawing posts, "finish this drawing" posts, and "guess the drawing" posts. Each post carries forward the necessary data while hiding sensitive information (like the secret word) from players who shouldn't see it. Backend API : Using Express.js, I created a RESTful API that handles drawing data persistence, user authentication through Reddit's context system, and score tracking. The server manages the transition between game phases and ensures data integrity across the collaborative process. I implemented custom post types, menu actions for moderators, and proper flair systems to help organize game content within the subreddit. Challenges we ran into State Persistence : Managing game state across multiple Reddit posts while keeping sensitive data secure was complex. I had to design a system where the secret word travels with the data but remains hidden from the second player, while ensuring the community can verify correct guesses later. Image Optimization : The original logo and drawing assets were causing slow load times, especially on mobile connections. I implemented a comprehensive image optimization strategy, creating multiple sizes for responsive loading and adding preload hints to improve perceived performance. Accomplishments that we're proud of Community Driven : I think I understand what drives community driven games. If the game is in the feed, it will draw more user engagement. If there is too many screens or steps it will create churn. I tried my best to make sure it was all in line and immersive mode which did not interfere to much with the user's reddit feed. I also learned test users on what they wanted and what they needed. What we learned User Experience Design : Building for a community platform taught me the importance of designing for both individual users and group dynamics. The game needed to be engaging for players while creating shareable moments for the broader community. Performance Matters : Even small delays in drawing responsiveness or image loading significantly impact user engagement. I learned to prioritize performance optimization from the beginning rather than treating it as an afterthought. Platform Constraints Drive Creativity : Working within Devvit's limitations forced me to find creative solutions that often ended up being better than my original ideas. The post-based game flow, for instance, creates natural sharing moments that wouldn't exist in a traditional web app. Community Feedback Integration : Building for Reddit meant constant community feedback during development. This taught me to iterate quickly and prioritize features that actually enhance the collaborative experience over technical complexity. What's next for Split Sketch Advanced Drawing Tools : I plan to add more sophisticated drawing features like layers, shape tools, and texture brushes while maintaining the simplicity that makes the game accessible. Tournament Mode : A structured competition system where communities can run drawing tournaments with brackets, eliminations, and prizes. Theme Challenges : Special events with themed word lists (holidays, pop culture, community-specific topics) to keep the content fresh and relevant. The goal is to evolve Split Sketch into a platform that not only entertains but actively strengthens Reddit communities through shared creative experiences. Acknowledgments While the core game mechanics, and backend systems are completely original, I've incorporated some excellent open source UI components to enhance the visual experience: Wheel of Doom Visual Components : Original spinning wheel mechanics and Grim Reaper SVG artwork by Ryan Mulligan Used under MIT License for the visual foundation of our interactive wheel system I've extensively modified and integrated these components with our custom game logic, Redis state management, and Reddit API integration Special thanks to Jesper Hills for the beautiful button styling from their open source CodePen ( https://codepen.io/nopr/pen/kxZQvE ), which helped give Split Sketch its polished visual appeal. Button Styling License Copyright (c) 2025 by Jesper Hills (https://codepen.io/nopr/pen/kxZQvE) Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. Wheel of Doom License Copyright (c) 2025 by Ryan Mulligan (https://codepen.io/hexagoncircle/pen/bGqVyxm) Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. <div