---
slug: "holdingplace"
url: "https://devpost.com/software/holdingplace"
title: "ChainRunners"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 648
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/code_repository"
---

# ChainRunners

> Compete and hold each other accountable. Friends can contribute to a smart contract that will weekly evaluate Strava API Data and declare a winner, who will receive a monetary reward

[Devpost](https://devpost.com/software/holdingplace) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[code_repository]]

**stack** chainlink, hardhat, react, solidity, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chainrunners

## Body

Inspiration ChainRunners is inspired by the powerful motivation that comes with committing to a competition, especially when that commitment is solidified in the immutable realm of blockchain technology. We wanted to capitalize on the initial surge of enthusiasm that athletes experience upon entering a contest, harnessing this energy and setting it in stone through a smart contract. By staking Ether and initiating a competition, participants make a binding commitment - there is no turning back, only moving forward. This firm commitment, paired with the integration of decentralized technology and fitness tracking through Strava's API via Chainlink, creates a unique platform that binds physical exertion to digital rewards, fostering a community where fitness and technology synergize for mutual motivation and benefit. What it does ChainRunners is a decentralized application where users can participate in competitions by staking Ether. It utilizes Chainlink to connect with the Strava API, allowing real-time tracking of athletes' performance. Participants join competitions with a set buy-in amount (dictated by the competition creator) and compete based on the distance logged on their Strava accounts. The application intelligently handles payouts at predetermined intervals and ultimately rewards the overall competition winner, integrating blockchain technology with real-world athletic achievements. How we built it The application is built on Solidity, with critical functionalities dependent on Chainlink for API calls to Strava. We designed a smart contract system where users stake Ether to participate in competitions. The contract, through Chainlink automation, periodically checks athletes' progress and handles payouts. Our front-end interface, though challenging, was crafted to offer a seamless user experience, allowing easy participation and tracking of competitions. Challenges we ran into Our primary challenges stemmed from limited experience in coding and understanding the intricacies of Chainlink functions and API integration. Handling authentication calls with Chainlink was particularly challenging, requiring a frontend call to the strava api, and a backend script to upload the access token for each athlete to the don. There were instances of failed chainlink function calls with a status of "Fulfilled with error", and I couldn't tell what was causing it. Attempting the call again or redeploying the same contract would result in a successful call. Additionally, the front-end development presented significant learning curves. Learning to use wagmi to read and write to the smart contract meant getting familiar with hooks. A major concern is ensuring the integrity of the data from Strava, as the system currently trusts the input without a robust mechanism to prevent cheating. Accomplishments that we're proud of We are immensely proud of successfully integrating Chainlink functions with the Strava API, enabling automated and fair distribution of rewards based on real athletic performance. The smart contract functions effectively, handling complex logic for competition management and payouts. This project significantly enhanced our confidence in writing and interacting with smart contracts and deepened our understanding of blockchain technologies. What we learned This project was a profound learning journey. We gained substantial expertise in smart contract development, including deployment and interaction within the Hardhat environment. We learned to use event listeners and delved into Chainlink's offerings, understanding how to utilize its services and toolkit for managing secrets. Front-end development was also a challenge, but I am more comfortable with using hooks in React now and using Wagmi to interact with my smart contract. What's next for ChainRunners Moving forward, we plan to refine the smart contract logic and enhance the front-end interface. We aim to improve the management of API call secrets and restructure the incentive system. Instead of the current betting framework, we envision a system where athletes earn ERC20 tokens based on their logged distances, with substantial bonuses for winners. These tokens could be used to mint NFTs, introducing an element of rarity and value through Chainlink's VRF-based randomization. This evolution of ChainRunners will not only increase user engagement but also add an exciting layer of digital collectibles tied to physical fitness achievements. <div