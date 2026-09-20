---
slug: "rose-derby"
url: "https://devpost.com/software/rose-derby"
title: "Rose Derby"
hackathon: "Privacy4Web3 Hackathon"
organization: "Oasis Foundation"
winner: true
words: 713
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/privacy_tech"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "substrate/financial_record"
---

# Rose Derby

> A Web3 horse betting game with incentivized participation that utilizes Sapphire RNG and selective privacy of participants.

[Devpost](https://devpost.com/software/rose-derby) · hackathon [[Privacy4Web3 Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[privacy_tech]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[legal_justice]]
**substrate** [[financial_record]]

**stack** hardhat, netlify, oasis, sapphire, solidity, sveltekit, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for rose derby

## Body

Race list Create a race Bet on a race Determine results Inspiration I was excited to see all the new documentation and activity on Sapphire and after having enjoyed building my first dapp on it , I wanted to try something a bit more difficult that made use of Sapphire RNG. What it does It's a horse betting "game", similar to real-world horse betting, except with simulated races using Sapphire RNG to determine the race results. What makes it interesting is that the participants are all completely private but the statistics and game activity is public, so it's obvious people are playing (and winning), but no one knows who is playing. Players are incentivized to schedule and find participants for races by setting a % organizer "take" which awards them a percentage of the total betting pool on a race. Then once the betting window has ended, players are then further incentivized to call the "determine race results" function to compute the results with Sapphire RNG and receive an additional percentage of the pool. I believe this project would be a great starter project for more serious web3 on-chain gaming or even for casinos. How I built it I started with the hardhat boilerplate project with typescript so I could have a baseline to work from, then completed the main contract and got it unit tested. Once that was done, I moved to the UI with SvelteKit (Svelte is amazing). I tried to model the UI off typical web3 style dapps combined with sports betting sites that highlight current statistics. Challenges I ran into It was tricky at first trying to come up with a way to schedule races and then determine the results. At first I thought I'd have a bot that schedules them daily and determines the results, but that would have to come out of my own pocket. Then I came up with a way to incentivize players to do it instead. Since players would be the ones scheduling races and determining results, I had to write the contract in a way that wasn't too gas heavy. You should do that anyway, but it did affect many of my decisions and storage and computation. It was also tricky at first to come up with unit tests considering the private nature of Oasis. In the end I opted for using test overrides of internal accessors so I could test on hardhat network. I also used a deterministic override for testing the functions that use RNG so that my test expectations could be fixed. Finally, I wanted to simulate more of the betting types that real horse races allow (win bets, place bets, and show bets) but after analyzing how much additional complexity it would add and considering the hackathon deadline, I settled for only allowing win bets. Accomplishments that I'm proud of It's nostalgic using old algorithms you learned way back when. The race results algorithm takes 5 bytes of Sapphire RNG, converts them to integers bounded to 0-4 and then uses them to perform a random shuffle of the horses to find their final race positions. What I learned The effortlessness of getting end-to-end encryption and selective privacy with Sapphire and the sapphire wrap sdk is very inspiring and has me excited about what else I can build that would normally take way longer and be less open with web2 alternatives. Also, after I initially submitted my entry, @dotandat from the Oasis Core team pointed out that a malicious contract could call the results transaction and revert/retry it if it didn't go their way. I hadn't even considered other contracts using it, let alone the various gotchas related to that. I fixed it and I'm very grateful they pointed that out so I know to think about those kinds of things in the future. Sapphire's documentation has improved since the last time I used it. What's next for Rose Derby I was nervous about submitting a dapp that could be considered "gambling", so I'm not sure what is next for that same reason considering the legal implications. However I hope that others will use this project as a starting point. I may not grow the project further but I will certainly reference it for my next projects on Sapphire. <div