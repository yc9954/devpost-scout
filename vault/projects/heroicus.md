---
slug: "heroicus"
url: "https://devpost.com/software/heroicus"
title: "Heroicus"
hackathon: "Fantom Hackathon Q2 2023"
organization: "Fantom Foundation"
winner: true
words: 659
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/housing_homeless"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Heroicus

> Cloud computing using NFT rentals and AWS

[Devpost](https://devpost.com/software/heroicus) · hackathon [[Fantom Hackathon Q2 2023]]

## Facets

**domain** [[housing_homeless]]
**substrate** [[code_repository]] [[video_visual]]

**stack** amazon-web-services, hardhat, nextjs, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i'm proud of
- what's next for heroicus

## Body

logo Inspiration Lately, I've been having fun running stable diffusion servers in the cloud (for AI Image generation). Then I was reading about EIP-4907 , which is a NFT Rental extension. That got me thinking about the different possibilities for NFT rental, and I came up with the idea to create a cloud server rental platform using NFT rentals. What it does Heroicus is a cloud server rental platform that uses NFTs to represent ownership of a server. It uses the EIP-4907 extension, which adds an expiration date to NFT ownership. This makes it possible for the user to pay for a certain amount of time, and it will expire automatically. The user can choose from different server templates, which define what software is preinstalled and automatically starts up on server start. For the first release, the choices are: Stable Diffusion (for generating AI images) - Runs automatic1111 on high-end GPU servers. Docker - Runs Portainer on burstable CPU servers. It allows you to run any docker image, either from Docker Hub, a custom repository, or uploaded from your computer. This allows you to run practically any application. The user will pay for the server rental in USDC, which is sent to the contract as a deposit for the rental time selected. An NFT is minted to the user with the expiration date. During the time the user owns the NFT, the user is able to extend the rental. They can also terminate the rental early, getting a refund for unused time. How I built it Frontend and APIs are built with Nextjs and Wagmi, and deployed to AWS Amplify. Docs pages are built with Docusaurus and deployed to AWS Amplify. An AWS Lambda Fn that monitors the blockchain and terminates expired server rentals. AWS EC2 is the server platform that actually runs the servers. The APIs and Lambda Fn talk to EC2 to manage the servers. See Architecture and Sequence Diagrams Challenges we ran into Synchronization. It was hard to figure out an approach to synchronize the starting/stopping of servers with the contract events, making sure the platform could not be exploited. Resource limits. It turned out to that it was possible for the server creation to fail in AWS, if they don't have enough resources available in that region. Luckily this happened to me during testing, otherwise I wouldn't have covered it. The only solution I could find was to, if server creation failed, have the server-side code make a call to the contract to refund the user. AMI Restoration is slow . It turns out that creating new servers from machine images is very slow if there is a lot of data that needs to be loaded into memory (which is the case for stable diffusion servers). I ended up having to download some of the data on every rental instead of copy it from a machine image. But the startup times of stable diffusion servers could still use a lot of improvement. It was my first web3 and AWS project. . There was a ton to learn and debug through. Accomplishments that I'm proud of Creating a unique use case for NFTs and NFT rentals. Learning AWS and Web3 in less than 2 months. The landing page turned out pretty sweet and was built from scratch. What's next for Heroicus Cheaper server rentals. The price is elevated to make sure it covers all the costs. The price can be lowered at a later time as the total costs are calculated. Faster startup times. The startup time for Stable Diffusion servers can take up to 10 minutes. There are optimizations that can be done with more time and research. More server options. Persistent rentals. Allow stopping a server while still persisting hard drive. This will allow a user to keep all the data on the data, while minimizing the costs. Security improvements. There are many security enhancements that should be done for the docker servers. <div