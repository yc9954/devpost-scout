---
slug: "erc-20-erc-721-token-minter-gui"
url: "https://devpost.com/software/erc-20-erc-721-token-minter-gui"
title: "ERC-20 + ERC-721 Token Minter Gui"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 432
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# ERC-20 + ERC-721 Token Minter Gui

> Gui that can apply filters to images and mint them into NFT's. The user will also get from 1 - 15 ERC-20 tokens for using this service.

[Devpost](https://devpost.com/software/erc-20-erc-721-token-minter-gui) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**substrate** [[video_visual]]

**stack** brownie, chainlink, ethereum, opencv, openzeppelin, pyqt5, python, solidity

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for erc-20 + erc-721 token minter gui

## Body

Inspiration I find that the best way to learn is to just dive in. So that is what I tried to do. What it does This project aims to give users an all in one NFT creation experience, and is comprised of two smart contracts. The first is an NFT Factory contract. The second contract is a basic ERC-20 token contract that incentivizes users to mint their NFT's through this program. Using the gui included as part of the GitHub repo, users are able to select any .PNG or .JPG images from local storage, apply basic style filters, give a name and description, and mint it onto an Ethereum network. When a user mints an NFT, they will also be awarded from 1 and 15 ERC-20 tokens for minting their NFT through this projects ERC-721 contract. When an NFT created on this platform sells, a small fee will be applied. A Chainlink VRF was used to generate the randomness for deciding how many ERC-20 tokens are given to the user for minting an NFT. This project is still in it's infancy, so no smart contracts exist on-chain, however, both contracts are provided in the repo, and can be deployed to test the gui's functionality. See video. How I built it 1) For the gui, I used PyQt Designer along with python to program the functionality. 2) For the image styling, I used python's OpenCv library. 3) For the smart contracts, I used Solidity with brownie and depended upon OpenZeppelin contracts. Challenges I ran into The main challenge for me was learning the technology as a whole. For the last seven months, I have been teaching myself how to program, so I am relatively new to the space in general. This made learning about blockchain programming tough, yet exceedingly interesting and fun. In addition, up until the start of this hackathon, I was only learning Javascript with Truffle, so moving to Python and brownie was a real change. Accomplishments that I'm proud of As stated above, I am self teaching, and pretty new to programming in general so just finishing a big project (for me) is incredibly motivating. What I learned To persevere through frustration. What's next for ERC-20 + ERC-721 Token Minter Gui After completely optimizing and refactoring a lot of the code, I want to make this into an app where users can snap a picture, apply a style, and mint it as an NFT. The size of the photo would be the same dimensions of Instagram photos too. I want to learn so much more about so much more. <div