---
slug: "jsinrust-nearopenai"
url: "https://devpost.com/software/jsinrust-nearopenai"
title: "JSinRust+NearOpenAI"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 307
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# JSinRust+NearOpenAI

> Initiated by a tweet challenge in 2022 for combining Rust and Javascript layer for customising smart contracts. How to take this further and combine with OpenAI APIs.

[Devpost](https://devpost.com/software/jsinrust-nearopenai) · hackathon [[-REDACTED- Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**substrate** [[code_repository]]

**stack** c, emscripten, quickjs, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for jsinrust+nearopenai

## Body

Inspiration The project was initiated by this tweet in 2022 https://x.com/ilblackdragon/status/1561368373618941954 , but also from my own idea of providing a Javascript runtime into smart contracts. My WebAssembly Music project is based on creating music in Javascript, and so I wanted to create music in the smart contracts too. What it does Today I have Rust implementations of NFT, web4 and Fungible Token contracts that can be customised with Javascript. The NFT contract has several deployments, including https://webassemblymusic.near.page , and also AI generated NFTs on BOS: https://near.social/petersalomonsen.near/widget/GPTMinter How we built it The Javascript runtime is QuickJS, written in C, and compiled to WebAssembly using Emscripten. It's linked into the Rust standard contracts and there is also the connections between the Rust NEAR environment and the Javascript runtime. It is all in this repository here: https://github.com/petersalomonsen/quickjs-rust-near Challenges we ran into Challenges that are solved is being able to run tests inside a Wasm runtime. Compiling QuickJS and embedding it into a Rust NEAR smart contract is a challenge in itself. Also getting the smart contract size down to something that is deployable was hard. Accomplishments that we're proud of Proud of being able to solve the challenges, and to provide a codebase with comprehensive automated test coverage. What we learned It has been a raise of knowledge and skills in combining C, Rust and Javascript, and understanding NEAR. What's next for JSinRust+NearOpenAI Improve documentation, add more NEAR interfaces to the Javascript runtime, create more examples. Also currently in the process of using the Fungible Token for charging requests to OpenAI APIs, providing a mechanism for paying an amount up front for the conversation, and refund what is not spent when the conversation is finished. This makes it possible for the end user not having to commit to a monthly subscription, but only pay for the AI usage. <div