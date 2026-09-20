---
slug: "pymatic"
url: "https://devpost.com/software/pymatic"
title: "Pymatic"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 516
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
---

# Pymatic

> Python port of matic.js

[Devpost](https://devpost.com/software/pymatic) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[developer_tools]]

**stack** python, web3.py

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pymatic

## Body

We're on PyPi! Actions: yes, cross-chain is SLOW! Code stats We're on ReadTheDocs! Inspiration Looking through available Polygon infrastructure, it is easy to notice that almost everything is built with JavaScript or even TypeScript. I hate this language for numerous reasons, so I wanted to develop SDK in Python for those who don't want to write JS/TS code like me. What it does It is almost exact port of well-known matic.js library. It includes also web3 client implementation from maticjs-web3 and plasma bridge from maticjs-plasma. How we built it I was going to work hard on this project at the end of July, when I was notified that deadline is moved for almost a month and felt relaxed. It demotivated me completely, so most of this project was built during last 10 days. Challenges we ran into There is no ethers.js direct python port, so I had to search for alternative libraries that provide similar functionality. This was the initial issue I mentioned here, and it was the most simple one: web3.py provides excellent interface and works as a drop-in replacement. The absence of good Merkle-Patricia trie python implementation was more troublesome. I ended up partially reworking existing project to add required functionality and resolve dependency conflicts. So, after the end of this contest I have two PyPi packages! https://pypi.org/project/merkle-patricia-trie/ . However, perhaps the most challenging in development of this library was testing difficulty. Mining is fast enough to allow for on-chain tests running, but inter-chain transfers (which are the core of library - POS bridge) are annoyingly slow. Goerli/Mumbai transfer takes approx. 10 minutes, which is not very bad. Mumbai/Goerli transfer waits for checkpoint event for 40-80 minutes, and this is way too much. Finally, some minor bugs in original implementation (will be reported later) made it harder to port the library. And Plasma bridge for ERC721 withdrawal does not work at all - neither in library nor via direct contracts interaction. Accomplishments that we're proud of This may not look like a real accomplishment, but the thing I'm most proud of here is that I went through difficult initial understanding process. I struggled for a few days trying to understand how this works: first - how to obtain the tokens and why I keep getting "insufficient balance", then - resolving a bunch if problems I had personally nothing to do: RPC issues and misconfigured contract addresses. What we learned I learned in detail how do POS and plasma bridges work and how does cross-chain interaction happen. What's next for Pymatic I think that the primary concern is better test coverage and more on-chain tests. They take eternity to complete, but are the only way to confirm that everything works in real scenarios. matic.js lacks tests badly, so they have to be properly (re)designed and implemented. Second, but not less important, direction is improving the documentation: current is outdated sometimes and contains cruel mistakes . Perhaps merging our steps with matic.js documentation and maintaining singlee good documentation base with language toggle is a way to go. Also we should port @maticnetwork/maticjs-staking just for completeness. <div