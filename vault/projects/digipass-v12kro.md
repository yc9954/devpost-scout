---
slug: "digipass-v12kro"
url: "https://devpost.com/software/digipass-v12kro"
title: "Digipass"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 712
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/general_public"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Digipass

> A dNFT-based ticketing system that gamifies the public transportation experience, to make it more user-friendly and environmental-friendly simultaneously.

[Devpost](https://devpost.com/software/digipass-v12kro) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[finance_payments]] [[transportation]]
**user** [[general_public]]
**substrate** [[video_visual]] [[web_dom]]

**stack** avalanche, chainlink, foundry, javascript, nextjs, openai, solidity, subgraph, typescript

## How they structured the write-up

- introduction
- what it does?
- what inspired us
- what we learned
- how we built the project
- tech used
- challenges faced

## Body

Main page Tech components/User journey Waterloo station AI image - generated after the travel Coming Soon Introduction Digipass is a dNFT-based ticketing system that gamifies the public transportation experience, to make it more user-friendly and environmental-friendly simultaneously. What it does? With Digipass, the users are able to mint a NFT representing their travel card on the Avalanche network. Whenever they reach their destination station, it generates an AI image (DALL·E 3) of that station and fetches the price of the fare from our API using Chainlink Functions, which are then saved to the contract and mapped to the user's pass. This gamifies the traveling experience by allowing people to "collect" their visited stations in their pass, while also adding additional trust and transparency in regards to the correct price with Chainlink Functions. What inspired us My Apple Pay failed at a tube station terminal recently. I was left in complete disbelief. So I ended up ubering that evening and spent a good part of the next day at Apple Store Genesis Bar. When I saw the dNFT tweet (or xeet?) by Chainlink the other day, it got me thinking. For residents of metropolitan areas, public transportation is an integral part of our everyday lives. We commute to work, and to visit our friends and families. Public Transit payment is one of the mundane tasks we do day in and day out. It is almost like our second nature. But what if we can transform this seemingly mundane task into a seamless and enjoyable experience? By re-inventing the way we pay for public transit, it injects new life into our daily routines and makes our journeys all the more enjoyable. More than that, by replacing physical cards with digital ones, we can further reduce the environmental impact of public travel and onboard more young commuters who are both digital-native and environmental-conscious. For illustration purpose, we use the London TFL system as an example. What we learned In building the dApp, we have learned: How to properly use Chainlink Functions & integrate them in the contract. How to deploy & make a dApp work on Avalanche Testnet. How to fetch information about an ENS name using their Subgraph and how to add custom data to an existing ENS with the ENS Public Resolver contract. How to build an API which works with DALL·E 3. How we built the project The project consists of 3 segments. The contract, the backend API and the dApp. Contract The contract is deployed on Avalanche Fuji. It's a mix of ERC721A and Chainlink Functions Consumer contracts which allows users to mint their NFT pass and to submit their travels. Each travel is assigned a Chainlink Request ID, which upon a successful data fetch, is used to find the particular travel and assign the right price fetched from the API. Backend API The API stores and provides the right fare prices based on the visited station. It's also connected to OpenAI API to generate AI visualisations of the visited stations. dApp The dApp allows visitors to mint their pass and to access all their pass travels, along with statistics such as total travels, total £ spent and the collected NFTs. If the user owns an ENS domain, it will display it as the user's name along with the avatar. On top of that, it lets the user save their total travel amount to their ENS profile on-chain, so that it can be used in other dApps. Tech used Here's a summary of the key tech used in this project. Category Subcategory Description Chainlink Chainlink Functions Fetch the fare price from the API and upload it to the contract along with the AI-image link. Avalanche C-Chain Dapp The contract/dapp are deployed on/using the Avalanche Fuji network. ENS ENS Display Displaying the ENS name and avatar. Subgraph ENS Subgraph Fetching information about the ENS (node id). ENS ENS Resolver Contract Creating a field with the total travels amount with setText() . Challenges faced The first attempts with the Chainlink Functions playground were a bit difficult, as the playground would not be compatible with APIs with stricter CORS policies. It was also slightly difficult to use the official Avalanche Fuji faucet, although the one on the Chainlink's website was more than helpful. <div