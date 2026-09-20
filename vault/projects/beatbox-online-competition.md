---
slug: "beatbox-online-competition"
url: "https://devpost.com/software/beatbox-online-competition"
title: "Online Beatbox Competition"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1043
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Online Beatbox Competition

> It is a decentralized application to create and manage online beatbox competitions.

[Devpost](https://devpost.com/software/beatbox-online-competition) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[agriculture_food]] [[civic_government]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[structured_db]] [[video_visual]]

**stack** chainlink, hardhat, ipfs, moralis, nextjs, polygon, solidity, vercel, web3.storage

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for beatbox online competition

## Body

Online Beatbox competition Homepage. Competition page. Inspiration I am a beatbox lover and I have known beatbox since 2013. If you wonder what beatboxing is, it is a musical art form that uses the vocal tract to mimic percussion and other sound effects. So, I thought of doing a project with beatbox in mind. So, in the beatbox world, there are offline and online competitions where beatboxers compete with each other. There is an online beatbox competition going on called BBU(Beatbox United) started by two professional Beatboxers Sxin and Chezame which is different from the previous online competitions taking place. Many people love the idea on which the competition is based and there is a huge prize pool also. So, smart contracts can be used to make sure that the winner gets the winning amount as soon as the battle ends, and also there will be a fair selection of beatboxers for battle as random beatboxers are selected for battle in each round. Also, multiple judges can be added for the fair judging of the battles along with the user voting in terms of video likes. So with this love for beatbox and smart contracts being able to do what's promised, I became inspired to complete a web3 project for creating a decentralized application to be able to start and manage online beatbox competitions. What it does The online beatbox competition dApp gives an interface to start an online beatbox competition. Then the competition creator can start the wildcard submissions and any participants can submit the wildcard videos until the wildcard submission ends. The competition creator can add judges to evaluate the wildcards and the battles. After the top 16 wildcards are selected, the creator can start the beatbox battles between two participants on which the judges can vote with the points for the judging criteria namely originality, timing, enjoyment of listening, video, audio, battle, and extra point. After the battle ends chainlink keeper automates getting Youtube video likes to finalize the winner based on the judges voting and Youtube video likes count (as user voting). Battles continue from Top 16 to Top 8, Top 8 to the semifinal, and semifinal to final to select the winner. The creator can also start the particular battle with the winning amount so that the winning amount is sent to the battle winner. All the judge's voting can be viewed for the particular battles. How I built it I used three services from chainlink namely Chainlink Keepers, Chainlink VRF, and Youtube data API external adapter. I used VRF to randomly shuffle the beatboxers for random battles between them so the battles are not selected manually. I used a Youtube external adapter to get the likes to count on the video of the battle to judge the competition winner in addition to other points voted by the judges. And I used the chainlink keeper to monitor the battle end time and fetch the likes count on battle videos when all votes are voted by the judges and the time for the battle has passed or the battle has ended with partial voting. I have used Next.js for the dApp frontend and used an API for uploading videos to web3 storage which stores the data on the IPFS and filecoin storage for persistence. I have used both Moralis Speedy nodes and Alchemy RPC nodes to interact with the blockchain. I have also used Moralis servers in the frontend for the sign-in, index the created competitions, store the competition images (on IPFS), and used the moralis database to store the wildcard entries and wildcard winners, judges, financial supports, and the competition update posts. Lastly, I deployed the contracts on the Polygon Mumbai Testnet as it's an Ethereum-based cost-effective blockchain. Challenges I ran into The competition battles needed to get the youtube video likes to count on-chain so that the winner is selected based on the likes count and other voting criteria. In order to do so, I needed to make use of the external adapter for it and in the beginning, I thought I would host the chainlink node locally and use the external adapter but my laptop was not that powerful to run the chainlink node, and my development setup at the same time so I asked help on the chainlink node operators channel on discord and I got help from Matt | Block-Farms.io#7823 to host the external adapter. The other challenge is that I am not so great at frontend but I think I made a good frontend overall. Accomplishments that I am proud of This is my first hackathon since I started learning web3 through different materials like youtube courses, blockchain Coursera courses, etc. I am proud that I started this project and became successful in submitting the project no matter what the results might be. I love beatbox and I am proud that I could submit my dApp showcasing a way to conduct decentralized beatbox competition to the web3 world. Thank you chainlink and all the sponsors for this hackathon. What I learned I learned a lot during the hackathon as I was only learning through tutorials before. True learning happens when doing a project with the learning from before. So I learned a lot about chainlink services like VRF, Keepers, and external adapters and how they can help to bring the off-chain data on-chain but in a decentralized manner. I was working solo on the contracts and the dApp, so it was a great learning and building this project. I also learned much about Moralis as it was much helpful for this project. So, it's great learning to bring a working concept to a dApp where smart contracts take control to assist the competition in an easier and fair manner. What's next for Beatbox Online Competition So with the completion of the chainlink hackathon, the development of this project will not stop but will progress further. The next thing for this project can be to optimize the project further and also advance into a project to assist beatboxers in creating online competitions, NFTs, tokens, crowdfunding, DAOs, and much more. I think Web3 is the future and so the beatbox community should also become part of web3 and utilize this technology to the fullest. <div