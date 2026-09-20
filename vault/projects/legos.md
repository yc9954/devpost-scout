---
slug: "legos"
url: "https://devpost.com/software/legos"
title: "LEGOGEN"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 302
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/supply_logistics"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# LEGOGEN

> Create any Lego set you can think of out of whatever Legos you have.

[Devpost](https://devpost.com/software/legos) · hackathon [[NexHacks]]

## Facets

**mechanism** [[vision_ocr]]
  <sub>weak: multi_agent</sub>
**domain** [[supply_logistics]]
**substrate** [[video_visual]] [[web_dom]]

**stack** brickognize, css3, devswarm, fastapi, github, html5, javascript, kaggle, meshyai, node.js, npm, python, svg, trae

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for legogen

## Body

voxel and legos sample input Inspiration Anyone who owns Legos also owns a miscellaneous collection of pieces, a place where Lego are left to collect dust, never to be reunited with their brethren. We decided to provide a use for these forgotten souls, using computer vision, AI tools, and heuristic-guided algorithms to transform them into any given form. What it does Our website inputs a text description and an image of a sprawl of Legos and returns a design with instructions and visualizer of the described Lego set using those Legos. How we built it We built a full-stack application featuring a Vue.js web interface and a Python backend powered by FastAPI. The system simultaneously uses a computer vision model to inventory your bricks from an image and an AI service (Meshy) to generate a 3D model from your text description. Then, a custom algorithm converts that model into a voxel grid and generates step-by-step building instructions tailored to your specific brick collection, using a complex heuristic to guide assembly. Challenges we ran into One challenge we faced was the lack of model and data for identifying bricks, so we had to bring together multiple hand-trained ML models and ML APIs to accurately take inventory of the pieces. Accomplishments that we're proud of We are proud of the algorithm we use to put together the pieces to fill the voxel space. We derived these rules from the base up and learned a lot about optimization and accuracy for complex algorithms. What we learned We learned a lot about dealing with complex situations and how to optimize when the most correct solution is impractical. What's next for LEGOGEN We think there is always more to improve on, especially with our algorithm. We hope to improve our model with a mathematically proven algorithm. <div