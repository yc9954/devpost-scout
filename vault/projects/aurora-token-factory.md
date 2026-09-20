---
slug: "aurora-token-factory"
url: "https://devpost.com/software/aurora-token-factory"
title: "Aurora Token Factory"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 365
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
---

# Aurora Token Factory

> Aurora Token Factory is a dApp that provides an easy way to create ERC-20 tokens and interact with its contracts in the Aurora network.

[Devpost](https://devpost.com/software/aurora-token-factory) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**substrate** [[code_repository]]

**stack** react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what i learned
- what's next for aurora token factory

## Body

Home Token creation Token interaction (search) Token interaction (result) Inspiration I found inspiration in this projects for different networks: https://cointool.app/createToken/eth https://vittominacori.github.io/erc20-generator/create-token/ https://www.createmytoken.com/token-builder/ What it does Allows to create personalized ERC-20 tokens through a easy-to-use user interface, for people that are not familiarized with programming. Shows information of an existing ERC-20 token, given its contract address. Interacts with the smart contract directly from the dApp. How I built it I used Remix to create an ERC-20 token template. I compiled it and copied the ABI, bytecode and flattened source code so that I can use them in the dApp. I created a React application to interact with the Aurora network in order to deploy the ERC-20 contract with the parameters provided by the user and interact with an existing contract in the blockchain. Challenges I ran into I created a functionality to verify a contract after its creation, however I wasn't able to get it work in a reliable manner. I am not sure if the problem comes from the API itself or by the way I am trying to do it. Sometimes it works, especially when testing with very simple contracts, but not always. The idea was to provide different types of smart contracts and get the ABI directly from the API, so that the interaction form is created dynamically. This is the way it is created right now, however I am using always the template ABI, so only interaction with ERC-20 tokens is supported. Accomplishments that we're proud of I managed to create my first React app (I usually work with Angular) and one of my first interaction with Solidity (I had only played a bit with it), and I think I created a good product for a first timer. What I learned How to use React. How to deploy a smart contract from a web client. How to interact directly with the ABI in order to get its function data. What's next for Aurora Token Factory Solve the issue with the contract verification feature. Allow interaction with different types of smart contracts. Add more configuration parameters to the ERC-20 token creation. Add support for the creation of more standards (ERC-721, ERC-1155, etc.). <div