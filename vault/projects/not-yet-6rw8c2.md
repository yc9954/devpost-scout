---
slug: "not-yet-6rw8c2"
url: "https://devpost.com/software/not-yet-6rw8c2"
title: "Trypto"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1141
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Trypto

> A web3-based travel social platform.

[Devpost](https://devpost.com/software/not-yet-6rw8c2) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]]

**stack** amazon-web-services, automation, chainlink, datafeed, dnft, go, hardhat, javascript, nextjs, polygon, solidity, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trypto

## Body

Inspiration Travel is about creating memories. The ways to preserve memories are through personal memories or pictures. However, relying solely on personal memories has its limitations, which is why many people choose to digitally capture their memories through pictures. Nevertheless, even photographs have their limitations. Pictures stored in certain locations can be deleted or lost, and when the pictures are deleted, the associated memory can no longer be found again. However, by utilizing blockchain technology, we can ensure that memories are preserved indefinitely, immune to deletion or disappearance. The data associated with each memory is recorded on the blockchain, guaranteeing its eternal existence. We combine the concept of memories with travel services and offer a platform called Trypto, where memories are stored on the blockchain. What it does Users can create itineraries and interact with users worldwide by sharing and communicating about their travel schedules on the community page. To record and commemorate their visited destinations, users receive badges in the form of dNFTs, which feature landmarks of the respective countries. dNFT - To prove and commemorate having traveled within the platform, a badge is issued in the form of a dNFT by using GPS to verify that you were in a specific country. Automation - If you have visited a country multiple times, you can upgrade the badge for that country using dNFT and Automation. - Example: 1st visit: Bronze / 2nd visit: Silver / 4th visit: Gold Datafeed - To facilitate currency exchange in the respective countries, the platform provides users with easy access to real-time exchange rates through Datafeed (EUR/USD), allowing them to stay informed. Travel Plan - Users can create travel itineraries that are stored in the database and made available to other users. These plans are intended to be issued as NFTs in the future. Front/Back end - The platform has been designed with user convenience and accessibility in mind, ensuring a smooth flow and user-friendly interface. The backend facilitates seamless data integration and interaction among contracts, frontend, and the database. How we built it The core APIs created in the backend are as follows: Badge API This API manages the issuance of dynamic NFT badges and user information. When a user requests a badge, the count of badges is updated in the database and blockchain. Initially, users are assigned a bronze tier, and as they visit more tourist destinations and earn badges, they can upgrade to silver and gold tiers. The Dynamic NFT function is called to synchronize data between the blockchain and the database. The database is used as a fallback in case of slow network or blockchain issues. The goal of incorporating gaming elements like tier upgrades is to make the tourism experience more enjoyable for users. Travel Plan API This API allows users to create and modify travel plans by providing essential details. Users can input the country and travel duration to generate a travel plan. For each day of travel, users can specify the start and end times, as well as add titles and notes to manage the entire itinerary. User API This API addresses readability issues associated with MetaMask wallet addresses by allowing users to register nicknames. Additionally, the User Profile API provides information about the number of travel plans created and badges issued, enabling users to track their travel history and badge achievements. Challenges we ran into Back-end In order to implement the tier system progressing from bronze to silver and gold, I needed to enable counting of Dynamic NFTs. Initially, I was unsure how to synchronize the DB data with this aspect, which caused some obstacles. However, during this process, I contemplated on how to synchronize the DB data with the blockchain data, and came up with the idea of syncing the NFTID provided by the contract with the NFTID in the database. To accomplish this, I created a separate upgrade function. This upgrade function synchronizes the DB and blockchain data, counts the number of badges issued by the user, and upgrades the badge tier when a certain count is reached. Contract Errors when we try to utilize VRF and Automation at the same time We tried to use VRF and Automation in contract at the same time, but there was a error and we couldn't fix it. We were putting VRF functions inside PerformKeep in order to get random number every interval, but we failed. It looks like high costs or sth. Writing code with affordable gas price I learned Writing Smart contract needs to be very attentive and sensitive because of gas price. Every single line of codes have to be effecient, so we kept thinking of gas fee when we write codes. Accomplishments that we're proud of It is a great accomplishment to have developed the frontend with a user-friendly design that allows easy access for users to reminisce about their travels. The contract development for issuing badges, which enables users to digitally preserve their travel memories in the digital space and gives them a sense of collecting something through their travels, is also fulfilling. Moreover, the seamless integration between the frontend and contract, along with the development of a database where users can create and store itineraries, recording what they did in each travel destination, is a significant achievement. Additionally, the development efforts have resulted in the creation of Trypto, a platform that allows our team to collectively preserve memories from May. It is truly rewarding to have collaborated with exceptional developers in each field to bring this platform to life. What we learned Front-end Through this project, I found that the technology called dNFT was very useful, which cannot be done with NFT alone. I thought about how to make dNFT more friendly to users and designed the process to give a positive UI/UX feeling. When I first used the user's location recognition, I became interested in security and there are more things I want to apply in the future. Back-end We've learned how to manage the DB and NFT contract data in the backend. To synchronize the DB and blockchain data, we need to manage them through dedicated automation functions. Additionally, we've learned the importance of creating a system that allows us to manage all the data through statistics. Contract What is Chainlink and what they do for block-chain industry How to use Chainlink functions (VRF, Data Feed, Automation) How to integrate ethereum smart contract with chainlink functions How to use Foundry, Hardhat What's next for Trypto Development of a self-governance token for use on the travel social platform. Development of an in-house travel marketplace. Development of QR codes for authentication of accommodation reservations. Issuance of travel itineraries in the form of NFTs. Implementation of a VRF-based event prize draw for badge issuers. Provides a recommendation service of photos of tourist attractions around the world in the form of web VR <div