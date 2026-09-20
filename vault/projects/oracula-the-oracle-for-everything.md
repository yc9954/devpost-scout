---
slug: "oracula-the-oracle-for-everything"
url: "https://devpost.com/software/oracula-the-oracle-for-everything"
title: "Oracula - The Oracle for Everything"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 672
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Oracula - The Oracle for Everything

> Our oracle allows anyone to ask any binary question, and get a result on-chain in a reliable way. This is achieved by utilizing game theoretic concepts, together with the power of a distributed token.

[Devpost](https://devpost.com/software/oracula-the-oracle-for-everything) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**domain** [[civic_government]] [[finance_payments]] [[legal_justice]]
**substrate** [[code_repository]] [[web_dom]]

**stack** next.js, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for oracula - the oracle for everything

## Body

Inspiration Oracles like ChainLink and WinkLink are great at providing financial data, such as the price of BTC at a given time. However, they are not good at providing answers to questions such as "Did England win the Fifa World Cup 2022?". We wanted to create something that can any answer any binary question (which in theory means every question, not just binary). This is why we created Oracula, an optimistic oracle. With a functioning optimistic oracle, tons of applications can be built on top of it such as prediction markets, insurance products, lending markets and much more. What it does Oracula is what's called an optimistic oracle . The optimistic part comes from the fact that when an answer is proposed to the blockchain, it is ASSUMED to be true UNLESS it's disputed. Every question start with these 2 steps Question is asked (anyone can ask anything) Answer is proposed (anyone can propose but you need to post a bond of 10 tokens) Now if the answer is correct, then you do nothing and wait until it finalizes (24 hours but customizable). BUT, if you believe that the answer is wrong, you open a dispute . If you open a dispute, you also need to post a bond of 10 tokens. If you are right you'll get them back, otherwise you'll lose them. If an answer is disputed, then the question goes to "the court" where token holders vote. When the token holders vote, Oracula uses a "commit-reveal scheme". It means that you first commit your vote on chain, and later reveal it. When the vote is commited, no one else can see what you voted on. Later in the reveal-phase, you reveal your vote and then everyone can see it. Read more about commit-reveal schemes here https://medium.com/swlh/exploring-commit-reveal-schemes-on-ethereum-c4ff5a777db8 . When the voting period is finished, the smart contract counts the votes and finalizes an answer. If the proposer was correct from the start, he will receive the 10 tokens from his bond back PLUS the 10 tokens from the disputer. If the disputer was proven to be correct, the opposite will happen. This incentivizes "good behaviour". Provide the correct answer, you earn money. Provide the wrong answer, you lose money. The question is visualized in the diagram below: How we built it We first designed interface for the oracle that you can find here: https://github.com/laplacesdemon420/oracula/blob/main/contracts/src/interfaces/OOInterface.sol . When that was done we started to work on the UI with mock data. Finally, we the UI finished we implemented that actual oracle contract, and you can take a look at it here https://github.com/laplacesdemon420/oracula/blob/main/contracts/src/OptimisticOracle.sol . To name more technical details, the frontend is next.js and the contract are of course in solidity. Check the github for more details. Challenges we ran into How to get around the fact that votes can turn into "Keynesian beauty contests", which mean votes where everyone just votes on what's popular. The solution to this is commit-reveal voting, where the votes are private until the voting period is closed. Another challenge was how we should hash questions and give them id, and we arrived to the conclusion to do hash(question, resolutionSource, date). That enforces uniqueness across all questions, and the hash is the questionId. Accomplishments that we're proud of That the app actually works! You can ask a question, you can propose answers, you can open disputes, you can vote and you can finalize answers! We are most proud of the oracle contract, and especially the voting part with the commit-reveal scheme. It's necessary to keep votes private until they can't be changed, so that everyone thinks for themselves and doesn't just vote the same as the other voters. What we learned I learnt some cryptography when implementing the commit-reveal scheme for voting. It's really cool how you can use it to hide information on a public blockchain. What's next for Oracula - The Oracle for Everything Develop an API Make it possible to ask non-binary questions from the website Come up with a system that rewards voters <div