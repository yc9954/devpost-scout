---
slug: "riveth"
url: "https://devpost.com/software/riveth"
title: "RivETH"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 773
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# RivETH

> A local Ethereum smart contract development toolkit that runs in the browser.

[Devpost](https://devpost.com/software/riveth) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]] [[geospatial]] [[web_dom]]

**stack** bash, css, html, javascript, node.js, solidity

## How they structured the write-up

- inspiration
- what it does
- latest features
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for riveth

## Body

Interact with smart contracts RivETH UI Default hardhat accounts Terminal logs Load and deploy contracts Explorer - RivETHScan Transaction data decoder Inspiration I built RivETH as a result of my limitations when I started learning more about Smart Contracts. My development environment was Visual Studio Code with associated extensions, it was enough for what I did at the time. In the long run, I wanted to start learning foundry, a popular solidity development and testing framework, I realized I could not install it on my computer, I resorted to using foundry through the Google Cloud Shell Editor. After a while, I found out that unlike most other software development workflows, most smart contract developers do not have a way to 'visually' interact with their contracts. Remix was a tool I used to that effect but I could not install it on my laptop too. This was what drove me to build a tool I could use to visualize and interact with smart contracts. What it does RivETH allows developers to visualize and interact with smart contracts directly in the browser, just like you would with a conventional application. It grabs compiled artifacts (ABI and bytecode) from its project folder and generates a UI that the developer can interact with in the browser. Some of its popular features are: Call contract functions with the click of a button. 20 pre-funded default accounts which you can switch between with a drop-down. Transaction logs in the browser and terminal, useful for debugging. Open multiple RivETH tabs in cases of cross-contract calls. ETH converter to convert between ETH and WEI Latest Features A local explorer feature that listens for transactions on the contract, the explorer can be opened in a new tab, and it will be populated when ever a transaction is called on the contract. Injected provider: Devs can connect web3 wallets and use them to test contract deployment and interactions. Workflows: Devs can write workflow files to automate smart contract deployment and interactions. Updated UI with colour codes for the buttons. Blue -> View/Pure functions; Red -> Payable; Orange -> State-changing functions. Keyboard shortcuts for easy access to repetitive tasks. The shortcuts can be assessed from the RivETH dashboard by clicking the key [M] How I built it I built RivETH with the holy trinity of HTML, CSS and JavaScript, I also used ethers.js for some web3 functionality (hardhat, solidity compiler). I could have used frontend frameworks but I considered speed, files are served directly from the Live Server extension, no hot module reloads or bundling of any sort, just native, out-of-the-box behaviour. That way, RivETH runs locally once installed, no fussing about network latency, giving the developer a snappy experience. RivETH exposes the default hardhat JSON-RPC URL and allows contracts to interact with it, get accounts and their balances. It uses JavaScript's fetch API to grab a contract's ABI and bytecode, maps the ABI to a user interface that is displayed in the browser. Challenges I ran into Some challenges I ran into while building RivETH include: Parsing function parameter data types like bytes, addresses and arrays, when sending transactions. At the moment, users have to parse them in the UI before sending transactions. Handling fallback and receive functions. Handing constructor arguments. At the moment, there is only a single input field to pass in constructor arguments when deploying contracts in the browser. Arguments are separated with commas. I am currently working on fixing some of these issues in the next release. Accomplishments that I am proud of Looking back on building RivETH, I can be proud of how much I have learnt and built to solve a problem that I was stuck with. I am also proud of the fact that I have built something that could be of help to other developers who might find themselves in my shoes. Also, I am proud of the fact that I could apply my skills in frontend development and web3 to solving a real problem. What I learned Building RivETH taught me that web3 is not only about the users, the developers also need access to good developer experience and top development environments to build secure and trustless systems. I also learnt the art of idea execution: build first, iterate later; and learning by doing and building. By building RivETH, I understand that anything I can imagine is real and can be done. What's next for RivETH I plan to revamp a local block explorer feature in RivETH to allow developers to track transactions and events emitted by contracts. I also plan to add an optional AI feature, that could improve the developer experience. <div