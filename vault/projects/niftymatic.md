---
slug: "niftymatic"
url: "https://devpost.com/software/niftymatic"
title: "NiftyMatic"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 442
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# NiftyMatic

> Harness the power of AI to create NFTs instantly on Polygon.

[Devpost](https://devpost.com/software/niftymatic) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**substrate** [[video_visual]]

**stack** docker, ethers, ipfs, node.js, polygon, quicknode, react, stable-diffusion, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for niftymatic

## Body

Bengal cat generated using Stable Diffusion Main interface for generating images Inspiration This project was inspired by the way AIs such as stable diffusion and DALL-E2 are disrupting art. Since chainlink can be used to offload computation-intensive processes that couldn't run under the constraints of the Ethereum Virtual Machine, it was the ideal oracle platform to connect stable diffusion to NFTs on the blockchain. What it does NiftyMatic takes a text prompt describing the kind of image you want to generate, and using a ChainLink external adapter, it sends the request to a Gradio API hosting stable diffusion, renders the image using Stable Diffusion, uploads the resulting image to IPFS, then returns the ipfs link to an ERC721 smart contract, where the link to the image you requested is then stored as an NFT on the Polygon blockchain. It lets you harness the power of AI to generate a unique NFT in any style imaginable! How we built it The infrastructure for managing a chainlink node was containerized using Docker. The middleware external adapter for connecting to stable diffusion was developed in NodeJS and the API server for stable-diffusion was based on opening an API endpoint from the excellent stable-diffusion-webui package by Automatic1111. IPFS storage is provided by both a local node and the NFT.storage API by protocol labs. This allows for multiple copies of the images to be stored to ensure faster delivery and availability of the images. The front-end was developed in React utilizing scaffold-eth, tailwind, ethers and eth-hooks libraries. Challenges we ran into Latent diffusion is a very computationally intensive process, so finding a reasonable set of defaults, investigating command line params and configuring to optimize resource usage was a challenge Accomplishments that we're proud of First time operating a chainlink node and writing TOML specs. Finding ways to decentralize the front-end hosting while still triggering the backend processes via Chainlink. Learning more React and how to best interface it to web3 using hooks. What we learned I learned a lot of the operational requirements of running a Chainlink node, how to specify new job types and what needs to be deployed to the target blockchain to enable bidirectional communication between the Chainlink network and smart contracts. I learned more about how to write functional react using hooks and the benefits of using hooks versus class-based React components. What's next for NiftyMatic I hope to run stable diffusion on higher end hardware, experiment with clustering and multiple nodes to allow more users to be able to render concurrently. Further development to make it easy for anyone to spin up their own Chainlink Node for running stable diffusion jobs! <div