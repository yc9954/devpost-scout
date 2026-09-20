---
slug: "ecoblock"
url: "https://devpost.com/software/ecoblock"
title: "EcoBlock"
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 963
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# EcoBlock

> A Sustainable & Scalable Blockchain That Can Save Entire Countries Worth Of Energy.

[Devpost](https://devpost.com/software/ecoblock) · hackathon [[HooHacks 2021]]

## Facets

**mechanism** [[vision_ocr]]
  <sub>weak: developer_tools</sub>
**user** [[educator_student]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** blockchain, dart, flutter, node.js, python, typescript

## How they structured the write-up

- 🌱 inspiration
- ⚡ what ecoblock does
- 👷 how we built it
- ⚠️ challenges we ran into
- 😀 accomplishments that we're proud of
- 📚 what we learned
- ⏭️ what's next for ecoblock

## Body

Google Vision API Output Single Node Closeup Blockchain Node Outputs Logic Node w/ Python CLI UI layouts from Figma Firebase Popup Widget Example Debugging on a Physical Device Firebase BaaS 🌱 Inspiration Currently Bitcoin mining is estimated to use more energy than the entire United Kingdom per year (Up to 445 annualised terawatt hours). The act of mining and transferring one Bitcoin is one of the most energy intensive things we as humans can do. Needless to say, with the current widespread adoption of cryptocurrencies a massive energy and sustainability crisis has been set in motion. So we asked ourselves How can we create an extremely scalable solution to the cryptocurrency energy crisis? ⚡ What EcoBlock does TL;DR EcoBlock uses an alternative method of coin production that uses over 99% less energy than cryptocurrencies such as Bitcoin and Etherium. Additionally, we utilize machine learning to reward coin miners/minters that use green energy to incentivise a move towards a cleaner, more sustainable blockchain. ♻️ Built Different || EcoBlock uses a Proof of Stake system (POS) built using Typescript for coin distribution compared to the common Proof of Work system (POW). POS rewards users for how many coins they hold (stake) while POW rewards users based on their computing power to solve math problems. The move from computing intensive generation to a much more energy efficient "lottery" esque generation accounts for the majority of energy savings that EcoBlock can do. 🍀 Reward the Good || What differentiates us from other existing POS currencies is that we reward miners/minter for using certified green energy sources through our EcoBoost system. We use Google Cloud Vision to scan energy bills to determine is a mining/minting operation uses certified clean energy to run their computers. If so, we reward them by increasing their adding a multiplier onto their balance when deciding who wins a newly minted block. Combined these two approaches create one of the greenest and most sustainable approaches to cryptocurrency possible. 🚀 Ready for Takeoff || EcoBlock isn't only a simple blockchain. We were able to implement many features needed to introduce EcoBlock to the real world such as creating an IOS and Android wallet for storing, monitoring, transfering, and minting coins. Additionally we ensure that our system is secure as we prevent tampering by checking blocks and not adding any tampered blocks to the blockchain. A malicious user would need to own over 51% of the entire currency to tamper with the blockchain which is extremely unrealistic in practice. Key Working Features: Proof of Stake Blockchain with P2P connection and automatic host finding, OCR with Google Cloud Vision through REST API, Flutter frontend connected to Firebase and Blockchain, working private and public keys with wallets, functional transactions between blockchain nodes, python CLI for the blockchain. 👷 How we built it The EcoBlock blockchain was made using Typescript and Node.JS and had testing tools and a CLI (command line interface) done with Python . For determining if person use was using eco-friendly energy we used the Google Cloud Vision API which we implemented using a REST API and Dart . We used a Google Firebase database to store non-sensitive information related to EcoBlock users. The frontend was drafted and prototyped with Figma and implemented using the Flutter framework for Dart. ⚠️ Challenges we ran into The largest challenge for us was that everything was new to us as we chose languages, frameworks, and API's that we were unfamiliar with. This meant we had to do lots of documentation reading, asking mentors, and referring to online tutorials and resources. Besides the large number of technical challenges we also had to deal with each team member being in a different time zone making it hard to coordinate times to meet and sync up. However, we were able to overcome these challenges very well through proper time management and communication letting us deliver a project that we are all proud of. 😀 Accomplishments that we're proud of We were really proud that we completed a complex proof of stake blockchain for the backend with several advanced features such as automatic peer finding. For the frontend we felt that the UI was very clean and fulfilled its purpose of being an interactive way of accessing the blockchain. We were also very proud of figuring out how to use Google Cloud Vision for finding if a user is using clean energy. 📚 What we learned We were able to learn lots about different languages and frameworks as we were all new to Typescript, Dart, Flutter and REST API's. Additionally, through the course of this project we gained lots of insight into blockchain expercially with the advantages and disadvantages of Proof of Stake versus Proof of Work. Lastly, we all learnt more about how to work under tight timelines and working together to solve problems through this hackathon. ⏭️ What's next for EcoBlock We didn't have time to get into too many details when it came to security for certain parts of the project such as ensuring documents submitted for green energy certification checks so we wish we had more time to secure those parts of the project. We also want to try and continue work on blockchain and see if our idea is able to come to fruition as we believe that our project today could really be a feasible solution to the cryptocurrency energy problems that exist. Sponsor Prize Eligibility Sustainable IT as we created an extremely efficient and scalable alternative to energy wasting blockchains potentially saving the same amount of energy that entire countries use while promoting clean energy. Google Cloud as we utilized Google Cloud Vision and Firebase to complete and enhance some of the most innovative and challenging parts of EcoBlock (Green energy OCR and Blockchain tracking). <div