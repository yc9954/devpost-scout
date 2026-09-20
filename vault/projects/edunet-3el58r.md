---
slug: "edunet-3el58r"
url: "https://devpost.com/software/edunet-3el58r"
title: "EduNet"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 425
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
---

# EduNet

> Teaching and Learning get easy and fun

[Devpost](https://devpost.com/software/edunet-3el58r) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[education]]
**user** [[educator_student]]

**stack** ipfs, javascript, livepeer, react, solidity, superfluid, web3storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for edunet

## Body

Inspiration Many times we see users want to watch only a certain part of the course but they have to buy the complete course to watch that part. They either buy the complete course which costs them a lot or they buy a course and claim a refund after one month which is not justified for the creator. So now it’s a win-win situation for both users and content creators. Rewards are always a great way to appreciate people for their hard work and strive them to achieve more. A person who feels appreciated will always do more than what is expected. So we are rewarding them with dynamic NFT What it does Content creators can upload courses or Livestream their courses using live peer API. Based on how much course users watch the money will be sent to the creator. Let’s say the course is worth 5000 INR and the total watch hours are 1 hour (3600 second) so 1-second cost is 1.38888888889 Rs. Money will stream per second to the creator depending on users watch time. Once the money is deducted for that time it will not be deducted again if the user watches that part again. If the user watches the course for only 30 minutes then the user needs to pay only 1.38888888889*1800=2500. Rewards are always a great way to appreciate people for their hard work and strive them to achieve more. After every video lesson, you will receive a quiz starting from beginner to advance level. Depending upon your performance and level of competition you will be awarded dynamic nft. Each level has its own NFT as you reach to next level your NFT will upgrade. How we built it We use lens protocol as a social graph layer. All the profile creation and video posting work is done through lens protocol. There is a collect module too to monetize content creators by allowing their followers to purchase the content. We have used chainlink logic-based trigger automation to award the dynamic reward to students. Challenges we ran into We faced some issues integrating lens protocol, and some modules are not working properly but we solved them later. Accomplishments that we're proud of We have built most of the UI using the Lens protocol and integrated live peer successfully. What we learned We learnt about automation of smart based on certain conditions using chainlink, use lens protocol various modules, livepeer and storing data on web3 storage. What's next for EduNet Superfluid part is not completed yet. We integrate it completely. <div