---
slug: "sublimealgo"
url: "https://devpost.com/software/sublimealgo"
title: "SublimeAlgo"
hackathon: "OpenD/I: Shaping Data & Infrastructure for the next 10-20 Years"
organization: "Openmesh Network"
winner: true
words: 331
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
---

# SublimeAlgo

> SublimeAlgo is an anonymous, distributed, and decentralized computation system using advanced genetic algorithms to find novel neural architectures.

[Devpost](https://devpost.com/software/sublimealgo) · hackathon [[OpenD-I- Shaping Data - Infrastructure for the next 10-20 Years]]

## Facets

  <sub>weak: code_repository</sub>

**stack** fastapi, mongodb, python, pytorch, tor

## Body

I want to find better neural network architectures, focusing on smaller scale models that can be tested quickly and improved rapidly. I believe the best way forward for this is with genetic algorithms, and scaling the solution out to many machines computing the required fitness functions. The HyperCycle challenge at this hackathon lined up with my vision, so I decided to put things into practice and submit a project to this hackathon. There were some challenges to getting things finished since I wanted to highlight the potential of this approach, but some ideas were slowing me down. In the process however, I was able to invent what I believe is a new and very powerful genetic algorithm, so I focused the last few days of the hackathon on that task and finished writing the documentation. My laptop mic also broke, and I was not able to fix it, so I had to resort to using TTS for the presentation video, though I think that worked out well in the end. The core of the project is built in python with a server-client architecture. The server handles the genetic reproduction, while the clients handle the calculation of the fitness functions. A big feature of this system is that it is designed to work with the Tor network, and provide anonymity to the server and clients. This requires that the system defend against malicious attacks, so much of the early days of the hackathon were dedicated to making it robust against such attack vectors. By the end of the hackathon, I had created some genetic algorithms that reproduced classic results and features in deep learning, and created the aforementioned GA*, or GAS algorithm, which is explained in more detail in my presentation and source code. The next steps are to phrase the phenotype encoding to be able to express more complex neural architectures, to improve the GAS algorithm (making it more adaptive), and then pushing it out to a large computational network. <div