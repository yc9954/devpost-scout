---
slug: "cyclimate"
url: "https://devpost.com/software/cyclimate"
title: "CYCLIMATE"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1128
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# CYCLIMATE

> With CYCLIMATE we can calculate carbon footprint in cities while promoting and rewarding healthy practices such as cycling; with IoT technology we'll be able to measure the carbon pulse on the planet

[Devpost](https://devpost.com/software/cyclimate) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[climate_energy]] [[developer_tools]] [[finance_payments]] [[supply_logistics]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** amazon-web-services, arduino, chainlink, estuary, ether.js, firebase, fleek, graphql, hardhat, iot, ipfs, moralis, node.js, openzeppelin

## How they structured the write-up

- carbon pulse of the world
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cyclimate

## Body

CYCLIMATE CARBON PULSE OF THE WORLD Inspiration Our main motivation is to provide real, real-time and transparent information to support the processes of achieving carbon neutrality for the entire planet; Starting from this, different approaches are born that motivate us to continue: Promote healthy practices such as the use of bicycles and reward physical activity through a native token exchangeable for prizes, services and others. The technical challenge of providing information in real time and storing it in the blockchain through the use of different tools such as Chainlink, Filecoin and many more. The challenge of combining various technologies to build a solid project. What it does Cyclimate is a tool that allows you to calculate carbon footprint in cities while promoting and rewarding healthy practices such as cycling; with IoT technology we'll be able to measure the pulse of carbon on the planet. With Cyclimate we seek to promote an urban carbon monoxide measurement model while encouraging the use of healthy practices such as cycling; In the future, people will be able to acquire our measurement device in order to calculate the carbon footprint through different routes in their cities. For this work, people can be rewarded in a diverse ecosystem of benefits, starting with being able to transfer the information collected by a native token called $CYCLI, which can be used to acquire goods, services, prizes and other benefits, which will be in a marketplace that we build. Users, in turn, will have the option of swapping our $CYCLI token in different DEXes or, if they wish, through the developed gateway they will be able to directly exchange their tokens for FIAT money and this will go directly to their Paypal account. Cyclimate seeks to develop as a ReFi project by allowing compensation and adding value throughout a chain, since we propose an ecosystem in which we reward the valuable action of users when collecting data, while this data can be used to help achieve the goals of carbon neutrality of different actors, both public and private. How we built it The construction of CYCLIMATE begins with the creation of the sensor, one of our members had previous experience and led us in the construction of the tool and the storage system. Our sensor measures carbon monoxide and sends data through a Wi-Fi connection to an endpoint developed in Python; this data is stored temporarily, and when it reaches 60, it is sent and stored in packets through the IPFS Estuary; a small index is left in SQL simply to make the queries faster and have a better user interface, so when the user proceeds to claim their CYCLI tokens, this record is stored in IPFS, the data is exchanged and from there they will be stored directly in the contract. When we get the information, the user can connect through the website in Fleek where they will find the IPFS page, then they will be able to connect easily through Metamask, there they will be able to make requests to the blockchain through the cyclimate front; The front has been developed with React and Ether.js, this in turn has an interaction with Python, which here connects with all the data processing done with Estuary; We also mentioned that we made another back with node.js to use the request services from Moralis. For more requests we use Filceoin again to store the metadata of our NFTs with web3storage; We use Firebase to index the information that was stored with web3storage, we use Pinata to store the files corresponding to the NFTs in our marketplace. We use GraphQL to make a sub-graph of the marketplace and do a proper management of money and the flow of NFTs, keep an inventory of the purchase and sale; As a development environment for smart contracts we used Hardhat, where we did tests and deployments and the contracts were created as such; the contracts were made in Solidity and in Solidity we use OpenZepelin to: the ERC-777 for the marketplace for benefits section for the payment gateway (which is connected via an ANY API node from Chainlink) And another ANY API or JobID to exchange the data that is stored in Estuary and mint the native CYCLIMATE tokens, $CYCLI, for the number of packages stored; In addition to the above, we implement Push Protocol to notify people when they purchase an NFT. Finally we use Etherscan as a tool to query information from the Blockchain to finally deploy it on the Polygon testnet, Mumbai. Challenges we ran into 4 big challenges we had in the process First to be able to store data and query the data from python, since there is no direct interface from python, we had to build the requests from scratch to make it useable Second, make the call from the contract to the endpoint created to redeem the data packages that were ready to be redeemed for the native $CYCLI token. After this occurred, the contract would issue the tokens to the user's wallet. Third, in the implementation of the ANY API for chainlink, there were inconveniences for the approval of the node's sender because there are no permissions to add new senders on the oracle that the Chainlink documentation shows, after several tests failed, it was decided to deploy a own oracle where it was possible to add the node as sender. Fourth, to create a liquidity pool in Uniswap it is not very easy to find the address of the router contract for mumbai. Accomplishments that we're proud of With CYCLIMATE we can calculate carbon footprint in cities while promoting and rewarding healthy practices such as cycling; with IoT technology we'll be able to measure the carbon pulse on the planet. Our main pillars or banners are: 🍃Our commitment to obtaining real information that allows us to achieve carbon neutrality🍃 🚴Promote healthy practices🚴 🌿Build a sustainable model focused on regenerative finance ReFi🌿 What we learned The application of a external adapter of chainlink for use of the payment gateway change from native tokens to FIAT. The use of Estuary (Filecoin) (Alpha phase) IPFS storage of sensor CO2 readings and IPFS storage of native token redemption The use of Fleek (Filecoin) for the deployment on IPFS of the app. The use of the SDK of the web3storage tool (Filecoin) for storage of images and metadata for NFTs What's next for CYCLIMATE Our Roadmap Lite for 2023 Q1 Measurement device improvements Automation in the generation of heat maps on the Dashboard Development and improvements in UX/UI design Q2 Alpha testing phase with cyclists, early adopters Alpha test benefits launch Token release on testnet Q3 Token generation event CYCLIMATE app and wallet CYCLI staking Q4 Official NFTs and benefits Data analysis and new economies DAO building <div