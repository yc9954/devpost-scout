---
slug: "card-club-qtj1d0"
url: "https://devpost.com/software/card-club-qtj1d0"
title: "Card.Club"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 719
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/education"
  - "domain/security_privacy"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Card.Club

> AI generated flashcards with cryptographically proven analytics.

[Devpost](https://devpost.com/software/card-club-qtj1d0) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[education]] [[security_privacy]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[code_repository]] [[structured_db]]

**stack** chainlink, hardhat, rust, solidity, svelte, typescript

## How they structured the write-up

- why i built card.club
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for card.club
- sxt issues i raised

## Body

Homepage Flashcard example Why I built Card.Club This time I wanted to create my own platform, because last time I tried to built a smart contract product based on giveaway Tweets and they increased API prices to 5k or 42k per month (plans I needed for my product unfortunately). Also a well known web2 company specialised in memorising tools/flashcards used my (and other users) data to paywall other students/people, while it was a freemium model before (ads or pay for seeing no ads). This will create an extra barrier for students with a low-income. With the current AI improvements of ChatGPT and other LLM's I immediately knew I would like to generate/finetune my own flashcards and want to build a platform that rewards the creators as well without charging students. To make this platform free for people that want to learn it requires to cover the maintenance costs and reward creators that produce excellent flashcard decks for the platform. I dislike putting advertisements solutions on there (and from work experience I know how shady those advertisement solutions are). With Chainlink Functions/SpaceAndTime I thought let's build my own web3 cryptographically verified analytics which guarantees honest advertising. What it does You can choose a flashcard deck and learn or generate your own. The platform let anyone buy advertising on the end of the flashcard deck on-chain. How we built it Used Sveltekit for the frontend/backend, with Upstash as database (managed Redis) hosted with Cloudflare pages. The SpaceAndTime CLI tool is built in Rust Chainlink Functions <-> Hardhat repository Challenges we ran into Exposing Chainlink Functions solidity function to everyone really required some interesting solutions (source hash to prevent secret phishing scripts, make the solidity function/Chainlink function publicly callable and let users pay for it themselves, refund policy when there is no ad space left). You can read more about it in the smart contract repository: https://github.com/card-club/advertising-evm-contract Rust CLI tool wasn't easy to create (struggled with SxT biscuits and Rust of course). Also to prevent Chainlink Function timeouts (3 seconds) when doing SxT queries I had a proxy caching endpoint and retry policy to combat this. Pronounce the letter S in the presentation :P. I have a lisp and tried to rewrite the presentation to have as few as possible words with S in it. Practiced on the word flashcard deck a lot Accomplishments that we're proud of Documented what to think about when you expose Chainlink Functions to be callable by outsiders. Really liked the experience creating my first scaffolding Rust CLI tool. Retry policy for Chainlink function and caching proxy endpoint solution. AI flashcard generator What we learned Chainlink functions, biscuits, SpaceAndTime and some Rust, finetuning ChatGPT prompts What's next for Card.club Finetune the experience for generate/editing flashcard decks and probably use other models than ChatGPT (really interested in the open-source models like Falcon). Also really interested in Chainlink functions and the changes that will be implemented during the beta. Have some ideas about simplifying the functions starter kit as well. The Chainlink Functions team can reach out to me if they want :) For the SpaceAndTime CLI tool I stripped a lot of commands during a refactor, but curious if there is an interest to let me extend the tool again with stats command and have a load function that uses a kafka producer. Hopefully going from proof of concept towards a real platform after the two products (Chainlink functions and SpaceAndTime) are out of beta. Also really like the Flow blockchain onboarding mechanism (secure managed wallets that work on social oAuth) and it is cheap enough to put the flashcards on chain, however because of the lack of Chainlink integrations I skipped that (and didn't had the time to figure out Chainlink Functions, Space and time and build a frontend but also learn Cadence from scratch) SxT issues I raised https://github.com/SxT-Community/python-api-examples/issues/1 https://github.com/SxT-Community/chainlink-hackathon/issues/5 Feedback: I really would try to built a professional CLI tool that saves keypairs and biscuits safely and make it easy to work with. Similar to the AWS CLI or even a better version that encrypts the values with a pw like the Chainlink env-enc package PS: To the judges, I will keep working on the frontend, but I will leave the smart contract code and CLI code untouched so it can be judged fairly <div