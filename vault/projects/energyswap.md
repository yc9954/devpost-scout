---
slug: "energyswap"
url: "https://devpost.com/software/energyswap"
title: "EnergySwap"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1097
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# EnergySwap

> Peer to peer decentralized energy trading platform to sell your excess energy to your neighbors

[Devpost](https://devpost.com/software/energyswap) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[climate_energy]] [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** alchemyapi, amazon-web-services, arduino, chainlink, chartjs, iot, javascript, nestjs, nextjs, node.js, remix, solidity, tailwindcss, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for energyswap
- links

## Body

Landing Page Dashboard P2P listings P2P seller mode Connect Wallet Inspiration The idea for EnergySwap was largely driven by the realization that the current energy market suffers from a lack of transparency and accessibility. We felt the need for decentralization in this space. We identified a void in the marketplace for a platform that would allow for decentralized, peer-to-peer energy trading. We saw an opportunity to leverage IoT and blockchain technology to create a platform where users could easily manage their energy assets, exchange excess power, and contribute to a more sustainable energy ecosystem​. This will socially impact the planet and help promote healthy production and consumption of energy through usage of renewable resources. What it does EnergySwap enables users in a locality to exchange energy(electricity) amongst each other through their local grid hence making it a peer to peer electricity exchange. User flow for seller/producer/prosumer: Electricity gets produced by the producer at his unit(house). Then it is sent to the local grid from which it can reach the buyers. User flow for buyer: Buyer goes to the listings page and buys energy immediately from the seller they want. The grid is notified and makes sure to allot that much electricity to the buyer's house. How we built it Assumption: Production data and Consumption data are assumed to communicate with the local grid which has the IoT setup and currently this production and consumption data is simulated by the ESP32 which sends this information to AWS. For the IoT, we used ESP32, which is setup as a Thing on AWS IoT Core, to simulate the data and send the data to the DynamoDB table on AWS. Then a lambda function takes that info and sets up along with the data and this is exposed to an API using API Gateway. We bring this data to Chainlink through an external adapter and bridge. So once data is requested, it starts a job to fulfill and makes changes on the Operator UI. There are 3 smart contracts setup: UserContract allows users to register users and give them seller role should they choose to sell electricity. EnergyDataContract uses the Chainlink oracle network to fetch and store energy production and consumption data. This makes state changes to the blockchain as well when you call the request functions. MarketContract enables the purchasing and listing of the energy and hence handles the payments made onchain. Challenges we ran into Frontend: User-friendly Design: Understanding the complexities of blockchain technology and implementing it into a user-friendly interface was a challenge. Displaying Real-time Updates: Ensuring seamless and real-time updates on the frontend based on the IoT data and blockchain transactions. Blockchain: Since it was the first time working with Chainlink, there were lots of implementation errors initially with fulfilling requests and creating bridges, external adapter and jobs etc but the amazing documentation from Chainlink side with a little help from their discord helped fixed all the issues. Initially we combined all the functions in a single smart contract so at the start it didn't work as expected so after debugging and redeploying multiple times we decided to break down the workflow into 3 different contracts. IoT: Connectivity issues from the ESP32 to the local network to send data. AWS: Since it was our first time using AWS, a lot of things weren't functioning as expected but this was quickly fixed by adding appropriate permissions, roles, and policies. API Gateway consistently showed an 'Internal Server Error' message. Accomplishments that we're proud of Successful IoT and AWS integration: We managed to create a seamless integration between the Internet of Things (IoT) and Amazon Web Services (AWS). Through the use of an ESP32 device, we simulated and produced real-time data that was sent to a DynamoDB table on AWS. Seamless frontend, backend, and blockchain integration: One of the major achievements was successfully integrating the user interface with the backend and the blockchain. This accomplishment involved a complex process of connecting multiple technologies and platforms, all while ensuring that the end result was user-friendly. This demonstrates our ability to work with diverse technology stacks and create a seamless user experience. Effective use of smart contracts: We developed and deployed three separate smart contracts that handled user registration, energy data management, and energy marketplace transactions. Overcoming technical challenges: During the development process, we encountered numerous technical challenges, ranging from implementation errors with Chainlink to issues with AWS permissions and roles. Despite these challenges, we were able to find solutions and build a working prototype. This accomplishment demonstrates our problem-solving skills. Creation of a potential game-changing platform: Perhaps the most significant accomplishment is the creation and ideation of EnergySwap itself. The platform represents an innovative solution to the lack of transparency and accessibility in the energy market, leveraging IoT and blockchain technology to enable peer-to-peer energy trading. This accomplishment highlights the team's ability to identify a gap in the market, envision a solution, and bring it to life through technology. What we learned We learned how to leverage AWS for IoT data processing and storage, including how to create a Thing on IoT Core, set up tables on DynamoDB, and create lambda functions to process the data. We gained a deep understanding of smart contract development, including how to design, write, and test them, as well as how to troubleshoot and optimize them for gas costs. We understood the intricacies of integrating IoT with blockchain, and how to handle the challenges that come with real-time data transmission and storage. We became familiar with Chainlink and learned how to use it to fetch and store energy production and consumption data. We gained experience in creating user-friendly interfaces for complex systems, ensuring that the user experience is intuitive even for those who may not be familiar with blockchain or IoT. We understood how to work with APIs, especially in the context of AWS, and how to troubleshoot and fix issues that come up during development. What's next for EnergySwap Enhance the user interface and user experience to ensure the platform is as accessible and intuitive as possible. Explore potential partnerships and collaborations with energy companies and green initiatives to further expand the platform's reach and impact Implementation of testing and security measures to ensure the safety and reliability of smart contracts so that it's not susceptible to hacks. We want normal web2 users to join in as well so the payments will be enabled to be made using regular credit cards, debit cards, PayPal, and other such payment methods. Ship to mainnet! Links Figma: here Further reading and References: IRENA P2P Trading Doc <div