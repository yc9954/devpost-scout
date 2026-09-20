---
slug: "tacult"
url: "https://devpost.com/software/tacult"
title: "Tacult"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 576
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Tacult

> An Alpha-Zero like AI to play Ultimate-Tic-Tac-Toe, complete with customized gym environments, vectorization, batch processing, self-playing data generation, and an arena to test out different agents.

[Devpost](https://devpost.com/software/tacult) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[code_repository]] [[video_visual]]

**stack** c++, flask, python, torch

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges iran into
- accomplishments that i'm proud of
- what i learned
- what's next for tacult

## Body

An example Game AI in training Inspiration My journey into AI game agents started with ambitious dreams of creating a chess engine. While that proved too complex due to computational limitations and the vast domain knowledge required, it led me through various game implementations including Balatro. These experiences ultimately guided me to Ultimate Tic-Tac-Toe, where I could apply both classical game theory algorithms and modern machine learning approaches to create something truly competitive. What it does Tacult is a reinforcement learning agent that masters Ultimate Tic-Tac-Toe through self-play. It competes against other algorithms and human players through the uttt.ai platform, demonstrating remarkable strategic depth despite having no pre-programmed game-specific strategies. How I built it The development process evolved through several stages: Initial implementation of classical game theory algorithms (Minimax, Alpha-Beta Pruning) Transition to reinforcement learning techniques Integration of self-play training methodology Implementation of neural network architecture for policy and value prediction Integration with uttt.ai's platform for testing and deployment Challenges Iran into Overcoming the initial complexity barrier of chess engine development Managing computational resources effectively for training Balancing exploration and exploitation during the learning process Designing an efficient neural network architecture that could capture the game's strategic elements Integrating the trained model with the existing uttt.ai platform Accomplishments that I'm proud of Achieving a remarkable 95% win rate against sophisticated MCTS (Monte Carlo Tree Search) opponents Successfully creating an AI that learned purely through self-play, without human knowledge injection Developing a system that could generalize well across different game situations Successfully transitioning from classical algorithms to modern ML approaches What I learned The importance of choosing the right scope for AI projects Practical implementation of reinforcement learning techniques The power of self-play in training game-playing agents How to effectively integrate ML models with existing platforms The balance between computational resources and algorithm sophistication What's next for Tacult Further optimization of the neural network architecture Exploration of hybrid approaches combining reinforcement learning with classical algorithms Potential expansion to other similar game domains Implementation of an explainable AI component to understand the agent's decision-making Development of a training interface for human players to learn from the AI's strategies Technical details: The project uses a lot of high level optimizations and low level compilations. A list of relevant repositories used: https://github.com/lunathanael/utac https://github.com/lunathanael/utac-gym https://github.com/lunathanael/tacult Starting from utac, the repository is written by me in entirety in C++, it is very fast, because it is C++. However, when you think of 3d tic tac toe, you would image a two-dimension vector of ints. The board representation is actually an array of 9 integers, using bitmasking and perfectly hashes lookup tables to evaluate positions in efficient times. At the next level, utac-gym is a pip installable python package that serves to wrap and deploy the functions written in C++. It uses nanobind - a pybind alternative, to call the low level C++ functions and classes with little to no overhead. This library provides strong typing and a gymnasium compatible class environment. Finally, tacult is the actual repository responsible for the training. It it based on a repository by clean-rl, and implements extensively vectorized NN-MCTS and vectorized Arenas for batch processing. If you want to test it yourself or want more information behind the research and the theory of the actual network, please reach out or leave a comment. I'm unable to fully deploy the AI as there wasn't enough time to fully deploy a browser usable version in a production environment. <div