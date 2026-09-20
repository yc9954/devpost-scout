---
slug: "tracker-link"
url: "https://devpost.com/software/tracker-link"
title: "Tweet.Win"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 756
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "user/small_business"
  - "substrate/code_repository"
---

# Tweet.Win

> Never trust some giveaway tweet anymore! Our giveaways are cryptographically fair . Creating a tweet giveaway is under 1 dollar! Only scammers don't pay that ;)

[Devpost](https://devpost.com/software/tracker-link) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[deterministic_policy]]
**user** [[small_business]]
**substrate** [[code_repository]]

**stack** chainlink, filecoin, foundry, polygon, react, redis, remix, solidity, typescript, upstash, web3storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tweet.win

## Body

Homepage Onboarding if Twitter account and Web3 wallet are not linked Dashboard after linking Twitter account and Web3 wallet Easy to create a giveaway Job on the chainlink node mumbai testnet Giveaway update screen Inspiration First idea was when I talked with a webshop owner that wanted a new referral program. He was interested in decentralised crypto systems and was curious if I could create such a system for him based on stable-coins. I saw this hackathon and thought a crypto referral system is something I definitely needed Chainlink for so that was fortunate! Unfortunately the webshop owner pulled out after the whole FTX fiasco... He said crypto isn't trustworthy for most people anymore and crypto should clean up their act. I agree with him and didn't leave the referral systems alone, but I did a pivot. Crypto Twitter is a mess with all the promises for potential prizes if you retweet a certain tweet, but we can't check if the promises from that party were fulfilled. I will fix that with Tweet.Win! (The scam bots are still a thing that Elon needs to fix though :P) What it does Tweet.Win let you create a beautiful giveaway tweet that is trustless, so people can retweet it without trusting you and know they have a chance for an actual prize and not a promise they cannot check. The Retweeter only have to sign a message to link their twitter user id to their Web3 wallet, so no risk there. How we built it We use Chainlink ANY API in our foundry smart contract repo, but also Filecoin Web3 storage for uploading the snapshot we take just before we pick the winners. For the Web2 tech I'm using Vercel/Remix and Upstash for a serverless stack that won't need much attention. Challenges we ran into I spent a lot of time on Polygon ID (really innovative and love that we still care about privacy in the blockchain world) for the first hackathon idea I had. There were certain challenges with figuring out what would work the best and how to circumvent the limited amount of attributes in a schema. I'm also very terrified for writing solidity code from a security point of view (so probably were bit too restrictive, only tokens sent is public but all other functions are gated by onlyOwner or the Chainlink API fullFill request). Slither helps a bit and foundry fuzzing tests as well. The real challenge was the Twitter API and figuring out how to get a secure trustless approach that people can verify from. The Twitter API has some weird pagination approach to get all retweets (so let's say max 100 is not max 100 returns even if there are more retweets). This makes it necessary to check always the previous pagination before going to the latest because you could miss retweeters in the first call. Getting all the data into a solidity contract was quite difficult to find a suiting solution, so we are doing it differently. The Chainlink Any API call in combination with storing the participants off-chain with cryptographically seed is really the key. We have committed the retweeters already on IPFS with a certain hash, timestamp and a big cryptographically random number. After that the Chainlink Any API call we send in the block.timestamp as well to the API and it will return deterministically the winner so other people can verify if it is the real winner. The winner should always be the same if somebody checks the IPFS file and runs the same code and we emit events where we announce the winner and giveaway on chain so people can check it themselves all the time. Also there is something weird with Chainlink Any API where it doesn't get fulfilled on testnet with a created chainlink node on naas.link (also saw some Github issues about never fulfilled requests on Polygon). After the hackathon I will contact someone from the Chainlink team to figure out what is wrong (probably I'm doing something wrong or did forget something). Accomplishments that we're proud of A clear and simple product standing on the tech of giants like Chainlink, Polygon and Filecoin. Also something that is ready for production after a smart contract audit! What we learned How to tackle a scam problem and make it trustless! What's next for Tweet.Win Features like allowlist of legit ERC-20 tokens, NFT's but also features like custom Twitter thumbnail (with Satori), analytics and mails how the giveaway is going but also to notify the winner. <div