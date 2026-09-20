---
slug: "verifree"
url: "https://devpost.com/software/verifree"
title: "VeriFree"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1329
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# VeriFree

> Free blockchain for Verified Students.

[Devpost](https://devpost.com/software/verifree) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[civic_government]] [[developer_tools]] [[education]] [[finance_payments]]
**user** [[developer]] [[educator_student]]
**substrate** [[financial_record]] [[web_dom]]

**stack** avacloud, avalanche, ccip, chainlink, functions, hardhat, nextjs, polygonid, solidity, subnets

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for verifree

## Body

Inspiration Being a student, it is wonderful to have perks such as discounted or even free services. This allows us to get exposure to what the world has to offer without breaking the bank. It's not possible to get free transactions on blockchains however, because of two challenges: Verification & Privacy. Who do we trust to verify and publish the student verification status? And, how do we publish this verification proof while preserving user's privacy? (we don't want sensitive information published directly on the blockchain). This inspired me to create a blockchain where transactions are free for verified students. What it does VeriFree is a semi-permissioned blockchain subnet on the Avalanche network, currently deployed as a DevNet using Avacloud. VeriFree uses PolygonID to verify that a student has a valid edu email address by sending a verification QR code via email. This is used to generate a VerifiedStudentCredential in student's PolygonID wallet. The second step is to publish this proof on-chain. The Verifier Smart contract uses ZKProofs to verify the wallet address of the sender against the same address' BigInt representation in the proof sent. This is important as it stops users from using the same proof with multiple wallet addresses. -This enables us to have a system where 1 student email address = 1 wallet address = 1 Proof verification. The transaction fails if the same proof or address is used multiple times. The verification status is sent to the avalanche C-Chain using CCIP and to the VeriFreeSubnet from there. The Verified students get a VerifiedStudent SoulBoundToken (VSBT) which can be used as a Voting token in the VeriFree DAO. Only verified students can vote on this DAO. 1 VSBT = 1 Vote. The VeriFree DAO can be used to do the usual DAO executions, such as changing DAO parameters, executing contracts, controlling a treasury, but I have also added functionality to add Valid domains to the VeriFree dApp, and update the subnet access allowlist using the DAO. This enables the DAO to control access to the VeriFree blockchain by: Allowing students with different school emails to get verified. Let certain addresses try out the verifree subnet without going through the verification. The CCIP message also invokes a Chainlink Function (which mimic the AWM/teleporter standard), to update access to the VeriFree subnet on devnet. Only users who have gone through this verification process get access to transact and deploy contracts on this subnet. Also, 1000 VFT (native coin on the VeriFree blockchain) is minted to the student's address upon successful verification. To conclude, VeriFree is a blockchain run by the students, for the students, allowing free access to blockchain transactions using the power of Avalanche, PolygonID, and Chainlink. How I built it VeriFree uses a self-hosted PolygonID issuer which issues VerifiedStudentCredentials. These credentials store the email as well as wallet address. The credential is used to publish on-chain proof using a StudentVerifier (modified ZKPVerifier) smart contract on Polygon Mumbai. Upon verifying the proof with ZKcircuits and a dynamic value (the sender's address), the smart contract calls the DestinationVSBTMinter contract on Avalanche C-chain using CCIP. The Destination minter contract mints VSBTs to the verified address, and invokes the VeriFreeControl smart contract with a Chainlink function. This Chainlink function receives an encoded message, the same way a teleporter contract would, and sends it on the VeriFree devnet via an API. The corresponding VeriFreeSubnetControl contract implements the teleporterReceiver interface, and receives/decodes the message as if it was sent via a teleporterMessenger. The decoded data is used to add the sent address to the transaction & contract manager allowlists via precompiles, providing access to the VeriFree devnet. The VeriFreeDAO can also invoke the VeriFreeControl contract with the CL function, allowing the DAO to control the Devnet. Mimicking the teleporter allows me to demonstrate how the functionality would work using AWM and allows easy migration once teleporters are live on C-Chain. Challenges I ran into Working on a project with so many moving parts as a solo developer is a huge undertaking. I had to learn a lot of different technologies like PolygonID (issuer and on-chain verification), Chainlink CCIP and Functions, Avalanche Subnets, etc. This along with the frontend work (and my full-time job) was exhausting due to constant context switching. The first big issue I ran into was that there was no direct way to use dynamic inputs in the ZK Verifier. i.e once the ZKPRequest is set using setZKPrequest method, the input specified in the proof is fixed. This meant the same user can use the same proof multiple times with different wallet addresses, as the user's wallet address cannot be set as a parameter to validate against, after the initial setZKPrequest. I overcame this by looking through the inner-working of ZKPVerifier contract and changing the value field in the _beforeProofSubmit hook, setting the value to the BigInt representation of message sender. This way, the ZKCircuit fails if the user submits the same proof with an address not contained in the proof itself. The second hurdle was that I designed the system with the assumption that C-Chain can natively send cross chain messages using AWM/teleporter to the subnets. As this functionality is not present in testnet yet, I used a workaround with Chainlink Functions to call an API to mimic the teleporter interface. Last but not the least, I was able to get the whole system working end-to-end multiple times with my friends using northeastern email ids, but the verification system started failing during the demo recording. I had to scramble and reset the issuer from scratch in the last minute. Demo days are scary! Accomplishments that I'm proud of I am most proud of getting the system working end to end with multiple users. Had to manage a lot of moving parts as a solo dev to pull that off! Setting the ZKPRequest value dynamically, allowing 1 email = 1 address = 1 Verification/SBT. This helped me accomplish an idea I had since I learned about DAO's: truly decentralized voting system. I am also happy to open source all my learnings from this project. This project can be used as a framework to build different types of semi-permissioned systems! What I learned I think I have learned more about Web3 development in 1 month that in the last 3 years! I learned to use various awesome technologies like PolygonID, Avalanche subnets, and Chainlink products such as CCIP and Chainlink Functions to integrate them. I learned a lot about full-stack web3 development using NextJs as well. What's next for VeriFree With such a broad scope, there are numerous directions VeriFree can take in the future. With that in mind, following are the possible next steps: I will work with fellow community members (shoutout to the NEU blockchain club) as well as other students to use this DAO to control the future of VeriFree. I will implement teleporter as soon as possible as I think interoperable subnets on Avalanche are the future. I will work on creating an all-in-one wallet (PolygonID verification, DAO, subnet interaction) for the verifree blockchain, provided a smooth UX to those who are new to crypto and blockchain. I also want to inspire others to build similar systems for gated access to subnets. For example, a game development studio can gate access to only those who have bought a specific game on steam on their app-specific subnet, allowing gasless transactions for their users. I will also look into developing Dapps which are not practical on public blockchains for VeriFree users. Example: an event management system on the blockchain, or university services using the blockchain like food credits, library credits, etc. You can read the how-it-works guide on the website to learn more about the project. I am open to talk about my project to other members of the community, feel free to reach out to me on discord through the hackathon channel. Discord username: shailesh_shenoy The video has been fast-forwarded to fit the time limit Thank you! <div