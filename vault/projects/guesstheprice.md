---
slug: "guesstheprice"
url: "https://devpost.com/software/guesstheprice"
title: "GuessThePrice"
hackathon: "TRON Grand Hackathon - HackaTRON Season 6"
organization: "TRON DAO"
winner: true
words: 729
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "substrate/code_repository"
---

# GuessThePrice

> Decentralized platform for forecasting asset prices on BitTorrent Chain

[Devpost](https://devpost.com/software/guesstheprice) · hackathon [[TRON Grand Hackathon - HackaTRON Season 6]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**substrate** [[code_repository]]

**stack** api, bandchain, ether, openzeppelin, react, solidity, typescript

## How they structured the write-up

- project goal
- what it does
- how we built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for guesstheprice

## Body

Project goal Our project aims to create a groundbreaking decentralized application (dApp) on BitTorrent Chain that revolutionizes the way individuals engage with financial forecasting. What it does Using “GuessThePrice” platform, users have the opportunity to: Make new price forecasts for various assets; Trade in P2P mode already created positions / forecasts by other users on the market; By allowing users to select the asset, pledge amount, target date and time, exercise price, and side (OVER or UNDER) with corresponding odds, our dApp provides a comprehensive and customizable forecasting experience. By leveraging blockchain technology, “GuessThePrice” ensures a transparent, secure, and trustless environment for financial forecasting. How we built it Our project utilizes a cutting-edge technology stack, including: React, TypeScript: the dApp frontend features a user-friendly interface, ensuring a seamless and intuitive user experience. EthersJS: facilitates interactions with the blockchain, allowing users to connect their wallets and interacting with the decentralized platform. Solidity / Smart contracts: the contracts manage ERC721 tokens for forecast positions and handle the creation, trading, and settlement of forecast positions, ensuring a fair and transparent process. Blockchain integrations: OpenZeppelin contracts: The use of ERC721 tokens for each forecast position guarantees unique ownership and transferability, providing users with a tangible stake in their predictions. Band Protocol Price Feeds: Integration with a decentralized oracle ensures that price data is accurate and tamper-proof, enhancing the credibility and reliability of our forecasts. BandChain's role as an Oracle instills confidence in the reliability and precision of the data it provides. By tapping into BandChain's robust infrastructure, we ensure that the financial data powering our forecasts is not only real-time but also highly precise, enabling users to make informed decisions with complete assurance. This integration underscores the commitment to elevating the standard of accuracy within decentralized finance, reinforcing our platform's credibility and enhancing user trust. … and more soon Our platform integrates CRON tasks : In our backend, each asset is assigned a singular wallet relayer responsible for monitoring forecast expiration. When the exercise time of a forecast arrives, the relayer marks it as expired and fetches the asset price from BandChain. This fetched price is securely updated in smart contracts, guaranteeing accurate price at the exercise time. Challenges I ran into Notable challenges: Designing and implementing the intricate logic of the smart contracts. Creating these contracts required meticulous attention to detail to ensure they effectively managed ERC721 tokens for forecast positions. Integrating the price data from BandChain's decentralized oracle into my smart contracts posed a distinct challenge. Overcoming this challenge not only strengthened my understanding of blockchain integration but also highlighted the importance of reliable data sources in decentralized applications. Accomplishments that I'm proud of Firstly, I am immensely proud of the accomplishment of designing and implementing the entire logic of the smart contracts for "GuessThePrice". Additionally, the integration with a decentralized Oracle/Data provider such as BandChain demonstrates my commitment to guaranteeing the utmost accuracy and trustworthiness of our platform's financial forecasting capabilities. Furthermore, the creation of a user-friendly frontend interface underscores my dedication to ensuring accessibility and seamless interaction, making financial forecasting on the blockchain both intuitive and engaging. Overall, these accomplishments reflect my dedication, expertise, and innovative spirit in revolutionizing the landscape of decentralized finance (DeFi) through "GuessThePrice." What I learned Despite these challenges, the journey of overcoming them has been immensely rewarding. It has deepened my expertise in smart contract development and blockchain integration. Through the development and deployment of "GuessThePrice" platform, I gained invaluable experience into integrating blockchain technology with real-world data and APIs (in this case with an decentralized oracle platform that aggregates price feeds), ensuring transparency and reliability in financial forecasting. What's next for GuessThePrice [🟢 DONE 🟢] 🟢Creating the frontend 🟢Smart contracts deployment on BitTorrent Chain Testnet 🟢Integration with Coingecko API 🟢Integration with BandChain Price Feeds 🟢Create on the backend CRON jobs for relayers 🟢Optimize smart contracts for efficiency and user experience [🟡 May 8 - May 20 🟡] 🟡Add support for more assets/markets 🟡Add the option to make price forecasts not only with native coins, but also with ERC20 tokens [🟡 May 21 - May 31🟡] 🟡Deploy smart contracts and launch on BitTorrent Chain Mainnet 🟡Increase the plan of Coingecko API to avoid rate limits and ensure uninterrupted access to price data or explore alternative providers 🟡Continuously enhance the UI / UX for all devices, conduct thorough testing to ensure functionality and security <div