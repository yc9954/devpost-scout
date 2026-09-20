---
slug: "synsplatt"
url: "https://devpost.com/software/synsplatt"
title: "Mirage"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 233
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
---

# Mirage

> Robots and self-driving cars need training data. Mirage synthesizes 3D world-model training data covering hard-to-capture scenes - like driving in a hailstorm.

[Devpost](https://devpost.com/software/synsplatt) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[simulation_digital_twin]]
  <sub>weak: supply_logistics</sub>

**stack** gpu, modal, python

## How they structured the write-up

- motivation
- what did we do?
- future work (half completed at hackathon)

## Body

"Street with deer in the road "Elephant in the road" "Warehouse with boxes" "TreeHacks venue" Motivation The future of AI-like robots and self-driving cars requires lots and lots of data. Current datasets are extensive, but they cover common senarios, like driving in a sunny or cold day. They overrepresent positive cases and underrepresent edge cases and failure cases, where things could actually go wrong. This leads us to believe that simulations of world models will be key to simulating edge cases, like driving when a tree hits the ground, to train more robust and safe models. Conviction is furthered by Waymo beginning similar research, seen here What did we do? Users will create prompts, such as "Generate a road that had a tree break and fall down on" , a unique scenario that would be unlikely to be present in current datasets, but very valid and important to train a model on. An LLM hosted on Google Cloud will expand the user prompt Veo3 model hosted on Google Cloud will generate a video of the simulated road Modal hosting multiple h100 GPUs will run an open source world model / gaussian splatting algorithm to create a 3d representation of this world Future work (half completed at hackathon) Physics + simulations in 3D generated space Segmentation of objects in 3d representation space (enabling the moving of objects in the space, identification, and training) <div