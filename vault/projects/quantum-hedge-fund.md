---
slug: "quantum-hedge-fund"
url: "https://devpost.com/software/quantum-hedge-fund"
title: "Quantum Hedge Fund"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 488
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/transportation"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Quantum Hedge Fund

> Quantum Hedge Fund is an on-chain hedge fund powered by Chainlink that implements advanced fund management strategies by using a quantum algorithm for portfolio diversification.

[Devpost](https://devpost.com/software/quantum-hedge-fund) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[revocation_withdrawal]]
**domain** [[transportation]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[web_dom]]

**stack** chainlink, fastapi, hardhat, nextjs, python, qiskit, solidity, typescript

## How they structured the write-up

- overview
- features
- components
- tech stack
- quantum algorithm
- links
- getting started
- security
- license
- contact
- acknowledgements

## Body

Fund dashboard Architecture diagram part 1 Architecture diagram part 2 Quantum algorithm formula and operations Quantum algorithm optimisation Quantum API Logo Quantum Hedge Fund Overview Quantum Hedge Fund is an on-chain hedge fund powered by Chainlink that implements advanced fund management strategies by using a quantum algorithm for portfolio diversification. This project features smart contracts for managing a cryptocurrency vault, integrating Chainlink oracles for accurate pricing and Quickswap for token exchanges. Features Token Management : Support for a diverse range of cryptocurrencies, enabling dynamic adjustments to the portfolio. Vault Shares : Tokenization of shares in the vault using VaultShareToken . Deposits and Withdrawals : Robust mechanisms for depositing and withdrawing funds. Automated Rebalancing : Portfolio rebalancing executed based on strategies defined in the FundManager contract. Chainlink and Uniswap Integration : Ensures reliable price feeds and efficient liquidity management. Quantum portfolio diversification : unique and advanced fund strategy based on a quantum algorithm Components Chainlink: Datafeed: calculating the total value of the pool Functions: retrieving allocations from the quantum oracle Automation: initiating rebalancing of assets Smart Contracts: Vault Contract : Manages core functions such as deposits, withdrawals, and rebalancing. FundManager Contract : Oversees token weights and handles oracle requests for portfolio management. VaultShareToken Contract : ERC20 token representing a stake in the vault. Quantum Computing API: Send asset prices to the API and choose algorithm to run (quantum or quantum-inspired) Runs quantum algorithm with asset prices Sends optimal selection of assets from quantum algorithm Draws diagram of quantum program and plots optimisation Deployed at URL User Interface: User can deposit funds User can withdraw funds Visual representation of the asset allocations Tech Stack Chainlink Functions: Fetching the asset prices and sending them to the quantum oracle and receiving the results Chainlink Datafeed: Fetching the prices of each asset real-time on the smart contract Chainlink Automation: Rebalancing the allocation of the assets every day Polygon: deployed on Polygon mainnet Quickswap: Exchange for rebalancing the assets Qiskit: Quantum computing software development kit for running the quantum algorithm Quantum Algorithm The algorithm is based on the Qiskit Portfolio Diversification algorithm: https://qiskit.org/ecosystem/finance/tutorials/02_portfolio_diversification.html We modified the algorithm to fit the needs of our quantum hedge fund. Links Technical Links Github: https://github.com/Quantum-Hedge-Funds App: https://quantum-hedge-fund-app.vercel.app/ API: https://api-production-5752.up.railway.app/docs Presentation Links Video demo: https://youtu.be/6QXWxM5b-Pg Presentation: https://bit.ly/quantum-fund-presentation Architecture Diagram: https://bit.ly/quantum-fund-diagram Getting Started Engaging with Quantum Hedge Fund requires familiarity with Solidity, Ethereum blockchain, and smart contract development. Prerequisites Node.js and npm Hardhat Installation Clone the repository: git clone https://github.com/Quantum-Hedge-Funds/smart-contracts.git Install the required packages: npm install Compile the smart contracts with Hardhat: npx hardhat compile Deploy the contracts: npx hardhat run scripts/deploy.ts --network polygonMainnet Testing Run the test suite to ensure everything functions as expected: npx hardhat test Security This project is in the developmental phase. Thoroughly review the code before deploying it in production environments. License This project is licensed under the MIT License. Contact You can contact us at contact@yashgoyal.dev , contact@jessicapointing.com Acknowledgements Chainlink Quickswap OpenZeppelin Qiskit <div