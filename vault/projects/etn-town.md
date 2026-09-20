---
slug: "etn-town"
url: "https://devpost.com/software/etn-town"
title: "ETN Town"
hackathon: "Electroneum Hackathon 2025"
organization: "Electroneum"
winner: true
words: 1267
team_size: 0
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ETN Town

> Welcome to ETN Town, where blockchain meets innovation! Get ready to experience seamless transactions, rewards, and gameplay like never before

[Devpost](https://devpost.com/software/etn-town) · hackathon [[Electroneum Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[security_privacy]]
**user** [[legal_professional]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** ankr, css3, electroneum, javascript, mysql, node.js, php

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned?
- what's next?

## Body

Lnading page of the awesome application (not allowing non ETN testnet chain) With just a click, player can interact with the project Easter egg showing a fun fact about Electroneum Maze runner game Timer running out in maze runner game (showing error) Reasoning behind a correct triplet in flip the tiles Purchasing a hint Streak section; & users will receive rewards for that Rewards for the weekly top scorer Transaction explorer (in and out transactions) Stats which can be seen by visiting the bottom-right home Inspiration In a world where blockchain technology is often associated with just trading and investments, I wanted to redefine its potential by merging education, gaming, and rewards. Electroneum (ETN) has built a strong foundation for easy and accessible crypto transactions, so why not use it for an interactive, knowledge-driven experience? Our inspiration was simple: Make learning engaging, rewarding, and decentralized . Traditional educational platforms lack excitement, while most blockchain games focus only on financial incentives. With ETN Town, we bridge this gap, creating an ecosystem where players enhance their knowledge, improve their logical reasoning, and get rewarded for it . By integrating Electroneum's blockchain into a gamified learning experience, we’re not just building another dApp—we're crafting an ecosystem that simultaneously empowers users with knowledge and cryptocurrency . What it does ETN Town is an innovative gaming platform that leverages the Electroneum blockchain to make learning fun and rewarding. It consists of four distinct games that test players' problem-solving abilities, memory, and knowledge across various domains: 🌀 Maze Runner: Find the correct path in a time-based maze challenge before time runs out. 🎭 Flip the Tiles: Match triplets of text and image cards related to topics like Operating Systems, DBMS, JavaScript, and Electroneum. Each correct match provides a detailed explanation along with a resource link for further learning. Players can purchase hints using ETN via the Metamask extension for a smoother experience. 🎥 Video Q&A: Watch blockchain-hosted educational videos and answer multiple-choice questions within a limited time. With 9 videos covering different topics (history, technology, education) , this mode ensures learning beyond just gaming. 🔤 Alpha Quest: A digital version of "Name, Place, Animal, Thing." Each day, four random letters are assigned, and players must fill in the blanks based on category hints. A fun way to boost creativity and word association skills! 🔹 Additional Features: 1️⃣ Login Streak Rewards: Players who maintain a streak of 3 or more days earn extra ETN for completing levels, while those having a streak of 1 and 2 days will also get some login bonus. 2️⃣ Weekly Leaderboard: The top scorer of the week is rewarded with ETN, keeping the competition alive. 3️⃣ Background Music Store: Players can purchase custom music tracks to personalize their experience—only the first track is free! 4️⃣ Privileged Judge Mode: For event judges, a wallet-free experience lets them explore all features effortlessly. Do note that this is just for hackathon purposes so that every user, even without the wallet, could play the games It would be removed in the later version so that you have to use the ETN chain to interact with this project. ETN Town is not just a game—it’s a gateway to knowledge and blockchain adoption . ETN Who pays whom? Reason 0.000005 Player spends Buying the drive music track 0.0000075 " " Buying the wallpaper music track 0.00001 " " Buying the flupping duck music track 0.0000125 " " Buying the powerful trap music track 0.000015 " " Buying the dark passenger music track 0.000005 " " Getting the hints for flip the tiles game 0.000015 Players gets reward Maintaing a login streak of 1 day 0.000017 Players gets reward Maintaing a login streak of 2 days 0.000019 Players gets reward Maintaing a login streak of 3+ days Varying ETN Players gets reward For becoming the weekly top scorer Note: I have used a small amount of ETN to be transferred because this project is on mainnet, and every token costed me real money How I built it Bringing ETN Town to life required integrating multiple technologies while ensuring seamless blockchain transactions. Here's how we built it: 🔹 Frontend: Developed using JavaScript, HTML, and CSS for a smooth and interactive UI. Game logic and UI built with React.js for efficient rendering and responsiveness. 🔹 Backend: Node.js & Express.js server to handle transactions, user authentication, and game logic. ANKR API is used for blockchain interactions like sending ETN rewards and validating transactions. MySQL database to store user data, scores, transaction logs, and streaks. 🔹 Blockchain Integration: 🅰️ Metamask integration allows users to connect their ETN Mainnet wallet to make transactions for hints, rewards, and music purchases. 🅱️ Privileged Mode bypasses wallet requirements for event judges, enabling them to experience the project without blockchain limitations. ©️ CRON jobs automate weekly leaderboard rewards, ensuring fairness and consistency. Bringing all these elements together resulted in a fully functional and engaging blockchain-powered learning ecosystem. Challenges I ran into Every great project faces roadblocks, and ETN Town was no exception. Some of the key challenges I overcame: ⚠️ Blockchain Transactions & Gas Fees: Ensuring fast and cost-efficient ETN transactions required deep research into ANKR API optimization. ⚠️ Dynamic Game Logic: Implementing real-time streak tracking, leaderboard updates, and hint purchases required meticulous backend development. ⚠️Metamask Integration Issues: Ensuring smooth Metamask-based transactions across all browsers was challenging, as some users faced UI blocking issues. ⚠️Privileged Mode Implementation: Creating a judge-specific mode without compromising security and blockchain integrity needed careful backend modifications. ⚠️ Ensuring Decentralized Video Hosting: Storing video Q&A content on blockchain rather than centralized servers was a new challenge, but we made it work! Through persistence and problem-solving, we tackled every obstacle and built a robust, user-friendly platform. Accomplishments That I Am Proud Of ✅ Successfully integrating ETN blockchain into a fully functional gaming ecosystem. ✅ Creating a seamless experience for both blockchain and non-blockchain users via Judge Mode. ✅ Implementing real-world crypto transactions where players can buy, earn, and interact using ETN. ✅ Building a gamified learning system that enhances user knowledge while making crypto adoption fun. ✅ Automate weekly rewards with a CRON job to ensure fair distribution of ETN incentives. ✅ Creating a scalable and adaptable platform that can integrate more games and blockchain utilities in the future. The journey was tough, but the results? Worth it! What I Learned? 📌 Deep Understanding of Blockchain Transactions: From gas fees to smart contract interactions, I gained hands-on experience with ETN blockchain and ANKR API. 📌 Optimizing Game Logic for Seamless Experience: Handling real-time updates, scoring mechanisms, and dynamic transactions made me more proficient in game development. 📌 Enhancing User Experience in Crypto-Based Apps: I learned how to bridge the gap between Web 2 and Web 3, making blockchain adoption easy for new users. 📌 Security & Fraud Prevention: Implementing wallet-based restrictions and avoiding double-spending exploits helped me grasp crypto security best practices. 📌 The Power of Persistence: Every challenge—whether it was transaction errors, UI bugs, or server issues—taught me that persistence and debugging lead to breakthroughs. ETN Town has been a transformational learning experience that pushed my skills to the next level. What's Next? 🚀 NFT-Based Achievements: Players can unlock NFT badges based on their gameplay progress, which can be traded or displayed on their profile. 🚀 On-Chain Leaderboard & Smart Contracts: Moving the leaderboard & reward system fully on-chain to make it completely decentralized. 🚀 Mobile App Launch: Optimizing ETN Town for mobile gaming with PWA support and Metamask mobile integration. The journey has just begun. ETN Town is not just a project—it’s the future of blockchain-based gamified learning . <div