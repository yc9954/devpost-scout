---
slug: "random-beacon"
url: "https://devpost.com/software/random-beacon"
title: "Verifiable Random Beacon"
hackathon: "Building Privacy in Web3 - Powered by Partisia's MPC"
organization: "Partisia Blockchain Foundation"
winner: true
words: 528
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
---

# Verifiable Random Beacon

> A verifiable compute random beacon which can be used across various applications and blockchains using attested results.

[Devpost](https://devpost.com/software/random-beacon) · hackathon [[Building Privacy in Web3 - Powered by Partisia-s MPC]]

## Facets

**mechanism** [[provenance_signing]]

**stack** partisia, react, rust, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for random beacon

## Body

Inspiration I was looking for verifiable random numbers which can be used in nft raffles/dice games etc. There are options like chainlink VRNG generators but it works for only blockchains which are supported by chainlink. With partisia, verifiable computation is available along with option of secret multi party computation which gave an idea for counter based pseudo random number generator. What it does This application helps generate a set of unbiased verifiable random numbers in specific range. So the result can be used in other blockchains/applications and verified if result is tampered or not. How we built it To make random numbers unpredictable, there is need of a secret seed. With partisia we get the feature of secret multi party computations which can be used to operate (sum/substract/multiply etc) on values to generate a secret seed. So with a secret seed and public counter, we can create counter based Pseudo random numbers which can be difficult to predict if there is at least a single honest party in initial ceremony to generate secret seed. With a secret seed, we can not store a public counter in contract state and increment everytime a new random number is generated. Challenges we ran into As I was new to random number generators, it took some time to understand different kind of pseudo random number generators. For my use case, I needed a partial secret state and public state which can help in generating random numbers. I came across counter based PRNGs. In Counter based PRNGs, I tried out squaremax and philox but finally found threefry suited my requirements. With threefry we can have a secret seed which does not need to change and a public counter which can keep on increasing. Finding threefry implementation and porting it to rust took sometime. One more challenge was how to store secret seed as there is no secret state in Partisia. Only secret computations are there. After some thought, it made sense to generate secret seed on the fly every time with the zk inputs stored in contract state using SecretMetadata field One more issue which I faced was that I wanted to send keccak256 hash as input which can be attested by zk nodes so that the result can be uniquely verified. To send 32bytes signature input in zk function, I had to divide it into 2 Sbi128 or 4 Sbi64 but then faced issues with 3 other inputs of Sbi64, Sbi64 and Sbi8. Finally got it working by sending a signature as 4 Sbi64 inputs, Sbi8 input as count and Sbi64 input which can have start and end range of 2^58 size. Accomplishments that we're proud of Creating a verifiable pseudo random number generator and understanding MPC in short span of time What we learned Understanding Secret MPC and how they work. It opens up possibilities for variety of new applications of using verifiable secret computations Understanding and implement a verifiable Counter based PRNG What's next for Random Beacon This can be used in variety of board/card games where we need random input in PvE and PvP games. Planning on creating a simple board game which uses output of this application <div