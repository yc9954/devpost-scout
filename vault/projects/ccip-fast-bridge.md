---
slug: "ccip-fast-bridge"
url: "https://devpost.com/software/ccip-fast-bridge"
title: "Chronomancer"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 600
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# Chronomancer

> Fast, Chainlink CCIP-backed transfers bypassing time-to-finality using a smart contract endpoint and order-filling bot

[Devpost](https://devpost.com/software/ccip-fast-bridge) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**substrate** [[geospatial]]

**stack** ethers-rs, godot, godot-rust, remix, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for chronomancer

## Body

Inspiration CCIP offers best-in-class security for cross-chain transfers, but source chains with long time to finality are slow to reach settlement. I wanted to solve this problem by creating a flexible fast transfer solution that preserves the security properties of CCIP. I also wanted the solution to work with existing tokens, while remaining as frictionless, accessible, and adaptable as possible. Chronomancer is available for MacOS, Ubuntu, and Windows. Download it here to try it out! What it does Chronomancer scans for outgoing CCIP messages on a source chain and provides instant token transfers on the destination chain. It has two components: a smart contract endpoint and an order-filling bot. The bot works by monitoring CCIP OnRamp contracts and filtering EVM2EVM messages using criteria set by the user. It can copy selected messages and forward them to the endpoint on any destination chain, transferring tokens to the intended recipient (and data, if the recipient is a contract). This transfer will be tracked by a mapping on the endpoint contract. Transfers are tracked by their "order path", which is the sequence of identifiers unique to every CCIP message. When the in-flight CCIP message eventually arrives at the endpoint, it will check whether its unique order path has been filled. If it has, it will transfer tokens to whichever address filled the order. If not, it will instead send the tokens to their intended recipient. Any sent CCIP message is compatible with Chronomancer as long as message.receiver is set to the endpoint contract, and message.data includes the intended recipient address and some bytes (which can contain any arbitrary data). How we built it The application was built using Godot, which provides the user interface and handles all HTTP requests to RPC nodes. Via Godot Rust, Ethers-rs is used to sign calldata and decode RPC responses. I used Remix to write and deploy contracts. Accomplishments that we're proud of My goal was to make a system that was easy to understand and use, because I believe a fast transfer framework will be much more viable if many people are providing liquidity. As a proof of concept, I'm very happy with the look and performance of the bot, and I think it will make complex cross-chain operations accessible to more people. On top of making a cool bot, I also majorly revamped my "Godot Ethers" code. "Ethers.gd" is a global singleton that can be accessed from any Godot node. It creates an HTTPRequest on demand, which after querying an RPC node will call back to a user-defined function on a user-defined Godot node. This is both convenient and much cleaner to use. I also reorganized my Rust library and included common type conversions and operations, which should make it easier to read and build with. What we learned I learned more about how CCIP works, and how I can use the onramp contracts and EVM2EVM messages to easily pull CCIP activity data. What's next for Chronomancer This was my first attempt to create a "crypto infrastructure app" with the goal of allowing people to easily provide a service to others or supplement their dApp's functionality. I can see ways in which Chronomancer could be improved: multiple signers, additional networks, more customization, perhaps a headless mode if people would prefer to run the configured bot as a process without the UI. It would be good to have feedback to know what kind of features people want most from these kinds of applications. I'm also curious if there are other applications or tools that would be suited to the same visual approach that I've applied here. <div