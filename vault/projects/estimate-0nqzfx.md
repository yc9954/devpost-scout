---
slug: "estimate-0nqzfx"
url: "https://devpost.com/software/estimate-0nqzfx"
title: "EstiMate"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 547
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# EstiMate

> Friends Fueled Fun: Betting Made Easy and Secure

[Devpost](https://devpost.com/software/estimate-0nqzfx) · hackathon [[TreeHacks 2024]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[financial_record]] [[structured_db]]

**stack** anvil, apns, caldera, convex, ethers, express.js, forge, node.js, oauth, signinwithapple, solidity, swiftui, togetherai

## How they structured the write-up

- inspiration 🌱
- what it does 💡
- how we built it 🛠️
- challenges we ran into 🌃
- what we learned 📝
- what's next? 🚀

## Body

Inspiration 🌱 We got this idea after noticing a common annoyance—tracking casual bets was a mess. Whether it was predicting the snow day or daring each other over who could do the craziest things, our bets were often forgotten, leaving behind a trail of "who said what." We created EstiMate , an app that makes betting with friends easy and secure. Our aim is to solidify those playful moments into lasting memories. Check out the fun video that inspired us! What it does 💡 EstiMate lets you set up bets and share them with your friends, whether it's a one-on-one challenge or a wager within your group, club, or frat. After creating a bet, you can pick how long the bet lasts, how much is at stake, and which side you're on. Inviting friends is super easy – just send a link or hold your phones close to each other to share with AirDrop. EstiMate is built on blockchain, allowing for seamless, protected, and transparent transactions. How we built it 🛠️ In EstiMate, when a user logs in using their Apple ID , they are taken to their dashboard where all ongoing bets are displayed. After creating a bet, the frontend sends a request to our backend, which is built on Bun-powered Express , with the necessary details including userId, bet name, bet amount, and timeframe. This request is processed by our backend, which interacts with the Convex database to register the bet and retrieve the user's private key. Next, we use Solidity for writing smart contracts that handle the logic of holding bets on the Caldera chain. These smart contracts are crucial for ensuring the integrity and security of each transaction. Using Ethers , we obtain private keys from Convex to broadcast transactions from clients' accounts on the Caldera chain. Challenges we ran into 🌃 One of the main technical challenges we faced was managing the complexity of integrating multiple components, including iOS for the frontend, express.js and ethers.js for the backend, and on-chain technology for the blockchain functionality. Coordinating these distinct areas required careful planning and collaboration among team members specialized in each domain. Additionally, understanding user needs and behaviors presented another hurdle. To address this, we conducted market validation surveys, interviewing over 10 individuals. This effort helped us segment our target market—college students—more effectively, allowing us to tailor EstiMate to better meet their preferences and betting habits. What we learned 📝 While developing EstiMate, we learned the critical importance of adopting a user-centered approach. Transforming a traditional, pen-and-paper practice into a digital social application highlighted the need to understand and prioritize user needs and behaviors — ensuring the app's design and functionality are both intuitive and engaging. Additionally, given the diverse technological backgrounds of our team members and the variety of APIs and development environments we utilized, meshing these different elements helped to hone both our technical and teamwork skills. What's next? 🚀 Looking ahead, we plan to expand EstiMate's capabilities by supporting multichain blockchain technology. We aim to transform the platform into a public marketplace for campus and institution-wide betting, allowing us to leverage tokenomics within the app. Additionally, our next steps include evaluating partnerships with campus organizations like SideChat and Fizz to enhance the social aspect of creating and sharing bets. <div