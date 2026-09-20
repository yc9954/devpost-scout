---
slug: "zk-minesweeper"
url: "https://devpost.com/software/zk-minesweeper"
title: "ZK Minesweeper"
hackathon: "Zero-Knowledge Proof Hackathon"
organization: "Bitcoin Association"
winner: true
words: 147
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# ZK Minesweeper

> Minesweeper on a public blockchain by leveraging ZKP.

[Devpost](https://devpost.com/software/zk-minesweeper) · hackathon [[Zero-Knowledge Proof Hackathon]]

## Facets

  <sub>weak: code_repository</sub>

**stack** react, scrypt, typescript, zokrates

## Body

For the hackathon I've built an implementation of the game Minesweeper that can be played on a public blockchain, namely Bitcoin in my specific case. Because the mine location cannot be revealed publicly, the solution leverages ZK-SNARKS. Once the player picks a mine field, the servers job is to create a proof of whether the selected field actually contains a mine or not. Thanks to Bitcoin predicates the server is commited to the initial mine field configuration so he cannot change it during the game. This ensures the server is honest, so there's minimal trust needed between the player and the server. I've recorded a short elaboration video in which I briefly go over my solution: https://youtu.be/D00WUgdSGTA The code is avaliable on GitHub: https://github.com/msinkec/zk-minesweeper Edit (late submission): I've now also recorded a demonstration of playing a full game on the bitcoin testnet. https://www.youtube.com/watch?v=b5Tp4aLf6Es ~Mihael Šinkec, 2022-12-02 <div