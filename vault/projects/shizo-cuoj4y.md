---
slug: "shizo-cuoj4y"
url: "https://devpost.com/software/shizo-cuoj4y"
title: "Shizo Play"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 593
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/transportation"
  - "substrate/geospatial"
---

# Shizo Play

> A city-based strategic game with the goal of creating a decentralized map

[Devpost](https://devpost.com/software/shizo-cuoj4y) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[transportation]]
**substrate** [[geospatial]]

**stack** chainlink, golang, polygon, react, solidity, thegraph

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for shizo

## Body

Navigation Disclaimer: Our team participated in another hackathon with the "Shizo" project which at that moment was basically a map to buy/sell lands and roads as NFTs and won a prize there. During Polygon BUIDL IT : Summer 2022 hackathon , we managed to make a P2E game out of our previous project. All the features mentioned below and in the video are implemented during this hackathon. Inspiration Imagine a decentralized map with a clear and fully transparent validation process. Reporters can suggest updates for the map (like changing the name of a road or reporting a high traffic area). After the validation, the reporter and validators will be rewarded. There are a couple of technical challenges before we get to this point like how we're going to migrate huge amounts of data to the blockchain. Doing it even for a big company is very expensive. There are billions of roads and lands and some of them have a relatively large amount of data. This project is an effort for migrating lands and roads to the blockchain by designing a game. What it does Shizo is a P2E city-based strategic game where players compete with each other to grab loots that are spawned randomly on the map. This game encourages players to mint more roads/lands and while minting, we're going to migrate the basic data and tags of those entities to the blockchain. How we built it Shizo DApp is connected to three smart contracts: SHEN (Shizo Energy): It's the currency of the game. Chest: Using Chainlink VRF we're generating random positions for our chests. Players compete to reach the chests before others and claim the reward of it. Shizo: All the other core logic of the game is implemented here. Things like transportation, blocking a road, teleportation, minting, marketplace, etc. Challenges we ran into One of the most challenging parts was to calculate haversine distance in an efficient way. We need to implement this formula to detect whether the player is near the chest to claim it or not. To calculate Sin and Cos of latitudes and longitudes we implemented a lightweight Solidity version of Dave Dribin's trigint library which itself is written in C. The optimizing challenges were very interesting. Also making a real-time game on the blockchain without a centralized coordinator is difficult. We managed to remove a significant part of those centralized dependencies without making functions that require a lot of gas. This results in a real-time feeling experience by making a small number of state changes on the blockchain. Accomplishments that we're proud of This was our first game. The scope of this project was so big that we never expected to be able to make it. Despite all the mentioned challenges, we were able to provide a solution for each of them and also implement them. What we learned The only part of developing a P2E game is not the technical/graphical aspect of it. One of the most important things is the design of the virtual economy. It should be balanced and stop players from exploiting the game. There's a lot to learn about designing virtual economies. What's next for Shizo Creating a data structure to store the geometry of roads in an efficient way. Adding other elements to the game like buff cards, classes, clans, ... Continue optimizing until it's ready to be deployed on the Mainnet. This game is the first step toward making a decentralized map. We're also trying to develop a method of verification to be used on these kinds of maps. <div