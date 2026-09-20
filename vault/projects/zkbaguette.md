---
slug: "zkbaguette"
url: "https://devpost.com/software/zkbaguette"
title: "ZkBaguette"
hackathon: "Zero-Knowledge Proof Hackathon"
organization: "Bitcoin Association"
winner: true
words: 247
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
---

# ZkBaguette

> A quick and easy way for anyone building a ZK app to reduce *a lot* the fees their user payTo do so, they just have to use my scrypt library instead of the default one provided by scrypt.

[Devpost](https://devpost.com/software/zkbaguette) · hackathon [[Zero-Knowledge Proof Hackathon]]

## Facets


**stack** racket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zkbaguette

## Body

Inspiration I was frustrated by the large size of the zksnark smart contract, probably like everyone else, and believed I could provide an easy to use alternative for everyone building a zk app. What it does The size of the script code is reduced so users pay less fees. With release mode, the verifier is now 1.27MB instead of 5MB With debug mode, the verifier is 1.38MB instead of 9MB I believe the result is impressive and very useful, as a very large portion of each zk smart contracts will be this verifier! [EDIT]: I just tried on one of the submission of this hackaton, zk-minesweeper, and the size of their contracts went from 7 575 932 Bytes to 1 954 015 Bytes when compiled with release. So it works. (With debug it goes from 11 715 614 Bytes to 2 128 335 Bytes). More details at the top of the readme. How we built it It's built with Baguette (and of course scrypt) Challenges we ran into It's quite challenging to be 100% sure that the produced code is correct. Being only 99% sure is not enough! Accomplishments that we're proud of The whole thing. It's easy to use for anyone (just copy/paste 2 scrypt files) and allow anyone to pay less fees. What we learned That I really need to rewrite Baguette in common lisp. Too much technical debt. I also learnt a lot about zk. What's next for ZkBaguette Support other zk primitives. <div